from Scripts.glossary.items.tools import tools
from Scripts.utilities.items import myItem

weapons = {
    # Bladed
    'broadsword': myItem(
        name = 'broadsword',
        itemID = 0x0F5E,
        color = 0x0000,
        category = 'weapon',
        weight = 6
    ),
    'cutlass': myItem(
        name = 'cutlass',
        itemID = 0x1441,
        color = 0x0000,
        category = 'weapon',
        weight = 8
    ),
    'katana': myItem(
        name = 'katana',
        itemID = 0x13FF,
        color = 0x0000,
        category = 'weapon',
        weight = 6
    ),
    'kryss': myItem(
        name = 'kryss',
        itemID = 0x1401,
        color = 0x0000,
        category = 'weapon',
        weight = 2
    ),
    'longsword': myItem(
        name = 'longsword',
        itemID = 0x0F61,
        color = 0x0000,
        category = 'weapon',
        weight = 7
    ),
    'scimitar': myItem(
        name = 'scimitar',
        itemID = 0x13B6,
        color = 0x0000,
        category = 'weapon',
        weight = 5
    ),
    'viking sword': myItem(
        name = 'viking sword',
        itemID = 0x13B9,
        color = 0x0000,
        category = 'weapon',
        weight = 6
    ),


    # Axes
    'axe': myItem(
        name = 'axe',
        itemID = 0x0F49,
        color = 0x0000,
        category = 'weapon',
        weight = 4
    ),
    'battle axe': myItem(
        name = 'battle axe',
        itemID = 0x0F47,
        color = 0x0000,
        category = 'weapon',
        weight = 4
    ),
    'double axe': myItem(
        name = 'double axe',
        itemID = 0x0F4B,
        color = 0x0000,
        category = 'weapon',
        weight = 8
    ),
    'executioner\'s axe': myItem(
        name = 'executioner\'s axe',
        itemID = 0x0F45,
        color = 0x0000,
        category = 'weapon',
        weight = 8
    ),
    'hatchet': myItem(
        name = 'hatchet',
        itemID = 0x0F43,
        color = 0x0000,
        category = 'weapon',
        weight = 4
    ),
    'large battle axe': myItem(
        name = 'large battle axe',
        itemID = 0x13FB,
        color = 0x0000,
        category = 'weapon',
        weight = 6
    ),
    'two handed axe': myItem(
        name = 'two handed axe',
        itemID = 0x1443,
        color = 0x0000,
        category = 'weapon',
        weight = 8
    ),
    'war axe': myItem(
        name = 'war axe',
        itemID = 0x13B0,
        color = 0x0000,
        category = 'weapon',
        weight = 8
    ),


    # Polearms
    'bardiche': myItem(
        name = 'bardiche',
        itemID = 0x0F4D,
        color = 0x0000,
        category = 'weapon',
        weight = 7
    ),
    'halberd': myItem(
        name = 'halberd',
        itemID = 0x143E,
        color = 0x0000,
        category = 'weapon',
        weight = 16
    ),
    'short spear': myItem(
        name = 'short spear',
        itemID = 0x1403,
        color = 0x0000,
        category = 'weapon',
        weight = 4
    ),
    'spear': myItem(
        name = 'spear',
        itemID = 0x0F62,
        color = 0x0000,
        category = 'weapon',
        weight = 7
    ),
    'war fork': myItem(
        name = 'war fork',
        itemID = 0x1405,
        color = 0x0000,
        category = 'weapon',
        weight = 9
    ),


    # Bashing
    'hammer pick': myItem(
        name = 'hammer pick',
        itemID = 0x143D,
        color = 0x0000,
        category = 'weapon',
        weight = 9
    ),
    'mace': myItem(
        name = 'mace',
        itemID = 0x0F5C,
        color = 0x0000,
        category = 'weapon',
        weight = 14
    ),
    'maul': myItem(
        name = 'maul',
        itemID = 0x143B,
        color = 0x0000,
        category = 'weapon',
        weight = 10
    ),
    'war mace': myItem(
        name = 'war mace',
        itemID = 0x1407,
        color = 0x0000,
        category = 'weapon',
        weight = 17
    ),
    'war hammer': myItem(
        name = 'war hammer',
        itemID = 0x1439,
        color = 0x0000,
        category = 'weapon',
        weight = 10
    ),


    # Ranged
    'bow': myItem(
        name = 'bow',
        itemID = 0x13B2,
        color = 0x0000,
        category = 'weapon',
        weight = 6
    ),
    'TODO: compound bow': myItem(
        name = 'broadsword',
        itemID = 0x0000,
        color = 0x0000,
        category = 'weapon',
        weight = 0
    ),
    'crossbow': myItem(
        name = 'crossbow',
        itemID = 0x0F50,
        color = 0x0000,
        category = 'weapon',
        weight = 7
    ),
    'heavy crossbow': myItem(
        name = 'heavy crossbow',
        itemID = 0x13FD,
        color = 0x0000,
        category = 'weapon',
        weight = 9
    ),

    # Wooden
    'black staff': myItem(
        name = 'black staff',
        itemID = 0x0DF0,
        color = 0x0000,
        category = 'weapon',
        weight = 6
    ),
    'sheperd\'s crook': myItem(
        name = 'sheperd\'s crook',
        itemID = 0x0E81,
        color = 0x0000,
        category = 'weapon',
        weight = 4
    ),
    'quarter staff': myItem(
        name = 'quarter staff',
        itemID = 0x0E89,
        color = 0x0000,
        category = 'weapon',
        weight = 4
    ),
    'gnarled staff': myItem(
        name = 'gnarled staff',
        itemID = 0x13F8,
        color = 0x0000,
        category = 'weapon',
        weight = 3
    ),
    'club': myItem(
        name = 'club',
        itemID = 0x13B4,
        color = 0x0000,
        category = 'weapon',
        weight = 9
    ),

    # Uncraftable
    'pitchfork': myItem(
        name = 'pitchfork',
        itemID = 0x0E87,
        color = 0x0000,
        category = 'weapon',
        weight = 11
    ),
    'butcher knife': myItem(
        name = 'butcher knife',
        itemID = 0x13F6,
        color = 0x0000,
        category = 'weapon',
        weight = 1
    ),
}

weapons[ 'cleaver' ] = tools[ 'cleaver' ]
weapons[ 'dagger' ] = tools[ 'dagger' ]
weapons[ 'pickaxe (left)' ] = tools[ 'pickaxe (left)' ]
weapons[ 'pickaxe (right)' ] = tools[ 'pickaxe (right)' ]
weapons[ 'skinning knife' ] = tools[ 'skinning knife' ]
