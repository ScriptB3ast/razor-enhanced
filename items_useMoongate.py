from Scripts.glossary.items.moongates import FindMoongates

moongates = FindMoongates( Items )
if len( moongates ) > 0:
    Items.UseItem( moongates[ 0 ] )

    Gumps.WaitForGump( 3716879466, 2000 )
    Gumps.SendAction( 3716879466, 1 )
