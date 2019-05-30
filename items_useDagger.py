from Scripts.glossary.items.tools import tools
from Scripts.utilities.items import FindItem
from Scripts.glossary.colors import colors

dagger = FindItem( tools[ 'dagger' ].itemID, Player.Backpack )

if dagger != None:
    Items.UseItem( dagger )
else:
    Player.HeadMessage( 'You don\'t have a dagger!' )

Misc.Pause( 50 )
