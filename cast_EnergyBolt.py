enemy = Target.GetTargetFromList( 'enemy' )
while True:
    enemy = Mobiles.FindBySerial( enemy.Serial )
    if enemy == None:
        break
    while Player.Mana > 20:
        enemy = Mobiles.FindBySerial( enemy.Serial )
        if enemy == None:
            break
        Spells.CastMagery( 'Energy Bolt' )
        Target.WaitForTarget( 2000, False )
        Target.TargetExecute( enemy )
        Misc.Pause( 1600 )
    enemy = Mobiles.FindBySerial( enemy.Serial )
    if enemy == None:
        break
    Player.UseSkill( 'Meditation' )
    while Player.Mana < 34:
        Misc.Pause( 100 )
