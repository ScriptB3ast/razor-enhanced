from Scripts.glossary.colors import colors

bandages = Items.FindByID( 0x0E21, -1, Player.Backpack.Serial )
if bandages != None:
    Items.UseItem( bandages )
    Target.WaitForTarget( 2000, False )
    Target.TargetExecute( Player.Serial )
else:
    Player.HeadMessage( colors[ 'red' ], 'Out of bandages!' )
