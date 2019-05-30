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
    retainsMark = None
    retainsColor = None
    minSkill = None
    resourcesNeeded = None
    gumpPath = None

    def __init__ ( self, name, retainsMark, retainsColor, minSkill, resourcesNeeded, gumpPath ):
        self.name = name
        self.retainsMark = retainsMark
        self.retainsColor = retainsColor
        self.minSkill = minSkill
        self.resourcesNeeded = resourcesNeeded
        self.gumpPath = gumpPath


blacksmithCraftables = {
    ### Deeds: Gump Button 1 ###
    'dragon barding deed': BlacksmithCraftable(
        name = 'dragon barding deed',
        retainsMark = True,
        retainsColor = True,
        minSkill = 110.0,
        resourcesNeeded = { 'ingots': 2000, 'rope': 10 },
        gumpPath = ( GumpSelection( 949095101, 1 ), GumpSelection( 949095101, 2 ) )
    ),


    ### Ringmail: Gump Button 8 ###
    'ringmail gloves': BlacksmithCraftable(
        name = 'ringmail gloves',
        retainsMark = True,
        retainsColor = True,
        minSkill = 12.0,
        resourcesNeeded = { 'ingots': 10 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 2 ) )
    ),
    'ringmail leggings': BlacksmithCraftable(
        name = 'ringmail leggings',
        retainsMark = True,
        retainsColor = True,
        minSkill = 19.4,
        resourcesNeeded = { 'ingots': 16 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 9 ) )
    ),
    'ringmail sleeves': BlacksmithCraftable(
        name = 'ringmail sleeves',
        retainsMark = True,
        retainsColor = True,
        minSkill = 16.9,
        resourcesNeeded = { 'ingots': 14 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 16 ) )
    ),
    'ringmail tunic': BlacksmithCraftable(
        name = 'ringmail tunic',
        retainsMark = True,
        retainsColor = True,
        minSkill = 21.9,
        resourcesNeeded = { 'ingots': 18 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 23 ) )
    ),


    ### Chainmail: Gump Button 15 ###
    'chainmail coif': BlacksmithCraftable(
        name = 'chainmail coif',
        retainsMark = True,
        retainsColor = True,
        minSkill = 14.5,
        resourcesNeeded = { 'ingots': 10 },
        gumpPath = ( GumpSelection( 949095101, 15 ), GumpSelection( 949095101, 2 ) )
    ),
    'chainmail leggings': BlacksmithCraftable(
        name = 'chainmail leggings',
        retainsMark = True,
        retainsColor = True,
        minSkill = 36.7,
        resourcesNeeded = { 'ingots': 18 },
        gumpPath = ( GumpSelection( 949095101, 15 ), GumpSelection( 949095101, 9 ) )
    ),
    'chainmail tunic': BlacksmithCraftable(
        name = 'chainmail tunic',
        retainsMark = True,
        retainsColor = True,
        minSkill = 39.1,
        resourcesNeeded = { 'ingots': 20 },
        gumpPath = ( GumpSelection( 949095101, 15 ), GumpSelection( 949095101, 16 ) )
    ),

    ### Platemail: Gump Button 22 ###
    'platemail arms': BlacksmithCraftable(
        name = 'platemail arms',
        retainsMark = True,
        retainsColor = True,
        minSkill = 66.3,
        resourcesNeeded = { 'ingots': 18 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 2 ) )
    ),
    'platemail gloves': BlacksmithCraftable(
        name = 'platemail gloves',
        retainsMark = True,
        retainsColor = True,
        minSkill = 58.9,
        resourcesNeeded = { 'ingots': 12 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 9 ) )
    ),
    'platemail gorget': BlacksmithCraftable(
        name = 'platemail gorget',
        retainsMark = True,
        retainsColor = True,
        minSkill = 56.4,
        resourcesNeeded = { 'ingots': 10 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 16 ) )
    ),
    'platemail legs': BlacksmithCraftable(
        name = 'platemail legs',
        retainsMark = True,
        retainsColor = True,
        minSkill = 68.8,
        resourcesNeeded = { 'ingots': 20 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 23 ) )
    ),
    'platemail (tunic)': BlacksmithCraftable(
        name = 'platemail (tunic)',
        retainsMark = True,
        retainsColor = True,
        minSkill = 75.0,
        resourcesNeeded = { 'ingots': 25 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 30 ) )
    ),
    'platemail (female)': BlacksmithCraftable(
        name = 'platemail (female)',
        retainsMark = True,
        retainsColor = True,
        minSkill = 44.1,
        resourcesNeeded = { 'ingots': 20 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 37 ) )
    ),
    'dragon gloves': BlacksmithCraftable(
        name = 'dragon gloves',
        retainsMark = True,
        retainsColor = True,
        minSkill = 68.9,
        resourcesNeeded = { 'Dragon Scales': 16 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 44 ) )
    ),
    'dragon gorget': BlacksmithCraftable(
        name = 'dragon gorget',
        retainsMark = True,
        retainsColor = True,
        minSkill = 66.4,
        resourcesNeeded = { 'Dragon Scales': 14 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 51 ) )
    ),
    'dragon helm': BlacksmithCraftable(
        name = 'dragon helm',
        retainsMark = True,
        retainsColor = True,
        minSkill = 72.6,
        resourcesNeeded = { 'Dragon Scales': 20 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 58 ) )
    ),
    'dragon leggings': BlacksmithCraftable(
        name = 'dragon leggings',
        retainsMark = True,
        retainsColor = True,
        minSkill = 78.8,
        resourcesNeeded = { 'Dragon Scales': 28 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 65 ) )
    ),
    'dragon sleeves': BlacksmithCraftable(
        name = 'dragon sleeves',
        retainsMark = True,
        retainsColor = True,
        minSkill = 76.3,
        resourcesNeeded = { 'Dragon Scales': 24 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 72 ) )
    ),
    'dragon breastplate': BlacksmithCraftable(
        name = 'dragon breastplate',
        retainsMark = True,
        retainsColor = True,
        minSkill = 85.0,
        resourcesNeeded = { 'Dragon Scales': 36 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 79 ) )
    ),


    ### Helmets: Gump Button 29 ###
    'bascinet': BlacksmithCraftable(
        name = 'bascinet',
        retainsMark = True,
        retainsColor = True,
        minSkill = 8.3,
        resourcesNeeded = { 'ingots': 15 },
        gumpPath = ( GumpSelection( 949095101, 29 ), GumpSelection( 949095101, 2 ) )
    ),
    'close helmet': BlacksmithCraftable(
        name = 'close helmet',
        retainsMark = True,
        retainsColor = True,
        minSkill = 37.9,
        resourcesNeeded = { 'ingots': 15 },
        gumpPath = ( GumpSelection( 949095101, 29 ), GumpSelection( 949095101, 9 ) )
    ),
    'helmet': BlacksmithCraftable(
        name = 'helmet',
        retainsMark = True,
        retainsColor = True,
        minSkill = 37.9,
        resourcesNeeded = { 'ingots': 15 },
        gumpPath = ( GumpSelection( 949095101, 29 ), GumpSelection( 949095101, 16 ) )
    ),
    'norse helm': BlacksmithCraftable(
        name = 'norse helm',
        retainsMark = True,
        retainsColor = True,
        minSkill = 37.9,
        resourcesNeeded = { 'ingots': 15 },
        gumpPath = ( GumpSelection( 949095101, 29 ), GumpSelection( 949095101, 23 ) )
    ),
    'plate helm': BlacksmithCraftable(
        name = 'plate helm',
        retainsMark = True,
        retainsColor = True,
        minSkill = 62.6,
        resourcesNeeded = { 'ingots': 15 },
        gumpPath = ( GumpSelection( 949095101, 29 ), GumpSelection( 949095101, 30 ) )
    ),


    ### Shields: Gump Button 36 ###
    'buckler': BlacksmithCraftable(
        name = 'buckler',
        retainsMark = True,
        retainsColor = True,
        minSkill = 0.0,
        resourcesNeeded = { 'ingots': 10 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 2 ) )
    ),
    'bronze shield': BlacksmithCraftable(
        name = 'bronze shield',
        retainsMark = True,
        retainsColor = True,
        minSkill = 0.0,
        resourcesNeeded = { 'ingots': 12 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 9 ) )
    ),
    'heater shield': BlacksmithCraftable(
        name = 'heater shield',
        retainsMark = True,
        retainsColor = True,
        minSkill = 24.3,
        resourcesNeeded = { 'ingots': 18 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 16 ) )
    ),
    'metal shield': BlacksmithCraftable(
        name = 'metal shield',
        retainsMark = True,
        retainsColor = True,
        minSkill = 0.0,
        resourcesNeeded = { 'ingots': 14 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 23 ) )
    ),
    'metal kite shield': BlacksmithCraftable(
        name = 'metal kite shield',
        retainsMark = True,
        retainsColor = True,
        minSkill = 4.6,
        resourcesNeeded = { 'ingots': 16 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 30 ) )
    ),
    'tear kite shield': BlacksmithCraftable(
        name = 'tear kite shield',
        retainsMark = True,
        retainsColor = True,
        minSkill = 0.0,
        resourcesNeeded = { 'ingots': 8 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 37 ) )
    ),


    ### Bladed: Gump Button 43 ###
    'broadsword': BlacksmithCraftable(
        name = 'broadsword',
        retainsMark = True,
        retainsColor = True,
        minSkill = 35.4,
        resourcesNeeded = { 'ingots': 10 },
        gumpPath = ( GumpSelection( 949095101, 43 ), GumpSelection( 949095101, 2 ) )
    ),
    'cutlass': BlacksmithCraftable(
        name = 'cutlass',
        retainsMark = True,
        retainsColor = True,
        minSkill = 24.3,
        resourcesNeeded = { 'ingots': 8 },
        gumpPath = ( GumpSelection( 949095101, 43 ), GumpSelection( 949095101, 9 ) )
    ),
    'dagger': BlacksmithCraftable(
        name = 'dagger',
        retainsMark = True,
        retainsColor = True,
        minSkill = 0.0,
        resourcesNeeded = { 'ingots': 3 },
        gumpPath = ( GumpSelection( 949095101, 43 ), GumpSelection( 949095101, 16 ) )
    ),
    'katana': BlacksmithCraftable(
        name = 'katana',
        retainsMark = True,
        retainsColor = True,
        minSkill = 44.1,
        resourcesNeeded = { 'ingots': 8 },
        gumpPath = ( GumpSelection( 949095101, 43 ), GumpSelection( 949095101, 23 ) )
    ),
    'kryss': BlacksmithCraftable(
        name = 'kryss',
        retainsMark = True,
        retainsColor = True,
        minSkill = 36.7,
        resourcesNeeded = { 'ingots': 8 },
        gumpPath = ( GumpSelection( 949095101, 43 ), GumpSelection( 949095101, 30 ) )
    ),
    'longsword': BlacksmithCraftable(
        name = 'longsword',
        retainsMark = True,
        retainsColor = True,
        minSkill = 28.0,
        resourcesNeeded = { 'ingots': 12 },
        gumpPath = ( GumpSelection( 949095101, 43 ), GumpSelection( 949095101, 37 ) )
    ),
    'scimitar': BlacksmithCraftable(
        name = 'scimitar',
        retainsMark = True,
        retainsColor = True,
        minSkill = 31.7,
        resourcesNeeded = { 'ingots': 10 },
        gumpPath = ( GumpSelection( 949095101, 43 ), GumpSelection( 949095101, 44 ) )
    ),
    'viking sword': BlacksmithCraftable(
        name = 'viking sword',
        retainsMark = True,
        retainsColor = True,
        minSkill = 24.3,
        resourcesNeeded = { 'ingots': 14 },
        gumpPath = ( GumpSelection( 949095101, 43 ), GumpSelection( 949095101, 51 ) )
    ),


    ### Axes: Gump Button 50 ###
    'axe': BlacksmithCraftable(
        name = 'axe',
        retainsMark = True,
        retainsColor = True,
        minSkill = 34.2,
        resourcesNeeded = { 'ingots': 14 },
        gumpPath = ( GumpSelection( 949095101, 50 ), GumpSelection( 949095101, 2 ) )
    ),
    'battle axe': BlacksmithCraftable(
        name = 'battle axe',
        retainsMark = True,
        retainsColor = True,
        minSkill = 30.5,
        resourcesNeeded = { 'ingots': 14 },
        gumpPath = ( GumpSelection( 949095101, 50 ), GumpSelection( 949095101, 9 ) )
    ),
    'double axe': BlacksmithCraftable(
        name = 'double axe',
        retainsMark = True,
        retainsColor = True,
        minSkill = 29.3,
        resourcesNeeded = { 'ingots': 12 },
        gumpPath = ( GumpSelection( 949095101, 50 ), GumpSelection( 949095101, 16 ) )
    ),
    'executioner\'s axe': BlacksmithCraftable(
        name = 'executioner\'s axe',
        retainsMark = True,
        retainsColor = True,
        minSkill = 34.2,
        resourcesNeeded = { 'ingots': 14 },
        gumpPath = ( GumpSelection( 949095101, 50 ), GumpSelection( 949095101, 23 ) )
    ),
    'large battle axe': BlacksmithCraftable(
        name = 'large battle axe',
        retainsMark = True,
        retainsColor = True,
        minSkill = 28.0,
        resourcesNeeded = { 'ingots': 12 },
        gumpPath = ( GumpSelection( 949095101, 50 ), GumpSelection( 949095101, 30 ) )
    ),
    'two handed axe': BlacksmithCraftable(
        name = 'two handed axe',
        retainsMark = True,
        retainsColor = True,
        minSkill = 33.0,
        resourcesNeeded = { 'ingots': 16 },
        gumpPath = ( GumpSelection( 949095101, 50 ), GumpSelection( 949095101, 37 ) )
    ),
    'war axe': BlacksmithCraftable(
        name = 'war axe',
        retainsMark = True,
        retainsColor = True,
        minSkill = 39.1,
        resourcesNeeded = { 'ingots': 16 },
        gumpPath = ( GumpSelection( 949095101, 50 ), GumpSelection( 949095101, 44 ) )
    ),


    ### Polearms: Gump Button 57 ###
    'bardiche': BlacksmithCraftable(
        name = 'bardiche',
        retainsMark = True,
        retainsColor = True,
        minSkill = 31.7,
        resourcesNeeded = { 'ingots': 18 },
        gumpPath = ( GumpSelection( 949095101, 57 ), GumpSelection( 949095101, 2 ) )
    ),
    'halberd': BlacksmithCraftable(
        name = 'halberd',
        retainsMark = True,
        retainsColor = True,
        minSkill = 39.1,
        resourcesNeeded = { 'ingots': 20 },
        gumpPath = ( GumpSelection( 949095101, 57 ), GumpSelection( 949095101, 9 ) )
    ),
    'short spear': BlacksmithCraftable(
        name = 'short spear',
        retainsMark = True,
        retainsColor = True,
        minSkill = 45.3,
        resourcesNeeded = { 'ingots': 6 },
        gumpPath = ( GumpSelection( 949095101, 57 ), GumpSelection( 949095101, 16 ) )
    ),
    'spear': BlacksmithCraftable(
        name = 'spear',
        retainsMark = True,
        retainsColor = True,
        minSkill = 49.0,
        resourcesNeeded = { 'ingots': 12 },
        gumpPath = ( GumpSelection( 949095101, 57 ), GumpSelection( 949095101, 23 ) )
    ),
    'war fork': BlacksmithCraftable(
        name = 'war fork',
        retainsMark = True,
        retainsColor = True,
        minSkill = 42.9,
        resourcesNeeded = { 'ingots': 12 },
        gumpPath = ( GumpSelection( 949095101, 57 ), GumpSelection( 949095101, 30 ) )
    ),


    ### Bashing: Gump Button 64 ###
    'hammer pick': BlacksmithCraftable(
        name = 'hammer pick',
        retainsMark = True,
        retainsColor = True,
        minSkill = 34.2,
        resourcesNeeded = { 'ingots': 16 },
        gumpPath = ( GumpSelection( 949095101, 64 ), GumpSelection( 949095101, 2 ) )
    ),
    'mace': BlacksmithCraftable(
        name = 'mace',
        retainsMark = True,
        retainsColor = True,
        minSkill = 14.5,
        resourcesNeeded = { 'ingots': 6 },
        gumpPath = ( GumpSelection( 949095101, 64 ), GumpSelection( 949095101, 9 ) )
    ),
    'maul': BlacksmithCraftable(
        name = 'maul',
        retainsMark = True,
        retainsColor = True,
        minSkill = 19.4,
        resourcesNeeded = { 'ingots': 10 },
        gumpPath = ( GumpSelection( 949095101, 64 ), GumpSelection( 949095101, 16 ) )
    ),
    'war mace': BlacksmithCraftable(
        name = 'war mace',
        retainsMark = True,
        retainsColor = True,
        minSkill = 28.0,
        resourcesNeeded = { 'ingots': 14 },
        gumpPath = ( GumpSelection( 949095101, 64 ), GumpSelection( 949095101, 23 ) )
    ),
    'war hammer': BlacksmithCraftable(
        name = 'war hammer',
        retainsMark = True,
        retainsColor = True,
        minSkill = 34.2,
        resourcesNeeded = { 'ingots': 16 },
        gumpPath = ( GumpSelection( 949095101, 64 ), GumpSelection( 949095101, 30 ) )
    ),


    ### Ship Ammunition: Gump Button 71 ###
    'an iron cannonball': BlacksmithCraftable(
        name = 'an iron cannonball',
        retainsMark = False,
        retainsColor = False,
        minSkill = 65.0,
        resourcesNeeded = { 'ingots': 1 },
        gumpPath = ( GumpSelection( 949095101, 71 ), GumpSelection( 949095101, 2 ) )
    ),
    'a sack of 100 cannonballs': BlacksmithCraftable(
        name = 'a sack of 100 cannonballs',
        retainsMark = False,
        retainsColor = False,
        minSkill = 85.0,
        resourcesNeeded = { 'ingots': 100, 'cloth': 50 },
        gumpPath = ( GumpSelection( 949095101, 71 ), GumpSelection( 949095101, 9 ) )
    ),
    'a sack of 200 cannonballs': BlacksmithCraftable(
        name = 'a sack of 200 cannonballs',
        retainsMark = False,
        retainsColor = False,
        minSkill = 95.0,
        resourcesNeeded = { 'ingots': 175, 'cloth': 50 },
        gumpPath = ( GumpSelection( 949095101, 71 ), GumpSelection( 949095101, 16 ) )
    ),
    'a sack of 300 cannonballs': BlacksmithCraftable(
        name = 'a sack of 300 cannonballs',
        retainsMark = False,
        retainsColor = False,
        minSkill = 105.0,
        resourcesNeeded = { 'ingots': 250, 'cloth': 50 },
        gumpPath = ( GumpSelection( 949095101, 71 ), GumpSelection( 949095101, 23 ) )
    ),


    ### Ship Parts: Gump Button 78 ###
    'forged metal': BlacksmithCraftable(
        name = 'forged metal',
        retainsMark = False,
        retainsColor = False,
        minSkill = 85.0,
        resourcesNeeded = { 'ingots': 1000 },
        gumpPath = ( GumpSelection( 949095101, 78 ), GumpSelection( 949095101, 2 ) )
    ),


    ### Ship Upgrades: Gump Button 85 ###
    'Improved Munitions': BlacksmithCraftable(
        name = 'Improved Munitions',
        retainsMark = False,
        retainsColor = False,
        minSkill = 85.0,
        resourcesNeeded = { 'ingots': 1000 },
        gumpPath = ( GumpSelection( 949095101, 85 ), GumpSelection( 949095101, 2 ) )
    ),
    'Chain Shot': BlacksmithCraftable(
        name = 'Chain Shot',
        retainsMark = False,
        retainsColor = False,
        minSkill = 85.0,
        resourcesNeeded = { 'ingots': 1000 },
        gumpPath = ( GumpSelection( 949095101, 85 ), GumpSelection( 949095101, 9 ) )
    ),


    ### Forge Items: Gump Button 92 ###
    'Thorax Spikes': BlacksmithCraftable(
        name = 'Thorax Spikes',
        retainsMark = False,
        retainsColor = False,
        minSkill = 85.0,
        resourcesNeeded = { 'ingots': 1000, 'scales': 50 },
        gumpPath = ( GumpSelection( 949095101, 92 ), GumpSelection( 949095101, 2 ) )
    )
}
