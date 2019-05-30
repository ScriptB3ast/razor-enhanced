from Scripts.glossary.colors import colors

enemy = Target.GetTargetFromList( 'enemy' )
if enemy != None:
    if Target.HasTarget():
        Target.TargetExecute( enemy )
    else:
        Player.Attack( enemy )
else:
    Player.HeadMessage( colors[ 'red' ], 'No enemies nearby!' )

Misc.Pause( 100 )
