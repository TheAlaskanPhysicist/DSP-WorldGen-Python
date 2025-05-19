from enum import Enum, IntFlag


class EStarType(Enum):
    MainSeqStar = 0
    GiantStar = 1
    WhiteDwarf = 2
    NeutronStar = 3
    BlackHole = 4


class ESpectrType(Enum):
    M = 0
    K = 1
    G = 2
    F = 3
    A = 4
    B = 5
    O = 6
    X = 7

class EPlanetType(Enum):
    none = 0
    Volcano = 1
    Ocean = 2
    Desert = 3
    Ice = 4
    Gas = 5

class EPlanetSingularity(IntFlag):
    none = 0x0
    TidalLocked = 0x1
    TidalLocked2 = 0x2
    TidalLocked4 = 0x4
    LaySide = 0x8
    ClockwiseRotate = 0x10
    MultipleSatellites = 0x20