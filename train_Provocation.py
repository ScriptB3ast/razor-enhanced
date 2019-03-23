'''
Author: TheWarDoctor95
Other Contributors:
Last Contribution By: TheWarDoctor95 - March 14, 2019

Description: Uses the instruments from the player's backpack and the selected target
    to train Provocation to GM
'''

provocationTimerMilliseconds = 10200

from Scripts.utilities.colors import colors

provocationTarget = Target.PromptTarget( 'Select enemy to train on' )
Target.SetLast( provocationTarget )
Mobiles.Message( Target.GetLast(), 52, 'Selected for provocation training' )

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
Mobiles.Message( Target.GetLast(), colors[ 'yellow' ], 'Selected for provocation training' )


def TrainProvocation():
    '''
    Trains Musicianship by using the instruments in the player's bag
    Transitions to a new instrument if the one being used runs out of uses
    '''
    global provocationTimerMilliseconds

    Timer.Create( 'provocationTimer', 1 )

    instrument = FindInstrument()
    if instrument == None:
        Misc.SendMessage( 'No instruments to train with', colors[ 'red' ] )
        return

    Misc.SendMessage( 'Training with: %s' % instrument )

    while instrument != None and Player.GetSkillValue( 'Provocation' ) < 100 and not Player.IsGhost:
        targetStillExists = Mobiles.FindBySerial( Target.GetLast() )
        if targetStillExists == None:
            Misc.SendMessage( 'Provo target has disappeared', colors[ 'red' ] )
            provocationTarget = Target.PromptTarget( 'Select enemy to train on' )
            Target.SetLast( provocationTarget )
            Mobiles.Message( Target.GetLast(), colors[ 'yellow' ], 'Selected for provocation training' )
        if not Timer.Check( 'provocationTimer' ):
            Journal.Clear()
            Player.UseSkill( 'Provocation' )
            if Journal.Search( 'What instrument shall you play?' ):
                # Instrument either broke or hasn't been selected
                instrument = FindInstrument()
                if instrument == None:
                    # No more instruments, stop the provo attempt
                    Target.Cancel()
                    continue
                else:
                    Misc.SendMessage( 'Training with: %s' % instrument )
                    Target.WaitForTarget( 10000, False )
                    Target.TargetExecute( instrument.Serial )
            enemy = Target.GetLast()
            Target.WaitForTarget( 10000, False )
            Target.TargetExecute( enemy )
            Target.WaitForTarget( 10000, False )
            Target.TargetExecute( Player.Serial )
            Target.SetLast( enemy )

            Timer.Create( 'provocationTimer', provocationTimerMilliseconds )

    if instrument == None:
        Misc.SendMessage( 'Ran out of instruments to train with', colors[ 'red' ] )

# Start Training
TrainProvocation()
