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

import re
from System.Collections.Generic import List
from Scripts.glossary.items import FindInstrument
from Scripts.glossary.enemies import GetEnemyNotorieties, GetEnemies
from Scripts.utilities.mobiles import GetEmptyMobileList
from Scripts.utilities.colors import colors
from Scripts import config

enemiesProvodSharedValue = 'enemiesProvod'

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
    paragon = next( ( enemy for enemy in enemiesToProvo if enemy.Color == 1157 ), None )
    if paragon != None:
        return paragon

    warMode = next( ( enemy for enemy in enemiesToProvo if enemy.WarMode ), None )
    if warMode != None:
        return warMode

    return Mobiles.Select( enemiesToProvo, 'Nearest' )


def ProvoEnemies():
    '''
    Identifies enemies that need to be provo'd and uses the Provocation skill on them
    Having this encapsulated in a function makes it possible to use the 'return' keyword
    '''
    enemies = GetEnemies( Mobiles, 0, 12, GetEnemyNotorieties(), IgnorePartyMembers = True )

    if enemies == None or len( enemies ) < 2:
        Misc.SendMessage( 'Not enough enemies to provo!', colors[ 'red' ] )
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
        enemyToProvo1 = SelectEnemyToProvo( enemies )
        Target.TargetExecute( enemyToProvo1 )

        # Remove the selected enemy to ensure we don't provo an enemy onto themselves
        enemies.Remove( enemyToProvo1 )

        Target.WaitForTarget( 2000, True )
        enemyToProvo2 = SelectEnemyToProvo( enemies )
        Target.TargetExecute( enemyToProvo2 )

        # Wait for the journal entry to appear
        Misc.Pause( config.journalEntryDelayMilliseconds )

        if Journal.SearchByType( 'Your music succeeds, as you start a fight.', 'Regular' ):
            newEntry = '%i`%i' % ( enemyToProvo1.Serial, enemyToProvo2.Serial )
            enemiesAlreadyProvodCheck = Misc.CheckSharedValue( enemiesProvodSharedValue )
            if enemiesAlreadyProvodCheck:
                enemiesAlreadyProvod = Misc.ReadSharedValue( enemiesProvodSharedValue )
                Misc.SetSharedValue( enemiesProvodSharedValue, enemiesAlreadyProvod + ',' + newEntry )
            else:
                Misc.SetSharedValue( enemiesProvodSharedValue, newEntry )

# Run ProvoEnemies
ProvoEnemies()
