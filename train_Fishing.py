'''
Author: TheWarDoctor95
Other Contributors:
Last Contribution By: TheWarDoctor95 - May 1, 2019

Description: Trains Fishing to its skill cap while on a boat.

Start the script while standing on tile to the south of the boats recall point
'''

# True will move the boat with the 'foward' and 'backword' commands
# False will move the boat with the 'left' and 'right' commands
moveForwardBackward = False

autoFightMacroName = 'cast_EnergyBolt.py'

from Scripts import config
from Scripts.glossary.colors import colors
from Scripts.glossary.items.containers import FindHatch
from Scripts.glossary.items.tools import tools
from Scripts.utilities.items import FindItem
from System.Collections.Generic import List

fishIDs = [ 0x09CF, 0x09CE, 0x09CC, 0x09CD ]

def Fish( fishingPole, x, y ):
    '''
    Casts the fishing pole and returns True while the fish are biting
    '''

    global fishIDs

    Journal.Clear()
    Items.UseItemByID( tools[ 'fishing pole' ].itemID )

    Target.WaitForTarget( 2000, True )

    statics = Statics.GetStaticsTileInfo( x, y, 0 )
    if len( statics ) > 0:
        water = statics[ 0 ]
        Target.TargetExecute( x, y, water.StaticZ, water.StaticID )
    else:
        Target.TargetExecute( x, y, -5, 0x0000 )


    Misc.Pause( config.dragDelayMilliseconds )

    Timer.Create( 'timeout', 20000 )
    while not ( Journal.SearchByType( 'You pull', 'Regular' ) or
            Journal.SearchByType( 'You fish a while, but fail to catch anything.', 'Regular' ) or
            Journal.SearchByType( 'The fish don\'t seem to be biting here', 'Regular' ) or
            Journal.SearchByType( 'Your fishing pole bends as you pull a big fish from the depths!', 'Regular' ) or
            Journal.SearchByType( 'Uh oh! That doesn''t look like a fish!', 'Regular' ) ):
        if not Timer.Check( 'timeout' ):
            return False
        Misc.Pause( 50 )

    if Journal.SearchByType( 'The fish don\'t seem to be biting here', 'Regular' ):
        return False

    if Player.Weight >= Player.MaxWeight:
        for fishID in fishIDs:
            fish = Items.FindByID( fishID, 0x0000, Player.Backpack.Serial )
            if fish != None:
                Items.UseItemByID( 0x0F52 )
                Target.WaitForTarget( 2000, True )
                Target.TargetExecute( fish )
                Misc.Pause( config.dragDelayMilliseconds )

        if Player.Weight > Player.MaxWeight - 10:
            # Throw the fish and shoes into the boat's hatch
            directionsToHatch = [ 'Up', 'Up', 'North', 'North', 'North',
                'East', 'East', 'North', 'North', 'North' ]

            for direction in directionsToHatch:
                Player.Walk( direction )
                Misc.Pause( 1000 )

            hatch = FindHatch( Items )

            rawFishSteaks = Items.FindByID( 0x097A, -1, Player.Backpack.Serial )
            Items.Move( rawFishSteaks, hatch, 0 )
            Misc.Pause( config.dragDelayMilliseconds )

            directionsToMast = [ 'South', 'South', 'South', 'East', 'East',
                'South', 'South', 'South', 'Left', 'Left' ]

            for direction in directionsToHatch:
                Player.Walk( direction )
                Misc.Pause( 1000 )

    return True


def FightEnemy():
    enemy = Target.GetTargetFromList( 'enemy' )
    if enemy != None:
        Misc.ScriptRun( autoFightMacroName )
        while enemy != None:
            Misc.Pause( 100 )
            enemy = Mobiles.FindBySerial( enemy.Serial )
        Player.ChatSay( 0, 'left one' )
        Misc.Pause( 1000 )
        Player.ChatSay( 0, 'right one' )
        Misc.Pause( 1000 )
        Player.ChatSay( 0, 'right one' )
        Misc.Pause( 1000 )

        corpseFilter = Items.Filter()
        corpseFilter.Movable = False
        corpseFilter.Graphics = List[int]( [ 0x2006 ] )
        corpses = Items.ApplyFilter( corpseFilter )
        for corpse in corpses:
            for item in corpse.Contains:
                Items.Move( item, Player.Backpack.Serial, 0 )
                Misc.Pause( config.dragDelayMilliseconds )


def TrainFishing():
    '''
    Trains Fishing to its skill cap
    '''

    global moveForwardBackward

    if Player.GetSkillValue( 'Fishing' ) == Player.GetSkillCap( 'Fishing' ):
        Player.HeadMessage( colors[ 'green' ], 'Your Fishing is already at its skill cap!' )
        return

    fishingPoleTool = tools[ 'fishing pole' ]
    fishingPole = FindItem( fishingPoleTool.itemID, Player.Backpack )

    Misc.SendMessage( 'Beginning Fishing training', colors[ 'cyan' ] )

    moveBoatInThisDirection = None
    if moveForwardBackward:
        moveBoatInThisDirection = 'north'
    else:
        moveBoatInThisDirection = 'right'
    # while skill can increase and player is not dead
    while not Player.IsGhost and Player.GetSkillValue( 'Fishing' ) < Player.GetSkillCap( 'Fishing' ):
        # Start fishing to the East
        if not Player.Direction == 'Up':
            Player.Walk( 'Up' )
        x = Player.Position.X - 3
        y = Player.Position.Y - 3
        while Fish( fishingPole, x, y ):
            enemy = Target.GetTargetFromList( 'enemy' )
            if enemy != None:
                FightEnemy()

        Player.Walk( 'Right' )
        x = Player.Position.X + 3
        y = Player.Position.Y - 3
        while Fish( fishingPole, x, y ):
            enemy = Target.GetTargetFromList( 'enemy' )
            if enemy != None:
                FightEnemy()

        Player.Walk( 'Down' )
        x = Player.Position.X + 3
        y = Player.Position.Y + 3
        while Fish( fishingPole, x, y ):
            enemy = Target.GetTargetFromList( 'enemy' )
            if enemy != None:
                FightEnemy()

        Player.Walk( 'Left' )
        x = Player.Position.X - 3
        y = Player.Position.Y + 3
        while Fish( fishingPole, x, y ):
            enemy = Target.GetTargetFromList( 'enemy' )
            if enemy != None:
                FightEnemy()

        Misc.Pause( 320 )
        for i in range( 0, 11 ):
            Player.ChatSay( 0, ( '%s one' % moveBoatInThisDirection ) )
            Misc.Pause( 320 )
        Misc.Pause( 320 )

        Misc.Pause( config.journalEntryDelayMilliseconds )
        if Journal.Search( 'Ar, we\'ve stopped sir.' ):
            if moveForwardBackward:
                if moveBoatInThisDirection == 'forward':
                    moveBoatInThisDirection = 'backward'
                else:
                    moveBoatInThisDirection = 'forward'
            else:
                if moveBoatInThisDirection == 'right':
                    moveBoatInThisDirection = 'left'
                else:
                    moveBoatInThisDirection = 'right'

            Misc.Pause( 320 )
            for i in range( 0, 11 ):
                Player.ChatSay( 0, ( '%s one' % moveBoatInThisDirection ) )
                Misc.Pause( 320 )
            Misc.Pause( 320 )

    Player.HeadMessage( 'Congratulations! Your Fishing is now at its skill cap!', colors[ 'green' ] )


# Start Fishing Training
TrainFishing()
