from dotNET import clamp, rand_normal, lerp
import math
from namegen import NameGen
from data_structures import *
from dotnet.rng import DotNet35Random


# Universal constants
GRAVITY: float = 1.3538551990520382E-06



class PlanetGenerator:
    def __init__(self):
        self.GRAVITATIONAL_CONSTANT: float = 346586930.95732176
        self.PLANET_MASS: float = 0.006
        self.GIANT_MASS_COEF: float = 3.33333
        self.GIANT_MASS: float = 0.019999979
        self.gasCoef: float = 1
        self.tmp_theme: list[int] = []
        self.ORBITAL_RADIUS = [0.0, 0.4, 0.7, 1.0, 1.4, 1.9, 2.5, 3.3, 4.3, 5.5, 6.9, 8.4, 10.0, 11.7, 13.5, 15.4, 17.5]

    def create_planet(self, cluster: "ClusterData", star: "StarData", theme_ids: list[int], index: int, orbit_around: int,
                      orbit_index: int, number: int, gas_giant: bool, info_seed: int, gen_seed: int) -> PlanetData:
        planet_data: PlanetData = PlanetData()
        dotnet_35_random: DotNet35Random = DotNet35Random(info_seed)
        planet_data.index = index
        planet_data.cluster = cluster
        planet_data.star = star
        planet_data.seed = gen_seed
        planet_data.info_seed = info_seed
        planet_data.orbit_around = orbit_around
        planet_data.orbit_index = orbit_index
        planet_data.number = number
        planet_data.id = star.id + index + 1
        stars = cluster.stars
        num = sum([star.planet_count for star in stars[:star.index]])
        num += index
        if orbit_around > 0:
            for j in range(star.planet_count):
                if orbit_around == star.planets[j].number and star.planets[j].orbit_around == 0:
                    planet_data.orbit_around_planet = star.planets[j]
                    if orbit_index > 1:
                        planet_data.orbit_around_planet.singularity |= EPlanetSingularity.MultipleSatellites
                    break
            assert planet_data.orbit_around_planet is not None
        text = None
        planet_data.name = "{} {}{}".format(star.name, (str(index + 1) if star.planet_count > 20 else NameGen.roman[index + 1]), "star")
        num2 = dotnet_35_random.next_double()
        num3 = dotnet_35_random.next_double()
        num4 = dotnet_35_random.next_double()
        num5 = dotnet_35_random.next_double()
        num6 = dotnet_35_random.next_double()
        num7 = dotnet_35_random.next_double()
        num8 = dotnet_35_random.next_double()
        num9 = dotnet_35_random.next_double()
        num10 = dotnet_35_random.next_double()
        num11 = dotnet_35_random.next_double()
        num12 = dotnet_35_random.next_double()
        num13 = dotnet_35_random.next_double()
        rand = dotnet_35_random.next_double()
        num14 = dotnet_35_random.next_double()
        rand2 = dotnet_35_random.next_double()
        rand3 = dotnet_35_random.next_double()
        rand4 = dotnet_35_random.next_double()
        theme_seed: int = dotnet_35_random.next()
        num15: float = pow(1.2, num2 * (num3 - 0.5) * 0.5)
        num16: float = 0.0
        if orbit_around == 0:
            num16 = self.ORBITAL_RADIUS[orbit_index] * star.orbit_scaler
            num17: float = (num15 - 1.0) / max(1.0, num16) + 1.0
            num16 *= num17
        else:
            num16 = float((1600 * orbit_index + 200) * pow(star.orbit_scaler, 0.3) * lerp(num15, 1.0, 0.5) + planet_data.orbit_around_planet.real_radius) / 40000.0
        planet_data.orbit_radius = num16
        planet_data.orbit_inclination = float(num4 * 16.0 - 8.0)
        if orbit_around > 0:
            planet_data.orbit_inclination *= 2.2
        planet_data.orbit_longitude = float(num5 * 360.0)
        if star.type == EStarType.NeutronStar or star.type == EStarType.BlackHole:
            if planet_data.orbit_inclination > 0:
                planet_data.orbit_inclination += 3.0
            else:
                planet_data.orbit_inclination -= 3.0
        if planet_data.orbit_around_planet is None:
            planet_data.orbital_period = math.sqrt(39.47841760435743 * num16 * num16 * num16 / (1.3538551990520382E-06 * star.mass))
        else:
            planet_data.orbital_period = math.sqrt(39.47841760435743 * num16 * num16 * num16 / 1.0830842106853677E-08)
        planet_data.orbit_phase = float(num6 * 360.0)
        if num14 < 0.03999999910593033:
            planet_data.obliquity = float(num7 * (num8 - 0.5) * 39.9)
            if planet_data.obliquity < 0.0:
                planet_data.obliquity -= 70.0
            else:
                planet_data.obliquity += 70.0
            planet_data.singularity |= EPlanetSingularity.LaySide
        elif num14 < 0.10000000149011612:
            planet_data.obliquity = float(num7 * (num8 - 0.5) * 80.0)
            if planet_data.obliquity < 0.0:
                planet_data.obliquity -= 30.0
            else:
                planet_data.obliquity += 30.0
        else:
            planet_data.obliquity = float(num7 * (num8 - 0.5) * 60.0)
        planet_data.rotation_period = float(num9 * 0.5 + 0.5) * float(num10 * 0.5 + 0.5) * float(num11 * 0.5 + 0.5) * float(num12 * 0.5 + 0.5) * float(num13 * 0.5 + 0.5) * float(rand2 * 0.5 + 0.5)
        if not gas_giant:
            if star.type == EStarType.WhiteDwarf:
                planet_data.rotation_period *= 0.5
            elif star.type == EStarType.NeutronStar:
                planet_data.rotation_period *= 0.20000000298023224
            elif star.type == EStarType.BlackHole:
                planet_data.rotation_period *= 0.15000000596046448
        planet_data.rotation_phase = float(num11 * 360.0)
        planet_data.sun_distance = planet_data.orbit_radius if orbit_around == 0 else planet_data.orbit_around_planet.orbit_radius
        planet_data.scale = 1.0
        num18: float = planet_data.orbital_period if orbit_around == 0 else planet_data.orbit_around_planet.orbital_period
        planet_data.rotation_period = 1.0 / (1.0 / num18 + 1.0 / planet_data.rotation_period)
        if orbit_around == 0 and orbit_index <= 4 and not gas_giant:
            if num14 > 0.9599999785423279:
                planet_data.obliquity *= 0.01
                planet_data.rotation_period = planet_data.orbital_period
                planet_data.singularity |= EPlanetSingularity.TidalLocked
            elif num14 > 0.9300000071525574:
                planet_data.obliquity *= 0.1
                planet_data.rotation_period = planet_data.orbital_period * 0.5
                planet_data.singularity |= EPlanetSingularity.TidalLocked2
            elif num14 > 0.8999999761581421:
                planet_data.obliquity *= 0.2
                planet_data.rotation_period = planet_data.orbital_period * 0.25
                planet_data.singularity |= EPlanetSingularity.TidalLocked4
        if 0.85 < num14 <= 0.9:
            planet_data.rotation_period = 0.0 - planet_data.rotation_period
            planet_data.singularity |= EPlanetSingularity.ClockwiseRotate
        habitable_radius = star.habitable_radius
        if gas_giant:
            planet_data.type = EPlanetType.Gas
            planet_data.radius = 80.0
            planet_data.scale = 10.0
            planet_data.habitable_bias = 100.0
        else:
            num19: float = math.ceil(float(star.cluster.star_count) * 0.29)
            if num19 < 11.0: num19 = 11.0
            num20: float = num19 - float(star.cluster.habitable_count)
            num21: float = float(star.cluster.star_count) - float(star.index)
            sun_distance: float = planet_data.sun_distance
            num22: float = 1000.0
            num23: float = 1000.0
            if habitable_radius > 0.0 and sun_distance > 0.0:
                num23 = sun_distance / habitable_radius
                num22 = math.fabs(math.log(num23))
            num24: float = clamp(math.sqrt(habitable_radius), 1.0, 2.0) - 0.04
            a: float = num20 / num21
            a = lerp(a, 0.35, 0.5)
            a = clamp(a, 0.08, 0.8)
            planet_data.habitable_bias = num22 * num24
            planet_data.temperature_bias = 1.2 / (num23 + 0.2) - 1.0
            f: float = clamp(planet_data.habitable_bias / a, 0, 1)
            p: float = a * 10.0
            f: float = pow(f, p)
            if (num12 > f and star.index > 0) or (planet_data.orbit_around > 0 and planet_data.orbit_index == 1 and star.index == 0):
                planet_data.type = EPlanetType.Ocean
                star.cluster.habitable_count += 1
            elif num23 < 0.833333:
                num25: float = max(0.15, num23 * 2.5 - 0.85)
                if num13 < num25:
                    planet_data.type = EPlanetType.Desert
                else:
                    planet_data.type = EPlanetType.Volcano
            elif num23 < 1.2:
                planet_data.type = EPlanetType.Desert
            else:
                num26: float = (0.9 / num23) - 0.1
                if num13 < num26:
                    planet_data.type = EPlanetType.Desert
                else:
                    planet_data.type = EPlanetType.Ice
            planet_data.radius = 200.0
        if planet_data.type != EPlanetType.Gas and planet_data.type != EPlanetType.none:
            planet_data.precision = 200
            planet_data.segment = 5
        else:
            planet_data.precision = 64
            planet_data.segment = 2
        planet_data.luminosity = pow(planet_data.star.light_balance_radius / (planet_data.sun_distance + 0.01), 0.6)
        if planet_data.luminosity > 1.0:
            planet_data.luminosity = math.log(planet_data.luminosity) + 1.0
            planet_data.luminosity = math.log(planet_data.luminosity) + 1.0
            planet_data.luminosity = math.log(planet_data.luminosity) + 1.0
        planet_data.luminosity = round(planet_data.luminosity * 100.0) / 100.0
        self.set_planet_theme(planet_data, theme_ids, rand, rand2, rand3, rand4, theme_seed)
        return planet_data

    def set_planet_theme(self, planet: PlanetData, theme_ids: list[int], rand1: float, rand2: float, rand3: float, rand4: float, theme_seed: int) -> None:
        pass

class StarGenerator:
    def __init__(self):
        self.ORBITAL_RADII: list[float] = [0.0, 0.4, 0.7, 1.0, 1.4, 1.9, 2.5, 3.3, 4.3, 5.5, 6.9, 8.4, 10.0, 11.7, 13.5, 15.4, 17.5]
        self.specify_birth_star_mass: float = 0.0
        self.specify_birth_star_age: float = 0.0
        self._p_gas: list[float] = [0.0] * 10

    def create_star(self, cluster: "ClusterData", pos: Vec3, id: int, seed: int,
                    need_type: EStarType, need_spectr: ESpectrType = ESpectrType.X) -> StarData:
        star_data: StarData = StarData()
        star_data.cluster = cluster
        star_data.index = id - 1
        if cluster.star_count > 1:
            star_data.level = float(star_data.index) / float(cluster.star_count - 1)
        else:
            star_data.level = 0.0
        star_data.id = id
        star_data.seed = seed
        dotnet_35_random: DotNet35Random = DotNet35Random(seed)
        seed2: int = dotnet_35_random.next()
        seed3: int = dotnet_35_random.next()
        star_data.position = pos
        num: float = math.sqrt(pos.x * pos.x + pos.y * pos.y + pos.z * pos.z)
        num2: float = num / 32.0
        if num2 > 1.0:
            for _ in range(5):
                num2 = math.log(num2) + 1.0
        star_data.resource_coef = math.pow(7.0, num2) * 0.6
        dotnet_35_random2: DotNet35Random = DotNet35Random(seed3)
        num3: float = dotnet_35_random2.next_double()
        num4: float = dotnet_35_random2.next_double()
        num5: float = dotnet_35_random2.next_double()
        rn: float = dotnet_35_random2.next_double()
        rt: float = dotnet_35_random2.next_double()
        num6: float = (dotnet_35_random2.next_double() - 0.5) * 0.2
        num7: float = dotnet_35_random2.next_double() * 0.2 + 0.9
        num8: float = dotnet_35_random2.next_double() * 0.4 - 0.2
        num9: float = math.pow(2.0, num8)
        dotnet_35_random3: DotNet35Random = DotNet35Random(dotnet_35_random2.next())
        num10: float = dotnet_35_random3.next_double()
        num11: float = lerp(-0.98, 0.88, star_data.level)
        num11 = (num11 + 0.65) if num11 >= 0 else (num11 - 0.65)
        standard_deviation: float = 0.33
        if need_type == EStarType.GiantStar:
            num11 = -1.5 if num8 > -0.08 else 1.6
            standard_deviation = 0.3
        num12: float = rand_normal(num11, standard_deviation, num3, num4)
        if need_spectr == ESpectrType.M:
            num12 = -3.0
        elif need_spectr == ESpectrType.O:
            num12 = 3.0
        num12 = num12 * 1 if num12 <= 0 else num12 * 2
        num12 = clamp(num12, -2.4, 4.65) + num6 + 1.0
        if need_type == EStarType.BlackHole:
            star_data.mass = 18.0 + num3 * num4 * 30.0
        elif need_type == EStarType.NeutronStar:
            star_data.mass = 7.0 + num3 * 11.0
        elif need_type == EStarType.WhiteDwarf:
            star_data.mass = 1.0 + num4 * 5.0
        else:
            star_data.mass = math.pow(2.0, num12)
        d: float = 5.0
        if star_data.mass < 2.0:
            d = 2.0 + 0.4 * (1.0 - star_data.mass)
        star_data.lifetime = float(10000.0 * math.pow(0.1, math.log(star_data.mass * 0.5) / math.log(d) + 1.0) * num7)
        if need_type == EStarType.GiantStar:
            star_data.lifetime = float(10000.0 * math.pow(0.1, math.log(star_data.mass * 0.58) / math.log(d) + 1.0) * num7)
            star_data.age = float(num5 * 0.04 + 0.96)
        elif need_type == EStarType.WhiteDwarf or need_type == EStarType.NeutronStar or need_type == EStarType.BlackHole:
            star_data.age = float(num5 * 0.4 + 1.0)
            if need_type == EStarType.WhiteDwarf:
                star_data.lifetime += 10000.0
            elif need_type == EStarType.NeutronStar:
                star_data.lifetime += 1000.0
        else:
            if star_data.mass < 0.5:
                star_data.age = float(num5 * 0.12 + 0.02)
            elif star_data.mass < 0.8:
                star_data.age = float(num5 * 0.4 + 0.1)
            else:
                star_data.age = float(num5 * 0.7 + 0.2)
        num13: float = star_data.lifetime * star_data.age
        if num13 > 5000.0:
            num13 = (math.log(num13 / 5000.0) + 1.0) * 5000.0
        if num13 > 8000.0:
            num13 = (math.log(math.log(math.log(num13 / 8000.0) + 1.0) + 1.0) + 1.0) * 8000.0
        star_data.lifetime = num13 / star_data.age
        num14: float = (1.0 - math.pow(clamp(star_data.age, 0.0, 1.0), 20.0) * 0.5) * star_data.mass
        star_data.temperature = float(math.pow(num14, 0.56 + 0.14 / (math.log(num14 + 4.0) / math.log(5.0))) * 4450.0 + 1300.0)
        num15: float = math.log((star_data.temperature - 1300.0) / 4500.0) / math.log(2.6) - 0.5
        if num15 < 0.0: num15 *= 4.0
        if num15 > 2.0: num15 = 2.0
        elif num15 < -4.0: num15 = -4.0
        star_data.spectr = ESpectrType(round(num15 + 4.0))
        star_data.color = clamp((num15 + 3.5) * 0.2, 0.0, 1.0)
        star_data.class_factor = num15
        star_data.luminosity = math.pow(num14, 0.7)
        star_data.radius = float(math.pow(star_data.mass, 0.4) * num9)
        star_data.acdisk_radius = 0.0
        p: float = num15 + 2.0
        star_data.habitable_radius = math.pow(1.7, p) + 0.25 * min(1.0, star_data.orbit_scaler)
        star_data.light_balance_radius = math.pow(1.7, p)
        star_data.orbit_scaler = math.pow(1.35, p)
        if star_data.orbit_scaler < 1.0:
            star_data.orbit_scaler = lerp(star_data.orbit_scaler, 1.0, 0.6)
        self.set_star_age(star_data, star_data.age, rn, rt)
        star_data.dyson_radius = star_data.orbit_scaler * 0.28
        if star_data.dyson_radius * 40000.0 < star_data.physics_radius * 1.5:
            star_data.dyson_radius = float(star_data.physics_radius * 1.5 / 40000.0)
        star_data.uPosition = Vec3(star_data.position.x * 2400000.0, star_data.position.y * 2400000.0, star_data.position.z * 2400000.0)
        star_data.name = NameGen.random_star_name(seed2, star_data, cluster)
        star_data.overrideName = ""
        return star_data

    def create_birth_star(self, cluster: "ClusterData", seed: int) -> StarData:
        star_data: StarData = StarData()
        star_data.cluster = cluster
        star_data.index = 0
        star_data.level = 0.0
        star_data.id = 1
        star_data.seed = seed
        star_data.resource_coef = 0.6
        dotnet_35_random = DotNet35Random(seed)
        seed2: int = dotnet_35_random.next()
        seed3: int = dotnet_35_random.next()
        star_data.name = NameGen.random_name(seed2)
        star_data.overrideName = ""
        star_data.position = Vec3(0, 0, 0)
        dotnet_35_random2 = DotNet35Random(seed3)
        r: float = dotnet_35_random2.next_double()
        r2: float = dotnet_35_random2.next_double()
        num: float = dotnet_35_random2.next_double()
        rn: float = dotnet_35_random2.next_double()
        rt: float = dotnet_35_random2.next_double()
        num2: float = dotnet_35_random2.next_double() * 0.2 + 0.9
        y: float = dotnet_35_random2.next_double() * 0.4 - 0.2
        num3: float = pow(2.0, y)
        dotnet_35_random3 = DotNet35Random(dotnet_35_random2.next())
        num4: float = dotnet_35_random3.next_double()
        value: float = rand_normal(0.0, 0.08, r, r2)
        value = clamp(value, -0.2, 0.2)
        star_data.mass = pow(2.0, value)
        if self.specify_birth_star_mass > 0.1: star_data.mass = self.specify_birth_star_mass
        if self.specify_birth_star_age > 1E-05: star_data.age = self.specify_birth_star_age
        num5: float = 5.0
        num5 = 2.0 + 0.4 * (1.0 - star_data.mass)
        star_data.lifetime = float(10000.0 * pow(0.1, math.log(star_data.mass * 0.5) / math.log(num5) + 1.0) * num2)
        star_data.age = float(num * 0.4 + 0.3)
        if self.specify_birth_star_age > 1E-05: star_data.age = self.specify_birth_star_age
        num6: float = (1.0 - pow(clamp(star_data.age, 0.0, 1.0), 20.0) * 0.5) * star_data.mass
        star_data.temperature = float(pow(num6, 0.56 + 0.14 / (math.log(num6 + 4.0) / math.log(5.0))) * 4450.0 + 1300.0)
        num7: float = math.log((star_data.temperature - 1300.0) / 4500.0) / math.log(2.6) - 0.5
        if num7 < 0.0: num7 *= 4.0
        if num7 > 2.0: num7 = 2.0
        elif num7 < -4.0: num7 = -4.0
        star_data.spectr = ESpectrType(round(num7 + 4.0))
        star_data.color = clamp((num7 + 3.5) * 0.2, 0.0, 1.0)
        star_data.class_factor = num7
        star_data.luminosity = pow(num6, 0.7)
        star_data.radius = float(pow(star_data.mass, 0.4) * num3)
        star_data.acdisk_radius = 0.0
        p: float = num7 + 2.0
        star_data.habitable_radius = pow(1.7, p) + 0.2 * min(1.0, star_data.orbit_scaler)
        star_data.light_balance_radius = pow(1.7, p)
        star_data.orbit_scaler = pow(1.35, p)
        if star_data.orbit_scaler < 1.0: star_data.orbit_scaler = lerp(star_data.orbit_scaler, 1.0, 0.6)
        self.set_star_age(star_data, star_data.age, rn, rt)
        star_data.dyson_radius = star_data.orbit_scaler * 0.28
        if star_data.dyson_radius * 40000.0 < star_data.physics_radius * 1.5:
            star_data.dyson_radius = float(star_data.physics_radius * 1.5 / 40000.0)
        star_data.uPosition = Vec3(0, 0, 0)
        star_data.name = NameGen.random_star_name(seed2, star_data, cluster)
        star_data.overrideName = ""
        return star_data

    def create_star_planets(self, cluster: "ClusterData", star: StarData) -> None:
        PLANET_GENERATOR = PlanetGenerator()
        dotnet_35_random: DotNet35Random = DotNet35Random(star.seed)
        dotnet_35_random.next()
        dotnet_35_random.next()
        dotnet_35_random.next()
        dotnet_35_random2: DotNet35Random = DotNet35Random(dotnet_35_random.next())
        num: float = dotnet_35_random2.next_double()
        num2: float = dotnet_35_random2.next_double()
        num3: float = dotnet_35_random2.next_double()
        num4: float = dotnet_35_random2.next_double()
        num5: float = dotnet_35_random2.next_double()
        num6: float = dotnet_35_random2.next_double() * 0.2 + 0.9
        num7: float = dotnet_35_random2.next_double() * 0.2 + 0.9
        dotnet_35_random3: DotNet35Random = DotNet35Random(dotnet_35_random.next())
        if star.type == EStarType.BlackHole:
            star.planet_count = 1
            star.planets = [PlanetData() for _ in range(star.planet_count)]
            info_seed: int = dotnet_35_random2.next()
            gen_seed: int = dotnet_35_random2.next()
            star.planets[0] = PLANET_GENERATOR.create_planet(cluster, star, [],0, 0, 3, 1, gas_giant=False, info_seed=info_seed,
                                            gen_seed=gen_seed)
        elif star.type == EStarType.NeutronStar:
            star.planet_count = 1
            star.planets = [PlanetData() for _ in range(star.planet_count)]
            info_seed2: int = dotnet_35_random2.next()
            gen_seed2: int = dotnet_35_random2.next()
            star.planets[0] = PLANET_GENERATOR.create_planet(cluster, star, [],0, 0, 3, 1, gas_giant=False, info_seed=info_seed2,
                                            gen_seed=gen_seed2)
        elif star.type == EStarType.WhiteDwarf:
            if num < 0.699999988079071:
                star.planet_count = 1
                star.planets = [PlanetData() for _ in range(star.planet_count)]
                info_seed3: int = dotnet_35_random2.next()
                gen_seed3: int = dotnet_35_random2.next()
                star.planets[0] = PLANET_GENERATOR.create_planet(cluster, star, [],0, 0, 3, 1, gas_giant=False, info_seed=info_seed3,
                                                gen_seed=gen_seed3)
            else:
                star.planet_count = 2
                star.planets = [PlanetData() for _ in range(star.planet_count)]
                num8: int = 0
                num9: int = 0
                if num2 < 0.30000001192092896:
                    num8 = dotnet_35_random2.next()
                    num9 = dotnet_35_random2.next()
                    star.planets[0] = PLANET_GENERATOR.create_planet(cluster, star, [],0, 0, 3, 1, gas_giant=False, info_seed=num8,
                                                    gen_seed=num9)
                    num8 = dotnet_35_random2.next()
                    num9 = dotnet_35_random2.next()
                    star.planets[1] = PLANET_GENERATOR.create_planet(cluster, star, [],1, 0, 4, 2, gas_giant=False, info_seed=num8,
                                                    gen_seed=num9)
                else:
                    num8 = dotnet_35_random2.next()
                    num9 = dotnet_35_random2.next()
                    star.planets[0] = PLANET_GENERATOR.create_planet(cluster, star, [],0, 0, 4, 1, gas_giant=True, info_seed=num8,
                                                    gen_seed=num9)
                    num8 = dotnet_35_random2.next()
                    num9 = dotnet_35_random2.next()
                    star.planets[1] = PLANET_GENERATOR.create_planet(cluster, star, [],1, 1, 1, 1, gas_giant=False, info_seed=num8,
                                                    gen_seed=num9)
        elif star.type == EStarType.GiantStar:
            if num < 0.30000001192092896:
                star.planet_count = 1
                star.planets = [PlanetData() for _ in range(star.planet_count)]
                info_seed4: int = dotnet_35_random2.next()
                gen_seed4: int = dotnet_35_random2.next()
                orbit_index: int = 3 if num3 > 0.5 else 2
                star.planets[0] = PLANET_GENERATOR.create_planet(cluster, star, [],0, 0, orbit_index, 1, gas_giant=False, info_seed=info_seed4,
                                                gen_seed=gen_seed4)
            elif num < 0.800000011920929:
                star.planet_count = 2
                star.planets = [PlanetData() for _ in range(star.planet_count)]
                num10: int = 0
                num11: int = 0
                if num2 < 0.25:
                    num10 = dotnet_35_random2.next()
                    num11 = dotnet_35_random2.next()
                    orbit_index2: int = (3 if num3 > 0.5 else 2)
                    star.planets[0] = PLANET_GENERATOR.create_planet(cluster, star, [],0, 0, orbit_index2, 1, gas_giant=False, info_seed=num10,
                                                    gen_seed=num11)
                    num10 = dotnet_35_random2.next()
                    num11 = dotnet_35_random2.next()
                    orbit_index2: int = (4 if num3 > 0.5 else 3)
                    star.planets[1] = PLANET_GENERATOR.create_planet(cluster, star, [],1, 0, orbit_index2, 2, gas_giant=False, info_seed=num10,
                                                    gen_seed=num11)
                else:
                    num10 = dotnet_35_random2.next()
                    num11 = dotnet_35_random2.next()
                    star.planets[0] = PLANET_GENERATOR.create_planet(cluster, star, [],0, 0, 3, 1, gas_giant=True, info_seed=num10,
                                                    gen_seed=num11)
                    num10 = dotnet_35_random2.next()
                    num11 = dotnet_35_random2.next()
                    star.planets[1] = PLANET_GENERATOR.create_planet(cluster, star, [],1, 1, 1, 1, gas_giant=False, info_seed=num10,
                                                    gen_seed=num11)
            else:
                star.planet_count = 3
                star.planets = [PlanetData() for _ in range(star.planet_count)]
                num12: int = 0
                num13: int = 0
                if num2 < 0.15000000596046448:
                    num12 = dotnet_35_random2.next()
                    num13 = dotnet_35_random2.next()
                    orbit_index3: int = (3 if num3 > 0.5 else 2)
                    star.planets[0] = PLANET_GENERATOR.create_planet(cluster, star, [],0, 0, orbit_index3, 1, gas_giant=False, info_seed=num12,
                                                    gen_seed=num13)
                    num12 = dotnet_35_random2.next()
                    num13 = dotnet_35_random2.next()
                    orbit_index3: int = (4 if num3 > 0.5 else 3)
                    star.planets[1] = PLANET_GENERATOR.create_planet(cluster, star, [],1, 0, orbit_index3, 2, gas_giant=False, info_seed=num12,
                                                    gen_seed=num13)
                    num12 = dotnet_35_random2.next()
                    num13 = dotnet_35_random2.next()
                    orbit_index3: int = (5 if num3 > 0.5 else 4)
                    star.planets[2] = PLANET_GENERATOR.create_planet(cluster, star, [],2, 0, orbit_index3, 3, gas_giant=False, info_seed=num12,
                                                    gen_seed=num13)
                elif num2 < 0.75:
                    num12 = dotnet_35_random2.next()
                    num13 = dotnet_35_random2.next()
                    orbit_index4: int = (3 if num3 > 0.5 else 2)
                    star.planets[0] = PLANET_GENERATOR.create_planet(cluster, star, [],0, 0, orbit_index4, 1, gas_giant=False, info_seed=num12,
                                                    gen_seed=num13)
                    num12 = dotnet_35_random2.next()
                    num13 = dotnet_35_random2.next()
                    orbit_index4: int = (4 if num3 > 0.5 else 3)
                    star.planets[1] = PLANET_GENERATOR.create_planet(cluster, star, [],1, 0, orbit_index4, 2, gas_giant=False, info_seed=num12,
                                                    gen_seed=num13)
                    num12 = dotnet_35_random2.next()
                    num13 = dotnet_35_random2.next()
                    orbit_index4: int = (5 if num3 > 0.5 else 4)
                    star.planets[2] = PLANET_GENERATOR.create_planet(cluster, star, [],2, 0, orbit_index4, 3, gas_giant=False, info_seed=num12,
                                                    gen_seed=num13)
                else:
                    num12 = dotnet_35_random2.next()
                    num13 = dotnet_35_random2.next()
                    orbitalIndex5: int = (4 if num3 > 0.5 else 3)
                    star.planets[0] = PLANET_GENERATOR.create_planet(cluster, star, [],0, 0, orbitalIndex5, 1, gas_giant=True, info_seed=num12,
                                                    gen_seed=num13)
                    num12 = dotnet_35_random2.next()
                    num13 = dotnet_35_random2.next()
                    star.planets[1] = PLANET_GENERATOR.create_planet(cluster, star, [],1, 1, 1, 1, gas_giant=False, info_seed=num12,
                                                    gen_seed=num13)
                    num12 = dotnet_35_random2.next()
                    num13 = dotnet_35_random2.next()
                    star.planets[2] = PLANET_GENERATOR.create_planet(cluster, star, [],2, 1, 2, 2, gas_giant=False, info_seed=num12,
                                                    gen_seed=num13)
        else:
            self._p_gas = [0.0] * len(self._p_gas)
            if star.index == 0:
                star.planet_count = 4
                self._p_gas[0] = 0.0
                self._p_gas[1] = 0.0
                self._p_gas[2] = 0.0
            elif star.spectr == ESpectrType.M:
                if   num < 0.1: star.planet_count = 1
                elif num < 0.3: star.planet_count = 2
                elif num < 0.8: star.planet_count = 3
                else:           star.planet_count = 4
                if star.planet_count <= 3:
                    self._p_gas[0] = 0.2
                    self._p_gas[1] = 0.2
                else:
                    self._p_gas[0] = 0.0
                    self._p_gas[1] = 0.2
                    self._p_gas[2] = 0.3
            elif star.spectr == ESpectrType.K:
                if   num < 0.10: star.planet_count = 1
                elif num < 0.20: star.planet_count = 2
                elif num < 0.70: star.planet_count = 3
                elif num < 0.95: star.planet_count = 4
                else:            star.planet_count = 5
                if star.planet_count <= 3:
                    self._p_gas[0] = 0.18
                    self._p_gas[1] = 0.18
                else:
                    self._p_gas[0] = 0.0
                    self._p_gas[1] = 0.18
                    self._p_gas[2] = 0.28
                    self._p_gas[3] = 0.28
            elif star.spectr == ESpectrType.G:
                if   num < 0.40: star.planet_count = 3
                elif num < 0.90: star.planet_count = 4
                else:            star.planet_count = 5
                if star.planet_count <= 3:
                    self._p_gas[0] = 0.18
                    self._p_gas[1] = 0.18
                else:
                    self._p_gas[0] = 0.0
                    self._p_gas[1] = 0.2
                    self._p_gas[2] = 0.3
                    self._p_gas[3] = 0.3
            elif star.spectr == ESpectrType.F:
                if   num < 0.35: star.planet_count = 3
                elif num < 0.80: star.planet_count = 4
                else:            star.planet_count = 5
                if star.planet_count <= 3:
                    self._p_gas[0] = 0.2
                    self._p_gas[1] = 0.2
                else:
                    self._p_gas[0] = 0.0
                    self._p_gas[1] = 0.22
                    self._p_gas[2] = 0.31
                    self._p_gas[3] = 0.31
            elif star.spectr == ESpectrType.A:
                if   num < 0.30: star.planet_count = 3
                elif num < 0.75: star.planet_count = 4
                else:            star.planet_count = 5
                if star.planet_count <= 3:
                    self._p_gas[0] = 0.2
                    self._p_gas[1] = 0.2
                else:
                    self._p_gas[0] = 0.1
                    self._p_gas[1] = 0.28
                    self._p_gas[2] = 0.3
                    self._p_gas[3] = 0.35
            elif star.spectr == ESpectrType.B:
                if   num < 0.30: star.planet_count = 4
                elif num < 0.75: star.planet_count = 5
                else:            star.planet_count = 6
                if star.planet_count <= 3:
                    self._p_gas[0] = 0.2
                    self._p_gas[1] = 0.2
                else:
                    self._p_gas[0] = 0.1
                    self._p_gas[1] = 0.22
                    self._p_gas[2] = 0.28
                    self._p_gas[3] = 0.35
                    self._p_gas[4] = 0.35
            elif star.spectr == ESpectrType.O:
                if   num < 0.50: star.planet_count = 5
                else:            star.planet_count = 6
                self._p_gas[0] = 0.1
                self._p_gas[1] = 0.2
                self._p_gas[2] = 0.25
                self._p_gas[3] = 0.30
                self._p_gas[4] = 0.32
                self._p_gas[5] = 0.35
            else:
                star.planet_count = 1

        star.planets = [PlanetData() for _ in range(star.planet_count)]
        num14: int = 0
        num15: int = 0
        num16: int = 0
        num17: int = 1
        for i in range(star.planet_count):
            info_seed5 = dotnet_35_random2.next()
            gen_seed5 = dotnet_35_random2.next()
            num18: float = dotnet_35_random2.next_double()
            num19: float = dotnet_35_random2.next_double()
            flag: bool = False
            if num16 == 0:
                num14 += 1
                if i < star.planet_count - 1 and num18 < self._p_gas[i]:
                    flag = True
                    if num17 < 3: num17 = 3
                while True:
                    if star.index == 0 and num17 == 3:
                        flag = True
                        break
                    num20: int = star.planet_count - i
                    num21: int = 9 - num17
                    if num21 <= num20:
                        break
                    a: float = float(num20) / float(num21)
                    a = lerp(a, 1.0, 0.15) + 0.01 if num17 <= 3 else lerp(a, 1.0, 0.45) + 0.01
                    if dotnet_35_random2.next_double() < a:
                        break
                    num17 += 1
            else:
                num15 += 1
                flag = False
            star.planets[i] = PLANET_GENERATOR.create_planet(
                cluster, star, [], i, num16,
                                num17 if num16 == 0 else num15,
                                num14 if num16 == 0 else num15,
                                flag, info_seed5, gen_seed5
            )
            num17 += 1
            if flag:
                num16 = num14
                num15 = 0
            else:
                num16 = 0
                num15 = 0
        num22: int = 0
        num23: int = 0
        num24: int = 0
        num25: int = 0
        for j in range(star.planet_count):
            if star.planets[j].type == EPlanetType.Gas:
                num22 = star.planets[j].orbit_index
                break
        for k in range(star.planet_count):
            if star.planets[k].orbit_around == 0:
                num23 = star.planets[k].orbit_index
        if num22 > 0:
            num26: int = num22 - 1
            flag2: bool = True
            for l in range(star.planet_count):
                if star.planets[l].orbit_around == 0 and star.planets[l].orbit_index == num22 - 1:
                    flag2 = False
                    break
            if flag2 and num4 < 0.2 + num26 * 0.2:
                num24 = num26

        # Rest is Dark Fog

        return None

    @staticmethod
    def set_star_age(star: StarData, new_age: float, rn: float, rt: float) -> None:

        star.age = new_age

        num: float = float(rn * 0.1 + 0.95)
        num2: float = float(rt * 0.4 + 0.8)
        num3: float = float(rt * 9.0 + 1.0)

        if new_age >= 1.0:
            if star.mass >= 18.0:
                star.type = EStarType.BlackHole
                star.spectr = ESpectrType.X
                star.mass *= 2.5 * num2
                star.radius *= 1.0
                star.acdisk_radius = star.radius * 5.0
                star.temperature = 0.0
                star.luminosity *= 0.001 * num
                star.habitable_radius = 0.0
                star.light_balance_radius *= 0.4 * num
                star.color = 1.0
            elif star.mass >= 7.0:
                star.type = EStarType.NeutronStar
                star.spectr = ESpectrType.X
                star.mass *= 0.2 * num
                star.radius *= 0.15
                star.acdisk_radius = star.radius * 9.0
                star.temperature = num3 * 10000000.0
                star.luminosity *= 0.1 * num
                star.habitable_radius = 0.0
                star.light_balance_radius *= 3.0 * num
                star.orbit_scaler *= 1.5 * num
                star.color = 1.0
            else:
                star.type = EStarType.WhiteDwarf
                star.spectr = ESpectrType.X
                star.mass *= 0.2 * num
                star.radius *= 0.2
                star.acdisk_radius = 0.0
                star.temperature = num2 * 150000.0
                star.luminosity *= 0.04 * num2
                star.habitable_radius *= 0.15 * num2
                star.light_balance_radius *= 0.2 * num
                star.color = 0.7
        elif new_age >= 0.96:
            num4: float = float(math.pow(5.0, math.fabs(math.log(star.mass) - 0.7)) * 5.0)
            if num4 > 10:
                num4: float = (math.log(num4 * 0.1) + 1) * 10
            num5: float = 1.0 - math.pow(star.age, 30.0) * 0.5
            star.type = EStarType.GiantStar
            star.mass *= num5
            star.radius *= num4 * num2
            star.acdisk_radius = 0.0
            star.temperature *= num5
            star.luminosity *= 1.6 * num
            star.habitable_radius *= 9.0 * num
            star.light_balance_radius *= 3.0 * num
            star.orbit_scaler *= 3.3 * num

class ClusterGenerator:
    def __init__(self, seed: int, star_count: int):
        self.ALGORITHM_ID: int = 20200403
        self.tmp_poses: list[Vec3] = []
        self.tmp_drunk: list[Vec3] = []
        self.tmp_state: list[int] | None = None
        self.STAR_GENERATOR = StarGenerator()

    def _generate_temp_poses(self, seed: int, target_count: int, iter_count: int, min_dist: float,
                             min_step_length: float, max_step_length: float, flatten: float) -> int:
        # Force iterations to be between 1 and 16
        iter_count = int(clamp(iter_count, 1, 16))

        # Do random poses
        self._random_poses(seed, target_count * iter_count, min_dist, min_step_length, max_step_length, flatten)

        # Remove duplicates
        for num in range(len(self.tmp_poses) - 1, -1, -1):
            if num % iter_count != 0: self.tmp_poses.pop(num)
            if len(self.tmp_poses) <= target_count: break

        # Return the number of poses
        return len(self.tmp_poses)

    def _random_poses(self, seed: int, max_count: int, min_dist: float,
                      min_step_length: float, max_step_length: float, flatten: float) -> None:
        dotnet_35_random: DotNet35Random = DotNet35Random(seed)
        num: float = dotnet_35_random.next_double()
        self.tmp_poses.append(Vec3(0, 0, 0))
        num2: int = 6
        num3: int = 8
        if num2 < 1: num2 = 1
        if num3 < 1: num3 = 1
        num4: int = int(num * float(num3 - num2) + float(num2))

        for _ in range(num4):
            for num5 in range(256):
                num6: float =  dotnet_35_random.next_double() * 2.0 - 1.0
                num7: float = (dotnet_35_random.next_double() * 2.0 - 1.0) * flatten
                num8: float =  dotnet_35_random.next_double() * 2.0 - 1.0
                num9: float =  dotnet_35_random.next_double()
                num10: float = num6 * num6 + num7 * num7 + num8 * num8
                if num10 > 1.0 or num10 < 1E-08: continue
                num11: float = math.sqrt(num10)
                num9 = (num9 * (max_step_length - min_step_length) + min_dist) / num11
                vectorLF: Vec3 = Vec3(num6 * num9, num7 * num9, num8 * num9)
                if not self._check_collision(self.tmp_poses, vectorLF, min_dist):
                    self.tmp_drunk.append(vectorLF)
                    self.tmp_poses.append(vectorLF)
                    if len(self.tmp_poses) < max_count:
                        break
                    return

        for num12 in range(256):
            for j in range(len(self.tmp_drunk)):
                if dotnet_35_random.next_double() > 0.7: continue
                for num13 in range(256):
                    num14: float =  dotnet_35_random.next_double() * 2.0 - 1.0
                    num15: float = (dotnet_35_random.next_double() * 2.0 - 1.0) * flatten
                    num16: float =  dotnet_35_random.next_double() * 2.0 - 1.0
                    num17: float =  dotnet_35_random.next_double()
                    num18: float = num14 * num14 + num15 * num15 + num16 * num16
                    if num18 > 1.0 or num18 < 1E-08: continue
                    num19: float = math.sqrt(num18)
                    num17 = (num17 * (max_step_length - min_step_length) + min_dist) / num19
                    vectorLF2: Vec3 = Vec3(self.tmp_drunk[j].x + num14 * num17,
                                           self.tmp_drunk[j].y + num15 * num17,
                                           self.tmp_drunk[j].z + num16 * num17)
                    if not self._check_collision(self.tmp_poses, vectorLF2, min_dist):
                        self.tmp_drunk[j] = vectorLF2
                        self.tmp_poses.append(vectorLF2)
                        if len(self.tmp_poses) < max_count:
                            break
                        return

    @staticmethod
    def _check_collision(pts: list[Vec3], pt: Vec3, min_dist: float) -> bool:
        num: float = min_dist * min_dist
        for pt2 in pts:
            num2: float = pt.x - pt2.x
            num3: float = pt.y - pt2.y
            num4: float = pt.z - pt2.z
            if num2 * num2 + num3 * num3 + num4 * num4 < num:
                return True
        return False

    def create_cluster(self, *, cluster_seed: int, star_count: int) -> ClusterData:
        dotnet_35_random: DotNet35Random = DotNet35Random(cluster_seed)
        star_count: int = self._generate_temp_poses(dotnet_35_random.next(), star_count, 4, 2.0, 2.3, 3.5, 0.18)

        cluster_data: ClusterData = ClusterData()
        cluster_data.seed = cluster_seed
        cluster_data.star_count = star_count
        cluster_data.stars = [StarData() for _ in range(star_count)]
        assert star_count > 0, "Star count must be greater than 0"

        # Random variables
        num: float = dotnet_35_random.next_double()
        num2: float = dotnet_35_random.next_double()
        num3: float = dotnet_35_random.next_double()
        num4: float = dotnet_35_random.next_double()
        num5: int = int(math.ceil(0.010 * star_count + num * 0.3))
        num6: int = int(math.ceil(0.010 * star_count + num2 * 0.3))
        num7: int = int(math.ceil(0.016 * star_count + num3 * 0.4))
        num8: int = int(math.ceil(0.013 * star_count + num4 * 1.4))
        num9: int = star_count - num5
        num10: int = num9 - num6
        num11: int = num10 - num7
        num12: int = (num11 - 1) // num8
        num13: int = num12 // 2

        # Generate stars
        for i in range(star_count):
            star_seed: int = dotnet_35_random.next()
            if i == 0:
                cluster_data.stars[i] = self.STAR_GENERATOR.create_birth_star(cluster_data, star_seed)
                continue
            need_spectr: ESpectrType = ESpectrType.X
            if   i == 3:         need_spectr = ESpectrType.M
            elif i == num11 - 1: need_spectr = ESpectrType.O
            need_type: EStarType = EStarType.MainSeqStar
            if i % num12 == num13: need_type = EStarType.GiantStar
            if i >= num9:          need_type = EStarType.BlackHole
            elif i >= num10:       need_type = EStarType.NeutronStar
            elif i >= num11:       need_type = EStarType.WhiteDwarf
            cluster_data.stars[i] = self.STAR_GENERATOR.create_star(cluster_data, self.tmp_poses[i], i + 1, star_seed, need_type, need_spectr)

        # Generate planets
        for star in cluster_data.stars:
            self.STAR_GENERATOR.create_star_planets(cluster_data, star)

        return cluster_data




def main() -> None:
    SEED: int = 1
    STAR_COUNT = 64




    cluster_generator: ClusterGenerator = ClusterGenerator(SEED, STAR_COUNT)
    cluster_data: ClusterData = cluster_generator.create_cluster(cluster_seed=SEED, star_count=STAR_COUNT)
    print(f"Cluster Seed: {cluster_data.seed}")
    print(f"Star Count: {cluster_data.star_count}")
    print("---------------------------------------------------")
    for star in cluster_data.stars:
        print(f"Star {star.index + 1}:")
        print(f"  Type: {star.type}")
        print(f"  Spectr: {star.spectr}")
        print(f"  Luminosity: {star.luminosity}")
        print("---------------------------------------------------")






if __name__ == "__main__":
    main()