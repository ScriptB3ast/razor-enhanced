'''
Author: TheWarDoctor95
Other Contributors:
Last Contribution By: TheWarDoctor95 - March 14, 2019

Description: Uses the selected target to train Animal Lore to its cap
'''

from Scripts.glossary.colors import colors

animalLoreTimerMilliseconds = 1200

# Select what to run Animal Lore on
animalLoreTarget = Target.PromptTarget( 'Select animal to train on' )
Mobiles.Message( animalLoreTarget, 52, 'Selected for animal lore training' )

def TrainAnimalLore():
    '''
    Trains Animal Lore with the selected target
    '''
    global animalLoreTarget

    Timer.Create( 'animalLoreTimer', 1 )
    targetStillExists = Mobiles.FindBySerial( animalLoreTarget )

    while targetStillExists != None and not Player.IsGhost and Player.GetRealSkillValue( 'Animal Lore' ) < Player.GetSkillCap( 'Animal Lore' ):
        if not Timer.Check( 'animalLoreTimer' ):
            Player.UseSkill( 'Animal Lore' )
            Target.WaitForTarget( 2000, True )
            Target.TargetExecute( animalLoreTarget )
            Timer.Create( 'animalLoreTimer', animalLoreTimerMilliseconds )

    if targetStillExists == None:
        Player.HeadMessage( colors[ 'red' ], 'Selected target for animal lore is gone' )
    elif Player.GetRealSkillValue( 'Animal Lore' ) >= Player.GetSkillCap( 'Animal Lore' ):
        Player.HeadMessage( colors[ 'green' ], 'Animal Lore training complete!' )

# Start Training
TrainAnimalLore()
