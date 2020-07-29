# Create tables
CREATE TABLE `swaps` (
  `uuid` char(36) NOT NULL,
  `started_at` datetime NOT NULL,
  `taker_coin` varchar(8) NOT NULL,
  `taker_amount` double(20,8) unsigned NOT NULL,
  `taker_gui` varchar(32) DEFAULT NULL,
  `taker_version` varchar(128) DEFAULT NULL,
  `taker_pubkey` varchar(64) DEFAULT NULL,
  `maker_coin` varchar(8) NOT NULL,
  `maker_amount` double(20,8) unsigned NOT NULL,
  `maker_gui` varchar(32) DEFAULT NULL,
  `maker_version` varchar(128) DEFAULT NULL,
  `maker_pubkey` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`uuid`),
  KEY `started_at` (`started_at`),
  KEY `maker_coin` (`maker_coin`),
  KEY `taker_coin` (`taker_coin`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `swaps_failed` (
  `uuid` char(36) NOT NULL,
  `started_at` datetime NOT NULL,
  `taker_coin` varchar(8) NOT NULL,
  `taker_amount` double(20,8) unsigned NOT NULL,
  `taker_error_type` varchar(32) DEFAULT NULL,
  `taker_error_msg` text,
  `taker_gui` varchar(32) DEFAULT NULL,
  `taker_version` varchar(128) DEFAULT NULL,
  `taker_pubkey` varchar(64) DEFAULT NULL,
  `maker_coin` varchar(8) NOT NULL,
  `maker_amount` double(20,8) unsigned NOT NULL,
  `maker_error_type` varchar(32) DEFAULT NULL,
  `maker_error_msg` text,
  `maker_gui` varchar(32) DEFAULT NULL,
  `maker_version` varchar(128) DEFAULT NULL,
  `maker_pubkey` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`uuid`),
  KEY `started_at` (`started_at`),
  KEY `maker_coin` (`maker_coin`),
  KEY `taker_coin` (`taker_coin`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
