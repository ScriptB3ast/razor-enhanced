'''
Author: TheWarDoctor95
Other Contributors:
Last Contribution By: TheWarDoctor95 - April 14, 2019

Description: Trains Tracking to its skill cap
'''

trackingTimerMilliseconds = 10500

from Scripts.glossary.colors import colors

def TrainTracking():
    '''
    Trains Tracking to its skill cap
    '''

    if Player.GetSkillValue( 'Tracking' ) == Player.GetSkillCap( 'Tracking' ):
        Player.HeadMessage( 'Your Tracking is already at its skill cap!', colors[ 'green' ] )
        return

    Misc.SendMessage( 'Beginning Tracking training', colors[ 'cyan' ] )

    Player.UseSkill( 'Tracking' )
    # Skill cooldown is 10,000 ms, but adding an extra 200 ms in case of latency issues
    Timer.Create( 'trackingTimer', trackingTimerMilliseconds )
    # while skill can increase and player is not dead
    while not Player.IsGhost and Player.GetSkillValue( 'Tracking' ) < Player.GetSkillCap( 'Tracking' ):
        if not Timer.Check( 'trackingTimer' ):
            # Cooldown has finished, we can use the skill again and reset the timer
            Player.UseSkill( 'Tracking' )
            Gumps.WaitForGump( 2976808305, 2000 )
            Gumps.SendAction( 2976808305, 4 )
            Gumps.WaitForGump( 2976808305, 2000 )
            Gumps.SendAction( 2976808305, 0 )
            Timer.Create( 'trackingTimer', trackingTimerMilliseconds )

    Player.HeadMessage( 'Congratulations! Your Tracking is now at its skill cap!', colors[ 'green' ] )

# Start Tracking training
TrainTracking()
