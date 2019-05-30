from Scripts.glossary.items.containers import FindTrashBarrel
from Scripts.glossary.items.miscellaneous import miscellaneous
from Scripts.glossary.crafting.cartography import cartographyTools, cartographyCraftables
from Scripts.glossary.colors import colors
from Scripts.utilities.items import FindItem, FindNumberOfItems, MoveItem

def FindTool( container ):
    '''
    Searches for a mapmaking tool in the specified container
    '''

    # Find the tool to craft with
    for tool in cartographyTools:
        tool = FindItem( tool.itemID, container )
        if tool != None:
            return tool


def TrainCartography():
    '''
    Trains Cartography to its skill cap
    '''

    if Player.GetRealSkillValue( 'Cartography' ) == Player.GetSkillCap( 'Cartography' ):
        Player.HeadMessage( colors[ 'green' ], 'Your Cartography is already at its skill cap!' )
        return

    tool = FindTool( Player.Backpack )
    if tool == None:
        Player.HeadMessage( colors[ 'red' ], 'No tools to train with!' )
        return

    trashBarrel = FindTrashBarrel( Items )
    if trashBarrel == None:
        Player.HeadMessage( colors[ 'red' ], 'No trash barrel nearby! Please move near a trash barrel so that the maps can be thrown away' )
        return

    while not Player.IsGhost and Player.GetRealSkillValue( 'Cartography' ) < 95.5:
        # Make sure the tool isn't broken. If it is broken, this will return None
        tool = Items.FindBySerial( tool.Serial )
        if tool == None:
            tool = FindTool( Player.Backpack )
            if tool == None:
                Player.HeadMessage( colors[ 'red' ], 'Ran out of tools!' )
                return

        # Select the item to craft
        itemToCraft = None
        if Player.GetSkillValue( 'Cartography' ) < 50.0:
            itemToCraft = cartographyCraftables[ 'local map' ]
        elif Player.GetSkillValue( 'Cartography' ) < 65.0:
            itemToCraft = cartographyCraftables[ 'city map' ]
        elif Player.GetSkillValue( 'Cartography' ) < 99.5:
            itemToCraft = cartographyCraftables[ 'world map' ]
        else:
            Player.HeadMessage( colors[ 'orange' ], 'You will need to finish training Cartography by decoding lvl 3 and 4 treasure maps' )
            return

        blankScrolls = FindNumberOfItems( miscellaneous[ 'blank scroll' ].itemID, Player.Backpack, 0x0000 )
        if blankScrolls[ miscellaneous[ 'blank scroll' ].itemID ] < itemToCraft.resourcesNeeded[ 'blank scroll' ]:
            Player.HeadMessage( colors[ 'red' ], 'Out of resources to craft with!' )
            return

        Items.UseItem( tool )
        for path in itemToCraft.gumpPath:
            Gumps.WaitForGump( path.gumpID, 2000 )
            Gumps.SendAction( path.gumpID, path.buttonID )

        # Wait for crafting to finish and close the gump
        Gumps.WaitForGump( 949095101, 2000 )
        Gumps.SendAction( 949095101, 0 )

        map = FindItem( miscellaneous[ 'map' ].itemID, Player.Backpack )
        if map != None:
            MoveItem( Items, Misc, map, trashBarrel )

    if not Player.IsGhost:
        Player.HeadMessage( colors[ 'orange' ], 'You will need to finish training Cartography by decoding lvl 3 and 4 treasure maps' )

# Start Cartography training
TrainCartography()
