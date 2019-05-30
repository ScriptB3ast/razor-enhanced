moveToBook = False
moveToDaviesLocker = True
daviesLockerSerial = 0x41B652AE

def DecodeMap( map ):
    Journal.Clear()
    Items.UseItem( map )
    Misc.Pause( 700 )
    while not ( Journal.SearchByName( 'You successfully decode a treasure map!', Player.Name ) or
            Journal.SearchByName( 'The treasure is marked by the red pin.', '' ) ):
        Items.UseItem( map )
        Misc.Pause( 700 )

if moveToBook:
    mapBook = Items.FindByID( 0x2252, 0x04F1, Player.Backpack.Serial )
    map = Items.FindByID( 0x14EC, 0x0000, Player.Backpack.Serial )
    while map != None:
        DecodeMap( map )
        Items.Move( map, mapBook, 0 )
        Misc.Pause( 700 )
        map = Items.FindByID( 0x14EC, 0x0000, Player.Backpack.Serial )
elif moveToDaviesLocker:
    daviesLocker = Items.FindBySerial( daviesLockerSerial )
    Items.UseItem( daviesLocker )
    Misc.Pause( 700 )
    Gumps.WaitForGump( 3738072638, 2000 )
    map = Items.FindByID( 0x14EC, 0x0000, Player.Backpack.Serial )
    while map != None:
        DecodeMap( map )
        Gumps.SendAction( 3738072638, 1000 )
        Target.WaitForTarget( 2000, True )
        Target.TargetExecute( map )
        Target.WaitForTarget( 2000, True )
        Target.Cancel()
        Gumps.WaitForGump( 3738072638, 2000 )
        map = Items.FindByID( 0x14EC, 0x0000, Player.Backpack.Serial )
