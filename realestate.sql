-- phpMyAdmin SQL Dump
-- version 3.3.7deb7
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generato il: 14 mar, 2013 at 12:50 PM
-- Versione MySQL: 5.1.66
-- Versione PHP: 5.3.3-7+squeeze15

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `realestate`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `adv`
--

CREATE TABLE IF NOT EXISTS `adv` (
  `id_adv` int(5) NOT NULL AUTO_INCREMENT,
  `id_user` int(4) NOT NULL,
  `date` date NOT NULL,
  `type` smallint(1) NOT NULL,
  `price` int(5) NOT NULL,
  PRIMARY KEY (`id_adv`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dump dei dati per la tabella `adv`
-- Comments: type is 0 or 1
--


-- --------------------------------------------------------

--
-- Struttura della tabella `contact`
--

CREATE TABLE IF NOT EXISTS `contact` (
  `id_contact` int(5) NOT NULL AUTO_INCREMENT,
  `id_adv` int(5) NOT NULL,
  `id_user_ins` int(4) NOT NULL,
  `id_user_read` int(4) NOT NULL,
  `date` date NOT NULL,
  `message` text NOT NULL,
  PRIMARY KEY (`id_contact`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dump dei dati per la tabella `contact`
-- Comments: id_user_inser is the id_user of the user that generated the adv, id_user_read is that of the user reading the adv
--


-- --------------------------------------------------------

--
-- Struttura della tabella `friend_list`
--

CREATE TABLE IF NOT EXISTS `friend_list` (
  `id_friend` int(5) NOT NULL AUTO_INCREMENT,
  `id_user` int(4) NOT NULL,
  `key_feature` varchar(20) NOT NULL,
  `value_feature` varchar(20) NOT NULL,
  `social` varchar(15) NOT NULL,
  PRIMARY KEY (`id_friend`,`id_user`,`key_feature`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dump dei dati per la tabella `friend_list`
-- Comments: key_feature is a feature that it is possible to save from a social network as name, username, pictures, etc; value_feature is the related value; social is the name of the considered social netowork (e.g.: facebook)
--




-- --------------------------------------------------------

--
-- Struttura della tabella `object`
--

CREATE TABLE IF NOT EXISTS `object` (
  `id_obj` int(3) NOT NULL AUTO_INCREMENT,
  `id_adv` int(4) NOT NULL,
  `key_feature` varchar(20) NOT NULL,
  `value_feature` varchar(20) NOT NULL,
  PRIMARY KEY (`id_obj`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dump dei dati per la tabella `object`
-- Comments: key_feature and value_feature allow to save all desidered features (e.g.: city, mq, nr of rooms) of a adv
--


-- --------------------------------------------------------

--
-- Struttura della tabella `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `id_user` int(3) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `password` varchar(8) NOT NULL,
  `f_name` varchar(20) NOT NULL,
  `l_name` varchar(20) NOT NULL,
  `photo` varchar(50) NOT NULL,
  `city` varchar(20) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `email` varchar(20) NOT NULL,
  `registration_date` date NOT NULL,
  PRIMARY KEY (`id_user`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dump dei dati per la tabella `user`
-- Comments: l_name and f_name are last name and first name respectively
--

