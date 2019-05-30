'''
Author: TheWarDoctor95
Other Contributors:
Last Contribution By: TheWarDoctor95 - April 26, 2019

Description: Trains Carpentry to its cap
'''

from Scripts.glossary.colors import colors
from Scripts.glossary.crafting.carpentry import FindCarpentryTool, carpentryCraftables
from Scripts.glossary.items.containers import FindTrashBarrel
from Scripts.utilities.items import FindItem, FindNumberOfItems, MoveItem

# Set to serial of bag or 'pet' for the mount that you are on
# Set to None if you don't want to keep slayers
slayerBag = 'pet'
petName = 'Beetlejuice'

def FindPet():
    '''
    Dismounts and finds the pet you were mounted on
    '''

    global petName

    if Player.Mount != None:
        Mobiles.UseMobile( Player.Serial )
        Misc.Pause( 700 )

    petFilter = Mobiles.Filter()
    petFilter.Enabled = True
    petFilter.RangeMin = 0
    petFilter.RangeMax = 1
    petFilter.Name = petName

    pet = Mobiles.ApplyFilter( petFilter )[ 0 ]
    return pet


def TrainCarpentry():
    '''
    Trains Carpentry to its skill cap
    '''

    if Player.GetRealSkillValue( 'Carpentry' ) == Player.GetSkillCap( 'Carpentry' ):
        Player.HeadMessage( colors[ 'green' ], 'Your Carpentry is already at its skill cap!' )
        return

    tool = FindCarpentryTool( Player.Backpack )
    if tool == None:
        Player.HeadMessage( colors[ 'red' ], 'No tools to train with!' )
        return

    trashBarrel = FindTrashBarrel( Items )
    if trashBarrel == None:
        Player.HeadMessage( colors[ 'red' ], 'No trash barrel nearby!' )
        return

    Journal.Clear()
    while not Player.IsGhost and Player.GetRealSkillValue( 'Carpentry' ) < Player.GetSkillCap( 'Carpentry' ):
        # Make sure the tool isn't broken. If it is broken, this will return None
        tool = Items.FindBySerial( tool.Serial )
        if tool == None:
            tool = FindCarpentryTool( Player.Backpack )
            if tool == None:
                Player.HeadMessage( colors[ 'red' ], 'Ran out of tools!' )
                break

        # Select the item to craft
        itemToCraft = None
        if Player.GetRealSkillValue( 'Carpentry' ) < 40.0:
            Player.HeadMessage( colors[ 'red' ], 'Use gold to train with an NPC' )
            break
        elif Player.GetRealSkillValue( 'Carpentry' ) < 68.0:
            itemToCraft = carpentryCraftables[ 'wooden shield' ]
        elif Player.GetRealSkillValue( 'Carpentry' ) < 74.0:
            itemToCraft = carpentryCraftables[ 'fishing pole' ]
        elif Player.GetRealSkillValue( 'Carpentry' ) < 80.0:
            itemToCraft = carpentryCraftables[ 'quarter staff' ]
        else:
            itemToCraft = carpentryCraftables[ 'gnarled staff' ]

        enoughResourcesToCraftWith = True
        numberOfItems = {}
        for resource in itemToCraft.resourcesNeeded:
            if resource == 'boards':
                numberOfBoards = FindNumberOfItems( 0x1BD7, Player.Backpack, 0x0000 )[ 0x1BD7 ]
                numberOfBoards += FindNumberOfItems( 0x1BDD, Player.Backpack, 0x0000 )[ 0x1BDD ]
                if numberOfBoards < itemToCraft.resourcesNeeded[ 'boards' ]:
                    enoughResourcesToCraftWith = False
                    break
            elif resource == 'cloth':
                numberOfItems[ 'cloth' ] = FindNumberOfItems( 0x1766, Player.Backpack, 0x0000 )[ 0x1766 ]
                if numberOfBoards < itemToCraft.resourcesNeeded[ 'cloth' ]:
                    enoughResourcesToCraftWith = False
                    break

        if not enoughResourcesToCraftWith:
            Player.HeadMessage( colors[ 'red' ], 'Out of resources to craft with!' )
            return

        Items.UseItem( tool )
        for path in itemToCraft.gumpPath:
            Gumps.WaitForGump( path.gumpID, 2000 )
            Gumps.SendAction( path.gumpID, path.buttonID )

        # Close the Carpentry gump (signals that crafting has completed, since the gump will have reopened)
        Gumps.WaitForGump( itemToCraft.gumpPath[ 0 ].gumpID, 5000 )
        Gumps.SendAction( itemToCraft.gumpPath[ 0 ].gumpID, 0 )

        # Wait a moment for the item to appear in the player's backpack
        Misc.Pause( 200 )

        # Move the item out of the player's backpack
        itemType = None
        if itemToCraft.name == 'wooden shield':
            itemType = 0x1B7A
        elif itemToCraft.name == 'fishing pole':
            itemType = 0x0000
        elif itemToCraft.name == 'quarter staff':
            itemType = 0x0E89
        elif itemToCraft.name == 'gnarled staff':
            itemType = 0x13F8
        item = FindItem( itemType, Player.Backpack )

        if item != None:
            if slayerBag != None and Journal.SearchByType( 'You have successfully crafted a slayer', 'Regular' ):
                Journal.Clear()
                if slayerBag == 'pet':
                    pet = FindPet()
                    MoveItem( Items, Misc, item, pet.Backpack )
                    Mobiles.UseMobile( pet )
                    Misc.Pause( 500 )
                else:
                    MoveItem( Items, Misc, item, slayerBag )
            else:
                MoveItem( Items, Misc, item, trashBarrel )

# Start Carpentry training
TrainCarpentry()
