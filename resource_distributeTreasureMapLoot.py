from Scripts.glossary.items.armor import armor
from Scripts.glossary.items.gems import gems
from Scripts.glossary.items.miscellaneous import miscellaneous
from Scripts.glossary.items.shields import shields
from Scripts.glossary.items.spellScrolls import spellScrolls
from Scripts.glossary.items.weapons import weapons
from Scripts.utilities.items import FindItem, MoveItem
from Scripts.glossary.colors import colors

goldChest = 0x40100558

#weaponChest = 0x42D8693B # top chest
#weaponChest = 0x42D85F9B # second from top chest
#weaponChest = 0x42D86905 # third from top chest
#weaponChest = 0x42D85F71 # third from bottom chest
weaponChest = 0x42D8697C # second from bottom chest

#armorChest = 0x43923A97 # top chest
#armorChest = 0x43923E47 # second from top chest
#armorChest = 0x43923DF9 # third from top chest
#armorChest = 0x43923FF7 # third from bottom chest
armorChest = 0x43923D54 # second from bottom chest

shieldChest = 0x43923F89
scrollChest = 0x43924063
gemChest = 0x43923D99

'''
weps = [0xf62,0x1403,0xe87,0x1405,0x1401,0xf52,0x13b0,0xdf0,0x1439,0x1407,0xe89,
0x143d,0x13b4,0xe81,0x13f8,0xf5c,0x143b,0x13b9,0xf61,0x1441,0x13b6,0xec4,0x13f6,
0xf5e,0x13ff,0xec3,0xf43,0xf45,0xf4d,0xf4b,0x143e,0x13fb,0x1443,0xf47,0xf49,
0xe85,0xe86,0x13fd,0xf50,0x13b2]

armor = [0x1b72,0x1b73,0x1b7b,0x1b74,0x1b79,0x1b7a,0x1b76,0x1408,0x1410,0x1411,
0x1412,0x1413,0x1414,0x1415,0x140a,0x140c,0x140e,0x13bb,0x13be,0x13bf,0x13ee,
0x13eb,0x13ec,0x13f0,0x13da,0x13db,0x13d5,0x13d6,0x13dc,0x13c6,0x13cd,0x13cc,
0x13cb,0x13c7,0x1db9,0x1c04,0x1c0c,0x1c02,0x1c00,0x1c08,0x1c06,0x1c0a]
'''

armorIDs = [ armor[ armorPiece ].itemID for armorPiece in armor if armor[ armorPiece ].itemID != 0 ]
gemIDs = [ gems[ gem ].itemID for gem in gems ]
shieldIDs = [ shields[ shield ].itemID for shield in shields if shields[ shield ].itemID != 0 ]
spellScrollIDs = [ spellScrolls[ scroll ].itemID for scroll in spellScrolls ]
weaponIDs = [ weapons[ weapon ].itemID for weapon in weapons if weapons[ weapon ].itemID != 0 ]

#beetle = 0x001D9588
#backpack = Mobiles.FindBySerial( beetle ).Backpack
backpack = Player.Backpack

gold = FindItem( miscellaneous[ 'gold coin' ].itemID, backpack )
while gold != None:
    MoveItem( Items, Misc, gold, goldChest )
    gold = FindItem( miscellaneous[ 'gold coin' ].itemID, backpack )

Misc.SendMessage( 'Emptying weapons', colors[ 'cyan' ] )
weapon = FindItem( weaponIDs, backpack )
while weapon != None:
    Misc.SendMessage( weapon.Name )
    MoveItem( Items, Misc, weapon, weaponChest )
    weapon = FindItem( weaponIDs, backpack )

Misc.SendMessage( 'Emptying armor', colors[ 'cyan' ] )
armorPiece = FindItem( armorIDs, backpack )
while armorPiece != None:
    Misc.SendMessage( armorPiece.Name )
    MoveItem( Items, Misc, armorPiece, armorChest )
    armorPiece = FindItem( armorIDs, backpack )

Misc.SendMessage( 'Emptying shields', colors[ 'cyan' ] )
shield = FindItem( shieldIDs, backpack )
while shield != None:
    Misc.SendMessage( shield.Name )
    MoveItem( Items, Misc, shield, shieldChest )
    shield = FindItem( shieldIDs, backpack )

Misc.SendMessage( 'Emptying spell scrolls', colors[ 'cyan' ] )
spellScroll = FindItem( spellScrollIDs, backpack )
while spellScroll != None:
    Misc.SendMessage( spellScroll.Name )
    MoveItem( Items, Misc, spellScroll, scrollChest )
    spellScroll = FindItem( spellScrollIDs, backpack )

Misc.SendMessage( 'Emptying gems', colors[ 'cyan' ] )
gem = FindItem( gemIDs, backpack )
while gem != None:
    Misc.SendMessage( gem.Name )
    MoveItem( Items, Misc, gem, gemChest )
    gem = FindItem( gemIDs, backpack )
