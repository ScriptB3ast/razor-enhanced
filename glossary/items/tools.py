from Scripts.utilities.items import myItem, FindItem

tools = {
    # Blacksmithing
    'sledge hammer': myItem(
        name = 'sledge hammer',
        itemID = 0x0FB5,
        color = 0x0000,
        category = 'tool',
        weight = 10
    ),
    'smith\'s hammer': myItem(
        name = 'smith\'s hammer',
        itemID = 0x13E3,
        color = 0x0000,
        category = 'tool',
        weight = 8
    ),
    'tongs': myItem(
        name = 'tongs',
        itemID = 0x0FBB,
        color = 0x0000,
        category = 'tool',
        weight = 2
    ),

    # Runic Hammers
    'agapite runic hammer': myItem(
        name = 'agapite runic hammer',
        itemID = 0x13E3,
        color = 0x097E,
        category = 'tool',
        weight = 8
    ),
    'bronze runic hammer': myItem(
        name = 'bronze runic hammer',
        itemID = 0x13E3,
        color = 0x06D8,
        category = 'tool',
        weight = 8
    ),
    'copper runic hammer': myItem(
        name = 'copper runic hammer',
        itemID = 0x13E3,
        color = 0x045F,
        category = 'tool',
        weight = 8
    ),
    'dull copper runic hammer': myItem(
        name = 'dull copper runic hammer',
        itemID = 0x13E3,
        color = 0x0415,
        category = 'tool',
        weight = 8
    ),
    'golden runic hammer': myItem(
        name = 'golden runic hammer',
        itemID = 0x13E3,
        color = 0x06B7,
        category = 'tool',
        weight = 8
    ),
    'shadow iron runic hammer': myItem(
        name = 'shadow iron runic hammer',
        itemID = 0x13E3,
        color = 0x0455,
        category = 'tool',
        weight = 8
    ),
    'verite runic hammer': myItem(
        name = 'verite runic hammer',
        itemID = 0x13E3,
        color = 0x07D2,
        category = 'tool',
        weight = 8
    ),
    'valorite runic hammer': myItem(
        name = 'valorite runic hammer',
        itemID = 0x13E3,
        color = 0x0544,
        category = 'tool',
        weight = 8
    ),

    # Carpentry	Scorp	Smoothing Plane
    'dovetail saw': myItem(
        name = 'dovetail saw',
        itemID = 0x1028,
        color = 0x0000,
        category = 'tool',
        weight = 2
    ),
    'draw knife': myItem(
        name = 'draw knife',
        itemID = 0x10E4,
        color = 0x0000,
        category = 'tool',
        weight = 1
    ),
    'froe': myItem(
        name = 'froe',
        itemID = 0x10E5,
        color = 0x0000,
        category = 'tool',
        weight = 1
    ),
    'hammer': myItem(
        name = 'hammer',
        itemID = 0x102A,
        color = 0x0000,
        category = 'tool',
        weight = 2
    ),
    'inshave': myItem(
        name = 'inshave',
        itemID = 0x10E6,
        color = 0x0000,
        category = 'tool',
        weight = 1
    ),
    'jointing plane': myItem(
        name = 'jointing plane',
        itemID = 0x1030,
        color = 0x0000,
        category = 'tool',
        weight = 2
    ),
    'moulding planes': myItem(
        name = 'moulding planes',
        itemID = 0x102C,
        color = 0x0000,
        category = 'tool',
        weight = 2
    ),
    'nails': myItem(
        name = 'nails',
        itemID = 0x102E,
        color = 0x0000,
        category = 'tool',
        weight = 2
    ),
    'saw': myItem(
        name = 'saw',
        itemID = 0x1034,
        color = 0x0000,
        category = 'tool',
        weight = 2
    ),
    'scorp': myItem(
        name = 'scorp',
        itemID = 0x10E7,
        color = 0x0000,
        category = 'tool',
        weight = 1
    ),
    'smoothing plane': myItem(
        name = 'smoothing plane',
        itemID = 0x1032,
        color = 0x0000,
        category = 'tool',
        weight = 1
    ),

    # Mining
    'gargoyle\'s pickaxe': myItem(
        name = 'gargoyle\'s pickaxe',
        itemID = 0x0E86,
        color = 0x0430,
        category = 'tool',
        weight = 11
    ),
    'pickaxe (left)': myItem(
        name = 'pickaxe',
        itemID = 0x0E85,
        color = 0x0000,
        category = 'tool',
        weight = 11
    ),
    'pickaxe (right)': myItem(
        name = 'pickaxe',
        itemID = 0x0E86,
        color = 0x0000,
        category = 'tool',
        weight = 11
    ),
    'prospector\'s tool': myItem(
        name = 'prospector\'s tool',
        itemID = 0x0FB4,
        color = 0x0000,
        category = 'tool',
        weight = 11
    ),
    'sturdy pickaxe': myItem(
        name = 'pickaxe',
        itemID = 0x0E86,
        color = 0x0973,
        category = 'tool',
        weight = 11
    ),

    # Tinkering
    'tinker\'s tools': myItem(
        name = 'tinker\'s tools',
        itemID = 0x1EBC,
        color = 0x0000,
        category = 'tool',
        weight = 1
    ),
    'tool kit': myItem(
        name = 'tool kit',
        itemID = 0x1EB8,
        color = 0x0000,
        category = 'tool',
        weight = 1
    ),

    # Tailoring
    'sewing kit': myItem(
        name = 'sewing kit',
        itemID = 0x0F9D,
        color = 0x0000,
        category = 'tool',
        weight = 2
    ),

    'cleaver': myItem(
        name = 'cleaver',
        itemID = 0x0EC3,
        color = 0x0000,
        category = 'tool',
        weight = 2
    ),
    'dagger': myItem(
        name = 'dagger',
        itemID = 0x0F52,
        color = 0x0000,
        category = 'weapon',
        weight = 1
    ),
    'disguise kit': myItem(
        name = 'disguise kit',
        itemID = 0x0E05,
        color = 0x0000,
        category = 'tool',
        weight = None
    ),
    'dyes': myItem(
        name = 'dyes',
        itemID = 0x0FA9,
        color = 0x0000,
        category = 'tool',
        weight = 3
    ),
    'dyeing tub': myItem(
        name = 'dyeing tub',
        itemID = 0x0FAB,
        color = 0x0000,
        category = 'tool',
        weight = 10
    ),
    'fishing pole': myItem(
        name = 'fishing pole',
        itemID = 0x0DBF,
        color = 0x0000,
        category = 'tool',
        weight = 8
    ),
    'interior decorator': myItem(
        name = 'interior decorator',
        itemID = 0x0FC1,
        color = 0x0000,
        category = 'tool',
        weight = 11
    ),
    'lockpick': myItem(
        name = 'lockpick',
        itemID = 0x14FC,
        color = 0x0000,
        category = 'tool',
        weight = 1
    ),
    'mapmaker\'s pen': myItem(
        name = 'mapmaker\'s pen',
        itemID = 0x0FBF,
        color = 0x0000,
        category = 'tool',
        weight = 1
    ),
    'scissors': myItem(
        name = 'scissors',
        itemID = 0x0F9F,
        color = 0x0000,
        category = 'tool',
        weight = 1
    ),
    'skinning knife': myItem(
        name = 'skinning knife',
        itemID = 0x0EC4,
        color = 0x0000,
        category = 'tool',
        weight = 1
    ),
}
