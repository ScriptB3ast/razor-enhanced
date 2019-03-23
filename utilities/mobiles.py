def GetEmptyMobileList( Mobiles ):
    '''
    Creates a filter that returns an empty list, and then returns the empty list
    '''
    emptyFilter = Mobiles.Filter()
    emptyFilter.Enabled = True
    emptyFilter.Name = 'there_is_no_way this_is someones_name_since_its_way_too_long'
    return Mobiles.ApplyFilter( emptyFilter )
