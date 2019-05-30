'''
Author: TheWarDoctor95
Other Contributors:
Last Contribution By: TheWarDoctor95 - May 1, 2019

Description: Trains Spirit Speak to its skill cap
'''

spiritSpeakTimerMilliseconds = 1200

from Scripts.glossary.colors import colors

def TrainSpiritSpeak():
    '''
    Trains Spirit Speak to its skill cap
    '''

    if Player.GetSkillValue( 'Spirit Speak' ) == Player.GetSkillCap( 'Spirit Speak' ):
        Player.HeadMessage( colors[ 'green' ], 'Your Spirit Speak is already at its skill cap!' )
        return

    Misc.SendMessage( 'Beginning Spirit Speak training', colors[ 'cyan' ] )

    Player.UseSkill( 'Spirit Speak' )
    # Skill cooldown is 10,000 ms, but adding an extra 200 ms in case of latency issues
    Timer.Create( 'spiritSpeakTimer', spiritSpeakTimerMilliseconds )
    # while skill can increase and player is not dead
    while not Player.IsGhost and Player.GetSkillValue( 'Spirit Speak' ) < Player.GetSkillCap( 'Spirit Speak' ):
        if not Timer.Check( 'spiritSpeakTimer' ):
            # Cooldown has finished, we can use the skill again and reset the timer
            Player.UseSkill( 'Spirit Speak' )
            Timer.Create( 'spiritSpeakTimer', spiritSpeakTimerMilliseconds )

    Player.HeadMessage( colors[ 'green' ], 'Congratulations! Your Spirit Speak is now at its skill cap!' )

# Start Spirit Speak training
TrainSpiritSpeak()
