containerToSort = 0x43924063
containerToSort = Items.FindBySerial( containerToSort )
Items.UseItem( containerToSort )
Misc.Pause( 700 )

circleOneBag = 0x41ACF8F7
circleTwoBag = 0x4025EC4C
circleThreeBag = 0x41ACF8F3
circleFourBag = 0x41AD6E77
circleFiveBag = 0x41AC0E93
circleSixBag = 0x42024252
circleSevenBag = 0x41ACDF7A
circleEightBag = 0x41AD1D51

from Scripts.glossary.spells import spells
from Scripts.glossary.items.spellScrolls import spellScrolls
spellScrollIDs = [ spellScrolls[ scroll ].itemID for scroll in spellScrolls ]
from Scripts.utilities.items import MoveItem

for item in containerToSort.Contains:
    if item.ItemID in spellScrollIDs:
        scrollType = None
        for scroll in spellScrolls:
            if spellScrolls[ scroll ].itemID == item.ItemID:
                scrollType = spellScrolls[ scroll ]
                break
        
        spell = spells[ scrollType.name.replace( ' scroll', '' ) ]
        if spell.circle == 1:
            MoveItem( Items, Misc, item, circleOneBag )
        elif spell.circle == 2:
            MoveItem( Items, Misc, item, circleTwoBag )
        elif spell.circle == 3:
            MoveItem( Items, Misc, item, circleThreeBag )
        elif spell.circle == 4:
            MoveItem( Items, Misc, item, circleFourBag )
        elif spell.circle == 5:
            MoveItem( Items, Misc, item, circleFiveBag )
        elif spell.circle == 6:
            MoveItem( Items, Misc, item, circleSixBag )
        elif spell.circle == 7:
            MoveItem( Items, Misc, item, circleSevenBag )
        elif spell.circle == 8:
            MoveItem( Items, Misc, item, circleEightBag )
