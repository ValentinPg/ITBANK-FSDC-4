DROP TABLE IF EXISTS `direccion`;

CREATE TABLE `direccion` (
  `id` number primary key,
  `calle` varchar(255) default NULL,
  `pais` varchar(100) default NULL,
  `provincia` varchar(50) default NULL,
  `ciudad` varchar(255),
  `customer_id` mediumint default NULL,
  `employee_id` mediumint default NULL,
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=1;

INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("281-7437 Eros Avenue","Ireland","Munster","Cork",227,211),
  ("6920 Ligula. St.","Brazil","Bahia","Salvador",7,222),
  ("Ap #526-7380 Felis St.","Mexico","Chiapas","San Cristóbal de las Casas",395,245),
  ("6427 Nam Avenue","Belgium","Waals-Brabant","Tourinnes-la-Grosse",466,381),
  ("Ap #514-8351 Sit St.","South Africa","Limpopo","Giyani",271,24),
  ("Ap #580-8974 Vulputate, Ave","Netherlands","Overijssel","Zwolle",391,8),
  ("4342 Semper St.","Nigeria","Benue","Gboko",206,289),
  ("Ap #499-4251 Interdum. Rd.","China","Xīnán","Yunnan",293,431),
  ("471-2601 Ante. Ave","Vietnam","Quảng Nam","Tam Kỳ",182,368),
  ("Ap #504-493 Pede. Av.","South Korea","South Jeolla","Gwangyang",324,179);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("Ap #778-2055 Dolor St.","South Africa","Mpumalanga","Emalahleni",455,139),
  ("Ap #332-2963 Nunc Rd.","Indonesia","Lampung","Bandar Lampung",473,118),
  ("859-1638 Erat Road","Philippines","National Capital Region","Valenzuela",358,390),
  ("164-2713 Nulla. Rd.","Indonesia","Central Sulawesi","Palu",111,306),
  ("Ap #625-649 Montes, Road","Chile","Coquimbo","La Serena",361,31),
  ("270-8676 Quisque Rd.","Netherlands","Flevoland","Lelystad",201,411),
  ("Ap #606-8555 Sit St.","Italy","Abruzzo","Treglio",92,37),
  ("Ap #179-3720 Eget Road","Mexico","Michoacán","Zamora de Hidalgo",298,121),
  ("209-3931 Placerat. Rd.","Chile","Valparaíso","Cabildo",138,165),
  ("Ap #311-1193 Elit, Street","France","Centre","Chartres",471,461);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("Ap #805-3047 Id Street","Mexico","Chihuahua","Hidalgo del Parral",140,257),
  ("313-6193 Ligula. Street","Peru","Cusco","Sicuani",260,191),
  ("Ap #692-9112 Ut Avenue","Peru","Ancash","Huaraz",118,27),
  ("701-6703 Nullam Avenue","Chile","Los Lagos","San Pablo",462,405),
  ("441-6863 Mauris Avenue","Belgium","West-Vlaanderen","Nieuwmunster",433,472),
  ("P.O. Box 575, 9105 Nulla Ave","South Africa","Limpopo","Seshego",494,333),
  ("723-9826 Sit Ave","South Korea","Gangwon","Gangneung",163,168),
  ("494-1934 Mollis. Street","Indonesia","West Sulawesi","Mamuju",200,37),
  ("551 Ultricies Av.","Ireland","Connacht","Galway",352,473),
  ("Ap #626-9753 Non, Rd.","Germany","Brandenburg","Oranienburg",399,66);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("6969 Libero. St.","Belgium","Brussels Hoofdstedelijk Gewest","Ukkel",435,48),
  ("Ap #165-1650 Cursus Rd.","Spain","Navarra","Pamplona",448,50),
  ("P.O. Box 436, 7925 Aliquam Road","Germany","Rheinland-Pfalz","Pirmasens",88,387),
  ("617-6228 Neque Avenue","Philippines","Davao Region","Panabo",157,23),
  ("P.O. Box 307, 2856 Donec Rd.","Australia","Tasmania","Launceston",102,473),
  ("Ap #482-817 Molestie Av.","Poland","Mazowieckie","Płock",407,182),
  ("P.O. Box 444, 3794 Adipiscing, Avenue","Turkey","Adana","Ceyhan",128,331),
  ("5917 Est, Av.","United Kingdom","Cumberland","Workington",454,426),
  ("Ap #249-812 Fusce St.","South Korea","South Gyeongsang","Cheonan",333,327),
  ("Ap #870-3730 Blandit Rd.","Italy","Trentino-Alto Adige","Bolzano/Bozen",288,267);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("349-1359 Ridiculus Ave","Vietnam","Lai Châu","Tam Đường",181,461),
  ("Ap #162-3476 Sapien. Rd.","United States","Texas","San Antonio",110,170),
  ("P.O. Box 469, 7403 Nulla Ave","Indonesia","Central Java","Semarang",7,61),
  ("Ap #594-5892 Quisque Avenue","Canada","Nova Scotia","New Glasgow",421,411),
  ("Ap #383-3706 Molestie St.","Spain","Melilla","Melilla",33,248),
  ("Ap #966-203 Erat Rd.","Russian Federation","Saint Petersburg City","Saint Petersburg",319,225),
  ("P.O. Box 383, 5329 Tempor Ave","Singapore","North Region","Mandai",270,231),
  ("605-9990 At Av.","Germany","Baden Württemberg","Esslingen",5,437),
  ("868-7826 Auctor St.","South Korea","South Gyeongsang","Tongyeong",280,140),
  ("5129 Eget Av.","Canada","Ontario","Lakeshore",60,96);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("Ap #428-6073 A St.","Ireland","Leinster","Dublin",309,215),
  ("Ap #229-5971 Habitant Ave","Brazil","Rio de Janeiro","São Gonçalo",118,427),
  ("P.O. Box 167, 9272 Tempor Rd.","Poland","Dolnośląskie","Wrocław",29,172),
  ("133-6609 Lorem Rd.","Costa Rica","Puntarenas","Barranca",498,25),
  ("Ap #790-6005 Nunc Avenue","Philippines","Northern Mindanao","Gingoog",449,170),
  ("Ap #206-9462 Et Rd.","Belgium","Oost-Vlaanderen","Afsnee",430,121),
  ("P.O. Box 326, 7032 Dapibus Road","Italy","Piemonte","Villar Pellice",440,2),
  ("Ap #238-1529 Vivamus Rd.","Vietnam","Nam Định","Gôi",38,421),
  ("644-3200 Nisl Av.","China","Huádōng","Anhui",348,459),
  ("458-9840 Eget, Rd.","Colombia","Valle del Cauca","Cali",340,127);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("440-7502 Lacus. Rd.","Turkey","Balıkesir","Gönen",188,210),
  ("375-989 Ac Av.","Sweden","Västra Götalands län","Borås",371,2),
  ("P.O. Box 770, 5428 Turpis. Rd.","China","Huádōng","Shandong",292,160),
  ("P.O. Box 445, 2055 Aliquam Ave","China","Huáběi","Hebei",363,84),
  ("572-7494 Adipiscing St.","Italy","Marche","Pergola",167,392),
  ("551-2002 Risus. Rd.","Sweden","Stockholms län","Åkersberga",144,332),
  ("Ap #429-9647 Auctor, St.","South Africa","Limpopo","Thabazimbi",31,459),
  ("360-470 Dolor. St.","Russian Federation","Bryansk Oblast","Dyatkovo",439,181),
  ("9077 Fusce Rd.","New Zealand","North Island","Pukekohe",136,348),
  ("Ap #260-7529 Facilisis Avenue","Pakistan","Khyber Pakhtoonkhwa","Peshawar",33,453);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("258-8456 Congue Street","Brazil","Bahia","Camaçari",451,225),
  ("Ap #755-3327 Imperdiet Av.","China","Huádōng","Zhejiang",124,341),
  ("8343 Magnis Ave","Belgium","Oost-Vlaanderen","Sint-Gillis-bij-Dendermonde",454,417),
  ("Ap #524-1934 Donec St.","Colombia","Guainía","Barranco Minas",358,177),
  ("P.O. Box 149, 6116 Odio. Rd.","Singapore","East Region","Changi Bay",129,154),
  ("533-3470 Lacus. Rd.","Ireland","Leinster","Dublin",8,232),
  ("8757 Mauris Av.","Sweden","Jönköpings län","Jönköping",455,339),
  ("P.O. Box 975, 1189 Faucibus Ave","Indonesia","Central Sulawesi","Palu",105,404),
  ("126-138 Nulla Avenue","Colombia","Meta","Villavicencio",233,442),
  ("3381 Nisl. Rd.","Poland","Warmińsko-mazurskie","Elbląg",310,377);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("Ap #706-4846 Nec St.","Ukraine","Kirovohrad oblast","Oleksandriia",381,244),
  ("868-7683 Curabitur Road","Nigeria","Oyo","Oyo",420,175),
  ("312-698 Nullam Rd.","Chile","Tarapacá","Alto Hospicio",211,288),
  ("913-1181 Facilisis. St.","Mexico","Tabasco","Villahermosa",307,442),
  ("Ap #380-6867 Augue St.","Singapore","West Region","Choa Chu Kang",173,88),
  ("P.O. Box 944, 1562 Nunc Avenue","France","Franche-Comté","Montbéliard",49,308),
  ("413-2407 Sem Av.","Chile","O'Higgins","San Vicente",152,386),
  ("Ap #200-7819 Maecenas St.","Pakistan","Khyber Pakhtoonkhwa","Kohistan",108,467),
  ("Ap #231-692 Nibh. Avenue","Spain","Castilla - La Mancha","Guadalajara",145,356),
  ("Ap #553-1530 Consectetuer Rd.","Costa Rica","Puntarenas","Barranca",350,349);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("1857 Orci Avenue","Pakistan","Punjab","Rawalpindi",41,334),
  ("2681 Aptent Street","Ukraine","Kirovohrad oblast","Oleksandriia",310,190),
  ("Ap #184-7979 Blandit St.","Austria","Lower Austria","Schwechat",35,366),
  ("366-6549 Cursus Road","Netherlands","Noord Holland","Laren",79,434),
  ("283-7441 Enim Street","Colombia","Vichada","Cumaribo",138,232),
  ("Ap #319-1837 Pretium St.","France","Pays de la Loire","La Roche-sur-Yon",60,26),
  ("721-8732 Et Avenue","United Kingdom","Worcestershire","Dudley",12,305),
  ("P.O. Box 217, 4200 Euismod Rd.","Italy","Piemonte","Olivola",272,355),
  ("Ap #111-9225 Vestibulum Rd.","Peru","Cajamarca","Jaén",309,206),
  ("877-6477 Risus. Av.","Sweden","Västra Götalands län","Göteborg",66,255);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("930-516 Ante. Road","Peru","Loreto","Yurimaguas",482,377),
  ("Ap #816-2928 Mus. Street","Canada","British Columbia","Dawson Creek",364,94),
  ("Ap #442-6147 Auctor Avenue","Nigeria","Niger","Bida",436,164),
  ("Ap #104-1543 Velit. Rd.","Russian Federation","Magadan Oblast","Magadan",15,203),
  ("P.O. Box 248, 6290 Magnis St.","Austria","Burgenland","Rechnitz",28,334),
  ("159-7573 Suscipit St.","Indonesia","Maluku","Tual",302,212),
  ("8719 Nibh Street","Austria","Lower Austria","Ternitz",413,356),
  ("8348 Est, Avenue","Colombia","Santander","Piedecuesta",281,211),
  ("760-8025 Lacinia. St.","New Zealand","South Island","Temuka",146,246),
  ("Ap #497-1033 Mauris Ave","Canada","Manitoba","Stonewall",409,55);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("Ap #876-7113 Et Rd.","Nigeria","Katsina","Katsina",365,323),
  ("497-9863 Sem Ave","Germany","Schleswig-Holstein","Neumünster",31,308),
  ("487-7394 Eu Avenue","Canada","New Brunswick","Dieppe",49,405),
  ("8965 Gravida. Street","Belgium","West-Vlaanderen","Assebroek",328,5),
  ("Ap #141-4688 Orci Av.","Peru","Puno","Puno",453,30),
  ("279-6982 Nulla Rd.","China","Xīnán","Tibet",421,124),
  ("664-6969 Ipsum. St.","Ukraine","Chernivtsi oblast","Vashkivtsi",314,168),
  ("Ap #444-8295 Facilisis. Rd.","Philippines","Eastern Visayas","Baybay",310,254),
  ("889-685 Tortor, Ave","South Korea","South Jeolla","Suncheon",324,412),
  ("P.O. Box 749, 3650 Mauris St.","Peru","Piura","Sullana",418,355);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("963-5565 Fermentum Ave","Poland","Pomorskie","Gdynia",478,144),
  ("Ap #800-2266 Felis. Av.","Nigeria","Delta","Sapele",166,248),
  ("Ap #676-659 Vestibulum, Ave","Turkey","Manisa","Soma",262,490),
  ("956-569 Magnis Rd.","Norway","Rogaland","Stavanger",40,455),
  ("2518 Nunc Rd.","South Korea","North Gyeongsang","Gyeongju",101,312),
  ("Ap #542-9749 Pharetra Ave","Pakistan","Gilgit Baltistan","Gojal Upper Hunza",241,74),
  ("7689 Amet, Street","Indonesia","Riau Islands","Tanjung Pinang",125,458),
  ("Ap #651-4321 Nullam Ave","Ukraine","Dnipropetrovsk oblast","Nikopol",16,369),
  ("Ap #385-8704 Dis Avenue","Indonesia","Bangka Belitung Islands","Pangkalpinang",58,362),
  ("917-5203 Non, Road","Mexico","Coahuila","Acuña",85,300);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("Ap #982-654 Leo. Ave","Mexico","Veracruz","Minatitlán",137,64),
  ("Ap #610-2450 Sem. Rd.","Pakistan","FATA","Khyber Agency",43,60),
  ("Ap #979-8688 Sed Street","Ukraine","Kharkiv oblast","Izium",84,475),
  ("P.O. Box 764, 7556 Semper St.","Sweden","Stockholms län","Åkersberga",144,201),
  ("Ap #952-3366 Suspendisse Road","Mexico","Veracruz","Córdoba",191,222),
  ("175-1149 Pharetra. Road","France","Bretagne","Saint-Malo",90,149),
  ("852-7582 Duis Rd.","Poland","Mazowieckie","Warszawa",41,192),
  ("850-4755 Nullam Road","South Korea","South Gyeongsang","Busan",59,392),
  ("Ap #224-9015 Aliquet Street","Sweden","Jönköpings län","Nässjö",498,232),
  ("295-1992 Hendrerit. St.","Colombia","Córdoba","Montelíbano",126,328);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("4772 Pretium Rd.","United States","Alabama","Mobile",17,428),
  ("Ap #609-5086 Nam Av.","Philippines","Northern Mindanao","Oroquieta",448,11),
  ("Ap #535-3811 Maecenas Rd.","Canada","British Columbia","Silverton",374,154),
  ("Ap #796-3293 Quis St.","Ukraine","Chernihiv oblast","Chernihiv",171,473),
  ("P.O. Box 878, 8145 Mi Rd.","Germany","Nordrhein-Westphalen","Mönchengladbach",60,21),
  ("129-2319 Aliquam Av.","Nigeria","Sokoto","Sokoto",195,159),
  ("971-1504 Proin St.","Chile","Atacama","Caldera",482,342),
  ("Ap #242-4994 Sem Ave","New Zealand","North Island","Waitara",221,210),
  ("P.O. Box 753, 9523 Non St.","Sweden","Dalarnas län","Mora",469,495),
  ("1522 Nec, Rd.","Singapore","West Region","Western Islands",133,83);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("P.O. Box 619, 3757 Lorem. Rd.","Nigeria","Oyo","Ibadan",408,402),
  ("406-1622 Elit St.","India","Mizoram","Aizwal",230,343),
  ("Ap #302-8509 Vulputate Avenue","India","Karnataka","Bijapur",195,60),
  ("Ap #345-394 Erat Rd.","Belgium","Luxemburg","Lamorteau",7,451),
  ("Ap #313-5824 Et Rd.","Colombia","Huila","Pitalito",157,483),
  ("752-4970 Blandit St.","Pakistan","Khyber Pakhtoonkhwa","Lakki Marwat",96,234),
  ("214-6630 Malesuada Av.","Russian Federation","Bryansk Oblast","Mglin",267,458),
  ("Ap #802-113 Donec Av.","Italy","Trentino-Alto Adige","Laives/Leifers",260,335),
  ("7383 Nonummy Rd.","Turkey","Konya","Ereğli",383,419),
  ("546-6671 Pellentesque Rd.","Nigeria","Ogun","Ijebu Ode",175,305);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("3346 Molestie Street","China","Xīběi","Shaanxi",231,74),
  ("Ap #449-7329 Facilisis, St.","Vietnam","Ninh Thuận","Phan Rang–Tháp Chàm",44,451),
  ("924-7893 Pellentesque St.","Sweden","Jönköpings län","Vetlanda",378,350),
  ("Ap #665-8812 Dui. Avenue","Netherlands","Noord Brabant","Grave",37,124),
  ("P.O. Box 914, 2360 Et Rd.","South Africa","Northern Cape","Kuruman",13,414),
  ("6818 Aliquam Av.","Peru","Lima","Mala",471,65),
  ("773-1411 Consectetuer Road","Peru","Lima","San Vicente de Cañete",135,310),
  ("521-3810 At St.","Poland","Sląskie","Sosnowiec",390,39),
  ("Ap #898-8618 Eros. Road","Vietnam","Tiền Giang","Mỹ Tho",354,51),
  ("469-897 Neque. Road","Colombia","Chocó","Quibdó",429,233);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("Ap #520-4697 Ante Rd.","Australia","Northern Territory","Darwin",316,123),
  ("697-8818 Vel, St.","Sweden","Östergötlands län","Mjölby",183,324),
  ("126-319 Libero. Rd.","Germany","Bayern","Fürth",360,253),
  ("P.O. Box 790, 9267 Id, St.","United States","Mississippi","Hattiesburg",264,11),
  ("537-6232 Praesent Avenue","China","Xīnán","Chongqing",390,118),
  ("Ap #420-2916 Nec Rd.","Sweden","Stockholms län","Märsta",24,419),
  ("255-7116 Mollis. Street","New Zealand","North Island","Porirua",262,327),
  ("P.O. Box 279, 2498 Justo Road","Mexico","Michoacán","Morelia",91,90),
  ("Ap #408-5622 Sit St.","United States","Pennsylvania","Philadelphia",311,128),
  ("8788 Id Av.","Colombia","Guaviare","Calamar",311,34);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("P.O. Box 909, 8068 Et Av.","Russian Federation","Novosibirsk Oblast","Novosibirsk",36,257),
  ("Ap #251-2996 Blandit Av.","Chile","Los Ríos","Lanco",294,167),
  ("215-9248 Enim, Avenue","Italy","Valle d'Aosta","Rhemes-Saint-Georges",181,286),
  ("1052 Etiam Av.","Austria","Carinthia","Klagenfurt",105,360),
  ("P.O. Box 294, 3294 Volutpat. St.","Ireland","Leinster","Dublin",260,28),
  ("Ap #192-1389 Tincidunt Av.","Colombia","Valle del Cauca","Cali",132,171),
  ("Ap #654-7018 Lorem, Road","Italy","Emilia-Romagna","Sant'Agata sul Santerno",458,156),
  ("P.O. Box 449, 7396 Faucibus Avenue","Italy","Trentino-Alto Adige","Campitello di Fassa",435,337),
  ("P.O. Box 572, 1582 Morbi Ave","South Korea","Gangwon","Wonju",304,433),
  ("5476 Gravida Av.","Chile","Aisén","Tortel",39,106);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("Ap #927-2712 Nibh Ave","Brazil","Paraíba","Sousa",227,317),
  ("Ap #961-923 Ipsum. St.","Canada","Newfoundland and Labrador","St. John's",132,106),
  ("7727 Urna. Avenue","Italy","Valle d'Aosta","Pollein",443,154),
  ("1274 Urna. Rd.","Poland","Dolnośląskie","Wrocław",276,219),
  ("Ap #521-404 Cras Road","Costa Rica","Alajuela","Quesada",150,321),
  ("Ap #278-7641 Mi Rd.","Australia","Victoria","Belgrave",132,228),
  ("1060 Mauris Avenue","Poland","Dolnośląskie","Wałbrzych",144,279),
  ("Ap #831-4089 Tristique Rd.","Sweden","Östergötlands län","Norrköping",403,35),
  ("Ap #936-9998 Dis St.","India","Uttarakhand","Haridwar",110,206),
  ("P.O. Box 530, 3445 Pede St.","India","Lakshadweep","Kavaratti",124,312);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("Ap #318-4704 Mi Ave","Belgium","West-Vlaanderen","Kortrijk",334,178),
  ("974-805 Nullam Rd.","Indonesia","Banten","Serang",196,254),
  ("8113 Amet Street","Pakistan","Sindh","Jacobabad",331,51),
  ("9361 Vitae, St.","Sweden","Dalarnas län","Mora",485,451),
  ("881-5093 Mi Av.","Brazil","Rio de Janeiro","Campos dos Goytacazes",54,261),
  ("Ap #652-1240 Risus. St.","Canada","Nova Scotia","Pictou",376,37),
  ("Ap #519-6412 Sagittis. Road","Pakistan","Balochistan","Awaran",328,180),
  ("Ap #139-5799 Gravida Ave","South Africa","North West","Mmabatho",434,479),
  ("733-9475 Tellus Av.","Australia","Tasmania","Burnie",194,20),
  ("2655 Nulla St.","France","Pays de la Loire","Rezé",347,330);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("3216 Nisi Av.","Australia","Victoria","Mildura",395,172),
  ("P.O. Box 753, 8191 At Road","Belgium","Vlaams-Brabant","Dilbeek",212,283),
  ("883-1827 Massa. Rd.","Australia","Western Australia","Mandurah",369,347),
  ("Ap #860-8158 Placerat, St.","Colombia","Cundinamarca","Mosquera",231,277),
  ("P.O. Box 122, 961 Urna Ave","United States","Georgia","Georgia",229,299),
  ("726-5641 Nascetur Av.","Spain","Navarra","Pamplona",144,158),
  ("P.O. Box 897, 7287 Nec Road","Turkey","Kahramanmaraş","Afşin",130,137),
  ("435-4071 Libero. Rd.","Sweden","Stockholms län","Stockholm",436,110),
  ("P.O. Box 763, 4698 Semper Rd.","Belgium","Waals-Brabant","Plancenoit",262,37),
  ("Ap #578-7187 Mi Road","Russian Federation","Omsk Oblast","Omsk",446,33);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("Ap #956-6806 Blandit Avenue","Philippines","Ilocos Region","Candon",352,290),
  ("8053 Tincidunt Street","Sweden","Västra Götalands län","Göteborg",84,190),
  ("905-8896 Gravida Av.","South Korea","North Chungcheong","Chungju",373,393),
  ("430-6775 Felis. Rd.","France","Bourgogne","Mâcon",392,21),
  ("Ap #142-262 Et St.","Sweden","Stockholms län","Upplands Väsby",288,328),
  ("376-7543 Massa. Street","Brazil","Ceará","Caucaia",219,244),
  ("321-9548 Risus. Rd.","Belgium","Luxemburg","Vaux-lez-Rosieres",256,22),
  ("Ap #143-4950 Non St.","Sweden","Östergötlands län","Motala",334,195),
  ("380-9196 Amet, Road","Vietnam","Quảng Nam","Tam Kỳ",460,329),
  ("500-8098 Mauris Road","Philippines","Northern Mindanao","El Salvador",18,257);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("Ap #629-7127 Sed Road","Ukraine","Mykolaiv oblast","Mykolaiv",339,425),
  ("Ap #723-8731 Metus. Rd.","Singapore","West Region","Choa Chu Kang",4,202),
  ("555 Mi. Road","United States","Pennsylvania","Harrisburg",78,454),
  ("P.O. Box 986, 2798 Nec Ave","Ukraine","Odessa oblast","Odessa",18,96),
  ("849-9690 Diam St.","Australia","Australian Capital Territory","Canberra",204,296),
  ("4263 Ipsum St.","Brazil","Santa Catarina","Chapecó",64,370),
  ("109-7987 Nisi Rd.","Mexico","Yucatán","Mérida",188,398),
  ("865-6404 Facilisis Road","India","Daman and Diu","Daman",242,194),
  ("534-3167 Taciti Av.","Indonesia","South Sulawesi","Palopo",344,393),
  ("Ap #967-1452 A, Ave","Spain","Extremadura","Cáceres",24,29);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("752-5948 Bibendum Rd.","France","Midi-Pyrénées","Tournefeuille",88,413),
  ("397-3195 Fringilla Av.","Sweden","Östergötlands län","Linköping",267,370),
  ("Ap #163-1517 Egestas Ave","Costa Rica","San José","San Felipe",498,383),
  ("Ap #242-3806 Nunc Road","France","Île-de-France","Montreuil",402,233),
  ("2071 Neque Road","Peru","Lambayeque","Chiclayo",478,469),
  ("7171 Erat Rd.","New Zealand","North Island","Masterton",305,355),
  ("3037 Non St.","Norway","Trøndelag","Trondheim",319,49),
  ("934-8418 A Rd.","Canada","New Brunswick","Moncton",356,256),
  ("190-2756 Nisi Rd.","Ukraine","Chernihiv oblast","Nizhyn",18,203),
  ("Ap #314-6188 Pretium St.","Spain","Comunitat Valenciana","Torrevieja",327,358);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("P.O. Box 869, 2516 Sagittis. Av.","Australia","New South Wales","Lithgow",469,428),
  ("6177 Mollis. Rd.","Pakistan","Balochistan","Kacchi",189,265),
  ("7189 Lectus Rd.","Italy","Marche","Falerone",320,244),
  ("Ap #991-6672 Non Av.","Chile","Arica y Parinacota","Putre",284,100),
  ("Ap #138-2831 Libero. St.","Russian Federation","Magadan Oblast","Magadan",121,473),
  ("663-2829 Sem Ave","Norway","Vestfold og Telemark","Porsgrunn",3,223),
  ("P.O. Box 496, 4475 Nullam Rd.","Pakistan","Punjab","Jhelum",242,95),
  ("465-1523 Egestas. St.","Turkey","Aydın","Nazilli",148,230),
  ("615-6449 Consequat, Ave","Germany","Sachsen","Bautzen",459,474),
  ("Ap #430-3146 Proin Ave","Turkey","Van","Erciş",417,2);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("8335 Ultrices. Rd.","Spain","Aragón","Huesca",133,43),
  ("975 Pede, Rd.","Philippines","Davao Region","Panabo",187,379),
  ("Ap #406-4675 Libero Road","India","Meghalaya","Shillong",272,405),
  ("Ap #559-1895 Elit. Av.","Canada","New Brunswick","Miramichi",214,13),
  ("Ap #615-8539 Amet, Rd.","Ireland","Ulster","Belfast",336,465),
  ("605-4160 Et, Road","Belgium","Luik","Comblain-Fairon",397,290),
  ("P.O. Box 799, 1516 Ultrices Ave","Poland","Kujawsko-pomorskie","Toruń",65,289),
  ("630-9390 Id, St.","South Africa","North West","Rustenburg",84,112),
  ("Ap #487-6000 Non Av.","Ukraine","Donetsk oblast","Sloviansk",194,419),
  ("8510 Suspendisse Road","Pakistan","Gilgit Baltistan","Gilgit",237,177);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("P.O. Box 154, 2669 Tempor Avenue","Turkey","Adana","Kozan",356,79),
  ("Ap #528-5158 Suspendisse Road","Poland","Lubuskie","Zielona Góra",339,155),
  ("2712 Turpis Avenue","Indonesia","East Java","Mojokerto",294,65),
  ("6394 Aenean Rd.","South Africa","Limpopo","Phalaborwa",403,426),
  ("Ap #964-9557 At Rd.","Mexico","Hidalgo","Pachuca",112,370),
  ("237-7137 Maecenas Road","Canada","British Columbia","Langley",432,407),
  ("987-184 Velit Rd.","Pakistan","Sindh","Karachi",367,334),
  ("3559 Orci, Street","France","Corse","Bastia",482,71),
  ("Ap #971-7468 Cras Av.","France","Nord-Pas-de-Calais","Roubaix",2,77),
  ("402-3603 Donec Street","Singapore","North Region","Sembawang",477,388);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("Ap #877-1995 Inceptos St.","South Korea","North Jeolla","Jeonju",249,233),
  ("131-5132 Sociosqu Av.","Russian Federation","Chelyabinsk Oblast","Magnitogorsk",80,259),
  ("P.O. Box 120, 1429 Mattis. Street","Poland","Sląskie","Częstochowa",223,105),
  ("Ap #496-3131 Sed Av.","Pakistan","Sindh","Hyderabad",75,469),
  ("P.O. Box 941, 8638 A St.","Netherlands","Zuid Holland","Gorinchem",504,177),
  ("4126 Pretium Rd.","Norway","Trøndelag","Orkanger",308,1),
  ("3496 Est Rd.","Russian Federation","Arkhangelsk Oblast","Mezen",295,429),
  ("Ap #607-3258 Nibh Av.","South Africa","Northern Cape","Port Nolloth",389,184),
  ("P.O. Box 760, 2081 Elit Ave","Brazil","Goiás","Anápolis",475,362),
  ("Ap #730-3819 Elementum, Rd.","Italy","Lazio","Monte San Giovanni in Sabina",385,315);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("P.O. Box 945, 8463 Egestas Rd.","Russian Federation","Kostroma Oblast","Kostroma",491,377),
  ("Ap #902-443 Consectetuer Rd.","Austria","Vorarlberg","Bludenz",430,175),
  ("Ap #394-8420 Tristique Av.","Chile","Tarapacá","Alto Hospicio",123,149),
  ("2669 Scelerisque Ave","Russian Federation","Nizhny Novgorod Oblast","Nizhny",61,16),
  ("P.O. Box 600, 8909 Non, Avenue","India","Maharastra","Akola",505,337),
  ("2162 Commodo Rd.","Brazil","Goiás","Rio Verde",199,271),
  ("Ap #745-8603 Quis, Ave","Vietnam","Hồ Chí Minh City","Hồ Chí Minh City",27,130),
  ("6505 Leo. Rd.","Pakistan","Punjab","Chiniot",256,335),
  ("278-2571 Ridiculus St.","Netherlands","Utrecht","Amersfoort",279,348),
  ("5410 Ut Ave","Brazil","Bahia","Camaçari",134,485);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("Ap #577-7240 Ultrices, Road","Ukraine","Chernivtsi oblast","Vashkivtsi",336,476),
  ("276-1736 Penatibus St.","Sweden","Östergötlands län","Linköping",88,492),
  ("Ap #519-7530 Mauris. Rd.","Netherlands","Flevoland","Almere",205,406),
  ("958-5477 Sit Rd.","South Africa","Gauteng","Roodepoort",101,196),
  ("7407 Odio, Av.","Costa Rica","Alajuela","Quesada",111,108),
  ("437-8471 Ornare, St.","Philippines","Central Luzon","Malolos",378,492),
  ("P.O. Box 139, 9625 Dui. Road","Spain","Andalucía","Algeciras",430,11),
  ("1750 Ipsum Road","Brazil","Pernambuco","Recife",270,339),
  ("Ap #483-8401 Massa. St.","Philippines","Calabarzon","San Pedro",294,232),
  ("5276 Cum Av.","India","Meghalaya","Shillong",164,272);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("715-7065 Ultrices St.","Norway","Agder","Flekkefjord",53,331),
  ("197-4501 Eu St.","Brazil","São Paulo","Guarulhos",340,473),
  ("2075 Adipiscing. Road","France","Picardie","Creil",198,16),
  ("Ap #867-5439 Mauris, Road","Colombia","Vaupés","Mitú",280,115),
  ("183-2317 Eget Road","Russian Federation","Kursk Oblast","Kursk",317,474),
  ("Ap #903-8617 Dolor St.","United States","Idaho","Pocatello",74,223),
  ("887-4133 Dui. Ave","Brazil","Bahia","Ilhéus",329,128),
  ("7320 Blandit Road","Costa Rica","Guanacaste","Nicoya",108,258),
  ("179-1100 Egestas, Street","Costa Rica","Heredia","Ulloa (Barrial]",410,18),
  ("Ap #267-9438 Nec Ave","Germany","Bayern","Nuremberg",247,290);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("Ap #589-2988 Non Ave","Australia","Western Australia","Mandurah",214,344),
  ("P.O. Box 430, 8808 Ut St.","Nigeria","Kano","Kano",232,378),
  ("3733 A, Rd.","Russian Federation","Novgorod Oblast","Novgorod",168,290),
  ("7031 Non Av.","Belgium","Vlaams-Brabant","Strijtem",212,175),
  ("P.O. Box 176, 5257 Egestas Av.","Philippines","Central Luzon","San Jose del Monte",388,469),
  ("Ap #183-8021 Cursus Avenue","Peru","Loreto","Iquitos",435,226),
  ("P.O. Box 583, 5193 Sed Road","United States","Alabama","Birmingham",334,218),
  ("P.O. Box 553, 506 Blandit Street","Singapore","West Region","Western Water Catchment",479,216),
  ("Ap #289-1640 Dui, Ave","Nigeria","Akwa Ibom","Uyo",81,45),
  ("6537 Ut Avenue","Nigeria","Niger","Bida",400,389);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("524-4909 Neque St.","Pakistan","Khyber Pakhtoonkhwa","Peshawar",46,367),
  ("Ap #403-3893 Elementum, Ave","Ukraine","Mykolaiv oblast","Pervomaisk",466,493),
  ("Ap #405-532 Felis Avenue","South Korea","South Gyeongsang","Jinju",457,92),
  ("989-1805 Urna Rd.","Austria","Styria","Weiz",505,471),
  ("Ap #701-3954 Interdum. Ave","South Africa","Free State","Bloemfontein",250,395),
  ("Ap #200-2929 Tempor Street","United States","Pennsylvania","Allentown",144,236),
  ("7165 Justo. St.","Russian Federation","Tambov Oblast","Tambov",66,118),
  ("225-1583 Eros Avenue","South Korea","Gyeonggi","Incheon",192,169),
  ("Ap #220-7784 Nulla Street","India","Uttarakhand","Haridwar",434,368),
  ("374-2620 Ut Rd.","Netherlands","Overijssel","Almelo",219,187);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("911-9376 Duis St.","Mexico","Mexico City","Mexico City",471,33),
  ("Ap #266-1295 Tellus. Rd.","Italy","Marche","Ostra Vetere",308,389),
  ("Ap #164-2788 Proin Rd.","Germany","Bayern","Erlangen",348,159),
  ("270-3271 Dignissim Road","United Kingdom","Kincardineshire","Inverbervie",228,294),
  ("P.O. Box 600, 5617 In St.","Russian Federation","Moscow City","Moscow",499,352),
  ("7607 Egestas Av.","Peru","Junín","Huancayo",376,328),
  ("P.O. Box 577, 7768 Elit Rd.","Spain","Aragón","Huesca",81,330),
  ("P.O. Box 544, 1477 Eu Street","Belgium","Oost-Vlaanderen","Kruibeke",415,104),
  ("Ap #748-4272 Vitae Street","Norway","Vestfold og Telemark","Holmestrand",369,324),
  ("4708 Mi Rd.","Singapore","East Region","Pasir Ris",319,499);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("123-7986 Nec Rd.","Sweden","Västra Götalands län","Vänersborg",254,199),
  ("4007 Eu, Ave","Sweden","Västra Götalands län","Skövde",68,345),
  ("3727 Eu Street","Ukraine","Chernivtsi oblast","Chernivtsi",275,381),
  ("Ap #220-2837 Purus. Rd.","Ireland","Munster","Cork",13,321),
  ("Ap #118-8914 Rutrum. Rd.","South Africa","Western Cape","Constantia",146,391),
  ("580 Donec Street","Spain","Galicia","Pontevedra",383,102),
  ("327-5053 Vitae, Avenue","Ireland","Connacht","Galway",386,52),
  ("3083 Nec, Av.","New Zealand","North Island","Auckland",437,6),
  ("4801 Arcu. Rd.","South Korea","North Gyeongsang","Cheongju",281,478),
  ("552-5956 Egestas. Street","Austria","Lower Austria","Amstetten",423,460);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("Ap #697-425 Sed, Rd.","Australia","Northern Territory","Palmerston",153,420),
  ("Ap #939-5372 Enim. Ave","Costa Rica","Heredia","Heredia",174,415),
  ("7817 Varius Ave","Brazil","Goiás","Rio Verde",342,208),
  ("Ap #828-7803 Ut, St.","Australia","Northern Territory","Palmerston",469,164),
  ("Ap #397-9443 Orci Ave","Mexico","Sinaloa","Culiacán",340,153),
  ("6281 Ante. Street","Costa Rica","Alajuela","Alajuela",375,269),
  ("Ap #507-3982 Nostra, St.","South Korea","South Gyeongsang","Ulsan",448,389),
  ("Ap #961-821 Pellentesque Avenue","Nigeria","Bauchi","Bauchi",215,63),
  ("Ap #675-6477 Eu Rd.","Ireland","Leinster","Dublin",139,47),
  ("Ap #792-7106 Et Rd.","China","Xīběi","Ningxia",297,361);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("Ap #268-8365 Pede Rd.","Germany","Nordrhein-Westphalen","Mülheim",166,338),
  ("935-4625 Pellentesque. Street","Italy","Valle d'Aosta","Ayas",251,483),
  ("614-2655 Id Street","Peru","Ancash","Huaraz",407,324),
  ("Ap #921-1791 Neque Street","Belgium","Brussels Hoofdstedelijk Gewest","Vorst",202,419),
  ("234-1919 Dolor. Street","Philippines","Western Visayas","San Carlos",134,2),
  ("P.O. Box 743, 2004 Eros Av.","Ireland","Leinster","Dublin",360,235),
  ("Ap #521-5182 Blandit St.","Germany","Niedersachsen","Salzgitter",109,94),
  ("3321 Lectus Rd.","Austria","Burgenland","Rechnitz",400,321),
  ("6558 Diam Av.","Colombia","Cauca","El Tambo",53,401),
  ("Ap #290-6944 Sit St.","China","Zhōngnán","Henan",225,319);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("8773 Proin Ave","Pakistan","Punjab","Khanewal",134,344),
  ("Ap #346-5437 Purus. Street","Mexico","Guanajuato","Salamanca",201,4),
  ("5636 Nunc, Ave","Spain","Murcia","Cartagena",102,385),
  ("7884 Luctus St.","Netherlands","Flevoland","Lelystad",347,93),
  ("1481 Ultricies Rd.","Nigeria","Bauchi","Bauchi",289,280),
  ("Ap #485-8065 Ante Rd.","China","Xīnán","Chongqing",78,408),
  ("426-7289 Mi Rd.","Peru","Ancash","Huaraz",86,452),
  ("Ap #807-3081 Eros. Rd.","Norway","Vestfold og Telemark","Sandefjord",139,116),
  ("Ap #532-4502 In Street","Austria","Salzburg","Wals-Siezenheim",289,170),
  ("764 Mauris Rd.","Brazil","Rio Grande do Sul","Pelotas",398,440);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("Ap #994-3411 Habitant Av.","Philippines","Central Visayas","Tanjay",499,164),
  ("P.O. Box 135, 1260 Nullam Road","Philippines","Soccsksargen","Koronadal",483,116),
  ("Ap #496-9380 Nam St.","India","Mizoram","Aizwal",409,250),
  ("Ap #833-6552 Euismod Street","Mexico","Veracruz","Boca del Río",173,47),
  ("P.O. Box 860, 5291 Ultrices Avenue","United States","Mississippi","Southaven",395,276),
  ("Ap #988-3387 Dui. Rd.","Ukraine","Zakarpattia oblast","Uzhhorod",236,129),
  ("P.O. Box 194, 5350 Leo. Road","Pakistan","Punjab","Mianwali",2,115),
  ("566-7886 Magna. St.","Brazil","Paraná","Ponta Grossa",47,27),
  ("745-3747 Vulputate St.","Netherlands","Noord Holland","Haarlem",399,25),
  ("668-285 Semper Av.","Canada","New Brunswick","Campbellton",336,152);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("Ap #476-9078 Morbi Av.","Norway","Nordland","Mo i Rana",334,55),
  ("Ap #937-2083 Lorem Avenue","New Zealand","North Island","Levin",79,458),
  ("P.O. Box 973, 6307 Ut Rd.","Norway","Troms og Finnmark","Harstad",351,451),
  ("Ap #491-5265 Cursus St.","Nigeria","Benue","Gboko",200,391),
  ("209-5915 Quis Street","South Korea","South Chungcheong","Gongju",31,472),
  ("139-2369 Tellus Rd.","Ukraine","Volyn oblast","Lutsk",97,198),
  ("772-821 Libero Street","Mexico","San Luis Potosí","Ciudad Valles",271,466),
  ("2877 Pede, Street","Ukraine","Vinnytsia oblast","Vinnytsia",283,310),
  ("Ap #555-7361 Pharetra Road","Singapore","North-East Region","Sengkang",207,322),
  ("711-7476 Accumsan Rd.","Norway","Oslo","Oslo",303,6);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("Ap #789-6017 Class Road","Germany","Bayern","Landshut",7,330),
  ("1450 Velit. St.","Italy","Campania","San Pietro al Tanagro",476,212),
  ("4559 Neque. St.","China","Huádōng","Shandong",465,310),
  ("Ap #359-4896 Velit Road","China","Xīnán","Chongqing",433,212),
  ("Ap #736-1217 Eu Rd.","Chile","Antofagasta","San Pedro de Atacama",178,451),
  ("511-9292 Dui. St.","Russian Federation","Astrakhan Oblast","Kamyzyak",415,299),
  ("238-6446 Urna St.","Poland","Mazowieckie","Warszawa",385,159),
  ("385-8900 Ipsum Ave","Pakistan","Sindh","Qambar Shahdadkot",351,8),
  ("Ap #516-6993 Urna. Ave","France","Provence-Alpes-Côte d'Azur","La Seyne-sur-Mer",244,417),
  ("P.O. Box 745, 6238 Semper Rd.","France","Languedoc-Roussillon","Nîmes",172,189);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("Ap #510-9111 Dui. Road","Chile","Araucanía","Pitrufquén",106,151),
  ("Ap #632-3833 Hendrerit St.","Spain","Illes Balears","Palma de Mallorca",505,390),
  ("1775 Tempus Avenue","Chile","Magallanes y Antártica Chilena","Timaukel",284,42),
  ("2359 Vitae Rd.","Italy","Sicilia","Caccamo",2,214),
  ("Ap #592-4848 At, Rd.","New Zealand","North Island","Waitakere",344,122),
  ("261-2874 Interdum. St.","Colombia","Distrito Capital","Bogotá",190,160),
  ("Ap #548-3021 Pellentesque Avenue","India","West Bengal","Krishnanagar",457,152),
  ("P.O. Box 449, 1851 Mauris Ave","Vietnam","Yên Bái","Yên Bái",17,159),
  ("P.O. Box 355, 1188 Quis, Road","United Kingdom","Perthshire","Pitlochry",150,375),
  ("5436 Hymenaeos. Road","Singapore","Central Region","Novena",489,339);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("697-7240 Et Avenue","Brazil","Minas Gerais","Montes Claros",176,6),
  ("697-5368 Vel, Rd.","Costa Rica","Alajuela","Alajuela",339,188),
  ("Ap #134-157 Aliquam Av.","Nigeria","Kano","Kano",224,222),
  ("Ap #693-3824 Ante Ave","Philippines","Western Visayas","Passi",436,213),
  ("P.O. Box 372, 6332 Vivamus Street","Indonesia","Southeast Sulawesi","Kendari",420,180),
  ("Ap #963-5556 Sed Street","Costa Rica","Limón","Siquirres",339,368),
  ("P.O. Box 804, 5299 Lectus Street","Ukraine","Ivano-Frankivsk oblast","Ivano-Frankivsk",394,203),
  ("1626 Eu Rd.","New Zealand","South Island","Picton",482,103),
  ("7766 Risus Ave","Italy","Sicilia","Pace del Mela",336,71),
  ("P.O. Box 346, 2485 Ipsum Ave","Spain","Melilla","Melilla",348,129);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("187-6005 Hendrerit. Rd.","Pakistan","Azad Kashmir","Mirpur",53,146),
  ("637-4000 Ligula. Road","Turkey","Adana","Adana",230,188),
  ("519-1445 Placerat, Road","Costa Rica","Heredia","San Pablo",464,343),
  ("P.O. Box 104, 7592 Tempor Ave","South Africa","North West","Rustenburg",377,9),
  ("P.O. Box 537, 8875 Senectus St.","Spain","Illes Balears","Palma de Mallorca",100,367),
  ("P.O. Box 768, 5184 Enim, Street","Poland","Mazowieckie","Warszawa",417,194),
  ("628-1624 Mattis Rd.","Nigeria","Bauchi","Bauchi",413,253),
  ("Ap #274-2385 Tincidunt St.","Germany","Nordrhein-Westphalen","Dortmund",121,204),
  ("Ap #846-3045 Ut Ave","Chile","Coquimbo","Monte Patria",204,177),
  ("558 Vivamus St.","China","Xīběi","Xinjiang",256,421);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("734-7045 Est, St.","Turkey","İzmir","Tire",335,216),
  ("3779 Dapibus Av.","China","Xīnán","Sichuan",228,258),
  ("732-1798 Vitae Av.","Italy","Sicilia","Acquedolci",190,267),
  ("Ap #944-6368 Bibendum St.","Pakistan","Gilgit Baltistan","Nagar",118,35),
  ("P.O. Box 887, 2326 Tincidunt Road","Italy","Abruzzo","Ofena",453,10),
  ("P.O. Box 573, 7778 Sit Road","United Kingdom","Somerset","Yeovil",114,52),
  ("4389 Leo, Av.","China","Huádōng","Zhejiang",112,419),
  ("491-3043 Tincidunt Av.","Australia","Victoria","Belgrave",71,337),
  ("680-8921 Sem. Av.","Ukraine","Volyn oblast","Lutsk",376,106),
  ("650-447 Est Street","Italy","Calabria","Marcedusa",435,39);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("P.O. Box 680, 6231 Eu, Street","Ukraine","Odessa oblast","Izmail",230,438),
  ("819-8155 Urna. Av.","Netherlands","Flevoland","Almere",300,341),
  ("6001 Erat Ave","Russian Federation","Belgorod Oblast","Borisovka",9,358),
  ("4529 In, Rd.","Canada","Manitoba","Flin Flon",92,486),
  ("139-1637 Id Street","Colombia","Magdalena","Plato",378,122),
  ("630-6305 Semper. Rd.","Austria","Salzburg","Wals-Siezenheim",129,168),
  ("947-9748 Penatibus St.","Ukraine","Volyn oblast","Lutsk",312,274),
  ("254-535 Ac Street","United Kingdom","Worcestershire","Stourbridge",445,179),
  ("472-4461 Eget St.","United States","Colorado","Denver",337,216),
  ("Ap #423-9139 Phasellus Rd.","Poland","Sląskie","Częstochowa",421,104);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("Ap #876-3536 Porta Street","United States","Tennessee","Chattanooga",82,121),
  ("Ap #856-5789 Nisl. Rd.","Colombia","Huila","Garzón",106,179),
  ("105 Congue. Road","Pakistan","FATA","North Waziristan",122,302),
  ("Ap #394-9607 Duis Av.","Ireland","Ulster","Belfast",6,101),
  ("P.O. Box 471, 5003 Aliquet St.","United States","Mississippi","Hattiesburg",151,91),
  ("944-3502 Amet Street","South Africa","Northern Cape","Kimberley",24,87),
  ("173-8177 Nec Ave","Germany","Sachsen","Hoyerswerda",389,270),
  ("5201 Lorem St.","Costa Rica","San José","Patalillo",429,101),
  ("Ap #873-3965 Felis, Street","Ireland","Munster","Cork",341,384),
  ("P.O. Box 704, 2820 Neque Av.","Turkey","Mersin","Silifke",167,77);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("Ap #179-7249 A Street","Netherlands","Noord Brabant","Breda",428,5),
  ("P.O. Box 220, 9648 Lectus Street","Italy","Friuli-Venezia Giulia","Socchieve",498,471),
  ("Ap #731-2921 Mauris Road","Australia","New South Wales","Goulburn",364,19),
  ("P.O. Box 379, 3149 Dictum Av.","Indonesia","Central Java","Semarang",33,165),
  ("855-1038 Sed, Ave","Ireland","Connacht","Galway",240,32),
  ("8635 Etiam Street","South Korea","South Jeolla","Suncheon",484,37),
  ("Ap #408-1028 Quisque Ave","Poland","Sląskie","Katowice",188,106),
  ("P.O. Box 737, 7674 Aliquam Street","Indonesia","West Java","Bogor",44,129),
  ("P.O. Box 935, 5663 Neque. St.","Russian Federation","Lipetsk Oblast","Lipetsk",45,263),
  ("P.O. Box 604, 378 Purus. Av.","Poland","Pomorskie","Gdańsk",277,362);
INSERT INTO `direccion` (`calle`,`pais`,`provincia`,`ciudad`,`customer_id`,`employee_id`)
VALUES
  ("3166 Pede. Rd.","Brazil","Paraíba","Santa Rita",304,169),
  ("143-7144 Ante St.","Vietnam","Đắk Nông","Gia Nghĩa",85,167),
  ("796-2434 Sed St.","South Korea","South Jeolla","Mokpo",208,41),
  ("826-2079 Leo. St.","Nigeria","Niger","Minna",429,244),
  ("Ap #994-2915 Id, Avenue","Philippines","National Capital Region","Valenzuela",77,474),
  ("P.O. Box 438, 597 Turpis Ave","Australia","South Australia","Port Pirie",29,65),
  ("954-8402 Donec Road","Pakistan","Punjab","Faisalabad",73,296),
  ("P.O. Box 858, 4364 Lorem Rd.","Chile","Tarapacá","Pica",205,176),
  ("540-1858 Dolor Road","United States","Georgia","Savannah",249,414),
  ("Ap #158-7888 Mauris St.","China","Huádōng","Jiangxi",266,299);
