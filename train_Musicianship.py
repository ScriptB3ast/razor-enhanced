'''
Author: TheWarDoctor95
Other Contributors:
Last Contribution By: TheWarDoctor95 - March 14, 2019

Description: Uses the instruments from the player's backpack to train Musicianship to GM
'''

musichianshipTimerMilliseconds = 6500

def FindItem( itemsToLookFor, items ):
    '''
    Recursively looks through a container for any items in the provided list
    Returns the first item found from the list
    '''
    # Iterate through each item in the given list
    for item in items:
        if item.ItemID in itemsToLookFor:
            return item
        elif item.IsContainer:
            # If the list of items contains a contianer, look in that container for the item too
            itemToReturn = FindItem( itemsToLookFor, item.Contains )
            if itemToReturn != None:
                return itemToReturn
    return None


def FindInstrument():
    '''
    Uses FindItem to find an instrument in the player's backpack
    Returns the first instrument found
    '''
    instruments = [
        0xe9c,  # Drum
        0x2805,  # Flute
        0xeb3,  # Lute

        # Harps
        0xeb2,  # Lap Harp
        0xeb1,  # Standing Harp

        # Tambourines
        0xe9e,  # Tambourine
        0xe9d   # Tambourine with red tassle
    ]

    instrument = FindItem( instruments, Player.Backpack.Contains )
    return instrument


def TrainMusicianship():
    '''
    Trains Musicianship by using the instruments in the player's bag
    Transitions to a new instrument if the one being used runs out of uses
    '''
    global instrument
    global musichianshipTimerMilliseconds

    Misc.SendMessage( 'Training with: %s' % instrument )

    Items.UseItem( instrument )
    Timer.Create( 'musichianshipTimer', musichianshipTimerMilliseconds )

    while instrument != None and Player.GetSkillValue( 'Musicianship' ) < 100 and not Player.IsGhost:
        if not Timer.Check( 'musichianshipTimer' ):
            Items.UseItem( instrument )
            Timer.Create( 'musichianshipTimer', musichianshipTimerMilliseconds )
            instrument = Items.FindBySerial( instrument.Serial )
            if instrument == None:
                # Our instrument broke, we need to find a new one if possible
                instrument = FindInstrument()
                if instrument != None:
                    Misc.SendMessage( 'Training with: %s' % instrument )

    if instrument == None:
        Misc.SendMessage( 'Ran out of instruments to train with', 1100 )


instrument = FindInstrument()

if instrument == None:
    Player.HeadMessage( 1100, 'No instrument found' )
else:
    TrainMusicianship()
