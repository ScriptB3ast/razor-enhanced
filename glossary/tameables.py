from System.Collections.Generic import List

class Animal:
    name = ''
    mobileID = 0
    color = 0
    minTamingSkill = -1
    maxTamingSkill = -1
    packType = None

    def __init__ ( self, name, mobileID, color, minTamingSkill, maxTamingSkill, packType ):
        self.name = name
        self.mobileID = mobileID
        self.color = color
        self.minTamingSkill = minTamingSkill
        self.maxTamingSkill = maxTamingSkill

animals = {
    # Organized based on taming difficulty with no previous owners according to uo.com, then alphabetically by and within species
    # https://uo.com/wiki/ultima-online-wiki/skills/animal-taming/tameable-creatures/#mobs

    ### Min skill 0, Max skill 10 ###
    'dog': Animal( 'dog', 0x00D9, 0x0000, 0, 10, [ 'canine' ] ),
    'gorilla': Animal( 'gorilla', 0x001D, 0x0000, 0, 10, None ),
    'parrot': Animal( 'parrot', 0x033F, 0x0000, 0, 10, None ),

    # Rabbits
    'rabbit (brown)': Animal( 'rabbit', 0x00CD, 0x0000, 0, 10, None ),
    'rabbit (black)': Animal( 'rabbit', 0x00CD, 0x090E, 0, 10, None ),
    'jack rabbit': Animal( 'jack rabbit', 0x00CD, 0x01BB, 0, 10, None ),

    'skittering hopper': Animal( 'skittering hopper', 0x012E, 0x0000, 0, 10, None ),
    'squirrel': Animal( 'squirrel', 0x0116, 0x0000, 0, 10, None ),


    ### Min skill 0, Max skill 20 ###
    'mongbat': Animal( 'mongbat', 0x0027, 0x0000, 0, 20, None ),


    ### Min skill 10, Max skill 20 ###
    # Birds
    # Note: the following share a color code:
    # 0x0835: Finch, hawk
    # 0x0847: Tern, Towhee
    # 0x0851: Nuthatch, woodpecker
    # 0x0901: Crow, Magpie, raven
    'chickadee': Animal( 'chickadee', 0x0006, 0x0840, 10, 20, None ),
    'crossbill': Animal( 'crossbill', 0x0006, 0x083A, 10, 20, None ),
    'crow': Animal( 'crow', 0x0006, 0x0901, 10, 20, None ),
    'finch': Animal( 'finch', 0x0006, 0x0835, 10, 20, None ),
    'hawk': Animal( 'hawk', 0x0006, 0x0835, 10, 20, None ),
    'kingfisher': Animal( 'kingfisher', 0x0006, 0x083F, 10, 20, None ),
    'lapwing': Animal( 'lapwing', 0x0006, 0x0837, 10, 20, None ),
    'magpie': Animal( 'magpie', 0x0006, 0x0901, 10, 20, None ),
    'nuthatch': Animal( 'nuthatch', 0x0006, 0x0851, 10, 20, None ),
    'plover': Animal( 'plover', 0x0006, 0x0847, 10, 20, None ),
    'raven': Animal( 'raven', 0x0006, 0x0901, 10, 20, None ),
    'skylark': Animal( 'skylark', 0x0006, 0x083C, 10, 20, None ),
    'starling': Animal( 'starling', 0x083E, 0x0845, 10, 20, None ),
    'swift': Animal( 'swift', 0x0006, 0x0845, 10, 20, None ),
    'tern': Animal( 'tern', 0x0006, 0x0847, 10, 20, None ),
    'towhee': Animal( 'towhee', 0x0006, 0x0847, 10, 20, None ),
    'woodpecker': Animal( 'woodpecker', 0x0006, 0x0851, 10, 20, None ),
    'wren': Animal( 'wren', 0x0006, 0x0850, 10, 20, None ),

    'cat': Animal( 'cat', 0x00C9, 0x0000, 10, 20, [ 'feline' ] ),
    'chicken': Animal( 'chicken', 0x00D0, 0x0000, 10, 20, None ),
    'mountain goat': Animal( 'mountain goat', 0x0058, 0x0000, 10, 20, None ),
    'rat': Animal( 'rat', 0x00EE, 0x0000, 10, 20, None ),
    'sewer rat': Animal( 'sewer rat', 0x00EE, 0x0000, 10, 20, None ),


    ### Min skill 20, Max skill 30 ###
    'cow (brown)': Animal( 'cow', 0x00E7, 0x0000, 20, 30, None ),
    'cow (black)': Animal( 'cow', 0x00D8, 0x0000, 20, 30, None ),
    'goat': Animal( 'goat', 0x00D1, 0x0000, 20, 30, None ),
    'pig': Animal( 'pig', 0x00CB, 0x0000, 20, 30, None ),
    'sheep': Animal( 'sheep', 0x00CF, 0x0000, 20, 30, None ),


    ### Min skill 20, Max skill 50 ###
    'giant beetle': Animal( 'giant beetle', 0x0317, 0x0000, 20, 50, None ),
    'slime': Animal( 'slime', 0x0033, 0x0000, 20, 50, None ),


    ### Min skill 30, Max skill 40 ###
    'eagle': Animal( 'eagle', 0x0005, 0x0000, 30, 40, None ),
    'bouraRuddy': None, # Not on UO Forever


    ### Min skill 40, Max skill 50 ###
    'boar': Animal( 'boar', 0x0122, 0x0000, 40, 50, None ),
    'bullfrog': Animal( 'bullfrog', 0x0051, 0x0000, 40, 50, None ),
    'lowland boura': None, # Not on UO Forever
    'ferret': Animal( 'ferret', 0x0117, 0x0000, 40, 50, None ),
    'giant rat': Animal( 'giant rat', 0x00D7, 0x0000, 40, 50, None ),
    'hind': Animal( 'hind', 0x00ED, 0x0000, 40, 50, None ),

    # Horses
    'horse': Animal( 'horse', 0x00C8, 0x0000, 40, 50, None ),
    'horse2': Animal( 'horse', 0x00E2, 0x0000, 40, 50, None ),
    'horse3': Animal( 'horse', 0x00CC, 0x0000, 40, 50, None ),
    'horse4': Animal( 'horse', 0x00E4, 0x0000, 40, 50, None ),
    'horsePack': Animal( 'pack horse', 0x0123, 0x0000, 40, 50, None ),
    'horsePalomino': None,
    'horseWar': None,

    # Llamas
    'pack llama': Animal( 'pack llama', 0x0124, 0x0000, 40, 50, None ),
    'llamaRideable': None,

    # Ostards
    'ostard': Animal( 'desert ostard', 0x00D2, 0x0000, 40, 50, [ 'ostard' ] ),
    'forest ostard (green)': Animal( 'forest ostard', 0x00DB, 0x88A0, 40, 50, [ 'ostard' ] ),
    'forest ostard (red)': Animal( 'forest ostard', 0x00DB, 0x889D, 40, 50, [ 'ostard' ] ),

    'timber wolf': Animal( 'timber wolf', 0x00E1, 0x0000, 40, 50, [ 'canine' ] ),
    'rideable wolf': Animal( 'rideable wolf', 0x0115, 0x0000, 40, 50, [ 'canine' ] ),


    ### Min skill 50, Max skill 60 ###
    'black bear': Animal( 'black bear', 0x00D3, 0x0000, 50, 60, [ 'bear' ] ),
    'polar bear': Animal( 'polar bear', 0x00D5, 0x0000, 50, 60, [ 'bear' ] ),
    'deathwatch beetle': None,
    'llama': Animal( 'llama', 0x00DC, 0x0000, 50, 60, None ),
    'walrus': Animal( 'walrus', 0x00DD, 0x0000, 50, 60, None ),


    ### Min skill 60, Max skill 70 ###
    'alligator': Animal( 'alligator', 0x00CA, 0x0000, 60, 70, None ),
    'brown bear': Animal( 'brown bear', 0x00A7, 0x0000, 60, 70, [ 'bear' ] ),
    'high plains boura': None, # Not on UO Forever
    'cougar': Animal( 'cougar', 0x003F, 0x0000, 60, 70, [ 'feline' ] ),
    'paralithode': None, # Not on UO Forever
    'scorpion': Animal( 'scorpion', 0x0030, 0x0000, 60, 70, None ),


    ### Min skill 70, Max skill 80 ###
    'rideable polar bear': Animal( 'rideable polar bear', 0x00D5, 0x0000, 70, 80, [ 'bear' ] ),
    'grizzly bear': Animal( 'grizzly bear', 0x00D4, 0x0000, 70, 80, [ 'bear' ] ),
    'young dragon': Animal( 'young dragon', 0x003C, 0x0000, 70, 80, None ),
    'great hart': Animal( 'great hart', 0x00EA, 0x0000, 70, 80, None ),
    'snow leopard': Animal( 'snow leopard', 0x0040, 0x0000, 70, 80, [ 'feline' ] ),
    'snow leopard2': Animal( 'snow leopard', 0x0041, 0x0000, 70, 80, [ 'feline' ] ),
    'panther': Animal( 'panther', 0x00D6, 0x0000, 70, 80, [ 'feline' ] ),
    'snake': Animal( 'snake', 0x0034, 0x0000, 70, 80, None ),
    'giant spider': Animal( 'giant spider', 0x001C, 0x0000, 70, 80, None ),
    'grey wolf (light grey)': Animal( 'grey wolf', 0x0019, 0x0000, 70, 80, [ 'canine' ] ),
    'grey wolf (dark grey)': Animal( 'grey wolf', 0x001B, 0x0000, 70, 80, [ 'canine' ] ),


    ### Min skill 80, Max skill 90 ###
    'gaman': None,
    'slithStone': None,
    'white wolf (dark grey)': Animal( 'white wolf', 0x0022, 0x0000, 80, 90, [ 'canine' ] ),
    'white wolf (light grey)': Animal( 'white wolf', 0x0025, 0x0000, 80, 90, [ 'canine' ] ),


    ### Min skill 90, Max skill 100 ###
    'bull (solid, brown)': Animal( 'bull', 0x00E8, 0x0000, 90, 100, [ 'bull' ] ),
    'bull (solid, black)': Animal( 'bull', 0x00E8, 0x0901, 90, 100, [ 'bull' ] ),
    'bull (spotted, brown)': Animal( 'bull', 0x00E9, 0x0000, 90, 100, [ 'bull' ] ),
    'bull (spotted, black)': Animal( 'bull', 0x00E9, 0x0901, 90, 100, [ 'bull' ] ),
    'foxBlood': None,
    'hellcat (small)': Animal( 'hellcat', 0x00C9, 0x0647, 90, 100, [ 'feline' ] ),
    'mongbatGreater': None,
    'frenzied ostard': Animal( 'frenzied ostard', 0x00DA, 0x0000, 90, 100, [ 'ostard' ] ),
    'osseinRam': None,
    'frost spider': Animal( 'frost spider', 0x0014, 0x0000, 90, 100, None ),
    'giant toad': Animal( 'giant toad', 0x0050, 0x0000, 90, 100, None ),
    'unicorn': None,
    'giant ice worm': Animal( 'giant ice worm', 0x0050, 0x0000, 90, 100, None ),


    ### Min skill 100, Max skill 110 ###
    # Drakes
    # pathaleo drake: 0x003C
    'drake (brown)': Animal( 'drake', 0x003C, 0x0000, 100, 110, None ),
    'drake (red)': Animal( 'drake', 0x003D, 0x0000, 100, 110, None ),
    'drakeCrimson': None,
    'drakePlatinum': None,
    'drakeStygian': None,

    'hellcat (large)': Animal( 'hellcat', 0x007F, 0x0000, 100, 110, [ 'feline' ] ),
    'hellhound': Animal( 'hellhound', 0x0062, 0x0000, 100, 110, [ 'canine' ] ),
    'imp': Animal( 'imp', 0x004A, 0x0000, 100, 110, [ 'daemon' ] ),
    'kitsuneBake': None,
    'lava lizard': Animal( 'lava lizard', 0x00CE, 0x0000, 100, 110, None ),

    # ridgebacks
    'ridgeback': Animal( 'ridgeback', 0x00BB, 0x0000, 100, 110, None ),
    'savage ridgeback': Animal( 'savage ridgeback', 0x00BC, 0x0000, 100, 110, None ),

    'slith': None,
    'dire wolf': Animal( 'dire wolf', 0x0017, 0x0000, 100, 110, [ 'canine' ] ),


    ### Min skill 110, Max skill 120 ###
    'beetleDeath': None,
    'beetleFire': None,
    'rune beetle': Animal( 'rune beetle', 0x00F4, 0x0000, 110, 120, None ),

    'dragon': Animal( 'dragon', 0x003B, 0x0000, 110, 120, None ),
    'dragonSwamp': None,
    'dragonWater': None,
    'dragonDeepWater': None,

    'drakeCold': None,

    'hiryu': None,
    'hiryuLesser': None,

    'lion': None,
    'kiRin': None,
    'nightbear': None,
    'nightdragon': None,
    'nightfrenzy': None,
    'nightmare': None,
    'nightllama': None,
    'nightridge': None,
    'nightwolf': None,
    'skree': None,
    'dread spider': Animal( 'dread spider', 0x000B, 0x0000, 110, 120, None ),
    'unicorn': None,
    'wolfTsuki': None,
    'white wyrm': Animal( 'white wyrm', 0x00B4, 0x0000, 110, 120, None ),


    ### Challenging ###
    'cuSidhe': None,

    'dimetrosaur': None, # Not on UO Forever

    # Dragons
    'dragonBane': None,
    'dragonFrost': None,
    'a greater dragon': None, #0x000C
    'dragonSerpentine': None,

    'gallusaurus': None,

    # Horses
    'steedFire': None, # Pack type: Daemon, Equine
    'steedSkeletal': None, # Pack type: Daemon, Equine
    'horseDreadWar': None,

    'miteFrost': None,
    'najasaurus': None, # Not on UO Forever
    'phoenix': None,
    'raptor': None, # Pack type: Raptor
    'reptalon': None, # Not on UO Forever
    'saurosurus': None, # Not on UO Forever

    # Tigers
    'tigerWild': None,
    'tigerSabreToothed': None,

    'triceratops': None, # Not on UO Forever
    'turtleHatchlingDragon': None,
    'wolfDragon': None,
    'shadow wyrm': Animal( 'shadow wyrm', 0x006A, 0x0000, 120, 120, None )
}


def GetAnimalIDsAtOrOverTamingDifficulty( minimumTamingDifficulty ):
    '''
    Looks through the list of tameables for animals at or over the minimum taming level
    '''
    global animals

    animalList = List[int]()
    for animal in animals:
        if ( not animals[ animal ] == None and
                not animalList.Contains( animals[ animal ].mobileID ) and
                animals[ animal ].minTamingSkill >= minimumTamingDifficulty ):
            animalList.Add( animals[ animal ].mobileID )

    return animalList
