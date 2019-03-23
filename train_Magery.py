'''
Author: TheWarDoctor95
Other Contributors:
Last Contribution By: TheWarDoctor95 - March 13, 2019

Description: Uses the recommended spells from the UO Forever Wiki (https://www.uoforum.com/wiki/index.php/Magery)
    to level Magery to GM. Will also increase Meditation if the skill is set to Up and not maxed out while running
'''

mageryTimerMilliseconds = 6500

class Reagent:
    name = ''
    itemType = 0x0

    def __init__ ( self, name, itemType ):
        self.name = name
        self.itemType = itemType

reagents = {
    'Black Pearl': Reagent( 'Black Pearl', 0x0F7A ),
    'Blood Moss': Reagent( 'Blood Moss', 0x0F7B ),
    'Garlic': Reagent( 'Garlic', 0x0F84 ),
    'Ginseng': Reagent( 'Ginseng', 0x0F85 ),
    'Mandrake Root': Reagent( 'Mandrake Root', 0x0F86 ),
    'Nightshade': Reagent( 'Nightshade', 0x0F88 ),
    'Spider\'s Silk': Reagent( 'Spider\'s Silk', 0x0F8D ),
    'Sulfurous Ash': Reagent( 'Sulfurous Ash', 0x0F8C )
}

spellReagents = {
    # First Circle
    'Clumsy': [
        reagents[ 'Blood Moss' ],
        reagents[ 'Nightshade' ]
    ],
    'Create Food': [
        reagents[ 'Garlic' ],
        reagents[ 'Ginseng' ],
        reagents[ 'Mandrake Root' ]
    ],
    'Feeblemind': [
        reagents[ 'Ginseng' ],
        reagents[ 'Nightshade' ]
    ],
    'Heal': [
        reagents[ 'Garlic' ],
        reagents[ 'Ginseng' ],
        reagents[ 'Spider\'s Silk' ]
    ],
    'Magic Arrow': [
        reagents[ 'Sulfurous Ash' ]
    ],
    'Night Sight': [
        reagents[ 'Spider\'s Silk' ],
        reagents[ 'Sulfurous Ash' ]
    ],
    'Reactive Armor': [
        reagents[ 'Garlic' ],
        reagents[ 'Spider\'s Silk' ],
        reagents[ 'Sulfurous Ash' ]
    ],
    'Weaken': [
        reagents[ 'Garlic' ],
        reagents[ 'Nightshade' ]
    ],

    # Second Circle
    'Agility': [
        reagents[ 'Blood Moss' ],
        reagents[ 'Mandrake Root' ]
    ],
    'Cunning': [
        reagents[ 'Mandrake Root' ],
        reagents[ 'Nightshade' ]
    ],
    'Cure': [
        reagents[ 'Garlic' ],
        reagents[ 'Ginseng' ]
    ],
    'Harm': [
        reagents[ 'Nightshade' ],
        reagents[ 'Spider\'s Silk' ]
    ],
    'Magic Trap': [
        reagents[ 'Garlic' ],
        reagents[ 'Spider\'s Silk' ],
        reagents[ 'Sulfurous Ash' ]
    ],
    'Magic Untrap': [
        reagents[ 'Blood Moss' ],
        reagents[ 'Sulfurous Ash' ]
    ],
    'Protection': [
        reagents[ 'Garlic' ],
        reagents[ 'Ginseng' ],
        reagents[ 'Sulfurous Ash' ]
    ],
    'Strength': [
        reagents[ 'Mandrake Root' ],
        reagents[ 'Nightshade' ]
    ],

    # Third Circle
    'Bless': [
        reagents[ 'Garlic' ],
        reagents[ 'Mandrake Root' ]
    ],
    'Fireball': [
        reagents[ 'Black Pearl' ]
    ],
    'Magic Lock': [
        reagents[ 'Blood Moss' ],
        reagents[ 'Garlic' ],
        reagents[ 'Sulfurous Ash' ]
    ],
    'Poison': [
        reagents[ 'Nightshade' ]
    ],
    'Telekinesis': [
        reagents[ 'Blood Moss' ],
        reagents[ 'Mandrake Root' ]
    ],
    'Teleport': [
        reagents[ 'Blood Moss' ],
        reagents[ 'Mandrake Root' ]
    ],
    'Unlock': [
        reagents[ 'Blood Moss' ],
        reagents[ 'Sulfurous Ash' ]
    ],
    'Wall of Stone': [
        reagents[ 'Blood Moss' ],
        reagents[ 'Garlic' ]
    ],

    # Fourth Circle
    'Arch Cure': [
        reagents[ 'Garlic' ],
        reagents[ 'Ginseng' ],
        reagents[ 'Mandrake Root' ]
    ],
    'Arch Protection': [
        reagents[ 'Garlic' ],
        reagents[ 'Ginseng' ],
        reagents[ 'Mandrake Root' ],
        reagents[ 'Sulfurous Ash' ]
    ],
    'Curse': [
        reagents[ 'Garlic' ],
        reagents[ 'Nightshade' ],
        reagents[ 'Sulfurous Ash' ]
    ],
    'Fire Field': [
        reagents[ 'Black Pearl' ],
        reagents[ 'Spider\'s Silk' ],
        reagents[ 'Sulfurous Ash' ]
    ],
    'Greater Heal': [
        reagents[ 'Garlic' ],
        reagents[ 'Ginseng' ],
        reagents[ 'Mandrake Root' ],
        reagents[ 'Spider\'s Silk' ]
    ],
    'Lightning': [
        reagents[ 'Mandrake Root' ],
        reagents[ 'Sulfurous Ash' ]
    ],
    'Mana Drain': [
        reagents[ 'Black Pearl' ],
        reagents[ 'Mandrake Root' ],
        reagents[ 'Spider\'s Silk' ]
    ],
    'Recall': [
        reagents[ 'Black Pearl' ],
        reagents[ 'Blood Moss' ],
        reagents[ 'Mandrake Root' ]
    ],

    # Fifth Circle
    'Blade Spirits': [
        reagents[ 'Black Pearl' ],
        reagents[ 'Mandrake Root' ],
        reagents[ 'Nightshade' ]
    ],
    'Dispel Field': [
        reagents[ 'Black Pearl' ],
        reagents[ 'Garlic' ],
        reagents[ 'Spider\'s Silk' ],
        reagents[ 'Sulfurous Ash' ]
    ],
    'Incognito': [
        reagents[ 'Blood Moss' ],
        reagents[ 'Garlic' ],
        reagents[ 'Nightshade' ]
    ],
    'Magic Reflection': [
        reagents[ 'Garlic' ],
        reagents[ 'Mandrake Root' ],
        reagents[ 'Spider\'s Silk' ]
    ],
    'Mind Blast': [
        reagents[ 'Black Pearl' ],
        reagents[ 'Mandrake Root' ],
        reagents[ 'Nightshade' ],
        reagents[ 'Sulfurous Ash' ]
    ],
    'Paralyze': [
        reagents[ 'Garlic' ],
        reagents[ 'Mandrake Root' ],
        reagents[ 'Spider\'s Silk' ]
    ],
    'Poison Field': [
        reagents[ 'Black Pearl' ],
        reagents[ 'Nightshade' ],
        reagents[ 'Spider\'s Silk' ]
    ],
    'Summon Creature': [
        reagents[ 'Blood Moss' ],
        reagents[ 'Mandrake Root' ],
        reagents[ 'Spider\'s Silk' ]
    ],

    # Sixth Circle
    'Dispel': [
        reagents[ 'Garlic' ],
        reagents[ 'Mandrake Root' ],
        reagents[ 'Sulfurous Ash' ]
    ],
    'Energy Bolt': [
        reagents[ 'Black Pearl' ],
        reagents[ 'Nightshade' ]
    ],
    'Explosion': [
        reagents[ 'Blood Moss' ],
        reagents[ 'Mandrake Root' ]
    ],
    'Invisibility': [
        reagents[ 'Blood Moss' ],
        reagents[ 'Nightshade' ]
    ],
    'Mark': [
        reagents[ 'Black Pearl' ],
        reagents[ 'Blood Moss' ],
        reagents[ 'Mandrake Root' ]
    ],
    'Mass Curse': [
        reagents[ 'Garlic' ],
        reagents[ 'Mandrake Root' ],
        reagents[ 'Nightshade' ],
        reagents[ 'Sulfurous Ash' ]
    ],
    'Paralyze Field': [
        reagents[ 'Black Pearl' ],
        reagents[ 'Ginseng' ],
        reagents[ 'Spider\'s Silk' ]
    ],
    'Reveal': [
        reagents[ 'Blood Moss' ],
        reagents[ 'Sulfurous Ash' ]
    ],

    # Seventh Circle
    'Chain Lightning': [
        reagents[ 'Black Pearl' ],
        reagents[ 'Blood Moss' ],
        reagents[ 'Mandrake Root' ],
        reagents[ 'Sulfurous Ash' ]
    ],
    'Energy Field': [
        reagents[ 'Black Pearl' ],
        reagents[ 'Mandrake Root' ],
        reagents[ 'Spider\'s Silk' ],
        reagents[ 'Sulfurous Ash' ]
    ],
    'Flamestrike': [
        reagents[ 'Spider\'s Silk' ],
        reagents[ 'Sulfurous Ash' ]
    ],
    'Gate Travel': [
        reagents[ 'Black Pearl' ],
        reagents[ 'Mandrake Root' ],
        reagents[ 'Sulfurous Ash' ]
    ],
    'Mana Vampire': [
        reagents[ 'Black Pearl' ],
        reagents[ 'Blood Moss' ],
        reagents[ 'Mandrake Root' ],
        reagents[ 'Spider\'s Silk' ]
    ],
    'Mass Dispel': [
        reagents[ 'Black Pearl' ],
        reagents[ 'Garlic' ],
        reagents[ 'Mandrake Root' ],
        reagents[ 'Sulfurous Ash' ]
    ],
    'Meteor Swarm': [
        reagents[ 'Blood Moss' ],
        reagents[ 'Mandrake Root' ],
        reagents[ 'Spider\'s Silk' ],
        reagents[ 'Sulfurous Ash' ]
    ],
    'Polymorph': [
        reagents[ 'Blood Moss' ],
        reagents[ 'Mandrake Root' ],
        reagents[ 'Spider\'s Silk' ]
    ],

    # Eighth Circle
    'Earthquake': [
        reagents[ 'Blood Moss' ],
        reagents[ 'Ginseng' ],
        reagents[ 'Mandrake Root' ],
        reagents[ 'Sulfurous Ash' ]
    ],
    'Energy Vortex': [
        reagents[ 'Black Pearl' ],
        reagents[ 'Blood Moss' ],
        reagents[ 'Mandrake Root' ],
        reagents[ 'Nightshade' ]
    ],
    'Resurrection': [
        reagents[ 'Blood Moss' ],
        reagents[ 'Garlic' ],
        reagents[ 'Ginseng' ]
    ],
    'Summon Air Elemental': [
        reagents[ 'Blood Moss' ],
        reagents[ 'Mandrake Root' ],
        reagents[ 'Spider\'s Silk' ]
    ],
    'Summon Daemon': [
        reagents[ 'Blood Moss' ],
        reagents[ 'Mandrake Root' ],
        reagents[ 'Spider\'s Silk' ],
        reagents[ 'Sulfurous Ash' ]
    ],
    'Summon Earth Elemental': [
        reagents[ 'Blood Moss' ],
        reagents[ 'Mandrake Root' ],
        reagents[ 'Spider\'s Silk' ]
    ],
    'Summon Fire Elemental': [
        reagents[ 'Blood Moss' ],
        reagents[ 'Mandrake Root' ],
        reagents[ 'Spider\'s Silk' ],
        reagents[ 'Sulfurous Ash' ]
    ],
    'Summon Water Elemental': [
        reagents[ 'Blood Moss' ],
        reagents[ 'Mandrake Root' ],
        reagents[ 'Spider\'s Silk' ],
    ],
}

class SpellInfo:
    name = ''
    circle = 0
    reagents = []
    manaCost = 0.0
    minSkill = 0
    delayInS = 0.0
    delayInMs = 0

    def __init__ ( self, name, circle, reagents, manaCost, minSkill, delayInS, delayInMs ):
        self.name = name
        self.circle = circle
        self.reagents = reagents
        self.manaCost = manaCost
        self.minSkill = minSkill
        self.delayInS = delayInS
        self.delayInMs = delayInMs

spellInfo = {
    # First Circle
    'Clumsy': SpellInfo( 'Clumsy', 1, spellReagents[ 'Clumsy' ], 4, 0.0, 0.5, 500 ),
    'Create Food': SpellInfo( 'Create Food', 1, spellReagents[ 'Create Food' ], 4, 0.0, 0.5, 500 ),
    'Feeblemind': SpellInfo( 'Feeblemind', 1, spellReagents[ 'Feeblemind' ], 4, 0.0, 0.5, 500 ),
    'Heal': SpellInfo( 'Heal', 1, spellReagents[ 'Heal' ], 4, 0.0, 0.5, 500 ),
    'Magic Arrow': SpellInfo( 'Magic Arrow', 1, spellReagents[ 'Magic Arrow' ], 4, 0.0, 0.5, 500 ),
    'Night Sight': SpellInfo( 'Night Sight', 1, spellReagents[ 'Night Sight' ], 4, 0.0, 0.5, 500 ),
    'Reactive Armor': SpellInfo( 'Reactive Armor', 1, spellReagents[ 'Reactive Armor' ], 4, 0.0, 0.5, 500 ),
    'Weaken': SpellInfo( 'Weaken', 1, spellReagents[ 'Weaken' ], 4, 0.0, 0.5, 500 ),

    # Second Circle
    'Agility': SpellInfo( 'Agility', 2, spellReagents[ 'Agility' ], 6, 0.0, 0.75, 750 ),
    'Cunning': SpellInfo( 'Cunning', 2, spellReagents[ 'Cunning' ], 6, 0.0, 0.75, 750 ),
    'Cure': SpellInfo( 'Cure', 2, spellReagents[ 'Cure' ], 6, 0.0, 0.75, 750 ),
    'Harm': SpellInfo( 'Harm', 2, spellReagents[ 'Harm' ], 6, 0.0, 0.75, 750 ),
    'Magic Trap': SpellInfo( 'Magic Trap', 2, spellReagents[ 'Magic Trap' ], 6, 0.0, 0.75, 750 ),
    'Magic Untrap': SpellInfo( 'Magic Untrap', 2, spellReagents[ 'Magic Untrap' ], 6, 0.0, 0.75, 750 ),
    'Protection': SpellInfo( 'Protection', 2, spellReagents[ 'Protection' ], 6, 0.0, 0.75, 750 ),
    'Strength': SpellInfo( 'Strength', 2, spellReagents[ 'Strength' ], 6, 0.0, 0.75, 750 ),

    # Third Circle
    'Bless': SpellInfo( 'Bless', 3, spellReagents[ 'Bless' ], 9, 9.0, 1.0, 1000 ),
    'Fireball': SpellInfo( 'Fireball', 3, spellReagents[ 'Fireball' ], 9, 9.0, 1.0, 1000 ),
    'Magic Lock': SpellInfo( 'Magic Lock', 3, spellReagents[ 'Magic Lock' ], 9, 9.0, 1.0, 1000 ),
    'Poison': SpellInfo( 'Poison', 3, spellReagents[ 'Poison' ], 9, 9.0, 1.0, 1000 ),
    'Telekinesis': SpellInfo( 'Telekinesis', 3, spellReagents[ 'Telekinesis' ], 9, 9.0, 1.0, 1000 ),
    'Teleport': SpellInfo( 'Teleport', 3, spellReagents[ 'Teleport' ], 9, 9.0, 1.0, 1000 ),
    'Unlock': SpellInfo( 'Unlock', 3, spellReagents[ 'Unlock' ], 9, 9.0, 1.0, 1000 ),
    'Wall of Stone': SpellInfo( 'Wall of Stone', 3, spellReagents[ 'Wall of Stone' ], 9, 9.0, 1.0, 1000 ),

    # Fourth Circle
    'Arch Cure': SpellInfo( 'Arch Cure', 4, spellReagents[ 'Arch Cure' ], 11, 24.0, 1.25, 1250 ),
    'Arch Protection': SpellInfo( 'Arch Protection', 4, spellReagents[ 'Arch Protection' ], 11, 24.0, 1.25, 1250 ),
    'Curse': SpellInfo( 'Curse', 4, spellReagents[ 'Curse' ], 11, 24.0, 1.25, 1250 ),
    'Fire Field': SpellInfo( 'Fire Field', 4, spellReagents[ 'Fire Field' ], 11, 24.0, 1.25, 1250 ),
    'Greater Heal': SpellInfo( 'Greater Heal', 4, spellReagents[ 'Greater Heal' ], 11, 24.0, 1.25, 1250 ),
    'Lightning': SpellInfo( 'Lightning', 4, spellReagents[ 'Lightning' ], 11, 24.0, 1.25, 1250 ),
    'Mana Drain': SpellInfo( 'Mana Drain', 4, spellReagents[ 'Mana Drain' ], 11, 24.0, 1.25, 1250 ),
    'Recall': SpellInfo( 'Recall', 4, spellReagents[ 'Recall' ], 11, 24.0, 1.25, 1250 ),

    # Fifth Circle
    'Blade Spirits': SpellInfo( 'Blade Spirits', 5, spellReagents[ 'Blade Spirits' ], 14, 38.0, 6.0, 6000 ),
    'Dispel Field': SpellInfo( 'Dispel Field', 5, spellReagents[ 'Dispel Field' ], 14, 38.0, 1.5, 1500 ),
    'Incognito': SpellInfo( 'Incognito', 5, spellReagents[ 'Incognito' ], 14, 38.0, 1.5, 1500 ),
    'Magic Reflection': SpellInfo( 'Magic Reflection', 5, spellReagents[ 'Magic Reflection' ], 14, 38.0, 1.5, 1500 ),
    'Mind Blast': SpellInfo( 'Mind Blast', 5, spellReagents[ 'Mind Blast' ], 14, 38.0, 1.5, 1500 ),
    'Paralyze': SpellInfo( 'Paralyze', 5, spellReagents[ 'Paralyze' ], 14, 38.0, 1.5, 1500 ),
    'Poison Field': SpellInfo( 'Poison Field', 5, spellReagents[ 'Poison Field' ], 14, 38.0, 1.5, 1500 ),
    'Summon Creature': SpellInfo( 'Summon Creature', 5, spellReagents[ 'Summon Creature' ], 14, 38.0, 6.0, 6000 ),

    # Sixth Circle
    'Dispel': SpellInfo( 'Dispel', 6, spellReagents[ 'Dispel' ], 20, 52.0, 1.75, 1750 ),
    'Energy Bolt': SpellInfo( 'Energy Bolt', 6, spellReagents[ 'Energy Bolt' ], 20, 52.0, 1.75, 1750 ),
    'Explosion': SpellInfo( 'Explosion', 6, spellReagents[ 'Explosion' ], 20, 52.0, 1.75, 1750 ),
    'Invisibility': SpellInfo( 'Invisibility', 6, spellReagents[ 'Invisibility' ], 20, 52.0, 1.75, 1750 ),
    'Mark': SpellInfo( 'Mark', 6, spellReagents[ 'Mark' ], 20, 52.0, 1.75, 1750 ),
    'Mass Curse': SpellInfo( 'Mass Curse', 6, spellReagents[ 'Mass Curse' ], 20, 52.0, 1.75, 1750 ),
    'Paralyze Field': SpellInfo( 'Paralyze Field', 6, spellReagents[ 'Paralyze Field' ], 20, 52.0, 1.75, 1750 ),
    'Reveal': SpellInfo( 'Reveal', 6, spellReagents[ 'Reveal' ], 20, 52.0, 1.75, 1750 ),

    # Seventh Circle
    'Chain Lightning': SpellInfo( 'Chain Lightning', 7, spellReagents[ 'Chain Lightning' ], 40, 67.0, 2.0, 2000 ),
    'Energy Field': SpellInfo( 'Energy Field', 7, spellReagents[ 'Energy Field' ], 40, 67.0, 2.0, 2000 ),
    'Flamestrike': SpellInfo( 'Flamestrike', 7, spellReagents[ 'Flamestrike' ], 40, 67.0, 2.0, 2000 ),
    'Gate Travel': SpellInfo( 'Gate Travel', 7, spellReagents[ 'Gate Travel' ], 40, 67.0, 2.0, 2000 ),
    'Mana Vampire': SpellInfo( 'Mana Vampire', 7, spellReagents[ 'Mana Vampire' ], 40, 67.0, 2.0, 2000 ),
    'Mass Dispel': SpellInfo( 'Mass Dispel', 7, spellReagents[ 'Mass Dispel' ], 40, 67.0, 2.0, 2000 ),
    'Meteor Swarm': SpellInfo( 'Meteor Swarm', 7, spellReagents[ 'Meteor Swarm' ], 40, 67.0, 2.0, 2000 ),
    'Polymorph': SpellInfo( 'Polymorph', 7, spellReagents[ 'Polymorph' ], 40, 67.0, 2.0, 2000 ),

    # Eighth Circle
    'Earthquake': SpellInfo( 'Earthquake', 8, spellReagents[ 'Earthquake' ], 50, 81.0, 2.25, 2250 ),
    'Energy Vortex': SpellInfo( 'Energy Vortex', 8, spellReagents[ 'Energy Vortex' ], 50, 81.0, 2.25, 2250 ),
    'Resurrection': SpellInfo( 'Resurrection', 8, spellReagents[ 'Resurrection' ], 50, 81.0, 2.25, 2250 ),
    'Summon Air Elemental': SpellInfo( 'Summon Air Elemental', 8, spellReagents[ 'Summon Air Elemental' ], 50, 81.0, 2.25, 2250 ),
    'Summon Daemon': SpellInfo( 'Summon Daemon', 8, spellReagents[ 'Summon Daemon' ], 50, 81.0, 2.25, 2250 ),
    'Summon Earth Elemental': SpellInfo( 'Summon Earth Elemental', 8, spellReagents[ 'Summon Earth Elemental' ], 50, 81.0, 2.25, 2250 ),
    'Summon Fire Elemental': SpellInfo( 'Summon Fire Elemental', 8, spellReagents[ 'Summon Fire Elemental' ], 50, 81.0, 2.25, 2250 ),
    'Summon Water Elemental': SpellInfo( 'Summon Water Elemental', 8, spellReagents[ 'Summon Water Elemental' ], 50, 81.0, 2.25, 2250 )
}


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
