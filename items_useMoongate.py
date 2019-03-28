from System.Collections.Generic import List

def FindMoongate():
    '''
    Finds a moongate that the player can use
    '''
    
    moongateFilter = Items.Filter()
    moongateFilter.OnGround = 1
    moongateFilter.RangeMin = 0
    moongateFilter.RangeMax = 1
    moongateFilter.Movable = False
    moongateFilter.Graphics = List[int]( [ 0x0F6C ] )
    
    moongate = Items.ApplyFilter( moongateFilter )
    return moongate

moongate = FindMoongate()
if len( moongate ) > 0:
    Items.UseItem( moongate[ 0 ] )
    
    Gumps.WaitForGump( 3716879466, 2000 )
    Gumps.SendAction( 3716879466, 1 )
