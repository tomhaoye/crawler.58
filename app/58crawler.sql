/*
Navicat MySQL Data Transfer

Source Server         : homestead
Source Server Version : 50716
Source Host           : 192.168.10.10:3306
Source Database       : 58crawler

Target Server Type    : MYSQL
Target Server Version : 50716
File Encoding         : 65001

Date: 2018-06-25 00:18:29
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for area
-- ----------------------------
DROP TABLE IF EXISTS `area`;
CREATE TABLE `area` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `city_index` varchar(64) NOT NULL,
  `area_index` varchar(64) NOT NULL,
  `area_id` varchar(128) NOT NULL,
  `insert` tinyint(255) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=147 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for community
-- ----------------------------
DROP TABLE IF EXISTS `community`;
CREATE TABLE `community` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `listname` varchar(255) NOT NULL,
  `city_index` varchar(32) NOT NULL,
  `area_index` varchar(64) NOT NULL,
  `infoid` int(11) NOT NULL DEFAULT '0',
  `area_name` varchar(128) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `alias` varchar(255) NOT NULL,
  `subway` varchar(255) DEFAULT NULL,
  `shangquan` varchar(128) DEFAULT NULL,
  `price` int(11) NOT NULL DEFAULT '0',
  `completiontime` varchar(128) DEFAULT NULL,
  `detail_info` text,
  `lat_lon` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38323 DEFAULT CHARSET=utf8mb4;
