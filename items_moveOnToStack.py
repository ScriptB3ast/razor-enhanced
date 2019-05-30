from Scripts import config
from Scripts.glossary.colors import colors

itemSerial = Target.PromptTarget( 'Select item to place' )
item = Items.FindBySerial( itemSerial )

stackItemSerial = Target.PromptTarget( 'Select item from stack to place on' )
stackItem = Items.FindBySerial( stackItemSerial )

Items.MoveOnGround( itemSerial, 0, stackItem.Position.X, stackItem.Position.Y, 0 )
Misc.Pause( config.dragDelayMilliseconds )

Player.HeadMessage( color[ 'cyan' ], 'Moved the item!' )
