class MasterSingleton:
    AutoLoot = None
    BandageHeal = None
    BuyAgent = None
    DPSMeter = None
    Dress = None
    Friend = None
    Items = None
    Journal = None
    Misc = None
    Mobiles = None
    Organizer = None
    PathFinding = None
    Player = None
    Restock = None
    Scavenger = None
    SellAgent = None
    Spells = None
    Statics = None
    Target = None
    Timer = None
    classesPopulated = False

    def __init__ ( self ):
        pass

    def PopulateClasses( self, AutoLoot, BandageHeal, BuyAgent, DPSMeter, Dress, Friend,
            Items, Journal, Misc, Mobiles, Organizer, PathFinding, Player, Restock,
            Scavenger, SellAgent, Spells, Statics, Target, Timer ):
        self.AutoLoot = AutoLoot
        self.BandageHeal = BandageHeal
        self.BuyAgent = BuyAgent
        self.DPSMeter = DPSMeter
        self.Dress = Dress
        self.Friend = Friend
        self.Items = Items
        self.Journal = Journal
        self.Misc = Misc
        self.Mobiles = Mobiles
        self.Organizer = Organizer
        self.PathFinding = PathFinding
        self.Player = Player
        self.Restock = Restock
        self.Scavenger = Scavenger
        self.SellAgent = SellAgent
        self.Spells = Spells
        self.Statics = Statics
        self.Target = Target
        self.Timer = Timer
        classesPopulated = True
