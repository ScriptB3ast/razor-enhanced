target = Target.PromptTarget( 'Select animal to tame' )
Journal.Clear()
while not Journal.SearchByName( 'You start to tame the creature', Player.Name ):
    Player.UseSkill( 'Animal Taming' )
    Target.WaitForTarget( 2000, False )
    Target.TargetExecute( target )
    Misc.Pause( 100 )
