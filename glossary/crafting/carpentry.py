from Scripts.glossary.crafting.craftable import Craftable
from Scripts.glossary.items.tools import tools
from Scripts.utilities.gumps import GumpSelection
from Scripts.utilities.items import FindItem

carpentryTools = [
    tools[ 'dovetail saw' ],
    tools[ 'draw knife' ],
    tools[ 'froe' ],
    tools[ 'hammer' ],
    tools[ 'inshave' ],
    tools[ 'jointing plane' ],
    tools[ 'moulding planes' ],
    tools[ 'nails' ],
    tools[ 'saw' ],
    tools[ 'scorp' ],
    tools[ 'smoothing plane' ],
]

def FindCarpentryTool( container ):
    '''
    Searches for a carpentry tool in the specified container
    '''

    global carpentryTools

    # Find the tool to craft with
    for tool in carpentryTools:
        tool = FindItem( tool.itemID, container )
        if tool != None:
            return tool


class CarpentryCraftable ( Craftable ):
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


carpentryCraftables = {
    ### Other: Gump Button 1 ###
    'barrel staves': CarpentryCraftable(
        name = 'barrel staves',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 0.0 },
        resourcesNeeded = { 'boards': 5 },
        gumpPath = ( GumpSelection( 949095101, 1 ), GumpSelection( 949095101, 2 ) )
    ),
    'barrel lid': CarpentryCraftable(
        name = 'barrel lid',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 11.0 },
        resourcesNeeded = { 'boards': 4 },
        gumpPath = ( GumpSelection( 949095101, 1 ), GumpSelection( 949095101, 9 ) )
    ),
    'short music stand (left)': CarpentryCraftable(
        name = 'short music stand (left)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 78.9 },
        resourcesNeeded = { 'boards': 15 },
        gumpPath = ( GumpSelection( 949095101, 1 ), GumpSelection( 949095101, 16 ) )
    ),
    'tall music stand (left)': CarpentryCraftable(
        name = 'tall music stand (left)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 81.5 },
        resourcesNeeded = { 'boards': 20 },
        gumpPath = ( GumpSelection( 949095101, 1 ), GumpSelection( 949095101, 23 ) )
    ),
    'easel (south)': CarpentryCraftable(
        name = 'easel (south)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 86.8 },
        resourcesNeeded = { 'boards': 20 },
        gumpPath = ( GumpSelection( 949095101, 1 ), GumpSelection( 949095101, 30 ) )
    ),


    ### Furniture: Gump Button 8 ###
    'foot stool': CarpentryCraftable(
        name = 'foot stool',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 11.0 },
        resourcesNeeded = { 'boards': 9 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 2 ) )
    ),
    'stool': CarpentryCraftable(
        name = 'stool',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 11.0 },
        resourcesNeeded = { 'boards': 9 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 9 ) )
    ),
    'straw chair': CarpentryCraftable(
        name = 'straw chair',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 21.0 },
        resourcesNeeded = { 'boards': 13 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 16 ) )
    ),
    'wooden chair': CarpentryCraftable(
        name = 'wooden chair',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 21.0 },
        resourcesNeeded = { 'boards': 13 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 23 ) )
    ),
    'Vesper-style chair': CarpentryCraftable(
        name = 'Vesper-style chair',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 42.1 },
        resourcesNeeded = { 'boards': 15 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 30 ) )
    ),
    'Trinsic-style chair': CarpentryCraftable(
        name = 'Trinsic-style chair',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 42.1 },
        resourcesNeeded = { 'boards': 13 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 37 ) )
    ),
    'wooden bench': CarpentryCraftable(
        name = 'wooden bench',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 52.6 },
        resourcesNeeded = { 'boards': 17 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 44 ) )
    ),
    'wooden throne': CarpentryCraftable(
        name = 'wooden throne',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 52.6 },
        resourcesNeeded = { 'boards': 17 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 51 ) )
    ),
    'Magnicia-style throne': CarpentryCraftable(
        name = 'Magnicia-style throne',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 73.6 },
        resourcesNeeded = { 'boards': 19 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 58 ) )
    ),
    'small table': CarpentryCraftable(
        name = 'small table',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 42.1 },
        resourcesNeeded = { 'boards': 17 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 65 ) )
    ),
    'writing table': CarpentryCraftable(
        name = 'writing table',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 63.1 },
        resourcesNeeded = { 'boards': 17 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 72 ) )
    ),
    'large table': CarpentryCraftable(
        name = 'large table',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 63.1 },
        resourcesNeeded = { 'boards': 23 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 79 ) )
    ),
    'Yew wood table': CarpentryCraftable(
        name = 'Yew wood table',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 84.2 },
        resourcesNeeded = { 'boards': 27 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 86 ) )
    ),
    'elegant low table': CarpentryCraftable(
        name = 'elegant low table',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 80.0 },
        resourcesNeeded = { 'boards': 35 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 93 ) )
    ),
    'plain low table': CarpentryCraftable(
        name = 'plain low table',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 80.0 },
        resourcesNeeded = { 'boards': 35 },
        gumpPath = ( GumpSelection( 949095101, 8 ), GumpSelection( 949095101, 100 ) )
    ),


    ### Containers: Gump Button 15 ###
    'wooden box': CarpentryCraftable(
        name = 'wooden box',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 21.0 },
        resourcesNeeded = { 'boards': 10 },
        gumpPath = ( GumpSelection( 949095101, 15 ), GumpSelection( 949095101, 2 ) )
    ),
    'small crate': CarpentryCraftable(
        name = 'small crate',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 10.0 },
        resourcesNeeded = { 'boards': 8 },
        gumpPath = ( GumpSelection( 949095101, 15 ), GumpSelection( 949095101, 9 ) )
    ),
    'medium crate': CarpentryCraftable(
        name = 'medium crate',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 31.0 },
        resourcesNeeded = { 'boards': 15 },
        gumpPath = ( GumpSelection( 949095101, 15 ), GumpSelection( 949095101, 16 ) )
    ),
    'large crate': CarpentryCraftable(
        name = 'large crate',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 47.3 },
        resourcesNeeded = { 'boards': 18 },
        gumpPath = ( GumpSelection( 949095101, 15 ), GumpSelection( 949095101, 23 ) )
    ),
    'wooden chest': CarpentryCraftable(
        name = 'wooden chest',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 73.6 },
        resourcesNeeded = { 'boards': 20 },
        gumpPath = ( GumpSelection( 949095101, 15 ), GumpSelection( 949095101, 30 ) )
    ),
    'wooden shelf': CarpentryCraftable(
        name = 'wooden shelf',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 31.5 },
        resourcesNeeded = { 'boards': 25 },
        gumpPath = ( GumpSelection( 949095101, 15 ), GumpSelection( 949095101, 37 ) )
    ),
    'armoire (red)': CarpentryCraftable(
        name = 'armoire (red)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 84.2 },
        resourcesNeeded = { 'boards': 35 },
        gumpPath = ( GumpSelection( 949095101, 15 ), GumpSelection( 949095101, 44 ) )
    ),
    'armoire': CarpentryCraftable(
        name = 'armoire',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 84.2 },
        resourcesNeeded = { 'boards': 35 },
        gumpPath = ( GumpSelection( 949095101, 15 ), GumpSelection( 949095101, 51 ) )
    ),
    'treasure chest (silver)': CarpentryCraftable(
        name = 'treasure chest',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 110.0 },
        resourcesNeeded = { 'log': 200, 'diamond': 100, 'ruby': 100, 'emerald': 100, 'sapphire': 100, 'forged metal': 5 },
        gumpPath = ( GumpSelection( 949095101, 15 ), GumpSelection( 949095101, 58 ) )
    ),
    'treasure chest (silver and gold)': CarpentryCraftable(
        name = 'treasure chest',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 115.0 },
        resourcesNeeded = { 'log': 200, 'diamond': 200, 'ruby': 200, 'emerald': 200, 'sapphire': 200, 'forged metal': 10 },
        gumpPath = ( GumpSelection( 949095101, 15 ), GumpSelection( 949095101, 65 ) )
    ),
    'treasure chest (scrolls and potions)': CarpentryCraftable(
        name = 'treasure chest',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 115.0 },
        resourcesNeeded = { 'log': 200, 'diamond': 200, 'ruby': 200, 'emerald': 200, 'sapphire': 200, 'forged metal': 10 },
        gumpPath = ( GumpSelection( 949095101, 15 ), GumpSelection( 949095101, 72 ) )
    ),
    'gilded wooden chest': CarpentryCraftable(
        name = 'gilded wooden chest',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 120.0 },
        resourcesNeeded = { 'boards': 1000 },
        gumpPath = ( GumpSelection( 949095101, 15 ), GumpSelection( 949095101, 79 ) )
    ),
    'gothic chest': CarpentryCraftable(
        name = 'gothic chest',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 100.0 },
        resourcesNeeded = { 'boards': 1000 },
        gumpPath = ( GumpSelection( 949095101, 15 ), GumpSelection( 949095101, 86 ) )
    ),
    'ornate wooden chest': CarpentryCraftable(
        name = 'ornate wooden chest',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 120.0 },
        resourcesNeeded = { 'boards': 1000 },
        gumpPath = ( GumpSelection( 949095101, 15 ), GumpSelection( 949095101, 93 ) )
    ),
    'wooden footlocker': CarpentryCraftable(
        name = 'wooden footlocker',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 120.0 },
        resourcesNeeded = { 'boards': 1000 },
        gumpPath = ( GumpSelection( 949095101, 15 ), GumpSelection( 949095101, 100 ) )
    ),
    'finished wooden chest': CarpentryCraftable(
        name = 'finished wooden chest',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 120.0 },
        resourcesNeeded = { 'boards': 1000 },
        gumpPath = ( GumpSelection( 949095101, 15 ), GumpSelection( 949095101, 107 ) )
    ),
    'short cabinet': CarpentryCraftable(
        name = 'short cabinet',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 120.0 },
        resourcesNeeded = { 'boards': 1000 },
        gumpPath = ( GumpSelection( 949095101, 15 ), GumpSelection( 949095101, 114 ) )
    ),
    'tall cabinet': CarpentryCraftable(
        name = 'tall cabinet',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 120.0 },
        resourcesNeeded = { 'boards': 1000 },
        gumpPath = ( GumpSelection( 949095101, 15 ), GumpSelection( 949095101, 121 ) )
    ),
    'plain wooden chest': CarpentryCraftable(
        name = 'plain wooden chest',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 90.0 },
        resourcesNeeded = { 'boards': 30 },
        gumpPath = ( GumpSelection( 949095101, 15 ), GumpSelection( 949095101, 128 ) )
    ),
    'red armoire': CarpentryCraftable(
        name = 'red armoire',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 90.0 },
        resourcesNeeded = { 'boards': 40 },
        gumpPath = ( GumpSelection( 949095101, 15 ), GumpSelection( 949095101, 135 ) )
    ),
    'elegant armoire': CarpentryCraftable(
        name = 'elegant armoire',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 90.0 },
        resourcesNeeded = { 'boards': 40 },
        gumpPath = ( GumpSelection( 949095101, 15 ), GumpSelection( 949095101, 142 ) )
    ),
    'maple armoire': CarpentryCraftable(
        name = 'maple armoire',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 90.0 },
        resourcesNeeded = { 'boards': 40 },
        gumpPath = ( GumpSelection( 949095101, 15 ), GumpSelection( 949095101, 149 ) )
    ),
    'cherry armoire': CarpentryCraftable(
        name = 'cherry armoire',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 90.0 },
        resourcesNeeded = { 'boards': 40 },
        gumpPath = ( GumpSelection( 949095101, 15 ), GumpSelection( 949095101, 156 ) )
    ),
    'keg': CarpentryCraftable(
        name = 'keg',
        retainsMark = False,
        retainsColor = False,
        minSkill = { 'Carpentry': 57.8 },
        resourcesNeeded = { 'barrel staves': 3, 'barrel hoops': 1, 'barrel lid': 1 },
        gumpPath = ( GumpSelection( 949095101, 15 ), GumpSelection( 949095101, 163 ) )
    ),

    ### Weapons and Armor: Gump Button 22 ###
    'shepherd\'s crook': CarpentryCraftable(
        name = 'shepherd\'s crook',
        retainsMark = True,
        retainsColor = True,
        minSkill = { 'Carpentry': 78.9 },
        resourcesNeeded = { 'boards': 7 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 2 ) )
    ),
    'quarter staff': CarpentryCraftable(
        name = 'quarter staff',
        retainsMark = True,
        retainsColor = True,
        minSkill = { 'Carpentry': 73.6 },
        resourcesNeeded = { 'boards': 6 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 9 ) )
    ),
    'gnarled staff': CarpentryCraftable(
        name = 'gnarled staff',
        retainsMark = True,
        retainsColor = True,
        minSkill = { 'Carpentry': 78.9 },
        resourcesNeeded = { 'boards': 7 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 16 ) )
    ),
    'wooden shield': CarpentryCraftable(
        name = 'wooden shield',
        retainsMark = True,
        retainsColor = True,
        minSkill = { 'Carpentry': 52.6 },
        resourcesNeeded = { 'boards': 9 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 23 ) )
    ),
    'club': CarpentryCraftable(
        name = 'club',
        retainsMark = True,
        retainsColor = True,
        minSkill = { 'Carpentry': 28.2 },
        resourcesNeeded = { 'boards': 6 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 30 ) )
    ),
    'fishing pole': CarpentryCraftable(
        name = 'fishing pole',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 68.4, 'Tailoring': 40.0 },
        resourcesNeeded = { 'boards': 5, 'cloth': 5 },
        gumpPath = ( GumpSelection( 949095101, 22 ), GumpSelection( 949095101, 37 ) )
    ),


    ### Instruments: Gump Button 29 ###
    'lap harp': CarpentryCraftable(
        name = 'lap harp',
        retainsMark = True,
        retainsColor = True,
        minSkill = { 'Carpentry': 63.1, 'Musicianship': 45.0 },
        resourcesNeeded = { 'boards': 20, 'cloth': 10 },
        gumpPath = ( GumpSelection( 949095101, 29 ), GumpSelection( 949095101, 2 ) )
    ),
    'standing harp': CarpentryCraftable(
        name = 'standing harp',
        retainsMark = True,
        retainsColor = True,
        minSkill = { 'Carpentry': 78.9, 'Musicianship': 45.0 },
        resourcesNeeded = { 'boards': 35, 'cloth': 15 },
        gumpPath = ( GumpSelection( 949095101, 29 ), GumpSelection( 949095101, 9 ) )
    ),
    'drum': CarpentryCraftable(
        name = 'drum',
        retainsMark = True,
        retainsColor = True,
        minSkill = { 'Carpentry': 57.8, 'Musicianship': 45.0 },
        resourcesNeeded = { 'boards': 20, 'cloth': 10 },
        gumpPath = ( GumpSelection( 949095101, 29 ), GumpSelection( 949095101, 16 ) )
    ),
    'lute': CarpentryCraftable(
        name = 'lute',
        retainsMark = True,
        retainsColor = True,
        minSkill = { 'Carpentry': 68.4, 'Musicianship': 45.0 },
        resourcesNeeded = { 'boards': 25, 'cloth': 10 },
        gumpPath = ( GumpSelection( 949095101, 29 ), GumpSelection( 949095101, 23 ) )
    ),
    'tambourine': CarpentryCraftable(
        name = 'tambourine',
        retainsMark = True,
        retainsColor = True,
        minSkill = { 'Carpentry': 57.8, 'Musicianship': 45.0 },
        resourcesNeeded = { 'boards': 15, 'cloth': 10 },
        gumpPath = ( GumpSelection( 949095101, 29 ), GumpSelection( 949095101, 30 ) )
    ),
    'tambourine (tassle)': CarpentryCraftable(
        name = 'tambourine (tassle)',
        retainsMark = True,
        retainsColor = True,
        minSkill = { 'Carpentry': 57.8, 'Musicianship': 45.0 },
        resourcesNeeded = { 'boards': 15, 'cloth': 15 },
        gumpPath = ( GumpSelection( 949095101, 29 ), GumpSelection( 949095101, 37 ) )
    ),
    'bamboo flute': CarpentryCraftable(
        name = 'bamboo flute',
        retainsMark = True,
        retainsColor = True,
        minSkill = { 'Carpentry': 80.0, 'Musicianship': 45.0 },
        resourcesNeeded = { 'boards': 15 },
        gumpPath = ( GumpSelection( 949095101, 29 ), GumpSelection( 949095101, 44 ) )
    ),


    ### Misc. Add-Ons: Gump Button 36 ###
    'small bed (south)': CarpentryCraftable(
        name = 'small bed (south)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 94.7, 'Tailoring': 75.0 },
        resourcesNeeded = { 'boards': 100, 'cloth': 100 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 2 ) )
    ),
    'small bed (east)': CarpentryCraftable(
        name = 'small bed (east)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 94.7, 'Tailoring': 75.0 },
        resourcesNeeded = { 'boards': 100, 'cloth': 100 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 9 ) )
    ),
    'large bed (south)': CarpentryCraftable(
        name = 'large bed (south)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 94.7, 'Tailoring': 75.0 },
        resourcesNeeded = { 'boards': 150, 'cloth': 150 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 16 ) )
    ),
    'large bed (east)': CarpentryCraftable(
        name = 'large bed (east)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 94.7, 'Tailoring': 75.0 },
        resourcesNeeded = { 'boards': 150, 'cloth': 150 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 23 ) )
    ),
    'dartboard (south)': CarpentryCraftable(
        name = 'dartboard (south)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 15.7 },
        resourcesNeeded = { 'boards': 5 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 30 ) )
    ),
    'dartboard (east)': CarpentryCraftable(
        name = 'dartboard (east)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 15.7 },
        resourcesNeeded = { 'boards': 5 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 37 ) )
    ),
    'bulletin board (east)': CarpentryCraftable(
        name = 'bulletin board (east)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 85.0 },
        resourcesNeeded = { 'boards': 200 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 44 ) )
    ),
    'bulletin board (south)': CarpentryCraftable(
        name = 'bulletin board (south)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 85.0 },
        resourcesNeeded = { 'boards': 200 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 51 ) )
    ),
    'ballot box': CarpentryCraftable(
        name = 'ballot box',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 47.3 },
        resourcesNeeded = { 'boards': 5 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 58 ) )
    ),
    'pentagram': CarpentryCraftable(
        name = 'pentagram',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 100.0, 'Magery': 75.0 },
        resourcesNeeded = { 'boards': 100, 'ingots': 40 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 65 ) )
    ),
    'abbatoir': CarpentryCraftable(
        name = 'abbatoir',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 100.0, 'Magery': 50.0 },
        resourcesNeeded = { 'boards': 100, 'ingots': 40 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 72 ) )
    ),
    'stone abbatoir': CarpentryCraftable(
        name = 'stone abbatoir',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 115.0, 'Magery': 100.0 },
        resourcesNeeded = { 'boards': 500, 'ingots': 500 },
        gumpPath = ( GumpSelection( 949095101, 36 ), GumpSelection( 949095101, 79 ) )
    ),


    ### Blacksmithing: Gump Button 43 ###
    'small forge': CarpentryCraftable(
        name = 'small forge',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 73.6, 'Blacksmithing': 75.0 },
        resourcesNeeded = { 'boards': 5, 'ingots': 75 },
        gumpPath = ( GumpSelection( 949095101, 43 ), GumpSelection( 949095101, 2 ) )
    ),
    'large forge (east)': CarpentryCraftable(
        name = 'large forge (east)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 78.9, 'Blacksmithing': 80.0 },
        resourcesNeeded = { 'boards': 5, 'ingots': 100 },
        gumpPath = ( GumpSelection( 949095101, 43 ), GumpSelection( 949095101, 9 ) )
    ),
    'large forge (south)': CarpentryCraftable(
        name = 'large forge (south)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 78.9, 'Blacksmithing': 80.0 },
        resourcesNeeded = { 'boards': 5, 'ingots': 100 },
        gumpPath = ( GumpSelection( 949095101, 43 ), GumpSelection( 949095101, 16 ) )
    ),
    'anvil (east)': CarpentryCraftable(
        name = 'anvil (east)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 73.6, 'Blacksmithing': 75.0 },
        resourcesNeeded = { 'boards': 5, 'ingots': 150 },
        gumpPath = ( GumpSelection( 949095101, 43 ), GumpSelection( 949095101, 23 ) )
    ),
    'anvil (south)': CarpentryCraftable(
        name = 'anvil (south)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 73.6, 'Blacksmithing': 75.0 },
        resourcesNeeded = { 'boards': 5, 'ingots': 150 },
        gumpPath = ( GumpSelection( 949095101, 43 ), GumpSelection( 949095101, 30 ) )
    ),


    ### Training: Gump Button 50 ###
    'training dummy (east)': CarpentryCraftable(
        name = 'training dummy (east)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 68.4, 'Tailoring': 50.0 },
        resourcesNeeded = { 'boards': 55, 'cloth': 60 },
        gumpPath = ( GumpSelection( 949095101, 50 ), GumpSelection( 949095101, 2 ) )
    ),
    'training dummy (south)': CarpentryCraftable(
        name = 'training dummy (south)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 68.4, 'Tailoring': 50.0 },
        resourcesNeeded = { 'boards': 55, 'cloth': 60 },
        gumpPath = ( GumpSelection( 949095101, 50 ), GumpSelection( 949095101, 9 ) )
    ),
    'pickpocket dip (east)': CarpentryCraftable(
        name = 'pickpocket dip (east)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 73.6, 'Tailoring': 50.0 },
        resourcesNeeded = { 'boards': 65, 'cloth': 60 },
        gumpPath = ( GumpSelection( 949095101, 50 ), GumpSelection( 949095101, 16 ) )
    ),
    'pickpocket dip (south)': CarpentryCraftable(
        name = 'pickpocket dip (south)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 73.6, 'Tailoring': 50.0 },
        resourcesNeeded = { 'boards': 65, 'cloth': 60 },
        gumpPath = ( GumpSelection( 949095101, 50 ), GumpSelection( 949095101, 23 ) )
    ),


    ### Tailoring and Cooking: Gump Button 57 ###
    'spinning wheel (east)': CarpentryCraftable(
        name = 'spinning wheel (east)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 73.6, 'Tailoring': 65.0 },
        resourcesNeeded = { 'boards': 75, 'cloth': 25 },
        gumpPath = ( GumpSelection( 949095101, 57 ), GumpSelection( 949095101, 2 ) )
    ),
    'spinning wheel (south)': CarpentryCraftable(
        name = 'spinning wheel (south)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 73.6, 'Tailoring': 65.0 },
        resourcesNeeded = { 'boards': 75, 'cloth': 25 },
        gumpPath = ( GumpSelection( 949095101, 57 ), GumpSelection( 949095101, 9 ) )
    ),
    'loom (east)': CarpentryCraftable(
        name = 'loom (east)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 84.2, 'Tailoring': 65.0 },
        resourcesNeeded = { 'boards': 85, 'cloth': 25 },
        gumpPath = ( GumpSelection( 949095101, 57 ), GumpSelection( 949095101, 16 ) )
    ),
    'loom (south)': CarpentryCraftable(
        name = 'loom (south)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 84.2, 'Tailoring': 65.0 },
        resourcesNeeded = { 'boards': 85, 'cloth': 25 },
        gumpPath = ( GumpSelection( 949095101, 57 ), GumpSelection( 949095101, 23 ) )
    ),


    ### Cooking: Gump Button 64 ###
    'stone oven (east)': CarpentryCraftable(
        name = 'stone oven (east)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 68.4, 'Tinkering': 50.0 },
        resourcesNeeded = { 'boards': 85, 'ingots': 125 },
        gumpPath = ( GumpSelection( 949095101, 64 ), GumpSelection( 949095101, 2 ) )
    ),
    'stone oven (south)': CarpentryCraftable(
        name = 'stone oven (south)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 68.4, 'Tinkering': 50.0 },
        resourcesNeeded = { 'boards': 85, 'ingots': 125 },
        gumpPath = ( GumpSelection( 949095101, 64 ), GumpSelection( 949095101, 9 ) )
    ),
    'flour mill (east)': CarpentryCraftable(
        name = 'flour mill (east)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 94.7, 'Tinkering': 50.0 },
        resourcesNeeded = { 'boards': 100, 'ingots': 50 },
        gumpPath = ( GumpSelection( 949095101, 64 ), GumpSelection( 949095101, 16 ) )
    ),
    'flour mill (south)': CarpentryCraftable(
        name = 'flour mill (south)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 94.7, 'Tinkering': 50.0 },
        resourcesNeeded = { 'boards': 100, 'ingots': 50 },
        gumpPath = ( GumpSelection( 949095101, 64 ), GumpSelection( 949095101, 23 ) )
    ),
    'water trough (east)': CarpentryCraftable(
        name = 'water trough (east)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 94.7 },
        resourcesNeeded = { 'boards': 150 },
        gumpPath = ( GumpSelection( 949095101, 64 ), GumpSelection( 949095101, 30 ) )
    ),
    'water trough (south)': CarpentryCraftable(
        name = 'water trough (south)',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 94.7 },
        resourcesNeeded = { 'boards': 150 },
        gumpPath = ( GumpSelection( 949095101, 64 ), GumpSelection( 949095101, 37 ) )
    ),


    ### Ship Parts: Gump Button 71 ###
    'ship ribs': CarpentryCraftable(
        name = 'ship ribs',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 85.0 },
        resourcesNeeded = { 'logs': 1000 },
        gumpPath = ( GumpSelection( 949095101, 71 ), GumpSelection( 949095101, 2 ) )
    ),


    ### Ship Upgrades: Gump Button 78 ###
    'Crow\'s Nest': CarpentryCraftable(
        name = 'Crow\'s Nest',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 85.0 },
        resourcesNeeded = { 'logs': 2000 },
        gumpPath = ( GumpSelection( 949095101, 78 ), GumpSelection( 949095101, 2 ) )
    ),
    'Experience Boost': CarpentryCraftable(
        name = 'Experience Boost',
        retainsMark = False,
        retainsColor = True,
        minSkill = { 'Carpentry': 85.0 },
        resourcesNeeded = { 'logs': 2000 },
        gumpPath = ( GumpSelection( 949095101, 78 ), GumpSelection( 949095101, 9 ) )
    ),


    ### Ships: Gump Button 85 ###
}
