from Scripts.utilities.items import MoveItem

item = Player.GetItemOnLayer( 'LeftHand' )
if item != None:
    MoveItem( Items, Misc, item, Player.Backpack )

item = Player.GetItemOnLayer( 'RightHand' )
if item != None:
    MoveItem( Items, Misc, item, Player.Backpack )
