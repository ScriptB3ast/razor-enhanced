from Scripts.glossary.items.miscellaneous import miscellaneous
from Scripts.glossary.items.ingots import ingots
from Scripts.glossary.colors import colors
from Scripts.utilities.items import FindItem, MoveItem

nameOfItemsToDeposit = [ 'gold coin' ]
nameOfIngotsToDeposit = [ 'dull copper ingot', 'shadow iron ingot',
    'copper ingot', 'bronze ingot', 'golden ingot', 'agapite ingot' ]

itemsToDeposit = []
for item in miscellaneous:
    if miscellaneous[ item ] != None and miscellaneous[ item ].name in nameOfItemsToDeposit:
        itemsToDeposit.append( miscellaneous[ item ] )
        
for ingot in ingots:
    if ingots[ ingot ] != None and ingots[ ingot ].name in nameOfIngotsToDeposit:
        itemsToDeposit.append( ingots[ ingot ] )
        
nameOfItemsFound = [ item.name for item in itemsToDeposit ]
nameOfItemsNotFound = [ itemName for itemName in nameOfItemsToDeposit if not itemName in nameOfItemsFound ]
for name in nameOfItemsNotFound:
    Misc.SendMessage( 'Unknown item: %s' % name, colors[ 'red' ] )

Player.ChatSay( colors[ 'cyan' ], 'bank' )
Misc.Pause( 200 )
    
for item in itemsToDeposit:
    itemInBag = FindItem( item.itemID, Player.Backpack, item.color )
    if itemInBag != None:
        MoveItem( Items, Misc, itemInBag, Player.Bank )
