"""
Custom creative search queries for difficult characters.
"""
from typing import List, Dict


# Custom search strategies for characters that need special handling
CUSTOM_QUERIES: Dict[str, List[str]] = {
    "WILLIAM I": [
        # Bayeux Tapestry specific scenes
        "Bayeux tapestry William Duke Normandy",
        "Tapisserie Bayeux Guillaume",
        "Bayeux embroidery William scene",
        "Bayeux tapestry 1066 William",
        "Bayeux tapestry coronation William",
        # Medieval manuscripts and seals
        "William Conqueror seal medieval",
        "Guillaume Conquérant sceau",
        "William I England seal wax",
        "William Duke Normandy manuscript illumination",
        "William Conqueror charter seal",
        # Paintings and engravings
        "William Conqueror engraving portrait",
        "Guillaume le Conquérant gravure",
        "William I England historical painting",
        "Norman invasion William portrait",
        "William Bastard Normandy portrait",
        # Battle of Hastings imagery
        "Battle Hastings 1066 William",
        "Hastings William Duke Normandy",
        "William Conqueror Hastings tapestry",
        # French language searches
        "Guillaume duc Normandie portrait",
        "Guillaume Bâtard portrait",
    ],

    "FREDERICK II": [
        "Friedrich der Große portrait",
        "Frederick II Prussia portrait",
        "Friedrich II Preußen portrait",
        "Frederick Great Prussia King",
        "Friedrich Große König Preußen",
        "Frederick II Sanssouci portrait",
        "Friedrich II Hohenzollern portrait",
        "Old Fritz portrait Prussia",
        "Friedrich der Große Gemälde",
        "Frederick II Prussia painting",
    ],

    "ISABELLA": [
        "Isabel Católica portrait Spain",
        "Isabella Catholic Monarchs Spain",
        "Isabel Castilla portrait",
        "Isabella Ferdinand Spain portrait",
        "Isabel primera Castilla portrait",
        "Isabella Catholic Queen portrait",
        "Isabel Reyes Católicos portrait",
        "Isabella Castile Aragon portrait",
        "Isabel católica España pintura",
        "Queen Isabella Spain 1492",
    ],

    "LOUIS IX": [
        "Saint Louis IX France portrait",
        "Louis IX crusade portrait",
        "Saint Louis roi France portrait",
        "Louis IX medieval manuscript",
        "Saint Louis crusader portrait",
        "Louis IX Sainte Chapelle",
        "Saint Louis France medieval art",
        "Louis IX canonized portrait",
        "Saint Louis relics portrait",
        "Louis IX crusades painting",
    ],

    "NICHOLAS I": [
        "Nicholas I Russia Tsar portrait",
        "Nikolai I Romanov portrait",
        "Nicholas I Russia Emperor",
        "Николай I portrait",
        "Nicholas I Tsar painting",
        "Nikolai Pavlovich portrait",
        "Nicholas I Russia 19th century",
        "Tsar Nicholas I Romanov",
        "Nicholas I autocrat portrait",
        "Nicholas I Russia military uniform",
    ],

    "PHILIP AUGUST": [
        "Philippe Auguste France portrait",
        "Philip II Augustus France",
        "Philippe II France roi portrait",
        "Philip Augustus medieval portrait",
        "Philippe Auguste Capétien portrait",
        "Philip II France crusade",
        "Philippe Auguste Bouvines",
        "Philip Augustus King France portrait",
        "Philippe II Auguste peinture",
        "Philip Augustus medieval manuscript",
    ],

    "STUPOR MUNDI": [
        "Frederick II Hohenstaufen portrait",
        "Friedrich II Holy Roman Emperor",
        "Frederick II Stupor Mundi portrait",
        "Federico II Svevia portrait",
        "Frederick II Sicily Emperor",
        "Friedrich II Staufer portrait",
        "Frederick II medieval emperor portrait",
        "Federico II Hohenstaufen portrait",
        "Frederick II falcon portrait",
        "Friedrich II Kaiser portrait",
    ],

    # Category S - Statesmen/Religious figures
    "ABBOT HUGH": [
        # Primary title: Abbot of Cluny
        "Abbot of Cluny portrait",
        "Abbot of Cluny medieval",
        "Abbé de Cluny portrait",
        "Cluny Abbey abbot portrait",
        "Cluny monastery abbot portrait",
        # Named searches
        "Hugh of Semur portrait",
        "Hugh Cluny abbot portrait",
        "Hugues de Semur portrait",
        "Hugh of Cluny medieval portrait",
        "Abbot Hugh Cluny painting",
        "Saint Hugh Cluny portrait",
        "Hugues de Cluny abbé portrait",
        "Hugh Semur Benedictine portrait",
        # Manuscript and illumination
        "Hugh Cluny manuscript illumination",
        "Cluny Abbey manuscript 11th century",
        "Benedictine abbot 11th century portrait",
        "Cluniac reform portrait Hugh",
        "Saint Hugh Semur medieval art",
        "Hugh of Cluny abbey portrait",
        # Historical context
        "Hugues Cluny saint portrait",
        "Hugh Semur monastery portrait",
        "Hugh Cluny Gregory VII portrait",
        "Saint Hugh Cluny France portrait",
        "Hugh Grand Abbot Cluny",
        "Hugues le Grand Cluny",
    ],

    "BECKET": [
        "Thomas Becket Canterbury portrait",
        "Saint Thomas Becket portrait",
        "Thomas à Becket medieval portrait",
        "Thomas Becket martyrdom painting",
        "Thomas Becket archbishop portrait",
        "Saint Thomas Canterbury portrait",
        "Thomas Becket murder Canterbury",
        "Thomas Becket medieval manuscript",
        "Thomas Becket saint portrait",
        "Thomas Becket Henry II portrait",
        "Thomas Becket Canterbury Cathedral",
        "Saint Thomas Becket medieval art",
        "Thomas Becket stained glass",
        "Thomas Becket shrine portrait",
        "Thomas Becket England archbishop",
    ],

    "BONIFACE VIII": [
        "Pope Boniface VIII portrait",
        "Boniface VIII papal portrait",
        "Bonifacio VIII papa portrait",
        "Pope Boniface VIII fresco",
        "Boniface VIII Giotto portrait",
        "Boniface VIII papal tiara",
        "Papa Bonifacio VIII ritratto",
        "Boniface VIII Rome portrait",
        "Pope Boniface VIII medieval",
        "Boniface VIII Gaetani portrait",
        "Boniface VIII jubilee portrait",
        "Pope Boniface VIII painting",
        "Boniface VIII Vatican portrait",
        "Bonifacio VIII affresco",
        "Boniface VIII medieval pope",
    ],

    "GREGORY VII": [
        "Pope Gregory VII portrait",
        "Gregory VII Hildebrand portrait",
        "Papa Gregorio VII ritratto",
        "Pope Gregory VII medieval portrait",
        "Gregory VII Canossa portrait",
        "Hildebrand pope portrait",
        "Gregory VII papal portrait",
        "Pope Gregory VII Henry IV",
        "Gregorio VII papa portrait",
        "Gregory VII investiture portrait",
        "Pope Gregory VII medieval art",
        "Gregory VII Hildebrand medieval",
        "Papa Gregorio VII affresco",
        "Gregory VII reform portrait",
        "Pope Gregory VII manuscript",
    ],

    "AVERROES": [
        # Primary name: Ibn Rushd
        "Ibn Rushd portrait",
        "Ibn Rushd philosopher portrait",
        "Ibn Rushd medieval portrait",
        "Ibn Rushd painting",
        "Ibn Rushd Islamic philosopher",
        # Averroes searches
        "Averroes philosopher portrait",
        "Averroes medieval portrait",
        "Averroes Islamic philosophy portrait",
        "Averroes Cordoba portrait",
        "Averroes commentator Aristotle",
        # Arabic variations
        "ابن رشد portrait",
        "Ibn Rushd al-Andalus portrait",
        "Ibn Rushd Córdoba portrait",
        # Historical context
        "Ibn Rushd 12th century portrait",
        "Averroes Andalusian philosopher",
        "Ibn Rushd judge portrait",
        "Averroes medieval manuscript",
        "Ibn Rushd Islamic Golden Age",
        "Averroes Arabic philosopher portrait",
        # Manuscript and art
        "Ibn Rushd medieval illumination",
        "Averroes medieval painting",
        "Ibn Rushd Arabic manuscript portrait",
        "Averroes scholar portrait",
    ],

    "MACHIAVELLI": [
        # Santi di Tito - the most famous portrait (Palazzo Vecchio)
        "Santi di Tito Machiavelli",
        "Machiavelli Santi di Tito painting",
        "Santi Tito Niccolò Machiavelli",
        "Machiavelli Palazzo Vecchio Santi Tito",
        # Palazzo Vecchio portrait
        "Machiavelli Palazzo Vecchio portrait",
        "Niccolò Machiavelli Palazzo Vecchio",
        "Machiavelli Florence Palazzo portrait",
        # Museum paintings
        "Machiavelli Uffizi portrait",
        "Machiavelli museum portrait painting",
        "Machiavelli Florence museum",
        # Renaissance portrait paintings
        "Machiavelli Renaissance portrait painting",
        "Machiavelli 16th century portrait painting",
        "Niccolò Machiavelli Renaissance painting",
        "Machiavelli Italian Renaissance painting",
        # Italian searches
        "Niccolò Machiavelli ritratto Santi Tito",
        "Machiavelli ritratto Palazzo Vecchio",
        "Niccolò Machiavelli dipinto Firenze",
        "Machiavelli ritratto storico",
        # Historical portrait terms
        "Machiavelli historical portrait painting",
        "Machiavelli authentic portrait",
        "Machiavelli contemporary portrait",
        "Machiavelli oil painting portrait",
        # Specific artwork searches
        "Machiavelli bust sculpture",
        "Machiavelli statue Florence",
    ],
}


def get_custom_queries(character_name: str) -> List[str]:
    """
    Get custom search queries for a character.

    Args:
        character_name: Name of the character (e.g., "WILLIAM I")

    Returns:
        List of custom search queries, or empty list if no custom queries
    """
    return CUSTOM_QUERIES.get(character_name.upper(), [])
