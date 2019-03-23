'''
Author: TheWarDoctor95
Other Contributors:
Last Contribution By: TheWarDoctor95 - March 13, 2019

Description: Uses the recommended spells from the UO Forever Wiki (https://www.uoforum.com/wiki/index.php/Magery)
    to level Magery to GM. Will also increase Meditation if the skill is set to Up and not maxed out while running
'''

from Scripts.glossary.spells import reagents, spells

mageryTimerMilliseconds = 6500


def FindReagents():
    '''
    Uses FindItem to find an the reagents in the player's backpack
    Returns a dictionary of the reagents found
    '''
    global reagents
    reagentItemTypes = []
    for reagent in reagents:
        reagentItemTypes.append( reagents[ reagent ].itemType )
    numberOfReagentsFound = FindNumberOfItems( reagentItemTypes, Player.Backpack.Contains )
    return numberOfReagentsFound


def CheckReagents( spellName ):
    '''
    Checks if the necessary reagents are available in the player's backpack to use a spell
    '''
    global spellInfo
    reagentsInBackpack = FindReagents()
    reagentsNeeded = spellInfo[ spellName ].reagents
    for reagent in reagentsNeeded:
        if reagentsInBackpack[ reagent.itemType ] == 0:
            return False
    return True


def TrainMagery():
    '''
    Trains Magery by casting spells on the player
    Stops training if the player runs out of the necessary reagents
    '''
    global mageryTimerMilliseconds

    Timer.Create( 'mageryTimer', 1 )

    while Player.GetSkillValue( 'Magery' ) < 100 and not Player.IsGhost:
        if not Timer.Check( 'mageryTimer' ):
            if Player.GetSkillValue( 'Magery' ) < 62.8:
                spell = spellInfo[ 'Mana Drain' ]
            elif Player.GetSkillValue( 'Magery' ) < 75.5:
                spell = spellInfo[ 'Invisibility' ]
            else:
                spell = spellInfo[ 'Mana Vampire' ]

            if not CheckReagents( spell.name ):
                reagentsNeeded = spell.reagents
                reagentsNeededAsString = ''
                for reagent in reagentsNeeded:
                    reagentsNeededAsString += reagent.name + ','
                reagentsNeededAsString[ : -1 ] # Removes the extra comma from the string
                Misc.SendMessage( 'Ran out of regs for %s! These regs are needed: %s' % ( spell.name, reagentsNeededAsString ), 1100 )
                break

            if not Timer.Check( 'mageryTimer' ) and Player.Mana > spell.manaCost:
                #Spells.CastMagery( spell.name )
                Misc.SendMessage( 'cast %s' % spell.name )
                Timer.Create( 'mageryTimer', spell.delayInMs + 100 ) # wait an extra 100 ms in case of latency
            elif not CheckReagents( spell.name ):
                Misc.SendMessage()

            # Target the cast spell on the player
            Target.WaitForTarget( 10000, False )
            Target.TargetExecute( Player.Serial )
            Timer.Create( 'mageryTimer', mageryTimerMilliseconds )

# Start the training
TrainMagery()
