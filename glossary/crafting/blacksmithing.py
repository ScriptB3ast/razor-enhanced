from Scripts.utilities.gumps import GumpSelection
from Scripts.glossary.items.tools import tools
from Scripts.utilities.items import FindItem

blacksmithTools = [ tools[ 'sledge hammer' ], tools[ 'smith\'s hammer' ], tools[ 'tongs' ] ]

def FindBlacksmithTool( container ):
    '''
    Searches for a blacksmithing tool in the specified container
    '''

    # Find the tool to craft with
    for tool in blacksmithTools:
        tool = FindItem( tool.itemID, container )
        if tool != None:
            return tool


class BlacksmithCraftable:
    name = None
    itemID = None
    retainsMark = None
    retainsColor = None
    minSkill = None
    resourcesNeeded = None
    gumpPath = None

    def __init__ ( self, name, itemID, retainsMark, retainsColor, minSkill, resourcesNeeded, gumpPath ):
        self.name = name
        self.itemID = itemID
        self.retainsMark = retainsMark
        self.retainsColor = retainsColor
        self.minSkill = minSkill
        self.resourcesNeeded = resourcesNeeded
        self.gumpPath = gumpPath


blacksmithCraftables = {
    ### Deeds: Gump Button 1 ###
    'dragon barding deed': BlacksmithCraftable(
        name = 'dragon barding deed',
        itemID = None,
        retainsMark = True,
        retainsColor = True,
        minSkill = 110.0,
        resourcesNeeded = { 'ingots': 2000, 'rope': 10 },
        gumpPath = ( GumpSelection( 949095101, 1 ), GumpSelection( 949095101, 2 ) )
    ),


    ### Ringmail: Gump Button 8 ###
    'ringmail gloves': BlacksmithCraftable(
        name = 'ringmail gloves',
        itemID = 0x13EB,
        retainsMark = True,
        retainsColor = True,
        minSkill = 12.0,
        resourcesNeeded = { 'ingots': 10 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 2 ) )
    ),
    'ringmail leggings': BlacksmithCraftable(
        name = 'ringmail leggings',
        itemID = 0x13F0,
        retainsMark = True,
        retainsColor = True,
        minSkill = 19.4,
        resourcesNeeded = { 'ingots': 16 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 9 ) )
    ),
    'ringmail sleeves': BlacksmithCraftable(
        name = 'ringmail sleeves',
        itemID = 0x13EE,
        retainsMark = True,
        retainsColor = True,
        minSkill = 16.9,
        resourcesNeeded = { 'ingots': 14 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 16 ) )
    ),
    'ringmail tunic': BlacksmithCraftable(
        name = 'ringmail tunic',
        itemID = 0x13EC,
        retainsMark = True,
        retainsColor = True,
        minSkill = 21.9,
        resourcesNeeded = { 'ingots': 18 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 23 ) )
    ),


    ### Chainmail: Gump Button 15 ###
    'chainmail coif': BlacksmithCraftable(
        name = 'chainmail coif',
        itemID = 0x13BB,
        retainsMark = True,
        retainsColor = True,
        minSkill = 14.5,
        resourcesNeeded = { 'ingots': 10 },
        gumpPath = ( GumpSelection( 949095101, 15 ), GumpSelection( 949095101, 2 ) )
    ),
    'chainmail leggings': BlacksmithCraftable(
        name = 'chainmail leggings',
        itemID = 0x13BE,
        retainsMark = True,
        retainsColor = True,
        minSkill = 36.7,
        resourcesNeeded = { 'ingots': 18 },
        gumpPath = ( GumpSelection( 949095101, 15 ), GumpSelection( 949095101, 9 ) )
    ),
    'chainmail tunic': BlacksmithCraftable(
        name = 'chainmail tunic',
        itemID = 0x13BF,
        retainsMark = True,
        retainsColor = True,
        minSkill = 39.1,
        resourcesNeeded = { 'ingots': 20 },
        gumpPath = ( GumpSelection( 949095101, 15 ), GumpSelection( 949095101, 16 ) )
    ),

    ### Platemail: Gump Button 22 ###
    'platemail arms': BlacksmithCraftable(
        name = 'platemail arms',
        itemID = 0x1410,
        retainsMark = True,
        retainsColor = True,
        minSkill = 66.3,
        resourcesNeeded = { 'ingots': 18 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 2 ) )
    ),
    'platemail gloves': BlacksmithCraftable(
        name = 'platemail gloves',
        itemID = 0x1414,
        retainsMark = True,
        retainsColor = True,
        minSkill = 58.9,
        resourcesNeeded = { 'ingots': 12 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 9 ) )
    ),
    'platemail gorget': BlacksmithCraftable(
        name = 'platemail gorget',
        itemID = 0x1413,
        retainsMark = True,
        retainsColor = True,
        minSkill = 56.4,
        resourcesNeeded = { 'ingots': 10 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 16 ) )
    ),
    'platemail legs': BlacksmithCraftable(
        name = 'platemail legs',
        itemID = 0x1411,
        retainsMark = True,
        retainsColor = True,
        minSkill = 68.8,
        resourcesNeeded = { 'ingots': 20 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 23 ) )
    ),
    'platemail (tunic)': BlacksmithCraftable(
        name = 'platemail (tunic)',
        itemID = 0x1415,
        retainsMark = True,
        retainsColor = True,
        minSkill = 75.0,
        resourcesNeeded = { 'ingots': 25 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 30 ) )
    ),
    'platemail (female)': BlacksmithCraftable(
        name = 'platemail (female)',
        itemID = 0x1C04,
        retainsMark = True,
        retainsColor = True,
        minSkill = 44.1,
        resourcesNeeded = { 'ingots': 20 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 37 ) )
    ),
    'dragon gloves': BlacksmithCraftable(
        name = 'dragon gloves',
        itemID = 0x2643,
        retainsMark = True,
        retainsColor = True,
        minSkill = 68.9,
        resourcesNeeded = { 'Dragon Scales': 16 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 44 ) )
    ),
    'dragon gorget': BlacksmithCraftable(
        name = 'dragon gorget',
        itemID = 0x2B69,
        retainsMark = True,
        retainsColor = True,
        minSkill = 66.4,
        resourcesNeeded = { 'Dragon Scales': 14 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 51 ) )
    ),
    'dragon helm': BlacksmithCraftable(
        name = 'dragon helm',
        itemID = 0x2645,
        retainsMark = True,
        retainsColor = True,
        minSkill = 72.6,
        resourcesNeeded = { 'Dragon Scales': 20 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 58 ) )
    ),
    'dragon leggings': BlacksmithCraftable(
        name = 'dragon leggings',
        itemID = 0x2647,
        retainsMark = True,
        retainsColor = True,
        minSkill = 78.8,
        resourcesNeeded = { 'Dragon Scales': 28 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 65 ) )
    ),
    'dragon sleeves': BlacksmithCraftable(
        name = 'dragon sleeves',
        itemID = 0x2657,
        retainsMark = True,
        retainsColor = True,
        minSkill = 76.3,
        resourcesNeeded = { 'Dragon Scales': 24 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 72 ) )
    ),
    'dragon breastplate': BlacksmithCraftable(
        name = 'dragon breastplate',
        itemID = 0x2641,
        retainsMark = True,
        retainsColor = True,
        minSkill = 85.0,
        resourcesNeeded = { 'Dragon Scales': 36 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 79 ) )
    ),


    ### Helmets: Gump Button 29 ###
    'bascinet': BlacksmithCraftable(
        name = 'bascinet',
        itemID = 0x140C,
        retainsMark = True,
        retainsColor = True,
        minSkill = 8.3,
        resourcesNeeded = { 'ingots': 15 },
        gumpPath = ( GumpSelection( 949095101, 29 ), GumpSelection( 949095101, 2 ) )
    ),
    'close helmet': BlacksmithCraftable(
        name = 'close helmet',
        itemID = 0x1408,
        retainsMark = True,
        retainsColor = True,
        minSkill = 37.9,
        resourcesNeeded = { 'ingots': 15 },
        gumpPath = ( GumpSelection( 949095101, 29 ), GumpSelection( 949095101, 9 ) )
    ),
    'helmet': BlacksmithCraftable(
        name = 'helmet',
        itemID = 0x140A,
        retainsMark = True,
        retainsColor = True,
        minSkill = 37.9,
        resourcesNeeded = { 'ingots': 15 },
        gumpPath = ( GumpSelection( 949095101, 29 ), GumpSelection( 949095101, 16 ) )
    ),
    'norse helm': BlacksmithCraftable(
        name = 'norse helm',
        itemID = 0x140E,
        retainsMark = True,
        retainsColor = True,
        minSkill = 37.9,
        resourcesNeeded = { 'ingots': 15 },
        gumpPath = ( GumpSelection( 949095101, 29 ), GumpSelection( 949095101, 23 ) )
    ),
    'plate helm': BlacksmithCraftable(
        name = 'plate helm',
        itemID = 0x1412,
        retainsMark = True,
        retainsColor = True,
        minSkill = 62.6,
        resourcesNeeded = { 'ingots': 15 },
        gumpPath = ( GumpSelection( 949095101, 29 ), GumpSelection( 949095101, 30 ) )
    ),


    ### Shields: Gump Button 36 ###
    'buckler': BlacksmithCraftable(
        name = 'buckler',
        itemID = 0x1B73,
        retainsMark = True,
        retainsColor = True,
        minSkill = 0.0,
        resourcesNeeded = { 'ingots': 10 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 2 ) )
    ),
    'bronze shield': BlacksmithCraftable(
        name = 'bronze shield',
        itemID = 0x1B72,
        retainsMark = True,
        retainsColor = True,
        minSkill = 0.0,
        resourcesNeeded = { 'ingots': 12 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 9 ) )
    ),
    'heater shield': BlacksmithCraftable(
        name = 'heater shield',
        itemID = 0x1B76,
        retainsMark = True,
        retainsColor = True,
        minSkill = 24.3,
        resourcesNeeded = { 'ingots': 18 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 16 ) )
    ),
    'metal shield': BlacksmithCraftable(
        name = 'metal shield',
        itemID = 0x1B7B,
        retainsMark = True,
        retainsColor = True,
        minSkill = 0.0,
        resourcesNeeded = { 'ingots': 14 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 23 ) )
    ),
    'metal kite shield': BlacksmithCraftable(
        name = 'metal kite shield',
        itemID = 0x1B74,
        retainsMark = True,
        retainsColor = True,
        minSkill = 4.6,
        resourcesNeeded = { 'ingots': 16 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 30 ) )
    ),
    'tear kite shield': BlacksmithCraftable(
        name = 'tear kite shield',
        itemID = 0x1B79,
        retainsMark = True,
        retainsColor = True,
        minSkill = 0.0,
        resourcesNeeded = { 'ingots': 8 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 37 ) )
    ),


    ### Bladed: Gump Button 43 ###
    'broadsword': BlacksmithCraftable(
        name = 'broadsword',
        itemID = 0x0F5E,
        retainsMark = True,
        retainsColor = True,
        minSkill = 35.4,
        resourcesNeeded = { 'ingots': 10 },
        gumpPath = ( GumpSelection( 949095101, 43 ), GumpSelection( 949095101, 2 ) )
    ),
    'cutlass': BlacksmithCraftable(
        name = 'cutlass',
        itemID = 0x1441,
        retainsMark = True,
        retainsColor = True,
        minSkill = 24.3,
        resourcesNeeded = { 'ingots': 8 },
        gumpPath = ( GumpSelection( 949095101, 43 ), GumpSelection( 949095101, 9 ) )
    ),
    'dagger': BlacksmithCraftable(
        name = 'dagger',
        itemID = 0x0F52,
        retainsMark = True,
        retainsColor = True,
        minSkill = 0.0,
        resourcesNeeded = { 'ingots': 3 },
        gumpPath = ( GumpSelection( 949095101, 43 ), GumpSelection( 949095101, 16 ) )
    ),
    'katana': BlacksmithCraftable(
        name = 'katana',
        itemID = 0x13FF,
        retainsMark = True,
        retainsColor = True,
        minSkill = 44.1,
        resourcesNeeded = { 'ingots': 8 },
        gumpPath = ( GumpSelection( 949095101, 43 ), GumpSelection( 949095101, 23 ) )
    ),
    'kryss': BlacksmithCraftable(
        name = 'kryss',
        itemID = 0x1401,
        retainsMark = True,
        retainsColor = True,
        minSkill = 36.7,
        resourcesNeeded = { 'ingots': 8 },
        gumpPath = ( GumpSelection( 949095101, 43 ), GumpSelection( 949095101, 30 ) )
    ),
    'longsword': BlacksmithCraftable(
        name = 'longsword',
        itemID = 0x0F61,
        retainsMark = True,
        retainsColor = True,
        minSkill = 28.0,
        resourcesNeeded = { 'ingots': 12 },
        gumpPath = ( GumpSelection( 949095101, 43 ), GumpSelection( 949095101, 37 ) )
    ),
    'scimitar': BlacksmithCraftable(
        name = 'scimitar',
        itemID = 0x13B6,
        retainsMark = True,
        retainsColor = True,
        minSkill = 31.7,
        resourcesNeeded = { 'ingots': 10 },
        gumpPath = ( GumpSelection( 949095101, 43 ), GumpSelection( 949095101, 44 ) )
    ),
    'viking sword': BlacksmithCraftable(
        name = 'viking sword',
        itemID = 0x13B9,
        retainsMark = True,
        retainsColor = True,
        minSkill = 24.3,
        resourcesNeeded = { 'ingots': 14 },
        gumpPath = ( GumpSelection( 949095101, 43 ), GumpSelection( 949095101, 51 ) )
    ),


    ### Axes: Gump Button 50 ###
    'axe': BlacksmithCraftable(
        name = 'axe',
        itemID = 0x0F49,
        retainsMark = True,
        retainsColor = True,
        minSkill = 34.2,
        resourcesNeeded = { 'ingots': 14 },
        gumpPath = ( GumpSelection( 949095101, 50 ), GumpSelection( 949095101, 2 ) )
    ),
    'battle axe': BlacksmithCraftable(
        name = 'battle axe',
        itemID = 0x0F47,
        retainsMark = True,
        retainsColor = True,
        minSkill = 30.5,
        resourcesNeeded = { 'ingots': 14 },
        gumpPath = ( GumpSelection( 949095101, 50 ), GumpSelection( 949095101, 9 ) )
    ),
    'double axe': BlacksmithCraftable(
        name = 'double axe',
        itemID = 0x0F4B,
        retainsMark = True,
        retainsColor = True,
        minSkill = 29.3,
        resourcesNeeded = { 'ingots': 12 },
        gumpPath = ( GumpSelection( 949095101, 50 ), GumpSelection( 949095101, 16 ) )
    ),
    'executioner\'s axe': BlacksmithCraftable(
        name = 'executioner\'s axe',
        itemID = 0x0F45,
        retainsMark = True,
        retainsColor = True,
        minSkill = 34.2,
        resourcesNeeded = { 'ingots': 14 },
        gumpPath = ( GumpSelection( 949095101, 50 ), GumpSelection( 949095101, 23 ) )
    ),
    'large battle axe': BlacksmithCraftable(
        name = 'large battle axe',
        itemID = 0x13FB,
        retainsMark = True,
        retainsColor = True,
        minSkill = 28.0,
        resourcesNeeded = { 'ingots': 12 },
        gumpPath = ( GumpSelection( 949095101, 50 ), GumpSelection( 949095101, 30 ) )
    ),
    'two handed axe': BlacksmithCraftable(
        name = 'two handed axe',
        itemID = 0x1443,
        retainsMark = True,
        retainsColor = True,
        minSkill = 33.0,
        resourcesNeeded = { 'ingots': 16 },
        gumpPath = ( GumpSelection( 949095101, 50 ), GumpSelection( 949095101, 37 ) )
    ),
    'war axe': BlacksmithCraftable(
        name = 'war axe',
        itemID = 0x13B0,
        retainsMark = True,
        retainsColor = True,
        minSkill = 39.1,
        resourcesNeeded = { 'ingots': 16 },
        gumpPath = ( GumpSelection( 949095101, 50 ), GumpSelection( 949095101, 44 ) )
    ),


    ### Polearms: Gump Button 57 ###
    'bardiche': BlacksmithCraftable(
        name = 'bardiche',
        itemID = 0x0F4D,
        retainsMark = True,
        retainsColor = True,
        minSkill = 31.7,
        resourcesNeeded = { 'ingots': 18 },
        gumpPath = ( GumpSelection( 949095101, 57 ), GumpSelection( 949095101, 2 ) )
    ),
    'halberd': BlacksmithCraftable(
        name = 'halberd',
        itemID = 0x143E,
        retainsMark = True,
        retainsColor = True,
        minSkill = 39.1,
        resourcesNeeded = { 'ingots': 20 },
        gumpPath = ( GumpSelection( 949095101, 57 ), GumpSelection( 949095101, 9 ) )
    ),
    'short spear': BlacksmithCraftable(
        name = 'short spear',
        itemID = 0x1403,
        retainsMark = True,
        retainsColor = True,
        minSkill = 45.3,
        resourcesNeeded = { 'ingots': 6 },
        gumpPath = ( GumpSelection( 949095101, 57 ), GumpSelection( 949095101, 16 ) )
    ),
    'spear': BlacksmithCraftable(
        name = 'spear',
        itemID = 0x0F62,
        retainsMark = True,
        retainsColor = True,
        minSkill = 49.0,
        resourcesNeeded = { 'ingots': 12 },
        gumpPath = ( GumpSelection( 949095101, 57 ), GumpSelection( 949095101, 23 ) )
    ),
    'war fork': BlacksmithCraftable(
        name = 'war fork',
        itemID = 0x1405,
        retainsMark = True,
        retainsColor = True,
        minSkill = 42.9,
        resourcesNeeded = { 'ingots': 12 },
        gumpPath = ( GumpSelection( 949095101, 57 ), GumpSelection( 949095101, 30 ) )
    ),


    ### Bashing: Gump Button 64 ###
    'hammer pick': BlacksmithCraftable(
        name = 'hammer pick',
        itemID = 0x143D,
        retainsMark = True,
        retainsColor = True,
        minSkill = 34.2,
        resourcesNeeded = { 'ingots': 16 },
        gumpPath = ( GumpSelection( 949095101, 64 ), GumpSelection( 949095101, 2 ) )
    ),
    'mace': BlacksmithCraftable(
        name = 'mace',
        itemID = 0x0F5C,
        retainsMark = True,
        retainsColor = True,
        minSkill = 14.5,
        resourcesNeeded = { 'ingots': 6 },
        gumpPath = ( GumpSelection( 949095101, 64 ), GumpSelection( 949095101, 9 ) )
    ),
    'maul': BlacksmithCraftable(
        name = 'maul',
        itemID = 0x143B,
        retainsMark = True,
        retainsColor = True,
        minSkill = 19.4,
        resourcesNeeded = { 'ingots': 10 },
        gumpPath = ( GumpSelection( 949095101, 64 ), GumpSelection( 949095101, 16 ) )
    ),
    'war mace': BlacksmithCraftable(
        name = 'war mace',
        itemID = 0x1407,
        retainsMark = True,
        retainsColor = True,
        minSkill = 28.0,
        resourcesNeeded = { 'ingots': 14 },
        gumpPath = ( GumpSelection( 949095101, 64 ), GumpSelection( 949095101, 23 ) )
    ),
    'war hammer': BlacksmithCraftable(
        name = 'war hammer',
        itemID = 0x1439,
        retainsMark = True,
        retainsColor = True,
        minSkill = 34.2,
        resourcesNeeded = { 'ingots': 16 },
        gumpPath = ( GumpSelection( 949095101, 64 ), GumpSelection( 949095101, 30 ) )
    ),


    ### Ship Ammunition: Gump Button 71 ###
    'an iron cannonball': BlacksmithCraftable(
        name = 'an iron cannonball',
        itemID = None,
        retainsMark = False,
        retainsColor = False,
        minSkill = 65.0,
        resourcesNeeded = { 'ingots': 1 },
        gumpPath = ( GumpSelection( 949095101, 71 ), GumpSelection( 949095101, 2 ) )
    ),
    'a sack of 100 cannonballs': BlacksmithCraftable(
        name = 'a sack of 100 cannonballs',
        itemID = None,
        retainsMark = False,
        retainsColor = False,
        minSkill = 85.0,
        resourcesNeeded = { 'ingots': 100, 'cloth': 50 },
        gumpPath = ( GumpSelection( 949095101, 71 ), GumpSelection( 949095101, 9 ) )
    ),
    'a sack of 200 cannonballs': BlacksmithCraftable(
        name = 'a sack of 200 cannonballs',
        itemID = None,
        retainsMark = False,
        retainsColor = False,
        minSkill = 95.0,
        resourcesNeeded = { 'ingots': 175, 'cloth': 50 },
        gumpPath = ( GumpSelection( 949095101, 71 ), GumpSelection( 949095101, 16 ) )
    ),
    'a sack of 300 cannonballs': BlacksmithCraftable(
        name = 'a sack of 300 cannonballs',
        itemID = None,
        retainsMark = False,
        retainsColor = False,
        minSkill = 105.0,
        resourcesNeeded = { 'ingots': 250, 'cloth': 50 },
        gumpPath = ( GumpSelection( 949095101, 71 ), GumpSelection( 949095101, 23 ) )
    ),


    ### Ship Parts: Gump Button 78 ###
    'forged metal': BlacksmithCraftable(
        name = 'forged metal',
        itemID = None,
        retainsMark = False,
        retainsColor = False,
        minSkill = 85.0,
        resourcesNeeded = { 'ingots': 1000 },
        gumpPath = ( GumpSelection( 949095101, 78 ), GumpSelection( 949095101, 2 ) )
    ),


    ### Ship Upgrades: Gump Button 85 ###
    'Improved Munitions': BlacksmithCraftable(
        name = 'Improved Munitions',
        itemID = None,
        retainsMark = False,
        retainsColor = False,
        minSkill = 85.0,
        resourcesNeeded = { 'ingots': 1000 },
        gumpPath = ( GumpSelection( 949095101, 85 ), GumpSelection( 949095101, 2 ) )
    ),
    'Chain Shot': BlacksmithCraftable(
        name = 'Chain Shot',
        itemID = None,
        retainsMark = False,
        retainsColor = False,
        minSkill = 85.0,
        resourcesNeeded = { 'ingots': 1000 },
        gumpPath = ( GumpSelection( 949095101, 85 ), GumpSelection( 949095101, 9 ) )
    ),


    ### Forge Items: Gump Button 92 ###
    'Thorax Spikes': BlacksmithCraftable(
        name = 'Thorax Spikes',
        itemID = None,
        retainsMark = False,
        retainsColor = False,
        minSkill = 85.0,
        resourcesNeeded = { 'ingots': 1000, 'scales': 50 },
        gumpPath = ( GumpSelection( 949095101, 92 ), GumpSelection( 949095101, 2 ) )
    )
}
