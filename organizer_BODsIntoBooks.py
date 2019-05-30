blacksmithingBook = 0x405947BE
tailoringBook = 0x4059463F

containerWithBODsSerial = Target.PromptTarget( 'Select container with BODs' )
if Mobiles.FindBySerial( containerWithBODsSerial ) != None:
    containerWithBODsSerial = Mobiles.FindBySerial( containerWithBODsSerial ).Backpack.Serial
    
containerWithBODs = Items.FindBySerial( containerWithBODsSerial )
Items.UseItem( containerWithBODs )
Misc.Pause( 700 )

from Scripts.utilities.items import FindItem, MoveItem

blacksmithingBOD = FindItem( 0x14EF, containerWithBODs, 0x044E )
while blacksmithingBOD != None:
    MoveItem( Items, Misc, blacksmithingBOD, blacksmithingBook )
    blacksmithingBOD = FindItem( 0x14EF, containerWithBODs, 0x044E )

tailoringBOD = FindItem( 0x14EF, containerWithBODs, 0x0483 )
while tailoringBOD != None:
    MoveItem( Items, Misc, tailoringBOD, tailoringBook )
    tailoringBOD = FindItem( 0x14EF, containerWithBODs, 0x0483 )
