import enum as enum

class Platform(str, enum.Enum):
    visium = "visium"
    xenium = "xenium"
    cosmx = "cosmx"

    def __str__(self):
        return self.value