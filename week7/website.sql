-- MySQL dump 10.13  Distrib 8.4.7, for macos15 (arm64)
--
-- Host: localhost    Database: website
-- ------------------------------------------------------
-- Server version	8.4.7

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `follower_count` int unsigned NOT NULL DEFAULT '0',
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `email_2` (`email`),
  KEY `idx_member_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES (1,'test2','test@test.com','test',0,'2025-11-12 00:01:48'),(2,'Alice','alice@example.com','pass123',5,'2025-11-12 01:15:00'),(3,'Bob','bob@example.com','secret456',12,'2025-11-13 06:30:00'),(4,'Cathy','cathy@example.com','mypwd789',3,'2025-11-14 03:45:00'),(5,'David','david@example.com','abc987',8,'2025-11-15 08:20:00'),(6,'Eva','eva@example.com','evepass321',7,'2025-11-15 06:00:00'),(7,'Frank','frank@example.com','frankie654',15,'2025-11-15 07:00:00'),(8,'Grace','grace@example.com','grace999',2,'2025-11-15 08:00:00'),(9,'Henry','henry@example.com','henry1234',9,'2025-11-15 09:00:00'),(10,'Ivy','ivy@example.com','ivypass456',4,'2025-11-15 10:00:00'),(11,'Jacky','jacky@example.com','jacky789',11,'2025-11-15 11:00:00'),(12,'Lily','lily@example.com','lilypass123',0,'2025-11-22 06:55:01'),(13,'Mark','mark@example.com','mark456',0,'2025-11-22 06:59:08'),(14,'Nina','nina@example.com','nina789',0,'2025-11-22 07:00:10'),(15,'Oscar','oscar@example.com','oscar321',0,'2025-11-22 07:05:48'),(16,'Paul','paul@example.com','paul654',0,'2025-11-22 09:49:07'),(17,'Quinn','quinn@example.com','quinn123',0,'2025-11-22 18:00:31'),(18,'Rachel','rachel@example.com','rachel456',0,'2025-11-29 11:49:01'),(19,'Tom','steve@example.com','steve789',0,'2025-11-29 11:53:08');
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `member_query`
--

DROP TABLE IF EXISTS `member_query`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member_query` (
  `id` int NOT NULL AUTO_INCREMENT,
  `member_id` int unsigned NOT NULL,
  `searcher_id` int unsigned NOT NULL,
  `time` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `idx_member_id` (`member_id`),
  KEY `idx_searcher_id` (`searcher_id`),
  KEY `idx_member_query_member` (`member_id`),
  KEY `idx_member_query_searcher` (`searcher_id`),
  CONSTRAINT `fk_member_id` FOREIGN KEY (`member_id`) REFERENCES `member` (`id`),
  CONSTRAINT `fk_searcher_id` FOREIGN KEY (`searcher_id`) REFERENCES `member` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=129 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member_query`
--

LOCK TABLES `member_query` WRITE;
/*!40000 ALTER TABLE `member_query` DISABLE KEYS */;
INSERT INTO `member_query` VALUES (1,3,5,'2025-11-24 02:15:42'),(2,3,5,'2025-11-24 02:15:42'),(3,1,2,'2025-11-24 03:00:11'),(4,7,3,'2025-11-24 04:20:55'),(5,3,5,'2025-11-24 02:15:42'),(6,1,2,'2025-11-24 02:18:10'),(7,7,3,'2025-11-24 02:21:35'),(8,10,6,'2025-11-24 02:25:12'),(9,14,12,'2025-11-24 02:30:01'),(10,2,8,'2025-11-24 02:33:27'),(11,5,11,'2025-11-24 02:36:50'),(12,9,4,'2025-11-24 02:40:15'),(13,6,13,'2025-11-24 02:43:42'),(14,8,1,'2025-11-24 02:47:08'),(15,11,10,'2025-11-24 02:50:30'),(16,4,7,'2025-11-24 02:53:55'),(17,12,9,'2025-11-24 02:57:18'),(18,15,2,'2025-11-24 03:00:40'),(19,16,14,'2025-11-24 03:04:05'),(20,13,8,'2025-11-24 03:07:28'),(21,17,5,'2025-11-24 03:10:50'),(22,2,12,'2025-11-24 03:14:15'),(23,5,3,'2025-11-24 03:17:42'),(24,1,6,'2025-11-24 03:21:05'),(25,7,11,'2025-11-24 03:24:28'),(26,10,2,'2025-11-24 03:27:50'),(27,14,9,'2025-11-24 03:31:12'),(28,3,8,'2025-11-24 03:34:40'),(29,6,1,'2025-11-24 03:38:05'),(30,9,15,'2025-11-24 03:41:28'),(31,8,4,'2025-11-24 03:44:55'),(32,11,7,'2025-11-24 03:48:20'),(33,4,16,'2025-11-24 03:51:42'),(34,12,5,'2025-11-24 03:55:08'),(35,15,13,'2025-11-24 03:58:30'),(36,16,10,'2025-11-24 04:01:55'),(37,13,2,'2025-11-24 04:05:18'),(38,17,12,'2025-11-24 04:08:40'),(39,2,6,'2025-11-24 04:12:05'),(40,5,3,'2025-11-24 04:15:28'),(41,1,14,'2025-11-24 04:18:55'),(42,7,9,'2025-11-24 04:22:20'),(43,10,8,'2025-11-24 04:25:42'),(44,14,1,'2025-11-24 04:29:05'),(45,3,7,'2025-11-24 04:32:28'),(46,6,4,'2025-11-24 04:35:55'),(47,9,5,'2025-11-24 04:39:20'),(48,8,11,'2025-11-24 04:42:42'),(49,11,2,'2025-11-24 04:46:05'),(50,4,12,'2025-11-24 04:49:28'),(51,12,3,'2025-11-24 04:52:55'),(52,15,6,'2025-11-24 04:56:20'),(53,16,10,'2025-11-24 04:59:42'),(54,13,9,'2025-11-24 05:03:05'),(55,17,1,'2025-11-24 05:06:28'),(56,2,14,'2025-11-24 05:09:55'),(57,5,7,'2025-11-24 05:13:20'),(58,1,13,'2025-11-24 05:16:42'),(59,7,5,'2025-11-24 05:20:05'),(60,10,2,'2025-11-24 05:23:28'),(61,14,11,'2025-11-24 05:26:55'),(62,3,6,'2025-11-24 05:30:20'),(63,6,8,'2025-11-24 05:33:42'),(64,9,15,'2025-11-24 05:37:05'),(65,8,4,'2025-11-24 05:40:28'),(66,11,7,'2025-11-24 05:43:55'),(67,4,16,'2025-11-24 05:47:20'),(68,12,5,'2025-11-24 05:50:42'),(69,15,13,'2025-11-24 05:54:05'),(70,16,10,'2025-11-24 05:57:28'),(71,13,2,'2025-11-24 06:00:55'),(72,17,12,'2025-11-24 06:04:20'),(73,2,6,'2025-11-24 06:07:42'),(74,5,3,'2025-11-24 06:11:05'),(75,1,14,'2025-11-24 06:14:28'),(76,7,9,'2025-11-24 06:17:55'),(77,10,8,'2025-11-24 06:21:20'),(78,14,1,'2025-11-24 06:24:42'),(79,3,7,'2025-11-24 06:28:05'),(80,6,4,'2025-11-24 06:31:28'),(81,9,5,'2025-11-24 06:34:55'),(82,8,11,'2025-11-24 06:38:20'),(83,11,2,'2025-11-24 06:41:42'),(84,4,12,'2025-11-24 06:45:05'),(85,12,3,'2025-11-24 06:48:28'),(86,15,6,'2025-11-24 06:51:55'),(87,16,10,'2025-11-24 06:55:20'),(88,13,9,'2025-11-24 06:58:42'),(89,17,1,'2025-11-24 07:02:05'),(90,2,14,'2025-11-24 07:05:28'),(91,5,7,'2025-11-24 07:08:55'),(92,1,13,'2025-11-24 07:12:20'),(93,7,5,'2025-11-24 07:15:42'),(94,10,2,'2025-11-24 07:19:05'),(95,14,11,'2025-11-24 07:22:28'),(96,3,6,'2025-11-24 07:25:55'),(97,6,8,'2025-11-24 07:29:20'),(98,9,15,'2025-11-24 07:32:42'),(99,8,4,'2025-11-24 07:36:05'),(100,11,7,'2025-11-24 07:39:28'),(101,4,16,'2025-11-24 07:42:55'),(102,12,5,'2025-11-24 07:46:20'),(103,15,13,'2025-11-24 07:49:42'),(104,16,10,'2025-11-24 07:53:05'),(105,13,2,'2025-11-24 07:56:28'),(106,17,12,'2025-11-24 07:59:55'),(107,2,6,'2025-11-24 08:03:20'),(108,5,3,'2025-11-24 08:06:42'),(109,1,14,'2025-11-24 08:10:05'),(110,7,9,'2025-11-24 08:13:28'),(111,10,8,'2025-11-24 08:16:55'),(112,14,1,'2025-11-24 08:20:20'),(113,3,7,'2025-11-24 08:23:42'),(114,6,4,'2025-11-24 08:27:05'),(115,9,5,'2025-11-24 08:30:28'),(116,8,11,'2025-11-24 08:33:55'),(117,11,2,'2025-11-24 08:37:20'),(118,4,12,'2025-11-24 08:40:42'),(119,12,3,'2025-11-24 08:44:05'),(120,15,6,'2025-11-24 08:47:28'),(121,16,10,'2025-11-24 08:50:55'),(122,13,9,'2025-11-24 08:54:20'),(123,17,1,'2025-11-24 08:57:42'),(124,10,11,'2025-11-29 19:45:19'),(125,17,18,'2025-11-29 19:49:37'),(126,1,19,'2025-11-29 19:53:41'),(127,2,19,'2025-11-29 19:53:47'),(128,11,5,'2025-11-29 20:31:49');
/*!40000 ALTER TABLE `member_query` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `message` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `member_id` int unsigned NOT NULL,
  `content` text NOT NULL,
  `like_count` int unsigned NOT NULL DEFAULT '0',
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `idx_member_id` (`member_id`),
  KEY `idx_message_id` (`id`),
  CONSTRAINT `message_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `member` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (1,1,'Test2 first post',0,'2025-11-12 01:00:00'),(2,2,'Alice first post',3,'2025-11-12 01:30:00'),(3,1,'Test2 second post',8,'2025-11-12 02:15:00'),(4,3,'Bob first post',6,'2025-11-13 07:00:00'),(5,1,'Test2 third post',8,'2025-11-13 08:00:00'),(6,4,'Cathy first post',2,'2025-11-14 04:00:00'),(7,5,'David first post',7,'2025-11-15 09:00:00'),(8,2,'Alice second post',8,'2025-11-15 10:00:00'),(9,3,'Bob second post',8,'2025-11-15 11:30:00'),(10,4,'Cathy second post',5,'2025-11-15 12:00:00'),(11,5,'David second post',0,'2025-11-16 00:00:00'),(12,2,'Alice third post',10,'2025-11-16 01:30:00'),(13,8,'Grace quick note',0,'2025-11-22 11:20:12'),(25,3,'Bob short message',0,'2025-11-22 15:19:27'),(26,3,'Bob new message',0,'2025-11-22 15:19:42'),(27,16,'Paul first post',0,'2025-11-22 15:44:23'),(46,7,'Frank lunch post',0,'2025-11-26 04:23:54');
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-11-29 21:11:31
