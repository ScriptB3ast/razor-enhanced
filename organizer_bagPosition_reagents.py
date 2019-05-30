def CorrectReagentsBagPosition():
    reagentsBag = None
    reagentsBagSharedValue = 'reagentsBag'

    if not Misc.CheckSharedValue( reagentsBagSharedValue ):
        reagentsBag = Target.PromptTarget( 'Select bag to move the reagents into' )
        Misc.SetSharedValue( reagentsBagSharedValue, reagentsBag )

    reagentsBag = Misc.ReadSharedValue( reagentsBagSharedValue )
    if reagentsBag == None or Items.FindBySerial( reagentsBag ) == None:
        Player.HeadMessage( 1100, 'Can\'t find reagents bag! Clearing stored bag' )
        Misc.RemoveSharedValue( reagentsBagSharedValue )
    reagentsBag = Items.FindBySerial( reagentsBag )

    blackPearl = Items.FindByID( 0x0F7A, -1, reagentsBag.Serial )
    bloodMoss = Items.FindByID( 0x0F7B, -1, reagentsBag.Serial )
    garlic = Items.FindByID( 0x0F84, -1, reagentsBag.Serial )
    ginseng = Items.FindByID( 0x0F85, -1, reagentsBag.Serial )
    madrakeRoot = Items.FindByID( 0x0F86, -1, reagentsBag.Serial )
    nightshade = Items.FindByID( 0x0F88, -1, reagentsBag.Serial )
    spidersSilk = Items.FindByID( 0x0F8D, -1, reagentsBag.Serial )
    sulfurousAsh = Items.FindByID( 0x0F8C, -1, reagentsBag.Serial )

    # Top row
    Items.Move( blackPearl, reagentsBag, 0, 0, 37 )
    Misc.Pause( 700 )
    Items.Move( bloodMoss, reagentsBag, 0, 60, 0 )
    Misc.Pause( 700 )
    Items.Move( garlic, reagentsBag, 0, 100, 0 )
    Misc.Pause( 700 )

    # Middle row
    Items.Move( ginseng, reagentsBag, 0, 45, 65 )
    Misc.Pause( 700 )
    Items.Move( madrakeRoot, reagentsBag, 0, 75, 65 )
    Misc.Pause( 700 )

    # Bottom row
    Items.Move( nightshade, reagentsBag, 0, 0, 100 )
    Misc.Pause( 700 )
    Items.Move( spidersSilk, reagentsBag, 0, 65, 100 )
    Misc.Pause( 700 )
    Items.Move( sulfurousAsh, reagentsBag, 0, 100, 100 )
    Misc.Pause( 700 )

CorrectReagentsBagPosition()
