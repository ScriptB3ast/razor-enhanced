homeRunebookSerial = None
if Player.Name == 'TheWarPhysician':
    homeRunebookSerial = 0x419880D0
elif Player.Name == 'TheWarMage':
    homeRunebookSerial = 0x42783F7F
elif Player.Name == 'TombRaider':
    homeRunebookSerial = 0x427841F6
    
Items.UseItem( homeRunebookSerial )
Gumps.WaitForGump( 1431013363, 2000 )
Misc.Pause( 50 )
Gumps.SendAction( 1431013363, 5 )
