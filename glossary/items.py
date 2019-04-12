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
    ### Body Parts ###
    'bone pile': myItem( 'bone pile', 0x1B10, 0x0000, 'body part', 10 ),
    'bone shards': myItem( 'bone shards', 0x1B1A, 0x0000, 'body part', 1 ),
    'bones of a temptress': myItem( 'bones of a temptress', 0x1B10, 0x0A4D, 'body part', 10 ),
    'dragon bone shards': myItem( 'dragon bone shards', 0x1B1A, 0x09C2, 'body part', 1 ),
    'dragon scales': myItem( 'dragon scales', 0x26B4, 0x0000, 'body part', 0.1 ),
    'dragon scales (red)': myItem( 'dragon scales (red)', 0x26B4, 0x066D, 'body part', 0.1 ),
    'dragon scales (blue)': myItem( 'dragon scales (blue)', 0x26B4, 0x08B0, 'body part', 0.1 ),
    'dragon scales (golden)': myItem( 'dragon scales (golden)', 0x26B4, 0x08A8, 'body part', 0.1 ),
    'intact dragon\'s heart': myItem( 'intact dragon\'s heart', 0x2808, 0x0A9E, 'body part', 1 ),
    'skull': myItem( 'skull', 0x1AE1, 0x0000, 'body part', 1 ),


    ### Clothing ###
    # Anniversary
    '6th Year Forever Shirt': myItem( '6th Year Forever Shirt', 0x25EB, 0x0799, 'clothing', 1 ),
    'UOForever\'s 6th Year Anniversary': myItem( 'UOForever\'s 6th Year Anniversary', 0x2B6E, 0x0000, 'decoration', 1 ),

    # Christmas
    'jingle bells necklace': myItem( 'jingle bells necklace', 0x4D0A, 0x0501, 'decoration', 1 ),

    'checkered shirt': myItem( 'checkered shirt', 0x25EB, 0x0000, 'clothing', 1 ),
    'full apron': myItem( 'full apron', 0x153D, 0x0000, 'clothing', 4 ),
    'gargish necklace': myItem( 'gargish necklace', 0x4D0A, 0x0000, 'clothing', 1 ),
    'Kiss the Cook apron': myItem( 'Kiss the Cook apron', 0x153D, 0x0844, 'clothing', 4 ),


    ### Containers ###
    'backpack': myItem( 'backpack', 0x0E75, 0x0000, 'container', 1 ),
    'bag': myItem( 'bag', 0x0E76, 0x0000, 'container', 1 ),
    'barrel': myItem( 'barrel', 0x0E77, 0x0000, 'container', 1 ),
    'crate': myItem( 'crate', 0x0E7E, 0x0000, 'container', 1 ),
    'metal chest (east/west)': myItem( 'metal chest', 0x0E7C, 0x0000, 'container', 1 ),
    'metal chest (north/south)': myItem( 'metal chest', 0x2DF3, 0x0000, 'container', 1 ),
    'ornate elven chest': myItem( 'ornate elven chest', 0x0E79, 0x0000, 'container', 1 ),
    'pouch': myItem( 'pouch', 0x0E79, 0x0000, 'container', 1 ),
    'trash barrel': myItem( 'trash barrel', 0x0E77, 0x03B2, 'container', 1 ),
    'wooden box': myItem( 'wooden box', 0x0E7D, 0x0000, 'container', 1 ),
    'wooden chest': myItem( 'wooden chest', 0x0E43, 0x0000, 'container', 1 ),


    ### Decoration ###
    # Christmas
    'box of snowdrops (east/west)': myItem( 'box of snowdrops', 0x3325, 0x0000, 'decoration', 1 ),
    'box of snowdrops (north/south)': myItem( 'box of snowdrops', 0x3326, 0x0000, 'decoration', 1 ),
    'broken ornament': myItem( 'broken ornament', 0x09B4, 0x0501, 'decoration', 1 ),
    'christmas lights': myItem( 'christmas lights', 0x17CE, 0x0B93, 'decoration', 1 ),
    'fancy holidy lamp': myItem( 'fancy holidy lamp', 0x4C51, 0x0785, 'decoration', 1 ),
    'green candycane': myItem( 'green candycane', 0x2BDF, 0x0000, 'decoration', 1 ),
    'holiday toy egg (red)': myItem( 'holiday toy egg (red)', 0x4CFD, 0x0026, 'decoration', 1 ),
    'holiday toy egg (blue)': myItem( 'holiday toy egg (blue)', 0x4CFD, 0x0000, 'decoration', 1 ),
    'holly jolly torch': myItem( 'holly jolly torch', 0x0F6B, 0x09E9, 'decoration', 1 ),
    'marshmallow snowballs': myItem( 'marshmallow snowballs', 0x09EB, 0x0481, 'decoration', 1 ),
    'old holiday sign (Santa\'s Workshop - Closed till next year)': myItem( 'old holiday sign (Santa\'s Workshop - Closed till next year)', 0x0BD9, 0x09F5, 'decoration', 1 ),
    'red candycane': myItem( 'red candycane', 0x2BDE, 0x0000, 'decoration', 1 ),

    # Dinner Ware
    'ceramic mug': myItem( 'ceramic mug', 0x0995, 0x0000, 'decoration', 1 ),
    'snow mug': myItem( 'snow mug', 0x0995, 0x0481, 'decoration', 1 ),

    'bloody hourglass': myItem( 'bloody hourglass', 0x1810, 0x0A93, 'decoration', 1 ),
    'dragon head': myItem( 'dragon head', 0x2235, 0x0000, 'decoration', 1 ),
    'ettin fire brew': myItem( 'ettin fire brew', 0x495F, 0x081B, 'decoration', 1 ),
    'hourglass': myItem( 'hourglass', 0x1810, 0x0000, 'decoration', 1 ),
    'lamp stainglass': myItem( 'lamp stainglass', 0x4C51, 0x0000, 'decoration', 1 ),
    'torch': myItem( 'torch', 0x0F6B, 0x0000, 'decoration', 1 ),
    'tub of vegetables': myItem( 'tub of vegetables', 0x31CE, 0x0000, 'decoration', 1 ),
    'UOForever\'s 6th Year': myItem( 'UOForever\'s 6th Year', 0x9BC8, 0x0AA1, 'decoration', 1 ),


    ### Deeds ###
    'bank check': myItem( 'bank check', 0x14F0, 0x0034, 'deed', 1 ),
    'power scroll': myItem( 'power scroll', 0x14F0, 0x0481, 'deed', 1 ),


    ### Healing ###
    'bandage': myItem( 'bandage', 0x0E21, 0x0000, 'healing', 0.1 ),
    'healingPotion': None,
    'greaterHealingPotion': None,


    ### Ingots ###
    'bronze ingot': myItem( 'bronze ingot', 0x1BF2, 0x06D8, 'ingot', 0.1 ),
    'copper ingot': myItem( 'copper ingot', 0x1BF2, 0x045F, 'ingot', 0.1 ),
    'dull copper ingot': myItem( 'dull copper ingot', 0x1BF2, 0x0415, 'ingot', 0.1 ),
    'iron ingot': myItem( 'iron ingot', 0x1BF2, 0x0000, 'ingot', 0.1 ),
    'shadow iron ingot': myItem( 'shadow iron ingot', 0x1BF2, 0x0455, 'ingot', 0.1 ),


    ### Instruments ###
    'drum': myItem( 'drum', 0x0E9C, 0x0000, 'instrument', None ),
    'flute': myItem( 'flute', 0x2805, 0x0000, 'instrument', None ),
    'lute': myItem( 'lute', 0x0EB3, 0x0000, 'instrument', None ),

    # Harps
    'lap harp': myItem( 'lap harp', 0x0EB2, 0x0000, 'instrument', None ),
    'standing harp': myItem( 'standing harp', 0x0EB1, 0x0000, 'instrument', None ),

    # Tambourines
    'tambourine': myItem( 'tambourine', 0x0E9E, 0x0000, 'instrument', None ),
    'tambourineWithTassles': myItem( 'tambourineWithRedTassles', 0x0E9D, 0x0000, 'instrument', None ),


    ### Moongates ###
    'blue moongate': myItem( 'blue moongate', 0x0F6C, 0x0000, 'moongate', None ),


    ### Ores ###
    # Weights are set to None since the weight varies depending on the player's mining skill
    'bronze ore': myItem( 'bronze ore', 0x19B9, 0x06D8, 'ore', None ),
    'copper ore': myItem( 'copper ore', 0x19B9, 0x045F, 'ore', None ),
    'dull copper ore': myItem( 'dull copper ore', 0x19B9, 0x0415, 'ore', None ),
    'iron ore': myItem( 'iron ore', 0x19B9, 0x0000, 'ore', None ),
    'shadow iron ore': myItem( 'shadow iron ore', 0x19B9, 0x0455, 'ore', None ),


    ### Reagents ###
    'Black Pearl': myItem( 'Black Pearl', 0x0F7A, 0x0000, 'reagent', 0.1 ),
    'Blood Moss': myItem( 'Blood Moss', 0x0F7B, 0x0000, 'reagent', 0.1 ),
    'Garlic': myItem( 'Garlic', 0x0F84, 0x0000, 'reagent', 0.1 ),
    'Ginseng': myItem( 'Ginseng', 0x0F85, 0x0000, 'reagent', 0.1 ),
    'Mandrake Root': myItem( 'Mandrake Root', 0x0F86, 0x0000, 'reagent', 0.1 ),
    'Nightshade': myItem( 'Nightshade', 0x0F88, 0x0000, 'reagent', 0.1 ),
    'Spider\'s Silk': myItem( 'Spider\'s Silk', 0x0F8D, 0x0000, 'reagent', 0.1 ),
    'Sulfurous Ash': myItem( 'Sulfurous Ash', 0x0F8C, 0x0000, 'reagent', 0.1 ),


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


def FindBandage( container ):
    '''
    Uses FindItem to look through the player's backpack for a bandage
    '''
    global items

    return FindItem( items[ 'bandage' ].itemID, container )


def FindInstrument( container ):
    '''
    Uses FindItem to look through the player's backpack for an instrument
    '''
    global instruments

    instrumentIDs = [ instruments[ instrument ].itemID for instrument in instruments ]

    return FindItem( instrumentIDs, container )


def FindMoongate():
    '''
    Finds a moongate that the player can use
    '''
    global moongates

    moongateIDs = [ moongates[ moongate ].itemID for moongate in moongates ]

    moongateFilter = Items.Filter()
    moongateFilter.OnGround = 1
    moongateFilter.RangeMin = 0
    moongateFilter.RangeMax = 1
    moongateFilter.Movable = False
    moongateFilter.Graphics = List[int]( moongateIDs )

    return Items.ApplyFilter( moongateFilter )


def MoveItem( item, destinationBag, amount = 0 ):
    RazorEnhancedClasses.Items.Move( item, destinationBag, amount )

    # Wait for the move to complete
    RazorEnhancedClasses.Misc.Pause( 600 )
