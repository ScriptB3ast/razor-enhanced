class Item:
    name = None
    itemID = None
    category = None
    weight = None

    def __init__ ( self, name, itemID, category, weight ):
        self.name = name
        self.itemID = itemID
        self.category = category
        self.weight = weight

items = {
    ### Healing ###
    'bandage': Item( 'bandage', 0x0E21, 'healing', 0.1 ),
    'healingPotion': None,
    'greaterHealingPotion': None,


    ### Ingots ###


    ### Instruments ###
    'drum': Item( 'drum', 0x0E9C, 'instrument', None ),
    'flute': Item( 'flute', 0x2805, 'instrument', None ),
    'lute': Item( 'lute', 0x0EB3, 'instrument', None ),

    # Harps
    'harpLap': Item( 'lap harp', 0x0EB2, 'instrument', None ),
    'harpStanding': Item( 'standing harp', 0x0EB1, 'instrument', None ),

    # Tambourines
    'tambourine': Item( 'tambourine', 0x0E9E, 'instrument', None ),
    'tambourineWithTassles': Item( 'tambourineWithRedTassles', 0x0E9D, 'instrument', None ),


    ### Ores ###
    'oreIron': Item( 'iron ore', 0x19B9, 'ore', 9 ),


    ### Reagents ###
    'Black Pearl': Item( 'Black Pearl', 0x0F7A, 'reagent', 0.1 ),
    'Blood Moss': Item( 'Blood Moss', 0x0F7B, 'reagent', 0.1 ),
    'Garlic': Item( 'Garlic', 0x0F84, 'reagent', 0.1 ),
    'Ginseng': Item( 'Ginseng', 0x0F85, 'reagent', 0.1 ),
    'Mandrake Root': Item( 'Mandrake Root', 0x0F86, 'reagent', 0.1 ),
    'Nightshade': Item( 'Nightshade', 0x0F88, 'reagent', 0.1 ),
    'Spider\'s Silk': Item( 'Spider\'s Silk', 0x0F8D, 'reagent', 0.1 ),
    'Sulfurous Ash': Item( 'Sulfurous Ash', 0x0F8C, 'reagent', 0.1 )
}

ores = { key: value for key, value in items.items() if value != None and value.category == 'ore' }
instruments = { key: value for key, value in items.items() if value != None and value.category == 'instrument' }
reagents = { key: value for key, value in items.items() if value != None and value.category == 'reagent' }


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
        numberOfItems[ item ] = 0
        foundItems = { item.ItemID: item.Amount for item in container.Contains if item.ItemID == itemID }
    elif isinstance( itemID, list ):
        for item in itemID:
            numberOfItems[ item ] = 0
        foundItems = { item.ItemID: item.Amount for item in container.Contains if item.ItemID in itemID }
    else:
        raise ValueError( 'Unknown argument type for itemID passed to FindItem().', itemID, container )

    # Add the contents found to the dictionary
    numberOfItems = { itemID: numberOfItems.get( itemID, 0 ) + foundItems.get( itemID, 0 ) for itemID in set( numberOfItems ).union( foundItems ) }

    subcontainers = [ item for item in container.Contains if item.IsContainer ]

    # Iterate through each item in the given list
    for subcontainer in subcontainers:
        numberOfItemsInSubcontainer = FindNumberOfItems( itemID, subcontainer )
        numberOfItems = { itemID: numberOfItems.get( itemID, 0 ) + numberOfItemsInSubcontainer.get( itemID, 0 ) for itemID in set( numberOfItems ).union( numberOfItemsInSubcontainer ) }

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
