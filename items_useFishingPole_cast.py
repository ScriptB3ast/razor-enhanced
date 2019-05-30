from Scripts.glossary.items.tools import tools

Items.UseItemByID( tools[ 'fishing pole' ].itemID )
    
Target.WaitForTarget( 2000, True )

x = Player.Position.X
y = Player.Position.Y - 3
statics = Statics.GetStaticsTileInfo( x, y, 0 )
if len( statics ) > 0:
    water = statics[ 0 ]
    Target.TargetExecute( x, y, water.StaticZ, water.StaticID )
else:
    Target.TargetExecute( x, y, -5, 0x0000 )
