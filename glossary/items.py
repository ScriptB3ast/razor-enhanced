from Scripts.glossary.razorEnhancedClassMasterSingleton import MasterSingleton

RazorEnhancedClasses = MasterSingleton()

class myItem:
    name = None
    itemID = None
    color = None
    category = None
    weight = None

    def __init__ ( self, name, itemID, color, category, weight ):
        self.name = name
        self.itemID = itemID
        self.color = color
        self.category = category
        self.weight = weight

items = {
    ### Reagents ###
    'Black Pearl': myItem( 'Black Pearl', 0x0F7A, 0x0000, 'reagent', 0.1 ),
    'Blood Moss': myItem( 'Blood Moss', 0x0F7B, 0x0000, 'reagent', 0.1 ),
    'Garlic': myItem( 'Garlic', 0x0F84, 0x0000, 'reagent', 0.1 ),
    'Ginseng': myItem( 'Ginseng', 0x0F85, 0x0000, 'reagent', 0.1 ),
    'Mandrake Root': myItem( 'Mandrake Root', 0x0F86, 0x0000, 'reagent', 0.1 ),
    'Nightshade': myItem( 'Nightshade', 0x0F88, 0x0000, 'reagent', 0.1 ),
    'Spider\'s Silk': myItem( 'Spider\'s Silk', 0x0F8D, 0x0000, 'reagent', 0.1 ),
    'Sulfurous Ash': myItem( 'Sulfurous Ash', 0x0F8C, 0x0000, 'reagent', 0.1 ),


    ### Slayer Runes ###
    'p rune': myItem( 'p rune', 0x486B, 0x0027, 'slayer rune', 1 ),
    'b rune': None,
    'm rune': None,
    'f rune': myItem( 'f rune', 0x484A, 0x0027, 'slayer rune', 1 ),
    'v rune': myItem( 'v rune', 0x487D, 0x0027, 'slayer rune', 1 ),
    'u rune': None,

    't rune': myItem( 't rune', 0x4877, 0x0027, 'slayer rune', 1 ),
    'd rune': None,
    'n rune': myItem( 'n rune', 0x4868, 0x0027, 'slayer rune', 1 ),
    's rune': myItem( 's rune', 0x4874, 0x0027, 'slayer rune', 1 ),
    'z rune': myItem( 'z rune', 0x4883, 0x0027, 'slayer rune', 1 ),
    'e rune': myItem( 'e rune', 0x4847, 0x0027, 'slayer rune', 1 ),

    'ch rune': myItem( 'ch rune', 0x4841, 0x0027, 'slayer rune', 1 ),
    'j rune': myItem( 'j rune', 0x4856, 0x0027, 'slayer rune', 1 ),
    'sh rune': myItem( 'sh rune', 0x4871, 0x0027, 'slayer rune', 1 ),
    'zh rune': myItem( 'zh rune', 0x4880, 0x0027, 'slayer rune', 1 ),
    'i rune': myItem( 'i rune', 0x4853, 0x0027, 'slayer rune', 1 ),

    'gl rune': myItem( 'gl rune', 0x4859, 0x0027, 'slayer rune', 1 ),
    'l rune': myItem( 'l rune', 0x485F, 0x0027, 'slayer rune', 1 ),

    'k rune': myItem( 'k rune', 0x485C, 0x0027, 'slayer rune', 1 ),
    'g rune': None,
    'ng rune': None,
    'h rune': None,
    'r rune': myItem( 'r rune', 0x486E, 0x0027, 'slayer rune', 1 ),
    'a rune': myItem( 'a rune', 0x483B, 0x0027, 'slayer rune', 1 ),


    ### Statuettes ###
    'dread spider statuette': myItem( 'dread spider statuette', 0x25C4, 0x0000, 'statuette', 1 ),
    'lich statuette': myItem( 'lich statuette', 0x25A4, 0x0000, 'statuette', 1 ),
    'orc shaman statuette': myItem( 'orc shaman statuette', 0x25B1, 0x0000, 'statuette', 1 ),
    'slime statuette': myItem( 'slime statuette', 0x20E8, 0x0000, 'statuette', 1 ),
    'snow elemental statuette': myItem( 'snow elemental statuette', 0x25DC, 0x0000, 'statuette', 1 ),


    ### Tailoring Materials ###
    'cut cloth': myItem( 'cut cloth', 0x1767, 0x07C2, 'tailoring', 10 ),
    'pile of folded besotted cloth': myItem( 'pile of folded besotted cloth', 0x1766, 0x0000, 'tailoring', 1 ),
    'piles of hides': myItem( 'piles of hides', 0x1079, 0x0000, 'tailoring', 10 ),
    'pieces of leather': myItem( 'pieces of leather', 0x1081, 0x0000, 'tailoring', 1 ),


    ### Scrolls ###
    # First Circle
    'Clumsy scroll': myItem( 'Clumsy scroll', 0x1F2E, 0x0000, 'magic scroll', 1 ),
    'Create Food scroll': myItem( 'Create Food scroll', 0x1F2F, 0x0000, 'magic scroll', 1 ),
    'Feeblemind scroll': myItem( 'Feeblemind scroll', 0x1F30, 0x0000, 'magic scroll', 1 ),
    'Heal scroll': myItem( 'Heal scroll', 0x1F31, 0x0000, 'magic scroll', 1 ),
    'Magic Arrow scroll': myItem( 'Magic Arrow scroll', 0x1F32, 0x0000, 'magic scroll', 1 ),
    'Night Sight scroll': myItem( 'Night Sight scroll', 0x1F33, 0x0000, 'magic scroll', 1 ),
    'Reactive Armor scroll': myItem( 'Reactive Armor scroll', 0x1F2D, 0x0000, 'magic scroll', 1 ),
    'Weaken scroll': myItem( 'Weaken scroll', 0x1F34, 0x0000, 'magic scroll', 1 ),

    # Second Circle
    'Agility scroll': myItem( 'Agility scroll', 0x1F35, 0x0000, 'magic scroll', 1 ),
    'Cunning scroll': myItem( 'Cunning scroll', 0x1F36, 0x0000, 'magic scroll', 1 ),
    'Cure scroll': myItem( 'Cure scroll', 0x1F37, 0x0000, 'magic scroll', 1 ),
    'Harm scroll': myItem( 'Harm scroll', 0x1F38, 0x0000, 'magic scroll', 1 ),
    'Magic Trap scroll': myItem( 'Magic Trap scroll', 0x1F39, 0x0000, 'magic scroll', 1 ),
    'Magic Untrap scroll': myItem( 'Magic Untrap scroll', 0x1F3A, 0x0000, 'magic scroll', 1 ),
    'Protection scroll': myItem( 'Protection scroll', 0x1F3B, 0x0000, 'magic scroll', 1 ),
    'Strength scroll': myItem( 'Strength scroll', 0x1F3C, 0x0000, 'magic scroll', 1 ),

    # Third Circle
    'Bless scroll': myItem( 'Bless scroll', 0x1F3D, 0x0000, 'magic scroll', 1 ),
    'Fireball scroll': myItem( 'Fireball scroll', 0x1F3E, 0x0000, 'magic scroll', 1 ),
    'Magic Lock scroll': myItem( 'Magic Lock scroll', 0x1F3F, 0x0000, 'magic scroll', 1 ),
    'Poison scroll': myItem( 'Poison scroll', 0x1F40, 0x0000, 'magic scroll', 1 ),
    'Telekinesis scroll': myItem( 'Telekinesis scroll', 0x1F41, 0x0000, 'magic scroll', 1 ),
    'Teleport scroll': myItem( 'Teleport scroll', 0x1F42, 0x0000, 'magic scroll', 1 ),
    'Unlock scroll': myItem( 'Unlock scroll', 0x1F43, 0x0000, 'magic scroll', 1 ),
    'Wall of Stone scroll': myItem( 'Wall of Stone scroll', 0x1F44, 0x0000, 'magic scroll', 1 ),

    # Fourth Circle
    'Arch Cure scroll': myItem( 'Arch Cure scroll', 0x1F45, 0x0000, 'magic scroll', 1 ),
    'Arch Protection scroll': myItem( 'Arch Protection scroll', 0x1F46, 0x0000, 'magic scroll', 1 ),
    'Curse scroll': myItem( 'Curse scroll', 0x1F47, 0x0000, 'magic scroll', 1 ),
    'Fire Field scroll': myItem( 'Fire Field scroll', 0x1F48, 0x0000, 'magic scroll', 1 ),
    'Greater Heal scroll': myItem( 'Greater Heal scroll', 0x1F49, 0x0000, 'magic scroll', 1 ),
    'Lightning scroll': myItem( 'Lightning scroll', 0x1F4A, 0x0000, 'magic scroll', 1 ),
    'Mana Drain scroll': myItem( 'Mana Drain scroll', 0x1F4B, 0x0000, 'magic scroll', 1 ),
    'Recall scroll': myItem( 'Recall scroll', 0x1F4C, 0x0000, 'magic scroll', 1 ),

    # Fifth Circle
    'Blade Spirits scroll': myItem( 'Blade Spirits scroll', 0x1F4D, 0x0000, 'magic scroll', 1 ),
    'Dispel Field scroll': myItem( 'Dispel Field scroll', 0x1F4E, 0x0000, 'magic scroll', 1 ),
    'Incognito scroll': myItem( 'Incognito scroll', 0x1F4F, 0x0000, 'magic scroll', 1 ),
    'Magic Reflection scroll': myItem( 'Magic Reflection scroll', 0x1F50, 0x0000, 'magic scroll', 1 ),
    'Mind Blast scroll': myItem( 'Mind Blast scroll', 0x1F51, 0x0000, 'magic scroll', 1 ),
    'Paralyze scroll': myItem( 'Paralyze scroll', 0x1F52, 0x0000, 'magic scroll', 1 ),
    'Poison Field scroll': myItem( 'Poison Field scroll', 0x1F53, 0x0000, 'magic scroll', 1 ),
    'Summon Creature scroll': myItem( 'Summon Creature scroll', 0x1F54, 0x0000, 'magic scroll', 1 ),

    # Sixth Circle
    'Dispel scroll': myItem( 'Dispel scroll', 0x1F55, 0x0000, 'magic scroll', 1 ),
    'Energy Bolt scroll': myItem( 'Energy Bolt scroll', 0x1F56, 0x0000, 'magic scroll', 1 ),
    'Explosion scroll': myItem( 'Explosion scroll', 0x1F57, 0x0000, 'magic scroll', 1 ),
    'Invisibility scroll': myItem( 'Invisibility scroll', 0x1F58, 0x0000, 'magic scroll', 1 ),
    'Mark scroll': myItem( 'Mark scroll', 0x1F59, 0x0000, 'magic scroll', 1 ),
    'Mass Curse scroll': myItem( 'Mass Curse scroll', 0x1F5A, 0x0000, 'magic scroll', 1 ),
    'Paralyze Field scroll': myItem( 'Paralyze Field scroll', 0x1F5B, 0x0000, 'magic scroll', 1 ),
    'Reveal scroll': myItem( 'Reveal scroll', 0x1F5C, 0x0000, 'magic scroll', 1 ),

    # Seventh Circle
    'Chain Lightning scroll': myItem( 'Chain Lightning scroll', 0x1F5D, 0x0000, 'magic scroll', 1 ),
    'Energy Field scroll': myItem( 'Energy Field scroll', 0x1F5E, 0x0000, 'magic scroll', 1 ),
    'Flamestrike scroll': myItem( 'Flamestrike scroll', 0x1F5F, 0x0000, 'magic scroll', 1 ),
    'Gate Travel scroll': myItem( 'Gate Travel scroll', 0x1F60, 0x0000, 'magic scroll', 1 ),
    'Mana Vampire scroll': myItem( 'Mana Vampire scroll', 0x1F61, 0x0000, 'magic scroll', 1 ),
    'Mass Dispel scroll': myItem( 'Mass Dispel scroll', 0x1F62, 0x0000, 'magic scroll', 1 ),
    'Meteor Swarm scroll': myItem( 'Meteor Swarm scroll', 0x1F63, 0x0000, 'magic scroll', 1 ),
    'Polymorph scroll': myItem( 'Polymorph scroll', 0x1F64, 0x0000, 'magic scroll', 1 ),

    # Eighth Circle
    'Earthquake scroll': myItem( 'Earthquake scroll', 0x1F65, 0x0000, 'magic scroll', 1 ),
    'Energy Vortex scroll': myItem( 'Energy Vortex scroll', 0x1F66, 0x0000, 'magic scroll', 1 ),
    'Resurrection scroll': myItem( 'Resurrection scroll', 0x1F67, 0x0000, 'magic scroll', 1 ),
    'Summon Air Elemental scroll': myItem( 'Summon Air Elemental scroll', 0x1F68, 0x0000, 'magic scroll', 1 ),
    'Summon Daemon scroll': myItem( 'Summon Daemon scroll', 0x1F69, 0x0000, 'magic scroll', 1 ),
    'Summon Earth Elemental scroll': myItem( 'Summon Earth Elemental scroll', 0x1F6A, 0x0000, 'magic scroll', 1 ),
    'Summon Fire Elemental scroll': myItem( 'Summon Fire Elemental scroll', 0x1F6B, 0x0000, 'magic scroll', 1 ),
    'Summon Water Elemental scroll': myItem( 'Summon Water Elemental scroll', 0x1F6C, 0x0000, 'magic scroll', 1 ),

    ### Tools ###
    'disguise kit': myItem( 'disguise kit', 0x0E05, 0x0000, 'tool', None ),
    'dovetail saw': myItem( 'dovetail saw', 0x1028, 0x0000, 'tool', None ),
    'dyes': myItem( 'dyes', 0x0FA9, 0x0000, 'tool', None ),
    'dyeing tub': myItem( 'dyeing tub', 0x0FAB, 0x0000, 'tool', None ),
    'gargoyle\'s pickaxe': myItem( 'gargoyle\'s pickaxe', 0x0E86, 0x0430, 'tool', 11 ),
    'interior decorator': myItem( 'interior decorator', 0x0FC1, 0x0000, 'tool', 11 ),
    'lockpick': myItem( 'lockpick', 0x14FC, 0x0000, 'tool', 11 ),
    'pickaxe': myItem( 'pickaxe', 0x0E86, 0x0000, 'tool', 11 ),
    'prospector\'s tool': myItem( 'prospector\'s tool', 0x0FB4, 0x0000, 'tool', 11 ),
    'sturdy pickaxe': myItem( 'pickaxe', 0x0E86, 0x0973, 'tool', 11 ),

    # Runic Hammers
    'agapite runic hammer': myItem( 'agapite runic hammer', 0x13E3, 0x097E, 'tool', 8 ),
    'bronze runic hammer': myItem( 'bronze runic hammer', 0x13E3, 0x06D8, 'tool', 8 ),
    'copper runic hammer': myItem( 'copper runic hammer', 0x13E3, 0x045F, 'tool', 8 ),
    'dull copper runic hammer': myItem( 'dull copper runic hammer', 0x13E3, 0x0415, 'tool', 8 ),
    'golden runic hammer': myItem( 'golden runic hammer', 0x13E3, 0x06B7, 'tool', 8 ),
    'shadow iron runic hammer': myItem( 'shadow iron runic hammer', 0x13E3, 0x0455, 'tool', 8 ),
    'verite runic hammer': myItem( 'verite runic hammer', 0x13E3, 0x07D2, 'tool', 8 ),
    'valorite runic hammer': myItem( 'valorite runic hammer', 0x13E3, 0x0544, 'tool', 8 ),

    'sledge hammer': myItem( 'sledge hammer', 0x0FB5, 0x0000, 'tool', 10 ),
    'smith\'s hammer': myItem( 'smith\'s hammer', 0x13E3, 0x0000, 'tool', 8 ),
    'tinker\'s tools': myItem( 'tinker\'s tools', 0x1EBC, 0x0000, 'tool', 1 ),
    'tongs': myItem( 'tongs', 0x0FBB, 0x0000, 'tool', 2 ),
    'tool kit': myItem( 'tool kit', 0x1EB8, 0x0000, 'tool', 1 )
}

instruments = { itemName: item for itemName, item in items.items() if item != None and item.category == 'instrument' }
moongates = { itemName: item for itemName, item in items.items() if item != None and item.category == 'moongate' }
ores = { itemName: item for itemName, item in items.items() if item != None and item.category == 'ore' }
reagents = { itemName: item for itemName, item in items.items() if item != None and item.category == 'reagent' }
tools = { itemName: item for itemName, item in items.items() if item != None and item.category == 'tool' }


def AddRazorEnhancedClassesToModule( AutoLoot, BandageHeal, BuyAgent, DPSMeter, Dress, Friend,
        Items, Journal, Misc, Mobiles, Organizer, PathFinding, Player, Restock,
        Scavenger, SellAgent, Spells, Statics, Target, Timer ):
    RazorEnhancedClasses.PopulateClasses( AutoLoot, BandageHeal, BuyAgent, DPSMeter, Dress, Friend,
        Items, Journal, Misc, Mobiles, Organizer, PathFinding, Player, Restock,
        Scavenger, SellAgent, Spells, Statics, Target, Timer )
    return


def FindItem( itemID, container, color = -1, ignoreContainer = [] ):
    '''
    Searches through the container for the item IDs specified and returns the first one found
    Also searches through any subcontainers, which Misc.FindByID() does not
    '''

    ignoreColor = False
    if color == -1:
        ignoreColor = True

    if isinstance( itemID, int ):
        foundItem = next( ( item for item in container.Contains if ( item.ItemID == itemID and ( ignoreColor or item.Hue == color ) ) ), None )
    elif isinstance( itemID, list ):
        foundItem = next( ( item for item in container.Contains if ( item.ItemID in itemID and ( ignoreColor or item.Hue == color ) ) ), None )
    else:
        raise ValueError( 'Unknown argument type for itemID passed to FindItem().', itemID, container )

    if foundItem != None:
        return foundItem

    subcontainers = [ item for item in container.Contains if ( item.IsContainer and not item.Serial in ignoreContainer ) ]
    for subcontainer in subcontainers:
        foundItem = FindItem( itemID, subcontainer, color, ignoreContainer )
        if foundItem != None:
            return foundItem


def FindNumberOfItems( itemID, container, color = -1 ):
    '''
    Recursively looks through a container for any items in the provided list
    Returns the a dictionary with the number of items found from the list
    '''

    ignoreColor = False
    if color == -1:
        ignoreColor = True

    # Create the dictionary
    numberOfItems = {}

    if isinstance( itemID, int ):
        # Initialize numberOfItems
        numberOfItems[ itemID ] = 0

        # Populate numberOfItems
        for item in container.Contains:
            if item.ItemID == itemID and ( ignoreColor or item.Hue == color ):
                numberOfItems[ itemID ] += item.Amount
    elif isinstance( itemID, list ):
        # Initialize numberOfItems
        for ID in itemID:
            numberOfItems[ ID ] = 0

        # Populate numberOfItems
        for item in container.Contains:
            if item.ItemID in itemID and ( ignoreColor or item.Hue == color ):
                numberOfItems[ item.ItemID ] += item.Amount
    else:
        raise ValueError( 'Unknown argument type for itemID passed to FindItem().', itemID, container )

    subcontainers = [ item for item in container.Contains if item.IsContainer ]

    # Iterate through each item in the given list
    for subcontainer in subcontainers:
        numberOfItemsInSubcontainer = FindNumberOfItems( itemID, subcontainer )
        for ID in numberOfItems:
            numberOfItems[ ID ] += numberOfItemsInSubcontainer[ ID ]

    return numberOfItems


def MoveItem( item, destinationBag, amount = 0 ):
    RazorEnhancedClasses.Items.Move( item, destinationBag, amount )

    # Wait for the move to complete
    RazorEnhancedClasses.Misc.Pause( 600 )
