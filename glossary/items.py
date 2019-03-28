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


    ### Ores ###
    'iron ore': myItem( 'iron ore', 0x19B9, 0x0000, 'ore', None ),
    'dull copper ore': myItem( 'dull copper ore', 0x19B9, 0x0415, 'ore', None ),


    ### Reagents ###
    'Black Pearl': myItem( 'Black Pearl', 0x0F7A, 0x0000, 'reagent', 0.1 ),
    'Blood Moss': myItem( 'Blood Moss', 0x0F7B, 0x0000, 'reagent', 0.1 ),
    'Garlic': myItem( 'Garlic', 0x0F84, 0x0000, 'reagent', 0.1 ),
    'Ginseng': myItem( 'Ginseng', 0x0F85, 0x0000, 'reagent', 0.1 ),
    'Mandrake Root': myItem( 'Mandrake Root', 0x0F86, 0x0000, 'reagent', 0.1 ),
    'Nightshade': myItem( 'Nightshade', 0x0F88, 0x0000, 'reagent', 0.1 ),
    'Spider\'s Silk': myItem( 'Spider\'s Silk', 0x0F8D, 0x0000, 'reagent', 0.1 ),
    'Sulfurous Ash': myItem( 'Sulfurous Ash', 0x0F8C, 0x0000, 'reagent', 0.1 ),


    ### Tools ###
    'sledge hammer': myItem( 'sledge hammer', 0x0FB5, 0x0000, 'tool', 10 ),
    'smith\'s hammer': myItem( 'smith\'s hammer', 0x13E3, 0x0000, 'tool', 8 ),
    'tinker\'s tools': myItem( 'tinker\'s tools', 0x1EBC, 0x0000, 'tool', 1 ),
    'tongs': myItem( 'tongs', 0x0000, 0x0FBB, 'tool', 2 ),
    'tool kit': myItem( 'tool kit', 0x1EB8, 0x0000, 'tool', 1 )
}

instruments = { itemName: item for itemName, item in items.items() if item != None and item.category == 'instrument' }
ores = { itemName: item for itemName, item in items.items() if item != None and item.category == 'ore' }
reagents = { itemName: item for itemName, item in items.items() if item != None and item.category == 'reagent' }
tools = { itemName: item for itemName, item in items.items() if item != None and item.category == 'tool' }


def FindItem( itemID, container, color = -1 ):
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

    subcontainers = [ item for item in container.Contains if item.IsContainer ]
    for subcontainer in subcontainers:
        foundItem = FindItem( itemID, subcontainer )
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
            if item.ItemID == itemID and ( ignoreColor or item.Color == color ):
                numberOfItems[ itemID ] += item.Amount
    elif isinstance( itemID, list ):
        # Initialize numberOfItems
        for ID in itemID:
            numberOfItems[ ID ] = 0

        # Populate numberOfItems
        for item in container.Contains:
            if item.ItemID in itemID and ( ignoreColor or item.Color == color ):
                numberOfItems[ itemID ] += item.Amount
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
