bank = Items.FindBySerial( 0x42566C03 )

if bank != None:
    # Iron Ingots
    ironIngots = Items.FindByID( 0x1BF2, 0x0000, bank.Serial )
    if ironIngots == None:
        Misc.SendMessage( 'Iron Ingots: 0 (worth 0 gold)' )
    else:
        Misc.SendMessage( 'Iron Ingots: %i (worth %i gold)' % ( ironIngots.Amount, ironIngots.Amount * 10 ) )
    
    # Dull Copper Ingots
    dullCopperIngots = Items.FindByID( 0x1BF2, 0x0415, bank.Serial )
    if dullCopperIngots == None:
        Misc.SendMessage( 'Dull Copper Ingots: 0 (worth 0 gold)' )
    else:
        Misc.SendMessage( 'Dull Copper Ingots: %i (worth %i gold)' % ( dullCopperIngots.Amount, dullCopperIngots.Amount * 15 ) )
    
    # Shadow Iron Ingots
    shadowIronIngots = Items.FindByID( 0x1BF2, 0x0455, bank.Serial )
    if shadowIronIngots == None:
        Misc.SendMessage( 'Shadow Iron Ingots: 0 (worth 0 gold)' )
    else:
        Misc.SendMessage( 'Shadow Iron Ingots: %i (worth %i gold)' % ( shadowIronIngots.Amount, shadowIronIngots.Amount * 20 ) )
    
    # Copper Ingots
    copperIngots = Items.FindByID( 0x1BF2, 0x045F, bank.Serial )
    if copperIngots == None:
        Misc.SendMessage( 'Copper Ingots: 0 (worth 0 gold)' )
    else:
        Misc.SendMessage( 'Copper Ingots: %i (worth %i gold)' % ( copperIngots.Amount, copperIngots.Amount * 25 ) )
    
    # Bronze Ingots
    bronzeIngots = Items.FindByID( 0x1BF2, 0x06D8, bank.Serial )
    if bronzeIngots == None:
        Misc.SendMessage( 'Bronze Ingots: 0 (worth 0 gold)' )
    else:
        Misc.SendMessage( 'Bronze Ingots: %i (worth %i gold)' % ( bronzeIngots.Amount, bronzeIngots.Amount * 35 ) )
    
    # Agapite Ingots
    agapiteIngots = Items.FindByID( 0x1BF2, 0x097E, bank.Serial )
    if agapiteIngots == None:
        Misc.SendMessage( 'Agapite Ingots: 0 (worth 0 gold)' )
    else:
        Misc.SendMessage( 'Agapite Ingots: %i (worth %i gold)' % ( agapiteIngots.Amount, agapiteIngots.Amount * 45 ) )
    
    # Verite Ingots
    veriteIngots = Items.FindByID( 0x1BF2, 0x07D2, bank.Serial )
    if veriteIngots == None:
        Misc.SendMessage( 'Verite Ingots: 0 (worth 0 gold)' )
    else:
        Misc.SendMessage( 'Verite Ingots: %i (worth %i gold)' % ( veriteIngots.Amount, veriteIngots.Amount * 50 ) )
    
    # Valorite Ingots
    valoriteIngots = Items.FindByID( 0x1BF2, 0x0544, bank.Serial )
    if valoriteIngots == None:
        Misc.SendMessage( 'Valorite Ingots: 0 (worth 0 gold)' )
    else:
        Misc.SendMessage( 'Valorite Ingots: %i (worth %i gold)' % ( valoriteIngots.Amount, valoriteIngots.Amount * 60 ) )
