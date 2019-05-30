# Adding an extra 200 ms in case of latency issues
hidingTimerMilliseconds = 10200
stealthTimerMilliseconds = 10200

Misc.SendMessage( 'Beginning Stealth training', 90 )

Timer.Create( 'hidingTimer', 1 )
Timer.Create( 'stealthTimer', 1 )

moveNorth = True

# while skill can increase and player is not dead
while Player.GetRealSkillValue( 'Stealth' ) < Player.GetSkillCap( 'Stealth' ) and not Player.IsGhost:
    if Player.GetSkillValue( 'Hiding' ) < 80.0:
        if not Timer.Check( 'hidingTimer' ):
            Player.UseSkill( 'Hiding' )
            Timer.Create( 'hidingTimer', hidingTimerMilliseconds )
            Timer.Create( 'stealthTimer', stealthTimerMilliseconds )
        continue

    if not Player.BuffsExist( 'Hiding' ):
        if not Timer.Check( 'hidingTimer' ):
            Player.UseSkill( 'Hiding' )
            Timer.Create( 'hidingTimer', hidingTimerMilliseconds )
            Timer.Create( 'stealthTimer', stealthTimerMilliseconds )
    elif Player.BuffsExist( 'Hiding' ) and not Timer.Check( 'stealthTimer' ):
        Player.UseSkill( 'Stealth' )
        Timer.Create( 'stealthTimer', stealthTimerMilliseconds )
        Timer.Create( 'hidingTimer', hidingTimerMilliseconds )

    if Player.GetSkillValue( 'Stealth' ) > 50.0:
        # After skill reaches 50, start walking to trigger stealth more often
        for i in range( 0, 5 ):
            if moveNorth:
                Player.Walk( 'North' )
            else:
                Player.Walk( 'South' )
            Misc.Pause( 50 )
        moveNorth = not moveNorth
        Misc.Pause( 200 )

    # Pause to ease CPU usage
    Misc.Pause( 500 )
Misc.SendMessage( 'Stealth training complete!' )
