if Player.Name == 'TheWarDoctor':
    Items.UseItem( 0x43D619A8 )
elif Player.Name == 'TheWarPhysician':
    Items.UseItem( 0x419880D0 )
elif Player.Name == 'DoctorWho':
    Items.UseItem( 0x431FCD45 )

Gumps.WaitForGump( 1431013363, 2000 )
Gumps.SendAction( 1431013363, 2 )
