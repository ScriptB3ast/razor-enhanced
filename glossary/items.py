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
