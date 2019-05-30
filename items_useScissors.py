from Scripts.glossary.items.tools import tools
from Scripts.utilities.items import FindItem
from Scripts.glossary.colors import colors

scissors = FindItem( tools[ 'scissors' ].itemID, Player.Backpack )

if scissors != None:
    Items.UseItem( scissors )
else:
    Player.HeadMessage( 'You don\'t have scissors!' )

Misc.Pause( 50 )
