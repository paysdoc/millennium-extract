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
