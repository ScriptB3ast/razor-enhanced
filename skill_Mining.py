from Scripts.utilities.items import FindItem, FindNumberOfItems, MoveItem
from Scripts.glossary.items.ores import ores
from Scripts.glossary.colors import colors

useMount = True
usePetStorage = True

def Mount():
    Misc.Pause( 700 )
    mountSerial = Misc.ReadSharedValue( 'mount' )
    if mountSerial != None:
        mount = Mobiles.FindBySerial( Misc.ReadSharedValue( 'mount' ) )
        if mount != None:
            Mobiles.UseMobile( mount )


def MoveOreToPet():
    petSerial = Misc.ReadSharedValue( 'petForStorage1' )
    if petSerial != None:
        pet = Mobiles.FindBySerial( Misc.ReadSharedValue( 'petForStorage1' ) )

    if pet == None:
        Player.HeadMessage( colors[ 'red' ], 'Could not find storage pet!' )

    for ore in ores:
        oreStack = FindItem( ores[ ore ].itemID, Player.Backpack, ores[ ore ].color )
        while oreStack != None:
            Misc.SendMessage( 'Moving stack of %s to pet' % ores[ ore ].name )
            MoveItem( Items, Misc, oreStack, pet.Backpack )

            oreStack = Items.FindBySerial( oreStack.Serial )
            if oreStack != None and oreStack.RootContainer != Player.Serial:
                # The stack still exists, but was moved to the pet
                oreStack = None

            if oreStack == None:
                continue

            # Stack wasn't moved, so the pet is either overweight or nearly overweight
            # Move as much as we can over to the pet by moving one item from the stack at a time
            amountBeforeMove = FindNumberOfItems( ores[ ore ].itemID, Player.Backpack, ores[ ore ].color )
            MoveItem( Items, Misc, oreStack, pet.Backpack, 1 )
            oreStack = Items.FindBySerial( oreStack.Serial )
            amountInBag = FindNumberOfItems( ores[ ore ].itemID, Player.Backpack, ores[ ore ].color )
            while amountInBag != amountBeforeMove:
                amountBeforeMove = amountInBag
                Misc.SendMessage( '%s' % oreStack )
                MoveItem( Items, Misc, oreStack, pet.Backpack, 1 )
                oreStack = Items.FindBySerial( oreStack.Serial )
                amountInBag = FindNumberOfItems( ores[ ore ].itemID, Player.Backpack, ores[ ore ].color )

            if Player.Weight <= Player.MaxWeight:
                Player.HeadMessage( colors[ 'green' ], 'Moved enough to pet for you to move normally' )

            Mobiles.Message( pet, colors[ 'red' ], 'Pet is overweight!' )
            # There is still some ore in the player's bag
            return False

    # We were able to move all of the ore
    return True


def Mine():
    global useMount
    global usePetStorage

    mount = None
    mountSerial = None
    pet = None
    petSerial = None

    if usePetStorage:
        petSerial = Misc.ReadSharedValue( 'petForStorage1' )
        if petSerial != None:
            pet = Mobiles.FindBySerial( Misc.ReadSharedValue( 'petForStorage1' ) )

    if Player.Mount != None:
        # We need to dismount to be able to mine
        Mobiles.UseMobile( Player.Serial )
        Misc.Pause( 1000 )

    Journal.Clear()
    while ( not Journal.SearchByName( 'There is no metal here to mine.', 'System' ) and
            not Journal.SearchByName( 'Target cannot be seen.', 'System' ) and
            not Journal.SearchByName( 'You can\'t mine there.', 'System' ) ):
        if Player.Weight <= Player.MaxWeight:
            pickaxe = FindItem( 0x0E86, Player.Backpack )
            if pickaxe == None:
                Player.HeadMessage( colors[ 'red' ], 'You\'re out of pickaxes!' )
                break

            Items.UseItem( pickaxe )
            Target.WaitForTarget( 2000, True )
            Target.TargetExecuteRelative( Player.Serial, 1 )

            Misc.Pause( 500 )
            if Journal.SearchByType( 'Target cannot be seen.', 'Regular' ):
                Journal.Clear()
                break

            # Wait for the mining animation to complete and then call the guards in case an elemental appears
            Misc.Pause( 500 )
            #Player.ChatSay( 90, 'guards' )
        else:
            Player.HeadMessage( colors[ 'red' ], 'You\'re overweight!' )

        # If we're overweight, move ore into a pet
        if usePetStorage and Player.Weight > Player.MaxWeight:
            Misc.SendMessage( 'Player overweight! Moving ore to pet.', colors[ 'cyan' ] )
            movedAllOre = MoveOreToPet()
            if not movedAllOre:
                if useMount:
                    Mount()
                return

        # Wait a little bit so that the while loop doesn't consume as much CPU
        Misc.Pause( 50 )

    Player.HeadMessage( colors[ 'red' ], 'No more ore to mine here!' )
    if useMount:
        Mount()


if useMount:
    if not Misc.CheckSharedValue( 'mount' ):
        if Player.Mount != None:
            mount = Player.Mount.Serial
        else:
            mount = Target.PromptTarget( 'Select your mount' )
        Misc.SetSharedValue( 'mount', mount )

if usePetStorage:
    if not Misc.CheckSharedValue( 'petForStorage1' ):
        pet = Target.PromptTarget( 'Select pet to store ore in' )
        Misc.SetSharedValue( 'petForStorage1', pet )

# Start mining
Mine()
#MoveOreToPet()
