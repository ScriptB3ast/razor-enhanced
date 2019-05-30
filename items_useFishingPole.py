from Scripts.glossary.items.tools import tools
from Scripts.utilities.items import FindItem

fishingPole = FindItem( tools[ 'fishing pole' ].itemID, Player.Backpack )

if fishingPole == None:
    Player.HeadMessage( colors[ 'red' ], 'No fishing pole to use!' )
else:
    Items.UseItem( fishingPole )
    Target.WaitForTarget( 2000, True )
    Target.TargetExecuteRelative( Player.Serial, 2 )

Misc.Pause( 50 )
