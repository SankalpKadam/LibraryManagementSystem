-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Apr 26, 2020 at 05:58 PM
-- Server version: 10.4.10-MariaDB
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `library_management`
--

-- --------------------------------------------------------

--
-- Table structure for table `book_add`
--

DROP TABLE IF EXISTS `book_add`;
CREATE TABLE IF NOT EXISTS `book_add` (
  `book_name` varchar(100) NOT NULL,
  `book_id` int(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `publisher` varchar(100) NOT NULL,
  `cost` varchar(100) NOT NULL,
  `category` varchar(100) NOT NULL,
  `attribute` varchar(100) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `book_add`
--

INSERT INTO `book_add` (`book_name`, `book_id`, `author`, `publisher`, `cost`, `category`, `attribute`) VALUES
('Money Heist', 4, 'Professor', 'Netflix', '4000', 'Thriller', 'Drama'),
('Tale of two Cities', 1, 'Sanaklp', 'samip', '1000', 'thriller', 'comic'),
('13 Reasons Why', 2, 'Hannah ', 'Bakers', '2000', 'Drama', 'Real Life');

-- --------------------------------------------------------

--
-- Table structure for table `book_issue`
--

DROP TABLE IF EXISTS `book_issue`;
CREATE TABLE IF NOT EXISTS `book_issue` (
  `book_id` int(100) NOT NULL,
  `book_name` varchar(100) NOT NULL,
  `publisher` varchar(100) NOT NULL,
  `attribute` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `cost` varchar(100) NOT NULL,
  `category` varchar(100) NOT NULL,
  `student_name` varchar(100) NOT NULL,
  `lib_id` varchar(100) NOT NULL,
  `issue_date` date NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `book_issue`
--

INSERT INTO `book_issue` (`book_id`, `book_name`, `publisher`, `attribute`, `author`, `cost`, `category`, `student_name`, `lib_id`, `issue_date`) VALUES
(2, '13 Reasons Why', 'Bakers', 'Real Life', 'Hannah ', '2000', 'Drama', 'Sankalp', '4323', '2020-04-15'),
(2, '13 Reasons Why', 'Bakers', 'Real Life', 'Hannah ', '2000', 'Drama', 'Samip', '3333', '2020-04-10');

-- --------------------------------------------------------

--
-- Table structure for table `book_return`
--

DROP TABLE IF EXISTS `book_return`;
CREATE TABLE IF NOT EXISTS `book_return` (
  `lib_id` varchar(100) NOT NULL,
  `book_name` varchar(100) NOT NULL,
  `student_name` varchar(100) NOT NULL,
  `book_id` int(100) NOT NULL,
  `issue_date` date NOT NULL,
  `return_date` date NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `book_return`
--

INSERT INTO `book_return` (`lib_id`, `book_name`, `student_name`, `book_id`, `issue_date`, `return_date`) VALUES
('lib1', 'book name', 'studentname', 4, '2014-08-01', '2020-04-21'),
('libid', 'book name', 'student name', 4, '2020-04-03', '2023-04-13'),
('libid', 'book name', 'student name', 4, '2020-04-03', '2020-04-24'),
('4333', 'corman', 'Jayesh', 4222, '2020-04-23', '2020-04-16'),
('3333', '13 Reasons Why', 'Samip', 2, '2020-04-10', '2020-04-17');

-- --------------------------------------------------------

--
-- Table structure for table `employee_info`
--

DROP TABLE IF EXISTS `employee_info`;
CREATE TABLE IF NOT EXISTS `employee_info` (
  `employee_name` varchar(100) NOT NULL,
  `contact_no` varchar(100) NOT NULL,
  `employee_id` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `employee_info`
--

INSERT INTO `employee_info` (`employee_name`, `contact_no`, `employee_id`, `address`) VALUES
('Salman Khan', '898987547', '5555', 'Mumbai'),
('Tom Cruise', '6565878754', '7777', 'USA');

-- --------------------------------------------------------

--
-- Table structure for table `student_info`
--

DROP TABLE IF EXISTS `student_info`;
CREATE TABLE IF NOT EXISTS `student_info` (
  `student_name` varchar(100) NOT NULL,
  `contact_no` varchar(100) NOT NULL,
  `lib_id` varchar(100) NOT NULL,
  `unique_id` varchar(100) NOT NULL,
  `course` varchar(100) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student_info`
--

INSERT INTO `student_info` (`student_name`, `contact_no`, `lib_id`, `unique_id`, `course`) VALUES
('Hritik Roshan', '9845788454', '3332', '9889', 'Computer'),
('Shahrukh Khan', '9898745478', '8812', '3321', 'IT');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
