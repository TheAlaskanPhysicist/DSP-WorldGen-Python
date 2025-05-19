from dotnet.rng import DotNet35Random
from data_structures import *












class NameGen:

    con0: list[str] = ["p", "t", "c", "k", "b", "d", "g", "f", "ph", "s", "sh", "th", "h", "v", "z", "th", "r", "ch", "tr", "dr", "m", "n", "l", "y", "w", "sp", "st", "sk", "sc", "sl", "pl", "cl", "bl", "gl", "fr", "fl", "pr", "br", "cr"]
    con1: list[str] = ["thr", "ex", "ec", "el", "er", "ev", "il", "is", "it", "ir", "up", "ut", "ur", "un", "gt", "phr"]
    vow0: list[str] = ["a", "an", "am", "al", "o", "u", "xe"]
    vow1: list[str] = ["ea", "ee", "ie", "i", "e", "a", "er", "a", "u", "oo", "u", "or", "o", "oa", "ar", "a", "ei", "ai", "i", "au", "ou", "ao", "ir"]
    vow2: list[str] = ["y", "oi", "io", "iur", "ur", "ac", "ic"]
    ending: list[str] = ["er", "n", "un", "or", "ar", "o", "o", "ans", "us", "ix", "us", "iurs", "a", "eo", "urn", "es", "eon", "y"]
    roman: list[str] = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX"]
    constellations: list[str] = [
        "Andromedae", "Antliae", "Apodis", "Aquarii", "Aquilae", "Arae", "Arietis", "Aurigae", "Bootis", "Caeli",
        "Camelopardalis", "Cancri", "Canum Venaticorum", "Canis Majoris", "Canis Minoris", "Capricorni", "Carinae",
        "Cassiopeiae", "Centauri", "Cephei",
        "Ceti", "Chamaeleontis", "Circini", "Columbae", "Comae Berenices", "Coronae Australis", "Coronae Borealis",
        "Corvi", "Crateris", "Crucis",
        "Cygni", "Delphini", "Doradus", "Draconis", "Equulei", "Eridani", "Fornacis", "Geminorum", "Gruis", "Herculis",
        "Horologii", "Hydrae", "Hydri", "Indi", "Lacertae", "Leonis", "Leonis Minoris", "Leporis", "Librae", "Lupi",
        "Lyncis", "Lyrae", "Mensae", "Microscopii", "Monocerotis", "Muscae", "Normae", "Octantis", "Ophiuchii",
        "Orionis",
        "Pavonis", "Pegasi", "Persei", "Phoenicis", "Pictoris", "Piscium", "Piscis Austrini", "Puppis", "Pyxidis",
        "Reticuli",
        "Sagittae", "Sagittarii", "Scorpii", "Sculptoris", "Scuti", "Serpentis", "Sextantis", "Tauri", "Telescopii",
        "Trianguli",
        "Trianguli Australis", "Tucanae", "Ursae Majoris", "Ursae Minoris", "Velorum", "Virginis", "Volantis",
        "Vulpeculae"
    ]
    alphabeta: list[str] = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Eta", "Theta", "Iota", "Kappa","Lambda"]
    alphabeta_letter: list[str] = ["α", "β", "γ", "δ", "ε", "ζ", "η", "θ", "ι", "κ","λ"]
    raw_star_names: list[str] = [
        "Acamar", "Achernar", "Achird", "Acrab", "Acrux", "Acubens", "Adhafera", "Adhara", "Adhil", "Agena",
        "Aladfar", "Albaldah", "Albali", "Albireo", "Alchiba", "Alcor", "Alcyone", "Alderamin", "Aldhibain", "Aldib",
        "Alfecca", "Alfirk", "Algedi", "Algenib", "Algenubi", "Algieba", "Algjebbath", "Algol", "Algomeyla", "Algorab",
        "Alhajoth", "Alhena", "Alifa", "Alioth", "Alkaid", "Alkalurops", "Alkaphrah", "Alkes", "Alkhiba", "Almach",
        "Almeisan", "Almuredin", "AlNa'ir", "Alnasl", "Alnilam", "Alnitak", "Alniyat", "Alphard", "Alphecca",
        "Alpheratz",
        "Alrakis", "Alrami", "Alrescha", "AlRijil", "Alsahm", "Alsciaukat", "Alshain", "Alshat", "Alshemali",
        "Alsuhail",
        "Altair", "Altais", "Alterf", "Althalimain", "AlTinnin", "Aludra", "AlulaAustralis", "AlulaBorealis", "Alwaid",
        "Alwazn",
        "Alya", "Alzirr", "AmazonStar", "Ancha", "Anchat", "AngelStern", "Angetenar", "Ankaa", "Anser", "Antecanis",
        "Apollo", "Arich", "Arided", "Arietis", "Arkab", "ArkebPrior", "Arneb", "Arrioph", "AsadAustralis", "Ascella",
        "Aschere", "AsellusAustralis", "AsellusBorealis", "AsellusPrimus", "Ashtaroth", "Asmidiske", "Aspidiske",
        "Asterion", "Asterope", "Asuia",
        "Athafiyy", "Atik", "Atlas", "Atria", "Auva", "Avior", "Azelfafage", "Azha", "Azimech", "BatenKaitos",
        "Becrux", "Beid", "Bellatrix", "Benatnasch", "Biham", "Botein", "Brachium", "Bunda", "Cajam", "Calbalakrab",
        "Calx", "Canicula", "Capella", "Caph", "Castor", "Castula", "Cebalrai", "Ceginus", "Celaeno", "Chara",
        "Chertan", "Choo", "Clava", "CorCaroli", "CorHydrae", "CorLeonis", "Cornu", "CorScorpii", "CorSepentis",
        "CorTauri",
        "Coxa", "Cursa", "Cymbae", "Cynosaura", "Dabih", "DenebAlgedi", "DenebDulfim", "DenebelOkab", "DenebKaitos",
        "DenebOkab",
        "Denebola", "Dhalim", "Dhur", "Diadem", "Difda", "DifdaalAuwel", "Dnoces", "Dubhe", "Dziban", "Dzuba",
        "Edasich", "ElAcola", "Elacrab", "Electra", "Elgebar", "Elgomaisa", "ElKaprah", "ElKaridab", "Elkeid",
        "ElKhereb",
        "Elmathalleth", "Elnath", "ElPhekrah", "Eltanin", "Enif", "Erakis", "Errai", "FalxItalica", "Fidis",
        "Fomalhaut",
        "Fornacis", "FumAlSamakah", "Furud", "Gacrux", "Gallina", "GarnetStar", "Gemma", "Genam", "Giausar",
        "GiedePrime",
        "Giedi", "Gienah", "Gienar", "Gildun", "Girtab", "Gnosia", "Gomeisa", "Gorgona", "Graffias", "Hadar",
        "Hamal", "Haris", "Hasseleh", "Hastorang", "Hatysa", "Heka", "Hercules", "Heze", "Hoedus", "Homam",
        "HyadumPrimus", "Icalurus", "Iclarkrav", "Izar", "Jabbah", "Jewel", "Jugum", "Juza", "Kabeleced", "Kaff",
        "Kaffa", "Kaffaljidma", "Kaitain", "KalbalAkrab", "Kat", "KausAustralis", "KausBorealis", "KausMedia", "Keid",
        "KeKouan",
        "Kelb", "Kerb", "Kerbel", "KiffaBoraelis", "Kitalpha", "Kochab", "Kornephoros", "Kraz", "Ksora", "Kuma",
        "Kurhah", "Kursa", "Lesath", "Maasym", "Maaz", "Mabsuthat", "Maia", "Marfik", "Markab", "Marrha",
        "Matar", "Mebsuta", "Megres", "Meissa", "Mekbuda", "Menkalinan", "Menkar", "Menkent", "Menkib", "Merak",
        "Meres", "Merga", "Meridiana", "Merope", "Mesartim", "Metallah", "Miaplacidus", "Mimosa", "Minelauva", "Minkar",
        "Mintaka", "Mirac", "Mirach", "Miram", "Mirfak", "Mirzam", "Misam", "Mismar", "Mizar", "Muhlifain",
        "Muliphein", "Muphrid", "Muscida", "NairalSaif", "NairalZaurak", "Naos", "Nash", "Nashira", "Navi", "Nekkar",
        "Nicolaus", "Nihal", "Nodus", "Nunki", "Nusakan", "OculusBoreus", "Okda", "Osiris", "OsPegasi", "Palilicium",
        "Peacock", "Phact", "Phecda", "Pherkad", "PherkadMinor", "Pherkard", "Phoenice", "Phurad", "Pishpai", "Pleione",
        "Polaris", "Pollux", "Porrima", "Postvarta", "Praecipua", "Procyon", "Propus", "Protrygetor", "Pulcherrima",
        "Rana",
        "RanaSecunda", "Rasalas", "Rasalgethi", "Rasalhague", "Rasalmothallah", "RasHammel", "Rastaban", "Reda",
        "Regor", "Regulus",
        "Rescha", "RigilKentaurus", "RiglalAwwa", "Rotanen", "Ruchba", "Ruchbah", "Rukbat", "Rutilicus", "Saak",
        "Sabik",
        "Sadachbia", "Sadalbari", "Sadalmelik", "Sadalsuud", "Sadatoni", "Sadira", "Sadr", "Saidak", "Saiph", "Salm",
        "Sargas", "Sarin", "Sartan", "Sceptrum", "Scheat", "Schedar", "Scheddi", "Schemali", "Scutulum", "SeatAlpheras",
        "Segin", "Seginus", "Shaula", "Shedir", "Sheliak", "Sheratan", "Singer", "Sirius", "Sirrah", "Situla",
        "Skat", "Spica", "Sterope", "Subra", "Suha", "Suhail", "SuhailHadar", "SuhailRadar", "Suhel", "Sulafat",
        "Superba", "Svalocin", "Syrma", "Tabit", "Tais", "Talitha", "TaniaAustralis", "TaniaBorealis", "Tarazed",
        "Tarf",
        "TaTsun", "Taygeta", "Tegmen", "Tejat", "TejatPrior", "Terebellum", "Theemim", "Thuban", "Tolimann",
        "Tramontana",
        "Tsih", "Tureis", "Unukalhai", "Vega", "Venabulum", "Venator", "Vendemiatrix", "Vespertilio", "Vildiur",
        "Vindemiatrix",
        "Wasat", "Wazn", "YedPosterior", "YedPrior", "Zaniah", "Zaurak", "Zavijava", "ZenithStar", "Zibel", "Zosma",
        "Zubenelakrab", "ZubenElgenubi", "Zubeneschamali", "ZubenHakrabi", "Zubra"
    ]
    raw_giant_names: list[str] = [
        "AH Scorpii", "Aldebaran", "Alpha Herculis", "Antares", "Arcturus", "AV Persei", "BC Cygni", "Betelgeuse",
        "BI Cygni", "BO Carinae",
        "Canopus", "CE Tauri", "CK Carinae", "CW Leonis", "Deneb", "Epsilon Aurigae", "Eta Carinae", "EV Carinae",
        "IX Carinae", "KW Sagittarii",
        "KY Cygni", "Mira", "Mu Cephei", "NML Cygni", "NR Vulpeculae", "PZ Cassiopeiae", "R Doradus", "R Leporis",
        "Rho Cassiopeiae", "Rigel",
        "RS Persei", "RT Carinae", "RU Virginis", "RW Cephei", "S Cassiopeiae", "S Cephei", "S Doradus", "S Persei",
        "SU Persei", "TV Geminorum",
        "U Lacertae", "UY Scuti", "V1185 Scorpii", "V354 Cephei", "V355 Cepheus", "V382 Carinae", "V396 Centauri",
        "V437 Scuti", "V509 Cassiopeiae", "V528 Carinae",
        "V602 Carinae", "V648 Cassiopeiae", "V669 Cassiopeiae", "V838 Monocerotis", "V915 Scorpii", "VV Cephei",
        "VX Sagittarii", "VY Canis Majoris", "WOH G64", "XX Persei"
    ]

    giant_name_formats: list[str] = [
        "HD {0:04}{1:02}",
        "HDE {0:04}{1:02}",
        "HR {0:04}",
        "HV {0:04}",
        "LBV {0:04}-{1:02}",
        "NSV {0:04}",
        "YSC {0:04}-{1:02}"
    ]

    neutron_star_name_formats: list[str] = [
        "NTR J{0:02}{1:02}+{2:02}",
        "NTR J{0:02}{1:02}-{2:02}"
    ]

    black_hole_name_formats: list[str] = [
        "DSR J{0:02}{1:02}+{2:02}",
        "DSR J{0:02}{1:02}-{2:02}"
    ]

    @staticmethod
    def random_name(seed: int) -> str:
        dotNet35Random: DotNet35Random = DotNet35Random(seed)
        num: int = int(dotNet35Random.next_double() * 1.8 + 2.3)
        text: str = ""
        for i in range(num):
            if not (dotNet35Random.next_double() < 0.05000000074505806) or i != 0:
                text += ""
            else:
                text += ""
        if "uu" in text >= 0:
            text = text.replace("uu", "u")
        if "ooo" in text >= 0:
            text = text.replace("ooo", "oo")
        if "eee" in text >= 0:
            text = text.replace("eee", "ee")
        if "eea" in text >= 0:
            text = text.replace("eea", "ea")
        if "aa" in text >= 0:
            text = text.replace("aa", "a")
        if "yy" in text >= 0:
            text = text.replace("yy", "y")

        if text == "":
            text = "NullStarString"
        return text[0].upper() + text[1:]





    @staticmethod
    def random_star_name(seed: int, star_data: StarData, galaxy: ClusterData) -> str:
        dotNet35Random: DotNet35Random = DotNet35Random(seed)
        num: int = 0
        while num < 256:
            text: str = NameGen._random_star_name(dotNet35Random.next(), star_data)
            flag: bool = False
            for i in range(galaxy.star_count):
                if galaxy.stars[i] is not None and galaxy.stars[i].name == text:
                    flag = True
                    break
            if not flag:
                return text
            num += 1
        return "XStar"

    @staticmethod
    def _random_star_name(seed: int, star_data: StarData) -> str:
        dotNet35Random: DotNet35Random = DotNet35Random(seed)
        seed2: int = dotNet35Random.next()
        num: float = dotNet35Random.next_double()
        num2: float = dotNet35Random.next_double()
        if star_data.type == EStarType.GiantStar:
            if num2 < 0.4000000059604645:
                return NameGen.random_giant_star_name_from_raw_names(seed2)
            if num2 < 0.699999988079071:
                return NameGen.random_giant_star_name_with_constellation_alpha(seed2)
            return NameGen.random_giant_star_name_with_format(seed2)
        if star_data.type == EStarType.NeutronStar:
            return NameGen.random_neutron_star_name_with_format(seed2)
        if star_data.type == EStarType.BlackHole:
            return NameGen.random_black_hole_name_with_format(seed2)
        if num < 0.6000000238418579:
            return NameGen.random_star_name_from_raw_names(seed2)
        if num < 0.9300000071525574:
            return NameGen.random_star_name_with_constellation_alpha(seed2)
        return NameGen.random_star_name_with_constellation_number(seed2)

    @staticmethod
    def random_giant_star_name_from_raw_names(seed: int):
        dotNet35Random: DotNet35Random = DotNet35Random(seed)
        num: int = dotNet35Random.next()
        num %= len(NameGen.raw_giant_names)
        return NameGen.raw_giant_names[num]
    @staticmethod
    def random_giant_star_name_with_constellation_alpha(seed: int):
        dotNet35Random: DotNet35Random = DotNet35Random(seed)
        num: int = dotNet35Random.next()
        num2: int = dotNet35Random.next_minmax(15, 26)
        num3: int = dotNet35Random.next_minmax(0, 26)
        num %= len(NameGen.constellations)
        num4: int = 65 + num2
        c: str = chr(65 + num3)
        return str(num4) + c + " " + NameGen.constellations[num]
    @staticmethod
    def random_giant_star_name_with_format(seed: int):
        dotNet35Random: DotNet35Random = DotNet35Random(seed)
        num: int = dotNet35Random.next()
        num2: int = dotNet35Random.next_max(10000)
        num3: int = dotNet35Random.next_max(100)
        num %= len(NameGen.giant_name_formats)
        return str.format(NameGen.giant_name_formats[num], num2, num3)
    @staticmethod
    def random_neutron_star_name_with_format(seed: int):
        dotNet35Random: DotNet35Random = DotNet35Random(seed)
        num: int = dotNet35Random.next()
        num2: int = dotNet35Random.next_max(24)
        num3: int = dotNet35Random.next_max(60)
        num4: int = dotNet35Random.next_minmax(0, 60)
        num %= len(NameGen.neutron_star_name_formats)
        return str.format(NameGen.neutron_star_name_formats[num], num2, num3, num4)
    @staticmethod
    def random_black_hole_name_with_format(seed: int):
        dotNet35Random: DotNet35Random = DotNet35Random(seed)
        num: int = dotNet35Random.next()
        num2: int = dotNet35Random.next_max(24)
        num3: int = dotNet35Random.next_max(60)
        num4: int = dotNet35Random.next_minmax(0, 60)
        num %= len(NameGen.black_hole_name_formats)
        return str.format(NameGen.black_hole_name_formats[num], num2, num3, num4)
    @staticmethod
    def random_star_name_from_raw_names(seed: int):
        dotNet35Random: DotNet35Random = DotNet35Random(seed)
        num: int = dotNet35Random.next()
        num %= len(NameGen.raw_star_names)
        return NameGen.raw_star_names[num]
    @staticmethod
    def random_star_name_with_constellation_alpha(seed: int):
        dotNet35Random: DotNet35Random = DotNet35Random(seed)
        num: int = dotNet35Random.next()
        num2: int = dotNet35Random.next()
        num %= len(NameGen.constellations)
        num2 %= len(NameGen.alphabeta)
        text: str = NameGen.constellations[num]
        if len(text) > 10:
            return NameGen.alphabeta_letter[num2] + " " + text
        return NameGen.alphabeta[num2] + " " + text
    @staticmethod
    def random_star_name_with_constellation_number(seed: int):
        dotNet35Random: DotNet35Random = DotNet35Random(seed)
        num: int = dotNet35Random.next()
        num2: int = dotNet35Random.next_minmax(27, 75)
        num %= len(NameGen.constellations)
        return str(num2) + " " + NameGen.constellations[num]









