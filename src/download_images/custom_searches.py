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

    "OCKHAM": [
        # William of Ockham variations
        "William Ockham portrait",
        "William Occam philosopher portrait",
        "Guilelmus de Ockham portrait",
        "Guillaume d'Ockham portrait",
        "William of Ockham medieval portrait",
        "William of Occam portrait",
        # Franciscan context
        "Ockham Franciscan portrait",
        "William Ockham friar portrait",
        "Ockham Franciscan medieval portrait",
        "William Occam Franciscan order",
        # Razor/philosophy context
        "Occam razor philosopher portrait",
        "Ockham razor portrait",
        "William Ockham nominalism portrait",
        "Ockham scholastic philosopher portrait",
        # Medieval art forms
        "William of Ockham manuscript illumination",
        "Ockham medieval manuscript portrait",
        "William Ockham medieval painting",
        "Ockham medieval fresco",
        # Latin variations
        "Guillelmus Occamus portrait",
        "Gulielmus de Ockham portrait",
        "Guilelmus Occam portrait",
        # Historical context
        "William Ockham 14th century portrait",
        "Ockham philosopher medieval art",
        "William of Ockham England portrait",
        "Ockham Surrey friar portrait",
    ],

    "SMITH": [
        # Adam Smith economist
        "Adam Smith economist portrait",
        "Adam Smith 1723 portrait",
        "Adam Smith philosopher portrait",
        "Adam Smith Scotland portrait",
        # Famous works context
        "Adam Smith Wealth of Nations portrait",
        "Adam Smith Theory Moral Sentiments portrait",
        "Adam Smith invisible hand portrait",
        # Scottish Enlightenment
        "Adam Smith Scottish Enlightenment portrait",
        "Adam Smith Edinburgh portrait",
        "Adam Smith Glasgow portrait",
        "Adam Smith Scotland philosopher",
        # Art forms
        "Adam Smith medallion portrait",
        "Adam Smith engraving portrait",
        "Adam Smith oil painting portrait",
        "Adam Smith bust sculpture",
        # Museum holdings
        "Adam Smith National Portrait Gallery",
        "Adam Smith Scottish National Gallery",
        "Adam Smith museum portrait",
        # Historical portraits
        "Adam Smith 18th century portrait",
        "Adam Smith James Tassie portrait",
        "Adam Smith John Kay portrait",
        "Adam Smith historical painting",
        # University context
        "Adam Smith University Glasgow portrait",
        "Adam Smith professor portrait",
        "Adam Smith academic portrait",
    ],

    "FERMI": [
        # University of Chicago archives - primary source
        "Enrico Fermi University Chicago archive photograph",
        "Enrico Fermi Photographic Archive Chicago",
        "Enrico Fermi metallurgical laboratory Chicago",
        # Manhattan Project photos
        "Enrico Fermi Manhattan Project photograph",
        "Enrico Fermi Chicago Pile 1942",
        "Enrico Fermi Argonne National Laboratory",
        "Enrico Fermi atomic pile photograph",
        # Nobel Prize context
        "Enrico Fermi Nobel Prize 1938 photograph",
        "Enrico Fermi Nobel laureate portrait",
        # Professor photos
        "Enrico Fermi professor physics photograph",
        "Enrico Fermi lecture photograph",
        "Enrico Fermi laboratory photograph 1940s",
        # Italian period
        "Enrico Fermi Rome University photograph",
        "Enrico Fermi fisico italiano fotografia",
        # Historical archive photos
        "Enrico Fermi 1930s portrait photograph",
        "Enrico Fermi 1940s portrait photograph",
        "Enrico Fermi official photograph",
        "Enrico Fermi portrait formal",
    ],

    "FIBONACCI": [
        # Giovanni Paganucci statue (1863) - main source
        "Fibonacci Giovanni Paganucci statue 1863",
        "Leonardo Fibonacci Paganucci sculpture",
        "Fibonacci statue Camposanto Pisa",
        "Leonardo Pisano statue Pisa cemetery",
        # Camposanto location
        "Fibonacci Camposanto monumentale Pisa",
        "Leonardo Fibonacci Piazza Miracoli",
        "Fibonacci statue western gallery Camposanto",
        # Engraved portraits (post-medieval)
        "Leonardo Fibonacci engraved portrait",
        "Leonardo Pisano engraving portrait",
        "Fibonacci 19th century engraving",
        "Leonardo Fibonacci copper engraving",
        # Italian references
        "Leonardo Fibonacci statua Pisa",
        "Fibonacci ritratto incisione",
        "Leonardo Pisano monumento",
        # Historical depictions
        "Fibonacci mathematician medieval depiction",
        "Leonardo Fibonacci Liber Abaci illustration",
        "Fibonacci medieval manuscript illustration",
        "Leonardo Pisano historical portrait",
        # Modern artistic renditions
        "Fibonacci portrait illustration",
        "Leonardo Fibonacci artistic portrait",
        "Fibonacci mathematician portrait drawing",
    ],

    "MAXWELL": [
        # William Dyce portrait (1833) - early portrait
        "James Clerk Maxwell William Dyce portrait 1833",
        "Maxwell Dyce painting Birmingham museum",
        "James Maxwell Mrs John Clerk Maxwell Dyce",
        # Lowes Cato Dickinson portrait
        "James Clerk Maxwell Lowes Cato Dickinson",
        "Maxwell Dickinson portrait Trinity College Cambridge",
        "James Maxwell Trinity College portrait",
        # National Portrait Gallery
        "James Clerk Maxwell National Portrait Gallery",
        "Maxwell George Stodart engraving",
        "James Clerk Maxwell John Fergus portrait",
        "Maxwell NPG portrait",
        # Scottish collections
        "James Clerk Maxwell Scottish National Portrait Gallery",
        "Maxwell Alexander Stoddart sculpture",
        "James Maxwell Edinburgh portrait",
        # General searches
        "James Clerk Maxwell physicist portrait 1870s",
        "James Clerk Maxwell photograph",
        "Maxwell Cambridge physicist portrait",
        "James Clerk Maxwell formal portrait",
        "James Maxwell scientist photograph",
    ],

    "PARACELSUS": [
        # Augustin Hirschvogel woodcut (1538) - earliest known
        "Paracelsus Augustin Hirschvogel 1538 woodcut",
        "Theophrastus Paracelsus Hirschvogel portrait",
        "Paracelsus 1538 portrait woodcut",
        # Quentin Matsys painting (copies)
        "Paracelsus Quentin Matsys portrait",
        "Theophrastus Paracelsus Matsys painting",
        "Paracelsus Louvre portrait Flemish",
        "Paracelsus 16th century portrait copy",
        # Holding sword by pommel (characteristic pose)
        "Paracelsus portrait holding sword pommel",
        "Theophrastus Paracelsus sword portrait",
        "Paracelsus standing sword portrait",
        # Pieter Soutman portrait (1615-43)
        "Paracelsus Pieter Soutman portrait",
        "Theophrastus Paracelsus Soutman 1615",
        # General 16th century portraits
        "Paracelsus 16th century engraving",
        "Theophrastus Bombastus von Hohenheim portrait",
        "Paracelsus Renaissance portrait",
        "Paracelsus physician alchemist portrait",
        "Paracelsus motto portrait Alterius non sit",
    ],

    "ROENTGEN": [
        # Nicola Perscheid photograph (1915)
        "Wilhelm Röntgen Nicola Perscheid 1915",
        "Roentgen Perscheid portrait photograph",
        "Wilhelm Conrad Röntgen Perscheid photo",
        # Nobel Prize 1901 photographs
        "Wilhelm Röntgen Nobel Prize 1901 photograph",
        "Roentgen Nobel laureate portrait",
        "Wilhelm Röntgen Nobel Prize portrait",
        # X-ray discovery context
        "Wilhelm Röntgen X-ray discovery portrait",
        "Roentgen physicist portrait photograph",
        "Wilhelm Conrad Röntgen laboratory photograph",
        # University affiliations
        "Wilhelm Röntgen Würzburg University portrait",
        "Roentgen professor portrait photograph",
        # German variations
        "Wilhelm Conrad Röntgen Fotografie",
        "Röntgen Physiker Portrait",
        # General photographs
        "Wilhelm Röntgen formal portrait photograph",
        "Roentgen 1900s photograph",
        "Wilhelm Röntgen official photograph",
    ],

    "RUTHERFORD": [
        # Sir James Gunn painting (1932)
        "Ernest Rutherford James Gunn 1932 portrait",
        "Rutherford Gunn oil painting NPG 2935",
        "Lord Rutherford James Gunn portrait",
        # William Rothenstein portrait
        "Ernest Rutherford William Rothenstein portrait",
        "Rutherford Rothenstein NPG 4793",
        # Francis Dodd portrait
        "Ernest Rutherford Francis Dodd portrait",
        "Rutherford Dodd NPG 4426",
        # Walter Stoneman photograph (1921)
        "Ernest Rutherford Walter Stoneman 1921",
        "Rutherford Stoneman photograph NPG",
        # Ramsey & Muspratt (1937)
        "Ernest Rutherford Ramsey Muspratt 1937",
        "Rutherford bromide print 1937",
        # National Portrait Gallery
        "Ernest Rutherford National Portrait Gallery",
        "Lord Rutherford Baron portrait",
        # General physicist portraits
        "Ernest Rutherford physicist portrait",
        "Rutherford Nobel Prize portrait",
        "Ernest Rutherford Cambridge portrait",
        "Lord Rutherford formal portrait",
    ],

    "WATSON": [
        # James Dewey Watson (note: different from James Watson the 19th century character!)
        # This might be the wrong Watson - let me check the dates
        "James Watson 1872 photograph",
        "James Watson 19th century portrait",
        "James Watson scientist 1870s photograph",
        # General Victorian era searches
        "James Watson Victorian scientist photograph",
        "James Watson physicist 1870s portrait",
        "James Watson formal portrait photograph",
        # Archive photographs
        "James Watson scientist portrait archive",
        "James Watson historical photograph",
        "James Watson 1900 portrait",
        # British scientist context
        "James Watson British scientist portrait",
        "James Watson physicist photograph Victorian",
    ],

    "AGRICOLA": [
        # Georgius Agricola - German scholar, mineralogist, father of mineralogy
        # Full name: Georg Bauer (Latinized to Georgius Agricola)
        "Georgius Agricola mineralogist portrait",
        "Georg Bauer Agricola portrait",
        "Georgius Agricola De Re Metallica portrait",
        "Agricola 16th century German scholar portrait",
        # Latin name variations
        "Georgius Agricola physician portrait",
        "Georg Agricola Renaissance scholar portrait",
        "Georgius Agricola Saxony portrait",
        "Agricola Chemnitz scholar portrait",
        # Works and titles
        "Georgius Agricola father mineralogy portrait",
        "Agricola De Re Metallica author portrait",
        "Georg Agricola mining scholar portrait",
        "Georgius Agricola metallurgy portrait",
        # German variations
        "Georg Bauer Agricola Gelehrter Portrait",
        "Georgius Agricola deutscher Gelehrter",
        "Agricola Bergbau Portrait",
        # Renaissance context
        "Georgius Agricola Renaissance portrait engraving",
        "Agricola 1550 portrait woodcut",
        "Georg Agricola humanist portrait",
        "Georgius Agricola physician Chemnitz portrait",
        # Historical art
        "Georgius Agricola woodcut portrait",
        "Agricola copper engraving portrait",
        "Georg Agricola book frontispiece portrait",
    ],

    "BACON, ROGER": [
        # Roger Bacon - English philosopher and Franciscan friar (c. 1219-1292)
        # Known as "Doctor Mirabilis" (Wonderful Teacher)
        "Roger Bacon Doctor Mirabilis portrait",
        "Roger Bacon Franciscan friar portrait",
        "Roger Bacon philosopher medieval portrait",
        "Roger Bacon Doctor Mirabilis medieval",
        # Franciscan context
        "Roger Bacon Franciscan medieval manuscript",
        "Roger Bacon friar Oxford portrait",
        "Roger Bacon Opus Majus portrait",
        # Experimental science context
        "Roger Bacon experimental science portrait",
        "Roger Bacon medieval scientist portrait",
        "Roger Bacon alchemist portrait",
        "Roger Bacon optics medieval portrait",
        # Medieval art forms
        "Roger Bacon medieval illumination",
        "Roger Bacon manuscript portrait 13th century",
        "Roger Bacon medieval fresco portrait",
        "Roger Bacon stained glass portrait",
        # Latin variations
        "Rogerus Bacon portrait",
        "Rogerus Baco medieval portrait",
        # Historical depictions
        "Roger Bacon laboratory medieval painting",
        "Roger Bacon scholar medieval portrait",
        "Roger Bacon Oxford medieval portrait",
        "Roger Bacon 13th century philosopher portrait",
        # French variations
        "Roger Bacon philosophe médiéval portrait",
        "Roger Bacon Docteur Admirable portrait",
    ],

    "ALHAZEN": [
        # Ibn al-Haytham (Alhazen) - Arab mathematician, physicist, astronomer (c. 965-1040)
        # Father of modern optics, Book of Optics
        "Ibn al-Haytham portrait",
        "Alhazen Ibn al-Haytham portrait",
        "Ibn Haytham Islamic scientist portrait",
        "Alhazen optics portrait",
        # Arabic name variations
        "Ibn al-Haytham physicist portrait",
        "Alhacen medieval portrait",
        "Al-Hazen portrait",
        "Abu Ali al-Hasan ibn al-Haytham portrait",
        # Book of Optics context
        "Ibn al-Haytham Kitab al-Manazir portrait",
        "Alhazen Book of Optics portrait",
        "Ibn Haytham optics manuscript portrait",
        # Islamic Golden Age
        "Ibn al-Haytham Islamic Golden Age portrait",
        "Alhazen Arab physicist portrait",
        "Ibn Haytham Basra scholar portrait",
        "Alhazen Cairo scientist portrait",
        # Medieval manuscript illustrations
        "Ibn al-Haytham medieval manuscript illustration",
        "Alhazen medieval Islamic art portrait",
        "Ibn Haytham Arabic manuscript portrait",
        "Alhazen camera obscura portrait",
        # Scientific context
        "Ibn al-Haytham mathematician portrait",
        "Alhazen astronomer portrait",
        "Ibn Haytham father of optics portrait",
        "Alhazen experimental method portrait",
        # Historical depictions
        "Ibn al-Haytham miniature portrait",
        "Alhazen medieval scientist illustration",
        "Ibn Haytham historical portrait painting",
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
