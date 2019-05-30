from Scripts.glossary.crafting.craftable import Craftable
from Scripts.glossary.items.tools import tools
from Scripts.utilities.gumps import GumpSelection
from Scripts.utilities.items import FindItem

tinkeringTools = [ tools[ 'tinker\'s tools' ], tools[ 'tool kit' ] ]

def FindTinkeringTool( container ):
    '''
    Searches for a carpentry tool in the specified container
    '''

    global tinkeringTools

    # Find the tool to craft with
    for tool in tinkeringTools:
        tool = FindItem( tool.itemID, container )
        if tool != None:
            return tool


class TinkeringCraftable ( Craftable ):
    name = None
    retainsMark = None
    retainsColor = None
    minSkill = None
    resourcesNeeded = None
    gumpPath = None

    def __init__ ( self, name, retainsMark, retainsColor, minSkill, resourcesNeeded, gumpPath ):
        self.retainsMark = retainsMark
        self.retainsColor = retainsColor

        # Invoking __init__ of parent class
        Craftable.__init__( self, name, minSkill, resourcesNeeded, gumpPath )


tinkeringCraftables = {
    ### Wooden Items: Gump Button 1 ###
    'jointing plane': TinkeringCraftable(
        name = 'jointing plane',
        retainsMark = True,
        retainsColor = False,
        minSkill = { 'tinkering': 0.0 },
        resourcesNeeded = { 'boards': 4 },
        gumpPath = ( GumpSelection( 949095101, 1 ), GumpSelection( 949095101, 2 ) )
    ),
    'moulding planes': TinkeringCraftable(
        name = 'moulding planes',
        retainsMark = True,
        retainsColor = False,
        minSkill = { 'tinkering': 0.0 },
        resourcesNeeded = { 'boards': 4 },
        gumpPath = ( GumpSelection( 949095101, 1 ), GumpSelection( 949095101, 9 ) )
    ),
    'smoothing plane': TinkeringCraftable(
        name = 'smoothing plane',
        retainsMark = True,
        retainsColor = False,
        minSkill = { 'tinkering': 0.0 },
        resourcesNeeded = { 'boards': 4 },
        gumpPath = ( GumpSelection( 949095101, 1 ), GumpSelection( 949095101, 16 ) )
    ),
    'clock frame': TinkeringCraftable(
        name = 'clock frame',
        retainsMark = False,
        retainsColor = False,
        minSkill = { 'tinkering': 0.0 },
        resourcesNeeded = { 'boards': 6 },
        gumpPath = ( GumpSelection( 949095101, 1 ), GumpSelection( 949095101, 23 ) )
    ),
    'axle': TinkeringCraftable(
        name = 'axle',
        retainsMark = False,
        retainsColor = False,
        minSkill = { 'tinkering': 0.0 },
        resourcesNeeded = { 'boards': 2 },
        gumpPath = ( GumpSelection( 949095101, 1 ), GumpSelection( 949095101, 30 ) )
    ),
    'rolling pin': TinkeringCraftable(
        name = 'rolling pin',
        retainsMark = True,
        retainsColor = False,
        minSkill = { 'tinkering': 0.0 },
        resourcesNeeded = { 'boards': 5 },
        gumpPath = ( GumpSelection( 949095101, 1 ), GumpSelection( 949095101, 37 ) )
    ),


    ### Tools: Gump Button 8 ###
    'scissors': TinkeringCraftable(
        name = 'scissors',
        retainsMark = False,
        retainsColor = False,
        minSkill = { 'tinkering': 5.0 },
        resourcesNeeded = { 'ingots': 2 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 2 ) )
    ),
    'mortar and pestle': TinkeringCraftable(
        name = 'mortar and pestle',
        retainsMark = True,
        retainsColor = False,
        minSkill = { 'tinkering': 20.0 },
        resourcesNeeded = { 'ingots': 3 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 9 ) )
    ),
    'scorp': TinkeringCraftable(
        name = 'scorp',
        retainsMark = True,
        retainsColor = False,
        minSkill = { 'tinkering': 30.0 },
        resourcesNeeded = { 'ingots': 2 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 16 ) )
    ),
    'tinker\'s tools': TinkeringCraftable(
        name = 'tinker\'s tools',
        retainsMark = True,
        retainsColor = False,
        minSkill = { 'tinkering': 10.0 },
        resourcesNeeded = { 'ingots': 2 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 23 ) )
    ),
    'hatchet': TinkeringCraftable(
        name = 'hatchet',
        retainsMark = True,
        retainsColor = True,
        minSkill = { 'tinkering': 30.0 },
        resourcesNeeded = { 'ingots': 4 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 30 ) )
    ),
    'draw knife': TinkeringCraftable(
        name = 'draw knife',
        retainsMark = True,
        retainsColor = False,
        minSkill = { 'tinkering': 30.0 },
        resourcesNeeded = { 'ingots': 2 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 37 ) )
    ),
    'sewing kit': TinkeringCraftable(
        name = 'sewing kit',
        retainsMark = True,
        retainsColor = False,
        minSkill = { 'tinkering': 10.0 },
        resourcesNeeded = { 'ingots': 2 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 44 ) )
    ),
    'saw': TinkeringCraftable(
        name = 'saw',
        retainsMark = True,
        retainsColor = False,
        minSkill = { 'tinkering': 30.0 },
        resourcesNeeded = { 'ingots': 4 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 51 ) )
    ),
    'dovetail saw': TinkeringCraftable(
        name = 'dovetail saw',
        retainsMark = True,
        retainsColor = False,
        minSkill = { 'tinkering': 30.0 },
        resourcesNeeded = { 'ingots': 4 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 58 ) )
    ),
    'froe': TinkeringCraftable(
        name = 'froe',
        retainsMark = True,
        retainsColor = False,
        minSkill = { 'tinkering': 30.0 },
        resourcesNeeded = { 'ingots': 2 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 65 ) )
    ),
    'shovel': TinkeringCraftable(
        name = 'shovel',
        retainsMark = True,
        retainsColor = False,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 4 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 72 ) )
    ),
    'hammer': TinkeringCraftable(
        name = 'hammer',
        retainsMark = True,
        retainsColor = False,
        minSkill = { 'tinkering': 30.0 },
        resourcesNeeded = { 'ingots': 1 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 79 ) )
    ),
    'tongs': TinkeringCraftable(
        name = 'tongs',
        retainsMark = True,
        retainsColor = False,
        minSkill = { 'tinkering': 35.0 },
        resourcesNeeded = { 'ingots': 1 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 86 ) )
    ),
    'smith\'s hammer': TinkeringCraftable(
        name = 'smith\'s hammer',
        retainsMark = True,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 4 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 93 ) )
    ),
    'sledge hammer': TinkeringCraftable(
        name = 'sledge hammer',
        retainsMark = True,
        retainsColor = False,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 4 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 100 ) )
    ),
    'inshave': TinkeringCraftable(
        name = 'inshave',
        retainsMark = True,
        retainsColor = False,
        minSkill = { 'tinkering': 30.0 },
        resourcesNeeded = { 'ingots': 2 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 107 ) )
    ),
    'pickaxe': TinkeringCraftable(
        name = 'pickaxe',
        retainsMark = True,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 4 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 114 ) )
    ),
    'lockpick': TinkeringCraftable(
        name = 'lockpick',
        retainsMark = False,
        retainsColor = False,
        minSkill = { 'tinkering': 45.0 },
        resourcesNeeded = { 'ingots': 1 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 121 ) )
    ),
    'skillet': TinkeringCraftable(
        name = 'skillet',
        retainsMark = True,
        retainsColor = False,
        minSkill = { 'tinkering': 30.0 },
        resourcesNeeded = { 'ingots': 4 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 128 ) )
    ),
    'flour sifter': TinkeringCraftable(
        name = 'flour sifter',
        retainsMark = True,
        retainsColor = False,
        minSkill = { 'tinkering': 50.0 },
        resourcesNeeded = { 'ingots': 3 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 135 ) )
    ),
    'fletcher\'s tools': TinkeringCraftable(
        name = 'fletcher\'s tools',
        retainsMark = True,
        retainsColor = False,
        minSkill = { 'tinkering': 35.0 },
        resourcesNeeded = { 'ingots': 3 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 142 ) )
    ),
    'mapmaker\'s pen': TinkeringCraftable(
        name = 'mapmaker\'s pen',
        retainsMark = True,
        retainsColor = False,
        minSkill = { 'tinkering': 25.0 },
        resourcesNeeded = { 'ingots': 1 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 149 ) )
    ),
    'scibe\'s pen': TinkeringCraftable(
        name = 'scibe\'s pen',
        retainsMark = True,
        retainsColor = False,
        minSkill = { 'tinkering': 25.0 },
        resourcesNeeded = { 'ingots': 1 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 156 ) )
    ),
    'a foraging kit': TinkeringCraftable(
        name = 'a foraging kit',
        retainsMark = True,
        retainsColor = False,
        minSkill = { 'tinkering': 85.0 },
        resourcesNeeded = { 'ingots': 20 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 163 ) )
    ),


    ### Parts: Gump Button 15 ###
    'gears': TinkeringCraftable(
        name = 'gears',
        retainsMark = False,
        retainsColor = False,
        minSkill = { 'tinkering': 5.0 },
        resourcesNeeded = { 'ingots': 2 },
        gumpPath = ( GumpSelection( 949095101, 15 ), GumpSelection( 949095101, 2 ) )
    ),
    'clock parts': TinkeringCraftable(
        name = 'clock parts',
        retainsMark = False,
        retainsColor = False,
        minSkill = { 'tinkering': 25.0 },
        resourcesNeeded = { 'ingots': 1 },
        gumpPath = ( GumpSelection( 949095101, 15 ), GumpSelection( 949095101, 9 ) )
    ),
    'barrel tap': TinkeringCraftable(
        name = 'barrel tap',
        retainsMark = False,
        retainsColor = False,
        minSkill = { 'tinkering': 35.0 },
        resourcesNeeded = { 'ingots': 2 },
        gumpPath = ( GumpSelection( 949095101, 15 ), GumpSelection( 949095101, 16 ) )
    ),
    'springs': TinkeringCraftable(
        name = 'springs',
        retainsMark = False,
        retainsColor = False,
        minSkill = { 'tinkering': 5.0 },
        resourcesNeeded = { 'ingots': 2 },
        gumpPath = ( GumpSelection( 949095101, 15 ), GumpSelection( 949095101, 23 ) )
    ),
    'sextant parts': TinkeringCraftable(
        name = 'sextant parts',
        retainsMark = False,
        retainsColor = False,
        minSkill = { 'tinkering': 30.0 },
        resourcesNeeded = { 'ingots': 4 },
        gumpPath = ( GumpSelection( 949095101, 15 ), GumpSelection( 949095101, 30 ) )
    ),
    'barrel hoops': TinkeringCraftable(
        name = 'barrel hoops',
        retainsMark = False,
        retainsColor = False,
        minSkill = { 'tinkering': 0.0 },
        resourcesNeeded = { 'ingots': 5 },
        gumpPath = ( GumpSelection( 949095101, 15 ), GumpSelection( 949095101, 37 ) )
    ),
    'hinge': TinkeringCraftable(
        name = 'hinge',
        retainsMark = False,
        retainsColor = False,
        minSkill = { 'tinkering': 5.0 },
        resourcesNeeded = { 'ingots': 2 },
        gumpPath = ( GumpSelection( 949095101, 15 ), GumpSelection( 949095101, 44 ) )
    ),

    ### Utensils: Gump Button 22 ###
    'butcher knife': TinkeringCraftable(
        name = 'butcher knife',
        retainsMark = True,
        retainsColor = True,
        minSkill = { 'tinkering': 25.0 },
        resourcesNeeded = { 'ingots': 2 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 2 ) )
    ),
    'spoon (left)': TinkeringCraftable(
        name = 'spoon (left)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 0.0 },
        resourcesNeeded = { 'ingots': 1 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 9 ) )
    ),
    'spoon (right)': TinkeringCraftable(
        name = 'spoon (right)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 0.0 },
        resourcesNeeded = { 'ingots': 1 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 16 ) )
    ),
    'plate': TinkeringCraftable(
        name = 'plate',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 0.0 },
        resourcesNeeded = { 'ingots': 1 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 23 ) )
    ),
    'fork (left)': TinkeringCraftable(
        name = 'fork (left)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 0.0 },
        resourcesNeeded = { 'ingots': 1 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 30 ) )
    ),
    'fork (right)': TinkeringCraftable(
        name = 'fork (right)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 0.0 },
        resourcesNeeded = { 'ingots': 1 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 37 ) )
    ),
    'cleaver': TinkeringCraftable(
        name = 'cleaver',
        retainsMark = True,
        retainsColor = True,
        minSkill = { 'tinkering': 20.0 },
        resourcesNeeded = { 'ingots': 3 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 44 ) )
    ),
    'knife (left)': TinkeringCraftable(
        name = 'knife (left)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 0.0 },
        resourcesNeeded = { 'ingots': 1 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 51 ) )
    ),
    'knife (right)': TinkeringCraftable(
        name = 'knife (right)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 0.0 },
        resourcesNeeded = { 'ingots': 1 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 58 ) )
    ),
    'goblet': TinkeringCraftable(
        name = 'goblet',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 10.0 },
        resourcesNeeded = { 'ingots': 2 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 65 ) )
    ),
    'pewter mug': TinkeringCraftable(
        name = 'pewter mug',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 10.0 },
        resourcesNeeded = { 'ingots': 2 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 72 ) )
    ),
    'skinning knife': TinkeringCraftable(
        name = 'skinning knife',
        retainsMark = True,
        retainsColor = True,
        minSkill = { 'tinkering': 25.0 },
        resourcesNeeded = { 'ingots': 2 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 79 ) )
    ),


    ### Miscellaneous: Gump Button 29 ###
    'key ring': TinkeringCraftable(
        name = 'key ring',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 10.0 },
        resourcesNeeded = { 'ingots': 2 },
        gumpPath = ( GumpSelection( 949095101, 29 ), GumpSelection( 949095101, 2 ) )
    ),
    'candelabra': TinkeringCraftable(
        name = 'candelabra',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 55.0 },
        resourcesNeeded = { 'ingots': 4 },
        gumpPath = ( GumpSelection( 949095101, 29 ), GumpSelection( 949095101, 9 ) )
    ),
    'scales': TinkeringCraftable(
        name = 'scales',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 60.0 },
        resourcesNeeded = { 'ingots': 4 },
        gumpPath = ( GumpSelection( 949095101, 29 ), GumpSelection( 949095101, 16 ) )
    ),
    'iron key': TinkeringCraftable(
        name = 'iron key',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 20.0 },
        resourcesNeeded = { 'ingots': 3 },
        gumpPath = ( GumpSelection( 949095101, 29 ), GumpSelection( 949095101, 23 ) )
    ),
    'globe': TinkeringCraftable(
        name = 'globe',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 55.0 },
        resourcesNeeded = { 'ingots': 4 },
        gumpPath = ( GumpSelection( 949095101, 29 ), GumpSelection( 949095101, 30 ) )
    ),
    'spyglass': TinkeringCraftable(
        name = 'spyglass',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 60.0 },
        resourcesNeeded = { 'ingots': 4 },
        gumpPath = ( GumpSelection( 949095101, 29 ), GumpSelection( 949095101, 37 ) )
    ),
    'lantern': TinkeringCraftable(
        name = 'lantern',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 30.0 },
        resourcesNeeded = { 'ingots': 4 },
        gumpPath = ( GumpSelection( 949095101, 29 ), GumpSelection( 949095101, 44 ) )
    ),
    'heating stand': TinkeringCraftable(
        name = 'heating stand',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 60.0 },
        resourcesNeeded = { 'ingots': 4 },
        gumpPath = ( GumpSelection( 949095101, 29 ), GumpSelection( 949095101, 51 ) )
    ),


    ### Jewelry: Gump Button 36 ###
    'star sapphire ring': TinkeringCraftable(
        name = 'star sapphire ring',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Star Sapphires': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 2 ) )
    ),
    'star sapphire necklace (silver)': TinkeringCraftable(
        name = 'star sapphire necklace (silver)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Star Sapphires': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 9 ) )
    ),
    'star sapphire necklace (jewelled)': TinkeringCraftable(
        name = 'star sapphire necklace (jewelled)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Star Sapphires': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 16 ) )
    ),
    'star sapphire earrings': TinkeringCraftable(
        name = 'star sapphire earrings',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Star Sapphires': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 23 ) )
    ),
    'star sapphire necklace (golden)': TinkeringCraftable(
        name = 'star sapphire necklace (golden)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Star Sapphires': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 30 ) )
    ),
    'star sapphire bracelet': TinkeringCraftable(
        name = 'star sapphire bracelet',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Star Sapphires': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 37 ) )
    ),
    'emerald ring': TinkeringCraftable(
        name = 'emerald ring',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Emeralds': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 44 ) )
    ),
    'emerald necklace (silver)': TinkeringCraftable(
        name = 'emerald necklace (silver)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Emeralds': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 51 ) )
    ),
    'emerald necklace (jewelled)': TinkeringCraftable(
        name = 'emerald necklace (jewelled)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Emeralds': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 58 ) )
    ),
    'emerald earrings': TinkeringCraftable(
        name = 'emerald earrings',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Emeralds': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 65 ) )
    ),
    'emerald necklace (golden)': TinkeringCraftable(
        name = 'emerald necklace (golden)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Emeralds': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 72 ) )
    ),
    'emerald bracelet': TinkeringCraftable(
        name = 'emerald bracelet',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Emeralds': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 79 ) )
    ),
    'sapphire ring': TinkeringCraftable(
        name = 'sapphire ring',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Sapphires': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 86 ) )
    ),
    'sapphire necklace (silver)': TinkeringCraftable(
        name = 'sapphire necklace (silver)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Sapphires': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 93 ) )
    ),
    'sapphire necklace (jewelled)': TinkeringCraftable(
        name = 'sapphire necklace (jewelled)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Sapphires': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 100 ) )
    ),
    'sapphire earrings': TinkeringCraftable(
        name = 'sapphire earrings',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Sapphires': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 107 ) )
    ),
    'sapphire necklace (golden)': TinkeringCraftable(
        name = 'sapphire necklace (golden)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Sapphires': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 114 ) )
    ),
    'sapphire bracelet': TinkeringCraftable(
        name = 'sapphire bracelet',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Sapphires': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 121 ) )
    ),
    'ruby ring': TinkeringCraftable(
        name = 'ruby ring',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Rubies': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 128 ) )
    ),
    'ruby necklace (silver)': TinkeringCraftable(
        name = 'ruby necklace (silver)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Rubies': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 135 ) )
    ),
    'ruby necklace (jewelled)': TinkeringCraftable(
        name = 'ruby necklace (jewelled)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Rubies': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 142 ) )
    ),
    'ruby earrings': TinkeringCraftable(
        name = 'ruby earrings',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Rubies': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 149 ) )
    ),
    'ruby necklace (golden)': TinkeringCraftable(
        name = 'ruby necklace (golden)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Rubies': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 156 ) )
    ),
    'ruby bracelet': TinkeringCraftable(
        name = 'ruby bracelet',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Rubies': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 163 ) )
    ),
    'citrine ring': TinkeringCraftable(
        name = 'citrine ring',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Citrines': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 170 ) )
    ),
    'citrine necklace (silver)': TinkeringCraftable(
        name = 'citrine necklace (silver)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Citrines': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 177 ) )
    ),
    'citrine necklace (jewelled)': TinkeringCraftable(
        name = 'citrine necklace (jewelled)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Citrines': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 184 ) )
    ),
    'citrine earrings': TinkeringCraftable(
        name = 'citrine earrings',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Citrines': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 191 ) )
    ),
    'citrine necklace (golden)': TinkeringCraftable(
        name = 'citrine necklace (golden)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Citrines': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 198 ) )
    ),
    'citrine bracelet': TinkeringCraftable(
        name = 'citrine bracelet',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Citrines': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 205 ) )
    ),
    'amethyst ring': TinkeringCraftable(
        name = 'amethyst ring',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Amethysts': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 212 ) )
    ),
    'amethyst necklace (silver)': TinkeringCraftable(
        name = 'amethyst necklace (silver)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Amethysts': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 219 ) )
    ),
    'amethyst necklace (jewelled)': TinkeringCraftable(
        name = 'amethyst necklace (jewelled)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Amethysts': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 226 ) )
    ),
    'amethyst earrings': TinkeringCraftable(
        name = 'amethyst earrings',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Amethysts': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 233 ) )
    ),
    'amethyst necklace (golden)': TinkeringCraftable(
        name = 'amethyst necklace (golden)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Amethysts': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 240 ) )
    ),
    'amethyst bracelet': TinkeringCraftable(
        name = 'amethyst bracelet',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Amethysts': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 247 ) )
    ),
    'tourmaline ring': TinkeringCraftable(
        name = 'tourmaline ring',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Tourmalines': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 254 ) )
    ),
    'tourmaline necklace (silver)': TinkeringCraftable(
        name = 'tourmaline necklace (silver)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Tourmalines': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 261 ) )
    ),
    'tourmaline necklace (jewelled)': TinkeringCraftable(
        name = 'tourmaline necklace (jewelled)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Tourmalines': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 268 ) )
    ),
    'tourmaline earrings': TinkeringCraftable(
        name = 'tourmaline earrings',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Tourmalines': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 275 ) )
    ),
    'tourmaline necklace (golden)': TinkeringCraftable(
        name = 'tourmaline necklace (golden)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Tourmalines': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 282 ) )
    ),
    'tourmaline bracelet': TinkeringCraftable(
        name = 'tourmaline bracelet',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Tourmalines': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 289 ) )
    ),
    'amber ring': TinkeringCraftable(
        name = 'amber ring',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Amber': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 296 ) )
    ),
    'amber necklace (silver)': TinkeringCraftable(
        name = 'amber necklace (silver)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Amber': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 303 ) )
    ),
    'amber necklace (jewelled)': TinkeringCraftable(
        name = 'amber necklace (jewelled)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Amber': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 310 ) )
    ),
    'amber earrings': TinkeringCraftable(
        name = 'amber earrings',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Amber': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 317 ) )
    ),
    'amber necklace (golden)': TinkeringCraftable(
        name = 'amber necklace (golden)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Amber': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 324 ) )
    ),
    'amber bracelet': TinkeringCraftable(
        name = 'amber bracelet',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Amber': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 331 ) )
    ),
    'diamond ring': TinkeringCraftable(
        name = 'diamond ring',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Diamonds': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 338 ) )
    ),
    'diamond necklace (silver)': TinkeringCraftable(
        name = 'diamond necklace (silver)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Diamonds': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 345 ) )
    ),
    'diamond necklace (jewelled)': TinkeringCraftable(
        name = 'diamond necklace (jewelled)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Diamonds': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 352 ) )
    ),
    'diamond earrings': TinkeringCraftable(
        name = 'diamond earrings',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Diamonds': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 359 ) )
    ),
    'diamond necklace (golden)': TinkeringCraftable(
        name = 'diamond necklace (golden)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Diamonds': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 366 ) )
    ),
    'diamond bracelet': TinkeringCraftable(
        name = 'diamond bracelet',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'tinkering': 40.0 },
        resourcesNeeded = { 'ingots': 2, 'Diamonds': 1 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 373 ) )
    ),


    ### Assemblies: Gump Button 43 ###
    'axle with gears': TinkeringCraftable(
        name = 'axle with gears',
        retainsMark = False,
        retainsColor = False,
        minSkill = { 'tinkering': 0.0 },
        resourcesNeeded = { 'axle': 1, 'gears': 1 },
        gumpPath = ( GumpSelection( 949095101, 43 ), GumpSelection( 949095101, 2 ) )
    ),
    'clock parts': TinkeringCraftable(
        name = 'clock parts',
        retainsMark = False,
        retainsColor = False,
        minSkill = { 'tinkering': 0.0 },
        resourcesNeeded = { 'axle with gears': 1, 'springs': 1 },
        gumpPath = ( GumpSelection( 949095101, 43 ), GumpSelection( 949095101, 9 ) )
    ),
    'sextant parts': TinkeringCraftable(
        name = 'sextant parts',
        retainsMark = False,
        retainsColor = False,
        minSkill = { 'tinkering': 0.0 },
        resourcesNeeded = { 'axle with gears': 1, 'hinge': 1 },
        gumpPath = ( GumpSelection( 949095101, 43 ), GumpSelection( 949095101, 16 ) )
    ),
    'clock (right)': TinkeringCraftable(
        name = 'clock (right)',
        retainsMark = False,
        retainsColor = False,
        minSkill = { 'tinkering': 0.0 },
        resourcesNeeded = { 'clock frame': 1, 'clock parts': 1 },
        gumpPath = ( GumpSelection( 949095101, 43 ), GumpSelection( 949095101, 23 ) )
    ),
    'clock (left)': TinkeringCraftable(
        name = 'clock (left)',
        retainsMark = False,
        retainsColor = False,
        minSkill = { 'tinkering': 0.0 },
        resourcesNeeded = { 'clock frame': 1, 'clock parts': 1 },
        gumpPath = ( GumpSelection( 949095101, 43 ), GumpSelection( 949095101, 30 ) )
    ),
    'sextant': TinkeringCraftable(
        name = 'sextant',
        retainsMark = False,
        retainsColor = False,
        minSkill = { 'tinkering': 0.0 },
        resourcesNeeded = { 'sextant parts': 1 },
        gumpPath = ( GumpSelection( 949095101, 43 ), GumpSelection( 949095101, 37 ) )
    ),
    'potion keg': TinkeringCraftable(
        name = 'potion keg',
        retainsMark = False,
        retainsColor = False,
        minSkill = { 'tinkering': 75.0 },
        resourcesNeeded = { 'empty keg': 1, 'empty bottle': 10, 'barrel lid': 1, 'barrel tap': 1 },
        gumpPath = ( GumpSelection( 949095101, 43 ), GumpSelection( 949095101, 44 ) )
    ),
    'crystal workbench': TinkeringCraftable(
        name = 'crystal workbench',
        retainsMark = False,
        retainsColor = False,
        minSkill = { 'tinkering': 115.0 },
        resourcesNeeded = {
            'Aqua Crystal Fragment': 1,
            'Blue Crystal Fragment': 1,
            'Green Crystal Fragment': 1,
            'Light Crystal Fragment': 1,
            'Orange Crystal Fragment': 1,
            'Pink Crystal Fragment': 1
        },
        gumpPath = ( GumpSelection( 949095101, 43 ), GumpSelection( 949095101, 51 ) )
    ),


    ### Traps: Gump Button 50 ###
    'dart trap': TinkeringCraftable(
        name = 'dart trap',
        retainsMark = False,
        retainsColor = False,
        minSkill = { 'tinkering': 30.0 },
        resourcesNeeded = { 'ingots': 1, 'crossbow bolt': 1 },
        gumpPath = ( GumpSelection( 949095101, 50 ), GumpSelection( 949095101, 2 ) )
    ),
    'poison trap': TinkeringCraftable(
        name = 'poison trap',
        retainsMark = False,
        retainsColor = False,
        minSkill = { 'tinkering': 30.0 },
        resourcesNeeded = { 'ingots': 1, 'green potions': 1 },
        gumpPath = ( GumpSelection( 949095101, 50 ), GumpSelection( 949095101, 9 ) )
    ),
    'explosion trap': TinkeringCraftable(
        name = 'explosion trap',
        retainsMark = False,
        retainsColor = False,
        minSkill = { 'tinkering': 55.0 },
        resourcesNeeded = { 'ingots': 1, 'purple potions': 1 },
        gumpPath = ( GumpSelection( 949095101, 50 ), GumpSelection( 949095101, 16 ) )
    ),
    'faction gas trap': TinkeringCraftable(
        name = 'faction gas trap',
        retainsMark = False,
        retainsColor = False,
        minSkill = { 'tinkering': 65.0 },
        resourcesNeeded = { 'faction silver': 1000, 'ingots': 10, 'green potions': 1 },
        gumpPath = ( GumpSelection( 949095101, 50 ), GumpSelection( 949095101, 23 ) )
    ),
    'faction explosion trap': TinkeringCraftable(
        name = 'faction explosion trap',
        retainsMark = False,
        retainsColor = False,
        minSkill = { 'tinkering': 65.0 },
        resourcesNeeded = { 'faction silver': 1000, 'ingots': 10, 'purple potions': 1 },
        gumpPath = ( GumpSelection( 949095101, 50 ), GumpSelection( 949095101, 30 ) )
    ),
    'faction saw trap': TinkeringCraftable(
        name = 'faction saw trap',
        retainsMark = False,
        retainsColor = False,
        minSkill = { 'tinkering': 65.0 },
        resourcesNeeded = { 'faction silver': 1000, 'ingots': 10, 'gears': 1 },
        gumpPath = ( GumpSelection( 949095101, 50 ), GumpSelection( 949095101, 37 ) )
    ),
    'faction spike trap': TinkeringCraftable(
        name = 'faction spike trap',
        retainsMark = False,
        retainsColor = False,
        minSkill = { 'tinkering': 65.0 },
        resourcesNeeded = { 'faction silver': 1000, 'ingots': 10, 'springs': 1 },
        gumpPath = ( GumpSelection( 949095101, 50 ), GumpSelection( 949095101, 44 ) )
    ),
    'faction trap removal kit': TinkeringCraftable(
        name = 'faction trap removal kit',
        retainsMark = False,
        retainsColor = False,
        minSkill = { 'tinkering': 90.0 },
        resourcesNeeded = { 'faction silver': 500, 'ingots': 10 },
        gumpPath = ( GumpSelection( 949095101, 50 ), GumpSelection( 949095101, 51 ) )
    ),


    ### Ship Tools: Gump Button 57 ###
    'a repair kit': TinkeringCraftable(
        name = 'a repair kit',
        retainsMark = False,
        retainsColor = False,
        minSkill = { 'tinkering': 85.0 },
        resourcesNeeded = { 'ingots': 100 },
        gumpPath = ( GumpSelection( 949095101, 57 ), GumpSelection( 949095101, 2 ) )
    ),
    'a superb repair kit': TinkeringCraftable(
        name = 'a superb repair kit',
        retainsMark = False,
        retainsColor = False,
        minSkill = { 'tinkering': 105.0 },
        resourcesNeeded = { 'ingots': 400 },
        gumpPath = ( GumpSelection( 949095101, 57 ), GumpSelection( 949095101, 9 ) )
    ),


    ### Ship Upgrades: Gump Button 64 ###
    'Fishing Trawler': TinkeringCraftable(
        name = 'Fishing Trawler',
        retainsMark = False,
        retainsColor = False,
        minSkill = { 'tinkering': 85.0 },
        resourcesNeeded = { 'ingots': 1000 },
        gumpPath = ( GumpSelection( 949095101, 64 ), GumpSelection( 949095101, 2 ) )
    ),
    'Improved Cannons': TinkeringCraftable(
        name = 'Improved Cannons',
        retainsMark = False,
        retainsColor = False,
        minSkill = { 'tinkering': 85.0 },
        resourcesNeeded = { 'ingots': 1000 },
        gumpPath = ( GumpSelection( 949095101, 64 ), GumpSelection( 949095101, 9 ) )
    ),


    ### Slayer Deeds: Gump Button 71 ###
    'Arachnid Doom': TinkeringCraftable(
        name = 'Arachnid Doom',
        retainsMark = False,
        retainsColor = False,
        minSkill = { 'tinkering': 105.0 },
        resourcesNeeded = { 'ingots': 100, 'dull copper ingot': 50, 'copper ingot': 50, 'valorite ingot': 10 },
        gumpPath = ( GumpSelection( 949095101, 71 ), GumpSelection( 949095101, 2 ) )
    ),
    'Elemental Ban': TinkeringCraftable(
        name = 'Elemental Ban',
        retainsMark = False,
        retainsColor = False,
        minSkill = { 'tinkering': 105.0 },
        resourcesNeeded = { 'ingots': 100, 'dull copper ingot': 50, 'bronze ingot': 25, 'agapite ingot': 25 },
        gumpPath = ( GumpSelection( 949095101, 71 ), GumpSelection( 949095101, 9 ) )
    ),
    'Exorcism': TinkeringCraftable(
        name = 'Exorcism',
        retainsMark = False,
        retainsColor = False,
        minSkill = { 'tinkering': 105.0 },
        resourcesNeeded = { 'ingots': 100, 'copper ingot': 50, 'agapite ingot': 25, 'valorite ingot': 10 },
        gumpPath = ( GumpSelection( 949095101, 71 ), GumpSelection( 949095101, 16 ) )
    ),
    'Fey': TinkeringCraftable(
        name = 'Fey',
        retainsMark = False,
        retainsColor = False,
        minSkill = { 'tinkering': 105.0 },
        resourcesNeeded = { 'ingots': 150, 'shadow ingot': 25, 'copper ingot': 25, 'gold ingot': 10 },
        gumpPath = ( GumpSelection( 949095101, 71 ), GumpSelection( 949095101, 23 ) )
    ),
    'Repond': TinkeringCraftable(
        name = 'Repond',
        retainsMark = False,
        retainsColor = False,
        minSkill = { 'tinkering': 105.0 },
        resourcesNeeded = { 'ingots': 150, 'bronze ingot': 50, 'verite ingot': 25, 'valorite ingot': 10 },
        gumpPath = ( GumpSelection( 949095101, 71 ), GumpSelection( 949095101, 30 ) )
    ),
    'Reptilain Death': TinkeringCraftable(
        name = 'Reptilain Death',
        retainsMark = False,
        retainsColor = False,
        minSkill = { 'tinkering': 105.0 },
        resourcesNeeded = { 'ingots': 150, 'gold ingot': 25, 'agapite ingot': 25, 'valorite ingot': 10 },
        gumpPath = ( GumpSelection( 949095101, 71 ), GumpSelection( 949095101, 37 ) )
    ),
    'Silver': TinkeringCraftable(
        name = 'Silver',
        retainsMark = False,
        retainsColor = False,
        minSkill = { 'tinkering': 105.0 },
        resourcesNeeded = { 'ingots': 100, 'dull copper ingot': 75, 'bronze ingot': 25, 'verite ingot': 10 },
        gumpPath = ( GumpSelection( 949095101, 71 ), GumpSelection( 949095101, 44 ) )
    ),
}
