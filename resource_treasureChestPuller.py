# Treasure Map Puller by MatsaMilla
# SHOULD pull gold first and palce in beetle
# keeps recalls, gate & lvl 8 summoning scrolls no matter what
# you will have to re-assign bags every time you close Razor... fault of the program.

from Scripts import config
from Scripts.glossary.items.armor import armor
from Scripts.glossary.items.clothing import clothingInTreasureChests
from Scripts.glossary.items.gems import gems
from Scripts.glossary.items.reagents import reagents
from Scripts.glossary.items.shields import shields
from Scripts.glossary.items.spellScrolls import spellScrolls
from Scripts.glossary.items.weapons import weapons
from Scripts.utilities.items import FindItem, MoveItem
from Scripts.glossary.colors import colors

msgColor = 68
self = Mobiles.FindBySerial( Player.Serial )

# *** Replace with beetle serial if you have one ***
beetle = 0x001D9588

# *** False if you do not have beetle ***
beetleBag = True

# True if you want to keep scrolls
keepScrolls = True


def GetBag ( sharedValue, promptString ):
    if Misc.CheckSharedValue( sharedValue ):
        bag = Misc.ReadSharedValue( sharedValue )
        if not Items.FindBySerial( bag ):
            bag = Target.PromptTarget( promptString )
            Misc.SetSharedValue( sharedValue, bag )
    else:
        bag = Target.PromptTarget( promptString )
        Misc.SetSharedValue( sharedValue, bag )
    return bag

# Check for reg bag
reagentsBag = GetBag( 'reagentsBag', 'Select Bag for Regs' )
weaponsBag = GetBag( 'weaponsBag', 'Select Bag for Weapons' )
armorBag = GetBag( 'armorBag', 'Select Bag for Armor' )
gemsBag = GetBag( 'gemsBag', 'Select Bag for Gems' )

scrollsBag = None
if keepScrolls:
    scrollsBag = GetBag( 'scrollsBag', 'Select Bag for Scrolls' )

trashCan = GetBag( 'trashCan', 'Select Corpse to dump on' )

chest = Target.PromptTarget( 'Select Treasure Chest' )
mapChest = Items.FindBySerial( chest )
if mapChest == None or not mapChest.IsContainer:
    Misc.SendMessage( 'Invalid treasure chest! Try running again', colors[ 'red' ] )
    Stop

#loot includes gate, recall & lvl 8 summoning scrolls
loot = [ 0x2260, 0x1f4c, 0x1f60, 0x1f66, 0x1f68, 0x1f69, 0x1f6a, 0x1f6b, 0x1f6c ]

gold = [ 0x0EED ]
wands = [ 0xdf5, 0xdf3, 0xdf4, 0xdf2 ]

armorIDs = [ armor[ item ].itemID for item in armor ]
gemIDs = [ gems[ gem ].itemID for gem in gems ]
reagentIDs = [ reagents[ reagent ].itemID for reagent in reagents ]
shieldIDs = [ shields[ shield ].itemID for shield in shields ]
scrollIDs = [ spellScrolls[ scroll ].itemID for scroll in spellScrolls ]
trashIDs = [ clothingInTreasureChests[ item ].itemID for item in clothingInTreasureChests ]
weaponIDs = [ weapons[ weapon ].itemID for weapon in weapons ]

Items.UseItem( mapChest )
Misc.Pause( config.dragDelayMilliseconds )

def checkDistance():
    Timer.Create( 'Distance', 1 )
    while mapChest.DistanceTo( self ) > 2:
        if not Timer.Check( 'Distance' ):
            Player.HeadMessage( msgColor, 'Too Far Away' )
            Timer.Create( 'Distance', 2500 )
    Items.UseItem( mapChest )
    Misc.Pause( dragDelayMilliseconds )


def checkWeight():
    if Player.Weight >= Player.MaxWeight:
        Player.ChatSay(msgColor, 'I am Overweight, stopping')
        Stop

#moves gold to beetle
if beetleBag:
    for item in mapChest.Contains:
        checkDistance()
        if item.ItemID in gold:
            if Player.Mount:
                # Dismount so we can access the beetle's bag
                Mobiles.UseMobile( Player.Serial )
                Misc.Pause( config.dragDelayMilliseconds )

            # Move the gold into the beetle
            MoveItem( Items, Misc, item, beetle )

            if not Player.Mount:
                # Remount
                Mobiles.UseMobile( beetle )
                Misc.Pause( config.dragDelayMilliseconds )

# Grab the gold
for item in mapChest.Contains:
    checkDistance()
    checkWeight()
    if item.ItemID in gold:
        if beetleBag:
            if Player.Mount:
                # Dismount so we can access the beetle's bag
                Mobiles.UseMobile( Player.Serial )
                Misc.Pause( config.dragDelayMilliseconds )

            # Move the gold into the beetle
            Items.Move( item, beetle, 0 )
            Misc.Pause( config.dragDelayMilliseconds )

            if not Player.Mount:
                # Remount
                Mobiles.UseMobile( beetle )
                Misc.Pause( config.dragDelayMilliseconds )
        else:
            MoveItem( Items, Misc, item, Player.Backpack.Serial )

# Grab the regs
for item in mapChest.Contains:
    checkDistance()
    checkWeight()
    if item.ItemID in reagentIDs:
        MoveItem( Items, Misc, item, reagentsBag )

# Grab the gems
for item in mapChest.Contains:
    checkDistance()
    checkWeight()
    if item.ItemID in gemIDs:
        MoveItem( Items, Misc, item, gemsBag )

# Grab everything else
for item in mapChest.Contains:
    checkDistance()
    checkWeight()
    if item.ItemID in loot:
        MoveItem( Items, Misc, item, Player.Backpack )
    elif item.ItemID in armorIDs or item.ItemID in shieldIDs:
        MoveItem( Items, Misc, item, armorBag )
    elif item.ItemID in weaponIDs:
        MoveItem( Items, Misc, item, weaponsBag )
    elif item.ItemID in wands:
        MoveItem( Items, Misc, item, Player.Backpack )
    elif keepScrolls:
        if item.ItemID in scrollIDs:
            MoveItem( Items, Misc, item, scrollsBag )

# Move the trash into the trash can
for item in mapChest.Contains:
    checkDistance()
    checkWeight()
    if item.ItemID in trashIDs or item.ItemID in scrollIDs:
        MoveItem( Items, Misc, item, trashCan )

Player.ChatSay( msgColor, 'Got it all, let''s bounce!' )
