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
    'dog': Animal( 'Dog', 0x00D9, 0x0000, 0, 10, [ 'Canine' ] ),
    'gorilla': Animal( 'Gorilla', 0x001D, 0x0000, 0, 10, None ),
    'parrot': Animal( 'Parrot', 0x033F, 0x0000, 0, 10, None ),
    'rabbitBrown': Animal( 'Rabbit', 0x00CD, 0x0000, 0, 10, None ),
    'rabbitBlack': Animal( 'Rabbit', 0x00CD, 0x090E, 0, 10, None ),
    'rabbitJack': Animal( 'Jack Rabbit', 0x00CD, 0x01BB, 0, 10, None ),
    'hopperSkittering': None,
    'squirrel': Animal( 'Squirrel', 0x0116, 0x01BB, 0, 10, None ),


    ### Min skill 0, Max skill 20 ###
    'mongbat': Animal( 'Mongbat', 0x0027, 0x0000, 0, 20, None ),


    ### Min skill 10, Max skill 20 ###
    # Birds
    # Note: the following share a color code:
    # 0x0835: Finch, Hawk
    # 0x0847: Tern, Towhee
    # 0x0851: Nuthatch, Woodpecker
    # 0x0901: Crow, Magpie, Raven
    'birdChickadee': Animal( 'Chickadee', 0x0006, 0x0840, 10, 20, None ),
    'birdCrossbill': Animal( 'Crossbill', 0x0006, 0x083A, 10, 20, None ),
    'birdCrow': Animal( 'Crow', 0x0006, 0x0901, 10, 20, None ),
    'birdFinch': Animal( 'Finch', 0x0006, 0x0835, 10, 20, None ),
    'birdHawk': Animal( 'Hawk', 0x0006, 0x0835, 10, 20, None ),
    'birdLapwing': Animal( 'Lapwing', 0x0006, 0x0837, 10, 20, None ),
    'birdMagpie': Animal( 'Magpie', 0x0006, 0x0901, 10, 20, None ),
    'birdNuthatch': Animal( 'Nuthatch', 0x0006, 0x0851, 10, 20, None ),
    'birdPlover': Animal( 'Plover', 0x0006, 0x0847, 10, 20, None ),
    'birdRaven': Animal( 'Raven', 0x0006, 0x0901, 10, 20, None ),
    'birdSkylark': Animal( 'Skylark', 0x0006, 0x083C, 10, 20, None ),
    'birdStarling': Animal( 'Starling', 0x083E, 0x0845, 10, 20, None ),
    'birdSwift': Animal( 'Swift', 0x0006, 0x0845, 10, 20, None ),
    'birdTern': Animal( 'Tern', 0x0006, 0x0847, 10, 20, None ),
    'birdTowhee': Animal( 'Towhee', 0x0006, 0x0847, 10, 20, None ),
    'birdWoodpecker': Animal( 'Woodpecker', 0x0006, 0x0851, 10, 20, None ),
    'birdWren': Animal( 'Wren', 0x0006, 0x0850, 10, 20, None ),

    'cat': Animal( 'Cat', 0x00C9, 0x0000, 10, 20, [ 'Feline' ] ),
    'chicken': Animal( 'Chicken', 0x00D0, 0x0000, 10, 20, None ),
    'goatMountain': Animal( 'Mountain Goat', 0x0058, 0x0000, 10, 20, None ),
    'rat': Animal( 'Rat', 0x00EE, 0x0000, 10, 20, None ),
    'ratSewer': Animal( 'Sewer Rat', 0x00EE, 0x0000, 10, 20, None ),


    ### Min skill 20, Max skill 30 ###
    'cowBrown': Animal( 'Cow', 0x00E7, 0x0000, 20, 30, None ),
    'cowBlack': Animal( 'Cow', 0x00D8, 0x0000, 20, 30, None ),
    'goat': Animal( 'Goat', 0x00D1, 0x0000, 20, 30, None ),
    'pig': Animal( 'Pig', 0x00CB, 0x0000, 20, 30, None ),
    'sheep': Animal( 'Sheep', 0x00CF, 0x0000, 20, 30, None ),


    ### Min skill 20, Max skill 50 ###
    'beetleGiant': Animal( 'Giant Beetle', 0x0317, 0x0000, 20, 50, None ),
    'slime': Animal( 'Slime', 0x0033, 0x0000, 20, 50, None ),


    ### Min skill 30, Max skill 40 ###
    'eagle': Animal( 'Eagle', 0x0005, 0x0000, 30, 40, None ),
    'bouraRuddy': None, # Not on UO Forever


    ### Min skill 40, Max skill 50 ###
    'boar': Animal( 'Boar', 0x0122, 0x0000, 40, 50, None ),
    'bullfrog': Animal( 'Bullfrog', 0x0051, 0x0000, 40, 50, None ),
    'bouraLowland': None, # Not on UO Forever
    'ferret': Animal( 'Ferret', 0x0117, 0x0000, 40, 50, None ),
    'ratGiant': Animal( 'Giant Rat', 0x00D7, 0x0000, 40, 50, None ),
    'hind': Animal( 'Hind', 0x00ED, 0x0000, 40, 50, None ),

    # Horses
    'horse': Animal( 'Horse', 0x00C8, 0x0000, 40, 50, None ),
    'horse2': Animal( 'Horse', 0x00E2, 0x0000, 40, 50, None ),
    'horse3': Animal( 'Horse', 0x00CC, 0x0000, 40, 50, None ),
    'horse4': Animal( 'Horse', 0x00E4, 0x0000, 40, 50, None ),
    'horsePack': Animal( 'Pack Horse', 0x0123, 0x0000, 40, 50, None ),
    'horsePalomino': None,
    'horseWar': None,

    # Llamas
    'llamaPack': Animal( 'Pack Llama', 0x0124, 0x0000, 40, 50, None ),
    'llamaRideable': None,

    # Ostards
    'ostardDesert': Animal( 'Desert Ostard', 0x00D2, 0x0000, 40, 50, [ 'Ostard' ] ),
    'ostardForestGreen': Animal( 'Forest Ostard', 0x00DB, 0x88A0, 40, 50, [ 'Ostard' ] ),
    'ostardForestRed': Animal( 'Forest Ostard', 0x00DB, 0x889D, 40, 50, [ 'Ostard' ] ),

    'wolfTimber': Animal( 'Timber Wolf', 0x00E1, 0x0000, 40, 50, [ 'Canine' ] ),
    'wolfRideable': Animal( 'Rideable Wolf', 0x0115, 0x0000, 40, 50, [ 'Canine' ] ),


    ### Min skill 50, Max skill 60 ###
    'bearBlack': Animal( 'Black Bear', 0x00D3, 0x0000, 50, 60, [ 'Bear' ] ),
    'bearPolar': Animal( 'Polar Bear', 0x00D5, 0x0000, 50, 60, [ 'Bear' ] ),
    'beetleDeathwatch': None,
    'llama': Animal( 'Llama', 0x00DC, 0x0000, 50, 60, None ),
    'walrus': Animal( 'Walrus', 0x00DD, 0x0000, 50, 60, None ),


    ### Min skill 60, Max skill 70 ###
    'alligator': Animal( 'Alligator', 0x00CA, 0x0000, 60, 70, None ),
    'bearBrown': Animal( 'Brown Bear', 0x00A7, 0x0000, 60, 70, [ 'Bear' ] ),
    'bouraHighPlains': None, # Not on UO Forever
    'cougar': Animal( 'Cougar', 0x003F, 0x0000, 60, 70, [ 'Feline' ] ),
    'paralithode': None, # Not on UO Forever
    'scorpion': Animal( 'Scorpion', 0x0030, 0x0000, 60, 70, None ),


    ### Min skill 70, Max skill 80 ###
    'bearRideablePolar': Animal( 'Polar Bear', 0x00D5, 0x0000, 70, 80, [ 'Bear' ] ),
    'bearGrizzly': Animal( 'Grizzly Bear', 0x00D4, 0x0000, 70, 80, [ 'Bear' ] ),
    'dragonYoung': None,
    'hartGreat': Animal( 'Great Hart', 0x00EA, 0x0000, 70, 80, None ),
    'leopardSnow': Animal( 'Snow Leopard', 0x0040, 0x0000, 70, 80, [ 'Feline' ] ),
    'leopardSnow2': Animal( 'Snow Leopard', 0x0041, 0x0000, 70, 80, [ 'Feline' ] ),
    'panther': Animal( 'Panther', 0x00D6, 0x0000, 70, 80, [ 'Feline' ] ),
    'snake': Animal( 'Snake', 0x0034, 0x0000, 70, 80, None ),
    'spiderGiant': Animal( 'Giant Spider', 0x001C, 0x0000, 70, 80, None ),
    'wolfGrey': Animal( 'Grey Wolf', 0x0019, 0x0000, 70, 80, [ 'Canine' ] ),
    'wolfGrey2': Animal( 'Grey Wolf', 0x001b, 0x0000, 70, 80, [ 'Canine' ] ),


    ### Min skill 80, Max skill 90 ###
    'gaman': None,
    'slithStone': None,
    'wolfWhite': Animal( 'White Wolf', 0x0022, 0x0000, 80, 90, [ 'Canine' ] ),
    'wolfWhite2': Animal( 'White Wolf', 0x0025, 0x0000, 80, 90, [ 'Canine' ] ),


    ### Min skill 90, Max skill 100 ###
    'bull': Animal( 'Bull', 0x00E8, 0x0000, 90, 100, [ 'Bull' ] ),
    'bull2': Animal( 'Bull', 0x00E9, 0x0000, 90, 100, [ 'Bull' ] ),
    'foxBlood': None,
    'hellcatSmall': Animal( 'Hellcat (Small)', 0x00C9, 0x0000, 90, 100, [ 'Feline' ] ),
    'mongbatGreater': None,
    'ostardFrenzied': Animal( 'Frenzied Ostard', 0x00DA, 0x0000, 90, 100, [ 'Ostard' ] ),
    'osseinRam': None,
    'spiderFrost': Animal( 'Frost Spider', 0x0014, 0x0000, 90, 100, None ),
    'toadGiant': Animal( 'Giant Toad', 0x0050, 0x0000, 90, 100, None ),
    'unicorn': None,
    'wormGiantIce': Animal( 'Giant Ice Worm', 0x0050, 0x0000, 90, 100, None ),


    ### Min skill 100, Max skill 110 ###
    # Drakes
    'drake': Animal( 'Drake', 0x003D, 0x0000, 100, 110, None ),
    'drakeCrimson': None,
    'drakePlaltinum': None,
    'drakeStygian': None,

    'hellcatLarge': Animal( 'Hellcat (Large)', 0x007F, 0x0000, 100, 110, [ 'Feline' ] ),
    'hellhound': Animal( 'Hellhound', 0x0062, 0x0000, 100, 110, [ 'Canine' ] ),
    'imp': None, # Pack type: Daemon
    'kitsuneBake': None,
    'lizardLava': Animal( 'Lava Lizard', 0x00CE, 0x0000, 100, 110, None ),

    # Ridgebacks
    'ridgeback': Animal( 'Ridgeback', 0x00BB, 0x0000, 100, 110, None ),
    'ridgebackSavage': Animal( 'Savage Ridgeback', 0x00BC, 0x0000, 100, 110, None ),

    'slith': None,
    'wolfDire': Animal( 'Dire Wolf', 0x0017, 0x0000, 100, 110, [ 'Canine' ] ), # Pack type: Canine


    ### Min skill 110, Max skill 120 ###
    'beetleDeath': None,
    'beetleFire': None,
    'beetleRune': None,

    'dragon': None,
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
    'spiderDread': Animal( 'Dread Spider', 0x000B, 0x0000, 110, 120, None ),
    'unicorn': None,
    'wolfTsuki': None,
    'wyrmWhite': None,


    ### Challenging ###
    'cuSidhe': None,

    'dimetrosaur': None, # Not on UO Forever

    # Dragons
    'dragonBane': None,
    'dragonFrost': None,
    'dragonGreater': None,
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
    'wyrmShadow': None,
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
