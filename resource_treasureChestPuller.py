# Treasure Map Puller by MatsaMilla
# SHOULD pull gold first and palce in beetle
# keeps recalls, gate & lvl 8 summoning scrolls no matter what
# you will have to re-assign bags every time you close Razor... fault of the program.

#*********** SETUP SECTION*********************************
# Set to none to not recall home if an RDA frag is found
recallHomeScript = 'recall_home_Spell.py'

# Replace with beetle serial if you have one
beetle = 0x001D9588

# False if you do not have beetle
beetleBag = True
if Player.Name == 'TombRaider':
    beetleBag = False

# True if you want to keep scrolls
keepScrolls = True

# Will use ID Wand if skill Item ID below 80
useIdWand = False
if Player.GetRealSkillValue( 'Item ID' ) < 80:
    useIdWand = True

slashProps = [ 'Invulnerability', 'Exceptional', 'Power' ]
subSlashProps = [ 'Indestructable', 'Fortified', 'Massive', 'Substantial', 'Supremely Accurate', 'Exceedingly Accurate' ]
itemQualitiesToKeep = [
    # Strength
    'Vanquishing',

    ### Slayer Types ###
    # Slayer Group: Humanoid
    'Repond', 'Goblin', 'Orc', 'Ogre', 'Troll',
    # Slayer Group: Undead
    'Undead', 'Silver',
    # Slayer Group: Fey
    'Fey',
    # Slayer Group: Elemental
    'Elemental', 'Air', 'Vacuum', 'Blood', 'Earth', 'Fire', 'Flame', 'Poison', 'Snow', 'Summer', 'Water',
    # Slayer Group: Abyss
    'Demon', 'Exorcism', 'Daemon', 'Gargoyle', 'Balron',
    # Slayer Group: Arachnid
    'Arachnid', 'Scorpion', 'Spider', 'Terathan',
    # Slayer Group: Reptilian
    'Reptile', 'Reptilian', 'Dragon', 'Lizardman', 'Ophidian', 'Snake'
]
#**********************************************************

msgColor = 68
self = Mobiles.FindBySerial( Player.Serial )

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
sellBag = GetBag( 'sellBag', 'Select Bag for BAD weps and armor' )
keepBag = GetBag( 'keepBag', 'Select Bag for GOOD weps and armor' )
gemsBag = GetBag( 'gemsBag', 'Select Bag for Gems' )

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
trashIDs = [ clothingInTreasureChests[ item ].itemID for item in clothingInTreasureChests ]
weaponIDs = [ weapons[ weapon ].itemID for weapon in weapons ]

# Scroll names can be found in glossary/items/spellScrolls.py
scrollsToKeep = [
    'Mana Drain scroll',
    'Recall scroll',
    'Energy Bolt scroll',
    'Explosion scroll',
    'Mark scroll',
    'Flamestrike scroll',
    'Gate Travel scroll',
    'Mana Vampire scroll',
    'Energy Vortex scroll',
    'Resurrection scroll',
    'Summon Air Elemental scroll',
    'Summon Daemon scroll',
    'Summon Earth Elemental scroll',
    'Summon Fire Elemental scroll',
    'Summon Water Elemental scroll',
]
scrollsToTrash = [
    'Clumsy scroll',
    'Create Food scroll',
    'Feeblemind scroll',
    'Heal scroll',
    'Magic Arrow scroll',
    'Night Sight scroll',
    'Reactive Armor scroll',
    'Weaken scroll',
]

scrollIDsToKeep = []
scrollIDsToSell = []
scrollIDsToTrash = []
for scroll in spellScrolls:
    if spellScrolls[ scroll ].name in scrollsToKeep:
        scrollIDsToKeep.append( spellScrolls[ scroll ].itemID )
    elif spellScrolls[ scroll ].name in scrollsToTrash:
        scrollIDsToTrash.append( spellScrolls[ scroll ].itemID )
    else:
        scrollIDsToSell.append( spellScrolls[ scroll ].itemID )

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

rdaFrag = Items.FindByID( 0x0F21, 0x0489, mapChest.Serial )
if rdaFrag != None:
    MoveItem( Items, Misc, rdaFrag, Player.Backpack )
    if recallHomeScript != None:
        Misc.ScriptRun( recallHomeScript )
        Misc.Pause( 50 )
        Misc.ScriptStop( 'resource_treasureChestPuller.py' )


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


# Grab wands
for item in mapChest.Contains:
    checkDistance()
    checkWeight()
    if item.ItemID in wands:
        MoveItem( Items, Misc, item, Player.Backpack )


# Grab scrolls
for item in mapChest.Contains:
    checkDistance()
    checkWeight()
    if item.ItemID in scrollIDsToKeep:
        MoveItem( Items, Misc, item, keepBag )
    elif item.ItemID in scrollIDsToSell:
        MoveItem( Items, Misc, item, sellBag )


def EquipWand():
    player_bag = Items.FindBySerial( Player.Backpack.Serial )

    if Player.GetItemOnLayer( 'LeftHand' ):
        Player.UnEquipItemByLayer( 'LeftHand' )
        Misc.Pause( config.dragDelayMilliseconds )

    if not Player.GetItemOnLayer( 'RightHand' ):
        for item in player_bag.Contains:
            if item.ItemID in wands:
                Player.EquipItem( item.Serial )
                Misc.Pause( config.dragDelayMilliseconds )
                wandSerial = Player.GetItemOnLayer( 'RightHand' ).Serial
    elif Player.GetItemOnLayer( 'RightHand' ).ItemID in wands:
        wandSerial = Player.GetItemOnLayer( 'RightHand' ).Serial
    else:
        Player.ChatSay( colors[ 'red' ], 'Out of wands!' )
        Player.ChatSay( colors[ 'red' ], 'Stopping Script' )
        Misc.ScriptStop( 'resource_treasureChestPuller.py' )

    return wandSerial


def NewIdTarget():
    global useIdWand

    if useIdWand:
        wandSerial = equipWand()
        Items.UseItem( wandSerial )
    else:
        Player.UseSkill( 'Item ID' )

    # Wait for target to appaar
    Misc.Pause( 100 )

    # Make sure target has appeared
    if not Target.HasTarget():
        NewIdTarget()


def IdItem( item ):
    itemIdentified = False
    while not itemIdentified:
        # ID the item
        NewIdTarget()
        Target.WaitForTarget( 1500 )
        Target.TargetExecute( item.Serial )

        Misc.Pause( config.journalEntryDelayMilliseconds )

        # Fetch the Journal entries (oldest to newest)
        regularText = Journal.GetTextByType( 'Regular' )

        # Reverse the Journal entries so that we read from newest to oldest
        regularText.Reverse()

        # Read back until the item ID was started to see if it succeeded
        for line in regularText[ 0 : len( regularText ) ]:
            if line == 'What do you wish to appraise and identify?':
                itemIdentified = True
            if line == 'You are not certain...':
                itemIdentified = False


# ID the weapons and armor
for item in mapChest.Contains:
    checkWeight()
    checkDistance()

    if item.ItemID in armorIDs or item.ItemID in shieldIDs or item.ItemID in weaponIDs:
        Journal.Clear()
        IdItem( item )
        Misc.Pause( 1500 )

        goodItem = False
        if any( Journal.Search( itemQuality ) for itemQuality in itemQualitiesToKeep ):
            # Good Stuff
            goodItem = True
        elif any( Journal.Search( slash ) for slash in slashProps ) and any( Journal.Search( sub ) for sub in subSlashProps ):
            # Good Stuff
            goodItem = True

        if goodItem:
            MoveItem( Items, Misc, item, keepBag )
        else:
            if item.Name == 'orc helm' or 'bone' in item.Name:
                MoveItem( Items, Misc, item, trashCan )
            else:
                MoveItem( Items, Misc, item, sellBag )


# Move the trash into the trash can
for item in mapChest.Contains:
    checkDistance()
    checkWeight()
    if item.ItemID in trashIDs or item.ItemID in scrollIDsToTrash:
        MoveItem( Items, Misc, item, trashCan )


Player.ChatSay( msgColor, 'Got it all, let''s bounce!' )
