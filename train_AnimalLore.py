'''
Author: TheWarDoctor95
Other Contributors:
Last Contribution By: TheWarDoctor95 - March 14, 2019

Description: Uses the selected target to train Animal Lore to GM
'''

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

    while Player.GetSkillValue( 'Animal Lore' ) < 100 and targetStillExists != None and not Player.IsGhost:
        if not Timer.Check( 'animalLoreTimer' ):
            Player.UseSkill( 'Animal Lore' )
            Target.WaitForTarget( 10000, False )
            Target.TargetExecute( animalLoreTarget )
            Timer.Create( 'animalLoreTimer', animalLoreTimerMilliseconds )

    if targetStillExists == None:
        Player.HeadMessage( 1100, 'Selected target for animal lore is gone' )
    elif Player.GetSkillValue( 'Animal Lore' ) >= 100:
        Player.HeadMessage( 32, 'Animal Lore training complete!' )
    else:
        Player.HeadMessage( 0, 'Something happened.' )

# Start Training
TrainAnimalLore()
