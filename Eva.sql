-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Client :  localhost:3306
-- Généré le :  Lun 21 Octobre 2019 à 18:47
-- Version du serveur :  5.7.27-0ubuntu0.18.04.1
-- Version de PHP :  7.2.19-0ubuntu0.18.04.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `Eva`
--

-- --------------------------------------------------------

--
-- Structure de la table `answer`
--

CREATE TABLE `answer` (
  `id` int(11) NOT NULL,
  `sequence` text NOT NULL,
  `type` varchar(75) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Contenu de la table `answer`
--

INSERT INTO `answer` (`id`, `sequence`, `type`) VALUES
(1, 'Que puis-je faire pour vous ?', 'listen\n'),
(2, 'Oui, Monsieur?', 'listen\n'),
(3, 'Je suis là.', 'listen\n'),
(4, 'Monsieur?', 'listen\n'),
(5, 'Vous m\'avez Appelé?', 'listen\n'),
(6, 'M\'auriez vous appelé?', 'listen\n'),
(7, 'Oui patron?', 'listen\n'),
(8, 'Oui boss?', 'listen\n'),
(9, 'Un instant s\'il vous plait.', 'load\n'),
(10, 'je m\'en occupe.', 'load\n'),
(11, 'Je suis une intelligence artificielle développé dans le but de répondre à des requêtes bien spécifique. En outre, je suis aussi capable d\'apprendre. Ma premiere version a vue le jour le Dimanche 13 Octobre.', 'whoEva\n'),
(12, 'Je m\'appelle éva. Je suis une I A permettant de répondre aux questions qui me sont posé. Je cherche à apprendre de ce que je sais deja monsieur.', 'whoEva\n'),
(13, 'Jeune génie,riche, play-boy et misanthrope. Mais les gens ont tendance à vous Appeler Yassine', 'whoIam\n'),
(14, 'De ce que je sais: Yassine, Monsieur', 'whoIam\n');

-- --------------------------------------------------------

--
-- Structure de la table `command`
--

CREATE TABLE `command` (
  `id` int(11) NOT NULL,
  `sequence` text NOT NULL,
  `idRecognition` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Contenu de la table `command`
--

INSERT INTO `command` (`id`, `sequence`, `idRecognition`) VALUES
(1, 'quel jour sommes-nous', 3),
(2, 'quel jour serons-nous demain', 4),
(3, 'quel jour etions-nous hier', 5),
(4, 'donne-moi le jour d\'hier', 5),
(5, 'Quel jour etions-nous hier', 5),
(6, 'Dans combien de jour nous serons le', 1),
(7, 'dis-moi quelle date nous sommes', 3),
(8, 'quel jour serons-nous demain', 4),
(9, 'dis-moi quel jour nous serons demain', 4),
(10, 'quel jour sommes-nous aujourd\'hui', 3),
(11, 'dis-moi quel jour nous sommes aujourd\'hui', 3),
(12, 'dis-moi quel jour nous sommes', 3),
(13, 'qui est Eva', 7),
(14, 'dis-moi qui est Eva', 7),
(15, 'dis-moi qui es-tu', 7),
(16, 'qui es-tu', 7),
(17, 'qui suis-je', 6),
(18, 'présente-moi', 6),
(19, 'dis-moi qui je suis', 6),
(20, 'dis-moi qui suis-je', 6),
(21, 'qui es-tu qui es-tu', 7),
(22, 'qui suis-je qui suis-je', 6),
(23, 'Recherche sur Wikipedia', 11),
(24, 'Wikipedia', 11),
(25, 'Trouves moi quelque chose sur Wikipedia', 11),
(26, 'cherche sur Wikipédia', 11),
(27, 'lance une recherche sur Wikipédia', 11),
(28, 'effectuer une recherche sur Wikipédia', 11);

-- --------------------------------------------------------

--
-- Structure de la table `myClass`
--

CREATE TABLE `myClass` (
  `id` int(11) NOT NULL,
  `name` varchar(75) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Contenu de la table `myClass`
--

INSERT INTO `myClass` (`id`, `name`) VALUES
(4, 'DateInformation\n'),
(5, 'Boss\n'),
(6, 'WikiSearch\n');

-- --------------------------------------------------------

--
-- Structure de la table `recognition`
--

CREATE TABLE `recognition` (
  `id` int(11) NOT NULL,
  `methodName` varchar(75) NOT NULL,
  `idMyClass` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Contenu de la table `recognition`
--

INSERT INTO `recognition` (`id`, `methodName`, `idMyClass`) VALUES
(1, 'getDayAtdate', 4),
(2, 'getDifferenceBetweenDate', 4),
(3, 'getToday', 4),
(4, 'getTomorrow', 4),
(5, 'getYesterday', 4),
(6, 'getPresentation', 5),
(7, 'mySelfPresentation', 5),
(8, 'whoEva', 5),
(9, 'whoIam', 5),
(10, 'GetAudio', 6),
(11, 'getSearchWikipedia', 6);

--
-- Index pour les tables exportées
--

--
-- Index pour la table `answer`
--
ALTER TABLE `answer`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `command`
--
ALTER TABLE `command`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `idRecognition` (`idRecognition`);

--
-- Index pour la table `myClass`
--
ALTER TABLE `myClass`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `recognition`
--
ALTER TABLE `recognition`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ClassName` (`idMyClass`);

--
-- AUTO_INCREMENT pour les tables exportées
--

--
-- AUTO_INCREMENT pour la table `answer`
--
ALTER TABLE `answer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
--
-- AUTO_INCREMENT pour la table `command`
--
ALTER TABLE `command`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;
--
-- AUTO_INCREMENT pour la table `myClass`
--
ALTER TABLE `myClass`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT pour la table `recognition`
--
ALTER TABLE `recognition`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
