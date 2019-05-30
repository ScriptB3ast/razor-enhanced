'''
Author: TheWarDoctor95
Other Contributors:
Last Contribution By: TheWarDoctor95 - April 8, 2019

Description: Uses lockpicks on a non-GM tinker box and a GM tinker box to train
    Lockpicking up to 95 (max for tinker-made boxes)
'''

lockpickingTimerMilliseconds = 4200
hidingTimerMilliseconds = 10200

from Scripts.glossary.colors import colors
from Scripts.glossary.items.tools import tools
from Scripts.utilities.items import FindItem

lockpickItem = tools[ 'lockpick' ]

def TrainLockpicking():
    '''
    Trains lockpicking to 95 (max for tinker-made boxes)
    '''

    global lockpickingTimerMilliseconds
    global hidingTimerMilliseconds

    lockpicks = FindItem( lockpickItem.itemID, Player.Backpack )

    if lockpicks == None:
        Player.HeadMessage( colors[ 'red' ], 'You don''t have any lockpicks!' )
        return

    if not Misc.CheckSharedValue( 'nonGMBox' ):
        nonGMBox = Target.PromptTarget( 'Select the non-GM box' )
        Misc.SetSharedValue( 'nonGMBox', nonGMBox )

    if not Misc.CheckSharedValue( 'GMBox' ):
        GMBox = Target.PromptTarget( 'Select the GM box' )
        Misc.SetSharedValue( 'GMBox', GMBox )

    if not Misc.CheckSharedValue( 'keyRing' ):
        keyRing = Target.PromptTarget( 'Select the key ring' )
        Misc.SetSharedValue( 'keyRing', keyRing )

    Target.ClearLastandQueue()
    Misc.Pause( 200 )

    nonGMBox = Misc.ReadSharedValue( 'nonGMBox' )
    GMBox = Misc.ReadSharedValue( 'GMBox' )
    keyRing = Misc.ReadSharedValue( 'keyRing' )

    lockpickOngoing = False
    lockpickUsedOn = None
    checkLockpicks = False

    #while not Player.IsGhost and Player.GetRealSkillValue( 'Lockpicking' ) < 95.0:
    while not Player.IsGhost and Player.GetRealSkillValue( 'Lockpicking' ) < Player.GetSkillCap( 'Lockpicking' ):
        if not Player.BuffsExist( 'Hiding' ):
            if not Timer.Check( 'hidingTimer' ):
                Player.UseSkill( 'Hiding' )
                Timer.Create( 'hidingTimer', hidingTimerMilliseconds )
        elif not lockpickOngoing:
            Items.UseItem( lockpicks.Serial )
            Target.WaitForTarget( 2000, True )

            if Player.GetSkillValue( 'Lockpicking' ) <= 74.9:
                Target.TargetExecute( nonGMBox )
                lockpickUsedOn = nonGMBox
            else:
                Target.TargetExecute( GMBox )
                lockpickUsedOn = GMBox

            Misc.Pause( 1000 )
            lockpickOngoing = True
        else:
            if ( Journal.SearchByName( 'The lock quickly yields to your skill.', '' ) or
                    Journal.SearchByType( 'This does not appear to be locked.', 'Regular' ) ):

                # Re-lock the box
                Items.UseItem( keyRing )
                Target.WaitForTarget( 2000, True )
                Target.TargetExecute( lockpickUsedOn )

                Misc.Pause( 1000 )

                Journal.Clear()
                lockpickOngoing = False
                checkLockpicks = True
            elif ( Journal.SearchByName( 'You are unable to pick the lock.', '' ) or
                    Journal.SearchByName( 'You don''t see how that lock can be manipulated.', '' ) ):
                Journal.Clear()
                lockpickOngoing = False
                checkLockpicks = True

        if checkLockpicks:
            lockpicks = FindItem( lockpickItem.itemID, Player.Backpack )
            if lockpicks == None:
                Player.HeadMessage( colors[ 'red' ], 'Ran out of lockpicks!' )

        # Wait a little bit so that the while loop doesn't consume as much CPU
        Misc.Pause( 50 )

# Start Lockpicking training
TrainLockpicking()
