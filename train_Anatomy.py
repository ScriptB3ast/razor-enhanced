'''
Author: TheWarDoctor95
Other Contributors:
Last Contribution By: TheWarDoctor95 - May 28, 2019

Description: Uses the selected target to train Anatomy to its cap
'''

from Scripts.glossary.colors import colors

anatomyTimerMilliseconds = 4200

# Select what to run Anatomy on
anatomyTarget = Target.PromptTarget( 'Select mob to train on (recommended to use a pet)' )
Mobiles.Message( anatomyTarget, 52, 'Selected for anatomy training' )

def TrainAnatomy():
    '''
    Trains Anatomy with the selected target
    '''
    global anatomyTarget

    Timer.Create( 'anatomyTimer', 1 )
    targetStillExists = Mobiles.FindBySerial( anatomyTarget )

    while targetStillExists != None and not Player.IsGhost and Player.GetRealSkillValue( 'Anatomy' ) < Player.GetSkillCap( 'Anatomy' ):
        if not Timer.Check( 'anatomyTimer' ):
            Player.UseSkill( 'Anatomy' )
            Target.WaitForTarget( 2000, True )
            Target.TargetExecute( anatomyTarget )
            Timer.Create( 'anatomyTimer', anatomyTimerMilliseconds )
        Misc.Pause( 50 )
        targetStillExists = Mobiles.FindBySerial( anatomyTarget )

    if targetStillExists == None:
        Player.HeadMessage( colors[ 'red' ], 'Selected target for anatomy is gone' )
    elif Player.GetRealSkillValue( 'Anatomy' ) >= Player.GetSkillCap( 'Anatomy' ):
        Player.HeadMessage( colors[ 'green' ], 'Anatomy training complete!' )

# Start Training
TrainAnatomy()
