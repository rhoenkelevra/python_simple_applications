create database if not exists ex;

use ex;


CREATE TABLE `nagoya_population` (
  `id` int(11) NOT NULL,
  `year` smallint(6) NOT NULL,
  `population` int(11) NOT NULL,
  `elderly` int(11) NOT NULL,
  `young_old` int(11) NOT NULL,
  `old_old` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


INSERT INTO `nagoya_population` (`year`, `population`, `elderly`, `young_old`, `old_old`) VALUES
(2010, 2263894, 471879, 256719, 215160),
(2011, 2248630, 474878, 251426, 223452),
(2012, 2248985, 491461, 258646, 232815),
(2013, 2253639, 511034, 270498, 240536),
(2014, 2258958, 529837, 282399, 247438),
(2015, 2266791, 542757, 286229, 256528),
(2016, 2276121, 552255, 285242, 267013),
(2017, 2285628, 559802, 282132, 277670),
(2018, 2292160, 565551, 279471, 286080),
(2019, 2299748, 568882, 273750, 295132);



CREATE TABLE `test_average` (
  `id` int(11) NOT NULL,
  `class` varchar(4) NOT NULL,
  `japanese` float NOT NULL,
  `math` float NOT NULL,
  `science` float NOT NULL,
  `socialstudies` float NOT NULL,
  `english` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



INSERT INTO `test_average` (`id`, `class`, `japanese`, `math`, `science`, `socialstudies`, `english`) VALUES
(1, 'A', 60.3, 52.7, 80.5, 76.7, 64.7),
(2, 'B', 61.2, 66.8, 69.5, 71.3, 72.9);


ALTER TABLE `nagoya_population`
  ADD PRIMARY KEY (`id`);


ALTER TABLE `test_average`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `class` (`class`);


ALTER TABLE `nagoya_population`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;


ALTER TABLE `test_average`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;


