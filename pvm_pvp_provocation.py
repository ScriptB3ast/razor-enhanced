'''
Author: TheWarDoctor95
Other Contributors:
Last Contribution By: TheWarDoctor95 - March 23, 2019

Description: Selects enemies to use the Provocation skill on.
    • Automatically selects an instrument if one is needed
    • Maintains a list of enemies that have been successfully been provo'd together and will ignore enemies that have been provo'd together
        • If one of the enemies that has already been provo'd dies, the script will detect the death and free up the enemy that is still alive to be provo'd again
    • Priority:
        1. Paragons
        2. Enemies in War Mode
        3. Any other enemy
'''

## Script options ##
# Change depending on whether or not you want a more verbose output on what is being provo'd or ignored by the script
showTargets = True

import re
from System.Collections.Generic import List
from Scripts.glossary.items.instruments import FindInstrument
from Scripts.glossary.enemies import GetEnemyNotorieties, GetEnemies
from Scripts.utilities.mobiles import GetEmptyMobileList
from Scripts.utilities.colors import colors
from Scripts import config

enemiesProvodSharedValue = 'enemiesProvod'

def CheckPlayerInDungeon( Player ):
    '''
    Uses the Player's X and Y coordinates to determine if they are in a dungeon
    '''

    if Player.Position.X < 5120:
        # Player is west of the dungeon cutoff
        return False

    if Player.Position.Y < 2305:
        # Player is east of the dungeon cutoff and to the north of the Lost Lands
        return True

    if Player.Position.X > 6140:
        # Player is east of the Lost Lands
        return True

    # Player is in the Lost Lands
    return False

def SelectEnemyToProvo( enemies ):
    '''
    Selects the nearest enemy who isn't provo'd to use Provocation on
    '''

    enemiesAlreadyProvod = None
    enemiesAlreadyProvodCheck = Misc.CheckSharedValue( enemiesProvodSharedValue )
    if enemiesAlreadyProvodCheck:
        enemiesAlreadyProvod = Misc.ReadSharedValue( enemiesProvodSharedValue )

        # Make sure the enemies we provo'd previously are still around
        verifiedEnemiesAlreadyProvod = None
        enemySets = enemiesAlreadyProvod.split( ',' )
        for enemySet in enemySets:
            enemySerials = enemySet.split( '`' )
            bothEnemiesStillExist = True

            for enemySerial in enemySerials:
                enemyMobile = Mobiles.FindBySerial( int( enemySerial ) )
                if enemyMobile == None:
                    bothEnemiesStillExist = False

            if bothEnemiesStillExist and verifiedEnemiesAlreadyProvod == None:
                verifiedEnemiesAlreadyProvod = enemySet
            elif bothEnemiesStillExist:
                verifiedEnemiesAlreadyProvod += ',' + enemySet

        # Update the stored values
        enemiesAlreadyProvod = verifiedEnemiesAlreadyProvod
        if verifiedEnemiesAlreadyProvod == None:
            Misc.RemoveSharedValue( enemiesProvodSharedValue )
        else:
            Misc.SetSharedValue( enemiesProvodSharedValue, verifiedEnemiesAlreadyProvod )

    enemiesNotYetProvod = enemies
    if enemiesAlreadyProvod != None:
        # Remove the enemies we've already provo'd from the list of potential enemies to provo
        enemiesAlreadyProvodSerials = []
        enemySets = enemiesAlreadyProvod.split( ',' )
        for enemySet in enemySets:
            enemySerials = enemySet.split( '`' )
            for enemy in enemySerials:
                enemiesAlreadyProvodSerials.append( int( enemy ) )

        enemiesNotYetProvodPythonList = list( filter( lambda enemy: not ( enemy.Serial in enemiesAlreadyProvodSerials ), enemies ) )

        # We have the Python formatted list, but we need a C# list to pass to Mobiles.Select()
        enemiesNotYetProvodCSharpList = GetEmptyMobileList( Mobiles )
        for enemy in enemiesNotYetProvodPythonList:
            enemiesNotYetProvodCSharpList.Add( enemy )
        enemiesNotYetProvod = enemiesNotYetProvodCSharpList

    # Make sure there are still enemies yet to be provod, if not, use all of the enemies given
    enemiesToProvo = enemiesNotYetProvod
    if len( enemiesToProvo ) == 0:
        enemiesToProvo = enemies

    # Select the enemy to provo
    paragons = [ enemy for enemy in enemiesToProvo if enemy.Color == 1157 ]
    if len( paragons ) > 0:
        paragonMobiles = GetEmptyMobileList( Mobiles )
        for paragon in paragons:
            paragonMobiles.Add( paragon )
        return Mobiles.Select( paragonMobiles, 'Nearest' )

    if not CheckPlayerInDungeon( Player ):
        # Make sure we're pulling enemies attacking and not birds or rabbits
        enemiesInWarMode = [ enemy for enemy in enemiesToProvo if enemy.WarMode ]
        if len( enemiesInWarMode ) > 0:
            warModeMobiles = GetEmptyMobileList( Mobiles )
            for enemyInWarMode in enemiesInWarMode:
                warModeMobiles.Add( enemyInWarMode )
            return Mobiles.Select( warModeMobiles, 'Nearest' )

    return Mobiles.Select( enemiesToProvo, 'Nearest' )


def ProvoEnemies():
    '''
    Identifies enemies that need to be provo'd and uses the Provocation skill on them
    Having this encapsulated in a function makes it possible to use the 'return' keyword
    '''

    global showTargets

    Misc.ClearIgnore()

    provoAttemptCompleted = False

    while not provoAttemptCompleted:
        enemies = GetEnemies( Mobiles, 0, 12, GetEnemyNotorieties(), IgnorePartyMembers = True )

        if enemies == None or len( enemies ) < 2:
            Misc.SendMessage( 'Not enough enemies to provo!', colors[ 'red' ] )
            return
        else:
            # Clear any previously selected target and the target queue
            Target.ClearLastandQueue()

            # Wait for the target to finish clearing
            Misc.Pause( config.targetClearDelayMilliseconds )

            Player.UseSkill( 'Provocation' )

            # Wait for the journal entry to appear
            Misc.Pause( config.journalEntryDelayMilliseconds )

            if Journal.SearchByType( 'You must wait a few moments to use another skill.', 'Regular' ):
                # Something is on cooldown, nothing we can do
                Journal.Clear()
                return
            elif Journal.SearchByType( 'What instrument shall you play?', 'Regular' ):
                instrument = FindInstrument( Player.Backpack )
                if instrument == None:
                    Misc.SendMessage( 'No instrument to provo with!', colors[ 'red' ] )
                    return
                Target.WaitForTarget( 2000, True )
                Target.TargetExecute( instrument )

            Target.WaitForTarget( 2000, True )
            enemyToProvo1 = SelectEnemyToProvo( enemies )
            Target.TargetExecute( enemyToProvo1 )

            # Wait for the journal entry to appear
            Misc.Pause( config.journalEntryDelayMilliseconds )

            if Journal.SearchByType( 'Target cannot be seen', 'Regular' ):
                if showTargets:
                    Mobiles.Message( enemyToProvo1, colors[ 'red' ], 'Target 1 cannot be seen' )
                Misc.IgnoreObject( enemyToProvo1 )
                Journal.Clear()
                provoAttemptCompleted = False
                Misc.Pause( 1000 )
                continue

            # Remove the selected enemy to ensure we don't provo an enemy onto themselves
            enemies.Remove( enemyToProvo1 )

            Target.WaitForTarget( 2000, True )
            enemyToProvo2 = SelectEnemyToProvo( enemies )
            Target.TargetExecute( enemyToProvo2 )

            # Wait for the journal entry to appear
            Misc.Pause( config.journalEntryDelayMilliseconds )

            if Journal.SearchByType( 'Target cannot be seen', 'Regular' ):
                if showTargets:
                    Mobiles.Message( enemyToProvo2, colors[ 'red' ], 'Target 2 cannot be seen' )
                Misc.IgnoreObject( enemyToProvo2 )
                Journal.Clear()
                provoAttemptCompleted = False
                Misc.Pause( 1000 )
                continue

            if showTargets:
                Mobiles.Message( enemyToProvo1, colors[ 'cyan' ], 'Provo Target 1' )
                Mobiles.Message( enemyToProvo2, colors[ 'cyan' ], 'Provo Target 2' )

            # Wait for the journal entry to appear
            Misc.Pause( config.journalEntryDelayMilliseconds )

            if Journal.SearchByType( 'Your music succeeds, as you start a fight.', 'Regular' ):
                Journal.Clear()
                newEntry = '%i`%i' % ( enemyToProvo1.Serial, enemyToProvo2.Serial )
                enemiesAlreadyProvodCheck = Misc.CheckSharedValue( enemiesProvodSharedValue )
                if enemiesAlreadyProvodCheck:
                    enemiesAlreadyProvod = Misc.ReadSharedValue( enemiesProvodSharedValue )
                    Misc.SetSharedValue( enemiesProvodSharedValue, enemiesAlreadyProvod + ',' + newEntry )
                else:
                    Misc.SetSharedValue( enemiesProvodSharedValue, newEntry )
            provoAttemptCompleted = True

# Run ProvoEnemies
ProvoEnemies()
