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
        "James Dewey Watson photograph",
        "James D. Watson 20th century portrait",
        "James D. Watson scientist photograph",
        # Archive photographs
        "James D. Watson scientist portrait archive",
        "James D. Watson historical photograph",
        "James D. Watson double helix"
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

    # Object-based representations for inventors
    "BELL": [
        # Alexander Graham Bell - represented by original telephone
        "Bell telephone 1876 original patent",
        "Alexander Graham Bell telephone prototype 1876",
        "Bell telephone original invention museum",
        "first telephone Alexander Graham Bell 1876",
        "Bell telephone patent model Smithsonian",
        "Alexander Bell telephone invention 1876",
        "Bell liquid transmitter telephone 1876",
        "original Bell telephone receiver transmitter",
        "Bell telephone Centennial Exhibition 1876",
        "Alexander Graham Bell telephone replica museum",
        "Bell telephone historical artifact",
        "first working telephone Bell 1876",
        "Bell telephone electromagnet receiver",
        "Alexander Bell gallows telephone 1876",
        "Bell telephone patent drawing telephone",
    ],

    "BRUNEL": [
        # Isambard Kingdom Brunel - represented by engineering projects
        "Clifton Suspension Bridge Bristol Brunel",
        "Great Eastern steamship Brunel",
        "SS Great Britain ship Brunel",
        "Royal Albert Bridge Saltash Brunel",
        "Great Western Railway Brunel",
        "Thames Tunnel Brunel engineering",
        "Maidenhead Railway Bridge Brunel",
        "Box Tunnel Brunel railway",
        "Brunel railway bridge engineering",
        "Great Western steamship Brunel",
        "Brunel suspension bridge chains",
        "Paddington Station Brunel",
        "Brunel viaduct railway bridge",
        "Wharncliffe Viaduct Brunel",
        "Brunel atmospheric railway",
    ],

    "EDISON": [
        # Thomas Edison - represented by original incandescent bulb
        "Edison light bulb 1879 original",
        "Thomas Edison incandescent lamp 1879",
        "Edison carbon filament bulb original",
        "first Edison light bulb museum",
        "Edison Menlo Park light bulb 1879",
        "Edison bamboo filament lamp",
        "original Edison incandescent bulb patent",
        "Edison light bulb invention 1879",
        "Edison lamp carbon filament glass",
        "Thomas Edison light bulb replica museum",
        "Edison incandescent lamp Smithsonian",
        "Edison bulb vacuum glass 1879",
        "first practical light bulb Edison",
        "Edison lamp invention demonstration",
        "Edison electric lamp 1879 patent",
    ],

    "DAGUERRE": [
        # Louis Daguerre - represented by daguerreotype/camera
        "daguerreotype camera original 1839",
        "Louis Daguerre camera invention",
        "first daguerreotype camera museum",
        "Daguerre camera obscura 1839",
        "daguerreotype process camera equipment",
        "Giroux daguerreotype camera 1839",
        "original Daguerre camera apparatus",
        "Susse Frères daguerreotype camera",
        "early daguerreotype camera brass",
        "Daguerre invention camera photography",
        "daguerreotype plate camera historical",
        "Daguerre photography equipment 1839",
        "first commercial camera Daguerre",
        "daguerreotype camera lens 19th century",
        "Daguerre Niépce camera invention",
    ],

    "GUTENBERG": [
        # Johannes Gutenberg - represented by printing press/Bible
        "Gutenberg printing press original",
        "Gutenberg Bible 42-line manuscript",
        "Johannes Gutenberg press replica museum",
        "Gutenberg Bible page illuminated",
        "moveable type Gutenberg invention",
        "Gutenberg press 15th century",
        "Gutenberg Bible Mainz original",
        "printing press Gutenberg museum",
        "Gutenberg type metal letters",
        "Gutenberg Bible two column page",
        "Johannes Gutenberg press woodcut",
        "Gutenberg printing workshop illustration",
        "Gutenberg Bible manuscript page",
        "printing press 1450 Gutenberg",
        "Gutenberg moveable type invention",
    ],

    "GROSSETESTE": [
        # Robert Grosseteste - represented by medieval works/optics
        "medieval manuscript illumination 13th century Oxford",
        "medieval optical diagram light refraction",
        "Robert Grosseteste manuscript medieval",
        "medieval rainbow optics diagram",
        "13th century scientific manuscript",
        "medieval light refraction illustration",
        "Grosseteste optical works manuscript",
        "medieval astronomy diagram 13th century",
        "Oxford medieval manuscript illumination",
        "medieval scientific treatise illustration",
        "13th century Bishop manuscript portrait",
        "medieval optics light rays diagram",
        "Robert Grosseteste works medieval art",
        "medieval natural philosophy manuscript",
        "Lincoln Cathedral medieval bishop",
    ],

    "PEREGRINUS": [
        # Petrus Peregrinus (Pierre de Maricourt) - 13th century scholar, magnetism pioneer
        # Portrait and manuscript searches
        "Petri Peregrini Maricurtensis",
        "Pierre Pelerin de Maricourt",
        "Petrus Peregrinus magents",
        "Epistola Petri Peregrini de Maricourt ad Sygerum de Foucaucourt",
        "Peregrinus de Maricourt manuscript",
    ],

    "STEPHENSON": [
        # George Stephenson - represented by locomotive/railway
        "Stephenson Rocket locomotive original",
        "George Stephenson Rocket steam engine",
        "Stephenson locomotive 1829 museum",
        "Rocket locomotive Rainhill trials",
        "George Stephenson railway engine",
        "Stephenson steam locomotive replica",
        "Rocket engine Science Museum London",
        "Stephenson locomotive Stockton Darlington",
        "early steam locomotive Stephenson",
        "George Stephenson Rocket patent",
        "Stephenson railway engine 1825",
        "Locomotion No 1 Stephenson",
        "Stephenson steam engine invention",
        "railway locomotive George Stephenson",
        "Stephenson Rocket historical photograph",
    ],

    "MERCATOR": [
        # Gerardus Mercator - cartographer, famous for Mercator projection (1512-1594)
        # Portrait searches
        "Gerardus Mercator portrait",
        "Gerard Mercator cartographer portrait",
        "Mercator 16th century portrait",
        "Gerardus Mercator engraving portrait",
        # Famous world maps - signature works
        "Mercator projection world map 1569",
        "Gerardus Mercator Nova et Aucta Orbis Terrae",
        "Mercator world map 1569 original",
        "Mercator Ad Usum Navigantium map 1569",
        "Gerardus Mercator world map double hemisphere",
        # Atlas and cartographic works
        "Mercator atlas cosmographicae meditations",
        "Gerardus Mercator atlas 1595",
        "Mercator historical atlas pages",
        "Mercator Duisburg atlas map",
        # Map projection - signature achievement
        "Mercator projection cylindrical map",
        "Mercator projection navigation chart",
        "Mercator conformal projection map",
        "Gerardus Mercator nautical chart",
        # Globe works
        "Gerardus Mercator terrestrial globe 1541",
        "Mercator celestial globe 1551",
        "Mercator globe pair terrestrial celestial",
        # General cartographic context
        "Gerardus Mercator cartography 16th century",
        "Mercator map maker portrait",
        "Gerard Mercator mathematician portrait",
        "Mercator Flemish cartographer portrait",
        # Portrait with maps/instruments
        "Gerardus Mercator portrait globe",
        "Mercator portrait compass cartography",
    ],

    "TOWNES": [
        # Charles Hard Townes - physicist, inventor of maser/laser (1915-2015)
        # Portrait searches
        "Charles Townes physicist portrait",
        "Charles Hard Townes portrait",
        "Charles H Townes physicist ",
        "Charles Townes scientist portrait",
        # Maser device - signature invention (1954)
        "maser device original 1954",
        "first maser apparatus ",
        "Townes maser device Columbia",
        "ammonia maser Townes 1954",
        "maser microwave amplification device",
        "Charles Townes first maser ",
        "maser apparatus original design",
        # Maser/laser achievements with portrait
        "Charles Townes maser inventor portrait",
        "Charles Townes laser inventor portrait",
        "Townes maser invention ",
        "Charles Townes laser physics portrait",
        "Townes maser Nobel Prize portrait",
        # Nobel Prize context (1964)
        "Charles Townes Nobel Prize 1964 portrait",
        "Charles Townes Nobel laureate",
        "Townes Nobel Prize physics portrait",
        "Charles Townes Nobel Prize ceremony ",
        # Columbia University context
        "Charles Townes Columbia University portrait",
        "Townes Columbia physicist ",
        "Charles Townes professor physics portrait",
        # Berkeley period
        "Charles Townes UC Berkeley portrait",
        "Townes Berkeley professor ",
        "Charles Townes University California portrait",
        # Laser/maser with apparatus
        "Charles Townes laboratory ",
        "Townes maser apparatus ",
        "Charles Townes laser laboratory portrait",
        "Townes physics experiment ",
        # Historical archive photos
        "Charles Townes 1950s ",
        "Charles Townes 1960s portrait",
        "Townes physicist archive ",
        "Charles Townes official portrait ",
    ],

    "VOLTA": [
        # Alessandro Volta - physicist, inventor of electric battery (1745-1827)
        # Portrait searches
        "Alessandro Volta portrait",
        "Alessandro Giuseppe Antonio Anastasio Volta portrait",
        "Volta physicist portrait",
        "Alessandro Volta 18th century portrait",
        # Voltaic pile - signature invention
        "Alessandro Volta voltaic pile portrait",
        "Volta electric battery invention portrait",
        "Alessandro Volta battery inventor portrait",
        "Volta voltaic pile demonstration portrait",
        "Alessandro Volta electricity portrait",
        # Famous demonstrations
        "Alessandro Volta Napoleon demonstration portrait",
        "Volta Institut de France portrait",
        "Alessandro Volta Paris demonstration portrait",
        "Volta electric battery Napoleon portrait",
        # Paintings and engravings
        "Alessandro Volta portrait painting",
        "Volta engraving portrait",
        "Alessandro Volta oil painting portrait",
        "Volta Italian physicist portrait",
        # University of Pavia context
        "Alessandro Volta University Pavia portrait",
        "Volta Pavia professor portrait",
        "Alessandro Volta Como portrait",
        # Italian variations
        "Alessandro Volta ritratto",
        "Volta fisico italiano ritratto",
        "Alessandro Volta ritratto storico",
        # Medals and honors
        "Alessandro Volta medal portrait",
        "Volta Copley Medal portrait",
        # With voltaic pile/apparatus
        "Alessandro Volta portrait voltaic pile",
        "Volta portrait electrical apparatus",
        "Alessandro Volta laboratory portrait",
    ],

    "WRIGHT W&O": [
        # Wilbur and Orville Wright - aviation pioneers, first powered flight (1903)
        # Portrait searches - both brothers
        "Wright Brothers portrait",
        "Wilbur Orville Wright portrait",
        "Wright Brothers aviation pioneers portrait",
        "Wilbur and Orville Wright photograph",
        # Kitty Hawk imagery - signature achievement location
        "Kitty Hawk North Carolina 1903",
        "Kitty Hawk first flight photograph",
        "Kill Devil Hills Wright Brothers",
        "Kitty Hawk sand dunes 1903",
        "Wright Brothers camp Kitty Hawk",
        "Kitty Hawk Wright Flyer takeoff",
        "historic Kitty Hawk flight photograph",
        # First flight - signature achievement
        "Wright Brothers first flight 1903 photograph",
        "Wright Brothers Kitty Hawk 1903 photograph",
        "Wilbur Wright first flight portrait",
        "Orville Wright first flight photograph",
        "Wright Brothers December 17 1903 photograph",
        # Wright Flyer aircraft
        "Wright Brothers Wright Flyer photograph",
        "Wright Brothers airplane 1903 photograph",
        "Wright Flyer Kitty Hawk photograph",
        "Wright Brothers aircraft photograph",
        # Kitty Hawk context with people
        "Wright Brothers Kitty Hawk portrait",
        "Wilbur Wright North Carolina photograph",
        "Orville Wright Kill Devil Hills photograph",
        "Wright Brothers Outer Banks photograph",
        # Together portrait
        "Wilbur and Orville Wright together portrait",
        "Wright Brothers bicycle shop portrait",
        "Wright Brothers Dayton Ohio portrait",
        "Wright Brothers workshop photograph",
        # Flight demonstrations
        "Wright Brothers flight demonstration photograph",
        "Wilbur Wright flying photograph",
        "Orville Wright pilot photograph",
        "Wright Brothers aviation photograph",
        # Archive photographs
        "Wright Brothers Library Congress photograph",
        "Wright Brothers historical photograph",
        "Wright Brothers official portrait",
        "Wright Brothers archive photograph",
        # Individual portraits
        "Wilbur Wright portrait photograph",
        "Orville Wright portrait photograph",
    ],

    "LEAKEY": [
        # Louis Leakey - paleoanthropologist, signature works at Olduvai Gorge
        # Portrait searches
        "Louis Leakey paleoanthropologist portrait",
        "Louis Leakey archaeologist photograph",
        "Louis Leakey Kenya portrait photograph",
        "Louis Leakey anthropologist portrait",
        # Olduvai Gorge context
        "Louis Leakey Olduvai Gorge photograph",
        "Louis Leakey Tanzania excavation photograph",
        "Louis Leakey fossil discovery photograph",
        "Louis Leakey Olduvai site photograph",
        "Louis Leakey excavation Olduvai portrait",
        # Fossil discoveries - signature works
        "Louis Leakey Zinjanthropus discovery photograph",
        "Louis Leakey Nutcracker Man skull photograph",
        "Louis Leakey Homo habilis discovery photograph",
        "Louis Leakey Olduvai Gorge skull photograph",
        "Louis Leakey fossil hominid discovery",
        # Field work photographs
        "Louis Leakey field work Kenya photograph",
        "Louis Leakey excavation site photograph",
        "Louis Leakey Mary Leakey Olduvai photograph",
        "Louis Leakey digging fossil photograph",
        "Louis Leakey archaeologist field photograph",
        # National Geographic context
        "Louis Leakey National Geographic photograph",
        "Louis Leakey National Geographic portrait",
        # Academic/professional photos
        "Louis Leakey professor photograph",
        "Louis Leakey scientist portrait photograph",
        "Louis Leakey lecture photograph",
        # Historical archive photos
        "Louis Leakey 1960s photograph",
        "Louis Leakey 1950s photograph",
        "Louis Leakey archive photograph",
        "Louis Leakey historical photograph",
    ],

    "LEEUWENHOEK": [
        # Antonie van Leeuwenhoek - microscopist, signature work with microscopes
        # Portrait with microscope
        "Antonie van Leeuwenhoek microscope portrait",
        "Leeuwenhoek microscope painting portrait",
        "Anton van Leeuwenhoek with microscope",
        "Leeuwenhoek microscope inventor portrait",
        # Microscope focus - signature work
        "Leeuwenhoek microscope original",
        "Antonie van Leeuwenhoek microscope design",
        "Leeuwenhoek single lens microscope",
        "van Leeuwenhoek microscope apparatus",
        "Leeuwenhoek microscope scientific instrument",
        # Historical portraits
        "Antonie van Leeuwenhoek portrait painting",
        "Anton van Leeuwenhoek 17th century portrait",
        "Leeuwenhoek Dutch scientist portrait",
        "Antonie Philips van Leeuwenhoek portrait",
        # Verkolje portrait (famous 1686 painting)
        "Leeuwenhoek Verkolje portrait 1686",
        "Jan Verkolje Leeuwenhoek painting",
        "Antonie van Leeuwenhoek Verkolje painting",
        # Dutch variations
        "Antonie van Leeuwenhoek portret",
        "Leeuwenhoek microscopist portret",
        # Scientific context
        "Leeuwenhoek microbiologist portrait",
        "van Leeuwenhoek scientist Delft portrait",
        "Leeuwenhoek Royal Society portrait",
    ],

    "LIVINGSTONE": [
        # David Livingstone - explorer, signature work Victoria Falls discovery
        # Portrait searches
        "David Livingstone explorer portrait",
        "David Livingstone missionary portrait",
        "David Livingstone Scotland portrait",
        "David Livingstone Africa explorer portrait",
        # Victoria Falls context - signature discovery
        "David Livingstone Victoria Falls portrait",
        "Livingstone Victoria Falls discovery",
        "David Livingstone Mosi-oa-Tunya portrait",
        "Livingstone Victoria Falls 1855 portrait",
        "David Livingstone waterfall discovery portrait",
        # Exploration context
        "David Livingstone Africa expedition portrait",
        "Livingstone Zambezi expedition portrait",
        "David Livingstone explorer Africa photograph",
        "Livingstone missionary explorer portrait",
        # Famous Stanley meeting
        "David Livingstone Stanley meeting portrait",
        "Livingstone I presume portrait",
        "David Livingstone Henry Stanley portrait",
        # Historical portraits and photographs
        "David Livingstone 19th century portrait",
        "David Livingstone photograph 1850s",
        "David Livingstone photograph 1860s",
        "David Livingstone formal portrait photograph",
        # London Missionary Society
        "David Livingstone missionary portrait photograph",
        "Livingstone LMS portrait",
        "David Livingstone Royal Geographical Society",
    ],

    "MARCO POLO": [
        # Marco Polo - Venetian explorer, traveler on the Silk Road
        # Medieval portrait searches
        "Marco Polo medieval portrait painting",
        "Marco Polo Venetian explorer portrait",
        "Marco Polo 13th century portrait",
        "Marco Polo traveler portrait medieval",
        # Kublai Khan context - his famous patron
        "Marco Polo Kublai Khan court portrait",
        "Marco Polo Yuan dynasty portrait",
        "Marco Polo China Kublai Khan painting",
        "Marco Polo Mongol court portrait",
        "Marco Polo Great Khan portrait",
        # Silk Road and journey context
        "Marco Polo Silk Road portrait",
        "Marco Polo journey Asia portrait",
        "Marco Polo travels China portrait",
        "Marco Polo Cathay portrait",
        "Marco Polo caravan portrait",
        # Book of Travels / Il Milione context
        "Marco Polo Il Milione portrait",
        "Marco Polo Travels manuscript portrait",
        "Marco Polo book portrait medieval",
        "Marco Polo Devisement du Monde portrait",
        # Venice context
        "Marco Polo Venice portrait",
        "Marco Polo Venetian merchant portrait",
        "Marco Polo Repubblica Venezia portrait",
        # Italian variations
        "Marco Polo ritratto medievale",
        "Marco Polo veneziano ritratto",
        "Marco Polo esploratore ritratto",
        # Historical depictions
        "Marco Polo medieval manuscript illumination",
        "Marco Polo medieval painting portrait",
        "Marco Polo historical portrait 14th century",
        "Marco Polo Renaissance portrait",
    ],
    
    "DUFAY": [
        "Du Fay (left) beside a portative organ, with Gilles Binchois (right) holding a small harp",
        "Du Fay portrait",
        "Du Fay composer portrait",
        "Guillaume Du Fay portrait",
    ],

    "JOSQUIN": [
        "Josquin des Prez portrait",
        "Josquin composer portrait",
        "Josquin des Prez music manuscript portrait",
    ],
    
    "GUIDO OF AREZZO": [
        "Guido of Arezzo medieval portrait",
        "Guido Aretinus portrait",
        "Guido of Arezzo music notation",
    ],
    
    "LEONIN": [
        "Leonin medieval portrait",
        "Perotin",
        "Perotin manuscript",
        "Leonin and Perotin",
        "Medieval polyphonism",
    ],

    "MACHAUT": [
        "Guillaume de Machaut portrait",
        "Machaut composer portrait",
        "Machaut medieval music manuscript",
        "Motets of Machaut",
    ],
    
    "MORLEY": [
        "Thomas Morley portrait",
        "Morley composer portrait",
        "Thomas Morley music manuscript",
    ],
    
    "PALESTRINA": [
        "Giovanni Pierluigi da Palestrina portrait",
        "Palestrina composer portrait",
        "Palestrina choral music manuscript",
    ],
    
    "PURCELL": [
        "Henry Purcell portrait",
        "Purcell composer portrait",
        "Henry Purcell music manuscript",
    ],
    
    "STOCKHAUSEN": [
        "Karlheinz Stockhausen portrait",
        "Stockhausen composer portrait",
        "Stockhausen music manuscript",
    ], 
    
    "SHUETZ": [
        "Heinrich Schütz portrait",
        "Schütz composer portrait",
        "Heinrich Schütz music manuscript", 
    ],
    
    "VENTADORN": [
        "Bernart de Ventadorn portrait",
        "Ventadorn troubadour portrait",
        "Bernart de Ventadorn music manuscript",
        "Bernart chansonier",
    ],

    # Category A - Artists (focus on iconic works, then portraits)
    "BERNINI": [
        # Most iconic sculptures
        "Ecstasy of Saint Teresa Bernini sculpture",
        "Gian Lorenzo Bernini Ecstasy Saint Teresa",
        "Bernini Teresa Avila sculpture Santa Maria Victoria",
        "Bernini Apollo Daphne sculpture Borghese",
        "Apollo and Daphne Bernini marble",
        "Gian Lorenzo Bernini Apollo Daphne transformation",
        "Bernini David sculpture Borghese",
        "David Bernini marble sculpture",
        "Bernini Pluto Proserpina sculpture",
        "Rape of Proserpina Bernini Borghese",
        # Fountains
        "Bernini Fountain Four Rivers Rome",
        "Fontana dei Quattro Fiumi Bernini",
        "Bernini Triton Fountain Rome",
        "Fontana del Tritone Bernini",
        # St Peter's works
        "Bernini Baldachin St Peter's Basilica",
        "Baldacchino Bernini Vatican bronze",
        "Bernini Cathedra Petri St Peter",
        "Bernini colonnade St Peter's Square",
        # Portrait busts
        "Bernini Bust Costanza Bonarelli",
        "Gian Lorenzo Bernini self portrait",
        # Portrait searches (fallback)
        "Gian Lorenzo Bernini portrait painting",
        "Bernini baroque sculptor portrait",
    ],

    "CEZANNE": [
        # Mont Sainte-Victoire series - most iconic
        "Cézanne Mont Sainte-Victoire painting",
        "Paul Cézanne Mont Sainte-Victoire",
        "Cezanne Montagne Sainte-Victoire",
        "Cézanne Mont Sainte-Victoire series",
        "Paul Cézanne Montagne Sainte-Victoire oil painting",
        # Card Players series
        "Cézanne Card Players painting",
        "Paul Cézanne Les Joueurs de cartes",
        "Cezanne Card Players series",
        "The Card Players Cézanne",
        # Bathers series
        "Cézanne Large Bathers painting",
        "Paul Cézanne Les Grandes Baigneuses",
        "Cezanne Bathers Philadelphia Museum",
        "Cézanne Bathers series painting",
        # Still life
        "Cézanne Still Life with Apples",
        "Paul Cézanne nature morte pommes",
        "Cezanne Basket of Apples painting",
        # Portrait (fallback)
        "Paul Cézanne self portrait painting",
        "Cezanne portrait photograph",
        "Paul Cézanne French painter portrait",
    ],

    "CHARTRES": [
        # Chartres Cathedral - the work itself
        "Chartres Cathedral stained glass windows",
        "Cathédrale Notre-Dame de Chartres vitraux",
        "Chartres Cathedral blue stained glass",
        "Chartres Cathedral rose window",
        "Chartres Cathedral west facade sculptures",
        "Royal Portal Chartres Cathedral",
        "Portail Royal Chartres sculpture",
        "Chartres Cathedral Gothic architecture",
        "Chartres Cathedral flying buttresses",
        "Notre-Dame de Chartres interior",
        "Chartres Cathedral nave Gothic",
        "Chartres Cathedral labyrinth floor",
        "Chartres blue stained glass medieval",
        "Chartres Cathedral Virgin Mary window",
        # External views
        "Chartres Cathedral towers facade",
        "Cathédrale de Chartres exterior",
        "Chartres Cathedral Gothic France",
    ],

    "CIMABUE": [
        # Santa Trinita Madonna - most famous work
        "Cimabue Santa Trinita Madonna",
        "Maestà Santa Trinita Cimabue Uffizi",
        "Cimabue Madonna Enthroned Santa Trinita",
        "Cimabue Virgin and Child Enthroned",
        # Crucifix works
        "Cimabue Crucifix Santa Croce Florence",
        "Crocifisso Cimabue Santa Croce",
        "Cimabue Crucifix Arezzo",
        # Assisi frescoes
        "Cimabue frescoes Assisi Basilica",
        "Cimabue Upper Basilica Assisi",
        "Cimabue St Francis frescoes",
        # Rucellai Madonna (disputed)
        "Cimabue Rucellai Madonna",
        "Madonna Rucellai Cimabue Uffizi",
        # Portrait (fallback)
        "Cimabue medieval painter portrait",
        "Cimabue Italian painter portrait",
        "Cenni di Pepo Cimabue portrait",
    ],

    "DELACROIX": [
        # Liberty Leading the People - most iconic
        "Delacroix Liberty Leading the People",
        "Eugène Delacroix La Liberté guidant le peuple",
        "Delacroix Liberty Leading People Louvre",
        "Delacroix Marianne flag barricade painting",
        "Liberty Guiding People Delacroix 1830",
        # Death of Sardanapalus
        "Delacroix Death of Sardanapalus",
        "Eugène Delacroix La Mort de Sardanapale",
        "Delacroix Sardanapalus painting Louvre",
        # Massacre at Chios
        "Delacroix Massacre at Chios",
        "Eugène Delacroix Scènes des massacres de Scio",
        # Women of Algiers
        "Delacroix Women of Algiers",
        "Eugène Delacroix Femmes d'Alger",
        # Portrait (fallback)
        "Eugène Delacroix self portrait",
        "Delacroix French painter portrait",
        "Eugène Delacroix romantic painter portrait",
    ],

    "EL GRECO": [
        # Most iconic works
        "El Greco Burial of Count Orgaz",
        "El Greco Entierro del Conde de Orgaz Toledo",
        "El Greco Burial Count Orgaz Santo Tomé",
        "El Greco View of Toledo painting",
        "El Greco Vista de Toledo storm",
        "El Greco Opening of Fifth Seal",
        "El Greco Apocalyptic Vision painting",
        "El Greco Assumption of Virgin",
        "El Greco Asunción de la Virgen",
        # Christ imagery
        "El Greco Christ Carrying Cross",
        "El Greco Disrobing of Christ",
        "El Greco Expolio",
        # Portraits
        "El Greco Cardinal Fernando Niño de Guevara",
        "El Greco portrait nobleman",
        # Self portrait (fallback)
        "El Greco self portrait",
        "Doménikos Theotokópoulos portrait",
        "El Greco Spanish painter portrait",
    ],

    "GIOTTO": [
        # Scrovegni Chapel frescoes - most famous
        "Giotto Scrovegni Chapel frescoes Padua",
        "Giotto Arena Chapel frescoes",
        "Giotto Lamentation Christ Scrovegni",
        "Giotto Kiss of Judas fresco Padua",
        "Giotto Last Judgment Scrovegni Chapel",
        "Giotto Meeting at Golden Gate fresco",
        "Giotto blue chapel Padua frescoes",
        # Assisi frescoes
        "Giotto St Francis Assisi frescoes",
        "Giotto Life of St Francis cycle",
        "Giotto Francis preaching birds fresco",
        # Ognissanti Madonna
        "Giotto Ognissanti Madonna Uffizi",
        "Giotto Madonna Enthroned Uffizi",
        # Campanile
        "Giotto Campanile Florence bell tower",
        # Portrait (fallback)
        "Giotto di Bondone portrait",
        "Giotto medieval painter portrait",
    ],

    "GOYA": [
        # Most iconic works
        "Goya Third of May 1808 painting",
        "Francisco Goya El tres de mayo de 1808",
        "Goya Third May execution painting Prado",
        "Goya Second of May 1808 uprising",
        "Goya Saturn Devouring His Son",
        "Goya Saturno devorando a su hijo",
        "Goya Black Paintings Saturn",
        # Maja paintings
        "Goya Naked Maja painting",
        "Goya La maja desnuda",
        "Goya Clothed Maja painting",
        "Goya La maja vestida",
        # Other famous works
        "Goya Family of Charles IV",
        "Goya La familia de Carlos IV",
        "Goya Disasters of War prints",
        "Goya Los desastres de la guerra",
        # Portrait (fallback)
        "Francisco Goya self portrait",
        "Goya Spanish painter portrait",
    ],

    "LEONARDO": [
        # Mona Lisa - most iconic
        "Leonardo da Vinci Mona Lisa painting",
        "Leonardo Mona Lisa Louvre",
        "La Gioconda Leonardo da Vinci",
        "Mona Lisa Leonardo portrait",
        # Last Supper
        "Leonardo da Vinci Last Supper",
        "Leonardo Last Supper Santa Maria Grazie Milan",
        "Il Cenacolo Leonardo da Vinci",
        "Leonardo Last Supper fresco",
        # Vitruvian Man
        "Leonardo da Vinci Vitruvian Man",
        "Leonardo Vitruvian Man drawing",
        "Uomo Vitruviano Leonardo",
        # Other paintings
        "Leonardo da Vinci Lady with Ermine",
        "Leonardo Lady Ermine painting",
        "Leonardo da Vinci Virgin of the Rocks",
        "Leonardo Vergine delle Rocce",
        "Leonardo da Vinci Annunciation painting",
        # Portrait (fallback)
        "Leonardo da Vinci self portrait",
        "Leonardo Renaissance portrait",
    ],

    "MASACCIO": [
        # Brancacci Chapel frescoes - most famous
        "Masaccio Brancacci Chapel frescoes Florence",
        "Masaccio Expulsion from Garden Eden",
        "Masaccio Cacciata Adam Eve",
        "Masaccio Tribute Money fresco",
        "Masaccio Tributo Brancacci Chapel",
        "Masaccio St Peter Healing Sick Shadow",
        # Holy Trinity
        "Masaccio Holy Trinity Santa Maria Novella",
        "Masaccio Trinità Santa Maria Novella",
        "Masaccio Holy Trinity perspective fresco",
        # Pisa Altarpiece
        "Masaccio Pisa Altarpiece",
        "Masaccio Madonna and Child Pisa",
        # Portrait (fallback)
        "Masaccio Renaissance painter portrait",
        "Tommaso Masaccio portrait",
    ],

    "MICHELANGELO": [
        # Sistine Chapel ceiling - most iconic
        "Michelangelo Sistine Chapel ceiling",
        "Michelangelo Creation of Adam",
        "Michelangelo Creazione di Adamo Sistine",
        "Michelangelo Sistine Chapel Last Judgment",
        "Michelangelo Giudizio Universale",
        # David sculpture
        "Michelangelo David sculpture Florence",
        "Michelangelo David marble Accademia",
        "David Michelangelo statue",
        # Pietà
        "Michelangelo Pietà St Peter's",
        "Michelangelo Pietà Vatican marble",
        "Pietà Michelangelo sculpture",
        # Other sculptures
        "Michelangelo Moses sculpture",
        "Michelangelo Mosè San Pietro Vincoli",
        "Michelangelo Dying Slave sculpture",
        # Portrait (fallback)
        "Michelangelo Buonarroti portrait",
        "Michelangelo self portrait",
    ],

    "MONET": [
        # Water Lilies - most iconic
        "Claude Monet Water Lilies painting",
        "Monet Nymphéas painting",
        "Monet Water Lilies Orangerie",
        "Claude Monet water lily pond painting",
        # Impression Sunrise
        "Monet Impression Sunrise painting",
        "Claude Monet Impression soleil levant",
        "Monet Impression Sunrise Le Havre",
        # Haystacks series
        "Monet Haystacks series painting",
        "Claude Monet Meules painting",
        "Monet Grainstacks painting",
        # Rouen Cathedral series
        "Monet Rouen Cathedral series",
        "Claude Monet Cathédrale de Rouen",
        # Japanese Bridge
        "Monet Japanese Bridge Giverny",
        "Claude Monet pont japonais",
        # Portrait (fallback)
        "Claude Monet portrait photograph",
        "Monet Impressionist painter portrait",
    ],

    "PISANO": [
        # Giovanni Pisano - pulpits are his masterwork
        "Giovanni Pisano pulpit Pisa Cathedral",
        "Pisano pulpit Sant'Andrea Pistoia",
        "Giovanni Pisano pergamo Duomo Pisa",
        "Pisano pulpit sculptures marble",
        "Giovanni Pisano Nativity pulpit relief",
        # Siena Cathedral facade
        "Giovanni Pisano Siena Cathedral facade sculptures",
        "Pisano Duomo Siena facade",
        "Giovanni Pisano prophets Siena Cathedral",
        # Madonna sculptures
        "Giovanni Pisano Madonna and Child sculpture",
        "Pisano Madonna Col Bambino",
        # Pisa Baptistery (Nicola Pisano, father)
        "Nicola Pisano Baptistery pulpit Pisa",
        "Pisano pulpit Battistero Pisa",
        # Portrait (fallback)
        "Giovanni Pisano sculptor portrait",
        "Pisano medieval sculptor portrait",
    ],

    "POLLOCK": [
        # Drip paintings - signature technique
        "Jackson Pollock drip painting",
        "Jackson Pollock No 5 1948",
        "Jackson Pollock One Number 31",
        "Jackson Pollock Number 1A",
        "Jackson Pollock Lavender Mist",
        "Jackson Pollock splatter painting canvas floor",
        # Action painting process
        "Jackson Pollock painting floor photograph",
        "Pollock action painting studio",
        "Jackson Pollock dripping paint photograph",
        # Portrait (fallback)
        "Jackson Pollock portrait photograph",
    ],

    "RAPHAEL": [
        # School of Athens - most iconic
        "Raphael School of Athens fresco",
        "Raphael Scuola di Atene Vatican",
        "Raphael School Athens Plato Aristotle",
        "Raphael Stanza della Segnatura",
        # Sistine Madonna
        "Raphael Sistine Madonna painting",
        "Raphael Madonna di San Sisto",
        "Raphael Sistine Madonna cherubs",
        # Transfiguration
        "Raphael Transfiguration painting",
        "Raphael Trasfigurazione Vatican",
        # Madonnas
        "Raphael Madonna of the Goldfinch",
        "Raphael Madonna del Cardellino",
        "Raphael Alba Madonna",
        # Self portrait (fallback)
        "Raphael self portrait Uffizi",
        "Raffaello Sanzio portrait",
        "Raphael Renaissance painter portrait",
    ],

    "REMBRANDT": [
        # Night Watch - most iconic
        "Rembrandt Night Watch painting",
        "Rembrandt De Nachtwacht Rijksmuseum",
        "Rembrandt Night Watch militia painting",
        "Night Watch Rembrandt Amsterdam",
        # Self portraits
        "Rembrandt self portrait",
        "Rembrandt self portrait 1669",
        "Rembrandt zelfportret",
        # Other famous works
        "Rembrandt Anatomy Lesson Dr Tulp",
        "Rembrandt anatomische les Dr Tulp",
        "Rembrandt Return of Prodigal Son",
        "Rembrandt Terugkeer verloren zoon",
        "Rembrandt Jewish Bride painting",
        "Rembrandt Het Joodse bruidje",
        # Portrait
        "Rembrandt van Rijn portrait",
        "Rembrandt Dutch Golden Age painter",
    ],

    "REYNOLDS": [
        # Famous portraits
        "Joshua Reynolds portrait painting",
        "Reynolds Mrs Siddons as Tragic Muse",
        "Reynolds Sarah Siddons portrait",
        "Joshua Reynolds Lady Caroline Howard",
        "Reynolds portrait Royal Academy",
        "Joshua Reynolds Lord Heathfield Gibraltar",
        "Reynolds Three Ladies Adorning Term Hymen",
        "Reynolds Age of Innocence painting",
        "Joshua Reynolds Colonel Tarleton painting",
        # Self portrait
        "Joshua Reynolds self portrait",
        "Reynolds self portrait Royal Academy",
        # General searches
        "Joshua Reynolds portrait painter",
        "Reynolds Georgian portrait painting",
        "Sir Joshua Reynolds portrait",
    ],

    "RODIN": [
        # The Thinker - most iconic
        "Rodin The Thinker sculpture",
        "Auguste Rodin Le Penseur",
        "Rodin Thinker bronze sculpture",
        "The Thinker Rodin Musée",
        # The Kiss
        "Rodin The Kiss sculpture",
        "Auguste Rodin Le Baiser",
        "Rodin Kiss marble sculpture",
        # Gates of Hell
        "Rodin Gates of Hell sculpture",
        "Auguste Rodin Porte de l'Enfer",
        "Rodin Gates Hell bronze portal",
        # Burghers of Calais
        "Rodin Burghers of Calais sculpture",
        "Auguste Rodin Bourgeois de Calais",
        # Other works
        "Rodin Monument to Balzac",
        "Auguste Rodin Balzac sculpture",
        # Portrait (fallback)
        "Auguste Rodin portrait photograph",
        "Rodin sculptor portrait",
    ],

    "RUBENS": [
        # Most famous works
        "Peter Paul Rubens Descent from Cross",
        "Rubens Descent Cross Antwerp Cathedral",
        "Rubens Kruisafneming painting",
        "Rubens Raising of the Cross",
        "Rubens Elevation Cross Antwerp",
        "Rubens Garden of Love painting",
        "Peter Paul Rubens Judgement of Paris",
        "Rubens Three Graces painting",
        "Rubens Massacre of Innocents",
        # Marie de' Medici cycle
        "Rubens Marie de Medici cycle Louvre",
        "Peter Paul Rubens Medici cycle",
        # Portrait
        "Peter Paul Rubens self portrait",
        "Rubens Flemish Baroque painter portrait",
        "Rubens portrait Isabella Brant",
    ],

    "TURNER": [
        # Most iconic works
        "JMW Turner Fighting Temeraire painting",
        "Turner Fighting Temeraire National Gallery",
        "Turner Temeraire sunset painting",
        "JMW Turner Rain Steam Speed",
        "Turner Rain Steam and Speed painting",
        "Turner railway painting",
        "JMW Turner Slave Ship painting",
        "Turner Slave Ship Slavers throwing overboard",
        # Venetian scenes
        "JMW Turner Venice Grand Canal",
        "Turner Venetian scene painting",
        # Seascapes
        "JMW Turner seascape painting",
        "Turner shipwreck painting",
        "Turner storm at sea painting",
        # Portrait (fallback)
        "JMW Turner portrait",
        "Joseph Mallord William Turner portrait",
        "Turner British painter portrait",
    ],

    "VAN EYCK": [
        # Ghent Altarpiece - most iconic
        "Jan van Eyck Ghent Altarpiece",
        "van Eyck Adoration Mystic Lamb",
        "Jan van Eyck Lam Gods altaarstuk",
        "Ghent Altarpiece van Eyck St Bavo",
        # Arnolfini Portrait
        "Jan van Eyck Arnolfini Portrait",
        "van Eyck Arnolfini Wedding National Gallery",
        "Jan van Eyck Giovanni Arnolfini portrait",
        # Other works
        "Jan van Eyck Man in Turban",
        "van Eyck self portrait turban",
        "Jan van Eyck Madonna Chancellor Rolin",
        "van Eyck Virgin Chancellor Rolin",
        # Portrait (fallback)
        "Jan van Eyck portrait painting",
        "van Eyck Flemish painter portrait",
    ],

    "VELASQUEZ": [
        # Las Meninas - most iconic
        "Velázquez Las Meninas painting",
        "Diego Velázquez Las Meninas Prado",
        "Velázquez Meninas Infanta Margarita",
        "Las Meninas Velázquez royal portrait",
        # Portrait of Pope Innocent X
        "Velázquez Portrait Pope Innocent X",
        "Velázquez Innocent X Doria Pamphilj",
        "Diego Velázquez Papa Inocencio X",
        # Surrender of Breda
        "Velázquez Surrender of Breda",
        "Diego Velázquez Las Lanzas",
        "Velázquez Breda lances painting",
        # Rokeby Venus
        "Velázquez Rokeby Venus",
        "Diego Velázquez Venus del espejo",
        "Velázquez Venus mirror National Gallery",
        # Portrait (fallback)
        "Diego Velázquez self portrait",
        "Velázquez Spanish painter portrait",
    ],

    "VEZELAY": [
        # Vézelay Basilica - the work itself
        "Vézelay Basilica tympanum sculpture",
        "Basilique Sainte-Marie-Madeleine Vézelay",
        "Vézelay Pentecost tympanum",
        "Vézelay narthex tympanum Pentecost",
        "Vézelay Mission Apostles tympanum",
        "Vézelay Romanesque tympanum",
        "Basilica Vézelay central portal sculpture",
        "Vézelay Christ Pantocrator tympanum",
        "Vézelay capitals Romanesque sculpture",
        "Basilique Vézelay nave architecture",
        "Vézelay church Romanesque Burgundy",
        "Vézelay abbey church facade",
        "Vézelay Sainte-Madeleine portal",
        # Architectural views
        "Vézelay Basilica interior Romanesque",
        "Vézelay church exterior Burgundy",
    ],

    # Category B - Buildings and Architects
    # For architects: Focus on their most iconic building first, then portraits
    # For buildings: Focus on the building itself

    "ALBERTI": [
        # Leon Battista Alberti - Renaissance architect, polymath (1404-1472)
        # Most iconic: Santa Maria Novella facade, Florence
        "Santa Maria Novella facade Alberti Florence",
        "Alberti Santa Maria Novella facade design",
        "Leon Battista Alberti Santa Maria Novella",
        "Santa Maria Novella Alberti Renaissance facade",
        # Sant'Andrea, Mantua
        "Sant'Andrea Mantua Alberti architecture",
        "Basilica Sant'Andrea Alberti design",
        "Leon Battista Alberti Sant'Andrea Mantua",
        "Sant'Andrea Mantua barrel vault Alberti",
        # Tempio Malatestiano, Rimini
        "Tempio Malatestiano Rimini Alberti",
        "Alberti Tempio Malatestiano facade",
        "Leon Battista Alberti Rimini cathedral",
        # Palazzo Rucellai, Florence
        "Palazzo Rucellai Alberti Florence",
        "Leon Battista Alberti Palazzo Rucellai",
        "Palazzo Rucellai Renaissance facade Alberti",
        # San Sebastiano, Mantua
        "San Sebastiano Mantua Alberti",
        "Leon Battista Alberti San Sebastiano",
        # Portrait fallback
        "Leon Battista Alberti portrait",
        "Alberti Renaissance architect portrait",
        "Leon Battista Alberti self portrait medal",
    ],

    "BORROMINI": [
        # Francesco Borromini - Baroque architect (1599-1667)
        # Most iconic: San Carlo alle Quattro Fontane, Rome
        "San Carlo alle Quattro Fontane Borromini Rome",
        "Borromini San Carlino Rome Baroque",
        "San Carlo Quattro Fontane facade Borromini",
        "Borromini San Carlo alle Quattro Fontane interior",
        "San Carlino dome Borromini",
        # Sant'Ivo alla Sapienza
        "Sant'Ivo alla Sapienza Borromini Rome",
        "Borromini Sant'Ivo spiral dome",
        "Sant'Ivo Sapienza Borromini Baroque",
        "Borromini Sant'Ivo courtyard spiral",
        # Sant'Agnese in Agone, Piazza Navona
        "Sant'Agnese Agone Borromini Piazza Navona",
        "Borromini Sant'Agnese Piazza Navona Rome",
        "Sant'Agnese facade Borromini Baroque",
        # Palazzo Spada perspective gallery
        "Palazzo Spada perspective gallery Borromini",
        "Borromini Palazzo Spada forced perspective",
        "Palazzo Spada colonnade Borromini illusion",
        # Sant'Andrea delle Fratte
        "Sant'Andrea delle Fratte Borromini campanile",
        "Borromini Sant'Andrea Fratte dome",
        # Portrait fallback
        "Francesco Borromini portrait",
        "Borromini Baroque architect portrait",
        "Borromini architect portrait engraving",
    ],

    "BRAMANTE": [
        # Donato Bramante - High Renaissance architect (1444-1514)
        # Most iconic: Tempietto San Pietro in Montorio, Rome
        "Tempietto San Pietro Montorio Bramante Rome",
        "Bramante Tempietto Rome Renaissance",
        "Tempietto Bramante circular martyrium",
        "San Pietro Montorio Tempietto Bramante architecture",
        "Bramante Tempietto High Renaissance",
        # St. Peter's Basilica (original design)
        "St Peter's Basilica Bramante original design",
        "Bramante St Peter's plan Greek cross",
        "Donato Bramante Vatican St Peter's",
        "St Peter's Bramante Renaissance design",
        # Santa Maria presso San Satiro, Milan
        "Santa Maria presso San Satiro Bramante Milan",
        "Bramante San Satiro perspective trompe l'oeil",
        "Santa Maria San Satiro Bramante choir illusion",
        # Cortile del Belvedere, Vatican
        "Cortile Belvedere Bramante Vatican",
        "Bramante Belvedere courtyard Vatican",
        "Belvedere Court Bramante Renaissance",
        # Santa Maria delle Grazie, Milan (tribune)
        "Santa Maria delle Grazie Bramante Milan tribune",
        "Bramante Santa Maria Grazie tribune dome",
        # Portrait fallback
        "Donato Bramante portrait",
        "Bramante Renaissance architect portrait",
        "Bramante architect portrait painting",
    ],

    "BRUNELLESCHI": [
        # Filippo Brunelleschi - Renaissance architect (1377-1446)
        # Most iconic: Florence Cathedral dome (Il Duomo)
        "Florence Cathedral dome Brunelleschi",
        "Brunelleschi Duomo Florence cupola",
        "Santa Maria del Fiore dome Brunelleschi",
        "Brunelleschi Florence Cathedral dome interior",
        "Duomo Florence Brunelleschi dome exterior",
        "Brunelleschi cupola double shell dome",
        # Ospedale degli Innocenti, Florence
        "Ospedale degli Innocenti Brunelleschi Florence",
        "Brunelleschi Foundling Hospital colonnade",
        "Ospedale Innocenti Brunelleschi loggia",
        "Brunelleschi Ospedale Innocenti Renaissance",
        # San Lorenzo, Florence
        "San Lorenzo Florence Brunelleschi",
        "Brunelleschi San Lorenzo basilica Florence",
        "San Lorenzo nave Brunelleschi Renaissance",
        "Basilica San Lorenzo Brunelleschi interior",
        # Santo Spirito, Florence
        "Santo Spirito Florence Brunelleschi",
        "Brunelleschi Santo Spirito basilica",
        "Santo Spirito nave Brunelleschi architecture",
        # Pazzi Chapel
        "Pazzi Chapel Brunelleschi Florence",
        "Brunelleschi Pazzi Chapel Santa Croce",
        "Cappella Pazzi Brunelleschi Renaissance",
        # Portrait fallback
        "Filippo Brunelleschi portrait",
        "Brunelleschi Renaissance architect portrait",
        "Brunelleschi portrait sculpture Donatello",
    ],

    "CANTERBURY": [
        # Canterbury Cathedral - already a building
        "Canterbury Cathedral Gothic architecture England",
        "Canterbury Cathedral nave Gothic",
        "Canterbury Cathedral crypt Romanesque",
        "Canterbury Cathedral Bell Harry tower",
        "Canterbury Cathedral stained glass windows",
        "Canterbury Cathedral choir Gothic",
        "Canterbury Cathedral Trinity Chapel",
        "Canterbury Cathedral interior Gothic vaulting",
        "Canterbury Cathedral west facade towers",
        "Canterbury Cathedral cloisters medieval",
        "Canterbury Cathedral chapter house",
        "Canterbury Cathedral Corona chapel",
        "Canterbury Cathedral Great South Window",
        "Canterbury Cathedral Perpendicular Gothic",
        "Canterbury Cathedral Kent medieval",
    ],

    "CLUNY": [
        # Cluny Abbey - already a building (mostly destroyed)
        "Cluny Abbey reconstruction Burgundy",
        "Cluny III abbey church medieval",
        "Abbaye de Cluny Romanesque architecture",
        "Cluny Abbey ruins France",
        "Cluny Abbey medieval monastery",
        "Cluny Abbey basilica reconstruction drawing",
        "Cluny Abbey Romanesque church Burgundy",
        "Cluny Abbey tower medieval",
        "Cluny III largest church medieval",
        "Cluny Abbey nave reconstruction",
        "Abbaye Cluny France medieval architecture",
        "Cluny Abbey octagonal tower",
        "Cluny Abbey capitals Romanesque sculpture",
        "Cluny monastery medieval France",
        "Cluny Abbey architectural remains",
    ],

    "FONTENAY": [
        # Fontenay Abbey - already a building (Cistercian abbey)
        "Fontenay Abbey Cistercian architecture Burgundy",
        "Abbaye de Fontenay Romanesque church",
        "Fontenay Abbey cloister medieval",
        "Fontenay Abbey France Cistercian monastery",
        "Fontenay Abbey nave barrel vault",
        "Abbaye Fontenay Burgundy Romanesque",
        "Fontenay Abbey church interior austere",
        "Fontenay Abbey dormitory medieval",
        "Fontenay Abbey forge building",
        "Cistercian Abbey Fontenay architecture",
        "Fontenay Abbey cloister arcade Romanesque",
        "Abbaye Fontenay France UNESCO",
        "Fontenay Abbey chapter house",
        "Fontenay Abbey medieval monastery France",
        "Fontenay Abbey gardens cloister",
    ],

    "KING'S CHAPEL": [
        # King's College Chapel, Cambridge - already a building
        "King's College Chapel Cambridge Gothic",
        "King's Chapel Cambridge fan vaulting",
        "King's College Chapel Cambridge interior",
        "King's Chapel Cambridge stained glass windows",
        "King's College Chapel Perpendicular Gothic",
        "King's Chapel Cambridge fan vault ceiling",
        "King's College Chapel Cambridge exterior",
        "King's Chapel Cambridge choir screen",
        "King's College Chapel Cambridge Rubens",
        "King's Chapel Cambridge Tudor architecture",
        "King's College Chapel Cambridge nave",
        "King's Chapel Cambridge England Gothic",
        "King's College Chapel Cambridge organ",
        "King's Chapel Cambridge architectural masterpiece",
        "King's College Chapel Cambridge university",
    ],

    "LE CORBUSIER": [
        # Le Corbusier - Modernist architect (1887-1965)
        # Most iconic: Villa Savoye, Poissy
        "Villa Savoye Le Corbusier Poissy",
        "Le Corbusier Villa Savoye modernist architecture",
        "Villa Savoye Poissy France Le Corbusier",
        "Le Corbusier Villa Savoye pilotis",
        "Villa Savoye Le Corbusier International Style",
        # Unité d'Habitation, Marseille
        "Unité d'Habitation Marseille Le Corbusier",
        "Le Corbusier Cité Radieuse Marseille",
        "Unite Habitation Le Corbusier brutalist",
        "Le Corbusier Marseille housing block",
        # Notre Dame du Haut, Ronchamp
        "Notre Dame du Haut Ronchamp Le Corbusier",
        "Le Corbusier Ronchamp chapel France",
        "Ronchamp chapel Le Corbusier modernist",
        "Notre Dame Haut Le Corbusier sculptural",
        # Villa La Roche, Paris
        "Villa La Roche Le Corbusier Paris",
        "Le Corbusier Villa Roche modernist",
        "Maison La Roche Le Corbusier white architecture",
        # Chandigarh - city planning
        "Chandigarh Le Corbusier India city planning",
        "Le Corbusier Chandigarh Capitol Complex",
        "Chandigarh Palace Assembly Le Corbusier",
        # Portrait fallback
        "Le Corbusier portrait architect",
        "Le Corbusier architect portrait photograph",
        "Charles-Édouard Jeanneret Le Corbusier portrait",
    ],

    "LOUVRE": [
        # Louvre Palace - already a building/palace
        "Louvre Palace Paris architecture",
        "Louvre pyramid glass pyramid Paris",
        "Louvre Palace courtyard Paris France",
        "Louvre museum facade Paris",
        "Louvre Palace Renaissance architecture",
        "Louvre Cour Carrée Paris",
        "Louvre colonnade Perrault Paris",
        "Louvre Palace Seine River Paris",
        "Louvre Napoleon courtyard pyramid",
        "Louvre Palace Tuileries Paris",
        "Louvre museum exterior architecture Paris",
        "Louvre Palace Richelieu wing",
        "Louvre architecture French Renaissance",
        "Louvre pyramid night Paris",
        "Louvre Palace historic monument Paris",
    ],

    "MANSART": [
        # Jules Hardouin-Mansart - Baroque architect (1646-1708)
        # Most iconic: Palace of Versailles (Hall of Mirrors, expansions)
        "Hall of Mirrors Versailles Hardouin-Mansart",
        "Jules Hardouin-Mansart Versailles palace",
        "Galerie des Glaces Mansart Versailles",
        "Versailles Hall of Mirrors Mansart architecture",
        "Hardouin-Mansart Versailles expansion",
        # Les Invalides dome, Paris
        "Les Invalides dome Paris Hardouin-Mansart",
        "Dôme des Invalides Mansart Paris",
        "Jules Hardouin-Mansart Invalides Paris",
        "Invalides dome golden Mansart Baroque",
        "Église du Dôme Invalides Mansart",
        # Place Vendôme, Paris
        "Place Vendôme Paris Hardouin-Mansart",
        "Mansart Place Vendôme Paris architecture",
        "Place Vendôme colonnade Mansart",
        # Chapel of Versailles
        "Versailles Royal Chapel Hardouin-Mansart",
        "Chapelle Royale Versailles Mansart",
        "Mansart Versailles chapel Baroque",
        # Grand Trianon, Versailles
        "Grand Trianon Versailles Hardouin-Mansart",
        "Mansart Grand Trianon marble palace",
        # Portrait fallback
        "Jules Hardouin-Mansart portrait",
        "Mansart architect portrait Baroque",
        "Hardouin-Mansart French architect portrait",
    ],

    "NEUMANN": [
        # Balthasar Neumann - Baroque architect (1687-1753)
        # Most iconic: Würzburg Residence (Residenz Würzburg)
        "Würzburg Residence Neumann Baroque architecture",
        "Residenz Würzburg Balthasar Neumann",
        "Würzburg Residence staircase Neumann Tiepolo",
        "Neumann Würzburg Residenz grand staircase",
        "Würzburg Residence Neumann Baroque palace",
        # Vierzehnheiligen (Basilica of the Fourteen Holy Helpers)
        "Vierzehnheiligen basilica Neumann Baroque",
        "Basilica Fourteen Holy Helpers Neumann",
        "Vierzehnheiligen Neumann Bavaria church",
        "Neumann Vierzehnheiligen interior Baroque",
        "Basilica Vierzehnheiligen Neumann pilgrimage",
        # Schloss Augustusburg, Brühl
        "Schloss Augustusburg Brühl Neumann staircase",
        "Augustusburg Palace Neumann Baroque",
        "Neumann Augustusburg grand staircase",
        # Basilica of Neresheim
        "Neresheim Abbey Neumann Baroque church",
        "Abtei Neresheim Neumann architecture",
        # Käppele, Würzburg
        "Käppele Würzburg Neumann pilgrimage church",
        "Wallfahrtskirche Käppele Neumann",
        # Portrait fallback
        "Balthasar Neumann portrait architect",
        "Neumann Baroque architect portrait",
        "Balthasar Neumann portrait engraving",
    ],

    "NOTRE DAME": [
        # Notre-Dame de Paris - already a building (cathedral)
        "Notre-Dame Paris cathedral Gothic architecture",
        "Notre-Dame Paris facade rose window",
        "Notre-Dame de Paris flying buttresses",
        "Notre-Dame Paris cathedral interior nave",
        "Notre-Dame Paris Gothic cathedral France",
        "Notre-Dame Paris west facade towers",
        "Notre-Dame Paris stained glass rose windows",
        "Notre-Dame Paris cathedral Seine River",
        "Notre-Dame Paris Gothic vaulting interior",
        "Notre-Dame Paris cathedral sculpture portal",
        "Notre-Dame Paris spire cathedral",
        "Notre-Dame Paris cathedral choir",
        "Notre-Dame Paris medieval Gothic architecture",
        "Notre-Dame Paris cathedral Île de la Cité",
        "Notre-Dame Paris before fire 2019",
    ],

    "PALLADIO": [
        # Andrea Palladio - Renaissance architect (1508-1580)
        # Most iconic: Villa Rotonda (Villa Capra), Vicenza
        "Villa Rotonda Palladio Vicenza",
        "Villa Capra Rotonda Palladio Italy",
        "Palladio Villa Rotonda Renaissance architecture",
        "Villa Rotonda Vicenza Palladio dome",
        "Villa Capra Palladio symmetrical villa",
        # Basilica Palladiana, Vicenza
        "Basilica Palladiana Vicenza Palladio",
        "Palladio Basilica Vicenza loggia",
        "Basilica Palladiana Palladio colonnade",
        # Teatro Olimpico, Vicenza
        "Teatro Olimpico Vicenza Palladio",
        "Palladio Teatro Olimpico indoor theatre",
        "Teatro Olimpico Vicenza Palladio stage",
        # San Giorgio Maggiore, Venice
        "San Giorgio Maggiore Venice Palladio",
        "Palladio San Giorgio Maggiore church",
        "San Giorgio Maggiore facade Palladio Venice",
        "Palladio San Giorgio Maggiore interior",
        # Il Redentore, Venice
        "Il Redentore Venice Palladio church",
        "Palladio Redentore Venice architecture",
        "Chiesa del Redentore Palladio Venice",
        # Villa Emo
        "Villa Emo Palladio Fanzolo",
        "Palladio Villa Emo Veneto",
        # Portrait fallback
        "Andrea Palladio portrait architect",
        "Palladio Renaissance architect portrait",
        "Andrea Palladio portrait painting",
    ],

    "PAXTON": [
        # Joseph Paxton - Victorian architect/gardener (1803-1865)
        # Most iconic: Crystal Palace, London (Great Exhibition 1851)
        "Crystal Palace Paxton London 1851",
        "Joseph Paxton Crystal Palace Great Exhibition",
        "Crystal Palace Hyde Park Paxton glass iron",
        "Paxton Crystal Palace architecture Victorian",
        "Great Exhibition 1851 Crystal Palace Paxton",
        "Crystal Palace interior Paxton 1851",
        "Joseph Paxton Crystal Palace design",
        "Crystal Palace Paxton prefabricated glass",
        # Chatsworth House conservatory
        "Chatsworth House conservatory Paxton",
        "Great Conservatory Chatsworth Paxton",
        "Joseph Paxton Chatsworth glasshouse",
        "Paxton Chatsworth conservatory Victorian",
        # Mentmore Towers
        "Mentmore Towers Paxton architecture",
        "Joseph Paxton Mentmore Towers Jacobean",
        # Birkenhead Park (landscape design)
        "Birkenhead Park Paxton landscape design",
        "Joseph Paxton Birkenhead Park public",
        # Portrait fallback
        "Joseph Paxton portrait architect",
        "Sir Joseph Paxton portrait Victorian",
        "Joseph Paxton portrait photograph",
    ],

    "SANTA CROCE": [
        # Basilica of Santa Croce, Florence - already a building
        "Santa Croce Florence basilica Gothic",
        "Basilica Santa Croce Florence facade",
        "Santa Croce Florence interior nave",
        "Santa Croce Florence Franciscan church",
        "Basilica Santa Croce Florence Gothic architecture",
        "Santa Croce Florence Giotto frescoes",
        "Santa Croce Florence Michelangelo tomb",
        "Santa Croce Florence Pazzi Chapel Brunelleschi",
        "Basilica Santa Croce Florence cloisters",
        "Santa Croce Florence Italian Pantheon",
        "Santa Croce Florence neo-Gothic facade",
        "Basilica Santa Croce Florence Galileo tomb",
        "Santa Croce Florence Dante cenotaph",
        "Santa Croce Florence Machiavelli tomb",
        "Santa Croce Florence Arnolfo di Cambio",
    ],

    "ST. DENIS": [
        # Abbey of Saint-Denis - already a building (Gothic cathedral)
        "Saint-Denis Abbey Gothic architecture France",
        "Abbaye de Saint-Denis basilica Paris",
        "Saint-Denis Abbey royal necropolis France",
        "Saint-Denis basilica Gothic cathedral",
        "Abbey Saint-Denis facade Gothic",
        "Saint-Denis Abbey choir Gothic stained glass",
        "Basilique Saint-Denis royal tombs France",
        "Saint-Denis Abbey ambulatory Gothic",
        "Abbey Saint-Denis Abbot Suger Gothic",
        "Saint-Denis basilica rose window",
        "Saint-Denis Abbey nave Gothic vaulting",
        "Basilica Saint-Denis Paris medieval",
        "Saint-Denis Abbey French kings burial",
        "Abbey Saint-Denis ribbed vault Gothic",
        "Saint-Denis basilica Gothic innovation",
    ],

    "ST. MARK'S": [
        # St. Mark's Basilica, Venice - already a building
        "St Mark's Basilica Venice Byzantine architecture",
        "Basilica San Marco Venice facade mosaics",
        "St Mark's Basilica Venice domes",
        "San Marco Venice Byzantine church Italy",
        "St Mark's Basilica Venice interior golden mosaics",
        "Basilica San Marco Venice Pala d'Oro",
        "St Mark's Basilica Venice horses bronze",
        "San Marco Venice Byzantine Gothic architecture",
        "St Mark's Basilica Venice Piazza San Marco",
        "Basilica San Marco Venice campanile bell tower",
        "St Mark's Basilica Venice narthex mosaics",
        "San Marco Venice basilica domes exterior",
        "St Mark's Basilica Venice marble columns",
        "Basilica San Marco Venice atrium mosaics",
        "St Mark's Venice Byzantine architecture Italy",
    ],

    "ST. PETER'S": [
        # St. Peter's Basilica, Vatican - already a building
        "St Peter's Basilica Vatican Rome",
        "San Pietro Vatican basilica dome Michelangelo",
        "St Peter's Basilica facade Vatican",
        "St Peter's Basilica interior Vatican nave",
        "Basilica San Pietro Vatican Rome",
        "St Peter's dome Michelangelo Vatican",
        "St Peter's Basilica Bernini colonnade piazza",
        "St Peter's Vatican basilica baldachin Bernini",
        "San Pietro Vatican Renaissance Baroque",
        "St Peter's Basilica Vatican interior Michelangelo",
        "St Peter's Square Vatican Bernini colonnade",
        "Basilica San Pietro Rome papal basilica",
        "St Peter's Vatican dome cupola interior",
        "St Peter's Basilica Vatican Pietà Michelangelo",
        "San Pietro Vatican largest church world",
    ],

    "TELFORD": [
        # Thomas Telford - civil engineer (1757-1834)
        # Most iconic: Menai Suspension Bridge, Wales
        "Menai Suspension Bridge Telford Wales",
        "Thomas Telford Menai Bridge Anglesey",
        "Menai Strait Bridge Telford suspension",
        "Telford Menai Bridge Wales engineering",
        "Menai Suspension Bridge Thomas Telford 1826",
        # Pontcysyllte Aqueduct, Wales
        "Pontcysyllte Aqueduct Telford Wales",
        "Thomas Telford Pontcysyllte Aqueduct canal",
        "Pontcysyllte Aqueduct Telford UNESCO",
        "Telford Pontcysyllte Wales aqueduct bridge",
        # Craigellachie Bridge, Scotland
        "Craigellachie Bridge Telford Scotland",
        "Thomas Telford Craigellachie Bridge cast iron",
        "Telford Craigellachie Bridge Speyside",
        # Caledonian Canal, Scotland
        "Caledonian Canal Telford Scotland",
        "Thomas Telford Caledonian Canal engineering",
        "Telford Caledonian Canal locks Scotland",
        # Dean Bridge, Edinburgh
        "Dean Bridge Edinburgh Telford",
        "Thomas Telford Dean Bridge Scotland",
        # Portrait fallback
        "Thomas Telford portrait engineer",
        "Thomas Telford portrait civil engineer",
        "Thomas Telford portrait engraving",
    ],

    "VERSAILLES": [
        # Palace of Versailles - already a building/palace
        "Palace of Versailles France architecture",
        "Château de Versailles gardens fountains",
        "Versailles palace Hall of Mirrors",
        "Versailles France royal palace Baroque",
        "Palace of Versailles facade architecture",
        "Versailles gardens André Le Nôtre",
        "Château Versailles France Louis XIV",
        "Versailles palace interior Hall Mirrors",
        "Versailles royal palace France architecture",
        "Palace Versailles gardens aerial view",
        "Versailles chapel royal architecture",
        "Château Versailles opera house",
        "Versailles palace Grand Trianon",
        "Versailles gardens fountains Baroque",
        "Palace Versailles France UNESCO heritage",
    ],

    "WESTMINSTER": [
        # Westminster Abbey - already a building
        "Westminster Abbey London Gothic architecture",
        "Westminster Abbey London facade towers",
        "Westminster Abbey interior nave Gothic",
        "Westminster Abbey London coronation church",
        "Westminster Abbey Henry VII Lady Chapel",
        "Westminster Abbey London Perpendicular Gothic",
        "Westminster Abbey chapter house medieval",
        "Westminster Abbey London royal weddings",
        "Westminster Abbey Poets' Corner",
        "Westminster Abbey London cloisters",
        "Westminster Abbey Gothic architecture England",
        "Westminster Abbey London fan vaulting",
        "Westminster Abbey royal tombs London",
        "Westminster Abbey London towers west facade",
        "Westminster Abbey England coronation church",
    ],

    "WINDSOR": [
        # Windsor Castle - already a building/castle
        "Windsor Castle England royal residence",
        "Windsor Castle Berkshire architecture",
        "Windsor Castle Round Tower England",
        "Windsor Castle State Apartments England",
        "Windsor Castle St George's Chapel",
        "Windsor Castle England medieval castle",
        "Windsor Castle royal palace Berkshire",
        "Windsor Castle England Thames Valley",
        "Windsor Castle State Apartments interior",
        "Windsor Castle St George's Chapel Gothic",
        "Windsor Castle England largest occupied castle",
        "Windsor Castle Upper Ward England",
        "Windsor Castle England royal fortress",
        "Windsor Castle architecture Norman",
        "Windsor Castle England Queen residence",
    ],

    "WREN": [
        # Christopher Wren - English Baroque architect (1632-1723)
        # Most iconic: St. Paul's Cathedral, London
        "St Paul's Cathedral Wren London",
        "Christopher Wren St Paul's Cathedral dome",
        "St Paul's Cathedral London Wren Baroque",
        "Wren St Paul's Cathedral London architecture",
        "St Paul's dome Christopher Wren London",
        "St Paul's Cathedral Wren west facade",
        # Royal Naval College, Greenwich
        "Royal Naval College Greenwich Wren",
        "Greenwich Hospital Christopher Wren",
        "Wren Royal Naval College Greenwich",
        "Old Royal Naval College Wren London",
        # St. Stephen Walbrook, London
        "St Stephen Walbrook Wren London",
        "Christopher Wren St Stephen Walbrook dome",
        "St Stephen Walbrook Wren church interior",
        # St. Mary-le-Bow, London
        "St Mary-le-Bow Wren London Cheapside",
        "Christopher Wren St Mary-le-Bow church",
        "St Mary Bow church Wren London",
        # Christ Church, Oxford (Tom Tower)
        "Tom Tower Christ Church Oxford Wren",
        "Christopher Wren Tom Tower Oxford",
        "Christ Church Oxford Wren architecture",
        # Sheldonian Theatre, Oxford
        "Sheldonian Theatre Oxford Wren",
        "Christopher Wren Sheldonian Theatre",
        # Portrait fallback
        "Christopher Wren portrait architect",
        "Sir Christopher Wren portrait",
        "Christopher Wren portrait Kneller",
    ],

    "WRIGHT": [
        # Frank Lloyd Wright - American architect (1867-1959)
        # Most iconic: Fallingwater (Kaufmann Residence)
        "Fallingwater Frank Lloyd Wright Pennsylvania",
        "Frank Lloyd Wright Fallingwater waterfall house",
        "Kaufmann Residence Fallingwater Wright",
        "Fallingwater Wright organic architecture",
        "Frank Lloyd Wright Fallingwater Bear Run",
        # Guggenheim Museum, New York
        "Guggenheim Museum Frank Lloyd Wright New York",
        "Frank Lloyd Wright Guggenheim spiral",
        "Solomon R Guggenheim Museum Wright NYC",
        "Guggenheim Museum Wright spiral ramp",
        "Frank Lloyd Wright Guggenheim Fifth Avenue",
        # Robie House, Chicago
        "Robie House Frank Lloyd Wright Chicago",
        "Frank Lloyd Wright Robie House Prairie Style",
        "Frederick C Robie House Wright Chicago",
        "Robie House Wright horizontal lines",
        # Taliesin West, Arizona
        "Taliesin West Frank Lloyd Wright Arizona",
        "Frank Lloyd Wright Taliesin West desert",
        "Taliesin West Wright Scottsdale Arizona",
        # Unity Temple, Illinois
        "Unity Temple Frank Lloyd Wright Oak Park",
        "Frank Lloyd Wright Unity Temple concrete",
        # Portrait fallback
        "Frank Lloyd Wright portrait architect",
        "Frank Lloyd Wright portrait photograph",
        "Frank Lloyd Wright architect portrait",
    ],

    # Category T - Towns, Cities, Regions, Countries
    # Focus on iconic buildings with cityscapes, aerial views, panoramas
    # For cities: iconic skylines, famous landmarks with cityscape
    # For regions/countries: aerial views, landscape panoramas

    "BELGIUM": [
        # Belgium - country, focus on iconic cityscapes and landmarks
        # Grand Place, Brussels - most iconic
        "Grand Place Brussels Belgium aerial view",
        "Brussels Grand Place cityscape Belgium",
        "Grote Markt Brussels Belgium panorama",
        "Grand Place Brussels Belgium guild houses",
        "Brussels Grand Place aerial Belgium architecture",
        # Bruges cityscape
        "Bruges Belgium medieval cityscape aerial",
        "Bruges Belfry tower cityscape Belgium",
        "Brugge Belgium canal cityscape panorama",
        "Bruges Belgium historic center aerial view",
        # Brussels cityscape
        "Brussels Belgium cityscape Atomium",
        "Brussels Belgium skyline panorama",
        "Brussels cityscape aerial view Belgium",
        # Antwerp
        "Antwerp Belgium cathedral cityscape",
        "Antwerp Belgium skyline aerial view",
        # Ghent
        "Ghent Belgium medieval cityscape aerial",
        "Gent Belgium cityscape towers panorama",
        # Country panoramas
        "Belgium countryside aerial view Flanders",
        "Belgium landscape panorama architecture",
        "Belgium historic cities aerial mosaic",
        # Additional aerial shots
        "Brussels city aerial shot Belgium",
        "Bruges aerial drone view Belgium",
        "Belgium cities aerial photograph",
        "Belgian cities aerial overview",
        "Belgium urban aerial view",
        # Map searches
        "Belgium country map political",
        "Belgium map geographic regions",
        "Belgium historical map Flanders Wallonia",
        "Belgium map cities provinces",
        "map of Belgium Europe",
    ],

    "BERLIN": [
        # Berlin - city, iconic buildings with cityscape
        # Brandenburg Gate - most iconic
        "Brandenburg Gate Berlin cityscape",
        "Brandenburger Tor Berlin aerial view",
        "Brandenburg Gate Berlin Pariser Platz cityscape",
        "Berlin Brandenburg Gate skyline panorama",
        # Reichstag building
        "Reichstag building Berlin cityscape dome",
        "Berlin Reichstag aerial view cityscape",
        "Bundestag Reichstag Berlin panorama",
        # Berlin Cathedral
        "Berlin Cathedral cityscape Berliner Dom",
        "Berliner Dom cathedral cityscape aerial",
        "Berlin Cathedral Spree River cityscape",
        # TV Tower (Fernsehturm)
        "Berlin TV Tower Fernsehturm cityscape",
        "Fernsehturm Berlin skyline Alexanderplatz",
        "Berlin television tower cityscape panorama",
        # Skyline views
        "Berlin skyline cityscape panorama",
        "Berlin cityscape aerial view Germany",
        "Berlin skyline sunset panorama",
        # Historic areas
        "Berlin Unter den Linden cityscape",
        "Potsdamer Platz Berlin cityscape modern",
        "Berlin Museum Island cityscape aerial",
        # Additional aerial shots
        "Berlin city aerial shot Germany",
        "Berlin aerial drone view cityscape",
        "Berlin aerial photograph overview",
        "Berlin bird's eye view city",
        "Berlin urban aerial shot",
    ],

    "BOLOGNA": [
        # Bologna - city, medieval towers and porticoes
        # Two Towers - most iconic
        "Due Torri Bologna cityscape Italy",
        "Two Towers Bologna Asinelli Garisenda",
        "Bologna Two Towers medieval cityscape",
        "Torri di Bologna cityscape aerial view",
        "Bologna Asinelli tower cityscape panorama",
        # Piazza Maggiore
        "Piazza Maggiore Bologna cityscape Italy",
        "Bologna Piazza Maggiore aerial view",
        "Bologna main square cityscape panorama",
        # Porticoes
        "Bologna porticoes cityscape Italy",
        "Bologna porticos aerial view historic center",
        "Bologna arcades cityscape UNESCO",
        # Skyline
        "Bologna skyline terracotta roofs Italy",
        "Bologna cityscape aerial view Emilia-Romagna",
        "Bologna historic center panorama Italy",
        # San Petronio
        "San Petronio Bologna cityscape basilica",
        "Bologna San Petronio Piazza Maggiore cityscape",
        # General views
        "Bologna medieval cityscape Italy",
        "Bologna cityscape red roofs towers",
        "Bologna Italy cityscape panorama",
        # Additional aerial shots
        "Bologna aerial shot Italy",
        "Bologna city aerial drone view",
        "Bologna aerial photograph towers",
        "Bologna bird's eye view Italy",
        "Bologna urban aerial overview",
    ],

    "CALIFORNIA": [
        # California - state, diverse landscapes and cities
        # Golden Gate Bridge - most iconic
        "Golden Gate Bridge San Francisco California aerial",
        "San Francisco Golden Gate Bridge cityscape",
        "Golden Gate Bridge California panorama",
        "San Francisco Bay Golden Gate aerial view",
        # San Francisco cityscape
        "San Francisco California cityscape aerial view",
        "San Francisco skyline Bay Bridge California",
        "San Francisco California panorama cityscape",
        # Los Angeles
        "Los Angeles California skyline aerial view",
        "LA California cityscape downtown panorama",
        "Los Angeles Hollywood sign cityscape aerial",
        # State Capitol
        "California State Capitol Sacramento aerial",
        "Sacramento California capitol building cityscape",
        # Natural landmarks
        "California coastline aerial view Pacific",
        "California landscape panorama aerial view",
        # Silicon Valley
        "Silicon Valley California aerial view",
        # San Diego
        "San Diego California skyline aerial view",
        # Diverse landscapes
        "California aerial view landscape panorama",
        "California coastline cities aerial mosaic",
        # Additional aerial shots
        "California state aerial shot",
        "California aerial drone photography",
        "California bird's eye view landscape",
        "California aerial overview cities",
        "California urban aerial photograph",
        # Map searches
        "California state map USA",
        "California map geographic regions",
        "California map topographic terrain",
        "California map cities counties",
        "map of California United States",
    ],

    "CAMBRIDGE": [
        # Cambridge - city, university colleges
        # King's College Chapel - most iconic
        "King's College Chapel Cambridge cityscape",
        "Cambridge King's College aerial view",
        "King's College Cambridge cityscape England",
        "Cambridge King's Chapel River Cam cityscape",
        # Cambridge colleges cityscape
        "Cambridge University colleges aerial view",
        "Cambridge England colleges cityscape panorama",
        "Cambridge colleges spires cityscape",
        # River Cam views
        "Cambridge River Cam colleges cityscape",
        "River Cam Cambridge aerial view colleges",
        "Cambridge backs River Cam cityscape",
        # City center
        "Cambridge city center England aerial view",
        "Cambridge historic center cityscape panorama",
        "Cambridge England cityscape university",
        # Senate House
        "Cambridge Senate House cityscape England",
        "Senate House Cambridge aerial view",
        # Trinity College
        "Trinity College Cambridge cityscape aerial",
        "Cambridge Trinity College Great Court cityscape",
        # General cityscape
        "Cambridge England skyline cityscape",
        "Cambridge cityscape aerial view England",
        # Additional aerial shots
        "Cambridge aerial shot England",
        "Cambridge city aerial drone view",
        "Cambridge aerial photograph overview",
        "Cambridge bird's eye view colleges",
        "Cambridge urban aerial panorama",
    ],

    "EDINBURGH": [
        # Edinburgh - city, castle and old town
        # Edinburgh Castle - most iconic
        "Edinburgh Castle cityscape Scotland",
        "Edinburgh Castle aerial view Old Town",
        "Edinburgh Castle skyline Scotland panorama",
        "Edinburgh Castle Rock cityscape aerial",
        # Old Town skyline
        "Edinburgh Old Town cityscape aerial view",
        "Edinburgh Royal Mile cityscape Scotland",
        "Edinburgh Old Town skyline panorama",
        "Edinburgh medieval cityscape Scotland",
        # Calton Hill views
        "Edinburgh Calton Hill cityscape panorama",
        "Edinburgh cityscape from Calton Hill Scotland",
        "Calton Hill Edinburgh aerial view skyline",
        # Arthur's Seat views
        "Edinburgh cityscape from Arthur's Seat",
        "Edinburgh panorama Arthur's Seat Scotland",
        # Princes Street
        "Princes Street Edinburgh cityscape Scotland",
        "Edinburgh Princes Street gardens cityscape",
        # General cityscape
        "Edinburgh Scotland cityscape aerial view",
        "Edinburgh skyline Scotland panorama",
        "Edinburgh cityscape sunset Scotland",
        "Edinburgh Scotland historic cityscape",
        # Additional aerial shots
        "Edinburgh aerial shot Scotland",
        "Edinburgh city aerial drone view",
        "Edinburgh aerial photograph overview",
        "Edinburgh bird's eye view castle",
        "Edinburgh urban aerial panorama",
    ],

    "FLORENCE": [
        # Florence - city, Renaissance architecture
        # Duomo (Cathedral dome) - most iconic
        "Florence Duomo cityscape Brunelleschi dome",
        "Duomo Florence cityscape aerial view Italy",
        "Florence Cathedral dome cityscape panorama",
        "Brunelleschi dome Florence cityscape Tuscany",
        "Florence Duomo Campanile cityscape aerial",
        # Ponte Vecchio
        "Ponte Vecchio Florence cityscape Arno River",
        "Florence Ponte Vecchio aerial view cityscape",
        "Ponte Vecchio Florence Italy cityscape",
        # Piazzale Michelangelo view
        "Florence cityscape from Piazzale Michelangelo",
        "Florence panorama Piazzale Michelangelo Italy",
        "Florence Arno River cityscape aerial view",
        # Palazzo Vecchio
        "Palazzo Vecchio Florence cityscape Piazza Signoria",
        "Florence Palazzo Vecchio tower cityscape",
        # General cityscape
        "Florence Italy cityscape aerial view",
        "Florence Tuscany skyline panorama",
        "Florence cityscape terracotta roofs Italy",
        "Florence Renaissance cityscape aerial Italy",
        "Firenze cityscape panorama Tuscany",
        # Additional aerial shots
        "Florence aerial shot Italy",
        "Florence city aerial drone view",
        "Florence aerial photograph Duomo",
        "Florence bird's eye view Tuscany",
        "Florence urban aerial overview",
    ],

    "HOLLAND": [
        # Holland (Netherlands) - country/region
        # Amsterdam canals - most iconic
        "Amsterdam canals aerial view Holland Netherlands",
        "Amsterdam Holland cityscape canals aerial",
        "Amsterdam Netherlands canal houses cityscape",
        "Amsterdam canals panorama Holland",
        # Windmills
        "Kinderdijk windmills Holland Netherlands aerial",
        "Dutch windmills Holland countryside aerial view",
        "Zaanse Schans windmills Holland cityscape",
        "Netherlands windmills landscape aerial Holland",
        # Rotterdam
        "Rotterdam Holland skyline aerial view",
        "Rotterdam Netherlands modern cityscape",
        # The Hague
        "The Hague Holland cityscape aerial Netherlands",
        "Den Haag Netherlands cityscape panorama",
        # Tulip fields
        "Dutch tulip fields aerial view Holland",
        "Holland tulip fields landscape Netherlands",
        # Countryside
        "Holland countryside aerial view Netherlands",
        "Netherlands landscape panorama Holland",
        "Dutch countryside canals aerial Holland",
        # Amsterdam skyline
        "Amsterdam Holland skyline panorama",
        # Additional aerial shots
        "Holland aerial shot Netherlands",
        "Amsterdam aerial drone view canals",
        "Holland aerial photograph windmills",
        "Netherlands bird's eye view cities",
        "Holland landscape aerial panorama",
        # Map searches
        "Netherlands country map political",
        "Holland map geographic regions",
        "Netherlands map provinces cities",
        "Holland historical map Dutch regions",
        "map of Netherlands Europe",
    ],

    "IVY LEAGUE": [
        # Ivy League - collection of universities (focus on iconic campuses)
        # Harvard Yard - most iconic
        "Harvard Yard aerial view Cambridge Massachusetts",
        "Harvard University campus aerial cityscape",
        "Harvard Yard buildings Massachusetts cityscape",
        # Yale
        "Yale University campus aerial view New Haven",
        "Yale campus Gothic architecture cityscape",
        "Yale University New Haven aerial panorama",
        # Princeton
        "Princeton University campus aerial view New Jersey",
        "Princeton campus Nassau Hall aerial",
        "Princeton University Gothic campus cityscape",
        # Columbia
        "Columbia University campus aerial view New York",
        "Columbia campus Morningside Heights cityscape",
        # Cornell
        "Cornell University campus aerial view Ithaca",
        "Cornell campus Ithaca New York panorama",
        # Penn
        "University of Pennsylvania campus aerial Philadelphia",
        "Penn campus Philadelphia cityscape aerial",
        # Dartmouth
        "Dartmouth College campus aerial Hanover",
        # Brown
        "Brown University campus aerial Providence",
        # General
        "Ivy League university campus aerial view",
        # Additional aerial shots
        "Ivy League campus aerial shot",
        "Harvard Yale aerial drone view",
        "Ivy League aerial photograph campuses",
        "university campus bird's eye view",
        "Ivy League aerial overview",
    ],

    "LOIRE VALLEY": [
        # Loire Valley - region, Renaissance châteaux
        # Château de Chambord - most iconic
        "Château de Chambord Loire Valley aerial view",
        "Chambord castle Loire Valley France aerial",
        "Château Chambord Loire Valley landscape panorama",
        "Chambord Loire Valley France countryside aerial",
        # Château de Chenonceau
        "Château de Chenonceau Loire Valley aerial",
        "Chenonceau castle Loire River aerial view",
        "Château Chenonceau Loire Valley France panorama",
        # Château d'Amboise
        "Château d'Amboise Loire Valley aerial view",
        "Amboise castle Loire Valley France cityscape",
        # Château de Villandry
        "Château de Villandry gardens Loire Valley aerial",
        "Villandry castle Loire Valley France aerial view",
        # Loire River landscape
        "Loire River valley France aerial view panorama",
        "Loire Valley France landscape aerial châteaux",
        "Loire Valley countryside France aerial panorama",
        # Multiple châteaux
        "Loire Valley castles France aerial view",
        "Loire Valley France châteaux landscape panorama",
        # Regional views
        "Loire Valley France vineyards aerial view",
        "Loire Valley France landscape panorama",
        # Additional aerial shots
        "Loire Valley aerial shot France",
        "Loire Valley aerial drone châteaux",
        "Loire Valley aerial photograph castles",
        "Loire Valley bird's eye view",
        "Loire Valley landscape aerial overview",
        # Map searches
        "Loire Valley map France region",
        "Loire Valley map châteaux castles",
        "Loire Valley tourist map France",
        "Loire Valley geographic map",
        "map of Loire Valley France",
    ],

    "LONDON (POST 1666)": [
        # London post-1666 - after Great Fire, rebuilt city
        # St. Paul's Cathedral - Wren's masterpiece, symbol of rebuilt London
        "St Paul's Cathedral London cityscape skyline",
        "St Paul's dome London aerial view cityscape",
        "London St Paul's Cathedral Millennium Bridge cityscape",
        "St Paul's Cathedral London Thames cityscape",
        # Tower Bridge
        "Tower Bridge London cityscape aerial view",
        "London Tower Bridge Thames River cityscape",
        "Tower Bridge London skyline panorama",
        # Big Ben / Houses of Parliament
        "Big Ben London cityscape Westminster",
        "Houses of Parliament London aerial view Thames",
        "Westminster Palace London cityscape panorama",
        # The Shard / Modern London
        "The Shard London skyline cityscape aerial",
        "London skyline Shard modern cityscape",
        # City of London financial district
        "City of London skyline aerial view",
        "London financial district cityscape panorama",
        # Thames River views
        "London Thames River cityscape panorama",
        "London aerial view Thames cityscape",
        # General modern cityscape
        "London England cityscape aerial view",
        "London skyline panorama England",
        # Additional aerial shots
        "London aerial shot England",
        "London city aerial drone view",
        "London aerial photograph Thames",
        "London bird's eye view skyline",
        "London urban aerial panorama",
    ],

    "LONDON (PRE 1666)": [
        # London pre-1666 - before Great Fire, explicitly dated searches
        # Specific date qualifiers
        "London before 1666 cityscape",
        "London pre-1666 cityscape historical",
        "London before Great Fire 1666",
        "London 1600 cityscape",
        "London 1650 cityscape",
        "London 16th century cityscape",
        "London early 17th century cityscape",
        # Medieval London (pre-1485)
        "medieval London cityscape illustration 1400s",
        "medieval London cityscape 1500 Thames",
        "medieval London panorama before 1600",
        # Tudor London (1485-1603)
        "Tudor London cityscape 1500s illustration",
        "Tudor London cityscape 1600 historic",
        "London Tudor period cityscape Thames",
        # Stuart London (1603-1666)
        "Stuart London cityscape 1650 before fire",
        "London 1640s cityscape historical",
        "London 1660 before Great Fire cityscape",
        # Old London Bridge (medieval with houses, destroyed 1831)
        "Old London Bridge medieval houses 1600 cityscape",
        "London Bridge before 1666 houses Thames",
        "medieval London Bridge cityscape houses illustration",
        # Old St. Paul's Cathedral (destroyed in Great Fire)
        "Old St Paul's Cathedral London before 1666",
        "St Paul's Cathedral medieval London pre-fire",
        "Old St Paul's London Gothic before 1666",
        # Historical reconstructions with dates
        "London 1600 reconstruction aerial cityscape",
        "London medieval reconstruction before 1666",
        "pre-fire London 1665 cityscape reconstruction",
        # Tower of London (built 1066, still standing)
        "Tower of London medieval 1500s cityscape",
        "Tower of London 1600 aerial historic cityscape",
        # Westminster Abbey (medieval, still standing)
        "Westminster Abbey London medieval 1500s cityscape",
        "Westminster Abbey 1600 London historic aerial",
    ],

    "MADRID": [
        # Madrid - city, Spanish capital
        # Royal Palace - most iconic
        "Royal Palace Madrid cityscape Spain",
        "Palacio Real Madrid aerial view cityscape",
        "Madrid Royal Palace panorama Spain",
        "Madrid Palacio Real Plaza Oriente cityscape",
        # Plaza Mayor
        "Plaza Mayor Madrid cityscape Spain",
        "Madrid Plaza Mayor aerial view Spain",
        # Puerta del Sol
        "Puerta del Sol Madrid cityscape Spain",
        "Madrid Puerta Sol aerial view cityscape",
        # Gran Vía
        "Gran Vía Madrid cityscape Spain",
        "Madrid Gran Via skyline aerial view",
        "Gran Vía Madrid Spain panorama cityscape",
        # Retiro Park
        "Parque del Retiro Madrid aerial view cityscape",
        "Madrid Retiro Park cityscape Spain",
        # Skyline
        "Madrid Spain skyline aerial view",
        "Madrid cityscape panorama Spain",
        "Madrid skyline sunset Spain cityscape",
        # Cibeles
        "Plaza de Cibeles Madrid cityscape Spain",
        "Madrid Cibeles fountain cityscape aerial",
        # Additional aerial shots
        "Madrid aerial shot Spain",
        "Madrid city aerial drone view",
        "Madrid aerial photograph overview",
        "Madrid bird's eye view",
        "Madrid urban aerial panorama",
    ],

    "MOSCOW": [
        # Moscow - city, Russian capital
        # Kremlin and Red Square - most iconic
        "Kremlin Red Square Moscow cityscape Russia",
        "Moscow Kremlin aerial view Red Square",
        "Red Square Moscow St Basil's Cathedral cityscape",
        "Moscow Kremlin Red Square panorama Russia",
        "Kremlin Moscow cityscape aerial view",
        # St. Basil's Cathedral
        "St Basil's Cathedral Moscow Red Square cityscape",
        "Moscow St Basil's Cathedral aerial cityscape",
        "Saint Basil Moscow colorful domes cityscape",
        # Moscow State University
        "Moscow State University cityscape aerial view",
        "Lomonosov Moscow University Stalin skyscraper cityscape",
        # Moscow River views
        "Moscow River Kremlin cityscape aerial view",
        "Moscow cityscape along Moscow River",
        # Seven Sisters (Stalin skyscrapers)
        "Seven Sisters Moscow cityscape skyscrapers",
        "Stalin skyscrapers Moscow cityscape aerial",
        # General cityscape
        "Moscow Russia cityscape aerial view",
        "Moscow skyline panorama Russia",
        "Moscow cityscape Russia panorama",
        # Additional aerial shots
        "Moscow aerial shot Russia",
        "Moscow city aerial drone view",
        "Moscow aerial photograph Kremlin",
        "Moscow bird's eye view",
        "Moscow urban aerial panorama",
    ],

    "NEW YORK": [
        # New York City - iconic skyline
        # Statue of Liberty with Manhattan skyline
        "Statue of Liberty New York Manhattan skyline",
        "New York Statue Liberty aerial view cityscape",
        "Manhattan skyline Statue Liberty New York aerial",
        # Empire State Building
        "Empire State Building New York cityscape skyline",
        "New York Empire State aerial view Manhattan",
        "Manhattan Empire State Building cityscape panorama",
        # Manhattan skyline
        "Manhattan skyline New York aerial view",
        "New York City skyline Manhattan panorama",
        "Manhattan New York cityscape skyscrapers aerial",
        # Brooklyn Bridge
        "Brooklyn Bridge Manhattan skyline New York",
        "New York Brooklyn Bridge cityscape aerial view",
        "Brooklyn Bridge New York panorama cityscape",
        # Times Square aerial
        "Times Square New York aerial view cityscape",
        "New York Times Square cityscape panorama",
        # Central Park aerial
        "Central Park Manhattan aerial view New York",
        "New York Central Park cityscape aerial panorama",
        # General aerial
        "New York City aerial view skyline",
        "Manhattan aerial panorama New York",
        # Additional aerial shots
        "New York aerial shot",
        "Manhattan aerial drone view",
        "New York City aerial photograph",
        "Manhattan bird's eye view",
        "NYC urban aerial panorama",
    ],

    "OXFORD": [
        # Oxford - city, university colleges
        # Radcliffe Camera - most iconic
        "Radcliffe Camera Oxford cityscape England",
        "Oxford Radcliffe Camera aerial view colleges",
        "Radcliffe Camera Oxford England cityscape panorama",
        # Oxford colleges cityscape
        "Oxford University colleges aerial view England",
        "Oxford colleges spires cityscape panorama",
        "Oxford England colleges cityscape aerial",
        # Christ Church
        "Christ Church Oxford Tom Tower cityscape",
        "Oxford Christ Church cathedral cityscape aerial",
        # Bodleian Library
        "Bodleian Library Oxford cityscape England",
        "Oxford Bodleian aerial view cityscape",
        # High Street
        "High Street Oxford cityscape spires England",
        "Oxford High Street aerial view colleges",
        # Dreaming spires
        "Oxford dreaming spires cityscape England",
        "Oxford spires skyline England panorama",
        # City center
        "Oxford city center England aerial view",
        "Oxford England historic cityscape panorama",
        # General views
        "Oxford England cityscape aerial view",
        "Oxford cityscape colleges panorama",
        # Additional aerial shots
        "Oxford aerial shot England",
        "Oxford city aerial drone view",
        "Oxford aerial photograph spires",
        "Oxford bird's eye view colleges",
        "Oxford urban aerial panorama",
    ],

    "PADUA": [
        # Padua (Padova) - city, northern Italy
        # Basilica of Saint Anthony - most iconic
        "Basilica of Saint Anthony Padua cityscape Italy",
        "Basilica Sant'Antonio Padova aerial view",
        "Padua St Anthony Basilica cityscape panorama",
        "Basilica del Santo Padua cityscape Italy",
        # Prato della Valle
        "Prato della Valle Padua cityscape Italy",
        "Padova Prato della Valle aerial view",
        "Prato della Valle Padua square cityscape",
        # Palazzo della Ragione
        "Palazzo della Ragione Padua cityscape Italy",
        "Padova Palazzo Ragione aerial view",
        # Scrovegni Chapel area
        "Padua Scrovegni Chapel cityscape Italy",
        "Padova historic center aerial view",
        # University area
        "Padua University historic buildings cityscape",
        "University of Padua cityscape Italy",
        # Historic center
        "Padua historic center Italy cityscape aerial",
        "Padova Italy cityscape panorama",
        "Padua cityscape northern Italy aerial view",
        # Piazza dei Signori
        "Piazza dei Signori Padua cityscape Italy",
        # General views
        "Padua Italy cityscape aerial panorama",
        # Additional aerial shots
        "Padua aerial shot Italy",
        "Padova aerial drone view",
        "Padua aerial photograph overview",
        "Padua bird's eye view",
        "Padua urban aerial panorama",
    ],

    "PARIS (POST 1685)": [
        # Paris post-1685 - Baroque, Neoclassical, Modern Paris
        # Eiffel Tower - most iconic modern symbol
        "Eiffel Tower Paris cityscape aerial view",
        "Paris Eiffel Tower skyline panorama France",
        "Tour Eiffel Paris cityscape Seine River",
        "Eiffel Tower Paris aerial view Champ Mars",
        # Arc de Triomphe
        "Arc de Triomphe Paris cityscape Champs-Élysées",
        "Paris Arc Triomphe aerial view cityscape",
        "Arc de Triomphe Paris panorama France",
        # Sacré-Cœur
        "Sacré-Cœur Paris cityscape Montmartre",
        "Paris Sacre Coeur basilica aerial cityscape",
        "Sacré-Cœur Montmartre Paris panorama",
        # Les Invalides
        "Les Invalides Paris golden dome cityscape",
        "Paris Les Invalides aerial view France",
        # Louvre Pyramid (modern)
        "Louvre Pyramid Paris cityscape France",
        "Paris Louvre glass pyramid aerial view",
        # Seine River panoramas
        "Paris Seine River cityscape aerial panorama",
        "Seine River Paris bridges cityscape",
        # General cityscape
        "Paris France cityscape aerial view",
        "Paris skyline panorama France",
        # Additional aerial shots
        "Paris aerial shot France",
        "Paris city aerial drone view",
        "Paris aerial photograph Eiffel",
        "Paris bird's eye view",
        "Paris urban aerial panorama",
    ],

    "PARIS (PRE 1685)": [
        # Paris pre-1685 - explicitly dated searches
        # Specific date qualifiers
        "Paris before 1685 cityscape",
        "Paris pre-1685 cityscape historical",
        "Paris 1600 cityscape",
        "Paris 1650 cityscape",
        "Paris 16th century cityscape",
        "Paris early 17th century cityscape",
        "Paris 1680 cityscape historical",
        # Medieval Paris (pre-1500)
        "medieval Paris cityscape illustration 1400s",
        "medieval Paris cityscape 1500 Seine",
        "medieval Paris panorama before 1600",
        "Paris medieval 1450 cityscape",
        # Renaissance Paris (1500-1600)
        "Renaissance Paris cityscape 1550 illustration",
        "Paris Renaissance period 1580 cityscape",
        "Paris 1500s cityscape historic Seine",
        # Early Modern Paris (1600-1685)
        "Paris 1620 cityscape historical",
        "Paris 1650s cityscape before expansion",
        "Paris 1680 before Louis XIV expansion cityscape",
        # Notre-Dame Cathedral (construction completed 1345)
        "Notre-Dame Cathedral Paris medieval 1500s cityscape",
        "Notre-Dame Paris 1600 Île de la Cité aerial",
        "Paris Notre-Dame medieval Seine cityscape before 1685",
        # Sainte-Chapelle (built 1248)
        "Sainte-Chapelle Paris Gothic 1600 cityscape",
        "Paris Sainte Chapelle medieval Île de la Cité aerial",
        # Louvre as medieval fortress/palace (before 1682 expansion)
        "Louvre Palace medieval Paris 1600 cityscape",
        "Paris Louvre fortress 1650 historic cityscape",
        "Louvre before Louis XIV Paris 1680 aerial",
        # Pont Neuf (oldest standing bridge, built 1578-1607)
        "Pont Neuf Paris 1610 historic bridge cityscape",
        "Paris Pont Neuf Seine 1650 cityscape",
        # Place des Vosges (built 1605-1612)
        "Place des Vosges Paris 1620 historic square cityscape",
        "Paris Place des Vosges 17th century aerial",
        # Historical reconstructions with dates
        "Paris 1600 reconstruction aerial cityscape",
        "Paris medieval reconstruction before 1685",
        "pre-expansion Paris 1680 cityscape reconstruction",
        "Paris 1550 bird's eye view historic",
    ],

    "ROME": [
        # Rome - city, ancient and modern
        # Colosseum - most iconic
        "Colosseum Rome cityscape aerial view Italy",
        "Rome Colosseum cityscape panorama",
        "Colosseum Rome Forum cityscape aerial",
        "Rome Colosseo cityscape Italy",
        # St. Peter's Basilica and Vatican
        "St Peter's Basilica Rome Vatican cityscape aerial",
        "Rome St Peter's dome Vatican cityscape",
        "Vatican St Peter's Rome aerial view cityscape",
        # Roman Forum area
        "Roman Forum Rome cityscape aerial view",
        "Rome Forum Colosseum cityscape panorama",
        # Trevi Fountain
        "Trevi Fountain Rome cityscape Italy",
        "Rome Trevi Fountain aerial cityscape",
        # Pantheon
        "Pantheon Rome cityscape aerial view Italy",
        "Rome Pantheon cityscape Italy",
        # Seven Hills panorama
        "Rome seven hills cityscape panorama Italy",
        "Rome cityscape from Gianicolo Hill",
        # General cityscape
        "Rome Italy cityscape aerial view",
        "Rome skyline panorama Italy",
        "Roma cityscape aerial view Italy",
        # Additional aerial shots
        "Rome aerial shot Italy",
        "Rome city aerial drone view",
        "Rome aerial photograph Colosseum",
        "Rome bird's eye view",
        "Rome urban aerial panorama",
    ],

    "SAXONY": [
        # Saxony - German state
        # Dresden - Frauenkirche and Zwinger most iconic
        "Dresden Frauenkirche cityscape Saxony Germany",
        "Dresden Elbe River cityscape aerial Saxony",
        "Frauenkirche Dresden Saxony cityscape panorama",
        "Dresden baroque cityscape Saxony aerial view",
        # Leipzig
        "Leipzig Saxony cityscape aerial view Germany",
        "Leipzig city center Saxony Germany panorama",
        # Zwinger Palace Dresden
        "Zwinger Palace Dresden Saxony aerial cityscape",
        "Dresden Zwinger Saxony baroque cityscape",
        # Saxon Switzerland
        "Saxon Switzerland Saxony landscape aerial view",
        "Sächsische Schweiz Saxony landscape panorama",
        "Bastei Bridge Saxony landscape aerial Germany",
        # Moritzburg Castle
        "Moritzburg Castle Saxony aerial view Germany",
        "Schloss Moritzburg Saxony landscape",
        # Regional views
        "Saxony Germany landscape aerial view",
        "Saxony region Germany cityscape panorama",
        "Sachsen Germany countryside aerial view",
        # Dresden skyline
        "Dresden skyline Saxony Germany aerial",
        # Additional aerial shots
        "Saxony aerial shot Germany",
        "Dresden aerial drone view",
        "Saxony aerial photograph landscape",
        "Saxony bird's eye view cities",
        "Saxony regional aerial panorama",
        # Map searches
        "Saxony state map Germany",
        "Saxony map geographic regions",
        "Saxony historical map Sachsen",
        "Saxony map cities Dresden Leipzig",
        "map of Saxony Germany",
    ],

    "ST. PETERSBURG": [
        # St. Petersburg - city, Russian imperial capital
        # Winter Palace / Hermitage - most iconic
        "Winter Palace St Petersburg cityscape Russia",
        "Hermitage Museum St Petersburg aerial view",
        "St Petersburg Winter Palace Neva River cityscape",
        "Palace Square St Petersburg cityscape Russia",
        # Church of the Savior on Spilled Blood
        "Church Savior Spilled Blood St Petersburg cityscape",
        "St Petersburg Church Spilled Blood aerial view",
        "Savior on Blood St Petersburg Russia cityscape",
        # Peter and Paul Fortress
        "Peter and Paul Fortress St Petersburg cityscape",
        "St Petersburg Peter Paul Cathedral aerial view",
        # Nevsky Prospekt
        "Nevsky Prospekt St Petersburg cityscape Russia",
        "St Petersburg Nevsky Avenue aerial cityscape",
        # Canals
        "St Petersburg canals cityscape aerial view",
        "St Petersburg Russia canals Venice North cityscape",
        # Peterhof (nearby)
        "Peterhof Palace St Petersburg aerial view",
        "Peterhof fountains St Petersburg cityscape",
        # General cityscape
        "St Petersburg Russia cityscape aerial view",
        "St Petersburg skyline panorama Russia",
        "Sankt Petersburg cityscape Russia",
        # Additional aerial shots
        "St Petersburg aerial shot Russia",
        "St Petersburg aerial drone view",
        "St Petersburg aerial photograph",
        "St Petersburg bird's eye view",
        "St Petersburg urban aerial panorama",
    ],

    "SWITZERLAND": [
        # Switzerland - country, Alpine landscapes and cities
        # Matterhorn - most iconic natural landmark
        "Matterhorn Switzerland Alpine landscape aerial",
        "Switzerland Matterhorn mountain panorama Alps",
        "Matterhorn Zermatt Switzerland landscape aerial view",
        # Zurich cityscape
        "Zurich Switzerland cityscape aerial view",
        "Zurich lake cityscape Switzerland panorama",
        "Zürich Switzerland cityscape Alps background",
        # Geneva
        "Geneva Switzerland Lake Geneva cityscape aerial",
        "Geneva Jet d'Eau cityscape Switzerland",
        "Genève Switzerland cityscape lake panorama",
        # Bern
        "Bern Switzerland old town aerial cityscape",
        "Bern Switzerland Aare River cityscape panorama",
        "Bern Switzerland capital cityscape aerial view",
        # Lucerne
        "Lucerne Chapel Bridge Switzerland cityscape",
        "Luzern Switzerland lake cityscape panorama",
        "Lucerne Switzerland mountain cityscape aerial",
        # Alpine landscapes
        "Switzerland Alps landscape aerial panorama",
        "Swiss Alps villages landscape aerial view",
        "Switzerland mountain landscape panorama",
        # Country views
        "Switzerland landscape aerial view Alps",
        # Additional aerial shots
        "Switzerland aerial shot Alps",
        "Switzerland aerial drone view",
        "Switzerland aerial photograph mountains",
        "Switzerland bird's eye view cities",
        "Swiss landscape aerial panorama",
        # Map searches
        "Switzerland country map political",
        "Switzerland map cantons regions",
        "Switzerland map topographic Alps",
        "Switzerland map cities languages",
        "map of Switzerland Europe",
    ],

    "VENICE": [
        # Venice - city, canals and lagoon
        # St. Mark's Square - most iconic
        "St Mark's Square Venice aerial view cityscape",
        "Piazza San Marco Venice cityscape Italy",
        "Venice St Mark's Basilica campanile aerial cityscape",
        "San Marco Venice aerial view lagoon",
        # Grand Canal
        "Grand Canal Venice aerial view cityscape",
        "Venice Grand Canal Rialto Bridge cityscape",
        "Canal Grande Venice aerial cityscape Italy",
        "Venice Grand Canal aerial panorama",
        # Rialto Bridge
        "Rialto Bridge Venice Grand Canal cityscape",
        "Ponte di Rialto Venice aerial view",
        "Venice Rialto Bridge aerial cityscape Italy",
        # Aerial lagoon views
        "Venice Italy aerial view lagoon cityscape",
        "Venice lagoon aerial panorama Italy",
        "Venice canals aerial view cityscape Italy",
        # Doge's Palace
        "Doge's Palace Venice aerial cityscape",
        "Palazzo Ducale Venice St Mark's cityscape",
        # General aerial
        "Venice Italy cityscape aerial view",
        "Venezia aerial panorama Italy cityscape",
        # Additional aerial shots
        "Venice aerial shot Italy",
        "Venice aerial drone view lagoon",
        "Venice aerial photograph canals",
        "Venice bird's eye view",
        "Venice urban aerial panorama",
    ],

    "VIENNA": [
        # Vienna - city, imperial capital
        # Schönbrunn Palace - most iconic
        "Schönbrunn Palace Vienna cityscape Austria",
        "Vienna Schönbrunn aerial view gardens cityscape",
        "Schloss Schönbrunn Vienna Austria aerial panorama",
        # St. Stephen's Cathedral
        "St Stephen's Cathedral Vienna cityscape Austria",
        "Stephansdom Vienna aerial view cityscape",
        "Vienna St Stephen Cathedral cityscape Austria",
        # Hofburg Palace
        "Hofburg Palace Vienna cityscape Austria",
        "Vienna Hofburg aerial view cityscape",
        # Belvedere Palace
        "Belvedere Palace Vienna cityscape Austria",
        "Vienna Belvedere aerial view gardens",
        "Schloss Belvedere Vienna Austria cityscape",
        # Ringstrasse
        "Ringstrasse Vienna cityscape aerial Austria",
        "Vienna Ring Road boulevard aerial cityscape",
        "Vienna Ringstraße aerial panorama",
        # State Opera
        "Vienna State Opera cityscape Austria",
        "Staatsoper Vienna aerial view cityscape",
        # General cityscape
        "Vienna Austria cityscape aerial view",
        "Vienna skyline panorama Austria",
        "Wien cityscape aerial view Austria",
        # Additional aerial shots
        "Vienna aerial shot Austria",
        "Vienna city aerial drone view",
        "Vienna aerial photograph overview",
        "Vienna bird's eye view",
        "Wien urban aerial panorama",
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
