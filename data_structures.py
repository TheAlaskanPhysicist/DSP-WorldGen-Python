from enums import *

class Vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return f"Vec3({self.x}, {self.y}, {self.z})"


class PlanetData:
    def __init__(self):
        self.cluster: "ClusterData" = None
        self.star: "StarData" = None
        self.seed: int = None
        self.info_seed: int = None
        self.id: int = None
        self.index: int = None
        self.orbit_around: int = None
        self.number: int = None
        self.orbit_index: int = None
        self.name: str = ''
        self.override_name: str = ''
        self.orbit_radius: float = 1.0
        self.orbit_inclination: float = None
        self.orbit_longitude: float = None
        self.orbital_period: float = 3600.0
        self.orbit_phase: float = None
        self.obliquity: float = None
        self.rotation_period: float = 480.0
        self.rotation_phase: float = None
        self.radius: float = 200.0
        self.scale: float = 1.0
        self.sun_distance: float = None
        self.habitable_bias: float = None
        self.temperature_bias: float = None
        self.ion_height: float = None
        self.wind_strength: float = None
        self.luminosity: float = None
        self.land_percent: float = None
        self.mod_x: float = None
        self.mod_y: float = None
        self.water_height: float = None
        self.water_item_id: int = None
        self.levelized: bool = None
        self.ice_flag: int = None
        self.type: EPlanetType = None
        self.singularity: EPlanetSingularity = EPlanetSingularity(0)
        self.theme: int = None
        self.style: int = None
        self.orbit_around_planet: "PlanetData" = None

    @property
    def display_name(self) -> str:
        if self.override_name:
            return self.override_name
        return self.name

    @property
    def real_radius(self) -> float:
        return self.radius * self.scale


class StarData:
    def __init__(self):
        self.cluster: "ClusterData" = None
        self.seed: int = None
        self.index: int = None
        self.id: int = None
        self.name: str = ''
        self.overrideName: str = ''
        self.position: Vec3 = Vec3(0, 0, 0)
        self.uPosition: Vec3 = None
        self.mass: float = 1.0
        self.lifetime: float = 50.0
        self.age: float = None
        self.type: EStarType = None
        self.temperature: float = 8500.0
        self.spectr: ESpectrType = None
        self.class_factor: float = None
        self.color: float = None
        self.luminosity: float = 1.0
        self.radius: float = 1.0
        self.acdisk_radius: float = None
        self.habitable_radius: float = 1.0
        self.light_balance_radius: float = 1.0
        self.dyson_radius: float = 10.0
        self.orbit_scaler: float = 1.0
        self.planet_count: int = None
        self.level: float = None
        self.resource_coef: float = 1.0
        self.planets: list["PlanetData"] = []
        self.PHYSICS_RADIUS_RATIO: float = 1200.0
        self.VIEW_RADIUS_RATIO: float = 800.0

    # If you want to calculate resources later, add it here and PlanetData

    @property
    def display_name(self) -> str:
        if self.overrideName:
            return self.overrideName
        return self.name

    @property
    def dyson_luminosity(self) -> float:
        return round(pow(self.luminosity, 0.33000001311302185) * 1000) / 1000

    @property
    def system_radius(self) -> float:
        sun_distance = self.dyson_radius
        if self.planet_count > 0:
            sun_distance = self.planets[self.planet_count - 1].sun_distance
        return sun_distance

    @property
    def physics_radius(self) -> float:
        return self.radius * self.PHYSICS_RADIUS_RATIO

    @property
    def view_radius(self) -> float:
        return self.radius * self.VIEW_RADIUS_RATIO


class ClusterData:
    def __init__(self):
        self.seed: int = 0
        self.star_count: int = 0
        self.stars: list[StarData] = []
        self.birth_planet_id: int = 0
        self.birth_star_id: int = 0
        self.habitable_count: int = 0
        self.AU: float = 40_000.0
        self.LY: float = 2_400_000.0

    def star_by_id(self, star_id: int) -> StarData | None:
        star_idx = star_id - 1
        if 0 <= star_idx < len(self.stars):
            return self.stars[star_idx]
        else:
            return None

    def planet_by_id(self, planet_id: int) -> PlanetData | None:
        star_idx   = planet_id // 100 - 1
        planet_idx = planet_id % 100 - 1
        if self.star_by_id(star_idx + 1) is None: return None
        if 0 <= planet_idx < len(self.stars[star_idx].planets):
            return self.stars[star_idx].planets[planet_idx]
        else:
            return None
