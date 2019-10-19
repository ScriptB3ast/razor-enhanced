from Scripts.glossary.enemies import GetEnemyNotorieties

def AttackEnemy():
    mobilesFilter = Mobiles.Filter()
    mobilesFilter.RangeMax = 1
    mobilesFilter.RangeMin = 1
    mobilesFilter.Friend = 0
    mobilesFilter.Notorieties = GetEnemyNotorieties()
    mobile = Mobiles.ApplyFilter( mobilesFilter )
    if len( mobile ) > 0:
        mobile = Mobiles.Select( mobile, 'Weakest' )
    else:
        return

    while Mobiles.FindBySerial( mobile.Serial ) != None and mobile.DistanceTo( Mobiles.FindBySerial( Player.Serial ) ) < 2:
        mobPosition = mobile.Position
        playerPosition = Player.Position
        if mobPosition.X == playerPosition.X and mobPosition.Y > playerPosition.Y:
            Player.ChatSay( 0, '!1' )
        elif mobPosition.X > playerPosition.X and mobPosition.Y > playerPosition.Y:
            Player.ChatSay( 0, '!2' )
        elif mobPosition.X > playerPosition.X and mobPosition.Y == playerPosition.Y:
            Player.ChatSay( 0, '!3' )
        elif mobPosition.X < playerPosition.X and mobPosition.Y > playerPosition.Y:
            Player.ChatSay( 0, '!4' )
        elif mobPosition.X > playerPosition.X and mobPosition.Y < playerPosition.Y:
            Player.ChatSay( 0, '!6' )
        elif mobPosition.X < playerPosition.X and mobPosition.Y == playerPosition.Y:
            Player.ChatSay( 0, '!7' )
        elif mobPosition.X < playerPosition.X and mobPosition.Y < playerPosition.Y:
            Player.ChatSay( 0, '!8' )
        elif mobPosition.X == playerPosition.X and mobPosition.Y < playerPosition.Y:
            Player.ChatSay( 0, '!9' )
        Misc.Pause( 1200 )

while True:
    AttackEnemy()
    Misc.Pause( 200 )
