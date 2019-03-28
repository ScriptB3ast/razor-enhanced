'''
Author: Aga - original author of the uosteam script
Other Contributors: TheWarDoctor95 - converted to Razor Enhanced script
Last Contribution By: TheWarDoctor95 - March 19, 2019

Description: Tames nearby animals to train Animal Taming to GM
'''

## Script options ##
# Change to the name that you want to rename the tamed animals to
renameTamedAnimalsTo = 'wardoc'
# Add any name of pets to ignore
petsToIgnore = [ renameTamedAnimalsTo, 'Crimson', 'Lizzy' ]
# Change to the number of followers you'd like to keep.
# The script will auto-release the most recently tamed animal if the follower number exceeds this number
# Some animals have a follower count greater than one, which may cause them to be released if this number is not set high enough
numberOfFollowersToKeep = 1
# Set to the maximum number of times to attempt to tame a single animal. 0 == attempt until tamed
maximumTameAttempts = 0
# Set the minimum taming difficulty to use when finding animals to tame
minimumTamingDifficulty = 31
# Set this to how you would like to heal your character if they take damage
# Options are:
# 'Healing' = use bandages
# 'Magery' = uses the Heal and Greater Heal ability depending on how much health is missing
# 'None' = do not auto-heal
healUsing = 'None'
# True or False to use Peacemaking if needed
enablePeacemaking = True
# True or False to track the animal being tamed
enableFollowAnimal = True
# Change depending on the latency to your UO shard
journalEntryDelayMilliseconds = 100
targetClearDelayMilliseconds = 100


from Scripts.glossary import items
from Scripts.glossary.enemies import GetEnemyNotorieties
from Scripts.glossary import spells
from Scripts.glossary import tameables
from System.Collections.Generic import List
from System import Byte

noAnimalsToTrainTimerMilliseconds = 10000
playerStuckTimerMilliseconds = 5000
catchUpToAnimalTimerMilliseconds = 20000
animalTamingTimerMilliseconds = 13000
peacemakingTimerMilliseconds = 10000
bandageTimerMilliseconds = 5000


def FindAnimalToTame():
    '''
    Finds the nearest tameable animal nearby
    '''
    global renameTamedAnimalsTo
    global minimumTamingDifficulty

    animalFilter = Mobiles.Filter()
    animalFilter.Enabled = True
    animalFilter.Bodies = tameables.GetAnimalIDsAtOrOverTamingDifficulty( minimumTamingDifficulty )
    animalFilter.RangeMin = 0
    animalFilter.RangeMax = 12
    animalFilter.IsHuman = 0
    animalFilter.IsGhost = 0
    animalFilter.CheckIgnoreObject = True

    tameableMobiles = Mobiles.ApplyFilter( animalFilter )

    # Exclude animals that have already been tamed by this player
    tameableMobilesTemp = tameableMobiles[:]
    for tameableMobile in tameableMobiles:
        if tameableMobile.Name in petsToIgnore:
            tameableMobilesTemp.Remove( tameableMobile )

    tameableMobiles = tameableMobilesTemp

    if len( tameableMobiles ) == 0:
        return None
    elif len( tameableMobiles ) == 1:
        return tameableMobiles[ 0 ]
    else:
        return Mobiles.Select( tameableMobiles, 'Nearest' )


def PlayerWalk( direction ):
    '''
    Moves the player in the specified direction
    '''

    playerPosition = Player.Position
    if Player.Direction == direction:
        Player.Walk( direction )
    else:
        Player.Walk( direction )
        Player.Walk( direction )
    return

def FollowMobile( mobile, maxDistanceToMobile = 2, startPlayerStuckTimer = False ):
    '''
    Uses the X and Y coordinates of the animal and player to follow the animal around the map
    Returns True if player is not stuck, False if player is stuck
    '''

    if not Timer.Check( 'catchUpToAnimalTimer' ):
        return False

    mobilePosition = mobile.Position
    playerPosition = Player.Position
    directionToWalk = ''
    if mobilePosition.X > playerPosition.X and mobilePosition.Y > playerPosition.Y:
        directionToWalk = 'Down'
    if mobilePosition.X < playerPosition.X and mobilePosition.Y > playerPosition.Y:
        directionToWalk = 'Left'
    if mobilePosition.X > playerPosition.X and mobilePosition.Y < playerPosition.Y:
        directionToWalk = 'Right'
    if mobilePosition.X < playerPosition.X and mobilePosition.Y < playerPosition.Y:
        directionToWalk = 'Up'
    if mobilePosition.X > playerPosition.X and mobilePosition.Y == playerPosition.Y:
        directionToWalk = 'East'
    if mobilePosition.X < playerPosition.X and mobilePosition.Y == playerPosition.Y:
        directionToWalk = 'West'
    if mobilePosition.X == playerPosition.X and mobilePosition.Y > playerPosition.Y:
        directionToWalk = 'South'
    if mobilePosition.X == playerPosition.X and mobilePosition.Y < playerPosition.Y:
        directionToWalk = 'North'

    if startPlayerStuckTimer:
        Timer.Create( 'playerStuckTimer', playerStuckTimerMilliseconds )

    playerPosition = Player.Position
    PlayerWalk( directionToWalk )

    newPlayerPosition = Player.Position
    if playerPosition == newPlayerPosition and not Timer.Check( 'playerStuckTimer' ):
        # Player has been stuck in the same position for a while, try to find them a way out of the stuck position
        if Player.Direction == 'Up':
            for i in range ( 5 ):
                Player.Walk( 'Down' )
        elif Player.Direction == 'Down':
            for i in range( 5 ):
                Player.Walk( 'Up' )
        elif Player.Direction == 'Right':
            for i in range( 5 ):
                Player.Walk( 'Left' )
        elif Player.Direction == 'Left':
            for i in range( 5 ):
                Player.Walk( 'Right' )
        Timer.Create( 'playerStuckTimer', playerStuckTimerMilliseconds )
    elif playerPosition != newPlayerPosition:
        Timer.Create( 'playerStuckTimer', playerStuckTimerMilliseconds )

    if Player.DistanceTo( mobile ) > maxDistanceToMobile:
        # This pause may need further tuning
        # Don't want to create a ton of infinite calls if the player is stuck, but also don't want to not be able to catch up to animals
        Misc.Pause( 100 )
        FollowMobile( mobile, maxDistanceToMobile )

    return True


def TrainAnimalTaming():
    '''
    Trains Animal Taming to GM
    '''

    # User variables
    global renameTamedAnimalsTo
    global numberOfFollowersToKeep
    global maximumTameAttempts
    global enablePeacemaking
    global enableFollowAnimal
    global journalEntryDelayMilliseconds
    global targetClearDelayMilliseconds

    # Script variables
    global noAnimalsToTrainTimerMilliseconds
    global playerStuckTimerMilliseconds
    global catchUpToAnimalTimerMilliseconds
    global animalTamingTimerMilliseconds
    global peacemakingTimerMilliseconds
    global bandageTimerMilliseconds

    if Player.GetRealSkillValue( 'Animal Taming' ) == Player.GetSkillCap( 'Animal Taming' ):
        Misc.SendMessage( 'You\'ve already maxed out Animal Taming!', 65 )
        return

    # Initialize variables
    animalBeingTamed = None
    tameHandled = False
    tameOngoing = False
    timesTried = 0
    bandageBeingApplied = False

    # Initialize skill timers
    Timer.Create( 'animalTamingTimer', 1 )
    if enablePeacemaking:
        Timer.Create( 'peacemakingTimer', 1 )

    if healUsing == 'Healing':
        Timer.Create( 'bandageTimer', 1 )
    elif healUsing == 'Magery':
        Timer.Create( 'healSpellTimer', 1 )

    # Initialize the journal and ignore object list
    Journal.Clear()
    Misc.ClearIgnore()

    # Toggle war mode to make sure the player isn't going to kill the animal being tamed
    Player.SetWarMode( True )
    Player.SetWarMode( False )

    while not Player.IsGhost and Player.GetRealSkillValue( 'Animal Taming' ) < 100:
        if not maximumTameAttempts == 0 and timesTried > maximumTameAttempts:
            Mobiles.Message( animalBeingTamed, 1100, 'Tried more than %i times to tame. Ignoring animal' % maximumTameAttempts )
            Mobiles.IgnoreObject( animalBeingTamed )
            animalBeingTamed = None
            timesTried = 0

        if Player.Hits != Player.HitsMax:
            if healUsing != 'None':
                if healUsing == 'Healing' and not Timer.Check( 'bandageTimer' ):
                    # Clear any previously selected target and the target queue
                    Target.ClearLastandQueue()
                    # Wait for the target to finish clearing
                    Misc.Pause( targetClearDelayMilliseconds )

                    bandage = items.FindBandage()
                    Item.UseItem( bandage )
                    Target.TargetExecute( Player.Self )

                    Timer.Create( 'bandageTimer', bandageTimerMilliseconds )
                elif healUsing == 'Magery':
                    if ( Player.MaxHits - Player.Hits ) > 30:
                        Spells.CastMagery( 'Greater Heal' )
                        Timer.Create( 'healSpellTimer', spells.spells[ 'Greater Heal' ].delayInMs )
                    else:
                        Spells.CastMagery( 'Heal' )
                        Timer.Create( 'healSpellTimer', spells. spell[ 'Heal' ].delayInMs )

            if enablePeacemaking:
                enemyFilter = Mobiles.Filter()
                enemyFilter.Enabled = True
                enemyFilter.CheckIgnoreObject = False
                enemyFilter.Notorieties = GetEnemyNotorieties()
                enemyFilter.RangeMin = 0
                enemyFilter.RangeMax = 12
                enemies = Mobiles.ApplyFilter( enemyFilter )

                enemyAtWar = False
                enemyToPutToPeace = None
                for enemy in enemies:
                    if enemy.WarMode:
                        enemyAtWar = True
                        enemyToPutToPeace = enemy
                        break

                Timer.Create( 'peacemakingTimer', 1 )
                while enemyAtWar:
                    if not Timer.Check( 'peacemakingTimer' ):
                        # Clear any previously selected target and the target queue
                        Target.ClearLastandQueue()
                        # Wait for the target to finish clearing
                        Misc.Pause( targetClearDelayMilliseconds )

                        Player.UseSkill( 'Peacemaking' )
                        # Wait for journal entry to come up
                        Misc.Pause( journalEntryDelayMilliseconds )
                        if Journal.SearchByType( 'What instrument shall you play?', 'Regular' ):
                            instrument = items.FindInstrument( Player.Backpack.Contains )
                            if instrument == None:
                                Misc.Message( 'No instruments to peacemake with.', 1100 )
                                break
                            else:
                                Target.WaitForTarget( 2000, True )
                                Target.TargetExecute( instrument.Serial )

                        if Journal.SearchByType( 'Whom do you wish to calm?', 'Regular' ):
                            Target.WaitForTarget( 2000, True )
                            Target.TargetExecute( enemyToPutToPeace )
                        Timer.Create( 'peacemakingTimer', peacemakingTimerMilliseconds )

                    enemyAtWar = False
                    enemyToPutToPeace = None
                    for enemy in enemies:
                        if enemy.WarMode:
                            enemyAtWar = True
                            enemyToPutToPeace = enemy
                            break

                    # Wait a little bit so that the while loop doesn't consume as much CPU
                    Misc.Pause( 50 )

                if Player.WarMode:
                    Player.SetWarMode( False )

        # If there is no animal being tamed, try to find an animal to tame
        if animalBeingTamed == None:
            animalBeingTamed = FindAnimalToTame()
            if animalBeingTamed == None:
                # No animals in the area. Pause for a while so that this is constantly running until something is available to tame
                Misc.Pause( 1000 )
                continue
            else:
                Mobiles.Message( animalBeingTamed, 90, 'Found animal to tame' )

        # Check if animal is close enough to tame
        if Player.DistanceTo( animalBeingTamed ) > 12:
            Misc.SendMessage( 'Animal moved too far away, ignoring for now', 1100  )
            animalBeingTamed = None
            continue
        elif animalBeingTamed != None and Player.DistanceTo( animalBeingTamed ) > 1:
            if enableFollowAnimal:
                Timer.Create( 'catchUpToAnimalTimer', catchUpToAnimalTimerMilliseconds )
                playerStuck = not FollowMobile( animalBeingTamed, 2, True )
                if playerStuck:
                    Player.HeadMessage( 1100, 'Player stuck!' )
                    return
            else:
                Mobiles.Message( animalBeingTamed, 34, 'Not close enough!' )

        # If peacemaking is enabled, make sure the animal being tamed is calm
        if enablePeacemaking:
            if animalBeingTamed.WarMode:
                if Player.WarMode:
                    Player.SetWarMode( False )
                if not Timer.Check( 'peacemakingTimer' ):
                    # Clear any previously selected target and the target queue
                    Target.ClearLastandQueue()
                    # Wait for the target to finish clearing
                    Misc.Pause( targetClearDelayMilliseconds )

                    Player.UseSkill( 'Peacemaking' )
                    # Wait for the journal entry to come up
                    Misc.Pause( journalEntryDelayMilliseconds )
                    if Journal.SearchByType( 'What instrument shall you play?', 'Regular' ):
                        instrument = items.FindInstrument( Player.Backpack.Contains )
                        if instrument == None:
                            Misc.Message( 'No instruments to peacemake with.', 1100 )
                            break
                        Target.WaitForTarget( 2000, True )
                        Target.TargetExecute( instrument )

                    Target.WaitForTarget( 2000, True )
                    Target.TargetExecute( animalBeingTamed )
                    Timer.Create( 'peacemakingTimer', peacemakingTimerMilliseconds )
                if Player.WarMode:
                    Player.SetWarMode( False )
            else:
                if Player.WarMode:
                    Player.SetWarMode( False )

        # Tame the animal if a tame is not currently being attempted and enough time has passed since last using Animal Taming
        if not tameOngoing and not Timer.Check( 'animalTamingTimer' ):
            # Clear any previously selected target and the target queue
            Target.ClearLastandQueue()
            # Wait for the target to finish clearing
            Misc.Pause( targetClearDelayMilliseconds )

            # Hey, we're finally using the Animal Taming skill! 'bout time!
            Player.UseSkill( 'Animal Taming' )
            Target.WaitForTarget( 2000, True )
            Target.TargetExecute( animalBeingTamed )

            # Check if Animal Taming was successfully triggered
            if Journal.SearchByType( 'Tame which animal?', 'Regular' ):
                timesTried += 1

                # Restart the timer so that it will go off when we'll be able to use the skill again
                Timer.Create( 'animalTamingTimer', animalTamingTimerMilliseconds )

                # Set tameOngoing to true to start the journal checks that will handle the result of the taming
                tameOngoing = True
            else:
                continue

        if tameOngoing:
            if ( Journal.SearchByName( 'It seems to accept you as master.', animalBeingTamed.Name ) or
                    Journal.SearchByType( 'That wasn\'t even challenging.', 'Regular' ) ):
                # Animal was successfully tamed
                if animalBeingTamed.Name != renameTamedAnimalsTo:
                    Misc.PetRename( animalBeingTamed, renameTamedAnimalsTo )
                if Player.Followers > numberOfFollowersToKeep:
                    # Release recently tamed animal
                    Misc.WaitForContext( animalBeingTamed.Serial, 2000 )
                    Misc.ContextReply( animalBeingTamed.Serial, 8 )
                    Gumps.WaitForGump( 2426193729, 10000 )
                    Gumps.SendAction( 2426193729, 2 )
                Misc.IgnoreObject( animalBeingTamed )
                animalBeingTamed = None
                timesTried = 0
                tameHandled = True
            elif ( Journal.SearchByName( 'You fail to tame the creature.', animalBeingTamed.Name ) or
                    Journal.SearchByType( 'You must wait a few moments to use another skill.', 'Regular' ) ):
                tameHandled = True
            elif ( Journal.SearchByType( 'That is too far away.', 'Regular' ) or
                    Journal.SearchByName( 'You are too far away to continue taming.', animalBeingTamed.Name ) ):
                # Animal moved too far away, set to None so that another animal can be found
                animalBeingTamed = None
                timesTried = 0
                Timer.Create( 'animalTamingTimer', 1 )
                tameHandled = True
            elif ( Journal.SearchByName( 'You have no chance of taming this creature', animalBeingTamed.Name ) or
                    Journal.SearchByType( 'Target cannot be seen', 'Regular' ) or
                    Journal.Search( 'Do not have a clear path to the animal' ) or
                    Journal.Search( 'This animal has had too many owners' ) or
                    Journal.Search( 'That animal looks tame already' ) ):
                # Ignore the object and set to None so that another animal can be found
                Misc.IgnoreObject( animalBeingTamed )
                animalBeingTamed = None
                timesTried = 0
                Timer.Create( 'animalTamingTimer', 1 )
                tameHandled = True

            if tameHandled:
                Journal.Clear()
                tameHandled = False
                tameOngoing = False

        # Wait a little bit so that the while loop doesn't consume as much CPU
        Misc.Pause( 50 )

# Start Animal Taming
TrainAnimalTaming()
