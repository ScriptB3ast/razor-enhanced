from Scripts.utilities.items import myItem, FindItem

instruments = {
    'bamboo flute': myItem( 'bamboo flute', 0x2805, 0x0000, 'instrument', None ),
    'drum': myItem( 'drum', 0x0E9C, 0x0000, 'instrument', None ),
    'lute': myItem( 'lute', 0x0EB3, 0x0000, 'instrument', None ),

    # Harps
    'lap harp': myItem( 'lap harp', 0x0EB2, 0x0000, 'instrument', None ),
    'standing harp': myItem( 'standing harp', 0x0EB1, 0x0000, 'instrument', None ),

    # Tambourines
    'tambourine': myItem( 'tambourine', 0x0E9E, 0x0000, 'instrument', None ),
    'tambourine (tassle)': myItem( 'tambourine', 0x0E9D, 0x0000, 'instrument', None )
}

def FindInstrument( container ):
    '''
    Uses FindItem to look through the player's backpack for an instrument
    '''
    global instruments

    instrumentIDs = [ instruments[ instrument ].itemID for instrument in instruments ]

    return FindItem( instrumentIDs, container )
