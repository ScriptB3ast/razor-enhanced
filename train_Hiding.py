'''
Author: TheWarDoctor95
Other Contributors:
Last Contribution By: TheWarDoctor95 - April 12, 2019

Description: Trains Hiding to its skill cap
'''

hidingTimerMilliseconds = 10200

from Scripts.glossary.colors import colors

def TrainHiding():
    '''
    Trains Hiding to its skill cap
    '''

    if Player.GetSkillValue( 'Hiding' ) == Player.GetSkillCap( 'Hiding' ):
        Player.HeadMessage( colors[ 'green' ], 'Your Hiding is already at its skill cap!' )
        return

    Misc.SendMessage( 'Beginning Hiding training', colors[ 'cyan' ] )

    Player.UseSkill( 'Hiding' )
    # Skill cooldown is 10,000 ms, but adding an extra 200 ms in case of latency issues
    Timer.Create( 'hidingTimer', hidingTimerMilliseconds )
    # while skill can increase and player is not dead
    while not Player.IsGhost and Player.GetSkillValue( 'Hiding' ) < Player.GetSkillCap( 'Hiding' ):
        if not Timer.Check( 'hidingTimer' ):
            # Cooldown has finished, we can use the skill again and reset the timer
            Player.UseSkill( 'Hiding' )
            Timer.Create( 'hidingTimer', hidingTimerMilliseconds )

    Player.HeadMessage( colors[ 'green' ], 'Congratulations! Your Hiding is now at its skill cap!' )

# Start Hiding training
TrainHiding()
