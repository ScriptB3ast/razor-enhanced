'''
Author: TheWarDoctor95
Other Contributors:
Last Contribution By: TheWarDoctor95 - March 20, 2019

Description: Uses bandages on a player's ghost to train Healing
'''

from Scripts.config import targetClearDelayMilliseconds
from Scripts.glossary.items import FindBandage
from Scripts.utilities.colors import colors

def TrainHealing():
    '''
    Trains Healing to the skill cap
    '''
    if Player.GetRealSkillValue( 'Healing' ) == Player.GetSkillCap( 'Healing' ):
        Misc.SendMessage( 'You\'ve already maxed out Healing!', colors[ 'green' ] )
        return

    bandages = FindBandage( Player.Backpack )

    if bandages == None:
        Misc.SendMessage( 'No bandages to train with', colors[ 'red' ] )
        return

    ghost = Target.PromptTarget( 'Select ghost to train on' )
    Mobiles.Message( ghost, colors[ 'cyan' ], 'Selected for Healing training' )

    Journal.Clear()

    while Player.GetRealSkillValue( 'Healing' ) < Player.GetSkillCap( 'Healing' ):
        # Clear any previously selected target and the target queue
        Target.ClearLastandQueue()

        # Wait for the target to finish clearing
        Misc.Pause( targetClearDelayMilliseconds )

        Items.UseItem( bandages )
        Target.WaitForTarget( 2000, True )
        Target.TargetExecute( ghost )

        # Wait for a journal entry to come up stating that the bandage application has finished
        while not ( Journal.SearchByType( 'You are unable to resurrect your patient', 'Regular' ) or
                Journal.SearchByType( 'You are able to resurrect your patient', 'Regular' ) ):
            Misc.Pause( 100 )

        Journal.Clear()

        bandages = FindBandage( Player.Backpack )
        if bandages == None:
            Misc.SendMessage( 'Ran out of bandages to train with', colors[ 'red' ] )
            return

        Misc.Pause( 50 )

    Misc.SendMessage( 'Healing training complete!', colors[ 'green' ] )

# Start Healing training
TrainHealing()
