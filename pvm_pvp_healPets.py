from Scripts.utilities.items import FindItem
from Scripts.glossary.colors import colors
from System.Collections.Generic import List

if Misc.ShardName() == 'UO Evolution':
    petsToCheck = [
        0x002A6E71, # Horse
        0x0015D121, # Zazzy
    ]
else:
    petsToCheck = [
        0x00048E19, # Saphira
        0x00102404, # Your Darkest Nightmare
        0x00189E83, # an avian steed
        0x00302246, # Bid'Daum
        0x0001801E, # Metalicana
        0x0009CA1B, # Toothless
        0x000EAFDB, # The Darkness
        0x0025E1FA, # Nocturnal llama
        0x00064ECB, # Izzo
        0x00088F42, # Give Me Relic
    ]

#for pet in petsToCheck:
#    Timer.Create( 'distanceTimer%s' % pet, 1 )

def TestBandagesApplying():
    # Fetch the Journal entries (oldest to newest)
    regularText = Journal.GetTextByType( 'Regular' )

    # Reverse the Journal entries so that we read from newest to oldest
    regularText.Reverse()

    # Read back until the bandages were started to see if they have finished applying
    for line in regularText[ 0 : len( regularText ) ]:
        if line == 'You begin applying the bandages.':
            break
        if ( line == 'You finish applying the bandages.' or
                line == 'You heal what little damage your patient had.' or
                line == 'You did not stay close enough to heal your patient!' or
                line == 'You apply the bandages, but they barely help.' or
                line == 'That being is not damaged!' or
                line == 'You fail to resurrect the creature.' or
                line == 'You are able to resurrect your patient.' or
                line == 'You have cured the target of all poisons!' or
                line == 'That is too far away.' ):
            return False
    return True


def WaitForBandagesToApply():
    bandageDone = False
    secondsCounter = 0
    while TestBandagesApplying():
        Misc.Pause( 1000 )
        secondsCounter += 1
        Misc.SendMessage( '%i seconds since bandage started' % ( secondsCounter ) )
    return


def HealPets():
    global petsToCheck
    
    bandages = FindItem( 0x0E21, Player.Backpack )
    
    if bandages == None:
        Misc.SendMessage( 'Out of bandages!', colors[ 'red' ] )
        return
    #Misc.SendMessage( 'healing pets' )
    
    petFilter = Mobiles.Filter()
    petFilter.RangeMin = 0
    petFilter.RangeMax = 1
    petFilter.IsHuman = 0
    petFilter.IsGhost = 0
    petFilter.Friend = 1
    
    pets = Mobiles.ApplyFilter( petFilter )
    
    if len( pets ) == 0:
        return
    
    petToHeal = Mobiles.Select( pets, 'Weakest' )
    
    if petToHeal.Hits == petToHeal.HitsMax:
        petFilter.Poisoned = 1
        pets = Mobiles.ApplyFilter( petFilter )
        if len( pets ) == 0:
            return
        else:
            petToHeal = Mobiles.Select( pets, 'Weakest' )
    
    Items.UseItem( bandages )
    Target.WaitForTarget( 10000, False )
    Target.TargetExecute( petToHeal )
    Player.HeadMessage( colors[ 'cyan' ], 'Applying bandage on %s (currently %i%% health)' % ( petToHeal.Name, ( float( petToHeal.Hits ) / float( petToHeal.HitsMax ) * 100 ) ) )

    Misc.Pause( 200 )

    WaitForBandagesToApply()
    return

    for petSerial in petsToCheck:
        pet = Mobiles.FindBySerial( petSerial )
        if pet == None:
            continue
        #Misc.SendMessage( 'Checking %s\'s health' % pet.Name )
        if Misc.ShardName() == 'UO Evolution':
            maxDistance = 2
        else:
            maxDistance = 1
        if pet.Hits < pet.HitsMax or pet.Poisoned:
            if Player.DistanceTo( pet ) > maxDistance:
                if not Timer.Check( 'distanceTimer%s' % petSerial ):
                    Misc.SendMessage( 'Too far away from %s to apply bandages' % ( pet.Name ), colors[ 'red' ] )
                    Timer.Create( 'distanceTimer%s' % petSerial, 1000 )
                continue

            Items.UseItem( bandages )
            Target.WaitForTarget( 10000, False )
            Target.TargetExecute( pet )
            Player.HeadMessage( colors[ 'cyan' ], 'Applying bandage on %s (currently %i%% health)' % ( pet.Name, ( float( pet.Hits ) / float( pet.HitsMax ) * 100 ) ) )
            
            Misc.Pause( 200 )
            
            bandageDone = False
            while not bandageDone:
                regularText = Journal.GetTextByType( 'Regular' )
                regularText.Reverse()
                for line in regularText[ 0 : len( regularText ) ]:
                    if line == 'You begin applying the bandages.':
                        break
                    if ( line == 'You finish applying the bandages.' or
                            line == 'You heal what little damage your patient had.' or
                            line == 'You did not stay close enough to heal your patient!' or
                            line == 'You apply the bandages, but they barely help.' or
                            line == 'That being is not damaged!' or
                            line == 'You fail to resurrect the creature.' or
                            line == 'You are able to resurrect your patient.' or
                            line == 'You have cured the target of all poisons!' ):
                        bandageDone = True
                        Misc.Pause( 100 )
                        break
                Misc.Pause( 50 )
            return

while not Player.IsGhost:
    HealPets()
    Misc.Pause( 150 )
