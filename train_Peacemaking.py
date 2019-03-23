'''
Author: TheWarDoctor95
Other Contributors:
Last Contribution By: TheWarDoctor95 - March 23, 2019

Description: Uses the Peacemaking skill on the player to train Peacemaking to GM
'''

peacemakingTimerMilliseconds = 10200

from System.Collections.Generic import List
from Scripts.glossary.items import FindInstrument
from Scripts.glossary.enemies import GetEnemyNotorieties, GetEnemies
from Scripts import config

def TrainPeacemaking():
    '''
    Trains Peacemaking to GM
    '''
    # Script variables
    global peacemakingTimerMilliseconds
    peacemakingHandled = False

    if Player.GetRealSkillValue( 'Peacemaking' ) == Player.GetSkillCap( 'Peacemaking' ):
        Misc.SendMessage( 'You\'ve already maxed out Animal Taming!', 65 )
        return

    # Initialize skill timers
    Timer.Create( 'peacemakingTimer', 1 )

    # Initialize the journal and ignore object list
    Journal.Clear()
    Misc.ClearIgnore()

    while not Player.IsGhost and Player.GetRealSkillValue( 'Peacemaking' ) < Player.GetSkillCap( 'Peacemaking' ):
        if not Timer.Check( 'peacemakingTimer' ):
            # Clear any previously selected target and the target queue
            Target.ClearLastandQueue()

            # Wait for the target to finish clearing
            Misc.Pause( config.targetClearDelayMilliseconds )

            Player.UseSkill( 'Peacemaking' )

            # Wait for the journal entry to come up
            Misc.Pause( config.journalEntryDelayMilliseconds )

            # Handle the Journal response
            if Journal.SearchByType( 'What instrument shall you play?', 'Regular' ):
                instrument = FindInstrument( Player.Backpack )
                if instrument == None:
                    Misc.Message( 'No instrument to peacemake with.', 1100 )
                    return
                Target.WaitForTarget( 2000, True )
                Target.TargetExecute( instrument )

            Target.WaitForTarget( 2000, True )
            Target.TargetExecute( Player.Serial )

            # Wait for the journal entry to come up
            Misc.Pause( config.journalEntryDelayMilliseconds )

            if ( Journal.SearchByType( 'You play hypnotic music, calming your target.', 'Regular' ) or
                    Journal.SearchByType( 'You play your hypnotic music, stopping the battle.', 'Regular' ) or
                    Journal.SearchByType( 'You attempt to calm everyone, but fail.', 'Regular' ) or
                    Journal.SearchByType( 'You play hypnotic music, but there is nothing in range for you to calm.', 'Regular' ) or
                    Journal.SearchByType( 'You attempt to calm your target, but fail.', 'Regular' ) ):
                # Skill was used successfully, even if the enemy was not successfully put to peace
                Timer.Create( 'peacemakingTimer', peacemakingTimerMilliseconds )
            elif Journal.SearchByType( 'You have no chance of calming that creature', 'Regular' ):
                # We weren't able to use the skill, indicate as such by not waiting for the typical cooldown
                Timer.Create( 'peacemakingTimer', 1 )
            else:
                # We weren't able to use the skill, indicate as such by not waiting for the typical cooldown
                Timer.Create( 'peacemakingTimer', 1 )

            Journal.Clear()

        # Wait a little bit so that the while loop doesn't consume as much CPU
        Misc.Pause( 50 )

# Start Peacemaking training
TrainPeacemaking()
