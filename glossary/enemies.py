from System.Collections.Generic import List
from System import Byte

class Notoriety:
    byte = Byte( 0 )
    color = ''
    description = ''

    def __init__ ( self, byte, color, description ):
        self.byte = byte
        self.color = color
        self.description = description

notorieties = {
    'innocent': Notoriety( Byte( 1 ), 'blue', 'innocent' ),
    'ally': Notoriety( Byte( 2 ), 'green', 'guilded/ally' ),
    'attackable': Notoriety( Byte( 3 ), 'gray', 'attackable but not criminal' ),
    'criminal': Notoriety( Byte( 4 ), 'gray', 'criminal' ),
    'enemy': Notoriety( Byte( 5 ), 'orange', 'enemy' ),
    'murderer': Notoriety( Byte( 6 ), 'red', 'murderer' ),
    'npc': Notoriety( Byte( 7 ), '', 'npc' )
}

def GetNotorietyList ( notorieties ):
    '''
    Returns a byte list of the selected notorieties
    '''
    notorietyList = []
    for notoriety in notorieties:
        notorietyList.append( notoriety.byte )

    return List[Byte]( notorietyList )

def GetEnemyNotorieties( minRange = 0, maxRange = 12 ):
    '''
    Returns a list of the common enemy notorieties
    '''
    global notorieties

    return GetNotorietyList( [
        notorieties[ 'attackable' ],
        notorieties[ 'criminal' ],
        notorieties[ 'enemy' ],
        notorieties[ 'murderer' ]
    ] )


def GetEnemies( Mobiles, minRange = 0, maxRange = 12, notorieties = GetEnemyNotorieties(), IgnorePartyMembers = False ):
    '''
    Returns a list of the nearby enemies with the specified notorieties
    '''

    if Mobiles == None:
        raise ValueError( 'Mobiles was not passed to GetEnemies' )

    enemyFilter = Mobiles.Filter()
    enemyFilter.Enabled = True
    enemyFilter.RangeMin = minRange
    enemyFilter.RangeMax = maxRange
    enemyFilter.Notorieties = notorieties
    enemyFilter.CheckIgnoreObject = True
    enemyFilter.Friend = False
    enemies = Mobiles.ApplyFilter( enemyFilter )

    if IgnorePartyMembers:
        partyMembers = [ enemy for enemy in enemies if enemy.InParty ]
        for partyMember in partyMembers:
            enemies.Remove( partyMember )

    return enemies
