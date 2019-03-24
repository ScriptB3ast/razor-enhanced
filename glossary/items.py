class Item:
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
    'bandage': Item( 'bandage', 0x0E21, 0x0000, 'healing', 0.1 ),
    'healingPotion': None,
    'greaterHealingPotion': None,


    ### Ingots ###


    ### Instruments ###
    'drum': Item( 'drum', 0x0E9C, 0x0000, 'instrument', None ),
    'flute': Item( 'flute', 0x2805, 0x0000, 'instrument', None ),
    'lute': Item( 'lute', 0x0EB3, 0x0000, 'instrument', None ),

    # Harps
    'harpLap': Item( 'lap harp', 0x0EB2, 0x0000, 'instrument', None ),
    'harpStanding': Item( 'standing harp', 0x0EB1, 0x0000, 'instrument', None ),

    # Tambourines
    'tambourine': Item( 'tambourine', 0x0E9E, 0x0000, 'instrument', None ),
    'tambourineWithTassles': Item( 'tambourineWithRedTassles', 0x0E9D, 0x0000, 'instrument', None ),


    ### Ores ###
    'oreIron': Item( 'iron ore', 0x19B9, 0x0000, 'ore', 9 ),


    ### Reagents ###
    'Black Pearl': Item( 'Black Pearl', 0x0F7A, 0x0000, 'reagent', 0.1 ),
    'Blood Moss': Item( 'Blood Moss', 0x0F7B, 0x0000, 'reagent', 0.1 ),
    'Garlic': Item( 'Garlic', 0x0F84, 0x0000, 'reagent', 0.1 ),
    'Ginseng': Item( 'Ginseng', 0x0F85, 0x0000, 'reagent', 0.1 ),
    'Mandrake Root': Item( 'Mandrake Root', 0x0F86, 0x0000, 'reagent', 0.1 ),
    'Nightshade': Item( 'Nightshade', 0x0F88, 0x0000, 'reagent', 0.1 ),
    'Spider\'s Silk': Item( 'Spider\'s Silk', 0x0F8D, 0x0000, 'reagent', 0.1 ),
    'Sulfurous Ash': Item( 'Sulfurous Ash', 0x0F8C, 0x0000, 'reagent', 0.1 ),


    ### Tools ###
    'sledge hammer': Item( 'sledge hammer', 0x0FB5, 0x0000, 'tool', 10 ),
    'smith\'s hammer': Item( 'smith\'s hammer', 0x13E3, 0x0000, 'tool', 8 ),
    'tinker\'s tools': Item( 'tinker\'s tools', 0x1EBC, 0x0000, 'tool', 1 ),
    'tongs': Item( 'tongs', 0x0000, 0x0FBB, 'tool', 2 ),
    'tool kit': Item( 'tool kit', 0x1EB8, 0x0000, 'tool', 1 )
}

ores = { key: value for key, value in items.items() if value != None and value.category == 'ore' }
instruments = { key: value for key, value in items.items() if value != None and value.category == 'instrument' }
reagents = { key: value for key, value in items.items() if value != None and value.category == 'reagent' }
tools = { key: value for key, value in items.items() if value != None and value.category == 'tool' }


def FindItem( itemID, container ):
    '''
    Searches through the container for the item IDs specified and returns the first one found
    Also searches through any subcontainers, which Misc.FindByID() does not
    '''

    if isinstance( itemID, int ):
        foundItem = next( ( item for item in container.Contains if item.ItemID == itemID ), None )
    elif isinstance( itemID, list ):
        foundItem = next( ( item for item in container.Contains if item.ItemID in itemID ), None )
    else:
        raise ValueError( 'Unknown argument type for itemID passed to FindItem().', itemID, container )

    if foundItem != None:
        return foundItem

    subcontainers = [ item for item in container.Contains if item.IsContainer ]
    for subcontainer in subcontainers:
        foundItem = FindItem( itemID, subcontainer )
        if foundItem != None:
            return foundItem


def FindNumberOfItems( itemID, container ):
    '''
    Recursively looks through a container for any items in the provided list
    Returns the a dictionary with the number of items found from the list
    '''

    # Create the dictionary
    numberOfItems = {}

    if isinstance( itemID, int ):
        # Initialize numberOfItems
        numberOfItems[ itemID ] = 0

        # Populate numberOfItems
        for item in container.Contains:
            if item.ItemID == itemID:
                numberOfItems[ itemID ] += item.Amount
    elif isinstance( itemID, list ):
        # Initialize numberOfItems
        for ID in itemID:
            numberOfItems[ ID ] = 0

        # Populate numberOfItems
        for item in container.Contains:
            if item.ItemID in itemID:
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

    instrumentIDs = [ instrument.itemID for instrument in instruments ]

    return FindItem( instrumentIDs, container )
