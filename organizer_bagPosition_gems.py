from Scripts.glossary.items.gems import gems

containerID = 0x43923D99

amber = Items.FindByID( gems[ 'amber' ].itemID, 0x0000, containerID )
Items.Move( amber, containerID, 0, 21, 13 )
Misc.Pause( 700 )

amethyst = Items.FindByID( gems[ 'amethyst' ].itemID, 0x0000, containerID )
Items.Move( amethyst, containerID, 0, 29, 13 )
Misc.Pause( 700 )

citrine = Items.FindByID( gems[ 'citrine' ].itemID, 0x0000, containerID )
Items.Move( citrine, containerID, 0, 34, 13 )
Misc.Pause( 700 )

diamond = Items.FindByID( gems[ 'diamond' ].itemID, 0x0000, containerID )
Items.Move( diamond, containerID, 0, 51, 13 )
Misc.Pause( 700 )

emerald = Items.FindByID( gems[ 'emerald' ].itemID, 0x0000, containerID )
Items.Move( emerald, containerID, 0, 72, 13 )
Misc.Pause( 700 )

rubies = Items.FindByID( gems[ 'rubies' ].itemID, 0x0000, containerID )
Items.Move( rubies, containerID, 0, 81, 13 )
Misc.Pause( 700 )

sapphire = Items.FindByID( gems[ 'sapphire' ].itemID, 0x0000, containerID )
Items.Move( sapphire, containerID, 0, 88, 13 )
Misc.Pause( 700 )

starSapphire = Items.FindByID( gems[ 'star sapphire' ].itemID, 0x0000, containerID )
Items.Move( starSapphire, containerID, 0, 87, 11 )
Misc.Pause( 700 )

tourmaline = Items.FindByID( gems[ 'tourmaline' ].itemID, 0x0000, containerID )
Items.Move( tourmaline, containerID, 0, 125, 13 )
Misc.Pause( 700 )
