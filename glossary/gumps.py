class GumpOption:
    name = ''
    id = -1

    def __init__ ( self, name, id ):
        self.name = name
        self.id = id

class Gump:
    name = ''
    id = -1
    options = {}

    def __init__ ( self, name, id, options ):
        self.name = name
        self.id = id

        for option in options:
            self.options[ option.name ] = option

gumps = {
    resurrectionOptions = [
        GumpOption( 'Cancel', 0 ),
        GumpOption( 'Continue', 1 )
    ]
    'Resurrection': Gump( 'Resurrection', 2957810225, resurrectionOptions )

    tailoringOptions = [
        GumpOption( 'Last Ten', 28 ),
        GumpOption( 'Hats', 1 ),
        GumpOption( 'Shirts', 8 ),
        GumpOption( 'Pants', 15 ),
        GumpOption( 'Miscellaneous', 22 ),
        GumpOption( 'Footwear', 29 ),
        GumpOption( 'Leather Armor', 36 ),
        GumpOption( 'Studded Armor', 43 ),
        GumpOption( 'Female Armor', 50 ),
        GumpOption( 'Bone Armor', 57 ),
        GumpOption( 'Ship Tools', 64 ),
        GumpOption( 'Ship Upgrades', 71 ),
        GumpOption( 'Leather/Hides', 7 ),
        GumpOption( 'Repair', 42 ),
        GumpOption( 'Toggle Mark', 49 ),
        GumpOption( 'Exit', 0 ),
        GumpOption( 'Make Last', 7 )
    ]
    'TailoringMenu': Gump( 'TailoringMenu', 949095101, tailoringOptions )

    tailoringMenuLastTenOptions = [
        GumpOption( 'lastCrafted', 4 ),
        GumpOption( 'openLastCraftedMenu', 5 ),
        GumpOption( 'secondLastCrafted', 11 ),
        GumpOption( 'openSecondLastCraftedMenu', 12 ),
        GumpOption( 'thirdLastCrafted', 18 ),
        GumpOption( 'openThirdLastCraftedMenu', 19 ),
        GumpOption( 'fourthLastCrafted', 25 ),
        GumpOption( 'openFourthLastCraftedMenu', 26 ),
        GumpOption( 'fifthLastCrafted', 32 ),
        GumpOption( 'openFifthLastCraftedMenu', 33 ),
        GumpOption( 'sixthLastCrafted', 39 ),
        GumpOption( 'openSixthLastCraftedMenu', 40 ),
        GumpOption( 'seventhLastCrafted', 46 ),
        GumpOption( 'openSeventhLastCraftedMenu', 47 ),
        GumpOption( 'eighthLastCrafted', 53 ),
        GumpOption( 'openEighthLastCraftedMenu', 54 ),
        GumpOption( 'ninthLastCrafted', 60 ),
        GumpOption( 'openNinthLastCraftedMenu', 61 ),
        GumpOption( 'tenthLastCrafted', 67 ),
        GumpOption( 'openTenthLastCraftedMenu', 68 )
    ]
    'TailoringMenuLastTen': Gump( 'TailoringMenuLastTen', 949095101, tailoringMenuLastTenOptions )

    tailoringMenuHatsOptions = [
        GumpOption( 'skullcap', 2 ),
        GumpOption( 'openSkullcapMenu', 3 ),
        GumpOption( 'bandana', 9 ),
        GumpOption( 'openBandanaMenu', 10 ),
        GumpOption( 'floppy hat', 16 ),
        GumpOption( 'openFloppyHatMenu', 17 ),
        GumpOption( 'cap', 23 ),
        GumpOption( 'openCapMenu', 24 ),
        GumpOption( 'wide-brim hat', 30 ),
        GumpOption( 'openWideBrimHatMenu', 31 ),
        GumpOption( 'straw hat', 37 ),
        GumpOption( 'openStrawHatMenu', 38 ),
        GumpOption( 'tall straw hat', 44 ),
        GumpOption( 'openTallStrawHatMenu', 45 ),
        GumpOption( 'wizard\'s hat', 51 ),
        GumpOption( 'openWizardsHatMenu', 52 ),
        GumpOption( 'bonnet', 58 ),
        GumpOption( 'openBonnetMenu', 59 ),
        GumpOption( 'feathered hat', 65 ),
        GumpOption( 'openFeatheredHatMenu', 66 ),
        GumpOption( 'tricorne hat', 72 ),
        GumpOption( 'openTricorneHatMenu', 73 ),
        GumpOption( 'jester hat', 79 ),
        GumpOption( 'openJesterHatMenu', 80 )
    ]
    'TailoringMenuHats': Gump( 'TailoringMenuHats', 949095101, tailoringMenuHatsOptions )

    tailoringMenuShirtsOptions = [
        GumpOption( 'doublet', 2 ),
        GumpOption( 'openDoubletMenu', 3 ),
        GumpOption( 'shirt', 9 ),
        GumpOption( 'openShirtMenu', 10 ),
        GumpOption( 'fancy shirt', 16 ),
        GumpOption( 'openFancyShirtMenu', 17 ),
        GumpOption( 'tunic', 23 ),
        GumpOption( 'openTunicMenu', 24 ),
        GumpOption( 'surcoat', 30 ),
        GumpOption( 'openSurcoatMenu', 31 ),
        GumpOption( 'plain dress', 37 ),
        GumpOption( 'openPlainDressMenu', 38 ),
        GumpOption( 'fancy dress', 44 ),
        GumpOption( 'openFancyDressMenu', 45 ),
        GumpOption( 'cloak', 51 ),
        GumpOption( 'openCloakMenu', 52 ),
        GumpOption( 'robe', 58 ),
        GumpOption( 'openRobeMenu', 59 ),
        GumpOption( 'jester suit', 65 ),
        GumpOption( 'openJesterSuitMenu', 66 )
    ]
    'TailoringMenuShirts': Gump( 'TailoringMenuShirts', 949095101, tailoringMenuShirtsOptions )

    tailoringMenuCraftItemOptions = [
        GumpOption( 'Back', 0 ),
        GumpOption( 'Make Now', 1 )
    ]
    'TailoringMenuCraftItem': Gump( 'TailoringMenuCraftItem', 304105006, tailoringMenuCraftItemOptions )
}
