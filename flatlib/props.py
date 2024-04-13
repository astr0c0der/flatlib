"""
    This file is part of flatlib - (C) FlatAngle
    Author: João Ventura (flatangleweb@gmail.com)
    

    This module defines some properties of Traditional Astrology core
    elements.
    
    It defines qualities of temperaments, orbs and genders of planets,
    if a house is cardinal, angular or succedent, among others.
    
    To keep things simple, properties are divided in types, such as 
    base properties, planet properties, house properties, etc. Each 
    property type is defined as a lowercased python class so that we 
    can mimic different namespaces in a single python module.
    
"""

from . import const



# ------------------- #
#   Base Properties   #
# ------------------- #

class base:
    # The four elements
    elements = [
        const.FIRE,
        const.EARTH,
        const.AIR,
        const.WATER
    ]

    # The four temperaments
    temperaments = [
        const.CHOLERIC,
        const.MELANCHOLIC,
        const.SANGUINE,
        const.PHLEGMATIC
    ]

    # Genders
    genders = [
        const.MASCULINE,
        const.FEMININE
    ]

    # Factions
    factions = [
        const.DIURNAL,
        const.NOCTURNAL
    ]

    # Sun seasons
    sunseasons = [
        const.SPRING,
        const.SUMMER,
        const.AUTUMN,
        const.WINTER
    ]

    # Element to Temperament
    elementTemperament = {
        const.FIRE: const.CHOLERIC,
        const.EARTH: const.MELANCHOLIC,
        const.AIR: const.SANGUINE,
        const.WATER: const.PHLEGMATIC
    }

    # Temperament to Element
    temperamentElement = {
        const.CHOLERIC: const.FIRE,
        const.MELANCHOLIC: const.EARTH,
        const.SANGUINE: const.AIR,
        const.PHLEGMATIC: const.WATER
    }

    # Qualities of elements
    elementQuality = {
        const.FIRE: [const.HOT, const.DRY],
        const.EARTH: [const.COLD, const.DRY],
        const.AIR: [const.HOT, const.HUMID],
        const.WATER: [const.COLD, const.HUMID]
    }

    # Qualities of temperaments
    temperamentQuality = {
        const.CHOLERIC: [const.HOT, const.DRY],
        const.MELANCHOLIC: [const.COLD, const.DRY],
        const.SANGUINE: [const.HOT, const.HUMID],
        const.PHLEGMATIC: [const.COLD, const.HUMID]
    }

    # Moon Phase Elements
    moonphaseElement = {
        const.MOON_FIRST_QUARTER: const.AIR,
        const.MOON_SECOND_QUARTER: const.FIRE,
        const.MOON_THIRD_QUARTER: const.EARTH,
        const.MOON_LAST_QUARTER: const.WATER
    }

    # Sun Season Elements
    sunseasonElement = {
        const.SPRING: const.AIR,
        const.SUMMER: const.FIRE,
        const.AUTUMN: const.EARTH,
        const.WINTER: const.WATER
    }


# ------------------- #
#   Sign Properties   #
# ------------------- #

class sign:
    _signs = const.LIST_SIGNS

    # Modes
    _modes = [const.CARDINAL, const.FIXED, const.MUTABLE]
    mode = dict(zip(_signs, _modes * 4))

    # Sun Season
    _sunseasons = [[season] * 3 for season in base.sunseasons]
    _sunseasons = sum(_sunseasons, [])
    sunseason = dict(zip(_signs, _sunseasons))

    # Simple properties
    gender = dict(zip(_signs, base.genders * 6))
    faction = dict(zip(_signs, base.factions * 6))
    element = dict(zip(_signs, base.elements * 3))
    temperament = dict(zip(_signs, base.temperaments * 3))

    # Fertilities
    fertility = {
        const.ARIES: const.SIGN_MODERATELY_STERILE,
        const.TAURUS: const.SIGN_MODERATELY_FERTILE,
        const.GEMINI: const.SIGN_STERILE,
        const.CANCER: const.SIGN_FERTILE,
        const.LEO: const.SIGN_STERILE,
        const.VIRGO: const.SIGN_STERILE,
        const.LIBRA: const.SIGN_MODERATELY_FERTILE,
        const.SCORPIO: const.SIGN_FERTILE,
        const.SAGITTARIUS: const.SIGN_MODERATELY_FERTILE,
        const.CAPRICORN: const.SIGN_MODERATELY_STERILE,
        const.AQUARIUS: const.SIGN_MODERATELY_STERILE,
        const.PISCES: const.SIGN_FERTILE
    }

    # Sign number
    number = dict((sign, i + 1) for (i, sign) in enumerate(_signs))

    # Sign figure properties
    figureBestial = [
        const.ARIES,
        const.TAURUS,
        const.LEO,
        const.SAGITTARIUS,
        const.CAPRICORN
    ]

    figureHuman = [
        const.GEMINI,
        const.VIRGO,
        const.LIBRA,
        const.AQUARIUS
    ]

    figureWild = [
        const.LEO
    ]

    fertility = {
        const.ARIES: const.FIRE,
        const.TAURUS: const.EARTH,
        const.GEMINI: const.AIR,
        const.CANCER: const.WATER,
        const.LEO: const.FIRE,
        const.VIRGO: const.EARTH,
        const.LIBRA: const.AIR,
        const.SCORPIO: const.WATER,
        const.SAGITTARIUS: const.FIRE,
        const.CAPRICORN: const.EARTH,
        const.AQUARIUS: const.AIR,
        const.PISCES: const.WATER
    }

# --------------------- #
#   Object Properties   #
# --------------------- #

class object:
    # Mean daily motions
    meanMotion = {
        const.NO_PLANET: 0,
        const.SUN: 0.9833,
        const.MOON: 13.1833,
        const.MERCURY: 0.9833,
        const.VENUS: 0.9833,
        const.MARS: 0.5166,
        const.JUPITER: 0.0833,
        const.SATURN: 0.0333,
        const.URANUS: 0.001,
        const.NEPTUNE: 0.0001,
        const.PLUTO: 0.00001,
        const.CHIRON: 0.00001,
        const.NORTH_NODE: 13.1833,
        const.SOUTH_NODE: 13.1833,
        const.SYZYGY: 0.0,
        const.PARS_FORTUNA:0.0
    }

    # Object orbs
    orb = {
        const.NO_PLANET: 0,
        const.SUN: 12,
        const.MOON: 12,
        const.MERCURY: 7,
        const.VENUS: 7,
        const.MARS: 8,
        const.JUPITER: 9,
        const.SATURN: 9,
        const.URANUS: 5,
        const.NEPTUNE: 5,
        const.PLUTO: 5,
        const.CHIRON: 5,
        const.NORTH_NODE: 12,
        const.SOUTH_NODE: 12,
        const.SYZYGY: 0,
        const.PARS_FORTUNA: 0
    }

    glyphs = {
        const.SUN: '☉',         # Sun symbol
        const.MOON: '☽',        # Moon symbol
        const.MERCURY: '☿',     # Mercury symbol
        const.VENUS: '♀',       # Venus symbol
        const.MARS: '♂',        # Mars symbol
        const.JUPITER: '♃',     # Jupiter symbol
        const.SATURN: '♄',      # Saturn symbol
        const.URANUS: '♅',      # Uranus symbol
        const.NEPTUNE: '♆',     # Neptune symbol
        const.PLUTO: '♇',       # Pluto symbol
        const.CHIRON: '⚷',      # Chiron symbol (note: not universally standardized)
        const.NORTH_NODE: '☊',  # North Node symbol (Caput Draconis or Dragon's Head)
        const.SOUTH_NODE: '☋',  # South Node symbol (Cauda Draconis or Dragon's Tail)
        const.SYZYGY: '☽☌☉',    # Syzygy symbol, combining the Moon and Sun conjunction
        const.PARS_FORTUNA: '⊗',  # Part of Fortune, often represented with a circle with an 'x' through it
    }

    # Planet elements
    element = {
        const.SATURN: const.EARTH,
        const.JUPITER: const.AIR,
        const.MARS: const.FIRE,
        const.SUN: const.FIRE,
        const.VENUS: const.AIR,
        const.MERCURY: const.EARTH,
        const.MOON: const.WATER,
        const.URANUS: const.AIR,
        const.NEPTUNE: const.WATER,
        const.PLUTO: const.WATER,
        const.CHIRON: const.NO_PLANET,
        const.NORTH_NODE: const.NO_PLANET,
        const.SOUTH_NODE: const.NO_PLANET,
        const.SYZYGY: const.NO_PLANET,
        const.PARS_FORTUNA: const.NO_PLANET
    }

    # Planet temperaments
    temperament = {
        const.SATURN: const.MELANCHOLIC,
        const.JUPITER: const.SANGUINE,
        const.MARS: const.CHOLERIC,
        const.SUN: const.CHOLERIC,
        const.VENUS: const.SANGUINE,
        const.MERCURY: const.MELANCHOLIC,
        const.MOON: const.PHLEGMATIC,
        const.URANUS: const.CHOLERIC,
        const.NEPTUNE: const.PHLEGMATIC,
        const.PLUTO: const.MELANCHOLIC,
        const.CHIRON: const.NO_PLANET,
        const.NORTH_NODE: const.NO_PLANET,
        const.SOUTH_NODE: const.NO_PLANET,
        const.SYZYGY: const.NO_PLANET,
        const.PARS_FORTUNA: const.NO_PLANET

    }

    # Planet genders
    gender = {
        const.SATURN: const.MASCULINE,
        const.JUPITER: const.MASCULINE,
        const.MARS: const.MASCULINE,
        const.SUN: const.MASCULINE,
        const.VENUS: const.FEMININE,
        const.MERCURY: const.NEUTRAL,
        const.MOON: const.FEMININE,
        const.URANUS: const.NEUTRAL,  # Often seen as breaking traditional boundaries, including gender
        const.NEPTUNE: const.NEUTRAL,  # Associated with universal or collective aspects transcending gender
        const.PLUTO: const.NEUTRAL,  # Power and transformation are beyond traditional gender roles
        const.CHIRON: const.NO_PLANET,
        const.NORTH_NODE: const.NO_PLANET,
        const.SOUTH_NODE: const.NO_PLANET,
        const.SYZYGY: const.NO_PLANET,
        const.PARS_FORTUNA: const.NO_PLANET
    }

    # Planet factions
    faction = {
        const.SATURN: const.DIURNAL,
        const.JUPITER: const.DIURNAL,
        const.MARS: const.NOCTURNAL,
        const.SUN: const.DIURNAL,
        const.VENUS: const.NOCTURNAL,
        const.MERCURY: const.NEUTRAL,
        const.MOON: const.NOCTURNAL,
        const.URANUS: const.DIURNAL,  # Associated with the sky and heavens, often active
        const.NEPTUNE: const.NOCTURNAL,  # Mystical and elusive, linked to the subconscious
        const.PLUTO: const.NOCTURNAL,  # Underworld connections suggest a more hidden, night-related nature
        const.CHIRON: const.NO_PLANET,
        const.NORTH_NODE: const.NO_PLANET,
        const.SOUTH_NODE: const.NO_PLANET,
        const.SYZYGY: const.NO_PLANET,
        const.PARS_FORTUNA: const.NO_PLANET
    }

    # Sign joy of planets
    signJoy = {
        const.SATURN: const.AQUARIUS,
        const.JUPITER: const.SAGITTARIUS,
        const.MARS: const.SCORPIO,
        const.SUN: const.LEO,
        const.VENUS: const.TAURUS,
        const.MERCURY: const.VIRGO,
        const.MOON: const.CANCER,
        const.URANUS: const.AQUARIUS,  # Joy for Uranus
        const.NEPTUNE: const.PISCES,  # Joy for Neptune
        const.PLUTO: const.SCORPIO,    # Joy for Pluto
        const.CHIRON: const.NO_PLANET,
        const.NORTH_NODE: const.NO_PLANET,
        const.SOUTH_NODE: const.NO_PLANET,
        const.SYZYGY: const.NO_PLANET,
        const.PARS_FORTUNA: const.NO_PLANET
    }
    # House joy of planets
    houseJoy = {
        const.SATURN: const.HOUSE12,
        const.JUPITER: const.HOUSE11,
        const.MARS: const.HOUSE6,
        const.SUN: const.HOUSE9,
        const.VENUS: const.HOUSE5,
        const.MERCURY: const.HOUSE1,
        const.MOON: const.HOUSE3,
        const.URANUS: const.HOUSE11,  # House of friendships and collective endeavors
        const.NEPTUNE: const.HOUSE12,  # House of solitude and hidden matters
        const.PLUTO: const.HOUSE8,  # House of transformation and shared resources
        const.CHIRON: const.NO_PLANET,
        const.NORTH_NODE: const.NO_PLANET,
        const.SOUTH_NODE: const.NO_PLANET,
        const.SYZYGY: const.NO_PLANET,
        const.PARS_FORTUNA: const.NO_PLANET
    }


# -------------------- #
#   House Properties   #
# -------------------- #

class house:
    _houses = const.LIST_HOUSES

    # House conditions
    _conditions = [const.ANGULAR, const.SUCCEDENT, const.CADENT]
    condition = dict(zip(_houses, _conditions * 4))

    # House genders
    gender = dict(zip(_houses, base.genders * 4))

    # Houses above and below horizon
    aboveHorizon = [
        const.HOUSE7, const.HOUSE8, const.HOUSE9,
        const.HOUSE10, const.HOUSE11, const.HOUSE12
    ]

    belowHorizon = [
        const.HOUSE1, const.HOUSE2, const.HOUSE3,
        const.HOUSE4, const.HOUSE5, const.HOUSE6
    ]

    houseNames = {
        const.HOUSE1: const.FIRSTHOUSE,
        const.HOUSE2: const.SECONDHOUSE,
        const.HOUSE3: const.THIRDHOUSE,
        const.HOUSE4: const.FOURTHHOUSE,
        const.HOUSE5: const.FIFTHHOUSE,
        const.HOUSE6: const.SIXTHHOUSE,
        const.HOUSE7: const.SEVENTHHOUSE,
        const.HOUSE8: const.EIGHTHHOUSE,
        const.HOUSE9: const.NINETHHOUSE,
        const.HOUSE10: const.TENTHHOUSE,
        const.HOUSE11: const.ELEVENTHHOUSE,
        const.HOUSE12: const.TWELFTHOUSE
        }

    element = { 
        const.HOUSE1: const.FIRE,
        const.HOUSE2: const.EARTH,
        const.HOUSE3: const.AIR,
        const.HOUSE4: const.WATER,
        const.HOUSE5: const.FIRE,
        const.HOUSE6: const.EARTH,
        const.HOUSE7: const.AIR,
        const.HOUSE8: const.WATER,
        const.HOUSE9: const.FIRE,
        const.HOUSE10: const.EARTH,
        const.HOUSE11: const.AIR,
        const.HOUSE12: const.WATER
    }


# --------------------- #
#   Aspect Properties   #
# --------------------- #

class aspect:
    # Names
    name = {
        # Major Aspects
        const.NO_ASPECT: 'None',
        const.CONJUNCTION: 'Conjunction',
        const.SEXTILE: 'Sextile',
        const.SQUARE: 'Square',
        const.TRINE: 'Trine',
        const.OPPOSITION: 'Opposition',

        # Minor Aspects
        const.SEMISEXTILE: 'Semisextile',
        const.SEMIQUINTILE: 'Semiquintile',
        const.SEMISQUARE: 'Semisquare',
        const.QUINTILE: 'Quintile',
        const.SESQUIQUINTILE: 'Sesquiquintile',
        const.SESQUISQUARE: 'Sesquisquare',
        const.BIQUINTILE: 'Biquintile',
        const.QUINCUNX: 'Quincunx'
    }


# ------------------------- #
#   Fixed Star Properties   #
# ------------------------- #

class fixedStar:
    pass


# ------------------------- #
#   House Sys. Properties   #
# ------------------------- #

class houseSystem:
    pass
