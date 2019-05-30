# Adjust to the number of reagents you would like in your reagents bag
restockTo = 50
if Player.Name == 'TheWarMage':
    restockTo = 150
    #pass
# Adjust to whether to not you want to remove reagents from your bag if you have more than the desired amount
removeReagentsIfOverRestockToAmount = True

houseReagentsChestSerial = 0x43923CEA
houseTopLeftCornerX = 975
houseTopLeftCornerY = 452
houseBottomRightCornerX = 987
houseBottomRightCornerY = 469

from Scripts.utilities.items import FindItem, MoveItem, FindNumberOfItems
from Scripts.glossary.items.reagents import reagents
from Scripts.glossary.colors import colors
from Scripts import config

def RestockReagents():
    global restockTo
    global removeReagentsIfOverRestockToAmount

    reagentsBagSharedValue = 'reagentsBag'

    if not Misc.CheckSharedValue( reagentsBagSharedValue ):
        reagentsBag = Target.PromptTarget( 'Select bag to move the reagents into' )
        Misc.SetSharedValue( reagentsBagSharedValue, reagentsBag )

    reagentsBag = Misc.ReadSharedValue( reagentsBagSharedValue )
    if reagentsBag == None or Items.FindBySerial( reagentsBag ) == None:
        Player.HeadMessage( colors[ 'red' ], 'Can\'t find reagents bag! Clearing stored bag, please run again' )
        Misc.RemoveSharedValue( reagentsBagSharedValue )
        return

    reagentsBag = Items.FindBySerial( reagentsBag )

    if ( Player.Position.X >= houseTopLeftCornerX and Player.Position.Y >= houseTopLeftCornerY and
            Player.Position.X <= houseBottomRightCornerX and Player.Position.Y <= houseBottomRightCornerY ):
        reagentsSource = Items.FindBySerial( houseReagentsChestSerial )
    else:
        reagentsSource = Target.PromptTarget( 'Select container to restock from' )
        reagentsSource = Items.FindBySerial( reagentsSource )
        if reagentsSource == None or not reagentsSource.IsContainer:
            Player.HeadMessage( colors[ 'red' ], 'Invalid source container' )

    Items.UseItem( reagentsSource )
    Misc.Pause( config.dragDelayMilliseconds )

    reagentItemIDs = [ reagents[ reagent ].itemID for reagent in reagents ]
    reagentsInBag = FindNumberOfItems( reagentItemIDs, reagentsBag )

    for reagent in reagents:
        currentReagent = reagents[ reagent ]
        if reagentsInBag[ currentReagent.itemID ] == restockTo:
            continue
        elif reagentsInBag[ currentReagent.itemID ] < restockTo:
            reagentStackFromReagentsBag = FindItem( currentReagent.itemID, reagentsBag )
            reagentStackFromSourceContainer = FindItem( currentReagent.itemID, reagentsSource )
            if reagentStackFromReagentsBag == None:
                MoveItem( Items, Misc, reagentStackFromSourceContainer, reagentsBag, restockTo )
            else:
                MoveItem( Items, Misc, reagentStackFromSourceContainer, reagentsBag, restockTo - reagentStackFromReagentsBag.Amount )
        elif removeReagentsIfOverRestockToAmount:
            reagentStackFromReagentsBag = FindItem( currentReagent.itemID, reagentsBag )
            Misc.SendMessage( 'Removing %i %s' % ( reagentStackFromReagentsBag.Amount - restockTo, currentReagent.name ) )
            MoveItem( Items, Misc, reagentStackFromReagentsBag, reagentsSource, reagentStackFromReagentsBag.Amount - restockTo )

RestockReagents()
