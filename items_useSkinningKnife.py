from Scripts.glossary.items.tools import tools
from Scripts.utilities.items import FindItem
from Scripts.glossary.colors import colors

skinningKnife = FindItem( tools[ 'skinning knife' ].itemID, Player.Backpack )

if skinningKnife != None:
    Items.UseItem( skinningKnife )
else:
    Player.HeadMessage( 'You don\'t have a skinning knife!' )
