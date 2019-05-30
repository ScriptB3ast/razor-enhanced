class Craftable:
    name = None
    minSkill = None
    resourcesNeeded = None
    gumpPath = None

    def __init__ ( self, name, minSkill, resourcesNeeded, gumpPath ):
        self.name = name
        self.minSkill = minSkill
        self.resourcesNeeded = resourcesNeeded
        self.gumpPath = gumpPath
