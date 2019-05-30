# RAZOR ENHANCED LOOT SCRIPT
#
# discord : Jewele
#
# Script for Razor Enhanced to show loot in nearby corpses.
#
# If you obtained this script by itself, stop immediately. It will not work without image files.
# Go to : https://github.com/gmccord333/UOScripts/tree/master/RazorEnhanced/EnhancedLoot
# and download the entire package.
#
# VERSION HISTORY
# ===============
# 1.6.2 - Initial release
#

import clr, time, thread, time, re, datetime, sys
clr.AddReference('System')
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Data')

import System
from System import TimeSpan, Guid
from System.IO import File, Directory, MemoryStream
from System.ComponentModel import BackgroundWorker
from System.Timers import Timer
from System.Collections.Generic import List
from System.Threading import Mutex, AbandonedMutexException
from System.Threading import Thread
from System.Threading.Thread import Sleep
from System.Drawing import Point, Color, Size, Image, Font, ContentAlignment
from System.Windows.Forms import (
    Application, Button, Form, BorderStyle, FormBorderStyle, Cursor, Cursors,
    Label, FlatStyle, DataGridView, DataGridViewAutoSizeColumnMode,
    DataGridViewRow, DataGridViewAutoSizeColumnsMode,
    DataGridViewSelectionMode, DataGridViewEditMode, CheckBox,
    DataGridViewDataErrorContexts, ControlStyles, DataGridViewCellBorderStyle,
    DataGridViewAdvancedCellBorderStyle, ToolTip,
    DataGridViewColumnHeadersHeightSizeMode, PictureBox, FormWindowState,
    ImageList, DataGridViewHeaderBorderStyle, DataGridViewCheckBoxColumn,
    DataGridViewColumn, DataGridViewColumnSortMode, BindingSource)
from System.Data import DataTable

SCRIPT_NAME = 'UORazor Enhanced Loot'
SCRIPT_VERSION = '1.6.2'
COLOR_NORMAL = 76
COLOR_WARN = 44
COLOR_ERROR = 33
BACKGROUND = Directory.GetCurrentDirectory() + "\\scripts\\images\\loot.png"
IMG_HAND = Directory.GetCurrentDirectory() + "\\scripts\\images\\hand.png"
IMG_PICK = Directory.GetCurrentDirectory() + "\\scripts\\images\\pick.png"
IMG_CLOSE = Directory.GetCurrentDirectory() + "\\scripts\\images\\close.png"
IMG_CUT = Directory.GetCurrentDirectory() + "\\scripts\\images\\cut.png"
IMG_HIDDEN = Directory.GetCurrentDirectory() + "\\scripts\\images\\hidden.png"
IMG_JEWEL = Directory.GetCurrentDirectory() + "\\scripts\\images\\jewel.png"
IMG_COIN = Directory.GetCurrentDirectory() + "\\scripts\\images\\coin.png"
IMG_BAG = Directory.GetCurrentDirectory() + "\\scripts\\images\\bag.png"
IMG_REDSKULL = Directory.GetCurrentDirectory() + "\\scripts\\images\\redskull.png"
IMG_SKULL = Directory.GetCurrentDirectory() + "\\scripts\\images\\skull.png"
FILE_LOOT = Directory.GetCurrentDirectory() + "\\loot.txt"
FILE_DEBUG = Directory.GetCurrentDirectory() + "\\debug.txt"
LOADED_IMG_REDSKULL = None
LOADED_IMG_SKULL = None
MSG_EMPTY = 'Corpse is empty, use Cut button to harvest materials or Close'
MSG_INNOCENT = 'You have disabled opening innocent corpses. Hit Refresh to renew status'
MSG_HIDDEN = 'You are hidden, opening a corpse not your own will reveal you!'

ZEROPOS_ITEMS = ['magical crystal (1F19)']

# Affects time to wait between looting multiple items. 
# 100ms is aggressive
# 400ms is safe
# 500ms was very safe

LOOT_WAIT = 300

# This is how often the script tries to synchronize itself with the 
# world around the player. A good estimate is 500 ms. There isn`t much
# benefit to making this a low number.
WORKER_WAIT = 1000

COLOR_NORMAL = 76
COLOR_WARN = 44
COLOR_ERROR = 33

MUTEX_NAME = Guid.NewGuid()
MUTEX = Mutex(MUTEX_NAME)

# do not enable this unless you are debugging
DEBUG = False

# word fix patterns I know about
WORD_FIXES = {
    "scro[l]+": "scroll",
    "scr?$": "scroll",
    "scro$": "scroll",
    "sc$": "scroll"
}

blades = [
    0x1401, 0xf52, 0x13b9, 0xf61, 0x1441, 0x13b6, 0xec4, 0x13f6, 0xf5e, 0x13ff,
    0xec3
]
axes = [0xf43, 0xf4b, 0x143e, 0xf45, 0x1443, 0xf4d]

##########
# Debug output to file, leave off unless investigating code issues.
#
def _debug(s):
    if DEBUG:
        with open(FILE_DEBUG, "a") as myfile:
            myfile.write("{0} {1}\n".format(datetime.datetime.now(), s))

##########
# Loads image from disk in non-blocking way so we dont have resource contention locks
#
def Image_From_File(path):

    try:
        bytes = File.ReadAllBytes(path)
        ms = MemoryStream(bytes)
        img = Image.FromStream(ms)
        return img
    except Exception as e:
        _debug("Caught exception in Image FromFile : {0}".format(str(e)))
            
##########
# Class which interfaces with a local file, containing user loot preferences
#
class Settings_Manager(object):

    ##########
    # Class initialization
    #
    def __init__(self, file):

        try:
            self.File = file
            if not File.Exists(self.File):
                File.Create(self.File)
            self.IDs = List[System.String]
            self.Load()

        except Exception as e:
            _debug("Caught exception in Settings_Manager.__init__: {0}".format(
                str(e)))
            raise

    ##########
    # Loads player preferences into memory
    #
    def Load(self):

        try:
            assert File.Exists(self.File), "Missing file : {0}".format(
                self.File)
            self.IDs = List[System.String](File.ReadAllLines(self.File))
        except Exception as e:
            _debug("Caught exception in Settings_Manager.Load {0}".format(
                str(e)))
            raise

    ##########
    # Allows script to query whether an item has been set as preferred
    #
    def IsAlwaysLoot(self, id):

        try:
            assert File.Exists(self.File), "Missing file : {0}".format(
                self.File)
            return self.IDs.Contains(str(id))
        except Exception as e:
            _debug("Caught exception in Settings_Manager.IsAlwaysLoot: {0}".
                   format(str(e)))
            raise

    ##########
    # Allows script to save an item`s preferred status. Only writes to file
    # if there was actually a change.
    #
    def SetAlwaysLoot(self, id, toggle):

        try:
            assert File.Exists(self.File), "Missing file : {0}".format(
                self.File)
            updated = False

            # amend list for new or removed items
            if self.IDs.Contains(str(id)):
                if toggle == False:
                    self.IDs.Remove(str(id))
                    updated = True
            else:
                if toggle == True:
                    self.IDs.Add(str(id))
                    updated = True

            if updated:
                file = open(self.File, 'w')
                file.write(System.String.Join("\n", self.IDs))
                file.close()

        except Exception as e:
            _debug(
                "Caught exception in Settings_Manager.SetAlwaysLoot() : {0}".
                format(str(e)))

##########
# Class which keeps track of all nearby corpses and tags the ones the user has processed already.
#
class Corpse_Manager(object):

    _corpses = []
    _ignore = []

    ##########
    # Copies the passed in list to a local variable; accepts a list of items from a filter
    # configured to locate corpses.
    #
    def Synchronize(self, corpses):

        _debug("Corpse_Manager.Synchronize.start")
        _debug(corpses)

        if not MUTEX.WaitOne(TimeSpan.Zero):
            return

        try:

            self._corpses = []
            for corpse in corpses:

                # do not add corpse if Player has already processed it
                if corpse.Serial in self._ignore:
                    _debug("ignored by serial {0}".format(corpse.Serial))
                    continue

                _debug("added {0}".format(corpse.Serial))
                self._corpses.append(corpse)

            _debug("_corpses = {0}".format(self._corpses))

        except Exception as e:

            _debug("Caught exception in Corpse_Manager.Synchronize() : {0}".
                   format(str(e)))
        finally:

            MUTEX.ReleaseMutex()
            _debug("Corpse_Manager.Synchronize.exit")

    ##########
    # Ignores a corpse; for example, user has looted it, or closed the window on viewing it
    #
    def Ignore(self, o):

        try:

            assert o is not None, "A valid object was passed to function"
            if o.Serial not in self._ignore:
                self._ignore.append(o.Serial)
            old = list(self._corpses)
            self.Synchronize(old)

        except Exception as e:

            _debug("Caught exception in Corpse_Manager.Ignore() : {0}".format(
                str(e)))

    ##########
    # Reports whether a corpse has been inventoried by this class instance. For example,
    # if a player encounters a new corpse, script can query this class to find out whether
    # the corpse was seen before, or is new.
    #
    def Contains(self, o):

        try:

            if o == None:
                return False
            for corpse in self._corpses:
                if corpse.Serial == o.Serial:
                    return True
            return False

        except Exception as e:

            _debug(
                "Caught exception in Corpse_Manager.Contains() : {0}".format(
                    str(e)))

    ##########
    # Returns first object in list or None
    #
    def GetNext(self):

        _debug("Corpse_Manager.GetNext (currently at {0})".format(
            len(self._corpses)))
        if len(self._corpses) > 0:
            return self._corpses[0]
        else:
            return None

##########
# User form
class LootForm(Form):

    CM = Corpse_Manager()
    SM = Settings_Manager(FILE_LOOT)
    DT = DataTable()
    BS = BindingSource()
    Corpse = None
    IsInnocent = False
    IsCriminal = False
    Loaded = False
    HasBag = False
    Contents = []
    LootBag = None
    isMouseDown = False
    lastLocation = None

    def __init__(self):

        _debug("LootForm.__init__.start()")

        try:

            self.ShownInTaskbar = True
            self.FormBorderStyle = System.Windows.Forms.FormBorderStyle. None
            self.SetStyle(ControlStyles.SupportsTransparentBackColor, True)
            self.BackColor = Color.FromArgb(0, 0, 1)
            self.ForeColor = Color.FromArgb(231, 231, 231)
            self.Size = Size(280, 340)
            self.Text = '{0} - v{1}'.format(SCRIPT_NAME, SCRIPT_VERSION)
            self.TopMost = True
            self.MinimizeBox = False
            self.MaximizeBox = False

            self.DT.Columns.Add('Item', System.Type.GetType("System.Object"))
            self.DT.Columns.Add('Loot?', System.Type.GetType("System.Boolean"))
            self.DT.Columns.Add('Name', clr.GetClrType(str))
            self.DT.Columns.Add('Always',
                                System.Type.GetType("System.Boolean"))

            # Data binding
            self.BS.DataSource = self.DT
            self.DataGridSetup()
            self.DataGrid.DataSource = self.BS

            # lbl name
            self.lblName = Label()
            self.lblName.Text = Player.Name
            self.lblName.Location = Point(51, 10)
            self.lblName.Width = 180
            self.lblName.Font = Font("Tahoma", 11)
            self.lblName.ForeColor = Color.Cyan
            self.lblName.BackColor = Color.Transparent
            self.lblName.TextAlign = ContentAlignment.MiddleCenter

            # lbl status
            self.lblStatus = Label()
            self.lblStatus.Text = ""
            self.lblStatus.Location = Point(51, 251)
            self.lblStatus.Width = 180
            self.lblStatus.Font = Font("Tahoma", 10)
            self.lblStatus.ForeColor = Color.White
            self.lblStatus.BackColor = Color.Transparent
            self.lblStatus.TextAlign = ContentAlignment.MiddleCenter
            self.lblStatus.Visible = False

            # lbl weight
            self.lblWeight = Label()
            self.lblWeight.Text = ''
            self.lblWeight.Location = Point(101, 40)
            self.lblWeight.Width = 80
            self.lblWeight.Font = Font("Tahoma", 9)
            self.lblWeight.ForeColor = Color.Gold
            self.lblWeight.BackColor = Color.Transparent
            self.lblWeight.TextAlign = ContentAlignment.MiddleCenter

            # lbl message
            self.lblMsg = Label()
            self.lblMsg.Text = ""
            self.lblMsg.Location = Point(40, 120)
            self.lblMsg.Width = 200
            self.lblMsg.Height = 80
            self.lblMsg.Font = Font("Tahoma", 9)
            self.lblMsg.ForeColor = Color.White
            self.lblMsg.BackColor = Color.Black
            self.lblMsg.Visible = True

            # open button
            self.btnOpen = Button()
            self.btnOpen.ForeColor = Color.White
            self.btnOpen.BackColor = Color.Transparent
            self.btnOpen.Text = "Open"
            self.btnOpen.Cursor = Cursors.Hand
            self.btnOpen.Location = Point(110, 175)
            self.btnOpen.Size = Size(50, 50)
            self.btnOpen.FlatStyle = FlatStyle.Flat
            self.btnOpen.FlatAppearance.BorderSize = 0
            self.btnOpen.Click += self.btnOpenPressed
            self.btnOpen.Image = Image_From_File(IMG_HIDDEN)
            self.btnOpen.GotFocus += self.Form_Open_GotFocus
            self.btnOpen.MouseEnter += self.Form_Open_MouseEnter
            self.btnOpen.MouseLeave += self.Form_Open_MouseLeave
            self.btnOpen.Visible = False

            # get button
            self.btnGet = Button()
            self.btnGet.BackColor = Color.Transparent
            self.btnGet.Cursor = Cursors.Hand
            self.btnGet.Location = Point(5, 285)
            self.btnGet.Size = Size(50, 50)
            self.btnGet.FlatStyle = FlatStyle.Flat
            self.btnGet.FlatAppearance.BorderSize = 0
            self.btnGet.Click += self.btnGetPressed
            self.btnGet.Image = Image_From_File(IMG_HAND)
            self.btnGet.GotFocus += self.Form_Get_GotFocus
            self.btnGet.MouseEnter += self.Form_Get_MouseEnter
            self.btnGet.MouseLeave += self.Form_Get_MouseLeave
            self.btnGet.Visible = False

            # cut button
            self.btnCut = Button()
            self.btnCut.Cursor = Cursors.Hand
            self.btnCut.BackColor = Color.Transparent
            self.btnCut.Location = Point(60, 285)
            self.btnCut.Size = Size(50, 50)
            self.btnCut.FlatStyle = FlatStyle.Flat
            self.btnCut.FlatAppearance.BorderSize = 0
            self.btnCut.Click += self.btnCutPressed
            self.btnCut.Image = Image_From_File(IMG_CUT)
            self.btnCut.GotFocus += self.Form_Cut_GotFocus
            self.btnCut.MouseEnter += self.Form_Cut_MouseEnter
            self.btnCut.MouseLeave += self.Form_Cut_MouseLeave
            self.btnCut.Visible = False

            # bag button
            self.btnBag = Button()
            self.btnBag.Cursor = Cursors.Hand
            self.btnBag.BackColor = Color.Transparent
            self.btnBag.Location = Point(115, 285)
            self.btnBag.Size = Size(50, 50)
            self.btnBag.FlatStyle = FlatStyle.Flat
            self.btnBag.FlatAppearance.BorderSize = 0
            self.btnBag.Click += self.btnBagPressed
            self.btnBag.Image = Image_From_File(IMG_BAG)
            self.btnBag.GotFocus += self.Form_Bag_GotFocus
            self.btnBag.MouseEnter += self.Form_Bag_MouseEnter
            self.btnBag.MouseLeave += self.Form_Bag_MouseLeave
            self.btnBag.Visible = False

            # pick button
            self.btnPick = Button()
            self.btnPick.Cursor = Cursors.Hand
            self.btnPick.BackColor = Color.Transparent
            self.btnPick.Location = Point(170, 285)
            self.btnPick.Size = Size(50, 50)
            self.btnPick.FlatStyle = FlatStyle.Flat
            self.btnPick.FlatAppearance.BorderSize = 0
            self.btnPick.Click += self.btnPickPressed
            self.btnPick.Image = Image_From_File(IMG_PICK)
            self.btnPick.GotFocus += self.Form_Pick_GotFocus
            self.btnPick.MouseEnter += self.Form_Pick_MouseEnter
            self.btnPick.MouseLeave += self.Form_Pick_MouseLeave
            self.btnPick.Visible = False

            # close button
            self.btnClose = Button()
            self.btnClose.Cursor = Cursors.Hand
            self.btnClose.BackColor = Color.Transparent
            self.btnClose.Location = Point(225, 285)
            self.btnClose.Size = Size(50, 50)
            self.btnClose.FlatStyle = FlatStyle.Flat
            self.btnClose.FlatAppearance.BorderSize = 0
            self.btnClose.Click += self.btnClosePressed
            self.btnClose.Image = Image_From_File(IMG_CLOSE)
            self.btnClose.GotFocus += self.Form_Close_GotFocus
            self.btnClose.MouseEnter += self.Form_Close_MouseEnter
            self.btnClose.MouseLeave += self.Form_Close_MouseLeave
            self.btnClose.Visible = False

            # upper right corner skull overlay
            self.picSkull = PictureBox()
            self.picSkull.Cursor = Cursors.Hand
            self.picSkull.Location = Point(221, 0)
            self.picSkull.Size = Size(59, 61)
            self.picSkull.Image = LOADED_IMG_SKULL
            self.picSkull.Click += self.picSkullPressed
            self.picSkull.MouseEnter += self.Form_Skull_MouseEnter
            self.picSkull.MouseLeave += self.Form_Skull_MouseLeave
            self.picSkull.Visible = True

            # mouse form move event handlers
            self.MouseDown += self.Form_MouseDown
            self.MouseMove += self.Form_MouseMove
            self.MouseUp += self.Form_MouseUp
            self.lblName.MouseDown += self.Form_MouseDown
            self.lblName.MouseMove += self.Form_MouseMove
            self.lblName.MouseUp += self.Form_MouseUp
            self.lblWeight.MouseDown += self.Form_MouseDown
            self.lblWeight.MouseMove += self.Form_MouseMove
            self.lblWeight.MouseUp += self.Form_MouseUp
            self.lblStatus.MouseDown += self.Form_MouseDown
            self.lblStatus.MouseMove += self.Form_MouseMove
            self.lblStatus.MouseUp += self.Form_MouseUp
            self.DataGrid.MouseDown += self.Form_MouseDown
            self.DataGrid.MouseMove += self.Form_MouseMove
            self.DataGrid.MouseUp += self.Form_MouseUp

            # tooltips
            self.ToolTip = ToolTip()
            self.ToolTip.SetToolTip(self.btnClose, "Close")
            self.ToolTip.SetToolTip(self.btnCut, "Cut corpse")
            self.ToolTip.SetToolTip(self.btnGet, "Get selected")
            self.ToolTip.SetToolTip(self.btnPick, "Set bag")
            self.ToolTip.SetToolTip(self.btnBag, "Open containers")

            # add controls
            self.Controls.Add(self.DataGrid)
            self.Controls.Add(self.btnGet)
            self.Controls.Add(self.btnOpen)
            self.Controls.Add(self.btnClose)
            self.Controls.Add(self.btnPick)
            self.Controls.Add(self.btnCut)
            self.Controls.Add(self.btnBag)
            self.Controls.Add(self.lblWeight)
            self.Controls.Add(self.lblMsg)
            self.Controls.Add(self.lblName)
            self.Controls.Add(self.picSkull)
            self.Controls.Add(self.lblStatus)

            self.BackgroundImage = Image_From_File(BACKGROUND)

            # add background worker
            self._worker = BackgroundWorker()
            self._worker.DoWork += self.__start
            self._worker.ProgressChanged += self.__update
            self._worker.WorkerReportsProgress      = True;
            self._worker.WorkerSupportsCancellation = True;
            self._worker.RunWorkerAsync();

            # hide on startup
            self.Opacity = 0
            self.ShowInTaskbar = False

        except Exception as e:

            _debug("Caught exception in LootForm.__init__() : {0}".format(
                str(e)))
            raise

        _debug("LootForm.__init__.exit")

    ##########
    # Sets up the DataGrid, doing initialization, formatting, and adding event handlers
    #
    def DataGridSetup(self):

        _debug("LootForm.DataGridSetup.start")
        self.DataGrid = DataGridView()
        self.DataGrid.RowHeadersVisible = False
        self.DataGrid.MultiSelect = False
        self.DataGrid.BackgroundColor = Color.Black
        self.DataGrid.RowsDefaultCellStyle.BackColor = Color.Black
        self.DataGrid.RowsDefaultCellStyle.ForeColor = Color.White
        self.DataGrid.EnableHeadersVisualStyles = False
        self.DataGrid.ColumnHeadersDefaultCellStyle.BackColor = Color.Black
        self.DataGrid.CellBorderStyle = DataGridViewCellBorderStyle. None
        self.DataGrid.RowHeadersBorderStyle = DataGridViewHeaderBorderStyle. None
        self.DataGrid.ColumnHeadersBorderStyle = DataGridViewHeaderBorderStyle. None
        self.DataGrid.AdvancedCellBorderStyle.Left = DataGridViewAdvancedCellBorderStyle. None
        self.DataGrid.AdvancedCellBorderStyle.Right = DataGridViewAdvancedCellBorderStyle. None
        self.DataGrid.AutoGenerateColumns = True
        self.DataGrid.BorderStyle = BorderStyle. None
        self.DataGrid.ForeColor = Color.White
        self.DataGrid.Location = Point(40, 60)
        self.DataGrid.Width = 200
        self.DataGrid.Height = 180
        self.DataGrid.AllowUserToResizeColumns = False
        self.DataGrid.AllowUserToResizeRows = False
        self.DataGrid.AllowUserToAddRows = False
        self.DataGrid.BorderStyle = BorderStyle. None
        self.DataGrid.DefaultCellStyle.Font = Font("Tahoma", 9)
        self.DataGrid.AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode. None
        self.DataGrid.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.DisableResizing
        self.DataGrid.CellMouseEnter += self.Form_DataGrid_MouseEnter
        self.DataGrid.CellContentClick += self.CellClick
        self.DataGrid.SelectionChanged += self.SelectionChanged
        self.DataGrid.CellPainting += self.Form_DataGrid_CellPaint
        self.DataGrid.Visible = False
        _debug("LootForm.DataGridSetup.exit")

    ##########
    # Event handler for drawing icons in the datagridview header row
    #
    def Form_DataGrid_CellPaint(self, sender, e):

        if e.RowIndex == -1 and e.ColumnIndex == 1:
            point = e.CellBounds.Location
            e.Graphics.DrawImage(Image_From_File(IMG_COIN), point)
            e.Handled = True
        elif e.RowIndex == -1 and e.ColumnIndex == 3:
            point = e.CellBounds.Location
            e.Graphics.DrawImage(Image_From_File(IMG_JEWEL), point)
            e.Handled = True

    ##########
    # (WORKER THREAD)
    # Function which the worker thread will execute outside the main thread. Script constantly
    # scans near player for a list of corpses, and if found, passes that list back to the UI
    # thread for processing.
    #
    def __start(self, sender, e):

        _debug("LootForm.[Worker].__start.start")

        _mutex = Mutex(MUTEX_NAME)

        try:

           
            # Loop waiting for cancel request from Form or script
            while not self._worker.CancellationPending:

                Thread.Sleep(WORKER_WAIT)

                # if dead just loop
                if Player.Hits == 0:
                    continue

                if not _mutex.WaitOne(TimeSpan.Zero):
                    _debug("worker: mutex locked")
                    continue

                try:

                    # 3 tiles, diagonal loot fix.
                    filter = Items.Filter()
                    filter.Enabled = True
                    filter.OnGround = True
                    filter.Movable = False
                    filter.RangeMax = 3
                    filter.IsCorpse = True

                    # this generates a list of coordinates around which a player can loot
                    loot_range = self.GetLootCoords()

                    # re-process the filter results, and add anything in range
                    corpse_list = []
                    for corpse in Items.ApplyFilter(filter):
                        for coord in loot_range:
                            if corpse.Position.X == coord[0] and corpse.Position.Y == coord[1]:
                                corpse_list.append(corpse)

                    # send list out of background worker to main thread
                    sender.ReportProgress(0, corpse_list)

                except Exception as e:
                    _debug(
                        "Caught exception in LootForm.[Worker].__start : {0} - {1}".
                        format(type(ex), ex))

                finally:
                    _mutex.ReleaseMutex()

            # Got the cancel request, exit normally
            if self._worker.CancellationPending:
                _debug(
                    "LootForm.[Worker].__start CancellationPending detected, sending Cancel request"
                )
                e.Cancel = True

        except Exception as ex:
            _debug("Caught exception in LootForm.[Worker].__start : {0} - {1}".
                   format(type(ex), ex))

        _debug("LootForm.[Worker].__start.exit")
    
        
    ##########
    # UORazor Enhanced range filters only work in straight lines on X,Y axes. It does not work in
    # diagonals, although the game supports looting at 2 diagonal tiles away from player.
    # In order to fix this, we need to generate a list of valid tiles around player in which
    # a corpse can be looted.
    #
    def GetLootCoords(self):

        _out = []

        # calculate tuples of coordinates around player within 2 spaces
        for x in range(Player.Position.X - 2, Player.Position.X + 3):
            for y in range(Player.Position.Y - 2, Player.Position.Y + 3):
                _out.append((x, y))

        return _out

    ##########
    # Event handler for worker thread progress notifications. When the worker thread updates
    # nearby corpses, it will send that list to this function, which runs in the main thread.
    #
    def __update(self, sender, e):

        _debug("LootForm.__update.start [{0}]".format(e.UserState))
        if not MUTEX.WaitOne(TimeSpan.FromSeconds(1)):
            return

        try:

            # synchronize Corpse Manager with corpses around player
            self.CM.Synchronize(e.UserState)
            
            # update player wait
            self.UpdateWeight()

            # process next corpse if not viewing one
            if self.Corpse == None:
                
                self.Corpse = self.CM.GetNext()
                
                # reset corpse flags and clear contents
                self.IsInnocent = False
                self.IsCriminal = False
                self.Loaded = False
                self.HasBag = False
                self.Contents = []

                # if we got valid corpse
                if self.Corpse != None:
            
                    # if player visible, load it
                    if Player.Visible:
                        self.LoadCorpse()
                        
                    self.UpdateViewState()
                
            # player is viewing an invalid corpse
            elif not self.CM.Contains(self.Corpse):
                
                self.Corpse = None
                self.UpdateViewState()

            # player is visible and corpse wasn`t loaded 
            # (handles case where player was hidden but 
            # becomes visible at corpse)
            elif Player.Visible and not self.Loaded and not self.IsInnocent:
                
                self.LoadCorpse()
                self.UpdateViewState()

        except Exception as ex:

            _debug("Caught exception in LootForm.__update : {0}".format(ex))
            raise

        finally:

            MUTEX.ReleaseMutex()
            _debug("LootForm.__update.exit")

    ##########
    # Retrieves contents of a container and sets local variables IsInnocent and IsCriminal
    #
    def InventoryContainer(self, container):

        _debug("LootForm.InventoryContainer.start")

        try:
            
            contents = []
            Journal.Clear()            
            
            if container != None:

                # Tries to open a container and get its contents 5 times
                # If we do not get a `must wait` in journal, that means we opened it.
                # There is no mechanism in the game to determine that you have opened a container,
                # other than trying to open it when its not ready will print a journal message.
                # If we do not get the wait message, we can conclude it opened.
                #
                # This is what a debug log looks like when this occurs:
                # -----------------------------------------------------
                # 2018-08-10 21:34:22.215000 LootForm.InventoryContainer.start
                # 2018-08-10 21:34:22.218000 Container open attempt 0
                # 2018-08-10 21:34:22.473000 Received journal wait message
                # 2018-08-10 21:34:22.482000 Container open attempt 1
                # 2018-08-10 21:34:22.673000 Received journal wait message
                # 2018-08-10 21:34:22.679000 Container open attempt 2
                # 2018-08-10 21:34:22.786000 No journal wait message
                # 2018-08-10 21:34:22.792000 Found item : clean bandage%s% (0E21)
                #
                # In example, failed twice, got it on 3rd attempt. ^^
                #
                for i in range(6):
                    
                    _debug("Container open attempt {0}".format(i))

                    Items.UseItem(container)
                    
                    # Pause to let journal catch up
                    Misc.Pause(100)
                    
                    # Wait for contents
                    Items.WaitForContents(container, 100)

                    # Wait for disabled corpse messages
                    if Journal.Search("disabled opening innocent corpses"):
                        _debug ("Innocent warning detected, returning")
                        self.IsInnocent = True
                        return []
                    else:
                        _debug ("No innocent warning detected")
                    
                    # Wait for criminal act messages
                    if Journal.Search("criminal act"):
                        _debug ("Criminal act warning detected")
                        self.IsCriminal = True
                    else:
                        _debug ("No criminal warning detected")

                    # Wait for must wait messages
                    if Journal.Search("must wait"):
                        _debug("Received journal wait message")
                        Journal.Clear()
                        continue
                    else:
                        _debug("No journal wait message")
                        break

                # load container contents
                for item in container.Contains:
                    
                    _debug("Found item : {0}".format(item.Name))
                    _debug(" -- container? {0}".format(item.IsContainer))
                    
                    if item.Position.X == 0 and item.Position.Y == 0 and item.Position.Z == 0 and item.Name:
                        _debug("Zero position item found")
                        if item.Name in ZEROPOS_ITEMS:
                            _debug("Adding")
                        else:
                            _debug("Phantom item detected, skipping")
                            continue

                    contents.append(item)
                    _debug("Added {0}".format(item.Name))

                # Perform one _last_ check on journal to make sure there
                # were no innocent or criminal messages - getting someone 
                # killed because they flagged is REALLY bad. I hate to wait
                # yet more time - but this is the stuff which kills people.
                Misc.Pause(500)

                # Wait for disabled corpse messages
                if Journal.Search("disabled opening innocent corpses"):
                    _debug ("Innocent warning detected, returning")
                    self.IsInnocent = True
                    return []
                else:
                    _debug ("No innocent warning detected")
                
                # Wait for criminal act messages
                if Journal.Search("criminal act"):
                    _debug ("Criminal act warning detected")
                    self.IsCriminal = True
                else:
                    _debug ("No criminal warning detected")

                return contents

            else:

                _debug("Corpse invalid, returning")

                return []

        except Exception as e:

            _debug(
                "Caught exception in LootForm.InventoryContainer : {0}".format(
                    str(e)))
            raise

        finally:

            _debug("LootForm.InventoryContainer.exit") 
            
    ##########
    # Performs a range check on the current corpse, and, if valid, loads the contents
    # into the data bound table. Contents of corpses are sorted by importance, using
    # settings manager.
    #
    def LoadCorpse(self):

        _debug("LootForm.LoadCorpse.start")

        if not MUTEX.WaitOne(TimeSpan.Zero):
            return

        try:

            # reset corpse flags and clear contents
            self.IsInnocent = False
            self.IsCriminal = False
            self.Loaded = False
            self.HasBag = False
            self.Contents = []
            
            # clear data table
            self.DT.Clear()

            # clear status
            self.lblStatus.Text = ""
            
            # run a quick range check
            self.RangeCheckCorpse()

            # if corpse still valid
            if self.Corpse != None:
                
                # get contents
                contents = self.InventoryContainer(self.Corpse)
                
                # IsInnocent flags return immediately
                if self.IsInnocent:
                    return

                # sort contents and detect bags
                sorted_contents = []
                for item in contents:

                    # preferred items appear at top
                    if self.SM.IsAlwaysLoot(item.ItemID):
                        sorted_contents.insert(0, item)
                    else:
                        sorted_contents.append(item)
                        
                    self.HasBag += item.IsContainer

                # load data table with contents
                self.LoadDataTable(sorted_contents)

                # refresh data grid view
                self.DataGrid.Refresh()
                
                # set loaded flag
                self.Loaded = True

        except Exception as ex:

            _debug("Caught exception in LootForm.LoadCorpse : {0}".format(ex))
            raise

        finally:

            MUTEX.ReleaseMutex()
            _debug("LootForm.LoadCorpse.exit")

    ##########
    # Performs a range check on current corpse handle, and if it is not in range, invalidates it
    # by setting class variable Corpse to None.
    #
    def RangeCheckCorpse(self):

        _debug("LootForm.RangeCheckCorpse.start")

        try:

            if self.Corpse != None:

                # check coordinates
                for coord in self.GetLootCoords():
                    if self.Corpse.Position.X == coord[0] and self.Corpse.Position.Y == coord[1]:
                        _debug("Corpse in range")
                        return True

            # invalidate handle
            _debug("corpse out of range")
            self.Corpse = None
            return False

        except Exception as ex:

            _debug("Caught exception in LootForm.RangeCheckCorpse: {0}".format(
                ex))
            raise

        finally:
            _debug("LootForm.RangeCheckCorpse.exit")

    ##########
    # Accepts a list of Items contained within a corpse and loads the class
    # data table instance.
    #
    # Data Table Structure:
    # =====================
    # Column 0 = bool (loot bool)
    # Column 1 = object (Item)
    # Column 2 = string (name)
    # Column 3 = bool (preference bool)
    #
    def LoadDataTable(self, contents):

        _debug("LootForm.LoadDataTable.start")

        try:
            self.DT.Clear()
            if contents == []:
                _debug("Corpse empty, nothing to load")
            else:
                _debug("Loading {0} items into table".format(len(contents)))
                for item in contents:
                    if item.Amount > 1:
                        self.DT.Rows.Add(item, self.SM.IsAlwaysLoot(
                            item.ItemID), "{0} ({1})".format(
                                self.Sanitize(item.Name), item.Amount),
                                         self.SM.IsAlwaysLoot(item.ItemID))
                    else:
                        self.DT.Rows.Add(item, self.SM.IsAlwaysLoot(
                            item.ItemID), "{0}".format(
                                self.Sanitize(item.Name)),
                                         self.SM.IsAlwaysLoot(item.ItemID))
            _debug(self.DT.Rows.ToString())
        except Exception as e:
            _debug("Caught exception in LootForm.LoadDataTable : {0}".format(
                str(e)))
            raise
        finally:
            _debug("LootForm.LoadDataTable.exit")

    ##########
    # Function which decides to show or hide form and/or controls based on various states
    # and takes care of all user interface updates. Can be called any time.
    #
    def UpdateViewState(self):

        _debug("LootForm.UpdateViewState.start")

        try:

            # Close and Pick are always available
            self.btnClose.Visible = True
            self.btnPick.Visible = True
            self.lblStatus.Text = ""

            # If user is not viewing a corpse, the form is hidden
            if self.Corpse == None:
                self.Visible = False
                self.ShowInTaskBar = False
                self.Opacity = 0
            else:
                self.Visible = True
                self.ShowInTaskBar = True
                self.Opacity = 100

            if self.Corpse != None:

                # If corpse didn`t load need to detect why
                if self.Loaded == False:

                        # hide all the corpse controls
                        self.DataGrid.Visible = False
                        self.btnGet.Visible = False
                        self.btnCut.Visible = False
                        self.lblWeight.Visible = False

                        # If player got innocent warning
                        if self.IsInnocent == True:                
                            self.lblMsg.Visible = True
                            self.lblMsg.Text = MSG_INNOCENT

                        # if player hidden, show warning
                        elif not Player.Visible:
                            self.btnOpen.Visible = True
                            self.lblMsg.Text = MSG_HIDDEN
                            self.lblMsg.Visible = True

                # Corpse was loaded
                else:
                        
                    self.btnCut.Visible = True
                    self.lblWeight.Visible = True
                    self.btnOpen.Visible = False
                    self.lblStatus.Visible = True

                    # If corpse was empty
                    if self.DT.Rows.Count == 0:
                        self.DataGrid.Visible = False
                        self.btnGet.Visible = False
                        self.lblMsg.Visible = True
                        self.lblMsg.Text = MSG_EMPTY

                    # Corpse was not empty
                    else:
                        self.DataGrid.Visible = True
                        self.btnGet.Visible = True
                        self.lblMsg.Visible = False
                        self.lblMsg.Text = ""
                        self.UpdateDataGrid()

                        self.btnBag.Visible = self.HasBag

                    # If player got criminal warning
                    if self.IsCriminal == True:     
                        self.lblStatus.Text = "CRIMINAL ACT"
                        self.lblStatus.ForeColor = Color.Red
                        self.lblStatus.BackColor = Color.Transparent           
                    else:
                        self.lblStatus.ForeColor = Color.White
                        self.lblStatus.BackColor = Color.Transparent   
                        
            if self.Visible:
                self.Activate()

        except Exception as ex:

            _debug("Caught exception in LootForm.UpdateViewState : {0}".format(
                ex))
            raise

        finally:

            _debug("LootForm.UpdateViewState.exit")

    ##########
    # Displays player weight and colors text based on load
    #
    def UpdateWeight(self):

        _debug("LootForm.UpdateWeight.start")
        # resolve player weight color and message

        self.lblWeight.Text = "{0}/{1}".format(Player.Weight, Player.MaxWeight)
        if Player.Weight > Player.MaxWeight:
            self.lblWeight.ForeColor = Color.Red
        elif Player.Weight + 20 >= Player.MaxWeight:
            self.lblWeight.ForeColor = Color.Orange
        elif Player.Weight + 50 >= Player.MaxWeight:
            self.lblWeight.ForeColor = Color.Yellow
        else:
            self.lblWeight.ForeColor = Color.Green

        _debug("LootForm.UpdateWeight.exit")

    ##########
    # Resizes the datagrid columns, sets sorting policy and recolors cells
    # based on content. Call after DataGrid has been loaded from DataTable
    # and is ready to display content to Player.
    #
    # Row color is cosmetic only and is not stored in the data table.
    #
    def UpdateDataGrid(self):

        if self.DataGrid.ColumnCount > 1:
            self.DataGrid.Columns[0].Width = -1
            self.DataGrid.Columns[0].Visible = False
            self.DataGrid.Columns[1].Width = 30
            self.DataGrid.Columns[
                2].AutoSizeMode = DataGridViewAutoSizeColumnMode.Fill
            self.DataGrid.Columns[3].Width = 25

        for column in self.DataGrid.Columns:
            column.SortMode = DataGridViewColumnSortMode.NotSortable

        for i in range(self.DataGrid.RowCount):
            self.DataGrid.Rows[i].Cells[2].ReadOnly = True

        for i in range(self.DT.Rows.Count):

            _debug("Row : {0} | {1} | {2}".format(
                self.DT.Rows[i][1], self.DT.Rows[i][2], self.DT.Rows[i][3]))

            if self.DT.Rows[i][1] == True:
                self.DataGrid.Rows[i].Cells[2].Style.BackColor = Color.SaddleBrown
                self.DataGrid.Rows[i].Cells[2].Style.ForeColor = Color.White
            else:
                self.DataGrid.Rows[i].Cells[2].Style.BackColor = Color.Black
                self.DataGrid.Rows[i].Cells[2].Style.ForeColor = Color.White

        self.DataGrid.Refresh()

    ##########
    # Converts game item strings to friendly strings. Sometimes game item strings
    # have control codes, which we need to filter out. Game control substrings
    # seem inconsistent at times, so just doing a best effort below.
    #
    def Sanitize(self, str):

        _debug("LootForm.Sanitize.start")
        _debug("raw string : '{0}'".format(str))

        try:

            # remove the item id
            matches = re.search('(.*)\\(', str)
            if matches:
                str = matches.group(1)

            # remove percents
            str = str.replace('%', '')

            # get rid of slash+character
            matches = re.findall('\/\w', str)
            for match in matches:
                str = str.replace(match, '')

            # remove whitespace
            str = str.strip()

            # check word updates dictionary
            for word in WORD_FIXES:
                matches = re.search(word, str, re.I)
                if matches:
                    str = str.replace(matches.group(0), WORD_FIXES[word])

            _debug("new string : '{0}'".format(str))
            return str.strip().lower()

        except Exception as e:

            _debug("Caught exception in LootForm.Sanitize : {0}".format(
                str(e)))

        finally:

            _debug("LootForm.Sanitize.exit")

    ##########
    # Utility function which returns the bag the user selected to contain loot,
    # or just the Player backpack if said bag was not set or not found
    #
    def GetLootBag(self):

        _debug("LootForm.GetLootBag.start")
        try:
            # see if Player set loot pack
            if self.LootBag != None:
                for item in Player.Backpack.Contains:
                    if item.Serial == self.LootBag:
                        return item

                Misc.SendMessage("Cannot find loot container, using Backpack",
                                 COLOR_WARN)
            return Player.Backpack

        except Exception as e:

            _debug("Caught exception in LootForm.GetLootBag: {0}".format(
                str(e)))
            raise

        finally:

            _debug("LootForm.GetLootBag.exit")

    ##########
    # Attempts to loot an item, placing in user selected bag if set.
    #
    # Cannot determine 100% that an item was moved, since API does not return success.
    # The solution I came up with was to check the item position before the move attempt,
    # then check it after the move attempt. If they are different = moved, if same = not moved.
    #
    # This function is intentionally simple - there are too many variables to consider when it comes
    # to looting an item : player moved, player overweight, item out of sight, someone else took it,
    # server lag, and the list goes on...
    #
    # If an item is missing, function will return True
    #
    # Looting notes : Item.Visible does not guarantee that the game agrees an item is in sight. 
    #                 (Example: terrain difference will result in out of sight messages)
    #
    # DEBUG UPDATE : When an item is stacked, it will report the _same_ XYZ position it had
    #                BEFORE the move attempt. Items that are _not stacked_ will correctly
    #                report the XYZ position change between a corpse and a player backpack.
    #                In order to find out of stacked items moved, we can try to find their serial,
    #                and if that is missing, then we can assume it was stacked.
    #
    def GetItem(self, item):

        _debug("LootForm.GetItem.start ({0}-{1}".format(
            item.Name, item.Serial))
        _success = False
        try:
            assert item != None and item.Serial > -1, "A valid item was passed to function"
            
            # range check corpse
            if self.RangeCheckCorpse() == False:
               _debug("Corpse is no longer in range")
               return False
            
            # get starting position of item
            posStart = self.GetItemPosition(item)
            if posStart == None:
                _debug(
                    "Item start position is invalid, assuming it was removed")
                return True
               
            # request a item move without incurring a wait from the server
            while True:
                
                Journal.Clear()

                # request move
                Items.Move(item, self.GetLootBag(), 0)
                Misc.Pause(100)

                if Journal.Search("must wait"):
                    _debug("Received journal wait message after move request")
                    Misc.Pause(100)
                    continue
                else:
                    break

            # loop for 3 seconds waiting for item location to shift
            for x in range(1, 31):

                # use Thread.Sleep here not Misc.Pause
                Sleep(100)

                # stackable items bug workaround
                search = Items.FindBySerial(item.Serial)
                if search == None:
                    _debug(
                        "Unable to locate item by Serial, must have been stacked"
                    )
                    return True

                # get final position to see if loot changed
                posFinish = self.GetItemPosition(item)

                # check results
                if posFinish == None:
                    _debug("posFinish = None. Move successful")
                    return True
                elif (posStart.X != posFinish.X or posStart.Y != posFinish.Y
                      or posStart.Z != posFinish.Z):
                    _debug("Move successful")
                    return True

            _debug("Move failed")
            return False

        except Exception as e:

            _debug("Caught exception in LootForm.GetItem : {0}".format(str(e)))
            return False

        finally:

            _debug("LootForm.GetItem.exit")

    ##########
    # Wrapper for item.Position call which handles exceptions
    #
    def GetItemPosition(self, item):

        _debug("LootForm.GetItemPosition.start")
        itemPOS = None
        try:
            assert item != None, "Item is not None"
            itemPOS = item.Position
        except Exception as e:
            _debug("Caught exception in LootForm.GetItemPosition : {0}".format(
                str(e)))
        finally:
            _debug("Item position is {0}".format(itemPOS))
            _debug("LootForm.GetItemPosition.exit")
            return itemPOS

    ##########
    # Iterates the current inventory the player is viewing and saves loot
    # preferences. This should be called any time player makes a change
    # to a loot preference (aka = Always).
    #
    def SaveUserData(self):

        _debug("LootForm.SaveUserData.start")

        try:

            for row in self.DT.Rows:
                self.SetAlwaysLoot(row[0].ItemID, row[3])

            self.UpdateViewState()

        except Exception as e:

            _debug("Caught exception in LootForm.SaveUserData : {0}".format(
                str(e)))

        finally:

            _debug("LootForm.SaveUserData.exit")

    ##########
    # Special function for retreiving an item when user clicks on it in a cell.
    #
    def GetSingleItem(self, row):

        _debug("LootForm.GetSingleItem.start")

        try:

            if Player.Weight > Player.MaxWeight:
                self.lblStatus.Text = "You are overweight!"
                return

            _debug("Retrieving {0}".format(self.DT.Rows[row][2]))
            if self.GetItem(self.DT.Rows[row][0]):
                self.lblStatus.Text = "{0}".format(self.DT.Rows[row][2])
                self.DT.Rows[row].Delete()
                self.DataGrid.Refresh()
            else:
                self.lblStatus.Text = "Unable to loot item"
                _debug("Failed")
            return

        except Exception as e:

            _debug("Caught exception in LootForm.GetSingleItem: {0}".format(
                str(e)))

        finally:

            _debug("LootForm.GetSingleItem.exit")

    #######################
    # FORM EVENT HANDLERS #
    #######################


    ##########
    # Event handler which cancels the user selection on a row and prevents
    # row highlights, which is default behavior for a grid control.
    #
    def SelectionChanged(self, sender, args):

        try:

            self.DataGrid.ClearSelection()

        except Exception as e:

            _debug(
                "Caught exception in LootForm.SelectionChanged : {0}".format(
                    str(e)))

    ##########
    # Event handler for cell clicks, where certain rules are enforced about selection behavior between
    # check boxes.
    #
    def CellClick(self, sender, args):

        try:
            _debug("LootForm.CellClick.start {0}.{1}".format(
                args.RowIndex, args.ColumnIndex))

            # Always column
            if (args.ColumnIndex == 3 and args.RowIndex >= 0):
                self.DataGrid.CommitEdit(DataGridViewDataErrorContexts.Commit)

                # if Always was enabled, also enable the corresponding Loot option
                if (self.DataGrid.Rows[args.RowIndex].Cells[3].Value == True):
                    self.DT.Rows[args.RowIndex][1] = True

                    # and then look through list for all other items which match the Always row and enable those too
                    for i in range(self.DT.Rows.Count):
                        if self.DT.Rows[i][0].Name == self.DT.Rows[
                                args.RowIndex][0].Name:
                            self.DT.Rows[i][1] = True

                self.SaveUserData()
                self.DataGrid.CurrentCell = None
                self.UpdateDataGrid()

            # item Loot option, make sure Always is unchecked if Loot is false
            elif (args.ColumnIndex == 1 and args.RowIndex >= 0):
                self.DataGrid.CommitEdit(DataGridViewDataErrorContexts.Commit)

                # if Loot was disabled
                if (self.DataGrid.Rows[args.RowIndex].Cells[1].Value == False):
                    self.DT.Rows[args.RowIndex][3] = False

                self.DataGrid.CurrentCell = None
                self.UpdateDataGrid()

            # Loot column header : which enables/disables all Loot options in column
            elif (args.ColumnIndex == 1 and args.RowIndex == -1):
                self.DataGrid.CommitEdit(DataGridViewDataErrorContexts.Commit)

                TrueCount = 0

                for row in self.DT.Rows:
                    if row[1] == True:
                        TrueCount += 1

                NewVal = True
                if TrueCount == self.DT.Rows.Count:
                    NewVal = False

                _debug(NewVal)

                for row in self.DT.Rows:
                    row[1] = NewVal

                self.DataGrid.CurrentCell = None
                self.UpdateDataGrid()

            # Item clicked; retrieve it
            elif (args.ColumnIndex == 2 and args.RowIndex > -1):
                self.GetSingleItem(args.RowIndex)

        except Exception as e:

            _debug("Caught exception in LootForm.CellClick : {0}".format(
                str(e)))

        finally:

            _debug("LootForm.CellClick.exit")

    ##########
    # Event handler for clicking on the skull picture, which is a refresh
    #
    def picSkullPressed(self, sender, args):

        _debug("LootForm.picSkullPressed.start")
        if not MUTEX.WaitOne(TimeSpan.Zero):
            return

        try:

            self.LoadCorpse()
            self.lblStatus.Text = "Contents refreshed"
            self.UpdateViewState()

        except Exception as e:

            _debug("Caught exception in LootForm.picSkullPressed : {0}".format(
                str(e)))

        finally:

            MUTEX.ReleaseMutex()
            _debug("LootForm.picSkullPressed.exit")

    ##########
    # Event handler for user mousing over data grid cells
    #
    def Form_DataGrid_MouseEnter(self, sender, args):

        try:

            if args.ColumnIndex == 1 and args.RowIndex == -1:
                self.DataGrid.Cursor = Cursors.Hand
            elif args.ColumnIndex == 2 and args.RowIndex > -1:
                self.DataGrid.Cursor = Cursors.Hand
            else:
                self.DataGrid.Cursor = Cursors.Default

            self.DataGrid.Refresh()

        except Exception as e:
            _debug("Caught exception in Form_DataGrid_MouseEnter : {0}".format(
                str(e)))

    ##########
    # Event handler for user pressing mouse down on form
    #
    def Form_MouseDown(self, sender, args):

        self.isMouseDown = True
        self.lastLocation = args.Location

    ##########
    # Event handler for user pressing mouse up on form
    #
    def Form_MouseUp(self, sender, args):

        self.isMouseDown = False

    ##########
    # Event handler for user trying to move form with a mouse click. This is a borderless
    # form which, by default, has no title bar to move it with. To compensate, we allow user
    # to drag form by clicking and holding mouse anywhere in form.
    #
    def Form_MouseMove(self, sender, e):

        try:
            if self.isMouseDown:

                self.Location = Point(
                    (self.Location.X - self.lastLocation.X) + e.X,
                    (self.Location.Y - self.lastLocation.Y) + e.Y)
                self.Update()

        except Exception as e:
            _debug("Caught exception in LootForm.Form_MouseMove : {0}".format(
                str(e)))

    def Form_Cut_GotFocus(self, sender, e):
        self.btnCut.NotifyDefault(False)

    def Form_Cut_MouseEnter(self, sender, e):
        self.btnCut.BackColor = Color.Silver

    def Form_Cut_MouseLeave(self, sender, e):
        self.btnCut.BackColor = Color.Transparent

    def Form_Get_GotFocus(self, sender, e):
        self.btnGet.NotifyDefault(False)

    def Form_Get_MouseEnter(self, sender, e):
        self.btnGet.BackColor = Color.Silver

    def Form_Get_MouseLeave(self, sender, e):
        self.btnGet.BackColor = Color.Transparent

    def Form_Pick_GotFocus(self, sender, e):
        self.btnPick.NotifyDefault(False)

    def Form_Pick_MouseEnter(self, sender, e):
        self.btnPick.BackColor = Color.Silver

    def Form_Pick_MouseLeave(self, sender, e):
        self.btnPick.BackColor = Color.Transparent

    def Form_Open_GotFocus(self, sender, e):
        self.btnOpen.NotifyDefault(False)

    def Form_Open_MouseEnter(self, sender, e):
        self.btnOpen.BackColor = Color.Silver

    def Form_Open_MouseLeave(self, sender, e):
        self.btnOpen.BackColor = Color.Transparent

    def Form_Close_GotFocus(self, sender, e):
        self.btnClose.NotifyDefault(False)

    def Form_Close_MouseEnter(self, sender, e):
        self.btnClose.BackColor = Color.Silver

    def Form_Close_MouseLeave(self, sender, e):
        self.btnClose.BackColor = Color.Transparent

    def Form_Bag_GotFocus(self, sender, e):
        self.btnBag.NotifyDefault(False)

    def Form_Bag_MouseEnter(self, sender, e):
        self.btnBag.BackColor = Color.Silver

    def Form_Bag_MouseLeave(self, sender, e):
        self.btnBag.BackColor = Color.Transparent

    def Form_Skull_MouseEnter(self, sender, e):
        self.picSkull.Image = LOADED_IMG_REDSKULL

    def Form_Skull_MouseLeave(self, sender, e):
        self.picSkull.Image = LOADED_IMG_SKULL
        
    def Form_FormClosing(self, sender, e):
        _debug("FormClosing")

    ##########
    # Event handler for user pressing Close on a corpse
    #
    def btnClosePressed(self, sender, args):

        _debug("LootForm.btnClosePressed.start")
        if not MUTEX.WaitOne(TimeSpan.Zero):
            return

        try:

            # ignore current corpse
            if self.Corpse is not None:
                self.CM.Ignore(self.Corpse)

            # flag current corpse instance invalid
            self.Corpse = None

            # refresh
            self.UpdateViewState()

        except Exception as e:

            _debug("Caught exception in LootForm.btnClosePressed : {0}".format(
                str(e)))
        finally:

            MUTEX.ReleaseMutex()
            _debug("LootForm.btnClosePressed.exit")

    ##########
    # Event handler for user pressing Pick icon
    #
    def btnPickPressed(self, sender, args):

        _debug("LootForm.btnPickPressed.start")

        try:

            Items.UseItem(Player.Backpack.Serial)
            Target.ClearQueue()
            Misc.Pause(500)
            Misc.SendMessage("Please select container to hold loot",
                             COLOR_NORMAL)
            # saves serial # of selected item
            self.LootBag = Target.PromptTarget()
            if self.LootBag < -1:
                self.LootBag = None
            else:
                self.lblStatus.Text = "Container set"

        except Exception as e:

            _debug("Caught exception in LootForm.btnPickPressed : {0}".format(
                str(e)))

        finally:

            _debug("LootForm.btnPickPressed.exit")

    ##########
    # Event handler for user pressing the Get button, which will retrieve
    # all selected items from the corpse and close the window.
    #
    # When looting a list of items, the first fail attempt will abort
    # further attempts and return a message to the player. 
    #
    # 1.6.1 - implements visibility check.
    # 
    def btnGetPressed(self, sender, args):

        _debug("LootForm.btnGetPressed.start")
        if not MUTEX.WaitOne(TimeSpan.Zero):
            return

        try:
            
            # range check
            if not self.RangeCheckCorpse():
                self.Visible = False
                return

            # update always loot settings
            for row in self.DT.Rows:
                self.SM.SetAlwaysLoot(row[0].ItemID, row[3])

            if Player.Weight > Player.MaxWeight:
                self.lblStatus.Text = "You are overweight!"
                return

            # iterate rows
            i = 0
            while i < self.DT.Rows.Count:
                if self.DT.Rows[i][1]:
                    _debug("Retrieving {0}".format(self.DT.Rows[i][2]))
                    if self.GetItem(self.DT.Rows[i][0]):
                        self.lblStatus.Text = "{0}".format(self.DT.Rows[i][2])
                        self.DT.Rows[i].Delete()
                        self.DataGrid.Refresh()
                        self.lblStatus.Refresh()
                    else:
                        _debug("Failed")
                        self.lblStatus.Text = "Unable to loot item"
                        return
                else:
                    i += 1

                Misc.Pause(LOOT_WAIT)

            # set current corpse to ignore
            self.CM.Ignore(self.Corpse)
            
            # invalidate handle
            self.Corpse = None

            # clear class variables
            self.IsInnocent = False
            self.IsCriminal = False
            self.Loaded = False
            self.HasBag = False
            self.Contents = []
            
            # clear data table
            self.DT.Clear()
            
            # refresh view state
            self.UpdateViewState()

        except Exception as e:

            _debug("Caught exception in LootForm.btnGetPressed : {0}".format(
                str(e)))

        finally:

            MUTEX.ReleaseMutex()
            _debug("LootForm.btnGetPressed.exit")

    ##########
    # Event handler for user pressing the Open button.
    #
    def btnOpenPressed(self, sender, args):

        _debug("LootForm.btnOpenPressed.start")
        if not MUTEX.WaitOne(TimeSpan.Zero):
            return

        try:

            self.LoadCorpse()
            self.UpdateViewState()

        except Exception as e:

            _debug("Caught exception in LootForm.btnOpenPressed : {0}".format(
                str(e)))

        finally:

            MUTEX.ReleaseMutex()
            _debug("LootForm.btnOpenPressed.exit")

    ##########
    # Event handler for user pressing button to cut a corpse.
    #
    def btnCutPressed(self, sender, args):

        _debug("LootForm.btnCutPressed.start")
        if not MUTEX.WaitOne(TimeSpan.Zero):
            return

        try:

            # range check
            if not self.RangeCheckCorpse():
                self.Visible = False
                return

            # check blades in pack
            for blade in blades:
                if Items.BackpackCount(blade, -1) > 0:
                    Items.UseItemByID(blade, -1)
                    Target.WaitForTarget(5000)
                    Target.TargetExecute(self.Corpse)
                    Misc.Pause(1000)
                    self.LoadCorpse()
                    self.UpdateViewState()
                    return

            # combine all weps
            weps = blades + axes

            # try whatever player is holding
            RH = Player.GetItemOnLayer("RightHand")
            for wep in weps:
                if RH is not None and RH.ItemID in weps:
                    Items.UseItemByID(RH.ItemID, -1)
                    Target.WaitForTarget(5000)
                    Target.TargetExecute(self.Corpse)
                    Misc.Pause(1000)
                    self.LoadCorpse()
                    self.UpdateViewState()
                    return

            Misc.SendMessage("No cutting weapons found")

        except Exception as e:

            _debug("Caught exception in LootForm.btnCutPressed : {0}".format(
                str(e)))

        finally:

            MUTEX.ReleaseMutex()
            _debug("LootForm.btnCutPressed.exit")

    ##########
    # Event handler for user pressing button to open all containers
    #
    def btnBagPressed(self, sender, args):

        _debug("LootForm.btnBagPressed.start")
        if not MUTEX.WaitOne(TimeSpan.Zero):
            return

        try:

            self.RangeCheckCorpse()

            if self.Corpse == None:
                return

            self.HasBag = False

            # iterate in reverse order
            for i in reversed(range(self.DT.Rows.Count)):
                if self.DT.Rows[i][0].IsContainer:
                    contents = self.InventoryContainer(self.DT.Rows[i][0])
                    self.DT.Rows[i].Delete()
                    if contents == []:
                        _debug("Bag empty, nothing to load")
                    else:
                        _debug("Loading {0} items into table".format(
                            len(contents)))
                        for item in contents:
                            self.DT.Rows.Add(item,
                                             self.SM.IsAlwaysLoot(item.ItemID),
                                             self.Sanitize(item.Name),
                                             self.SM.IsAlwaysLoot(item.ItemID))
                            self.HasBag += item.IsContainer

            self.UpdateViewState()

        except Exception as e:

            _debug("Caught exception in LootForm.btnBagPressed : {0}".format(
                str(e)))

        finally:

            MUTEX.ReleaseMutex()
            _debug("LootForm.btnBagPressed.exit")

# clean out the old debug log debug
File.Delete(FILE_DEBUG)
_debug("Script.Start")

# Auto-start delay for UO Razor Enhanced.
Misc.Pause(2000)
Misc.SendMessage("Starting ~Enhanced Loot~ script", COLOR_NORMAL)
 
try:
    try:
        
        LOADED_IMG_SKULL = Image_From_File(IMG_SKULL)
        LOADED_IMG_REDSKULL = Image_From_File(IMG_REDSKULL)
        form = LootForm()
        Application.Run(form)
        
    except Exception as ex:
        _debug("Caught Exception in Script : {0}".format(str(ex)))

    finally:

        form._worker.CancelAsync()
        form.Close()
        _debug("Script.Stop")
        
except Exception as e:
    _debug("Caught outer Exception in Script : {0}".format(str(ex)))
    
    
