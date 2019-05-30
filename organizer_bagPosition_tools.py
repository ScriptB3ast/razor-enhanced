toolBag = Items.FindBySerial( Target.PromptTarget( 'Select bag to organize' ) )
pickaxe = Items.FindByID( 0x0E86, -1, Player.Backpack.Serial )
tongs = Items.FindByID( 0x0FBB, -1, Player.Backpack.Serial )
smithsHammer = Items.FindByID( 0x13E3, -1, Player.Backpack.Serial )
sledgeHammer = Items.FindByID( 0x0FB5, -1, Player.Backpack.Serial )

if pickaxe != None:
    Items.Move( pickaxe, toolBag, 0, 100, 100 )
if tongs != None:
    Items.Move( tongs, toolBag, 0, 80, 0 )
if smithsHammer != None:
    Items.Move( smithsHammer, toolBag, 0, 75, 0 )
if sledgeHammer != None:
    Items.Move( sledgeHammer, toolBag, 0, 100, 0 )
