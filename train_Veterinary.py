'''
Author: TheWarDoctor95
Other Contributors:
Last Contribution By: TheWarDoctor95 - April 19, 2019

Description: Uses bandages on a pet's ghost to train Veterinary
'''

from Scripts.config import targetClearDelayMilliseconds
from Scripts.glossary.items import FindBandage
from Scripts.glossary.colors import colors

def TrainVeterinary():
    '''
    Trains Veterinary to the skill cap
    '''
    if Player.GetRealSkillValue( 'Veterinary' ) == Player.GetSkillCap( 'Veterinary' ):
        Misc.SendMessage( 'You\'ve already maxed out Veterinary!', colors[ 'green' ] )
        return

    bandages = FindBandage( Player.Backpack )

    if bandages == None:
        Misc.SendMessage( 'No bandages to train with', colors[ 'red' ] )
        return

    ghost = Target.PromptTarget( 'Select ghost to train on' )
    Mobiles.Message( ghost, colors[ 'cyan' ], 'Selected for Veterinary training' )

    Journal.Clear()

    while not Player.IsGhost and Player.GetRealSkillValue( 'Veterinary' ) < Player.GetSkillCap( 'Veterinary' ):
        # Clear any previously selected target and the target queue
        Target.ClearLastandQueue()

        # Wait for the target to finish clearing
        Misc.Pause( targetClearDelayMilliseconds )

        Items.UseItem( bandages )
        Target.WaitForTarget( 2000, True )
        Target.TargetExecute( ghost )

        # Wait for a journal entry to come up stating that the bandage application has finished
        while not ( Journal.SearchByType( 'You are able to resurrect the creature.', 'Regular' ) or
        Journal.SearchByType( 'You fail to resurrect the creature', 'Regular' ) ):
            if Journal.SearchByType( 'The pet\'s owner must be nearby to attempt the resurrection.', 'Regular' ):
                Misc.SendMessage( 'The pet\'s owner left, cannot continue training Veterinary', colors[ 'red' ] )
                return
            Misc.Pause( 100 )

        Journal.Clear()

        bandages = FindBandage( Player.Backpack )
        if bandages == None:
            Misc.SendMessage( 'Ran out of bandages to train with', colors[ 'red' ] )
            return

        Misc.Pause( 50 )

    if Player.GetRealSkillValue( 'Veterinary' ) == Player.GetSkillCap( 'Veterinary' ):
        Misc.SendMessage( 'Veterinary training complete!', colors[ 'green' ] )

# Start Veterinary training
TrainVeterinary()
