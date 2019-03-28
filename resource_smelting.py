'''
Author: TheWarDoctor95
Other Contributors:
Last Contribution By: TheWarDoctor95 - March 22, 2019

Description: Smelts all ore into ingots
'''

enableSmeltFromPet = True

from Scripts.glossary.items import ores
from Scripts.utilities.colors import colors

messages = [
    'You smelt the ore removing the impurities and put the metal in your backpack.',
    'You burn away the impurities but are left with less useable metal.',
    'You skillfully extract extra metal out of the ore pile.'
]

def SmeltAllInMobile( mobile ):
    '''
    Smelts all raw ore in the target mobiles backpack
    '''
    global ores

    Journal.Clear()

    for ore in ores:
        oreStack = Items.FindByID( ores[ ore ].itemID, -1, mobile.Backpack.Serial )
        while oreStack != None:
            Items.UseItem( oreStack )

            Misc.Pause( 500 )

            oreStack = Items.FindByID( ores[ ore ].itemID, -1, mobile.Backpack.Serial )

def Smelt():
    '''
    Smelts all raw ore into ingots
    '''
    global enableSmeltFromPet

    if enableSmeltFromPet:
        pet = Target.PromptTarget( 'Select pet the ore is stored in' )
        if pet == None:
            Misc.SendMessage( 'Could not find pet! Will attempt to smelt any ore in your backpack.', 1100 )
        else:
            pet = Mobiles.FindBySerial( pet )
            SmeltAllInMobile( pet )

    SmeltAllInMobile( Player )
    Player.HeadMessage( colors[ 'green' ], 'Done smelting!' )

# Start smelting
Smelt()
