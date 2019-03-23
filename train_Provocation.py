'''
Author: TheWarDoctor95
Other Contributors:
Last Contribution By: TheWarDoctor95 - March 23, 2019

Description: Uses the instruments from the player's backpack and the selected target
    to train Provocation to GM
'''

provocationTimerMilliseconds = 10200

from Scripts.glossary.items import FindInstrument
from Scripts.utilities.colors import colors

provocationTarget = Target.PromptTarget( 'Select enemy to train on' )
Mobiles.Message( provocationTarget, colors[ 'cyan' ], 'Selected for provocation training' )


def TrainProvocation():
    '''
    Trains Musicianship by using the instruments in the player's bag
    Transitions to a new instrument if the one being used runs out of uses
    '''
    global provocationTimerMilliseconds
    global provocationTarget

    Timer.Create( 'provocationTimer', 1 )

    instrument = FindInstrument()
    if instrument == None:
        Misc.SendMessage( 'No instruments to train with', colors[ 'red' ] )
        return

    Misc.SendMessage( 'Training with: %s' % instrument )

    while instrument != None and Player.GetSkillValue( 'Provocation' ) < 100 and not Player.IsGhost:
        targetStillExists = Mobiles.FindBySerial( provocationTarget )
        if targetStillExists == None:
            Misc.SendMessage( 'Provo target has disappeared', colors[ 'red' ] )
            provocationTarget = Target.PromptTarget( 'Select enemy to train on' )
            Target.SetLast( provocationTarget )
            Mobiles.Message( provocationTarget, colors[ 'cyan' ], 'Selected for provocation training' )
        if not Timer.Check( 'provocationTimer' ):
            Journal.Clear()
            Player.UseSkill( 'Provocation' )
            if Journal.Search( 'What instrument shall you play?' ):
                # Instrument either broke or hasn't been selected
                instrument = FindInstrument()
                if instrument == None:
                    # No more instruments, stop the provo attempt
                    Target.Cancel()

                    Misc.SendMessage( 'Ran out of instruments to train with', colors[ 'red' ] )
                    return
                else:
                    Misc.SendMessage( 'Training with: %s' % instrument )
                    Target.WaitForTarget( 2000, True )
                    Target.TargetExecute( instrument.Serial )

            Target.WaitForTarget( 2000, True )
            Target.TargetExecute( provocationTarget )
            Target.WaitForTarget( 2000, True )
            Target.TargetExecute( Player.Serial )
            Target.SetLast( enemy )

            Timer.Create( 'provocationTimer', provocationTimerMilliseconds )

        # Wait a little bit so that the while loop doesn't consume as much CPU
        Misc.Pause( 50 )

# Start Training
TrainProvocation()
