from Scripts.utilities.gumps import GumpSelection
from Scripts.glossary.items.tools import tools

cartographyTools = [ tools[ 'mapmaker\'s pen' ] ]


class CartographyCraftable:
    name = None
    minSkill = None
    resourcesNeeded = None
    gumpPath = None

    def __init__ ( self, name, minSkill, resourcesNeeded, gumpPath ):
        self.name = name
        self.minSkill = minSkill
        self.resourcesNeeded = resourcesNeeded
        self.gumpPath = gumpPath


cartographyCraftables = {
    'local map': CartographyCraftable(
        name = 'local map',
        minSkill = 10.0,
        resourcesNeeded = { 'blank scroll': 1 },
        gumpPath = ( GumpSelection( 949095101, 1 ), GumpSelection( 949095101, 2 ) )
    ),
    'city map': CartographyCraftable(
        name = 'city map',
        minSkill = 25.0,
        resourcesNeeded = { 'blank scroll': 1 },
        gumpPath = ( GumpSelection( 949095101, 1 ), GumpSelection( 949095101, 9 ) )
    ),
    'sea map': CartographyCraftable(
        name = 'sea map',
        minSkill = 35.0,
        resourcesNeeded = { 'blank scroll': 1 },
        gumpPath = ( GumpSelection( 949095101, 1 ), GumpSelection( 949095101, 16 ) )
    ),
    'world map': CartographyCraftable(
        name = 'world map',
        minSkill = 39.5,
        resourcesNeeded = { 'blank scroll': 1 },
        gumpPath = ( GumpSelection( 949095101, 1 ), GumpSelection( 949095101, 23 ) )
    )
}
