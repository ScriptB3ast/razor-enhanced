'''
Author: TheWarDoctor95
Other Contributors:
Last Contribution By: TheWarDoctor95 - April 16, 2019

Description: Uses the selected target to train Item Identification to its cap
'''

from Scripts.glossary.colors import colors

itemIdentificationTimerMilliseconds = 1200

# Select what to run Item Identification on
itemIdentificationTarget = Target.PromptTarget( 'Select item to train on' )

def TrainItemIdentification():
    '''
    Trains Item Identification with the selected target
    '''
    global itemIdentificationTarget

    Timer.Create( 'itemIdentificationTimer', 1 )
    targetStillExists = Items.FindBySerial( itemIdentificationTarget )

    while targetStillExists != None and not Player.IsGhost and Player.GetRealSkillValue( 'Item ID' ) < Player.GetSkillCap( 'Item ID' ):
        if not Timer.Check( 'itemIdentificationTimer' ):
            Player.UseSkill( 'Item ID' )
            Target.WaitForTarget( 2000, True )
            Target.TargetExecute( itemIdentificationTarget )
            Timer.Create( 'itemIdentificationTimer', itemIdentificationTimerMilliseconds )
        Misc.Pause( 50 )
        targetStillExists = Items.FindBySerial( itemIdentificationTarget )

    if targetStillExists == None:
        Player.HeadMessage( colors[ 'red' ], 'Selected target for Item Identification is gone' )
    elif Player.GetRealSkillValue( 'Item ID' ) >= Player.GetSkillCap( 'Item ID' ):
        Player.HeadMessage( colors[ 'green' ], 'Item Identification training complete!' )

# Start Training
TrainItemIdentification()
