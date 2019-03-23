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
    'oreIron': Item( 'iron ore', 0x19B9, 'ore', 9 )
}

ores = { key: value for key, value in items.items() if value != None and value.category == 'ore' }
instruments = { key: value for key, value in items.items() if value != None and value.category == 'instrument' }


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

    subcontainers = list( filter( lambda item: item.IsContainer, container.Contains ) )
    for subcontainer in subcontainers:
        foundItem = FindItem( itemID, subcontainer )
        if foundItem != None:
            return foundItem


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
