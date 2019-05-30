'''
Author: TheWarDoctor95
Other Contributors:
Last Contribution By: TheWarDoctor95 - March 23, 2019

Description: Uses the instruments from the player's backpack and the selected or
    auto-selected target to train Provocation to its cap
'''

autoSelectTarget = False
provocationTimerMilliseconds = 10200

from Scripts import config
from Scripts.glossary.items.instruments import FindInstrument
from Scripts.glossary.colors import colors
from Scripts.glossary.enemies import GetEnemies

def TrainProvocation():
    '''
    Trains Musicianship by using the instruments in the player's bag
    Transitions to a new instrument if the one being used runs out of uses
    '''
    global autoSelectTarget
    global provocationTimerMilliseconds

    Timer.Create( 'provocationTimer', 1 )

    instrument = FindInstrument( Player.Backpack )
    if instrument == None:
        Misc.SendMessage( 'No instruments to train with', colors[ 'red' ] )
        return
    
    provocationTarget = None
    while instrument != None and Player.GetSkillValue( 'Provocation' ) < 100 and not Player.IsGhost:
        if provocationTarget == None:
            if autoSelectTarget:
                enemies = GetEnemies( Mobiles, 0, 8 )
                provocationTarget = Mobiles.Select( enemies, 'Nearest' )
            else:
                provocationTarget = Target.PromptTarget( 'Select target to train provo on' )
                provocationTarget = Mobiles.FindBySerial( provocationTarget )
            
            if provocationTarget != None:
                Mobiles.Message( provocationTarget, colors[ 'cyan' ], 'Selected for provocation training' )
        else:
            provocationTarget = Mobiles.FindBySerial( provocationTarget.Serial )
            
        if autoSelectTarget and provocationTarget == None:
            Misc.Pause( 100 )
            continue

        if not Timer.Check( 'provocationTimer' ):
            Journal.Clear()
            Player.UseSkill( 'Provocation' )
            Misc.Pause( config.journalEntryDelayMilliseconds )
            if Journal.Search( 'What instrument shall you play?' ):
                # Instrument either broke or hasn't been selected
                instrument = FindInstrument( Player.Backpack )
                if instrument == None:
                    # No more instruments, stop the provo attempt
                    Target.Cancel()

                    Misc.SendMessage( 'Ran out of instruments to train with', colors[ 'red' ] )
                    return
                else:
                    Target.WaitForTarget( 2000, True )
                    Target.TargetExecute( instrument.Serial )

            Target.WaitForTarget( 2000, True )
            Target.TargetExecute( provocationTarget )
            Target.WaitForTarget( 2000, True )
            Target.TargetExecute( Player.Serial )
            Target.SetLast( provocationTarget )

            Timer.Create( 'provocationTimer', provocationTimerMilliseconds )

        # Wait a little bit so that the while loop doesn't consume as much CPU
        Misc.Pause( 50 )

# Start Training
TrainProvocation()
