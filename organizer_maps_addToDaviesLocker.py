daviesLockerSerial = 0x41B652AE
daviesLocker = Items.FindBySerial( daviesLockerSerial )
Items.UseItem( daviesLocker )
Gumps.WaitForGump( 3738072638, 2000 )
map = Items.FindByID( 0x14EC, 0x0000, Player.Backpack.Serial )
while map != None:
    Gumps.SendAction( 3738072638, 1000 )
    Target.WaitForTarget( 2000, True )
    Target.TargetExecute( map )
    Misc.Pause( 50 )
    map = Items.FindByID( 0x14EC, 0x0000, Player.Backpack.Serial )
