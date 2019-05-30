from Scripts import config

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


def MoveItem( Items, Misc, item, destinationBag, amount = 0 ):
    Items.Move( item, destinationBag, amount )

    # Wait for the move to complete
    Misc.Pause( config.dragDelayMilliseconds )
