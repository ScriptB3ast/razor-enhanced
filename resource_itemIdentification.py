# Set to True to use the Item Identification skill, False to use an Item Identification wand
useSkill = True
# Set to True if you'd like to have the script sort good items and bad items into different boxes
sortItems = True

itemIdentificationDelayMilliseconds = 500

from Scripts.glossary.items.armor import armor
from Scripts.glossary.items.shields import shields
from Scripts.glossary.items.weapons import weapons
from Scripts.utilities.items import MoveItem
from Scripts.glossary.colors import colors
from Scripts import config

itemQualityToKeep = [
    # Strength
    'Vanquishing', 'Power',
    # Property Combos
    'Indestructable/Invulnerability', 'Exceptional/Indestructible', 'Exceptional/Fortified',

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

# Comment out the below lines if you wish to exclude
#itemQualityToKeep.append( 'Surpassingly' ) # +10
#itemQualityToKeep.append( 'Eminently' ) # +15
itemQualityToKeep.append( 'Exceedingly' ) # +20
itemQualityToKeep.append( 'Supremely' ) # +25

containerToIdentify = Target.PromptTarget( 'Select container containing the items to identify' )
containerToIdentify = Items.FindBySerial( containerToIdentify )
if containerToIdentify == None or not containerToIdentify.IsContainer:
    Misc.SendMessage( 'Invalid selection for container to identify! Stopping script', colors[ 'red' ] )
    Stop

Items.UseItem( containerToIdentify )
Misc.Pause( config.dragDelayMilliseconds )

if sortItems:
    if not Misc.CheckSharedValue( 'itemsToKeepBox' ):
        itemsToKeepBox = Target.PromptTarget( 'Select box for items to keep' )
        itemsToKeepBox = Items.FindBySerial( itemsToKeepBox )
        if itemsToKeepBox == None or not itemsToKeepBox.IsContainer:
            Misc.SendMessage( 'Invalid selection for box for items to keep! Stopping script', colors[ 'red' ] )
            Stop
        else:
            Misc.SetSharedValue( 'itemsToKeepBox', itemsToKeepBox.Serial )
    else:
        itemsToKeepBox = Misc.ReadSharedValue( 'itemsToKeepBox' )
        itemsToKeepBox = Items.FindBySerial( itemsToKeepBox )

    if not Misc.CheckSharedValue( 'itemsToSellBox' ):
        itemsToSellBox = Target.PromptTarget( 'Select box for items to sell' )
        itemsToSellBox = Items.FindBySerial( itemsToSellBox )
        if itemsToSellBox == None or not itemsToSellBox.IsContainer:
            Misc.SendMessage( 'Invalid selection for box for items to sell! Stopping script', colors[ 'red' ] )
            Stop
        else:
            Misc.SetSharedValue( 'itemsToSellBox', itemsToSellBox.Serial )
    else:
        itemsToSellBox = Misc.ReadSharedValue( 'itemsToSellBox' )
        itemsToSellBox = Items.FindBySerial( itemsToSellBox )

    Items.UseItem( itemsToKeepBox )
    Misc.Pause( config.dragDelayMilliseconds )
    Items.UseItem( itemsToSellBox )
    Misc.Pause( config.dragDelayMilliseconds )

if not useSkill:
    wand = Target.PromptTarget( 'Select item identification wand' )
    wand = Items.FindBySerial( wand )
    if wand == None:
        Misc.SendMessage( 'Invalid selection for the item identification wand! Stopping script', colors[ 'red' ] )
        Stop

    # Make sure there's nothing in the left hand
    leftHandItem = Player.GetItemOnLayer( 'LeftHand' )
    if leftHandItem != None:
        Player.UnEquipItemByLayer( 'LeftHand' )
        Misc.Pause( config.dragDelayMilliseconds )

    # Equip the wand
    rightHandItem = Player.GetItemOnLayer( 'RightHand' )
    if rightHandItem == None or rightHandItem.Serial != wand:
        Player.EquipItem( wand )
        Misc.Pause( config.dragDelayMilliseconds )

for item in containerToIdentify.Contains:
    Journal.Clear()
    if sortItems:
        itemsToKeepBox = Items.FindBySerial( itemsToKeepBox.Serial )
        if len( itemsToKeepBox.Contains ) == 125:
            Misc.SendMessage( 'Box of items to keep is full! Stopping script', colors[ 'red' ] )
            Misc.RemoveSharedValue( 'itemsToSellBox' )
            Stop

        if itemsToSellBox.Serial != Player.Serial:
            itemsToSellBox = Items.FindBySerial( itemsToSellBox.Serial )
            if len( itemsToSellBox.Contains ) == 125:
                Misc.SendMessage( 'Box of items to sell is full! Stopping script', colors[ 'red' ] )
                Misc.RemoveSharedValue( 'itemsToSellBox' )
                Stop
        else:
            if Player.Weight >= Player.MaxWeight:
                Misc.SendMessage( 'You\'re overweight! Stopping script', colors[ 'red' ] )
                Stop

    if useSkill:
        Player.UseSkill( 'Item ID' )
        Target.WaitForTarget( 2000, True )
        Target.TargetExecute( item )

        # Wait for skill cooldown
        Misc.Pause( 1200 )

        while Journal.SearchByType( 'You are not certain...', 'Regular' ):
            # Failed to ID the item, keep trying until we succeed
            Journal.Clear()

            Player.UseSkill( 'Item ID' )
            Target.WaitForTarget( 2000, True )
            Target.TargetExecute( item )

            # Wait for the skill cooldown
            Misc.Pause( 1200 )
    else:
        Items.UseItem( wand )
        Target.WaitForTarget( 2000, True )
        Target.TargetExecute( item )
        Misc.Pause( config.journalEntryDelayMilliseconds )

    if sortItems:
        keepItem = False
        textInSystem = Journal.GetTextByType( 'System' )
        for itemQuality in itemQualityToKeep:
            if '/' in itemQuality:
                qualities = itemQuality.split( '/' )
                allQualitiesMet = True
                for quality in qualities:
                    if quality not in textInSystem:
                        allQualitiesMet = False

                if allQualitiesMet:
                    keepItem = True
            elif Journal.SearchByType( itemQuality, 'System' ):
                keepItem = True

            if keepItem:
                break

        if Journal.SearchByType( 'Ruin', 'System' ):
            keepItem = False

        if keepItem:
            #Misc.SendMessage( 'keep' )
            MoveItem( Items, Misc, item, itemsToKeepBox )
        else:
            #Misc.SendMessage( 'sell' )
            MoveItem( Items, Misc, item, itemsToSellBox )

    if Journal.SearchByType( 'This item is out of charges', 'Regular' ):
        Misc.SendMessage( 'Wand is out of charges! Stopping script', colors[ 'red' ] )
        Stop

Player.HeadMessage( colors[ 'green' ], 'Done identifying the items!' )
