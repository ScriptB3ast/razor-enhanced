sextant = Items.FindByID( 0x1058, -1, Player.Backpack.Serial )
if sextant != None:
    Items.UseItem( sextant )
Misc.Pause( 50 )
