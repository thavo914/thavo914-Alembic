# CREATE TABLE alembic_version (
#     version_num VARCHAR(32) NOT NULL,
#     CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
# );

-- Running upgrade  -> 5f0ccb076f5f

# CREATE TABLE account (
#     id INTEGER NOT NULL AUTO_INCREMENT,
#     name VARCHAR(50) NOT NULL,
#     description VARCHAR(200),
#     PRIMARY KEY (id)
# );
#
# INSERT INTO alembic_version (version_num) VALUES ('5f0ccb076f5f');
#
# -- Running upgrade 5f0ccb076f5f -> d4808f157a34
#
# ALTER TABLE account ADD COLUMN last_transaction_date DATETIME;
#
# UPDATE alembic_version SET version_num='d4808f157a34' WHERE alembic_version.version_num = '5f0ccb076f5f';
#
# -- Running upgrade d4808f157a34 -> e234eedc0f1b
#
# DROP TABLE account;



# UPDATE alembic_version SET version_num='e234eedc0f1b' WHERE alembic_version.version_num = 'd4808f157a34';

-- Running upgrade e234eedc0f1b -> d927d132458a

# CREATE TABLE account (
#     id INTEGER NOT NULL AUTO_INCREMENT,
#     name VARCHAR(50) NOT NULL,
#     description VARCHAR(200),
#     PRIMARY KEY (id)
# );

# UPDATE alembic_version SET version_num='d927d132458a' WHERE alembic_version.version_num = 'e234eedc0f1b';

-- Running upgrade d927d132458a -> 8b3baedae2d1

CREATE TABLE `App` (
    `AppId` INTEGER(11) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `Name` VARCHAR(128) CHARACTER SET utf8 NOT NULL, 
    `Dir` VARCHAR(32) CHARACTER SET utf8 NOT NULL, 
    `Desc` TEXT CHARACTER SET utf8, 
    PRIMARY KEY (`AppId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `Team` (
    `TeamId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `NameVi` VARCHAR(128) CHARACTER SET utf8mb4 NOT NULL, 
    `NameEn` VARCHAR(128) CHARACTER SET utf8mb4, 
    `CompanyId` INTEGER(10) UNSIGNED NOT NULL, 
    `DepartmentId` INTEGER(10) UNSIGNED NOT NULL, 
    `State` INTEGER(1) UNSIGNED NOT NULL COMMENT '0  - kh├┤ng ho?t ??ng
1 - ho?t ??ng' DEFAULT '1', 
    `AnnualLeaveTranning` DOUBLE, 
    `IsTimekeeping` SMALLINT(1) COMMENT '0: no checkin; 1 checkin; null get parent value (Company)' DEFAULT '1', 
    PRIMARY KEY (`TeamId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `RegulationsAndPolicies` (
    `Id` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `Title` VARCHAR(4096) COLLATE utf8mb4_unicode_ci, 
    `Path` VARCHAR(4096) COLLATE utf8mb4_unicode_ci, 
    `Priority` INTEGER(11) DEFAULT '99999', 
    `IsDeleted` INTEGER(11) DEFAULT '0', 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    `UpdatedDate` DATETIME, 
    `UpdatedBy` INTEGER(11), 
    PRIMARY KEY (`Id`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `OrgBranchAudit` (
    action VARCHAR(8) COLLATE utf8mb4_unicode_ci DEFAULT 'insert', 
    revision INTEGER(6) NOT NULL AUTO_INCREMENT, 
    `ActionDate` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    `OrgId` INTEGER(10) UNSIGNED NOT NULL, 
    `BranchId` INTEGER(10), 
    `IsVirtual` INTEGER(1) NOT NULL, 
    `CreatedDate` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    `CreatedStaffId` INTEGER(10) UNSIGNED NOT NULL DEFAULT '0', 
    `UpdatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `UpdatedStaffId` INTEGER(10) UNSIGNED DEFAULT '0', 
    PRIMARY KEY (revision)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `RegularGroup` (
    `RegularGroupId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `CompanyId` INTEGER(10) UNSIGNED NOT NULL, 
    `NameVi` VARCHAR(32) COLLATE utf8mb4_unicode_ci NOT NULL, 
    `NameEn` VARCHAR(32) COLLATE utf8mb4_unicode_ci NOT NULL, 
    `Ordering` INTEGER(10) UNSIGNED NOT NULL DEFAULT '0', 
    `RootId` INTEGER(10) UNSIGNED NOT NULL, 
    `ParentId` INTEGER(10) UNSIGNED NOT NULL, 
    `Lft` INTEGER(10) UNSIGNED NOT NULL, 
    `Rgt` INTEGER(10) UNSIGNED NOT NULL, 
    `Level` INTEGER(10) UNSIGNED NOT NULL, 
    PRIMARY KEY (`RegularGroupId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `StaffSignature` (
    `StaffSignatureId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `StaffId` INTEGER(11), 
    `Signature` LONGTEXT COLLATE utf8mb4_unicode_ci, 
    `State` INTEGER(11) DEFAULT '0', 
    `CreatedBy` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `UpdatedDate` DATETIME, 
    `UpdatedBy` INTEGER(11), 
    PRIMARY KEY (`StaffSignatureId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `WidgetViewing` (
    `WidgetId` INTEGER(11) UNSIGNED NOT NULL, 
    `ViewingId` INTEGER(11) UNSIGNED NOT NULL, 
    CONSTRAINT `fk_WidgetViewing_Viewing` FOREIGN KEY(`ViewingId`) REFERENCES `Viewing` (`ViewingId`), 
    CONSTRAINT `fk_WidgetViewing_Widget` FOREIGN KEY(`WidgetId`) REFERENCES `Widget` (`WidgetId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_WidgetViewing_WidgetId_idx` ON `WidgetViewing` (`WidgetId`);

CREATE INDEX `fk_WidgetViewing_ViewingId_idx` ON `WidgetViewing` (`ViewingId`);

CREATE TABLE `Bank` (
    `BankId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `NameVi` VARCHAR(64) CHARACTER SET utf8mb4, 
    `NameEn` VARCHAR(64) CHARACTER SET utf8mb4, 
    `State` INTEGER(10) UNSIGNED NOT NULL DEFAULT '1', 
    `Address` VARCHAR(128) CHARACTER SET utf8mb4, 
    `Priority` INTEGER(11) DEFAULT '99999', 
    `Type` INTEGER(11) COMMENT '1) Internal
2) ForCustomer
999) All', 
    PRIMARY KEY (`BankId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `ParamConfig` (
    `ID` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `ObjectCode` VARCHAR(50) NOT NULL, 
    `ObjectValue` VARCHAR(100) NOT NULL, 
    `DisplayName` VARCHAR(100), 
    `Priority` SMALLINT(6) NOT NULL DEFAULT '1', 
    `ExtendedData` TEXT CHARACTER SET utf8, 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`ID`, `ObjectCode`, `ObjectValue`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB;

CREATE TABLE `EmailReceiverGroupDetail` (
    `EmailReceiverGroupDetailId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `EmailReceiverGroupId` INTEGER(11), 
    `StaffId` INTEGER(11), 
    `CreatedBy` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`EmailReceiverGroupDetailId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `EmailStatusTracking` (
    `EmailStatusTrackingId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `EmailId` INTEGER(11), 
    `Status` INTEGER(11), 
    `UpdatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `UpdatedBy` INTEGER(11), 
    PRIMARY KEY (`EmailStatusTrackingId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `VnDistrictBK` (
    `VnDistrictId` INTEGER(10) UNSIGNED NOT NULL DEFAULT '0', 
    `VnProvinceId` INTEGER(10) UNSIGNED NOT NULL, 
    `DistrictCode` VARCHAR(8) CHARACTER SET utf8mb4, 
    `DistrictPostalCode` VARCHAR(8) CHARACTER SET utf8mb4, 
    `NameVi` VARCHAR(64) CHARACTER SET utf8mb4 NOT NULL, 
    `NameEn` VARCHAR(64) CHARACTER SET utf8mb4, 
    `LabelVi` VARCHAR(32) CHARACTER SET utf8mb4 NOT NULL COMMENT 'Qu?n
Th? x├ú
Huy?n
Th├ánh ph?', 
    `LabelEn` VARCHAR(32) CHARACTER SET utf8mb4 COMMENT 'Urban District
Town
Rural District
Provincial City', 
    `Ordering` INTEGER(10) UNSIGNED, 
    `IsDeleted` TINYINT(4)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `WorkProfilePosition` (
    `WorkProfilePositionId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `Name` VARCHAR(128) CHARACTER SET utf8mb4, 
    `Code` VARCHAR(128) CHARACTER SET utf8mb4, 
    `Ordering` INTEGER(11) NOT NULL DEFAULT '0', 
    `State` INTEGER(1) NOT NULL DEFAULT '1', 
    `GroupCode` VARCHAR(128) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'PK', 
    `IsAllowAccessOutside` TINYINT(4) DEFAULT '1', 
    `CreatedBy` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `UpdatedBy` INTEGER(11), 
    `UpdatedDate` DATETIME, 
    PRIMARY KEY (`WorkProfilePositionId`)
)COMMENT='vß╗ï tr├¡ c├┤ng viß╗çc trong c├┤ng ty' DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `VnWardBK` (
    `VnWardId` INTEGER(10) UNSIGNED NOT NULL, 
    `VnDistrictId` INTEGER(10) UNSIGNED NOT NULL, 
    `WardCode` VARCHAR(8) CHARACTER SET utf8mb4, 
    `WardPostalCode` VARCHAR(8) CHARACTER SET utf8mb4, 
    `NameVi` VARCHAR(64) CHARACTER SET utf8mb4 NOT NULL, 
    `NameEn` VARCHAR(64) CHARACTER SET utf8mb4, 
    `LabelVi` VARCHAR(32) CHARACTER SET utf8mb4 NOT NULL COMMENT 'Ph??ng
X├ú
Th? tr?n', 
    `LabelEn` VARCHAR(32) CHARACTER SET utf8mb4 COMMENT 'Commune
Ward
Township', 
    `Ordering` INTEGER(10) UNSIGNED
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `AbsenceRequestDetailByLeave` (
    `Id` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `AbsenceRequestId` INTEGER(11), 
    `UsedLastAnnualLeave` DECIMAL(5, 1) DEFAULT '0.0', 
    `UsedLastSeniorityLeave` DECIMAL(5, 1) DEFAULT '0.0', 
    `UsedLastRankLeave` DECIMAL(5, 1) DEFAULT '0.0', 
    `UsedLastTrainingLeave` DECIMAL(5, 1) DEFAULT '0.0', 
    `UsedAnnualLeave` DECIMAL(5, 1) DEFAULT '0.0', 
    `UsedSeniorityLeave` DECIMAL(5, 1) DEFAULT '0.0', 
    `UsedRankLeave` DECIMAL(5, 1) DEFAULT '0.0', 
    `UsedTrainingLeave` DECIMAL(5, 1) DEFAULT '0.0', 
    PRIMARY KEY (`Id`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `idx_AbsenceRequestId` ON `AbsenceRequestDetailByLeave` (`AbsenceRequestId`);

CREATE TABLE `Viewing` (
    `ViewingId` INTEGER(11) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `Name` VARCHAR(32) CHARACTER SET utf8 NOT NULL, 
    `Ordering` INTEGER(11) UNSIGNED NOT NULL, 
    `Description` TEXT CHARACTER SET utf8, 
    PRIMARY KEY (`ViewingId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `WorkPlaceChanging` (
    `WorkPlaceChangingId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `WorkContractId` INTEGER(11), 
    `BranchId` INTEGER(11), 
    `WorkLocationId` INTEGER(11), 
    `AvailableFrom` DATETIME, 
    `IsActived` SMALLINT(6) DEFAULT '1', 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    `CompanyId` INTEGER(11) NOT NULL DEFAULT '0', 
    `DepartmentId` INTEGER(11) NOT NULL DEFAULT '0', 
    `TeamId` INTEGER(11) NOT NULL DEFAULT '0', 
    `EndDate` DATETIME, 
    PRIMARY KEY (`WorkPlaceChangingId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `IX_WorkPlaceChanging_WorkContractId` ON `WorkPlaceChanging` (`WorkContractId`);

CREATE TABLE `StaffResignationRequest` (
    `StaffResignationRequestId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `StaffId` INTEGER(11), 
    `LastestWorkingDate` DATE, 
    `ApprovedBy` INTEGER(11), 
    `ApprovedDate` DATETIME, 
    `Status` INTEGER(11) COMMENT '1: New
2:Approved
3:Cancel', 
    `Reason` TEXT COLLATE utf8mb4_unicode_ci, 
    `ReasonNote` VARCHAR(1024) COLLATE utf8mb4_unicode_ci, 
    `CreatedBy` INTEGER(11), 
    `CreatedDate` DATETIME, 
    `UpdatedBy` INTEGER(11), 
    `UpdatedDate` DATETIME, 
    `Completed` INTEGER(11) DEFAULT '0', 
    PRIMARY KEY (`StaffResignationRequestId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `idx_StaffId` ON `StaffResignationRequest` (`StaffId`);

CREATE TABLE `TimekeepingRequest` (
    `TimeKeepingRequestId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `WorkProfileId` INTEGER(11) NOT NULL, 
    `Status` TINYINT(4) NOT NULL, 
    `StatusNote` VARCHAR(200) COLLATE utf8mb4_unicode_ci, 
    `ApprovedStaffId` INTEGER(11), 
    `ApprovedDate` DATETIME, 
    `ReasonId` INTEGER(11), 
    `OtherReason` VARCHAR(200) COLLATE utf8mb4_unicode_ci, 
    `CreatedDate` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11) NOT NULL, 
    `UpdatedDate` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    `UpdatedBy` INTEGER(11), 
    `ReasonNote` VARCHAR(200) COLLATE utf8mb4_unicode_ci, 
    PRIMARY KEY (`TimeKeepingRequestId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `IX_WorkProfileId` ON `TimekeepingRequest` (`WorkProfileId`);

CREATE INDEX `IX_CreatedDate` ON `TimekeepingRequest` (`CreatedDate`);

CREATE TABLE `Gender` (
    `GenderId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `GenderVi` VARCHAR(8) CHARACTER SET utf8mb4 NOT NULL, 
    `GenderEn` VARCHAR(8) CHARACTER SET utf8mb4 NOT NULL, 
    `Ordering` INTEGER(10) UNSIGNED NOT NULL, 
    PRIMARY KEY (`GenderId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `TicketSupportSpecificationDetail` (
    `TicketSupportSpecificationDetailId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `ParentCategoryCode` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    `ParentCategoryName` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `CategoryName` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `Priority` INTEGER(11), 
    `Status` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    `GroupName` VARCHAR(45) COLLATE utf8mb4_unicode_ci DEFAULT 'YCHC', 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`TicketSupportSpecificationDetailId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE alembic_version_history (
    id BIGINT(20) NOT NULL AUTO_INCREMENT, 
    alembic_version VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    prev_alembic_version VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    operation_type VARCHAR(32) COLLATE utf8mb4_unicode_ci NOT NULL, 
    operation_direction VARCHAR(32) COLLATE utf8mb4_unicode_ci NOT NULL, 
    user_version VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    changed_at DATETIME, 
    PRIMARY KEY (id)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `Reason` (
    `ReasonId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `ReasonGroupId` INTEGER(11), 
    `Name` VARCHAR(512), 
    `Code` VARCHAR(255), 
    `Priority` SMALLINT(6), 
    `State` INTEGER(11), 
    `CreatedBy` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `LastUpdatedBy` INTEGER(11), 
    `LastUpdatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`ReasonId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB;

CREATE TABLE `ByMonthDay` (
    `WorkScheduleId` INTEGER(10) UNSIGNED NOT NULL, 
    `MonthDayId` INTEGER(10) UNSIGNED NOT NULL, 
    `BranchId` INTEGER(10) UNSIGNED, 
    `StartTime` TIME NOT NULL, 
    `EndTime` TIME NOT NULL, 
    `TotalBreakTimeInMinute` INTEGER(11) NOT NULL, 
    CONSTRAINT `fk_ByMonthDay_MonthDay` FOREIGN KEY(`MonthDayId`) REFERENCES `MonthDay` (`MonthDayId`), 
    CONSTRAINT `fk_ByMonthDay_WorkSchedule` FOREIGN KEY(`WorkScheduleId`) REFERENCES `WorkSchedule` (`WorkScheduleId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_ByMonthDay_WorkSchedule_idx` ON `ByMonthDay` (`WorkScheduleId`);

CREATE INDEX `fk_ByMonthDay_WorkLocationId_idx` ON `ByMonthDay` (`BranchId`);

CREATE INDEX `fk_ByMonthDay_MonthDay_idx` ON `ByMonthDay` (`MonthDayId`);

CREATE TABLE `StaffLevelGroup` (
    `StaffLevelGroupId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `Name` VARCHAR(64) CHARACTER SET utf8mb4 NOT NULL, 
    `Ordering` INTEGER(11) NOT NULL DEFAULT '0', 
    `State` INTEGER(1) UNSIGNED NOT NULL DEFAULT '1', 
    `CompanyId` INTEGER(10) UNSIGNED NOT NULL, 
    `BaseSalary` DECIMAL(20, 2) UNSIGNED, 
    `NameVI` VARCHAR(256) COLLATE utf8mb4_unicode_ci, 
    `AnnualLeavePerYear` DOUBLE, 
    PRIMARY KEY (`StaffLevelGroupId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_StaffLevel_Company_idx` ON `StaffLevelGroup` (`CompanyId`);

CREATE TABLE `WorkProfilePositionMenuNavbar` (
    `Id` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `WorkProfilePositionId` INTEGER(11), 
    `MenuNavbarId` INTEGER(11), 
    `Alias` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    `IsDeleted` INTEGER(11) DEFAULT '0', 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`Id`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE UNIQUE INDEX `idx_WorkProfilePositionId_MenuNavbarId` ON `WorkProfilePositionMenuNavbar` (`WorkProfilePositionId`, `MenuNavbarId`);

CREATE TABLE `Task` (
    `TaskId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `Content` TEXT COLLATE utf8mb4_unicode_ci NOT NULL, 
    `DueTime` INTEGER(11) NOT NULL, 
    `StatusId` INTEGER(10) UNSIGNED NOT NULL, 
    `PriorityId` INTEGER(10) UNSIGNED NOT NULL, 
    `CreatedAt` INTEGER(11) NOT NULL, 
    `CreatedBy` INTEGER(10) UNSIGNED NOT NULL, 
    `UpdatedBy` INTEGER(10) UNSIGNED NOT NULL DEFAULT '0', 
    `UpdatedAt` INTEGER(11) NOT NULL DEFAULT '0', 
    PRIMARY KEY (`TaskId`), 
    CONSTRAINT `fk_Task_CreatedBy` FOREIGN KEY(`CreatedBy`) REFERENCES `User` (`UserId`), 
    CONSTRAINT `fk_Task_Priority` FOREIGN KEY(`PriorityId`) REFERENCES `TaskPriority` (`TaskPriorityId`), 
    CONSTRAINT `fk_Task_Status` FOREIGN KEY(`StatusId`) REFERENCES `TaskStatus` (`TaskStatusId`), 
    CONSTRAINT `fk_Task_EditedBy` FOREIGN KEY(`UpdatedBy`) REFERENCES `User` (`UserId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_Task_Status_idx` ON `Task` (`StatusId`);

CREATE INDEX `fk_Task_Priority_idx` ON `Task` (`PriorityId`);

CREATE INDEX `fk_Task_EditedBy_idx` ON `Task` (`UpdatedBy`);

CREATE INDEX `fk_Task_CreatedBy_idx` ON `Task` (`CreatedBy`);

CREATE TABLE `AllowanceStaffHistory` (
    `AllowanceStaffHistoryId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `Type` VARCHAR(128) COLLATE utf8mb4_unicode_ci, 
    `Amount` DECIMAL(18, 2) UNSIGNED NOT NULL DEFAULT '0.00', 
    `FromDate` DATE NOT NULL, 
    `ToDate` DATE, 
    `Note` VARCHAR(1000) COLLATE utf8mb4_unicode_ci, 
    `WorkContractHistoryId` INTEGER(11) NOT NULL, 
    `CreatedDate` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`AllowanceStaffHistoryId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `ScoreCampaignBranch` (
    `ScoreCampaignBranchId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `BranchId` INTEGER(11), 
    `NumberTreatmentRoom` INTEGER(11), 
    `NumberXRAYRoom` INTEGER(11), 
    `ScoreCampaignBranchcol1` INTEGER(11), 
    PRIMARY KEY (`ScoreCampaignBranchId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `WorkPosition` (
    `WorkPositionId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `NameVi` VARCHAR(128) CHARACTER SET utf8mb4 NOT NULL, 
    `NameEn` VARCHAR(128) CHARACTER SET utf8mb4, 
    `CompanyId` INTEGER(10) UNSIGNED NOT NULL, 
    `Ordering` INTEGER(11) NOT NULL DEFAULT '0', 
    `State` INTEGER(1) NOT NULL DEFAULT '1', 
    PRIMARY KEY (`WorkPositionId`)
)COMMENT='vß╗ï tr├¡ c├┤ng viß╗çc trong c├┤ng ty' DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_WorkPosition_Company_idx` ON `WorkPosition` (`CompanyId`);

CREATE TABLE `IncomeTypeLevel` (
    `IncomeTypeLevelId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `IncomeTypeId` INTEGER(11), 
    `Name` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `IsDeleted` INTEGER(11), 
    `IncomePerHour` DECIMAL(10, 2), 
    `IsIncomeByService` INTEGER(11), 
    `IsIncomeByServiceQuality` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    PRIMARY KEY (`IncomeTypeLevelId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `TicketSupportTracking` (
    `TicketSupportTrackingId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `TicketSupportId` INTEGER(11), 
    `ReceivingOrgId` INTEGER(11), 
    `TicketCategoryId` INTEGER(11), 
    `Content` TEXT COLLATE utf8mb4_unicode_ci, 
    `Status` TINYINT(4), 
    `CreatedBy` INTEGER(11), 
    `CreatedDate` DATETIME, 
    `ResultBy` INTEGER(11), 
    `ResultDate` DATETIME, 
    `ResultContent` TEXT COLLATE utf8mb4_unicode_ci, 
    `RatingContent` TEXT COLLATE utf8mb4_unicode_ci, 
    `RatingDate` DATETIME, 
    `CancelDate` DATETIME, 
    `ReceiveBy` INTEGER(11), 
    `ReceiveDate` DATETIME, 
    `ReceiveContent` TEXT COLLATE utf8mb4_unicode_ci, 
    `RejectedBy` INTEGER(10) UNSIGNED, 
    `RejectedDate` DATETIME, 
    `RejectedContent` TEXT COLLATE utf8mb4_unicode_ci, 
    `SendingOrgId` INTEGER(11), 
    `JsonContent` VARCHAR(4000) COLLATE utf8mb4_unicode_ci, 
    `IsPublic` INTEGER(11), 
    `PushedDate` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`TicketSupportTrackingId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `WeekDay` (
    `WeekDayId` INTEGER(10) UNSIGNED NOT NULL, 
    `Name` VARCHAR(16) CHARACTER SET utf8mb4 NOT NULL, 
    `Ordering` INTEGER(1) NOT NULL, 
    `IsWeekEnd` INTEGER(1) NOT NULL DEFAULT '0', 
    `StartTime` TIME NOT NULL, 
    `EndTime` TIME NOT NULL, 
    `TotalBreakTimeInMinute` INTEGER(10) UNSIGNED NOT NULL, 
    PRIMARY KEY (`WeekDayId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `TicketSupportReceivingOrg` (
    `TicketSupportReceivingOrg` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `Name` VARCHAR(1024) COLLATE utf8mb4_unicode_ci, 
    `Priority` INTEGER(11), 
    `IsDeleted` INTEGER(11) DEFAULT '0', 
    `CreatedDate` DATETIME, 
    `OrgId` INTEGER(11), 
    PRIMARY KEY (`TicketSupportReceivingOrg`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `IDX_OrId` ON `TicketSupportReceivingOrg` (`OrgId`);

CREATE TABLE `IncomeBonusClosedOfMonth` (
    `IncomeBonusClosedOfMonthId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `ClosedTime` DATE, 
    `StaffId` INTEGER(11), 
    `BonnusType` VARCHAR(255) COLLATE utf8mb4_unicode_ci COMMENT '1
 Th??ng Gi├ím S├ít Chung ,2
 th??ng Ch?t l??ng D?ch v?, 3
 Th??ng Kinh doanh', 
    `Value` DECIMAL(10, 2), 
    `ValueType` INTEGER(11) COMMENT '1
 Amount, 2
 Percent', 
    `RatingAVG` DECIMAL(10, 2), 
    `BranchId` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    PRIMARY KEY (`IncomeBonusClosedOfMonthId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `StaffAttendanceRecord` (
    `StaffAttendanceRecordId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `StaffId` INTEGER(10) UNSIGNED NOT NULL, 
    `StaffName` VARCHAR(64) NOT NULL, 
    `WorkProfilePositionId` INTEGER(11), 
    `StandardWorkingDay` FLOAT NOT NULL, 
    `NumberOfAttendanceDays` FLOAT, 
    `NumberOfAnnualLeave` FLOAT, 
    `NumberOfPaidWorkingDay` FLOAT, 
    `PayrollPeriod` VARCHAR(6), 
    `CreatedBy` INTEGER(11), 
    `CreatedDate` DATETIME, 
    `ApprovedBy` INTEGER(11), 
    `ApprovedDate` DATETIME, 
    `Note` VARCHAR(64), 
    PRIMARY KEY (`StaffAttendanceRecordId`, `StaffId`), 
    CONSTRAINT `fk_StaffAttendanceRecord_staffId` FOREIGN KEY(`StaffId`) REFERENCES `Staff` (`StaffId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB;

CREATE INDEX `fk_StaffAttendanceRecord_staffId_idx` ON `StaffAttendanceRecord` (`StaffId`);

CREATE TABLE `StaffWorkPlace` (
    `StaffId` INTEGER(11) NOT NULL, 
    `WorkContractId` INTEGER(11), 
    `CompanyId` INTEGER(11), 
    `DepartmentId` INTEGER(11), 
    `TeamId` INTEGER(11), 
    `EffectiveDate` DATE, 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `UpdatedDate` DATETIME
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `id_WorkContractId` ON `StaffWorkPlace` (`WorkContractId`);

CREATE INDEX `id_StaffId` ON `StaffWorkPlace` (`StaffId`);

CREATE TABLE `IncomeBonusDaily` (
    `IncomeBonusDailyId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `ClosedTime` DATE, 
    `StaffId` INTEGER(11), 
    `IncomeTypeId` INTEGER(11), 
    `IncomeTypeLevelId` INTEGER(11), 
    `BonnusType` VARCHAR(255) COLLATE utf8mb4_unicode_ci COMMENT '1
 Th??ng Gi├ím S├ít Chung ,2
 th??ng Ch?t l??ng D?ch v?, 3
 Th??ng Kinh doanh', 
    `IncomeJob` DECIMAL(18, 6), 
    `Value` DECIMAL(10, 2), 
    `ValueType` INTEGER(11) COMMENT '1
 Amount, 2
 Percent', 
    `RatingAVG` DECIMAL(10, 2), 
    `BranchId` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    `IsCurrent` INTEGER(11) DEFAULT '1', 
    PRIMARY KEY (`IncomeBonusDailyId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `PermissionGeneral` (
    `PermissionGeneralId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `GroupCode` VARCHAR(128) DEFAULT 'PK', 
    `PermissionCode` VARCHAR(128), 
    `ActionValue` VARCHAR(128), 
    `IsActive` INTEGER(11) DEFAULT '1', 
    `UpdatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `UpdatedBy` INTEGER(11), 
    PRIMARY KEY (`PermissionGeneralId`)
)DEFAULT CHARSET=latin1 ENGINE=InnoDB;

CREATE TABLE `ReasonGroup` (
    `ReasonGroupId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `Name` VARCHAR(255), 
    `Code` VARCHAR(45), 
    `Priority` INTEGER(11), 
    `State` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    `LastUpdatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `LastUpdatedBy` INTEGER(11), 
    PRIMARY KEY (`ReasonGroupId`)
)DEFAULT CHARSET=latin1 ENGINE=InnoDB;

CREATE TABLE `AllowanceStaff` (
    `Id` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `WorkProfileId` INTEGER(10) UNSIGNED NOT NULL, 
    `AllowanceId` INTEGER(10) UNSIGNED NOT NULL, 
    `StaffId` INTEGER(10) UNSIGNED NOT NULL, 
    `IssueFromDate` DATE, 
    `IssueToDate` DATE, 
    `Amount` DECIMAL(12, 2) NOT NULL, 
    `TaxInclude` INTEGER(1) NOT NULL COMMENT 'c├│ t├¡nh thu? kh├┤ng' DEFAULT '1', 
    `Note` TEXT COLLATE utf8mb4_unicode_ci COMMENT 'ghi ch├║', 
    PRIMARY KEY (`Id`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_AllowanceStaff_WorkProfile_idx` ON `AllowanceStaff` (`WorkProfileId`, `StaffId`);

CREATE INDEX `fk_AllowanceStaff_Allowance_idx` ON `AllowanceStaff` (`AllowanceId`);

CREATE INDEX `IX_AllowanceStaff_StaffId` ON `AllowanceStaff` (`StaffId`);

CREATE TABLE `StaffLanguage` (
    `LanguageId` INTEGER(10) UNSIGNED NOT NULL, 
    `StaffId` INTEGER(10) UNSIGNED NOT NULL, 
    `LanguageLevelId` INTEGER(10) UNSIGNED NOT NULL, 
    `UpdatedAt` INTEGER(10) UNSIGNED NOT NULL
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_StaffLanguage_Staff_idx` ON `StaffLanguage` (`StaffId`);

CREATE INDEX `fk_StaffLanguage_Language_idx` ON `StaffLanguage` (`LanguageId`);

CREATE INDEX `fk_StaffLanguage_LanguageLevel_idx` ON `StaffLanguage` (`LanguageLevelId`);

CREATE TABLE `ComplaintReasonGroup` (
    `ComplaintReasonGroupId` INTEGER(10) UNSIGNED NOT NULL, 
    `Name` VARCHAR(32) COLLATE utf8mb4_unicode_ci NOT NULL, 
    `State` INTEGER(1) UNSIGNED NOT NULL DEFAULT '1'
)COMMENT='Gom nh├│m c├íc complaint. C├íc nh├│m kh├┤ng chß╗ông lß║Ñn.' DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `IncomeServiceConfig` (
    `IncomeServiceConfigId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `ServiceId` INTEGER(11), 
    `IncomeTypeId` INTEGER(11), 
    `IncomeTypeLevelId` INTEGER(11), 
    `EffectFromDate` DATE, 
    `EffectToDate` DATE, 
    `Value` DECIMAL(18, 2), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    PRIMARY KEY (`IncomeServiceConfigId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `NetworkConfig` (
    `NetworkConfigId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `WanIp` VARCHAR(40) CHARACTER SET utf8mb4 NOT NULL, 
    `Description` TEXT CHARACTER SET utf8mb4, 
    `State` INTEGER(1) DEFAULT '1', 
    `WorkLocationId` INTEGER(10) UNSIGNED NOT NULL, 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`NetworkConfigId`), 
    CONSTRAINT `fk_NetworkConfig_WorkLocation` FOREIGN KEY(`WorkLocationId`) REFERENCES `WorkLocation` (`WorkLocationId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_NetworkConfig_WorkLocation_idx` ON `NetworkConfig` (`WorkLocationId`);

CREATE TABLE `StaffSalaryDetails_backup` (
    `StaffSalaryDetailsId` INTEGER(11) NOT NULL DEFAULT '0', 
    `StaffId` INTEGER(11), 
    `StaffCode` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `FullName` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'hß╗ì t├¬n', 
    `Company` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'C├┤ng ty', 
    `WorkProfilePosition` VARCHAR(100) COLLATE utf8mb4_unicode_ci COMMENT 'Chß╗⌐c danh', 
    `ContractType` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'Loß║íi hß╗úp ─æß╗ông', 
    `Branch` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'Chi nh├ính', 
    `StartDate` DATETIME, 
    `Shift` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'ca l├ám viß╗çc', 
    `Total` DECIMAL(13, 3) COMMENT 'Tß╗òng cß╗Öng' DEFAULT '0.000', 
    `NoTimekeeping` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'ko chß║Ñm c├┤ng', 
    `Level` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'bß║¡c', 
    `SalaryPerHour` DECIMAL(7, 2) COMMENT '─æ╞ín gi├í giß╗¥' DEFAULT '0.00', 
    `ActualHoursWorked` DECIMAL(5, 2) COMMENT 'sß╗æ giß╗¥ lv thß╗▒c tß║┐ HIS' DEFAULT '0.00', 
    `AnnualLeave` DECIMAL(5, 2) COMMENT 'nghß╗ë ph├⌐p' DEFAULT '0.00', 
    `CompensatoryLeave` DECIMAL(7, 2) COMMENT 'nghß╗ë b├╣' DEFAULT '0.00', 
    `PaidLeave` DECIMAL(5, 2) COMMENT 'nghß╗ë chß║┐ ─æß╗Ö' DEFAULT '0.00', 
    `PublicHolidaysLeave` DECIMAL(5, 2) COMMENT 'nghß╗ë lß╗à/tß║┐t' DEFAULT '0.00', 
    `TotalHour` DECIMAL(5, 2) COMMENT 'Tß╗òng c├┤ng' DEFAULT '0.00', 
    `TotalStandardHours` DECIMAL(5, 2) COMMENT 'tß╗òng c├┤ng t├¡nh l╞░╞íng' DEFAULT '0.00', 
    `StandardWage` DECIMAL(5, 2) COMMENT 'c├┤ng chuß║⌐n' DEFAULT '0.00', 
    `BasicSalary` DECIMAL(13, 3) COMMENT 'l╞░╞íng c╞í bß║ún' DEFAULT '0.000', 
    `PerformanceBonus` DECIMAL(13, 3) COMMENT 'Th╞░ß╗ƒng ├¥ thß╗⌐c v├á Tu├ón thß╗º/Th╞░ß╗ƒng Hiß╗çß╗Ñ quß║ú hoß║ít ─æß╗Öng' DEFAULT '0.000', 
    `LunchAllowance` DECIMAL(13, 3) COMMENT 'Phß╗Ñ cß║Ñp c╞ím tr╞░a' DEFAULT '0.000', 
    `UniformAllowance` DECIMAL(13, 3) COMMENT 'Phß╗Ñ cß║Ñp ─æß╗ông phß╗Ñc' DEFAULT '0.000', 
    `TotalLunchAllowance` DECIMAL(10, 2) COMMENT 'Th├ánh tiß╗ün PC c╞ím theo c├┤ng' DEFAULT '0.00', 
    `FixedIncomeWithLunchAllowance` DECIMAL(15, 3) COMMENT '─æß╗ïnh mß╗⌐c thu nhß║¡p cß╗æ ─æß╗ïnh (─æ├ú  bao gß╗ôm Pc c╞ím)' DEFAULT '0.000', 
    `FixedIncomeAmountWithLunchAllowance` DECIMAL(15, 3) COMMENT 'Th├ánh tiß╗ün thu nhß║¡p cß╗æ ─æß╗ïnh theo c├┤ng chuß║⌐n (─æ├ú bao gß╗ôm PC c╞ím)' DEFAULT '0.000', 
    `TotalIncomeWorkingDays` DECIMAL(13, 3) COMMENT 'Tß╗òng thu nhß║¡p theo ng├áy c├┤ng' DEFAULT '0.000', 
    `CRM/CSBonus` DECIMAL(13, 3) COMMENT 'Th╞░ß╗ƒng CRM/CS (C.Mai)' DEFAULT '0.000', 
    `DoctorBonus` DECIMAL(15, 3) COMMENT 'Th╞░ß╗ƒng b├íc s─⌐' DEFAULT '0.000', 
    `TaskBonus` DECIMAL(15, 3) COMMENT 'Th╞░ß╗ƒng c├┤ng viß╗çc' DEFAULT '0.000', 
    `ServiceQualityBonus` DECIMAL(13, 3) COMMENT 'Th╞░ß╗ƒng CLDV' DEFAULT '0.000', 
    `GeneralManagermentBonus` DECIMAL(13, 3) COMMENT 'Th╞░ß╗ƒng quß║ún l├╜ chung' DEFAULT '0.000', 
    `EfficiencyManagementBonus` DECIMAL(13, 3) COMMENT 'Th╞░ß╗ƒng hiß╗çu quß║ú quß║ún l├╜' DEFAULT '0.000', 
    `ClinicsAchievingKPIRevenueBonus` DECIMAL(15, 3) COMMENT 'Th╞░ß╗ƒng ph├▓ng kh├ím ─æß║ít KPI thu tiß╗ün' DEFAULT '0.000', 
    `EbitdaBonus` DECIMAL(13, 3) COMMENT 'Th╞░ß╗ƒng Ebitda' DEFAULT '0.000', 
    `VinmecBonus` DECIMAL(13, 3) COMMENT 'th╞░ß╗ƒng vinmec' DEFAULT '0.000', 
    `SecurityBonus` DECIMAL(13, 3) COMMENT 'th╞░ß╗ƒng an ninh' DEFAULT '0.000', 
    `HolidayBonus` DECIMAL(13, 3) COMMENT 'th╞░ß╗ƒng lß╗à/tß║┐t' DEFAULT '0.000', 
    `TotalBonus` DECIMAL(12, 2) COMMENT 'tß╗òng th╞░ß╗ƒng' DEFAULT '0.00', 
    `AssistantManagerAndConcurrentBonus` DECIMAL(15, 3) COMMENT 'PC Phß╗Ñ t├í tr╞░ß╗ƒng v├á ki├¬m nhiß╗çm' DEFAULT '0.000', 
    `GuaranteedIncomeAllowance` DECIMAL(15, 3) COMMENT 'Phß╗Ñ cß║Ñp ─æß║úm bß║úo thu nhß║¡p' DEFAULT '0.000', 
    `ParkingTravelAllowance` DECIMAL(13, 3) COMMENT 'PC gß╗¡i xe/c├┤ng t├íc' DEFAULT '0.000', 
    `ProfessionalCertificateAllowance` DECIMAL(13, 3) COMMENT 'Phß╗Ñ cß║Ñp chß╗⌐ng chß╗ë h├ánh nghß╗ü' DEFAULT '0.000', 
    `OtherAllowances` DECIMAL(13, 3) COMMENT 'phß╗Ñ cß║Ñp kh├íc' DEFAULT '0.000', 
    `DentalTour` DECIMAL(15, 3) DEFAULT '0.000', 
    `WarehouseAllowance` DECIMAL(15, 3) COMMENT 'Phß╗Ñ cß║Ñp kho' DEFAULT '0.000', 
    `TotalAllowances` DECIMAL(13, 3) COMMENT 'Tß╗òng phß╗Ñ cß║Ñp', 
    `OtherTotalIncome` DECIMAL(15, 3) COMMENT 'Tß╗òng thu nhß║¡p kh├íc' DEFAULT '0.000', 
    `OtherAddition` DECIMAL(13, 3) COMMENT 'cß╗Öng kh├íc' DEFAULT '0.000', 
    `OtherDeductions` DECIMAL(13, 3) COMMENT 'trß╗½ kh├íc' DEFAULT '0.000', 
    `TotalIncomeBeforeTax` DECIMAL(13, 3) COMMENT 'tß╗òng thu nhß║¡p tr╞░ß╗¢c thuß║┐' DEFAULT '0.000', 
    `ParticipatingSalaryInSocialInsurance` DECIMAL(13, 3) COMMENT 'Mß╗⌐c l╞░╞íng tham gia BHXH' DEFAULT '0.000', 
    `PersonalHealthInsurance` DECIMAL(13, 3) COMMENT 'BHYT 1,5%' DEFAULT '0.000', 
    `PersonalSocialInsurance` DECIMAL(13, 3) COMMENT 'BHXH 8%' DEFAULT '0.000', 
    `PersonalUnemploymentInsurance` DECIMAL(13, 3) COMMENT 'BHTN 1%' DEFAULT '0.000', 
    `EmployeeSocialInsurance` DECIMAL(13, 3) COMMENT 'NLD ─æ├│ng BHXH 10,5%' DEFAULT '0.000', 
    `EmployeeUnionFee` DECIMAL(13, 3) COMMENT 'NL─É ─æ├│ng ph├¡ c├┤ng ─æo├án 1%' DEFAULT '0.000', 
    `CompanySocialInsurance` DECIMAL(13, 3) COMMENT 'BHXH 17%' DEFAULT '0.000', 
    `CompanyOccupaitionalAccidentOrDisease` DECIMAL(13, 3) COMMENT 'TNL─É / BNN 0.5%' DEFAULT '0.000', 
    `CompanyHealthInsurance` DECIMAL(13, 3) COMMENT 'BHYT 3%' DEFAULT '0.000', 
    `CompanyUnemploymentInsurance` DECIMAL(13, 3) COMMENT 'BHTN 1%' DEFAULT '0.000', 
    `EnterpriseSocialInsurance` DECIMAL(13, 3) COMMENT 'doanh nghiß╗çp ─æ├│ng BHXH 21.5%' DEFAULT '0.000', 
    `EnterpriseUnionFee` DECIMAL(13, 3) COMMENT 'Doanh nghiß╗çp ─æ├│ng c├┤ng ─æo├án 2%' DEFAULT '0.000', 
    `LunchOrUniformAllowanceNoTax` DECIMAL(13, 3) COMMENT 'Kh├┤ng t├¡nh thuß║┐ ( phß╗Ñ cß║Ñp c╞ím tr╞░a/ ─Éß╗ông phß╗Ñc)' DEFAULT '0.000', 
    `TotalTaxableIncome` DECIMAL(13, 3) COMMENT 'Tß╗òng thu nhß║¡p chß╗ïu thuß║┐' DEFAULT '0.000', 
    `TaxableIncomeObject` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT '─Éß╗æi t╞░ß╗úng t├¡nh thuß║┐ TNCN', 
    `Commitment` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'Cam kß║┐t', 
    `Dependents` INTEGER(11) COMMENT 'Sß╗æ ng╞░ß╗¥i phß╗Ñ thuß╗Öc' DEFAULT '0', 
    `TotalAssessableIncome` DECIMAL(13, 3) COMMENT 'Tß╗òng thu nhß║¡p t├¡nh thuß║┐' DEFAULT '0.000', 
    `PersonalIncomeTaxCollection` DECIMAL(13, 3) COMMENT 'Thu tiß╗ün thuß║┐ TNCN' DEFAULT '0.000', 
    `ActualPayment` DECIMAL(12, 2) COMMENT 'Thß╗▒c l├únh' DEFAULT '0.00', 
    `CompanyPaysSocialInsurance` DECIMAL(13, 3) COMMENT 'Cty ─æ├│ng hß╗ì BHXH' DEFAULT '0.000', 
    `WithholdSocialInsurance` DECIMAL(13, 3) COMMENT 'thu hß╗Ö tiß╗ün BHXH 21.5%' DEFAULT '0.000', 
    `PaidHolidayBonus` DECIMAL(11, 2) COMMENT '─É├ú thanh to├ín th╞░ß╗ƒng Lß╗à/tß║┐t\\n' DEFAULT '0.00', 
    `PaidOthers` DECIMAL(11, 2) COMMENT '─É├ú thanh to├ín kh├íc\\n' DEFAULT '0.00', 
    `BankTransfer` DECIMAL(12, 2) COMMENT 'chuyß╗ân khoß║ún' DEFAULT '0.00', 
    `NoteOtherAdditions` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'Ghi ch├║ cß╗Öt cß╗Öng kh├íc\\n', 
    `Name` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'T├¬n t├ái khoß║ún', 
    `AccountNumber` VARCHAR(255) COLLATE utf8mb4_unicode_ci COMMENT 'sß╗æ t├ái khoß║ún', 
    `Bank` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'ng├ón h├áng', 
    `Email` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'email', 
    `TransferAmount` DECIMAL(13, 2) COMMENT 'sß╗æ tiß╗ün chuyß╗ân khoß║ún', 
    `Additional` DECIMAL(13, 3) COMMENT 'bß╗ò sung' DEFAULT '0.000', 
    `Notes` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'ghi ch├║/ l├╜ do', 
    `PaymentDate` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'ng├áy thanh to├ín', 
    `PayPeriod` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'kß╗│ l╞░╞íng', 
    `Template` INTEGER(11) COMMENT '1-BO\\n2-Phu ta\\n3-Bac Si\\n4-Bao ve'
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `NotificationStatus` (
    `NotificationStatusId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `NotificationId` INTEGER(11), 
    `Status` INTEGER(11) COMMENT '1 New
2 Waiiting
3 Approved
4 Waiiting
5 Rejected
6 Recall', 
    `StatusNote` VARCHAR(256) COLLATE utf8mb4_unicode_ci, 
    `UpdatedDate` DATETIME, 
    `UpdatedBy` INTEGER(11), 
    PRIMARY KEY (`NotificationStatusId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `rptStaffSalary` (
    `MonthDate` DATE NOT NULL, 
    `StaffId` INTEGER(11) NOT NULL, 
    `GroupId` TINYINT(1) UNSIGNED COMMENT '1: BO, 2: PK', 
    `IsFullTime` TINYINT(1) NOT NULL, 
    `StatusId` TINYINT(1), 
    `SeniorityInMonth` INTEGER(11), 
    `SocialInsuranceSalary` DECIMAL(18, 2), 
    `PositionAllowance` DECIMAL(18, 2), 
    `AwarenessAllowance` DECIMAL(18, 2), 
    `LunchAllowance` DECIMAL(18, 2), 
    `UniformAllowance` DECIMAL(18, 2), 
    `ConcurrentlyAllowance` DECIMAL(18, 2), 
    `OthersAllowance` DECIMAL(18, 2), 
    `StandardWorkingHours` DECIMAL(8, 2), 
    `StandardWorkingDays` DECIMAL(8, 2), 
    `Holiday_ActualWorkingHours` DECIMAL(8, 2), 
    `Holiday_ActualWorkingDays` DECIMAL(8, 2), 
    `Weekend_ActualWorkingHours` DECIMAL(8, 2), 
    `Weekend_ActualWorkingDays` DECIMAL(8, 2), 
    `ActualWorkingHours` DECIMAL(8, 2), 
    `ActualWorkingDays` DECIMAL(8, 2), 
    `ActualLeaveHours` DECIMAL(8, 2), 
    `ActualLeaveDays` DECIMAL(8, 2), 
    `WorkingPercent` DECIMAL(20, 8), 
    `ActualSalary` DECIMAL(18, 2), 
    `ActualPositionAllowance` DECIMAL(18, 2), 
    `ActualAwarenessAllowance` DECIMAL(18, 2), 
    `ActualLunchAllowance` DECIMAL(18, 2), 
    `ActualUniformAllowance` DECIMAL(18, 2), 
    `ActualConcurrentlyAllowance` DECIMAL(18, 2), 
    `ActualOthersAllowance` DECIMAL(18, 2), 
    `WorkBonusAmount` DECIMAL(18, 2), 
    `HolidayBonusAmount` DECIMAL(18, 2), 
    `OthersBonusAmount` DECIMAL(18, 2), 
    `AddAmount` DECIMAL(18, 2), 
    `SubAmount` DECIMAL(18, 2), 
    `SocialInsuranceCompany` DECIMAL(18, 2), 
    `HealthInsuranceCompany` DECIMAL(18, 2), 
    `UnemploymentInsuranceCompany` DECIMAL(18, 2), 
    `UnionDueCompany` DECIMAL(18, 2), 
    `OccupationalDiseaseInsuranceCompany` DECIMAL(18, 2), 
    `SocialInsuranceEmployee` DECIMAL(18, 2), 
    `HealthInsuranceEmployee` DECIMAL(18, 2), 
    `UnemploymentInsuranceEmployee` DECIMAL(18, 2), 
    `UnionDueEmployee` DECIMAL(18, 2), 
    `PersonalDeductedAmount` DECIMAL(18, 2), 
    `DependantNumber` INTEGER(11), 
    `DependantDeductedAmount` DECIMAL(18, 2), 
    `TotalTaxableInCome` DECIMAL(18, 2), 
    `PersonalIncomeTax` DECIMAL(18, 2), 
    `NetSalary` DECIMAL(18, 2), 
    `CreatedBy` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `UpdatedBy` INTEGER(11), 
    `UpdatedDate` DATETIME
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `IX_StaffId` ON `rptStaffSalary` (`StaffId`, `MonthDate`);

CREATE INDEX `IX_MonthDate` ON `rptStaffSalary` (`MonthDate`, `IsFullTime`);

CREATE TABLE `WorkContractDocuments` (
    `WorkContractDocumentId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `WorkContractId` INTEGER(11), 
    `WorkContractAnnexId` INTEGER(11), 
    `FileName` VARCHAR(1024) COLLATE utf8mb4_unicode_ci, 
    `CDNURL` VARCHAR(2048) COLLATE utf8mb4_unicode_ci, 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    `DeletedDate` DATETIME, 
    `DeletedBy` INTEGER(11), 
    PRIMARY KEY (`WorkContractDocumentId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `IncomeType` (
    `IncomeTypeId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `Name` VARCHAR(255) COLLATE utf8mb4_unicode_ci COMMENT '1
 Ph? t├í, 2
 T? v?n vi├¬n, 3
 T? v?n vi├¬n, 4
 Gi├ím s├ít v?n h├ánh, 5
 OAM, 6
 CC Agent', 
    `IsDeleted` INTEGER(11), 
    `WorkHourPerMonth` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    PRIMARY KEY (`IncomeTypeId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `StaffLeave` (
    `StaffId` INTEGER(11) NOT NULL, 
    `YearNumber` SMALLINT(6) NOT NULL, 
    `TotalLeave` DECIMAL(5, 1) COMMENT 'Tß╗òng sß╗æ ng├áy ph├⌐p' DEFAULT '0.0', 
    `AvailableTotalLeave` DECIMAL(5, 1) COMMENT 'Tß╗òng sß╗æ ng├áy ph├⌐p khß║ú dß╗Ñng' DEFAULT '0.0', 
    `PendingTotalLeave` DECIMAL(5, 1) COMMENT 'Tß╗òng sß╗æ ng├áy ph├⌐p ─æang chß╗¥ duyß╗çt' DEFAULT '0.0', 
    `AnnualLeave` DECIMAL(5, 1) COMMENT 'Tß╗òng sß╗æ ng├áy ph├⌐p n─âm' DEFAULT '0.0', 
    `AvailableAnnualLeave` DECIMAL(5, 1) COMMENT 'Tß╗òng sß╗æ ng├áy ph├⌐p n─âm khß║ú dß╗Ñng' DEFAULT '0.0', 
    `PendingAnnualLeave` DECIMAL(5, 1) COMMENT 'Tß╗òng sß╗æ ng├áy ph├⌐p n─âm ─æang chß╗¥ duyß╗çt' DEFAULT '0.0', 
    `LastAnnualLeave` DECIMAL(5, 1) COMMENT 'Tß╗òng sß╗æ ng├áy ph├⌐p n─âm (tß╗ôn n─âm c┼⌐)' DEFAULT '0.0', 
    `AvailableLastAnnualLeave` DECIMAL(5, 1) COMMENT 'Tß╗òng sß╗æ ng├áy ph├⌐p n─âm (tß╗ôn n─âm c┼⌐) khß║ú dß╗Ñng' DEFAULT '0.0', 
    `PendingLastAnnualLeave` DECIMAL(5, 1) COMMENT 'Tß╗òng sß╗æ ng├áy ph├⌐p n─âm (tß╗ôn n─âm c┼⌐) ─æang chß╗¥ duyß╗çt' DEFAULT '0.0', 
    `SeniorityLeave` DECIMAL(5, 1) COMMENT 'Tß╗òng sß╗æ ng├áy ph├⌐p th├óm ni├¬n' DEFAULT '0.0', 
    `AvailableSeniorityLeave` DECIMAL(5, 1) COMMENT 'Tß╗òng sß╗æ ng├áy ph├⌐p th├óm ni├¬n khß║ú dß╗Ñng' DEFAULT '0.0', 
    `PendingSeniorityLeave` DECIMAL(5, 1) COMMENT 'Tß╗òng sß╗æ ng├áy ph├⌐p th├óm ni├¬n ─æang chß╗¥ duyß╗çt' DEFAULT '0.0', 
    `RankLeave` DECIMAL(5, 1) COMMENT 'Tß╗òng sß╗æ ng├áy ph├⌐p cß║Ñp bß║¡c' DEFAULT '0.0', 
    `AvailableRankLeave` DECIMAL(5, 1) COMMENT 'Tß╗òng sß╗æ ng├áy ph├⌐p cß║Ñp bß║¡c khß║ú dß╗Ñng' DEFAULT '0.0', 
    `PendingRankLeave` DECIMAL(5, 1) COMMENT 'Tß╗òng sß╗æ ng├áy ph├⌐p cß║Ñp bß║¡c ─æang chß╗¥ duyß╗çt' DEFAULT '0.0', 
    `TrainingLeave` DECIMAL(5, 1) COMMENT 'Tß╗òng sß╗æ ng├áy ph├⌐p ─æ├áo tß║ío' DEFAULT '0.0', 
    `AvailableTrainingLeave` DECIMAL(5, 1) COMMENT 'Tß╗òng sß╗æ ng├áy ph├⌐p ─æ├áo tß║ío khß║ú dß╗Ñng' DEFAULT '0.0', 
    `PendingTrainingLeave` DECIMAL(5, 1) COMMENT 'Tß╗òng sß╗æ ng├áy ph├⌐p ─æ├áo tß║ío ─æang chß╗¥ duyß╗çt' DEFAULT '0.0', 
    `UsedUnpaidLeave` DECIMAL(5, 1) COMMENT 'Tß╗òng sß╗æ ng├áy ph├⌐p kh├┤ng h╞░ß╗ƒng l╞░╞íng ─æ├ú d├╣ng' DEFAULT '0.0', 
    `PendingUnpaidLeave` DECIMAL(5, 1) COMMENT 'Tß╗òng sß╗æ ng├áy ph├⌐p kh├┤ng h╞░ß╗ƒng l╞░╞íng ─æang chß╗¥ duyß╗çt' DEFAULT '0.0', 
    `UsedSickLeave` DECIMAL(5, 1) COMMENT 'Tß╗òng sß╗æ ng├áy ph├⌐p ß╗æm/bß╗çnh ─æ├ú d├╣ng' DEFAULT '0.0', 
    `PendingSickLeave` DECIMAL(5, 1) COMMENT 'Tß╗òng sß╗æ ng├áy ph├⌐p ß╗æm/bß╗çnh ─æang chß╗¥ duyß╗çt' DEFAULT '0.0', 
    `UsedMarriageLeave` DECIMAL(5, 1) COMMENT 'Tß╗òng sß╗æ ng├áy ph├⌐p hiß║┐u hß╗ë (kß║┐t h├┤n) ─æ├ú d├╣ng' DEFAULT '0.0', 
    `PendingMarriageLeave` DECIMAL(5, 1) COMMENT 'Tß╗òng sß╗æ ng├áy ph├⌐p hiß║┐u hß╗ë (kß║┐t h├┤n) ─æang chß╗¥ duyß╗çt' DEFAULT '0.0', 
    `UsedCompassionateLeave` DECIMAL(5, 1) COMMENT 'Tß╗òng sß╗æ ng├áy ph├⌐p tang gia/tang chß║┐ ─æ├ú d├╣ng' DEFAULT '0.0', 
    `PendingCompassionateLeave` DECIMAL(5, 1) COMMENT 'Tß╗òng sß╗æ ng├áy ph├⌐p tang gia/tang chß║┐ ─æang chß╗¥ duyß╗çt' DEFAULT '0.0', 
    `UsedMaternityLeave` DECIMAL(5, 1) COMMENT 'Tß╗òng sß╗æ ng├áy ph├⌐p v├¼ thai sß║ún ─æ├ú d├╣ng' DEFAULT '0.0', 
    `PendingMaternityLeave` DECIMAL(5, 1) COMMENT 'Tß╗òng sß╗æ ng├áy ph├⌐p v├¼ thai sß║ún ─æang chß╗¥ duyß╗çt' DEFAULT '0.0', 
    `LastTotalLeave` DECIMAL(5, 1) COMMENT 'Tß╗òng sß╗æ ng├áy ph├⌐p t├┤╠Çn n─âm cu╠â' DEFAULT '0.0', 
    `LastAvailableTotalLeave` DECIMAL(5, 1) COMMENT 'Tß╗òng sß╗æ ng├áy ph├⌐p t├┤╠Çn n─âm cu╠â kha╠ë du╠úng' DEFAULT '0.0'
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE UNIQUE INDEX `uid_StaffLeaveDays` ON `StaffLeave` (`StaffId`, `YearNumber`);

CREATE TABLE `StaffPublicAsset` (
    `StaffPublicAssetId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `StaffId` INTEGER(10) UNSIGNED NOT NULL, 
    `BranchId` INTEGER(11), 
    `Note` TEXT COLLATE utf8mb4_unicode_ci COMMENT 'Ghi ch├║', 
    `PublicAssetId` INTEGER(10) UNSIGNED, 
    `DeviceSerialNumber` VARCHAR(250) COLLATE utf8mb4_unicode_ci, 
    `DeviceCode` VARCHAR(250) COLLATE utf8mb4_unicode_ci, 
    `DeviceName` VARCHAR(250) COLLATE utf8mb4_unicode_ci, 
    `IssueDate` DATE NOT NULL COMMENT 'Ng├áy cß║Ñp thiß║┐t bß╗ï', 
    `RetrievalDate` DATE COMMENT 'Ng├áy thu hß╗ôi thiß║┐t bß╗ï', 
    `State` INTEGER(1) UNSIGNED NOT NULL COMMENT 'Trß║íng th├íi: 1 - ─Éang sß╗¡ dß╗Ñng, 2 - Thu hß╗ôi' DEFAULT '1', 
    `CreatedBy` INTEGER(11), 
    `CreatedDate` DATETIME, 
    `UpdatedBy` INTEGER(11), 
    `UpdatedDate` DATETIME, 
    PRIMARY KEY (`StaffPublicAssetId`), 
    CONSTRAINT `fk_StaffPublicAsset_PublicAsset` FOREIGN KEY(`PublicAssetId`) REFERENCES `PublicAsset` (`PublicAssetId`), 
    CONSTRAINT `fk_StaffPublicAsset_Staff` FOREIGN KEY(`StaffId`) REFERENCES `Staff` (`StaffId`)
)COMMENT='t├ái s?n c?p cho nh├ón vi├¬n n├áo' DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_StaffPublicAsset_Staff_idx` ON `StaffPublicAsset` (`StaffId`);

CREATE INDEX `fk_StaffPublicAsset_PublicAsset_idx` ON `StaffPublicAsset` (`PublicAssetId`);

CREATE TABLE `ComplaintAboutReason` (
    `ComplaintAboutReasonId` INTEGER(10) UNSIGNED NOT NULL, 
    `ComplaintReasonGroupId` INTEGER(11) NOT NULL, 
    `Ordering` INTEGER(10) UNSIGNED NOT NULL, 
    `Reason` VARCHAR(128) COLLATE utf8mb4_unicode_ci NOT NULL, 
    `State` INTEGER(1) UNSIGNED NOT NULL DEFAULT '0', 
    `CreatedAt` INTEGER(10) UNSIGNED NOT NULL, 
    `CreatedBy` INTEGER(10) UNSIGNED NOT NULL, 
    `LanguageId` INTEGER(10) UNSIGNED NOT NULL
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `TaskTag` (
    `Tag` VARCHAR(32) COLLATE utf8mb4_unicode_ci NOT NULL, 
    `IsCore` INTEGER(1) UNSIGNED NOT NULL COMMENT 'tag m?c ??nh c?a h? th?ng' DEFAULT '0', 
    `CreatedAt` INTEGER(10) UNSIGNED NOT NULL, 
    `CreatedBy` INTEGER(10) UNSIGNED NOT NULL, 
    `ApprovedAt` INTEGER(10) UNSIGNED NOT NULL DEFAULT '0', 
    `ApprovedBy` INTEGER(10) UNSIGNED, 
    `Hits` INTEGER(10) UNSIGNED NOT NULL DEFAULT '1', 
    `ColorRGB` VARCHAR(6) COLLATE utf8mb4_unicode_ci NOT NULL, 
    PRIMARY KEY (`Tag`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE UNIQUE INDEX `Tag_UNIQUE` ON `TaskTag` (`Tag`);

CREATE TABLE `User` (
    `UserId` INTEGER(11) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `Email` VARCHAR(128) CHARACTER SET utf8 NOT NULL, 
    `Mobile` VARCHAR(16) CHARACTER SET utf8, 
    `Password` VARCHAR(196) CHARACTER SET utf8, 
    `Avatar` VARCHAR(196) CHARACTER SET utf8, 
    `DateOfBirth` DATE, 
    `Gender` INTEGER(1) DEFAULT '0', 
    `Name` VARCHAR(64) CHARACTER SET utf8, 
    `ReferentId` VARCHAR(128) CHARACTER SET utf8, 
    `ConnectedTo` INTEGER(11) UNSIGNED, 
    `AuthenMethod` VARCHAR(32) CHARACTER SET utf8, 
    `ChangedPassword` INTEGER(11), 
    `ChangedPasswordToken` VARCHAR(32) CHARACTER SET utf8, 
    `RegistedAt` INTEGER(11) DEFAULT '0', 
    `CreatedBy` INTEGER(11) UNSIGNED DEFAULT '0', 
    `CreatedAt` INTEGER(11) DEFAULT '0', 
    `BlockedBy` INTEGER(11) UNSIGNED DEFAULT '0', 
    `BlockedAt` INTEGER(11) DEFAULT '0', 
    `BlockedNote` TEXT CHARACTER SET utf8, 
    `ActivatedAt` INTEGER(11) DEFAULT '0', 
    `ActivatedBy` INTEGER(11) UNSIGNED DEFAULT '0', 
    `LastLogedIn` INTEGER(11) DEFAULT '0', 
    `LastUpdated` INTEGER(11) DEFAULT '0', 
    `Trashed` INTEGER(1) UNSIGNED COMMENT 'd├╣ng ?? l?u tr?ng th├íi b? xo├í, m?t user kh├┤ng bao gi? b? xo├í "th?t s?" kh?i b?ng' DEFAULT '0', 
    PRIMARY KEY (`UserId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `Permission` (
    `PermissionCodeId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `PermissionCode` VARCHAR(128) NOT NULL, 
    `Name` VARCHAR(256), 
    `TypeCode` VARCHAR(256) NOT NULL, 
    `Description` VARCHAR(1048), 
    `Priority` INTEGER(10) UNSIGNED DEFAULT '1', 
    `IsActive` TINYINT(1) DEFAULT '1', 
    `Parent` VARCHAR(255), 
    `CreatedBy` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `UpdatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `UpdatedBy` INTEGER(11), 
    PRIMARY KEY (`PermissionCodeId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB;

CREATE UNIQUE INDEX `UNIQUE` ON `Permission` (`PermissionCode`);

CREATE TABLE `Notification` (
    `NotificationId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `Code` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    `Name` VARCHAR(512) COLLATE utf8mb4_unicode_ci, 
    `Summary` VARCHAR(1024) COLLATE utf8mb4_unicode_ci, 
    `Content` LONGTEXT COLLATE utf8mb4_unicode_ci, 
    `ContentType` INTEGER(11) COMMENT '1 Text
2 Video
3 Link', 
    `Priority` INTEGER(11) COMMENT '1 High, 
2 Nomal,
3 Low', 
    `Status` TINYINT(4) COMMENT '1 New, 
2 Waiiting,
3 Approved,
4 Rejected,
5 Recall', 
    `StatusNote` VARCHAR(1024) COLLATE utf8mb4_unicode_ci, 
    `NotificationTemplateId` INTEGER(11), 
    `IsComment` TINYINT(4) DEFAULT '1', 
    `Position` TINYINT(4) COMMENT '1 Normal
2 Banner' DEFAULT '0', 
    `PublishedDate` DATETIME, 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    `UpdatedDate` DATETIME, 
    `UpdatedBy` INTEGER(11), 
    `FromDate` DATETIME DEFAULT '2001-01-01 00:00:00', 
    `ToDate` DATETIME DEFAULT '2999-01-01 00:00:00', 
    `KIMHuman` TINYINT(4) DEFAULT '0', 
    PRIMARY KEY (`NotificationId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `TicketSupportCategory` (
    `TicketSupportCategoryId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `Name` VARCHAR(1024) COLLATE utf8mb4_unicode_ci, 
    `TicketSupportReceivingOrgId` INTEGER(11), 
    `Priority` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `JsonData` VARCHAR(1000) COLLATE utf8mb4_unicode_ci, 
    PRIMARY KEY (`TicketSupportCategoryId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `RentalContractTracking` (
    `RentalContractTrackingId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `RentalContractId` INTEGER(11) NOT NULL, 
    `RentalContractTypeId` INTEGER(11), 
    `Name` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `Code` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `Representative` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `BranchId` INTEGER(11), 
    `SignedDate` DATETIME, 
    `FromDate` DATETIME, 
    `ToDate` DATETIME, 
    `TerminationDate` DATETIME, 
    `TerminationReason` TEXT COLLATE utf8mb4_unicode_ci, 
    `ProcessContent` TEXT COLLATE utf8mb4_unicode_ci, 
    `IsTermination` TINYINT(4) DEFAULT '0', 
    `IsProcessed` TINYINT(4) DEFAULT '0', 
    `IsAlert` TINYINT(4) DEFAULT '1', 
    `State` INTEGER(11) COMMENT '1: active, 2: expired, 3: alert' DEFAULT '1', 
    `AlertType` VARCHAR(255) COLLATE utf8mb4_unicode_ci DEFAULT 'Day', 
    `AlertBeforeTime` INTEGER(11) DEFAULT '0', 
    `PartnerCompany` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `PartnerAddress` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `PartnerRepresentative` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `PartnerEmail` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `PartnerPhone` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Comment` TEXT COLLATE utf8mb4_unicode_ci, 
    `ActionName` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    PRIMARY KEY (`RentalContractTrackingId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `YearlyRepeatHoliday` (
    `Month` INTEGER(2) UNSIGNED NOT NULL, 
    `Day` INTEGER(2) UNSIGNED NOT NULL, 
    `Name` VARCHAR(32) CHARACTER SET utf8mb4 NOT NULL, 
    PRIMARY KEY (`Month`, `Day`)
)COMMENT='b?ng l?u c├íc ng├áy l? l?p l?i m?i n?m theo l?ch d??ng: V├¡ d? T?t D??ng L?ch, Qu?c Kh├ính...' DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `PaidHoliday` (
    `Id` INTEGER(11) NOT NULL, 
    `Date` DATE, 
    `Name` VARCHAR(128) COLLATE utf8mb4_unicode_ci, 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    PRIMARY KEY (`Id`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE UNIQUE INDEX `Date_UNIQUE` ON `PaidHoliday` (`Date`);

CREATE TABLE `CertificateDetail` (
    `CertificateDetailId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `CertificateId` INTEGER(10), 
    `StaffId` INTEGER(10), 
    `WorkDay` VARCHAR(10) COLLATE utf8mb4_unicode_ci, 
    `startTime` TIME, 
    `endTime` TIME, 
    `BranchId` INTEGER(11), 
    `CreatedBy` INTEGER(10) UNSIGNED, 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `UpdatedBy` INTEGER(10) UNSIGNED, 
    `UpdatedDate` DATETIME, 
    `IsDeleted` INTEGER(11) DEFAULT '0', 
    PRIMARY KEY (`CertificateDetailId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `Month` (
    `MonthId` INTEGER(10) UNSIGNED NOT NULL, 
    `Name` VARCHAR(16) CHARACTER SET utf8mb4 NOT NULL, 
    `Ordering` INTEGER(2) NOT NULL, 
    PRIMARY KEY (`MonthId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `CertificateGroup` (
    `CertificateGroupId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `Name` VARCHAR(300) COLLATE utf8mb4_unicode_ci, 
    `Code` VARCHAR(100) COLLATE utf8mb4_unicode_ci, 
    `Ordering` INTEGER(10) UNSIGNED NOT NULL, 
    `State` TINYINT(1) UNSIGNED COMMENT 'Trß║íng th├íi: 0 - Inactive, 1 - Active' DEFAULT '1', 
    PRIMARY KEY (`CertificateGroupId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `SubsidizeStaffHistory` (
    `SubsidizeId` INTEGER(10) UNSIGNED NOT NULL, 
    `WorkProfileId` INTEGER(10) UNSIGNED NOT NULL, 
    `StaffId` INTEGER(10) UNSIGNED NOT NULL, 
    `IssueDate` DATE NOT NULL, 
    `Desc` MEDIUMTEXT CHARACTER SET utf8mb4, 
    `Amount` DECIMAL(12, 2) UNSIGNED NOT NULL, 
    `TaxInclude` INTEGER(1) NOT NULL DEFAULT '1', 
    `FlushedAt` INTEGER(11) UNSIGNED NOT NULL, 
    `EndDate` DATE
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `TicketSupportComment` (
    `TicketSupportCommentId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `TicketSupportId` INTEGER(11), 
    `Content` TEXT COLLATE utf8mb4_unicode_ci, 
    `CreatedBy` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`TicketSupportCommentId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `idx_Ticket` ON `TicketSupportComment` (`TicketSupportId`);

CREATE INDEX `idx_Staff` ON `TicketSupportComment` (`CreatedBy`);

CREATE TABLE `WorkMultiProfilePosition` (
    `WorkMultiProfilePositionId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `WorkContractId` INTEGER(11), 
    `WorkContractAnnexId` INTEGER(11), 
    `WorkProfilePositionId` INTEGER(11), 
    `CreatedBy` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `UpdatedBy` INTEGER(11), 
    `UpdatedDate` DATETIME, 
    `State` INTEGER(11), 
    PRIMARY KEY (`WorkMultiProfilePositionId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `StaffPublicAssetTracking` (
    `StaffPublicAssetTrackingId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `ActionName` VARCHAR(250) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'Create', 
    `StaffPublicAssetId` INTEGER(10) UNSIGNED, 
    `StaffId` INTEGER(10) UNSIGNED, 
    `BranchId` INTEGER(11), 
    `Note` TEXT COLLATE utf8mb4_unicode_ci COMMENT 'Ghi ch├║', 
    `PublicAssetId` INTEGER(10) UNSIGNED, 
    `DeviceSerialNumber` VARCHAR(250) COLLATE utf8mb4_unicode_ci, 
    `DeviceCode` VARCHAR(250) COLLATE utf8mb4_unicode_ci, 
    `DeviceName` VARCHAR(250) COLLATE utf8mb4_unicode_ci, 
    `IssueDate` DATE COMMENT 'Ng├áy cß║Ñp thiß║┐t bß╗ï', 
    `RetrievalDate` DATE COMMENT 'Ng├áy thu hß╗ôi thiß║┐t bß╗ï', 
    `State` INTEGER(1) UNSIGNED COMMENT 'Trß║íng th├íi: 1 - ─Éang sß╗¡ dß╗Ñng, 2 - Thu hß╗ôi' DEFAULT '1', 
    `CreatedBy` INTEGER(11), 
    `CreatedDate` DATETIME, 
    PRIMARY KEY (`StaffPublicAssetTrackingId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `CustomHolidayByYear` (
    `HolidayDate` DATE NOT NULL, 
    `Name` VARCHAR(32) CHARACTER SET utf8mb4 NOT NULL, 
    PRIMARY KEY (`HolidayDate`)
)COMMENT='b?ng l?u (ng├áy d??ng) c├íc ng├áy l? thi?t l?p theo t?ng n?m. V├¡ d?: t?t ├óm l?ch, gi? t? H├╣ng V??ng...' DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE UNIQUE INDEX `HolidayDate_UNIQUE` ON `CustomHolidayByYear` (`HolidayDate`);

CREATE TABLE `Relationship` (
    `RelationshipId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `Name` VARCHAR(64) COLLATE utf8mb4_unicode_ci, 
    `Ordering` INTEGER(10) UNSIGNED DEFAULT '0', 
    `RelationshipGroupId` INTEGER(10) UNSIGNED NOT NULL, 
    PRIMARY KEY (`RelationshipId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_Relationship_RelationshipGroup_idx` ON `Relationship` (`RelationshipGroupId`);

CREATE TABLE `PublicAsset` (
    `PublicAssetId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `Name` VARCHAR(32) COLLATE utf8mb4_unicode_ci NOT NULL, 
    `Ordering` INTEGER(11) NOT NULL DEFAULT '0', 
    `State` INTEGER(1) NOT NULL DEFAULT '1', 
    PRIMARY KEY (`PublicAssetId`)
)COMMENT='C├íc t├ái s?n c├┤ng c?p cho nh├ón vi├¬n' DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `WorkProfileFulltimeTracking` (
    `Id` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `StaffId` INTEGER(11) NOT NULL, 
    `WorkProfileId` INTEGER(10), 
    `WorkContractId` INTEGER(10), 
    `WorkScheduleId` INTEGER(11), 
    `IsFullTime` INTEGER(1) COMMENT '0 FullTime sang Ca, 1 Ca sang FullTime', 
    `FromDate` DATETIME, 
    `ToDate` DATETIME, 
    `CreatedBy` INTEGER(11), 
    `CreatedDate` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`Id`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `StaffIdentityPaper` (
    `StaffIdentityPaperId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `StaffId` INTEGER(11), 
    `Type` SMALLINT(6) COMMENT '1: CMND, 2: CCCD, 3: Passport', 
    `Code` VARCHAR(20) COLLATE utf8mb4_unicode_ci, 
    `IssuedDate` DATE, 
    `IssuedBy` VARCHAR(128) COLLATE utf8mb4_unicode_ci, 
    `IsOld` INTEGER(11) DEFAULT '0', 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11) COMMENT 'used UserId', 
    `UpdatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `UpdatedBy` INTEGER(11) COMMENT 'used UserId', 
    PRIMARY KEY (`StaffIdentityPaperId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `IX_StaffIdentityPaper_StaffId` ON `StaffIdentityPaper` (`StaffId`);

CREATE TABLE `MonthDay` (
    `MonthDayId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `Name` VARCHAR(8) CHARACTER SET utf8mb4 NOT NULL, 
    `Ordering` INTEGER(2) NOT NULL, 
    `StartTime` TIME NOT NULL, 
    `EndTime` TIME NOT NULL, 
    `TotalBreakTimeInMinute` INTEGER(10) UNSIGNED NOT NULL, 
    PRIMARY KEY (`MonthDayId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `AbsenceRequestDetail` (
    `AbsenceRequestId` INTEGER(10) UNSIGNED NOT NULL, 
    `Date` DATE NOT NULL, 
    `WorkScheduleId` INTEGER(10) UNSIGNED, 
    `WorkShiftId` INTEGER(10) UNSIGNED, 
    `AbsenceFromTime` TIME NOT NULL, 
    `AbsenceToTime` TIME NOT NULL, 
    `TotalDays` DECIMAL(6, 2) DEFAULT '0.00', 
    `RequestedBy` INTEGER(11), 
    PRIMARY KEY (`AbsenceRequestId`, `Date`, `AbsenceFromTime`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `ix_AbsenceRequestDetail_Date_RequestedBy` ON `AbsenceRequestDetail` (`Date`, `RequestedBy`);

CREATE INDEX `fk_AbsenceRequestDetail_AbsenceRequest_idx` ON `AbsenceRequestDetail` (`AbsenceRequestId`);

CREATE INDEX `Index` ON `AbsenceRequestDetail` (`WorkScheduleId`, `Date`);

CREATE TABLE `AbsenceConfig` (
    `AbsenceConfigId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `CompanyId` INTEGER(10) UNSIGNED NOT NULL, 
    `ApplyFromDate` DATE NOT NULL, 
    `ApplyToDate` DATE NOT NULL, 
    `State` INTEGER(1) UNSIGNED NOT NULL DEFAULT '1', 
    `MaximumOffDaysPerYear` INTEGER(11) COMMENT 's? ng├áy ngh? t?i ?a (l├ám theo ng├áy)', 
    `MaximumOffHoursPerYear` INTEGER(11) COMMENT 's? gi? ngh? t?i ?a (l├ám b├ín th?i gian, theo ca)', 
    `MaximumOfShiftsPerYear` INTEGER(11) COMMENT 's? ca ngh? t?i ?a (l├ám b├ín th?i gian, theo ca)', 
    `WorkDayEndAt` TIME NOT NULL, 
    `WorkDayStartAt` TIME NOT NULL, 
    `CreatedBy` INTEGER(10) UNSIGNED NOT NULL, 
    `CreatedAt` INTEGER(10) UNSIGNED NOT NULL, 
    `EditedBy` INTEGER(10) UNSIGNED NOT NULL, 
    `EditedAt` INTEGER(10) UNSIGNED NOT NULL, 
    PRIMARY KEY (`AbsenceConfigId`), 
    CONSTRAINT `fk_AbsenceConfig_Company` FOREIGN KEY(`CompanyId`) REFERENCES `Company` (`CompanyId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_AbsenceConfig_Company_idx` ON `AbsenceConfig` (`CompanyId`);

CREATE TABLE `IncomeBaseDaily` (
    `IncomeBaseDailyId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `StaffId` INTEGER(11), 
    `IncomeTypeId` INTEGER(11), 
    `IncomeTypeLevelId` INTEGER(11), 
    `WorkDate` DATE, 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    `TimeKeeperId` INTEGER(11), 
    `IncomePerHour` DECIMAL(18, 2), 
    `WorkHourStandard` DECIMAL(10, 2), 
    PRIMARY KEY (`IncomeBaseDailyId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `VnDistrictUpdate` (
    `VnDistrictId` INTEGER(10) UNSIGNED NOT NULL, 
    `VnProvinceId` INTEGER(10) UNSIGNED NOT NULL, 
    `DistrictCode` VARCHAR(8), 
    `DistrictPostalCode` VARCHAR(8), 
    `NameVi` VARCHAR(64) NOT NULL, 
    `NameEn` VARCHAR(64), 
    `LabelVi` VARCHAR(32) NOT NULL COMMENT 'Qu?n
Th? x├ú
Huy?n
Th├ánh ph?', 
    `LabelEn` VARCHAR(32) COMMENT 'Urban District
Town
Rural District
Provincial City', 
    `Ordering` INTEGER(10) UNSIGNED, 
    `NameViOld` VARCHAR(64), 
    PRIMARY KEY (`VnDistrictId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB;

CREATE INDEX `fk_VnDistrict_VnProvince_idx` ON `VnDistrictUpdate` (`VnProvinceId`);

CREATE TABLE `VnWard_BK_20230710` (
    `VnWardId` INTEGER(10) UNSIGNED NOT NULL, 
    `VnDistrictId` INTEGER(10) UNSIGNED NOT NULL, 
    `WardCode` VARCHAR(8) CHARACTER SET utf8mb4, 
    `WardPostalCode` VARCHAR(8) CHARACTER SET utf8mb4, 
    `NameVi` VARCHAR(64) CHARACTER SET utf8mb4 NOT NULL, 
    `NameEn` VARCHAR(64) CHARACTER SET utf8mb4, 
    `LabelVi` VARCHAR(32) CHARACTER SET utf8mb4 NOT NULL COMMENT 'Ph??ng
X├ú
Th? tr?n', 
    `LabelEn` VARCHAR(32) CHARACTER SET utf8mb4 COMMENT 'Commune
Ward
Township', 
    `Ordering` INTEGER(10) UNSIGNED, 
    `isDeleted` TINYINT(4)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `Widget` (
    `WidgetId` INTEGER(11) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `ExtensionId` INTEGER(11) UNSIGNED NOT NULL, 
    `AppId` INTEGER(11) UNSIGNED NOT NULL, 
    `SysLanguageId` INTEGER(11) UNSIGNED NOT NULL, 
    `Name` VARCHAR(128) CHARACTER SET utf8 NOT NULL, 
    `Dir` VARCHAR(32) CHARACTER SET utf8 NOT NULL, 
    `State` INTEGER(1) UNSIGNED NOT NULL DEFAULT '1', 
    `Title` VARCHAR(128) CHARACTER SET utf8 NOT NULL, 
    `IsShowTitle` INTEGER(1) DEFAULT '1', 
    `Position` VARCHAR(32) CHARACTER SET utf8 NOT NULL, 
    `Ordering` INTEGER(11) UNSIGNED NOT NULL DEFAULT '0', 
    `Config` TEXT CHARACTER SET utf8 NOT NULL, 
    `CreatedBy` INTEGER(11) UNSIGNED NOT NULL, 
    `CreatedAt` INTEGER(11) UNSIGNED NOT NULL, 
    `Description` TEXT CHARACTER SET utf8 NOT NULL, 
    `CheckedOutBy` INTEGER(11) UNSIGNED, 
    `CheckedOutAt` INTEGER(11) UNSIGNED DEFAULT '0', 
    `ShowUp` INTEGER(11), 
    `PutDown` INTEGER(11), 
    PRIMARY KEY (`WidgetId`), 
    CONSTRAINT `fk_Widget_CreatedBy` FOREIGN KEY(`CreatedBy`) REFERENCES `User` (`UserId`), 
    CONSTRAINT `fk_Widget_Extension` FOREIGN KEY(`ExtensionId`, `AppId`) REFERENCES `Extension` (`ExtensionId`, `AppId`), 
    CONSTRAINT `fk_Widget_SysLanguage` FOREIGN KEY(`SysLanguageId`) REFERENCES `SysLanguage` (`SysLanguageId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_Widget_SysLanguage_idx` ON `Widget` (`SysLanguageId`);

CREATE INDEX `fk_Widget_Extension_idx` ON `Widget` (`ExtensionId`, `AppId`);

CREATE INDEX `fk_Widget_CreatedBy_idx` ON `Widget` (`CreatedBy`);

CREATE TABLE `WorkContractHistory` (
    `WorkContractHistoryId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `IdNumber` VARCHAR(16) COLLATE utf8mb4_unicode_ci, 
    `FullName` VARCHAR(64) COLLATE utf8mb4_unicode_ci, 
    `DateOfBirth` DATE NOT NULL, 
    `Address` VARCHAR(196) COLLATE utf8mb4_unicode_ci, 
    `PhoneNumber` VARCHAR(16) COLLATE utf8mb4_unicode_ci, 
    `StaffId` INTEGER(10) UNSIGNED NOT NULL, 
    `StaffCode` VARCHAR(16) COLLATE utf8mb4_unicode_ci, 
    `WorkContractId` INTEGER(10) UNSIGNED NOT NULL, 
    `WorkContractCode` VARCHAR(32) COLLATE utf8mb4_unicode_ci, 
    `WorkContractFromDate` DATE NOT NULL, 
    `WorkContractToDate` DATE, 
    `WorkContractTypeId` INTEGER(10) UNSIGNED NOT NULL, 
    `EmploymentType` INTEGER(10) UNSIGNED NOT NULL, 
    `ContractAttachFile` VARCHAR(128) COLLATE utf8mb4_unicode_ci, 
    `OtherAgreements` VARCHAR(1000) COLLATE utf8mb4_unicode_ci, 
    `GrossSalary` DECIMAL(18, 2) UNSIGNED NOT NULL DEFAULT '0.00', 
    `BaseSalary` DECIMAL(18, 2) UNSIGNED NOT NULL DEFAULT '0.00', 
    `JobAllowance` DECIMAL(18, 2) UNSIGNED NOT NULL DEFAULT '0.00', 
    `ComplianceBonus` DECIMAL(18, 2) UNSIGNED NOT NULL DEFAULT '0.00', 
    `LunchAllowance` DECIMAL(18, 2) UNSIGNED NOT NULL DEFAULT '0.00', 
    `UniformAllowance` DECIMAL(18, 2) UNSIGNED NOT NULL DEFAULT '0.00', 
    `Action` VARCHAR(1000) COLLATE utf8mb4_unicode_ci, 
    `WorkContractAnnexCode` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    `ContractAnnexAttachFile` VARCHAR(128) COLLATE utf8mb4_unicode_ci, 
    `Note` VARCHAR(1000) COLLATE utf8mb4_unicode_ci, 
    `CreatedBy` INTEGER(11) NOT NULL, 
    `CreatedDate` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`WorkContractHistoryId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `IDX_WorkContractHistory_WorkContractId` ON `WorkContractHistory` (`WorkContractId`);

CREATE TABLE `AbsenceRequest` (
    `AbsenceRequestId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `AbsenceTypeId` INTEGER(10) UNSIGNED NOT NULL, 
    `CreatedBy` INTEGER(11), 
    `RequestedBy` INTEGER(10) UNSIGNED NOT NULL, 
    `RequestedAt` INTEGER(10) UNSIGNED NOT NULL, 
    `Note` TEXT CHARACTER SET utf8mb4, 
    `RequestStatus` INTEGER(10) UNSIGNED NOT NULL COMMENT 'tr?ng th├íi c?a request ngh?
1: ??ng ├╜
2: t? ch?i
3: h?y phi?u' DEFAULT '0', 
    `ProcessedBy` INTEGER(10) UNSIGNED COMMENT '???c x? l├╜ b?i ai (approved, denied,cancel...)', 
    `ProcessedAt` INTEGER(10) UNSIGNED, 
    `AbsenceConfigId` INTEGER(10) UNSIGNED NOT NULL, 
    `AbsenceFrom` INTEGER(11), 
    `AbsenceTo` INTEGER(11), 
    `ProcessedNote` TEXT CHARACTER SET utf8mb4, 
    `ActualStartDate` DATETIME, 
    `ActualEndDate` DATETIME, 
    `ActualTotalDays` DECIMAL(6, 2) DEFAULT '0.00', 
    PRIMARY KEY (`AbsenceRequestId`), 
    CONSTRAINT `fk_AbsenceRequest_AbsenceConfig` FOREIGN KEY(`AbsenceConfigId`) REFERENCES `AbsenceConfig` (`AbsenceConfigId`), 
    CONSTRAINT `fk_AbsenceRequest_AbsenceType` FOREIGN KEY(`AbsenceTypeId`) REFERENCES `AbsenceType` (`AbsenceTypeId`), 
    CONSTRAINT `fk_AbsenceRequest_RequestedBy` FOREIGN KEY(`RequestedBy`) REFERENCES `Staff` (`StaffId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_AbsenceRequest_RequestedBy_idx` ON `AbsenceRequest` (`RequestedBy`);

CREATE INDEX `fk_AbsenceRequest_AbsenceType_idx` ON `AbsenceRequest` (`AbsenceTypeId`);

CREATE INDEX `fk_AbsenceRequest_AbsenceConfig_idx` ON `AbsenceRequest` (`AbsenceConfigId`);

CREATE TABLE `Branch` (
    `BranchId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `BranchCode` VARCHAR(16) CHARACTER SET utf8mb4 NOT NULL, 
    `Name` VARCHAR(128) CHARACTER SET utf8mb4 NOT NULL, 
    `Address` VARCHAR(256) CHARACTER SET utf8mb4, 
    `CompanyId` INTEGER(10) UNSIGNED NOT NULL, 
    `CountryId` INTEGER(10) UNSIGNED NOT NULL, 
    `ProvinceId` INTEGER(10) UNSIGNED, 
    `DistrictId` INTEGER(10) UNSIGNED, 
    `WardId` INTEGER(10) UNSIGNED, 
    `BusinessLicenseCode` VARCHAR(10) COLLATE utf8mb4_unicode_ci, 
    `BusinessLicenseName` VARCHAR(200) COLLATE utf8mb4_unicode_ci, 
    `PublicPhoneNumber` VARCHAR(16) CHARACTER SET utf8mb4, 
    `PrivatePhoneNumber` VARCHAR(16) CHARACTER SET utf8mb4, 
    `PhoneExts` VARCHAR(64) CHARACTER SET utf8mb4, 
    `OpenAt` VARCHAR(8) CHARACTER SET utf8mb4 DEFAULT '8:00', 
    `CloseAt` VARCHAR(8) CHARACTER SET utf8mb4 DEFAULT '20:00', 
    `State` INTEGER(1) NOT NULL COMMENT 'trß║íng th├íi:
- sß║»p hoß║ít ─æß╗Öng (0)
- ─æang hoß║ít ─æß╗Öng (1)
- ng╞░ng hoß║ít ─æß╗Öng (-1)' DEFAULT '1', 
    `Ordering` INTEGER(11) NOT NULL COMMENT 'Sß║»p xß║┐p' DEFAULT '0', 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `ExcludeReport` INTEGER(11) DEFAULT '0', 
    `ORCRefCode` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `ORCExtraTime` INTEGER(10) COMMENT 'Hß╗ç thß╗æng sß║╜ tß╗▒ ─æß╗Öng x├íc nhß║¡n ─æ╞ín h├áng nß║┐u thß╗¥i gian x├íc nhß║¡n v╞░ß╗út qu├í sß╗æ ng├áy ORCExtraTime', 
    `Old_Address` VARCHAR(500) COLLATE utf8mb4_unicode_ci, 
    `GoogleMapIFrame` VARCHAR(4000) COLLATE utf8mb4_unicode_ci, 
    `ImageCDN` VARCHAR(4000) COLLATE utf8mb4_unicode_ci, 
    `WorkingTime` VARCHAR(4000) COLLATE utf8mb4_unicode_ci, 
    `LatestUpdated` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
    `Priority` INTEGER(11), 
    `GrandOpening` INTEGER(11) DEFAULT '0', 
    `IsFilterReport` TINYINT(4) DEFAULT '1', 
    PRIMARY KEY (`BranchId`), 
    CONSTRAINT `fk_Branch_Company` FOREIGN KEY(`CompanyId`) REFERENCES `Company` (`CompanyId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_Branch_Country_idx` ON `Branch` (`CountryId`);

CREATE INDEX `fk_Branch_Company_idx` ON `Branch` (`CompanyId`);

CREATE INDEX `IX_LatestUpdated` ON `Branch` (`LatestUpdated`);

CREATE TABLE `TicketSupportImage` (
    `TicketSupportImageId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `TicketSupportId` INTEGER(11), 
    `CDNURL` VARCHAR(1024) COLLATE utf8mb4_unicode_ci, 
    `IsDeleted` INTEGER(11) DEFAULT '0', 
    `Priority` TINYINT(4), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    PRIMARY KEY (`TicketSupportImageId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `IDX_TicketId` ON `TicketSupportImage` (`TicketSupportId`);

CREATE TABLE `LanguageLevel` (
    `LanguageLevelId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `LanguageId` INTEGER(10) UNSIGNED NOT NULL, 
    `Level` VARCHAR(255) CHARACTER SET utf8mb4, 
    `Ordering` INTEGER(10) UNSIGNED NOT NULL DEFAULT '0', 
    PRIMARY KEY (`LanguageLevelId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_LanguageLevel_language` ON `LanguageLevel` (`LanguageId`);

CREATE TABLE `AbsenceRequestSendTo` (
    `AbsenceRequestId` INTEGER(10) UNSIGNED NOT NULL, 
    `SendToStaffId` INTEGER(10) UNSIGNED NOT NULL, 
    `SentAt` INTEGER(10) UNSIGNED NOT NULL, 
    `ProcessedAt` INTEGER(10) UNSIGNED, 
    `Note` TEXT CHARACTER SET utf8mb4, 
    PRIMARY KEY (`AbsenceRequestId`, `SendToStaffId`), 
    CONSTRAINT `fk_AbsenceRequestSendTo_AbsenceRequest` FOREIGN KEY(`AbsenceRequestId`) REFERENCES `AbsenceRequest` (`AbsenceRequestId`), 
    CONSTRAINT `fk_AbsenceRequestSendTo_SendToStaffId` FOREIGN KEY(`SendToStaffId`) REFERENCES `Staff` (`StaffId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_AbsenceRequestSendTo_SendToStaffId_idx` ON `AbsenceRequestSendTo` (`SendToStaffId`);

CREATE INDEX `fk_AbsenceRequestSendTo_AbsenceRequest_idx` ON `AbsenceRequestSendTo` (`AbsenceRequestId`);

CREATE TABLE `CompanyManager` (
    `CompanyId` INTEGER(10) UNSIGNED NOT NULL, 
    `WorkProfileId` INTEGER(10) UNSIGNED NOT NULL, 
    `StaffId` INTEGER(10) UNSIGNED NOT NULL COMMENT '─æang l├á ng╞░ß╗¥i quß║ún l├╜ hiß╗çn tß║íi', 
    `Title` VARCHAR(128) CHARACTER SET utf8mb4, 
    `FromDate` DATE NOT NULL, 
    `ToDate` DATE, 
    `IsCurrentManager` INTEGER(1) UNSIGNED NOT NULL DEFAULT '1', 
    CONSTRAINT fk_company_manager FOREIGN KEY(`CompanyId`) REFERENCES `Company` (`CompanyId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_CompanyManager_WorkProfile_idx` ON `CompanyManager` (`WorkProfileId`, `StaffId`);

CREATE INDEX `fk_CompanyManager_Company_idx` ON `CompanyManager` (`CompanyId`);

CREATE TABLE `ByWeekDay` (
    `WorkScheduleId` INTEGER(10) UNSIGNED NOT NULL, 
    `WeekDayId` INTEGER(10) UNSIGNED NOT NULL, 
    `BranchId` INTEGER(10) UNSIGNED, 
    `StartTime` TIME NOT NULL, 
    `EndTime` TIME NOT NULL, 
    `TotalBreakTimeInMinute` INTEGER(11) NOT NULL DEFAULT '0', 
    CONSTRAINT `fk_ByWeekDay_WeekDay` FOREIGN KEY(`WeekDayId`) REFERENCES `WeekDay` (`WeekDayId`), 
    CONSTRAINT `fk_ByWeekDay_WorkSchedule` FOREIGN KEY(`WorkScheduleId`) REFERENCES `WorkSchedule` (`WorkScheduleId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_ByWeekDay_WorkSchedule_idx` ON `ByWeekDay` (`WorkScheduleId`);

CREATE INDEX `fk_ByWeekDay_WorkLocationId_idx` ON `ByWeekDay` (`BranchId`);

CREATE INDEX `fk_ByWeekDay_WeekDay_idx` ON `ByWeekDay` (`WeekDayId`);

CREATE TABLE `TicketSupportRelatedObject` (
    `TicketSupportObjectRelatedId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `TicketSupportId` INTEGER(11), 
    `ObjectType` TINYINT(4) COMMENT '1: Org
2:Person', 
    `ObjectId` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `DeletedDate` DATETIME, 
    PRIMARY KEY (`TicketSupportObjectRelatedId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `idx_ObjectId` ON `TicketSupportRelatedObject` (`ObjectId`);

CREATE TABLE `AdminExecute` (
    `AdminExecuteId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `ExecutedBy` INTEGER(10) UNSIGNED NOT NULL, 
    `ExecutedAt` INTEGER(10) UNSIGNED NOT NULL, 
    PRIMARY KEY (`AdminExecuteId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_AdminExecute_ExecutedBy_idx` ON `AdminExecute` (`ExecutedBy`);

CREATE TABLE `Province` (
    `ProvinceId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `ProviceCode` VARCHAR(5) COLLATE utf8mb4_unicode_ci, 
    `ProvinceName` VARCHAR(100) COLLATE utf8mb4_unicode_ci, 
    `Label` VARCHAR(20) COLLATE utf8mb4_unicode_ci, 
    `State` TINYINT(1) DEFAULT '1', 
    `VnProvinceId` INTEGER(11), 
    PRIMARY KEY (`ProvinceId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `WorkProfileStaffGroup` (
    `StaffGroupId` INTEGER(10) UNSIGNED NOT NULL, 
    `WorkProfileId` INTEGER(10) UNSIGNED NOT NULL, 
    `StaffId` INTEGER(10) UNSIGNED NOT NULL
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_WorkProfileStaffGroup_WorkProfile1_idx` ON `WorkProfileStaffGroup` (`WorkProfileId`, `StaffId`);

CREATE INDEX `fk_WorkProfileStaffGroup_StaffGroup1_idx` ON `WorkProfileStaffGroup` (`StaffGroupId`);

CREATE TABLE `CandidateOffer` (
    `CandidateOfferId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `CandidateId` INTEGER(11), 
    `Code` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    `Status` INTEGER(11) COMMENT '1 new, 2 finished,3 cancel', 
    `StatusNote` VARCHAR(4096) COLLATE utf8mb4_unicode_ci, 
    `OfferExpiredDate` DATETIME, 
    `CompanyId` INTEGER(11), 
    `DepartmentId` INTEGER(11), 
    `TeamId` INTEGER(11), 
    `WorkPositionId` INTEGER(11), 
    `StaffLevelId` INTEGER(11), 
    `BranchId` INTEGER(11), 
    `Location` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `WorkTimeMode` VARCHAR(20) COLLATE utf8mb4_unicode_ci, 
    `SalaryAmount` DECIMAL(18, 2), 
    `ProbationFromDate` DATE, 
    `ProbationToDate` DATE, 
    `ProbationWorkLocationId` INTEGER(11) COMMENT '  Json [{''Type'':''Ph? c?p ??m b?o thu nh?p'',''Amount'':200000},{''Type'':''Ph? c?p ch?ng ch? h├ánh ngh?'',''Amount'':500000}]', 
    `UpdatedDate` DATETIME, 
    `UpdatedBy` INTEGER(11), 
    `Type` TINYINT(4), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    `Note` TEXT COLLATE utf8mb4_unicode_ci, 
    PRIMARY KEY (`CandidateOfferId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `DependantPeople` (
    `DependantPeopleId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `FullName` VARCHAR(64) CHARACTER SET utf8mb4 NOT NULL, 
    `IdNumber` VARCHAR(16) CHARACTER SET utf8mb4, 
    `PassportNumber` VARCHAR(16) CHARACTER SET utf8mb4, 
    `NationalInsuranceNumber` VARCHAR(16) CHARACTER SET utf8mb4, 
    `TaxNumber` VARCHAR(16) CHARACTER SET utf8mb4, 
    `DateOfBirth` DATE, 
    `State` INTEGER(1) UNSIGNED NOT NULL, 
    `IssuedDate` DATE, 
    `ReleasedDate` DATE, 
    `Nationality` INTEGER(10) UNSIGNED NOT NULL, 
    `StaffId` INTEGER(10) UNSIGNED NOT NULL, 
    `DependantRelationshipId` INTEGER(10) UNSIGNED NOT NULL, 
    `PhoneNumber` VARCHAR(11) COLLATE utf8mb4_unicode_ci, 
    `IsDependant` INTEGER(1) NOT NULL DEFAULT '0', 
    `Address` VARCHAR(196) COLLATE utf8mb4_unicode_ci, 
    `Email` VARCHAR(128) COLLATE utf8mb4_unicode_ci, 
    `IsUrgentContact` INTEGER(1) NOT NULL DEFAULT '0', 
    `GenderId` INTEGER(11) COMMENT '1 Nam
2 N?', 
    `ProvinceId` INTEGER(11), 
    `WardId` INTEGER(11), 
    `EthnicId` INTEGER(11) NOT NULL COMMENT 'd├ón t├┤c' DEFAULT '1', 
    `InsuranceHospitalId` VARCHAR(20) COLLATE utf8mb4_unicode_ci, 
    `DistrictId` INTEGER(11), 
    `HealthInsuranceCode` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `IdentityIssuedDate` DATE, 
    `IdentityIssuedBy` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `DeductionFromDate` DATE, 
    `DeductionToDate` DATE, 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`DependantPeopleId`), 
    CONSTRAINT `fk_DependantPeople_DependantPeopleRelationshipId` FOREIGN KEY(`DependantRelationshipId`) REFERENCES `DependantRelationship` (`DependantRelationshipId`), 
    CONSTRAINT `fk_dependantPeople_staff` FOREIGN KEY(`StaffId`) REFERENCES `Staff` (`StaffId`)
)COMMENT='quan h? gi?m tr? gia c?nh' DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_DependantPeople_Staff_idx` ON `DependantPeople` (`StaffId`);

CREATE INDEX `fk_DependantPeople_DependantRelationship_idx` ON `DependantPeople` (`DependantRelationshipId`);

CREATE INDEX `IX_PhoneNumber` ON `DependantPeople` (`PhoneNumber`);

CREATE INDEX `IX_FullName` ON `DependantPeople` (`FullName`);

CREATE TABLE `TicketSupport` (
    `TicketSupportId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `ReceivingOrgId` INTEGER(11), 
    `TicketCategoryId` INTEGER(11), 
    `Content` TEXT COLLATE utf8mb4_unicode_ci, 
    `Status` TINYINT(4) COMMENT '1 New
5  Received
10 Completed', 
    `CreatedBy` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `ResultBy` INTEGER(11), 
    `ResultDate` DATETIME, 
    `ResultContent` TEXT COLLATE utf8mb4_unicode_ci, 
    `RatingContent` TEXT COLLATE utf8mb4_unicode_ci, 
    `RatingDate` DATETIME, 
    `CancelDate` DATETIME, 
    `ReceiveBy` INTEGER(11), 
    `ReceiveDate` DATETIME, 
    `ReceiveContent` TEXT COLLATE utf8mb4_unicode_ci, 
    `RejectedBy` INTEGER(10) UNSIGNED, 
    `RejectedDate` DATETIME, 
    `RejectedContent` TEXT COLLATE utf8mb4_unicode_ci, 
    `SendingOrgId` INTEGER(11), 
    `JsonContent` VARCHAR(4000) COLLATE utf8mb4_unicode_ci, 
    `IsPublic` INTEGER(11) DEFAULT '1', 
    `CustomerId` INTEGER(11), 
    `RelatedStaffId` INTEGER(11), 
    `SpecificationText` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `TicketSupportSpecificationDetailId` INTEGER(11), 
    `MethodSupport` INTEGER(11) COMMENT '1 offline
2) Online', 
    `MethodSupportNote` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `IsSOS` INTEGER(11) DEFAULT '0', 
    `TypeConsultation` TINYINT(4) COMMENT '1: T╞░ vß║Ñn | 2: ─Éiß╗üu trß╗ï | 3: Bß║úo h├ánh' DEFAULT '0', 
    PRIMARY KEY (`TicketSupportId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `idx_StaffId` ON `TicketSupport` (`CreatedBy`);

CREATE TABLE `NotificationComment` (
    `NotificationCommentId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `NotificationId` INTEGER(11), 
    `StaffId` INTEGER(11), 
    `Comment` TEXT COLLATE utf8mb4_unicode_ci, 
    `ParentNoticationCommentId` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `RemovedBy` INTEGER(11), 
    `RemovedDate` DATETIME, 
    PRIMARY KEY (`NotificationCommentId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `Plugin` (
    `PluginId` INTEGER(11) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `ExtensionId` INTEGER(11) UNSIGNED NOT NULL, 
    `AppId` INTEGER(11) UNSIGNED NOT NULL, 
    `Dir` VARCHAR(32) CHARACTER SET utf8 NOT NULL, 
    `Name` VARCHAR(128) CHARACTER SET utf8 NOT NULL, 
    `Scope` VARCHAR(32) CHARACTER SET utf8, 
    `Ordering` INTEGER(11) DEFAULT '0', 
    `Description` TEXT CHARACTER SET utf8, 
    `Config` TEXT CHARACTER SET utf8, 
    `State` INTEGER(1) DEFAULT '0', 
    PRIMARY KEY (`PluginId`), 
    CONSTRAINT `fk_Plugin_Extension` FOREIGN KEY(`ExtensionId`, `AppId`) REFERENCES `Extension` (`ExtensionId`, `AppId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_Plugin_Extension_idx` ON `Plugin` (`ExtensionId`, `AppId`);

CREATE TABLE `WorkShiftByWeekDay` (
    `WorkShiftId` INTEGER(10) UNSIGNED NOT NULL, 
    `WorkScheduleId` INTEGER(10) UNSIGNED NOT NULL, 
    `WeekDayId` INTEGER(10) UNSIGNED NOT NULL, 
    `BranchId` INTEGER(10) UNSIGNED NOT NULL, 
    `TotalBreakTimeInMinute` INTEGER(11) NOT NULL DEFAULT '0', 
    CONSTRAINT `fk_WorkShiftByWeekDay_WeekDay` FOREIGN KEY(`WeekDayId`) REFERENCES `WeekDay` (`WeekDayId`), 
    CONSTRAINT `fk_WorkShiftByWeekDay_WorkSchedule` FOREIGN KEY(`WorkScheduleId`) REFERENCES `WorkSchedule` (`WorkScheduleId`), 
    CONSTRAINT `fk_WorkShiftByWeekDay_WorkShift` FOREIGN KEY(`WorkShiftId`) REFERENCES `WorkShift` (`WorkShiftId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_WorkShiftByWeekDay_WorkShift_idx` ON `WorkShiftByWeekDay` (`WorkShiftId`);

CREATE INDEX `fk_WorkShiftByWeekDay_WorkSchedule_idx` ON `WorkShiftByWeekDay` (`WorkScheduleId`);

CREATE INDEX `fk_WorkShiftByWeekDay_WorkLocationId_idx` ON `WorkShiftByWeekDay` (`BranchId`);

CREATE INDEX `fk_WorkShiftByWeekDay_WeekDay_idx` ON `WorkShiftByWeekDay` (`WeekDayId`);

CREATE TABLE `StaffEmail` (
    `StaffEmailId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `Email` VARCHAR(64) CHARACTER SET utf8mb4 NOT NULL, 
    `IsWorkMail` INTEGER(1) UNSIGNED NOT NULL, 
    `IsBackupEmail` INTEGER(1) UNSIGNED DEFAULT '0', 
    `StaffId` INTEGER(10) UNSIGNED NOT NULL, 
    PRIMARY KEY (`StaffEmailId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_StaffEmail_Staff_idx` ON `StaffEmail` (`StaffId`);

CREATE TABLE `RoleMenuNavbar` (
    `RoleMenuNavbarId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `RoleId` INTEGER(11) NOT NULL, 
    `MenuNavbarId` INTEGER(11) NOT NULL, 
    `State` TINYINT(4) NOT NULL DEFAULT '1', 
    `CreatedBy` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`RoleMenuNavbarId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `StaffSalaryDetails` (
    `StaffSalaryDetailsId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `StaffId` INTEGER(11), 
    `StaffCode` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `FullName` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'hß╗ì t├¬n', 
    `Company` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'C├┤ng ty', 
    `WorkProfilePosition` VARCHAR(100) COLLATE utf8mb4_unicode_ci COMMENT 'Chß╗⌐c danh', 
    `ContractType` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'Loß║íi hß╗úp ─æß╗ông', 
    `Branch` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'Chi nh├ính', 
    `StartDate` DATETIME COMMENT 'ng├áy v├áo l├ám', 
    `Shift` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'ca l├ám viß╗çc', 
    `Level` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'bß║¡c', 
    `SalaryPerHour` DECIMAL(7, 2) COMMENT '─æ╞ín gi├í giß╗¥' DEFAULT '0.00', 
    `ActualHoursWorked` DECIMAL(5, 2) COMMENT 'sß╗æ giß╗¥ lv thß╗▒c tß║┐ HIS' DEFAULT '0.00', 
    `AnnualLeave` DECIMAL(5, 2) COMMENT 'nghß╗ë ph├⌐p' DEFAULT '0.00', 
    `PaidLeave` DECIMAL(5, 2) COMMENT 'nghß╗ë chß║┐ ─æß╗Ö' DEFAULT '0.00', 
    `PublicHolidaysLeave` DECIMAL(5, 2) COMMENT 'nghß╗ë lß╗à/tß║┐t' DEFAULT '0.00', 
    `TotalStandardHours` DECIMAL(5, 2) COMMENT 'tß╗òng c├┤ng t├¡nh l╞░╞íng' DEFAULT '0.00', 
    `StandardWage` DECIMAL(5, 2) COMMENT 'c├┤ng chuß║⌐n' DEFAULT '0.00', 
    `TotalIncomeWorkingDays` DECIMAL(13, 3) COMMENT 'Th├ánh tiß╗ün l╞░╞íng theo c├┤ng chuß║⌐n' DEFAULT '0.000', 
    `TaskBonus1` DECIMAL(15, 3) COMMENT 'Th╞░ß╗ƒng c├┤ng viß╗çc' DEFAULT '0.000', 
    `ServiceQualityBonus1` DECIMAL(13, 3) COMMENT 'Th╞░ß╗ƒng CLDV' DEFAULT '0.000', 
    `GeneralManagermentBonus1` DECIMAL(13, 3) COMMENT 'Th╞░ß╗ƒng quß║ún l├╜ chung' DEFAULT '0.000', 
    `EfficiencyManagementBonus` DECIMAL(13, 3) COMMENT 'Th╞░ß╗ƒng hiß╗çu quß║ú quß║ún l├╜' DEFAULT '0.000', 
    `EbitdaBonus` DECIMAL(13, 3) COMMENT 'Th╞░ß╗ƒng Ebitda' DEFAULT '0.000', 
    `OtherBonus` DECIMAL(13, 3) COMMENT 'th╞░ß╗ƒng kh├íc nß║┐u c├│' DEFAULT '0.000', 
    `SecurityBonus` DECIMAL(13, 3) COMMENT 'th╞░ß╗ƒng an ninh' DEFAULT '0.000', 
    `PerformanceBonus` DECIMAL(13, 3) COMMENT 'Th╞░ß╗ƒng n─âng suß║Ñt' DEFAULT '0.000', 
    `TaskBonus2` DECIMAL(15, 3) COMMENT 'Th╞░ß╗ƒng c├┤ng viß╗çc' DEFAULT '0.000', 
    `ServiceQualityBonus2` DECIMAL(13, 3) COMMENT 'Th╞░ß╗ƒng CLDV' DEFAULT '0.000', 
    `GeneralManagermentBonus2` DECIMAL(13, 3) COMMENT 'Th╞░ß╗ƒng quß║ún l├╜ chung' DEFAULT '0.000', 
    `KPIBonus` DECIMAL(15, 3) COMMENT 'Th╞░ß╗ƒng KPI' DEFAULT '0.000', 
    `VinmecBonus` DECIMAL(13, 3) COMMENT 'th╞░ß╗ƒng vinmec' DEFAULT '0.000', 
    `DoctorBonus` DECIMAL(15, 3) COMMENT 'Th╞░ß╗ƒng b├íc s─⌐' DEFAULT '0.000', 
    `OtherBonus3(vinmec)` DECIMAL(13, 3) COMMENT 'Th╞░ß╗ƒng kh├íc (vinmec)' DEFAULT '0.000', 
    `HolidayBonus` DECIMAL(13, 3) COMMENT 'th╞░ß╗ƒng lß╗à/tß║┐t' DEFAULT '0.000', 
    `TotalBonus` DECIMAL(12, 2) COMMENT 'tß╗òng th╞░ß╗ƒng' DEFAULT '0.00', 
    `AssistantManagerAndConcurrentBonus` DECIMAL(15, 3) COMMENT 'PC Phß╗Ñ t├í tr╞░ß╗ƒng v├á ki├¬m nhiß╗çm' DEFAULT '0.000', 
    `GuaranteedIncomeAllowance` DECIMAL(15, 3) COMMENT 'Phß╗Ñ cß║Ñp ─æß║úm bß║úo thu nhß║¡p' DEFAULT '0.000', 
    `ParkingTravelAllowance` DECIMAL(13, 3) COMMENT 'PC gß╗¡i xe/c├┤ng t├íc' DEFAULT '0.000', 
    `ProfessionalCertificateAllowance` DECIMAL(13, 3) COMMENT 'Phß╗Ñ cß║Ñp chß╗⌐ng chß╗ë h├ánh nghß╗ü' DEFAULT '0.000', 
    `OtherAllowances` DECIMAL(13, 3) COMMENT 'phß╗Ñ cß║Ñp kh├íc' DEFAULT '0.000', 
    `DentalTour` DECIMAL(15, 3) DEFAULT '0.000', 
    `WarehouseAllowance` DECIMAL(15, 3) COMMENT 'Phß╗Ñ cß║Ñp kho' DEFAULT '0.000', 
    `OtherTotalIncome` DECIMAL(15, 3) COMMENT 'Tß╗òng thu nhß║¡p kh├íc' DEFAULT '0.000', 
    `OtherAddition` DECIMAL(13, 3) COMMENT 'cß╗Öng kh├íc' DEFAULT '0.000', 
    `OtherDeductions` DECIMAL(13, 3) COMMENT 'trß╗½ kh├íc' DEFAULT '0.000', 
    `TotalIncomeBeforeTax` DECIMAL(13, 3) COMMENT 'tß╗òng thu nhß║¡p tr╞░ß╗¢c thuß║┐' DEFAULT '0.000', 
    `ParticipatingSalaryInSocialInsurance` DECIMAL(13, 3) COMMENT 'Mß╗⌐c l╞░╞íng tham gia BHXH' DEFAULT '0.000', 
    `PersonalHealthInsurance` DECIMAL(13, 3) COMMENT 'BHYT 1,5%' DEFAULT '0.000', 
    `PersonalSocialInsurance` DECIMAL(13, 3) COMMENT 'BHXH 8%' DEFAULT '0.000', 
    `PersonalUnemploymentInsurance` DECIMAL(13, 3) COMMENT 'BHTN 1%' DEFAULT '0.000', 
    `EmployeeSocialInsurance` DECIMAL(13, 3) COMMENT 'NLD ─æ├│ng BHXH 10,5%' DEFAULT '0.000', 
    `EmployeeUnionFee` DECIMAL(13, 3) COMMENT 'NL─É ─æ├│ng ph├¡ c├┤ng ─æo├án 1%' DEFAULT '0.000', 
    `CompanySocialInsurance` DECIMAL(13, 3) COMMENT 'BHXH 17%' DEFAULT '0.000', 
    `CompanyOccupaitionalAccidentOrDisease` DECIMAL(13, 3) COMMENT 'TNL─É / BNN 0.5%' DEFAULT '0.000', 
    `CompanyHealthInsurance` DECIMAL(13, 3) COMMENT 'BHYT 3%' DEFAULT '0.000', 
    `CompanyUnemploymentInsurance` DECIMAL(13, 3) COMMENT 'BHTN 1%' DEFAULT '0.000', 
    `EnterpriseSocialInsurance` DECIMAL(13, 3) COMMENT 'doanh nghiß╗çp ─æ├│ng BHXH 21.5%' DEFAULT '0.000', 
    `EnterpriseUnionFee` DECIMAL(13, 3) COMMENT 'Doanh nghiß╗çp ─æ├│ng c├┤ng ─æo├án 2%' DEFAULT '0.000', 
    `LunchOrUniformAllowanceNoTax` DECIMAL(13, 3) COMMENT 'Kh├┤ng t├¡nh thuß║┐ ( phß╗Ñ cß║Ñp c╞ím tr╞░a/ ─Éß╗ông phß╗Ñc)' DEFAULT '0.000', 
    `TotalTaxableIncome` DECIMAL(13, 3) COMMENT 'Tß╗òng thu nhß║¡p chß╗ïu thuß║┐' DEFAULT '0.000', 
    `TaxableIncomeObject` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT '─Éß╗æi t╞░ß╗úng t├¡nh thuß║┐ TNCN', 
    `Commitment` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'Cam kß║┐t', 
    `Dependents` INTEGER(11) COMMENT 'Sß╗æ ng╞░ß╗¥i phß╗Ñ thuß╗Öc' DEFAULT '0', 
    `TotalAssessableIncome` DECIMAL(13, 3) COMMENT 'Tß╗òng thu nhß║¡p t├¡nh thuß║┐' DEFAULT '0.000', 
    `PersonalIncomeTaxCollection` DECIMAL(13, 3) COMMENT 'Thu tiß╗ün thuß║┐ TNCN' DEFAULT '0.000', 
    `ActualPayment` DECIMAL(12, 2) COMMENT 'Thß╗▒c l├únh' DEFAULT '0.00', 
    `CompanyPaysSocialInsurance` DECIMAL(13, 3) COMMENT 'Cty ─æ├│ng hß╗ì BHXH' DEFAULT '0.000', 
    `WithholdSocialInsurance` DECIMAL(13, 3) COMMENT 'thu hß╗Ö tiß╗ün BHXH 21.5%' DEFAULT '0.000', 
    `PaidHolidayBonus` DECIMAL(11, 2) COMMENT '─É├ú thanh to├ín th╞░ß╗ƒng Lß╗à/tß║┐t\\n' DEFAULT '0.00', 
    `PaidOthers` DECIMAL(11, 2) COMMENT '─É├ú thanh to├ín kh├íc\\n' DEFAULT '0.00', 
    `BankTransfer` DECIMAL(12, 2) COMMENT 'chuyß╗ân khoß║ún' DEFAULT '0.00', 
    `NoteOtherAdditions` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'Ghi ch├║ cß╗Öt cß╗Öng kh├íc\\n', 
    `PayPeriod` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'kß╗│ l╞░╞íng', 
    `Template` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT '1-BO\\\\n2-Phu ta\\\\n3-Bac Si\\\\n4-Bao ve', 
    PRIMARY KEY (`StaffSalaryDetailsId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `Department` (
    `DepartmentId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `CompanyId` INTEGER(10) UNSIGNED NOT NULL, 
    `NameVi` VARCHAR(128) CHARACTER SET utf8mb4 NOT NULL, 
    `NameEn` VARCHAR(128) CHARACTER SET utf8mb4, 
    `State` INTEGER(1) UNSIGNED NOT NULL COMMENT '0  - kh├┤ng ho?t ??ng
1 - ho?t ??ng' DEFAULT '1', 
    PRIMARY KEY (`DepartmentId`), 
    CONSTRAINT fk_department_company FOREIGN KEY(`CompanyId`) REFERENCES `Company` (`CompanyId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_Department_Company_idx` ON `Department` (`CompanyId`);

CREATE TABLE `RegistedMobileDevice` (
    `RegistedMobileDeviceId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `MobileDeviceInfo` VARCHAR(188) CHARACTER SET utf8mb4, 
    `RegistedAt` INTEGER(10) UNSIGNED NOT NULL COMMENT 'th?i ?i?m ??ng k├¡ thi?t b? v?i h? th?ng', 
    `RegistedBy` INTEGER(10) UNSIGNED NOT NULL COMMENT 'ng??i th?c hi?n ??ng k├¡ mobile v?i h? th?ng', 
    `StaffId` INTEGER(10) UNSIGNED NOT NULL, 
    `State` INTEGER(1) UNSIGNED NOT NULL COMMENT 'tr?ng th├íi c?a device:
-1: deactivated
0: pending
1: active' DEFAULT '0', 
    `ApprovedAt` INTEGER(10) UNSIGNED DEFAULT '0', 
    `ApprovedBy` INTEGER(10) UNSIGNED DEFAULT '0', 
    PRIMARY KEY (`RegistedMobileDeviceId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_RegistedMobileDevice_Staff_idx` ON `RegistedMobileDevice` (`StaffId`);

CREATE INDEX `fk_RegistedMobileDevice_RegistedBy_idx` ON `RegistedMobileDevice` (`RegistedBy`);

CREATE TABLE `StaffHistory` (
    `StaffId` INTEGER(10) UNSIGNED NOT NULL, 
    `StaffCode` VARCHAR(16) CHARACTER SET utf8mb4 NOT NULL, 
    `IdNumber` VARCHAR(16) CHARACTER SET utf8mb4, 
    `IdNumberIssuedAt` DATE, 
    `IdNumberIssuedBy` INTEGER(11), 
    `PassportNumber` VARCHAR(16) CHARACTER SET utf8mb4, 
    `NationalInsuranceNumber` VARCHAR(16) CHARACTER SET utf8mb4, 
    `TaxNumber` VARCHAR(16) CHARACTER SET utf8mb4, 
    `UserId` INTEGER(10) UNSIGNED, 
    `FullName` VARCHAR(64) CHARACTER SET utf8mb4, 
    `FullNameNoSign` VARCHAR(64) CHARACTER SET utf8mb4, 
    `LastName` VARCHAR(16) CHARACTER SET utf8mb4, 
    `LastNameNoSign` VARCHAR(16) CHARACTER SET utf8mb4, 
    `DateOfBirth` DATE, 
    `Photo` VARCHAR(128) CHARACTER SET utf8mb4, 
    `PrimaryEmail` VARCHAR(255) CHARACTER SET utf8mb4, 
    `CreatedAt` INTEGER(10) UNSIGNED NOT NULL, 
    `CreatedBy` INTEGER(10) UNSIGNED NOT NULL, 
    `State` INTEGER(1) NOT NULL DEFAULT '1', 
    `GenderId` INTEGER(10) UNSIGNED NOT NULL, 
    `DegreeId` INTEGER(10) UNSIGNED, 
    `UpdatedAt` INTEGER(10) UNSIGNED, 
    `UpdatedBy` INTEGER(10) UNSIGNED, 
    `Nationality` INTEGER(10) UNSIGNED, 
    `FlushedAt` INTEGER(11) UNSIGNED NOT NULL
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `WorkProfilePositionRole` (
    `Id` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `WorkProfilePositionId` INTEGER(11), 
    `RoleId` INTEGER(11), 
    `State` INTEGER(11), 
    `CreatedBy` INTEGER(11), 
    `CreatedDate` DATETIME, 
    PRIMARY KEY (`Id`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `StaffAnnualLeave` (
    `YearNumber` INTEGER(11) NOT NULL, 
    `StaffId` INTEGER(11) NOT NULL, 
    `Total` DOUBLE NOT NULL DEFAULT '0', 
    `Pending` DOUBLE NOT NULL DEFAULT '0', 
    `Available` DOUBLE NOT NULL DEFAULT '0', 
    `AnnualYear` DECIMAL(8, 2), 
    `LockedAnnualYear` DECIMAL(8, 2), 
    `ByRank` DECIMAL(8, 2), 
    `LockedByRank` DECIMAL(8, 2), 
    `ToSeniority` DECIMAL(8, 2), 
    `Training` DECIMAL(8, 2), 
    `IsPaidTraining` TINYINT(4), 
    `ApprovedNumber` DOUBLE, 
    `WaitingNumberInMonth` DOUBLE, 
    `CreatedBy` INTEGER(11), 
    `CreatedDate` DATETIME, 
    `UpdatedBy` INTEGER(11), 
    `UpdatedDate` DATETIME, 
    PRIMARY KEY (`YearNumber`, `StaffId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `TicketSupportCustomerCashback` (
    `TicketSupportCustomerCashbackId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `TicketSupportId` INTEGER(11) NOT NULL, 
    `CustomerId` INTEGER(11), 
    `Amount` DECIMAL(18, 2), 
    `RelatedStaffId` INTEGER(11), 
    `RelatedBranchId` INTEGER(11), 
    `CreatedBy` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`TicketSupportCustomerCashbackId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `idx_TicketId` ON `TicketSupportCustomerCashback` (`TicketSupportId`);

CREATE INDEX `idx_StaffId` ON `TicketSupportCustomerCashback` (`RelatedStaffId`);

CREATE INDEX `idx_CustomerId` ON `TicketSupportCustomerCashback` (`CustomerId`);

CREATE TABLE `DayInfo` (
    `Id` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `Date` DATE, 
    `DayOfWeek` VARCHAR(10) COLLATE utf8mb4_unicode_ci, 
    `IsWeekend` TINYINT(1), 
    `IsHoliday` TINYINT(1), 
    `HolidayName` VARCHAR(100) COLLATE utf8mb4_unicode_ci, 
    PRIMARY KEY (`Id`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX idx_dayinfo_isweekend ON `DayInfo` (`IsWeekend`);

CREATE INDEX idx_dayinfo_date ON `DayInfo` (`Date`);

CREATE TABLE `WorkProfilePositionSalaryAmount` (
    `Id` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `PositionId` TINYINT(4) COMMENT '1: T╞░ vß║Ñn vi├¬n, 2: Phß╗Ñ t├í, 3: Quß║ún l├╜ ph├▓ng kh├ím', 
    `WorkProfilePositionId` INTEGER(11), 
    `WorkProfilePositionName` VARCHAR(1000) CHARACTER SET utf8mb4, 
    `StartDate` DATE, 
    `EndDate` DATE, 
    `State` TINYINT(4) DEFAULT '1', 
    `SalaryTypeId` TINYINT(4) COMMENT '1: giß╗¥, 2: ng├áy, 3: th├íng', 
    `SalaryAmount` DECIMAL(18, 5), 
    `CreatedBy` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `UpdatedBy` INTEGER(11), 
    `UpdatedDate` DATETIME, 
    PRIMARY KEY (`Id`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `idx_WorkProfilePositionSalaryAmount_WorkProfilePositionId` ON `WorkProfilePositionSalaryAmount` (`WorkProfilePositionId`);

CREATE TABLE `Menu` (
    `MenuId` INTEGER(11) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `SysLanguageId` INTEGER(11) UNSIGNED NOT NULL, 
    `AppId` INTEGER(11) UNSIGNED NOT NULL, 
    `Name` VARCHAR(128) CHARACTER SET utf8 NOT NULL, 
    `Description` TEXT CHARACTER SET utf8, 
    `CreatedBy` INTEGER(11) UNSIGNED NOT NULL, 
    `CreatedAt` INTEGER(11) UNSIGNED, 
    `CheckedOutBy` INTEGER(11) UNSIGNED, 
    `CheckedOutAt` INTEGER(11) UNSIGNED DEFAULT '0', 
    `State` INTEGER(1) DEFAULT '1', 
    PRIMARY KEY (`MenuId`), 
    CONSTRAINT `fk_Menu_AppId` FOREIGN KEY(`AppId`) REFERENCES `App` (`AppId`), 
    CONSTRAINT `fk_Menu_CreatedBy` FOREIGN KEY(`CreatedBy`) REFERENCES `User` (`UserId`), 
    CONSTRAINT `fk_Menu_SysLanguage` FOREIGN KEY(`SysLanguageId`) REFERENCES `SysLanguage` (`SysLanguageId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_Menu_SysLanguage_idx` ON `Menu` (`SysLanguageId`);

CREATE INDEX `fk_Menu_CreatedBy_idx` ON `Menu` (`CreatedBy`);

CREATE INDEX `fk_Menu_App_idx` ON `Menu` (`AppId`);

CREATE TABLE `IncludeHolidayDate` (
    `WorkScheduleId` INTEGER(10) UNSIGNED NOT NULL, 
    `HolidayDate` DATE NOT NULL, 
    PRIMARY KEY (`WorkScheduleId`, `HolidayDate`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `VnWardUpdate` (
    `VnWardId` INTEGER(10) UNSIGNED NOT NULL, 
    `VnDistrictId` INTEGER(10) UNSIGNED NOT NULL, 
    `WardCode` VARCHAR(8), 
    `WardPostalCode` VARCHAR(8), 
    `NameVi` VARCHAR(64) NOT NULL, 
    `NameEn` VARCHAR(64), 
    `LabelVi` VARCHAR(32) NOT NULL COMMENT 'Ph??ng
X├ú
Th? tr?n', 
    `LabelEn` VARCHAR(32) COMMENT 'Commune
Ward
Township', 
    `Ordering` INTEGER(10) UNSIGNED, 
    PRIMARY KEY (`VnWardId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB;

CREATE INDEX `fk_VnWard_VnDistrict_idx` ON `VnWardUpdate` (`VnDistrictId`);

CREATE TABLE `StaffProbationaryEvaluation` (
    `StaffProbationaryEvaluationId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `StaffId` INTEGER(11), 
    `Content` VARCHAR(8000) COLLATE utf8mb4_unicode_ci, 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    PRIMARY KEY (`StaffProbationaryEvaluationId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `BankBranch` (
    `BankBranchId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `BankId` INTEGER(10) UNSIGNED NOT NULL, 
    `NameVi` VARCHAR(64) CHARACTER SET utf8mb4, 
    `NameEn` VARCHAR(64) CHARACTER SET utf8mb4, 
    `State` INTEGER(11), 
    `Address` VARCHAR(45) CHARACTER SET utf8mb4, 
    PRIMARY KEY (`BankBranchId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_BankBranch_Bank_idx` ON `BankBranch` (`BankId`);

CREATE TABLE `Role` (
    `RoleId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `RoleName` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `State` TINYINT(4) DEFAULT '1', 
    `CreatedBy` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `UpdatedBy` INTEGER(11), 
    `UpdatedDate` DATETIME, 
    PRIMARY KEY (`RoleId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `NotificationTemplate` (
    `NotificationTemplateId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `NotificationTemplateCode` VARCHAR(1024) COLLATE utf8mb4_unicode_ci, 
    `Content` TEXT COLLATE utf8mb4_unicode_ci, 
    `IsDeleted` TINYINT(4), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    `Priority` INTEGER(11) DEFAULT '0', 
    `IsIncludeSubNode` TINYINT(4) DEFAULT '0', 
    PRIMARY KEY (`NotificationTemplateId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `CronJobHistory` (
    `Id` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `JobName` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `Message` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`Id`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `ComplaintChannel` (
    `ComplaintChannelId` INTEGER(10) UNSIGNED NOT NULL, 
    `Name` VARCHAR(32) COLLATE utf8mb4_unicode_ci NOT NULL, 
    `State` INTEGER(1) UNSIGNED NOT NULL DEFAULT '1'
)COMMENT='callcenter, app, web, reception...' DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `MenuNavbarPermission` (
    `MenuNavbarId` INTEGER(11) NOT NULL, 
    `PermissionCode` VARCHAR(128) COLLATE utf8mb4_unicode_ci NOT NULL, 
    PRIMARY KEY (`MenuNavbarId`, `PermissionCode`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `BranchExecutiveTarget` (
    `BranchExecutiveTargetId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `Revenue` DECIMAL(20, 2) UNSIGNED NOT NULL COMMENT 'target vß╗ü doanh thu cß╗ºa chi nh├ính', 
    `Appointment` INTEGER(10) UNSIGNED COMMENT 'target vß╗ü sß╗æ lß╗ïch hß║╣n cß╗ºa chi nh├ính', 
    `Checkin` INTEGER(10) UNSIGNED, 
    `Treatment` INTEGER(10) UNSIGNED, 
    `FromDate` DATE NOT NULL, 
    `ToDate` DATE, 
    `BranchId` INTEGER(10) UNSIGNED NOT NULL, 
    `CompanyId` INTEGER(11) NOT NULL, 
    PRIMARY KEY (`BranchExecutiveTargetId`)
)COMMENT='bß║úng l╞░u target hoß║ít ─æß╗Öng cß╗ºa c├íc chi nh├ính' DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_BranchExecutiveTarget_Branch_idx` ON `BranchExecutiveTarget` (`BranchId`);

CREATE TABLE `InsuranceHospital` (
    `InsuranceHospitalId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `InsuranceHospitalName` VARCHAR(500) CHARACTER SET utf8mb4 NOT NULL, 
    `Ordering` INTEGER(10) UNSIGNED NOT NULL DEFAULT '1', 
    PRIMARY KEY (`InsuranceHospitalId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `ScoreCampaignType` (
    `ScoreCampaignTypeId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `Name` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    PRIMARY KEY (`ScoreCampaignTypeId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `StaffPasswordTracking` (
    `StaffPasswordTrackingId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `StaffId` INTEGER(11), 
    `ChangedType` TINYINT(2) COMMENT '1: T? ??i m?t kh?u, 2: Nh├ón s? ??i m?t kh?u, 3: Qu├¬n m?t kh?u', 
    `ChangedDate` DATETIME, 
    `ChangedBy` INTEGER(11), 
    PRIMARY KEY (`StaffPasswordTrackingId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `IX_StaffId` ON `StaffPasswordTracking` (`StaffId`);

CREATE TABLE `Person` (
    `PersonId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `FullName` VARCHAR(300) CHARACTER SET utf8mb4 NOT NULL, 
    `Gender` TINYINT(1), 
    `Birthday` DATE, 
    `Address` VARCHAR(1000) CHARACTER SET utf8mb4, 
    `PhoneNumber` VARCHAR(15) CHARACTER SET utf8mb4, 
    `Email` VARCHAR(255) CHARACTER SET utf8mb4, 
    `Note` TEXT CHARACTER SET utf8mb4, 
    `CountryId` INTEGER(10) UNSIGNED, 
    `ProvinceId` INTEGER(10) UNSIGNED, 
    `DistrictId` INTEGER(10) UNSIGNED, 
    `WardId` INTEGER(10) UNSIGNED, 
    `FromChannelId` TINYINT(2), 
    `Status` TINYINT(2) COMMENT '1 ?ng Vi├¬n\\n10 ?├ú l├¬n l?ch phong v?n\\n20) Pass Ph?ng v?n\\n30) R?t ph?ng v?n\\n40) ?├ú nh?n Offer\\n50) Nh├ón Vi├¬n\\n60) Ngh? vi?c' DEFAULT '0', 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(10) UNSIGNED, 
    `UpdatedDate` DATETIME, 
    `UpdatedBy` INTEGER(10) UNSIGNED, 
    PRIMARY KEY (`PersonId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `StaffAnnualLeaveTransaction` (
    `Id` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `StaffId` INTEGER(11), 
    `AbsenceTypeId` INTEGER(11), 
    `AbsenceRequestId` INTEGER(11), 
    `Quantity` DOUBLE, 
    `TransactionType` VARCHAR(20) COLLATE utf8mb4_unicode_ci COMMENT '100 import
101 Deposit Monthly', 
    `TransactionDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `Note` VARCHAR(128) COLLATE utf8mb4_unicode_ci, 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    PRIMARY KEY (`Id`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `CandidateTracking` (
    `CandidateTrackingId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `CandidateId` INTEGER(11), 
    `TrackingTypeId` TINYINT(4) COMMENT '1)Pickup\\n2)Exchange Content\\n3)Change Interview4)UpdateCV', 
    `JsonDetail` VARCHAR(8000) COLLATE utf8mb4_unicode_ci, 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    PRIMARY KEY (`CandidateTrackingId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `InfrequentExcludeWorkShift` (
    `InfrequentExcludeWorkShiftId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `WorkScheduleId` INTEGER(10) UNSIGNED NOT NULL, 
    `Date` DATE NOT NULL, 
    `WorkShiftId` INTEGER(10) UNSIGNED NOT NULL, 
    `ExcludedAt` INTEGER(11) NOT NULL, 
    `ExcludedBy` INTEGER(10) UNSIGNED NOT NULL, 
    PRIMARY KEY (`InfrequentExcludeWorkShiftId`), 
    CONSTRAINT `fk_InfrequentExcludeWorkShift_ExcludedBy` FOREIGN KEY(`ExcludedBy`) REFERENCES `User` (`UserId`), 
    CONSTRAINT `fk_InfrequentExcludeWorkShift_WorkSchedule` FOREIGN KEY(`WorkScheduleId`) REFERENCES `WorkSchedule` (`WorkScheduleId`), 
    CONSTRAINT `fk_InfrequentExcludeWorkShift_WorkShift` FOREIGN KEY(`WorkShiftId`) REFERENCES `WorkShift` (`WorkShiftId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_InfrequentExcludeWorkShift_WorkShift_idx` ON `InfrequentExcludeWorkShift` (`WorkShiftId`);

CREATE INDEX `fk_InfrequentExcludeWorkShift_WorkSchedule_idx` ON `InfrequentExcludeWorkShift` (`WorkScheduleId`);

CREATE INDEX `fk_InfrequentExcludeWorkShift_ExcludedBy_idx` ON `InfrequentExcludeWorkShift` (`ExcludedBy`);

CREATE INDEX `IX_InfrequentExcludeWorkShift_Date` ON `InfrequentExcludeWorkShift` (`Date`);

CREATE TABLE `ASalaryPTa` (
    `Stt` INTEGER(11) NOT NULL, 
    `M├ú NV` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `FullName` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `C├┤ng ty` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `PositionProfile` VARCHAR(100) COLLATE utf8mb4_unicode_ci, 
    `Lo?i H├É` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Chi nh├ính` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Ca l├ám vi?c` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Bac` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Don Gia Gio` INTEGER(11), 
    `So Gio lam viec HIS` INTEGER(11), 
    `Ngh? ph├⌐p` INTEGER(11), 
    `Ngh? b├╣` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Ngh? ch? d? c├│ luong` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Ngh? l?` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `T?ng c├┤ng t├¡nh luong` INTEGER(11), 
    `C├┤ng chu?n` INTEGER(11), 
    `Th├ánh ti?n luong theo t?ng c├┤ng` INTEGER(11), 
    `├É?nh m?c PC com` INTEGER(11), 
    `Th├ánh ti?n PC com theo c├┤ng` INTEGER(11), 
    `├É?nh m?c thu nh?p c? d?nh (d├ú bao g?m PC com)` INTEGER(11), 
    `Th├ánh ti?n thu nh?p c? d?nh theo c├┤ng chu?n (d├ú bao g?m PC c` INTEGER(11), 
    `Thu?ng nang su?t` INTEGER(11), 
    `Thu?ng c├┤ng vi?c` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Thu?ng ch?t lu?ng d?ch v?` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Thu?ng qu?n l├╜, gi├ím s├ít` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Thu?ng ph├▓ng kh├ím d?t KPI Thu Ti?n` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Thu?ng L?/T?t` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `T?ng thu?ng` INTEGER(11), 
    `PC Ph? t├í tru?ng & Ki├¬m nhi?m` INTEGER(11), 
    `Ph? c?p d?m b?o thu nh?p` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `PC G?i xe/C├┤ng t├íc` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Ph? c?p ch?ng ch? h├ánh ngh?` INTEGER(11), 
    `Ph? c?p kh├íc` INTEGER(11), 
    `Dental tour` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Ph? c?p kho` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `T?ng thu nh?p kh├íc` INTEGER(11), 
    `T?ng thu nh?p tru?c thu?` INTEGER(11), 
    `M?c luong tham gia BHXH` INTEGER(11), 
    `BHYT (1,5%)` INTEGER(11), 
    `BHXH (8%)` INTEGER(11), 
    `BHTN (1%)` INTEGER(11), 
    `NL├É d├│ng BHXH (10.5%)` INTEGER(11), 
    `NL├É d├│ng ph├¡ C├┤ng do├án (1%)` INTEGER(11), 
    `BHXH (17%` INTEGER(11), 
    `TNL├É / BNN (0.5%)` INTEGER(11), 
    `BHYT (3%)` INTEGER(11), 
    `BHTN 1%` INTEGER(11), 
    `Doanh nghi?p d├│ng BHXH 21.5%` INTEGER(11), 
    `Doanh nghi?p d├│ng C├┤ng do├án 2%` INTEGER(11), 
    `Kh├┤ng t├¡nh thu? (Ph? c?p com trua/ ├É?ng ph?c)` INTEGER(11), 
    `T?NG THU NH?P CH?U THU?` INTEGER(11), 
    `├É?i tu?ng t├¡nh Thu? TNCN` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Cam k?t` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `S? ngu?i ph? thu?c` INTEGER(11), 
    `T?NG THU NH?P T├ìNH THU?` INTEGER(11), 
    `Thu Ti?n thu? TNCN` INTEGER(11), 
    `Th?c l├únh` INTEGER(11), 
    `Cty d├│ng h? BHXH` INTEGER(11), 
    `Thu h? ti?n BHXH (21.5%` INTEGER(11), 
    `Chuy?n kho?n` INTEGER(11), 
    `H? & t├¬n` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `S? t├ái kho?n` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Ng├ón h├áng` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Mail` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Chuy?n kho?n1` INTEGER(11), 
    `B? sung` INTEGER(11), 
    `L├╜ do` VARCHAR(100) COLLATE utf8mb4_unicode_ci, 
    `Ghi ch├║ ng├áy thanh to├ín` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    PRIMARY KEY (`Stt`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `BranchServiceQuality` (
    `Year` INTEGER(11) NOT NULL, 
    `Month` INTEGER(11) NOT NULL, 
    `AVGStar` FLOAT, 
    `QuantityRating` INTEGER(11), 
    `ScoreCardMark` FLOAT, 
    `CRVAssistant` FLOAT, 
    `CRVManager` FLOAT, 
    `CRVCoordinatingDoctor` FLOAT, 
    `UpdatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`Year`, `Month`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `StaffSelfAssessment` (
    `StaffSelfAssessmentId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `PeriodTime` DATE COMMENT '2023', 
    `StaffId` INTEGER(11), 
    `SelfAssessmentContent` TEXT COLLATE utf8mb4_unicode_ci COMMENT 'DataJon:"{CreatedBy:''1'',CreatedDate=''2024-01-12 23:58:14'', ''Content'':''''}', 
    `ManagerAssessmentContent` TEXT COLLATE utf8mb4_unicode_ci COMMENT 'DataJon:"{CreatedBy:''1'',CreatedDate=''2024-01-12 23:58:14'', ''Content'':''''}', 
    `DoctorAssistantContent` TEXT COLLATE utf8mb4_unicode_ci COMMENT 'DataJon:"{CreatedBy:''1'',CreatedDate=''2024-01-12 23:58:14'', ''Content'':''''}', 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    `UpdatedDate` DATETIME, 
    `UpdatedBy` INTEGER(11), 
    PRIMARY KEY (`StaffSelfAssessmentId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `Candidate` (
    `CandidateId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `PersonId` INTEGER(10) UNSIGNED, 
    `PositionId` INTEGER(10) UNSIGNED, 
    `PositionText` VARCHAR(300) CHARACTER SET utf8mb4, 
    `Location` VARCHAR(300) CHARACTER SET utf8mb4, 
    `ApplyDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CDNCV` VARCHAR(1024) CHARACTER SET utf8mb4, 
    `RowInterview` INTEGER(11), 
    `Status` TINYINT(2) UNSIGNED COMMENT '1: ?ng vi├¬n m?i, 2: ?ng vi├¬n kh├┤ng ??t, 3: ?├ú c├│ l?ch ph?ng v?n, 4: ?├ú c├│ offer, 5: ?├ú l├á nh├ón vi├¬n, 6: ?├ú ngh? vi?c' DEFAULT '1', 
    `CreatedBy` INTEGER(10) UNSIGNED, 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `UpdatedBy` INTEGER(10) UNSIGNED, 
    `UpdatedDate` DATETIME, 
    `DiscussionFromHR` TEXT COLLATE utf8mb4_unicode_ci, 
    `DiscussionFromCandidate` TEXT COLLATE utf8mb4_unicode_ci, 
    `EvaluationFromHR` TEXT COLLATE utf8mb4_unicode_ci, 
    `LastFolowByStaffId` INTEGER(11), 
    `LastFolowDate` DATETIME, 
    `StatusNote` VARCHAR(1000) COLLATE utf8mb4_unicode_ci, 
    PRIMARY KEY (`CandidateId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `IX_PersonId` ON `Candidate` (`PersonId`);

CREATE TABLE `WorkContractAnnexHistory` (
    `WorkContractAnnexHistoryId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `WorkContractAnnexId` INTEGER(10) UNSIGNED NOT NULL, 
    `WorkContractAnnexCode` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    `WorkContractAnnexType` VARCHAR(128) COLLATE utf8mb4_unicode_ci, 
    `WorkContractAnnexBonus` DECIMAL(18, 2) UNSIGNED NOT NULL DEFAULT '0.00', 
    `AttachFile` VARCHAR(128) COLLATE utf8mb4_unicode_ci, 
    `FromDate` DATE NOT NULL, 
    `ToDate` DATE, 
    `Note` VARCHAR(1000) COLLATE utf8mb4_unicode_ci, 
    `WorkContractHistoryId` INTEGER(11) NOT NULL, 
    `CreatedDate` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`WorkContractAnnexHistoryId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `WorkProfileHistory` (
    `WorkProfileId` INTEGER(10) UNSIGNED NOT NULL, 
    `StaffId` INTEGER(10) UNSIGNED NOT NULL, 
    `FromDate` DATE NOT NULL, 
    `ToDate` DATE, 
    `IsCurrentProfile` INTEGER(1) UNSIGNED NOT NULL DEFAULT '0', 
    `WorkPositionId` INTEGER(10) UNSIGNED NOT NULL, 
    `CompanyId` INTEGER(10) UNSIGNED NOT NULL, 
    `DepartmentId` INTEGER(10) UNSIGNED, 
    `TeamId` INTEGER(10) UNSIGNED, 
    `WorkContractId` INTEGER(10) UNSIGNED NOT NULL, 
    `StaffLevelId` INTEGER(10) UNSIGNED, 
    `BranchId` INTEGER(10) UNSIGNED, 
    `DegreeId` INTEGER(10) UNSIGNED NOT NULL, 
    `UpdatedAt` INTEGER(10) UNSIGNED, 
    `UpdatedBy` INTEGER(10) UNSIGNED, 
    `BaseSalary` DECIMAL(20, 2) UNSIGNED NOT NULL, 
    `ExtraMonthlyIncome` DECIMAL(20, 2) NOT NULL, 
    `BankId` INTEGER(10) UNSIGNED, 
    `BankBranchId` INTEGER(10) UNSIGNED, 
    `BankAccountName` VARCHAR(64) CHARACTER SET utf8mb4, 
    `BankAccountId` VARCHAR(16) CHARACTER SET utf8mb4, 
    `IsFullTime` INTEGER(1), 
    `CreatedBy` INTEGER(11), 
    `CreatedAt` INTEGER(11), 
    `FlushedAt` INTEGER(11) UNSIGNED NOT NULL, 
    `ActionType` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    `UpdatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `NotificationTemplateConfig` (
    `NotificationTemplateConfigId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `NotificationTemplateId` INTEGER(11) NOT NULL, 
    `ImpactType` INTEGER(11) COMMENT '1 Receiver
2 ApprovedBy', 
    `ObjectSource` INTEGER(11), 
    `ObjectId` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    `IsIncludeSubNode` TINYINT(4) DEFAULT '0', 
    PRIMARY KEY (`NotificationTemplateConfigId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `Subsidize` (
    `SubsidizeId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `Name` VARCHAR(64) COLLATE utf8mb4_unicode_ci NOT NULL, 
    `DefaultAmount` DECIMAL(12, 2) NOT NULL, 
    `Ordering` INTEGER(10) UNSIGNED NOT NULL, 
    `State` INTEGER(1) UNSIGNED NOT NULL DEFAULT '1', 
    PRIMARY KEY (`SubsidizeId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `Org20230228` (
    `OrgId` INTEGER(10) UNSIGNED NOT NULL DEFAULT '0', 
    `OrgCode` VARCHAR(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL, 
    `OrgName` VARCHAR(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL, 
    `CompanyId` INTEGER(10) UNSIGNED NOT NULL, 
    `ParentId` INTEGER(11) NOT NULL DEFAULT '0', 
    `DefaultBranchId` INTEGER(10) UNSIGNED, 
    `NumAnnualLeaveTraining` INTEGER(5) NOT NULL, 
    `IsViewAllBranch` INTEGER(1) NOT NULL, 
    `IsTimekeeping` INTEGER(1) NOT NULL, 
    `IsActive` INTEGER(1) NOT NULL, 
    `PosLeft` INTEGER(5) NOT NULL DEFAULT '0', 
    `PosRight` INTEGER(5) NOT NULL DEFAULT '0', 
    `RoleCode` VARCHAR(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci, 
    `CreatedDate` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    `CreatedStaffId` INTEGER(11) UNSIGNED NOT NULL DEFAULT '0', 
    `UpdatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `UpdatedStaffId` INTEGER(11) UNSIGNED DEFAULT '0', 
    `ParentDeleteOrgId` INTEGER(11), 
    `Level` INTEGER(11)
)DEFAULT CHARSET=latin1 ENGINE=InnoDB;

CREATE TABLE `Session` (
    `SessionId` INTEGER(11) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `AppId` INTEGER(11) UNSIGNED NOT NULL, 
    `UserId` INTEGER(11) UNSIGNED NOT NULL, 
    `MenuItemId` INTEGER(11) UNSIGNED NOT NULL, 
    `Uri` VARCHAR(196) CHARACTER SET utf8, 
    `AuthenMethod` VARCHAR(32) CHARACTER SET utf8, 
    `VisitedAt` INTEGER(11) DEFAULT '0', 
    `Config` TEXT CHARACTER SET utf8, 
    `Ip` VARCHAR(32) CHARACTER SET utf8 NOT NULL, 
    `Token` VARCHAR(64) CHARACTER SET utf8 NOT NULL, 
    `ClientInfo` TEXT CHARACTER SET utf8 COMMENT 'browser infomation', 
    `LogedOutAt` INTEGER(11) DEFAULT '0', 
    PRIMARY KEY (`SessionId`), 
    CONSTRAINT `fk_Session_App` FOREIGN KEY(`AppId`) REFERENCES `App` (`AppId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_Session_App_idx` ON `Session` (`AppId`);

CREATE TABLE `ByMonth` (
    `WorkScheduleId` INTEGER(10) UNSIGNED NOT NULL, 
    `MonthId` INTEGER(10) UNSIGNED NOT NULL
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_ByMonth_WorkSchedule_idx` ON `ByMonth` (`WorkScheduleId`);

CREATE INDEX `fk_ByMonth_Month_idx` ON `ByMonth` (`MonthId`);

CREATE TABLE `WorkPriorityLevel` (
    `WorkPriorityLevelId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `Name` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    `ShortName` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    `State` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`WorkPriorityLevelId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `ActivityLog` (
    `ActivityLogId` BIGINT(15) NOT NULL AUTO_INCREMENT, 
    `StaffId` INTEGER(11), 
    `ActionType` INTEGER(11) COMMENT '1) LockProfile
2) UnlockProfile
', 
    `Data` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`ActivityLogId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `TaskTagTask` (
    `TaskId` INTEGER(10) UNSIGNED NOT NULL, 
    `Tag` VARCHAR(32) COLLATE utf8mb4_unicode_ci NOT NULL, 
    CONSTRAINT `fk_TaskTagTask_Task` FOREIGN KEY(`TaskId`) REFERENCES `Task` (`TaskId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_TaskTagTask_Task_idx` ON `TaskTagTask` (`TaskId`);

CREATE TABLE `RewardDiscipline` (
    `RewardDisciplineId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `StaffId` INTEGER(11), 
    `Type` INTEGER(11) COMMENT '1:Reward
2:Discipline', 
    `Content` VARCHAR(8000) COLLATE utf8mb4_unicode_ci, 
    `Method` VARCHAR(4000) COLLATE utf8mb4_unicode_ci, 
    `RecordedDate` DATE, 
    `ApprovedByStaff` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    `Status` INTEGER(11) DEFAULT '0', 
    `UpadtedDate` DATETIME, 
    PRIMARY KEY (`RewardDisciplineId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `ABO21` (
    `Stt` INTEGER(11), 
    `M├ú NV` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Hß╗ì t├¬n` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `C├┤ng ty` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Chß╗⌐c danh` VARCHAR(100) COLLATE utf8mb4_unicode_ci, 
    `Loß║íi H─É` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Chi nh├ính` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Ng├áy v├áo l├ám` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Ca l├ám viß╗çc` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `L╞░╞íng c╞í bß║ún` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Th╞░ß╗ƒng ├¥ thß╗⌐c v├á Tu├ón thß╗º/Th╞░ß╗ƒng Hiß╗çß╗Ñ quß║ú hoß║ít ─æß╗Öng` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Tß╗òng cß╗Öng` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Ghi ch├║ k chß║Ñm c├┤ng` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Sß╗æ giß╗¥ lv thß╗▒c tß║┐ (HIS)` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Nghß╗ë ph├⌐p` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Nghß╗ë chß║┐ ─æß╗Ö` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Nghß╗ë lß╗à/tß║┐t` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Tß╗òng c├┤ng t├¡nh l╞░╞íng` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `C├┤ng chuß║⌐n` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `L╞░╞íng c╞í bß║ún1` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Th╞░ß╗ƒng ├¥ thß╗⌐c v├á Tu├ón thß╗º/Th╞░ß╗ƒng Hiß╗çß╗Ñ quß║ú hoß║ít ─æß╗Öng1` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Tß╗òng thu nhß║¡p theo ng├áy c├┤ng` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Th╞░ß╗ƒng CRM/CS (C.Mai)` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Th╞░ß╗ƒng CLDV` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Th╞░ß╗ƒng Quß║ún l├╜ chung` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Th╞░ß╗ƒng hiß╗çu quß║ú quß║ún l├╜` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Th╞░ß╗ƒng Ebitda` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Th╞░ß╗ƒng Vinmec` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Th╞░ß╗ƒng an ninh` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Th╞░ß╗ƒng Lß╗à/Tß║┐t` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Tß╗òng th╞░ß╗ƒng` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `PC Gß╗¡i xe/C├┤ng t├íc` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Phß╗Ñ cß║Ñp chß╗⌐ng chß╗ë h├ánh nghß╗ü` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Phß╗Ñ cß║Ñp kh├íc` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Tß╗òng phß╗Ñ cß║Ñp` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Trß╗½ kh├íc` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Tß╗òng thu nhß║¡p tr╞░ß╗¢c thuß║┐` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Mß╗⌐c l╞░╞íng tham gia BHXH` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `BHYT (1,5%)` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `BHXH (8%)` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `BHTN (1%)` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `NL─É ─æ├│ng BHXH (10.5%)` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `NL─É ─æ├│ng ph├¡ C├┤ng ─æo├án (1%)` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `BHXH (17%` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `TNL─É / BNN (0.5%)` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `BHYT (3%)` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `BHTN 1%` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Doanh nghiß╗çp ─æ├│ng BHXH 21.5%` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Doanh nghiß╗çp ─æ├│ng C├┤ng ─æo├án 2%` INTEGER(11), 
    `Kh├┤ng t├¡nh thuß║┐ (Phß╗Ñ cß║Ñp c╞ím tr╞░a/ ─Éß╗ông phß╗Ñc)` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Tß╗öNG THU NHß║¼P CHß╗èU THUß║╛` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `─Éß╗æi t╞░ß╗úng t├¡nh Thuß║┐ TNCN` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Cam kß║┐t` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Sß╗æ ng╞░ß╗¥i phß╗Ñ thuß╗Öc` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Tß╗öNG THU NHß║¼P T├ìNH THUß║╛` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Thu Tiß╗ün thuß║┐ TNCN` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Thß╗▒c l├únh` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Cty ─æ├│ng hß╗Ö BHXH` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Thu hß╗Ö tiß╗ün BHXH (21.5%` INTEGER(11), 
    `Chuyß╗ân khoß║ún` DOUBLE(10, 3), 
    `Column1` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Hß╗ì & t├¬n` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Sß╗æ t├ái khoß║ún` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Ng├ón h├áng` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Mail` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `─É├ú Chuyß╗ân khoß║ún 05/02/2024` DOUBLE(10, 3), 
    `Bß╗ò sung` INTEGER(11), 
    `Ghi ch├║` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Ng├áy thanh to├ín` VARCHAR(50) COLLATE utf8mb4_unicode_ci
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `IncomeByJobClosedOfMonth` (
    `IncomeByJobClosedOfMonthId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `StaffId` INTEGER(11), 
    `ClosedTime` DATE, 
    `BusinessType` INTEGER(11), 
    `NumberCases` INTEGER(11), 
    `IncomePerCase` DECIMAL(10, 2), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    PRIMARY KEY (`IncomeByJobClosedOfMonthId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `VnProvince` (
    `VnProvinceId` INTEGER(10) UNSIGNED NOT NULL, 
    `ProvinceCode` VARCHAR(8) CHARACTER SET utf8mb4, 
    `ProvincePostalCode` VARCHAR(8) CHARACTER SET utf8mb4, 
    `NameVi` VARCHAR(64) CHARACTER SET utf8mb4 NOT NULL, 
    `NameEn` VARCHAR(64) CHARACTER SET utf8mb4, 
    `LabelVi` VARCHAR(32) CHARACTER SET utf8mb4 NOT NULL COMMENT 'Th├ánh ph?
T?nh', 
    `LabelEn` VARCHAR(32) CHARACTER SET utf8mb4 COMMENT 'Municipality
Province', 
    `Ordering` INTEGER(10) UNSIGNED, 
    `State` INTEGER(11) DEFAULT '1', 
    PRIMARY KEY (`VnProvinceId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `ModuleViewing` (
    `ViewingId` INTEGER(11) UNSIGNED NOT NULL, 
    `ModuleId` INTEGER(11) UNSIGNED NOT NULL, 
    CONSTRAINT `fk_ModuleViewing_Module` FOREIGN KEY(`ModuleId`) REFERENCES `Module` (`ModuleId`), 
    CONSTRAINT `fk_ModuleViewing_Viewing` FOREIGN KEY(`ViewingId`) REFERENCES `Viewing` (`ViewingId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_ModuleViewing_ViewingId_idx` ON `ModuleViewing` (`ViewingId`);

CREATE INDEX `fk_ModuleViewing_ModuleId_idx` ON `ModuleViewing` (`ModuleId`);

CREATE TABLE `OrgHierarchy` (
    `OrgHierarchyId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `NameVi` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `NameEn` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL, 
    `Priority` INTEGER(11) DEFAULT '0', 
    `Status` INTEGER(11) COMMENT '1 active
0 deactice' DEFAULT '1', 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`OrgHierarchyId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `ContactFavorite` (
    `UserId` INTEGER(10) UNSIGNED NOT NULL, 
    `ContactId` INTEGER(10) UNSIGNED NOT NULL, 
    `StaffPhoneId` INTEGER(10) UNSIGNED NOT NULL, 
    CONSTRAINT `fk_ContactFavorite_User` FOREIGN KEY(`UserId`) REFERENCES `User` (`UserId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_ContactFavorite_User_idx` ON `ContactFavorite` (`UserId`);

CREATE TABLE `ScoreCampaign` (
    `ScoreCampaignId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `Code` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    `Name` VARCHAR(512) COLLATE utf8mb4_unicode_ci, 
    `Description` VARCHAR(512) COLLATE utf8mb4_unicode_ci, 
    `MinScoreToPass` INTEGER(11) DEFAULT '10', 
    `IsCycle` TINYINT(4) DEFAULT '1', 
    `ScoreMethod` TINYINT(4) COMMENT '1 Arrived
2 Camera' DEFAULT '1', 
    `AlertMethod` TINYINT(4) COMMENT '1 SMS 
2 Email 
 3 Ticket' DEFAULT '1', 
    `FromDate` DATETIME, 
    `ToDate` DATETIME, 
    `NumerTime` TINYINT(4) DEFAULT '1', 
    `Unit` INTEGER(11) COMMENT '1 Ng├áy
2 tuan
3 thang' DEFAULT '0', 
    `MinimunToNextTime` INTEGER(11) COMMENT 'hour' DEFAULT '0', 
    `IsIncludeSubNode` TINYINT(4) DEFAULT '1', 
    `TicketProcessingTime` TINYINT(4) COMMENT 'hour', 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    `UpdatedDate` DATETIME, 
    `UpdatedBy` INTEGER(11), 
    PRIMARY KEY (`ScoreCampaignId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `SalaryPerHour` (
    `Id` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `StaffId` INTEGER(11), 
    `StartDate` DATE, 
    `EndDate` DATE, 
    `PositionId` INTEGER(11) COMMENT '1: T? v?n vi├¬n, 2: Ph? t├í, 3: Qu?n l├╜ ph├▓ng kh├ím', 
    `WorkProfilePositionId` INTEGER(11), 
    `WorkProfilePositionLevel` VARCHAR(50) CHARACTER SET utf8mb4, 
    `Amount` DECIMAL(15, 5), 
    PRIMARY KEY (`Id`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `IX_StartDate_EndDate` ON `SalaryPerHour` (`StartDate`, `EndDate`);

CREATE INDEX `IX_StaffId` ON `SalaryPerHour` (`StaffId`, `StartDate`, `EndDate`);

CREATE TABLE `NotificationBanner` (
    `NotificationBannerId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `NotificationId` INTEGER(11), 
    `CDNURL` VARCHAR(1024) COLLATE utf8mb4_unicode_ci, 
    `Type` TINYINT(4), 
    `Duration` INTEGER(4), 
    `Link` VARCHAR(1024) COLLATE utf8mb4_unicode_ci, 
    `CreatedBy` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`NotificationBannerId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `UserGroupViewing` (
    `UserGroupId` INTEGER(11) UNSIGNED NOT NULL, 
    `ViewingId` INTEGER(11) UNSIGNED NOT NULL, 
    CONSTRAINT `fk_UserGroupViewing_UserGroup` FOREIGN KEY(`UserGroupId`) REFERENCES `UserGroup` (`UserGroupId`), 
    CONSTRAINT `fk_UserGroupViewing_Viewing` FOREIGN KEY(`ViewingId`) REFERENCES `Viewing` (`ViewingId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_UserGroupViewing_ViewingId_idx` ON `UserGroupViewing` (`ViewingId`);

CREATE INDEX `fk_UserGroupViewing_UserGroupId_idx` ON `UserGroupViewing` (`UserGroupId`);

CREATE TABLE `Theme` (
    `ThemeId` INTEGER(11) UNSIGNED NOT NULL, 
    `ExtensionId` INTEGER(11) UNSIGNED NOT NULL, 
    `AppId` INTEGER(11) UNSIGNED NOT NULL, 
    `Name` VARCHAR(128) CHARACTER SET utf8 NOT NULL, 
    `Dir` VARCHAR(32) CHARACTER SET utf8 NOT NULL, 
    `State` INTEGER(1) NOT NULL DEFAULT '1', 
    `Config` TEXT CHARACTER SET utf8, 
    `IsDefault` INTEGER(1) DEFAULT '0', 
    PRIMARY KEY (`ThemeId`), 
    CONSTRAINT `fk_Theme_Extension` FOREIGN KEY(`ExtensionId`, `AppId`) REFERENCES `Extension` (`ExtensionId`, `AppId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_Theme_Extension_idx` ON `Theme` (`ExtensionId`, `AppId`);

CREATE TABLE `ExecuteValidConfig` (
    `ExecuteValidConfigId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `CheckinValidAfter` INTEGER(10) UNSIGNED NOT NULL COMMENT 'kho?ng th?i gian gi?i h?n l?n checkin v?n c├▓n hi?u l?c. T├¡nh theo ph├║t' DEFAULT '20', 
    `CheckoutValidBefore` INTEGER(10) UNSIGNED NOT NULL COMMENT 'kho?ng th?i gian gi?i h?n l?n checkout v?n c├▓n hi?u l?c. T├¡nh theo ph├║t' DEFAULT '20', 
    `State` INTEGER(10) UNSIGNED NOT NULL DEFAULT '1', 
    `InvalidCheckinMessage` VARCHAR(64) COLLATE utf8mb4_unicode_ci, 
    `InvalidCheckoutMessage` VARCHAR(64) COLLATE utf8mb4_unicode_ci, 
    `IsShiftConfig` INTEGER(11) COMMENT 'Config d├╣ng cho r├║t c├┤ng theo ca hay r├║t c├┤ng the ng├áy fulltime' DEFAULT '0', 
    PRIMARY KEY (`ExecuteValidConfigId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `Degree` (
    `DegreeId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `NameVi` VARCHAR(32) CHARACTER SET utf8mb4 NOT NULL, 
    `NameEn` VARCHAR(32) CHARACTER SET utf8mb4 NOT NULL, 
    `Ordering` INTEGER(11), 
    PRIMARY KEY (`DegreeId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `StaffLevel` (
    `StaffLevelId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `StaffLevelGroupId` INTEGER(11), 
    `Name` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    `Ordering` INTEGER(11), 
    `State` INTEGER(11), 
    PRIMARY KEY (`StaffLevelId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `VnDistrict_BK_20230710` (
    `VnDistrictId` INTEGER(10) UNSIGNED NOT NULL DEFAULT '0', 
    `VnProvinceId` INTEGER(10) UNSIGNED NOT NULL, 
    `DistrictCode` VARCHAR(8) CHARACTER SET utf8mb4, 
    `DistrictPostalCode` VARCHAR(8) CHARACTER SET utf8mb4, 
    `NameVi` VARCHAR(64) CHARACTER SET utf8mb4 NOT NULL, 
    `NameEn` VARCHAR(64) CHARACTER SET utf8mb4, 
    `LabelVi` VARCHAR(32) CHARACTER SET utf8mb4 NOT NULL COMMENT 'Qu?n
Th? x├ú
Huy?n
Th├ánh ph?', 
    `LabelEn` VARCHAR(32) CHARACTER SET utf8mb4 COMMENT 'Urban District
Town
Rural District
Provincial City', 
    `Ordering` INTEGER(10) UNSIGNED, 
    `isDeleted` TINYINT(4)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `OrgWorkProfile` (
    `OrgWorkProfileId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `WorkProfileId` INTEGER(11), 
    `OrgId` INTEGER(11) NOT NULL, 
    `Status` INTEGER(11) COMMENT '0: Deleted | 1: Active', 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    `UpdatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `UpdatedBy` INTEGER(11), 
    `PosistionType` TINYINT(3) COMMENT '1 Normal,2 Manager, 3 Concurrently' DEFAULT '1', 
    `FromDate` DATETIME, 
    `ToDate` DATETIME, 
    `ObjectType` INTEGER(11) COMMENT '1:WorkContractAnnex, 2:WorkPlaceChanging', 
    `ObjectId` INTEGER(11), 
    `ExpectedToDate` DATETIME COMMENT 'when update Todate move ToDate data to ExpectedToDate', 
    `IsProcess` INTEGER(11) DEFAULT '0', 
    `RefWorkProfileId` INTEGER(11), 
    `IsHidden` TINYINT(1), 
    `StaffId` INTEGER(11), 
    `UserId` INTEGER(11), 
    `WorkProfilePositionId` INTEGER(11), 
    `AutoRenew` TINYINT(1) DEFAULT '1', 
    `IsMainPosition` TINYINT(4) NOT NULL DEFAULT '0', 
    PRIMARY KEY (`OrgWorkProfileId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `idx_WorkProfileID` ON `OrgWorkProfile` (`WorkProfileId`);

CREATE INDEX `idx_OrgId` ON `OrgWorkProfile` (`OrgId`);

CREATE INDEX `Idx_UserId` ON `OrgWorkProfile` (`UserId`);

CREATE INDEX `Idx_StaffId` ON `OrgWorkProfile` (`StaffId`);

CREATE TABLE `NotificationRecipient` (
    `NotificationRecipientId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `NotificationId` INTEGER(11), 
    `RecipientId` INTEGER(11), 
    `RecipientType` INTEGER(11) COMMENT '1 Org\\n2 Staff', 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    `UpdatedDate` DATETIME, 
    `UpdatedBy` INTEGER(11), 
    `IsIncludeSubNode` TINYINT(4) DEFAULT '0', 
    PRIMARY KEY (`NotificationRecipientId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `ASalaryBO` (
    `StaffSalaryDetailsId` INTEGER(11), 
    `StaffId` INTEGER(11), 
    `StaffCode` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `FullName` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Company` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `WorkProfilePosition` VARCHAR(100) COLLATE utf8mb4_unicode_ci, 
    `ContractType` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Branch` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `StartDate` DOUBLE(10, 3), 
    `Shift` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Total` INTEGER(11), 
    `NoTimekeeping` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `ActualHoursWorked` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `AnnualLeave` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `PaidLeave` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `PublicHolidaysLeave` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `TotalStandardHours` DOUBLE(10, 3), 
    `StandardWage` INTEGER(11), 
    `BasicSalary` INTEGER(11), 
    `PerformanceBonus` INTEGER(11), 
    `LunchAllowance` INTEGER(11), 
    `UniformAllowance` INTEGER(11), 
    `TotalIncomeWorkingDays` INTEGER(11), 
    `CRM/CSBonus` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `ServiceQualityBonus` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `GeneralManagermentBonus` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `EfficiencyManagementBonus` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `EbitdaBonus` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `VinmecBonus` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `SecurityBonus` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `HolidayBonus` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `TotalBonus` INTEGER(11), 
    `ParkingTravelAllowance` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `ProfessionalCertificateAllowance` INTEGER(11), 
    `OtherAllowances` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `TotalAllowances` INTEGER(11), 
    `OtherDeductions` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `TotalIncomeBeforeTax` INTEGER(11), 
    `ParticipatingSalaryInSocialInsurance` INTEGER(11), 
    `PersonalHealthInsurance` INTEGER(11), 
    `PersonalSocialInsurance` INTEGER(11), 
    `PersonalUnemploymentInsurance` INTEGER(11), 
    `EmployeeSocialInsurance` INTEGER(11), 
    `EmployeeUnionFee` INTEGER(11), 
    `CompanySocialInsurance` INTEGER(11), 
    `CompanyOccupaitionalAccidentOrDisease` INTEGER(11), 
    `CompanyHealthInsurance` INTEGER(11), 
    `CompanyUnemploymentInsurance` INTEGER(11), 
    `EnterpriseSocialInsurance` INTEGER(11), 
    `EnterpriseUnionFee` INTEGER(11), 
    `LunchOrUniformAllowanceNoTax` INTEGER(11), 
    `TotalTaxableIncome` INTEGER(11), 
    `TaxableIncomeObject` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Commitment` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Dependents` INTEGER(11), 
    `TotalAssessableIncome` INTEGER(11), 
    `PersonalIncomeTaxCollection` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `ActualPayment` INTEGER(11), 
    `CompanyPaysSocialInsurance` INTEGER(11), 
    `WithholdSocialInsurance` INTEGER(11), 
    `BankTransfer` INTEGER(11), 
    `Name` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `AccountNumber` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `Bank` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Email` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `TransferAmount` INTEGER(11), 
    `Additional` INTEGER(11), 
    `Notes` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `PaymentDate` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Level` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `SalaryPerHour` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `CompensatoryLeave` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `TotalLunchAllowance` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `FixedIncomeWithLunchAllowance` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `FixedIncomeAmountWithLunchAllowance` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `TaskBonus` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `ClinicsAchievingKPIRevenueBonus` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `AssistantManagerAndConcurrentBonus` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `GuaranteedIncomeAllowance` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `DentalTour` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `WarehouseAllowance` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `OtherTotalIncome` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `DoctorBonus` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `AdjustmentForDecemberShortfall` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `PayPeriod` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Template` INTEGER(11) COMMENT '1-BO
2-Phu ta
3-Bac Si
4-Bao ve' DEFAULT '1'
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `File` (
    `FileId` INTEGER(11) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `FromModule` INTEGER(11) UNSIGNED NOT NULL, 
    `FromApp` INTEGER(11) UNSIGNED NOT NULL, 
    `Name` VARCHAR(196) CHARACTER SET utf8, 
    `FileName` VARCHAR(196) CHARACTER SET utf8, 
    `FileThumbnail` VARCHAR(196) CHARACTER SET utf8, 
    `FileExt` VARCHAR(5) CHARACTER SET utf8, 
    `FileMine` VARCHAR(128) CHARACTER SET utf8, 
    `FileSize` INTEGER(11), 
    `CreatedBy` INTEGER(11) UNSIGNED NOT NULL DEFAULT '0', 
    `CreatedAt` INTEGER(11) UNSIGNED NOT NULL DEFAULT '0', 
    `IsImage` INTEGER(1) DEFAULT '0', 
    PRIMARY KEY (`FileId`), 
    CONSTRAINT `fk_File_CreatedBy` FOREIGN KEY(`CreatedBy`) REFERENCES `User` (`UserId`), 
    CONSTRAINT `fk_File_App` FOREIGN KEY(`FromApp`) REFERENCES `App` (`AppId`), 
    CONSTRAINT `fk_File_Module` FOREIGN KEY(`FromModule`) REFERENCES `Module` (`ModuleId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_File_Module_idx` ON `File` (`FromModule`);

CREATE INDEX `fk_File_CreatedBy_idx` ON `File` (`CreatedBy`);

CREATE INDEX `fk_File_App_idx` ON `File` (`FromApp`);

CREATE TABLE `MenuItem` (
    `MenuItemId` INTEGER(11) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `RootId` INTEGER(11) UNSIGNED NOT NULL DEFAULT '0', 
    `MenuId` INTEGER(11) UNSIGNED NOT NULL, 
    `ParentId` INTEGER(11) UNSIGNED NOT NULL DEFAULT '0', 
    `ThemeId` INTEGER(11) UNSIGNED NOT NULL, 
    `Name` VARCHAR(128) CHARACTER SET utf8, 
    `Alias` VARCHAR(128) CHARACTER SET utf8, 
    `State` INTEGER(1) DEFAULT '1', 
    `Type` INTEGER(1), 
    `App` VARCHAR(32) CHARACTER SET utf8, 
    `Mod` VARCHAR(32) CHARACTER SET utf8, 
    `Description` TEXT CHARACTER SET utf8, 
    `Level` INTEGER(11) DEFAULT '0', 
    `Lft` INTEGER(11) DEFAULT '1', 
    `Rgt` INTEGER(11) DEFAULT '2', 
    `Link` VARCHAR(196) CHARACTER SET utf8, 
    `Path` VARCHAR(196) CHARACTER SET utf8, 
    `ViewingId` INTEGER(11) DEFAULT '0', 
    `IsDefault` INTEGER(1) DEFAULT '0', 
    `CreatedBy` INTEGER(11) UNSIGNED NOT NULL, 
    `CreatedAt` INTEGER(11) UNSIGNED NOT NULL, 
    `CheckedOutBy` INTEGER(11) UNSIGNED NOT NULL DEFAULT '0', 
    `CheckedOutAt` INTEGER(11) DEFAULT '0', 
    `Config` TEXT CHARACTER SET utf8, 
    `Ordering` INTEGER(11) DEFAULT '0', 
    PRIMARY KEY (`MenuItemId`), 
    CONSTRAINT `fk_MenuItem_CreatedBy` FOREIGN KEY(`CreatedBy`) REFERENCES `User` (`UserId`), 
    CONSTRAINT `fk_MenuItem_Menu` FOREIGN KEY(`MenuId`) REFERENCES `Menu` (`MenuId`), 
    CONSTRAINT `fk_MenuItem_Theme` FOREIGN KEY(`ThemeId`) REFERENCES `Theme` (`ThemeId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_MenuItem_Theme_idx` ON `MenuItem` (`ThemeId`);

CREATE INDEX `fk_MenuItem_Menu_idx` ON `MenuItem` (`MenuId`);

CREATE INDEX `fk_MenuItem_CreatedBy_idx` ON `MenuItem` (`CreatedBy`);

CREATE TABLE `MenuNavbarGroup` (
    `MenuNavbarGroupId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `NameVI` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `NameEN` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `Priority` INTEGER(11), 
    `CreatedDate` DATETIME, 
    `Status` INTEGER(11) DEFAULT '1', 
    PRIMARY KEY (`MenuNavbarGroupId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `Country` (
    `CountryId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `Name` VARCHAR(64) CHARACTER SET utf8mb4 NOT NULL, 
    `Code` VARCHAR(8) CHARACTER SET utf8mb4 NOT NULL, 
    `Ordering` INTEGER(11) NOT NULL DEFAULT '0', 
    `NationalityLabel` VARCHAR(128) COLLATE utf8mb4_unicode_ci, 
    PRIMARY KEY (`CountryId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `WorkContractAnnexDetail` (
    `WorkContractAnnexDetailid` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `WorkContractAnnexId` INTEGER(11), 
    `WorkContractAnnexIntentId` INTEGER(11), 
    `IsDeleted` SMALLINT(6) DEFAULT '0', 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    `DepartmentId` INTEGER(11), 
    `TeamId` INTEGER(11), 
    `WorkPosition` INTEGER(11), 
    `WorkTimeMode` VARCHAR(20) COLLATE utf8mb4_unicode_ci COMMENT 'Hour, Month', 
    `SalaryAmount` DECIMAL(18, 2), 
    `SocialInsuranceSalary` DECIMAL(18, 2), 
    `AdditionalSalaryAmount` DECIMAL(18, 2), 
    `WorkPositionNote` VARCHAR(128) COLLATE utf8mb4_unicode_ci, 
    `StaffLevelId` INTEGER(11), 
    `WorkProfilePositionId` INTEGER(11), 
    `IncomeTypeId` INTEGER(11), 
    `IncomeTypeLevelId` INTEGER(11), 
    `WorkProfilePositionSalaryAmountId` INTEGER(11), 
    PRIMARY KEY (`WorkContractAnnexDetailid`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `IX_WorkContractAnnexDetail_WorkContractAnnexId` ON `WorkContractAnnexDetail` (`WorkContractAnnexId`);

CREATE TABLE `TimeKeeper` (
    `TimeKeeperId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `StaffId` INTEGER(10) UNSIGNED NOT NULL, 
    `WorkProfileId` INTEGER(10) UNSIGNED NOT NULL, 
    `Day` DATE NOT NULL, 
    `CheckInAt` INTEGER(10) UNSIGNED, 
    `CheckOutAt` INTEGER(10) UNSIGNED DEFAULT '0', 
    `FromIp` VARCHAR(16) CHARACTER SET utf8mb4, 
    `RegistedMobileDeviceId` INTEGER(10) UNSIGNED, 
    `MobileAppId` INTEGER(10) UNSIGNED, 
    `CheckInLocationId` INTEGER(10), 
    `CheckOutLocationId` INTEGER(11), 
    `WorkShiftId` INTEGER(11), 
    `WorkShiftStartTime` TIME, 
    `WorkShiftEndTime` TIME, 
    `EditedAt` INTEGER(11), 
    `EditedBy` INTEGER(11), 
    `WeekDayTotalBreakTimeInMunite` INTEGER(11) NOT NULL DEFAULT '0', 
    `WorkShiftTotalBreakTimeInMinute` INTEGER(11) NOT NULL DEFAULT '0', 
    `WorkScheduleId` INTEGER(11) UNSIGNED, 
    `Status` INTEGER(11) DEFAULT '1', 
    `ExpectedCheckInAt` INTEGER(10), 
    `ExpectedCheckOutAt` INTEGER(10), 
    `ReasonNote` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `UpdatedStatusDate` DATETIME, 
    `UpdatedStatusById` INTEGER(11), 
    `IsDeleted` TINYINT(4) DEFAULT '0', 
    `ConfirmCheckIn` TIME, 
    `ConfirmCheckOut` TIME, 
    `IsEdited` TINYINT(4) DEFAULT '0', 
    `ApprovedAt` DATETIME, 
    `ApprovedBy` INTEGER(11), 
    `TotalHour` DECIMAL(3, 1), 
    `TotalPaidHour` DECIMAL(3, 1), 
    `ShiftStart` TIME, 
    `ShiftEnd` TIME, 
    `TotalBreakTimeInMinute` INTEGER(11), 
    `StaffConfirmNote` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `Order` INTEGER(11), 
    `LastCheckOut` TIME, 
    `TimeKeepingRequestId` INTEGER(11), 
    PRIMARY KEY (`TimeKeeperId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_TimeKeeper_WorkProfile_idx` ON `TimeKeeper` (`WorkProfileId`);

CREATE INDEX `fk_TimeKeeper_WorkLocation_idx` ON `TimeKeeper` (`CheckInLocationId`);

CREATE INDEX `fk_TimeKeeper_Staff_idx` ON `TimeKeeper` (`StaffId`, `Day`);

CREATE INDEX `fk_TimeKeeper_RegistedMobileDevice_idx` ON `TimeKeeper` (`RegistedMobileDeviceId`);

CREATE INDEX `fk_TimeKeeper_MobileApp_idx` ON `TimeKeeper` (`MobileAppId`);

CREATE INDEX `fk_TimeKeeper_EditUser` ON `TimeKeeper` (`EditedBy`);

CREATE INDEX `fk_TimeKeeper_Day` ON `TimeKeeper` (`Day`);

CREATE TABLE `TaskPriority` (
    `TaskPriorityId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `Name` VARCHAR(16) COLLATE utf8mb4_unicode_ci NOT NULL, 
    `Ordering` INTEGER(11) NOT NULL, 
    `ColorRGB` VARCHAR(6) COLLATE utf8mb4_unicode_ci NOT NULL, 
    PRIMARY KEY (`TaskPriorityId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `EmailAttachFile` (
    `EmailAttachFileId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `EmailId` INTEGER(11), 
    `CDNURL` VARCHAR(2048) COLLATE utf8mb4_unicode_ci, 
    `FileType` VARCHAR(20) COLLATE utf8mb4_unicode_ci, 
    `FileName` VARCHAR(128) COLLATE utf8mb4_unicode_ci, 
    `FileSize` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    PRIMARY KEY (`EmailAttachFileId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `AddressType` (
    `AddressTypeId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `Name` VARCHAR(32) COLLATE utf8mb4_unicode_ci NOT NULL, 
    `Ordering` INTEGER(10) UNSIGNED NOT NULL, 
    PRIMARY KEY (`AddressTypeId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `WorkContractAnnexIntent` (
    `WorkContractAnnexIntentId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `Name` VARCHAR(128) COLLATE utf8mb4_unicode_ci, 
    `Description` VARCHAR(128) COLLATE utf8mb4_unicode_ci, 
    `IsActive` INTEGER(11) DEFAULT '1', 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    PRIMARY KEY (`WorkContractAnnexIntentId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `AbsenceType` (
    `AbsenceTypeId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `AbsenceTypeCode` VARCHAR(8) CHARACTER SET utf8mb4 NOT NULL, 
    `AbsenceGroupType` TINYINT(4) COMMENT '1: Ngh? ph├⌐p c├│ h??ng l??ng c?a c├┤ng ty, 2: Ngh? ph├⌐p kh├┤ng h??ng l??ng c?a c├┤ng ty', 
    `Name` VARCHAR(128) CHARACTER SET utf8mb4 NOT NULL, 
    `Note` TEXT CHARACTER SET utf8mb4, 
    `Ordering` INTEGER(10) UNSIGNED NOT NULL, 
    `GroupType` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    `Value` DOUBLE, 
    `MaxValue` DOUBLE, 
    `AppliedDate` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    `IsHidden` TINYINT(4) DEFAULT '0', 
    PRIMARY KEY (`AbsenceTypeId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `WorkLocation` (
    `WorkLocationId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `Name` VARCHAR(128) CHARACTER SET utf8mb4 NOT NULL, 
    `State` INTEGER(1) UNSIGNED DEFAULT '1', 
    `Address` VARCHAR(128) CHARACTER SET utf8mb4, 
    `Lat` DECIMAL(12, 3), 
    `Lng` DECIMAL(12, 3), 
    `VnProvinceId` INTEGER(10) UNSIGNED, 
    `VnDistrictId` INTEGER(10) UNSIGNED, 
    `VnWardId` INTEGER(10) UNSIGNED, 
    `CompanyId` INTEGER(11), 
    PRIMARY KEY (`WorkLocationId`)
)COMMENT='vß╗ï tr├¡ vß║¡t l├╜ li├¬n quan ─æß║┐n viß╗çc check chß║Ñm c├┤ng. V├¡ dß╗Ñ 33 ─Éinh Ti├¬n Ho├áng vß╗½a gß╗ôm HO lß║íi vß╗½a gß╗ôm Nha Khoa' DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_WorkLocation_VnWard_idx` ON `WorkLocation` (`VnWardId`);

CREATE INDEX `fk_WorkLocation_VnProvince_idx` ON `WorkLocation` (`VnProvinceId`);

CREATE INDEX `fk_WorkLocation_VnDistrict_idx` ON `WorkLocation` (`VnDistrictId`);

CREATE UNIQUE INDEX `Name_UNIQUE` ON `WorkLocation` (`Name`);

CREATE TABLE `SysLanguage` (
    `SysLanguageId` INTEGER(11) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `ExtensionId` INTEGER(11) UNSIGNED NOT NULL, 
    `AppId` INTEGER(11) UNSIGNED NOT NULL, 
    `Code` VARCHAR(2) CHARACTER SET utf8, 
    `Name` VARCHAR(32) CHARACTER SET utf8, 
    `Ordering` INTEGER(11) DEFAULT '0', 
    `State` INTEGER(1) DEFAULT '1', 
    `IsGlobal` INTEGER(1) COMMENT 'ng├┤n ng? n├áy ???c th?y b?i t?t c? c├íc app' DEFAULT '0', 
    `IsDefault` INTEGER(1) COMMENT 'ng├┤n ng? default c?a app t??ng ?ng' DEFAULT '0', 
    PRIMARY KEY (`SysLanguageId`), 
    CONSTRAINT `fk_Language_Extension` FOREIGN KEY(`ExtensionId`, `AppId`) REFERENCES `Extension` (`ExtensionId`, `AppId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_Language_Extension_idx` ON `SysLanguage` (`ExtensionId`, `AppId`);

CREATE TABLE `EmailReceiver` (
    `EmailReceiverlId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `EmailId` INTEGER(11), 
    `ReceiverId` INTEGER(11), 
    `ReceiverType` INTEGER(11) COMMENT '1 Staff; 2 Group;3 Org' DEFAULT '1', 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `Type` TINYINT(4) COMMENT '1:To
2:CC
3:BCC
4:Forward', 
    PRIMARY KEY (`EmailReceiverlId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `rptTimekeeping` (
    `rptDate` DATE, 
    `StaffId` INTEGER(11), 
    `IsFullTime` TINYINT(4), 
    `WorkShiftId` INTEGER(11), 
    `StartTime` TIME, 
    `EndTime` TIME, 
    `CheckIn` TIME, 
    `CheckOut` TIME, 
    `RequestedCheckIn` TIME, 
    `RequestedCheckOut` TIME, 
    `RequestedNote` VARCHAR(2000) COLLATE utf8mb4_unicode_ci, 
    `Status` TINYINT(4) COMMENT '1: New, 2: Approved, 3: Rejected, 4: Cancelled', 
    `UpdatedStatusBy` INTEGER(11), 
    `UpdatedStatusDate` DATETIME, 
    `UpdatedStatusNote` VARCHAR(2000) COLLATE utf8mb4_unicode_ci, 
    `LeaveCountType` TINYINT(4) COMMENT '1: ngh? nguy├¬n ng├áy, 2: ngh? bu?i s├íng, 3: ngh? bu?i chi?u', 
    `ActualWorkingHours` DECIMAL(5, 2), 
    `ActualWorkingDays` DECIMAL(5, 2), 
    `PaidWorkingHours` DECIMAL(5, 2), 
    `PaidWorkingDays` DECIMAL(5, 2)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `idx_rptTimekeeping_rptDate` ON `rptTimekeeping` (`rptDate`);

CREATE INDEX `idx_rptTimekeeping_StaffId` ON `rptTimekeeping` (`StaffId`, `rptDate`);

CREATE TABLE `TimeKeeperHistory` (
    `TimeKeeperId` INTEGER(10) UNSIGNED NOT NULL, 
    `StaffId` INTEGER(10) UNSIGNED NOT NULL, 
    `WorkProfileId` INTEGER(10) UNSIGNED NOT NULL, 
    `Day` DATE NOT NULL, 
    `CheckInAt` INTEGER(10) UNSIGNED, 
    `CheckOutAt` INTEGER(10) UNSIGNED DEFAULT '0', 
    `FromIp` VARCHAR(16) CHARACTER SET utf8mb4, 
    `RegistedMobileDeviceId` INTEGER(10) UNSIGNED, 
    `MobileAppId` INTEGER(10) UNSIGNED, 
    `CheckInLocationId` INTEGER(10) UNSIGNED, 
    `CheckOutLocationId` INTEGER(11), 
    `WorkShiftId` INTEGER(11), 
    `WorkShiftStartTime` TIME, 
    `WorkShiftEndTime` TIME, 
    `WeekDayTotalBreakTimeInMunite` INTEGER(11) NOT NULL DEFAULT '0', 
    `WorkShiftTotalBreakTimeInMinute` INTEGER(11) NOT NULL DEFAULT '0', 
    `EditedAt` INTEGER(11), 
    `EditedBy` INTEGER(11), 
    `IsDeleted` TINYINT(4) DEFAULT '0', 
    `FlushedAt` INTEGER(11) UNSIGNED NOT NULL
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `StaffNationality` (
    `StaffNationalityId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `StaffId` INTEGER(11), 
    `CountryId` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    `UpdatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `UpdatedBy` INTEGER(11), 
    `IsActive` BIT(1), 
    `Priority` SMALLINT(6), 
    PRIMARY KEY (`StaffNationalityId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `Allowance` (
    `AllowanceId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `Name` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL, 
    `DefaultAmount` DECIMAL(12, 2) NOT NULL, 
    `Ordering` INTEGER(10) UNSIGNED NOT NULL, 
    `RepeatBy` INTEGER(1) COMMENT 'Chi l?p l?i theo:
1 - theo tu?n
2 - theo th├íng
3 - theo n?m' DEFAULT '2', 
    `State` INTEGER(1) UNSIGNED NOT NULL DEFAULT '1', 
    `LimitUse` INTEGER(11) DEFAULT '1', 
    PRIMARY KEY (`AllowanceId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `WorkProfilePositionPriorityMapping` (
    `WorkProfilePositionPriorityMappingId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `WorkProfilePositionId` INTEGER(11), 
    `WorkPriorityLevelId` INTEGER(11), 
    `State` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`WorkProfilePositionPriorityMappingId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `ServiceBranchMappingExclude` (
    `ServiceBranchMappingExcludeId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `ServiceId` INTEGER(11), 
    `BranchId` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`ServiceBranchMappingExcludeId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `ScoreCardTicket` (
    `ScoreCardTicketId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `ScoreCardId` INTEGER(11), 
    `ScoreCardDetailId` INTEGER(11), 
    `Code` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    `Name` VARCHAR(512) COLLATE utf8mb4_unicode_ci, 
    `Status` INTEGER(11) COMMENT '1 New
2 Working
3 Completed,4 Reject', 
    `StatusNote` VARCHAR(512) COLLATE utf8mb4_unicode_ci, 
    `DueDate` DATETIME, 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    `UpdatedDate` DATETIME, 
    `UpdatedBy` INTEGER(11), 
    `MediaURL` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `FinalResult` INTEGER(11) COMMENT '1 ??t\\n2 kh├┤ng ?atk' DEFAULT '0', 
    `RefCode` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    `PeriodDueTime` INTEGER(11) COMMENT 't├¡nh theo ph├║t', 
    `IsCurrent` INTEGER(11) DEFAULT '1', 
    `CompletedDate` DATETIME, 
    `CompletedBy` INTEGER(11), 
    PRIMARY KEY (`ScoreCardTicketId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `MenuNavbarOrgMapping` (
    `MenuNavbarOrgMappingId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `MenuNavbarId` INTEGER(11), 
    `OrgId` INTEGER(11), 
    `IsDeleted` INTEGER(11) DEFAULT '0', 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`MenuNavbarOrgMappingId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `StaffEvaluation` (
    `StaffEvaluationId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `WorkProfileId` INTEGER(11), 
    `StaffId` INTEGER(11), 
    `StaffEvaluationContent` TEXT COLLATE utf8mb4_unicode_ci COMMENT 'DataJon:"{CreatedBy:''1'',CreatedDate=''2024-01-12 23:58:14'', ''Content'':''''}', 
    `ManagerEvaluationContent` TEXT COLLATE utf8mb4_unicode_ci COMMENT 'DataJon:"{CreatedBy:''1'',CreatedDate=''2024-01-12 23:58:14'', ''Content'':''''}', 
    `IsPass` INTEGER(11) COMMENT '1/0 : ─æa╠út/ kh├┤ng ─æa╠út', 
    `IsSign` INTEGER(11) COMMENT '1/0 : ky╠ü/ kh├┤ng ky╠ü', 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    `UpdatedDate` DATETIME, 
    `UpdatedBy` INTEGER(11), 
    PRIMARY KEY (`StaffEvaluationId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `EmailReceiverGroup` (
    `EmailReceiverGroupId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `GroupName` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `IsActived` INTEGER(11), 
    `CreatedBy` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `UpdatedBy` INTEGER(11), 
    `UpdatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`EmailReceiverGroupId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `UserGroup` (
    `UserGroupId` INTEGER(11) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `RootId` INTEGER(11) UNSIGNED NOT NULL DEFAULT '0', 
    `ParentId` INTEGER(11) UNSIGNED NOT NULL DEFAULT '0', 
    `Name` VARCHAR(128) CHARACTER SET utf8 NOT NULL, 
    `Lft` INTEGER(11) UNSIGNED NOT NULL DEFAULT '1', 
    `Rgt` INTEGER(11) UNSIGNED NOT NULL DEFAULT '2', 
    `Level` INTEGER(11) DEFAULT '0', 
    `Description` TEXT CHARACTER SET utf8, 
    `CheckedOutBy` INTEGER(11) UNSIGNED NOT NULL DEFAULT '0', 
    `CheckedOutAt` INTEGER(11), 
    `DftGuest` INTEGER(11) DEFAULT '0', 
    PRIMARY KEY (`UserGroupId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `Org` (
    `OrgId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `OrgCode` VARCHAR(200) COLLATE utf8mb4_unicode_ci NOT NULL, 
    `OrgName` VARCHAR(200) COLLATE utf8mb4_unicode_ci NOT NULL, 
    `CompanyId` INTEGER(10) UNSIGNED NOT NULL, 
    `ParentId` INTEGER(11) NOT NULL DEFAULT '0', 
    `DefaultBranchId` INTEGER(10) UNSIGNED, 
    `NumAnnualLeaveTraining` INTEGER(5) NOT NULL, 
    `IsViewAllBranch` INTEGER(1) NOT NULL, 
    `IsTimekeeping` INTEGER(1) NOT NULL, 
    `IsActive` INTEGER(1) NOT NULL, 
    `PosLeft` INTEGER(5) NOT NULL DEFAULT '0', 
    `PosRight` INTEGER(5) NOT NULL DEFAULT '0', 
    `RoleCode` VARCHAR(32) COLLATE utf8mb4_unicode_ci, 
    `CreatedDate` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    `CreatedStaffId` INTEGER(11) UNSIGNED NOT NULL DEFAULT '0', 
    `UpdatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `UpdatedStaffId` INTEGER(11) UNSIGNED DEFAULT '0', 
    `ParentDeleteOrgId` INTEGER(11), 
    `Level` INTEGER(11), 
    `BranchId` INTEGER(11), 
    `IsSolvingTicket` SMALLINT(2), 
    PRIMARY KEY (`OrgId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `AbsenceRequestChangeHistory` (
    `AbsenceRequestChangeHistoryId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `AbsenceRequestId` INTEGER(11) NOT NULL, 
    `Note` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `AbsenceFrom` DATETIME, 
    `AbsenceTo` DATETIME, 
    `CreatedBy` INTEGER(11), 
    `CreatedDate` DATETIME, 
    PRIMARY KEY (`AbsenceRequestChangeHistoryId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `IncomeTypeLevelHistory` (
    `Id` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `IncomeTypeLevelId` INTEGER(11), 
    `IncomeTypeId` INTEGER(11), 
    `Name` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `IsDeleted` INTEGER(11), 
    `IncomePerHour` DECIMAL(10, 2), 
    `IsIncomeByService` INTEGER(11), 
    `IsIncomeByServiceQuality` INTEGER(11), 
    `CreatedDate` DATETIME, 
    `CreatedBy` INTEGER(11), 
    `TrackingDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`Id`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `StaffSalaryTaxSettlement` (
    `StaffSalaryTaxSettlementId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `TaxNumber` VARCHAR(45) COLLATE utf8mb4_unicode_ci COMMENT 'M├ú sß╗æ thuß║┐', 
    `StaffId` INTEGER(11), 
    `StaffCode` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'm├ú nh├ón vi├¬n', 
    `FullName` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'hß╗ì t├¬n', 
    `Company` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'c├┤ng ty', 
    `Branch` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'chi nh├ính', 
    `WorkPosition` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'chß╗⌐c danh', 
    `StartDate` DATETIME COMMENT 'ng├áy bß║»t ─æß║ºu', 
    `EndDate` DATETIME COMMENT 'ng├áy nghß╗ë viß╗çc', 
    `MaternityLeave` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'nghß╗ë thai sß║ún', 
    `WorkContractType` VARCHAR(45) COLLATE utf8mb4_unicode_ci COMMENT 'loß║íi hß╗úp ─æß╗ông', 
    `IdentityNumber` VARCHAR(45) COLLATE utf8mb4_unicode_ci COMMENT 'cccd', 
    `WorkedMonths` INTEGER(3) COMMENT 'sß╗æ th├íng l├ám viß╗çc', 
    `Authority` VARCHAR(60) COLLATE utf8mb4_unicode_ci COMMENT 'ß╗ºy quyß╗ün', 
    `TotalTaxableIncome` DECIMAL(12, 2) COMMENT 'tß╗òng thu nhß║¡p chß╗ïu thuß║┐', 
    `TotalTaxDeducted` DECIMAL(12, 2) COMMENT 'tß╗òng tiß╗ün thuß║┐ ─æ├ú khß║Ñu trß╗½', 
    `IncomeOutsideOfSalary` DECIMAL(12, 2) COMMENT 'thu nhß║¡p ngo├ái bß║úng l╞░╞íng', 
    `TaxCollectionOutsideSalary` DECIMAL(12, 2) COMMENT 'thu thuß║┐ ngo├ái bß║úng l╞░╞íng 10%', 
    `TaxableIncome` DECIMAL(12, 2) COMMENT 'thu nhß║¡p chß╗ïu thuß║┐', 
    `SocialInsuranceDeduction` DECIMAL(12, 2) COMMENT 'giß║úm trß╗½ bhxh', 
    `SelfDeduction` DECIMAL(12, 2) COMMENT 'giß║úm trß╗½ bß║ún th├ón', 
    `Dependents` DECIMAL(5, 2) COMMENT 'sß╗æ ng╞░ß╗¥i phß╗Ñ thuß╗Öc', 
    `NPTDeduction` DECIMAL(12, 2) COMMENT 'giß║úm trß╗½ npt', 
    `TotalFamilyDeduction` DECIMAL(12, 2) COMMENT 'giß║úm trß╗½ gia cß║únh', 
    `AssessableIncome` DECIMAL(12, 2) COMMENT 'thu nhß║¡p t├¡nh thuß║┐', 
    `PersonalIncomeTaxDeduction` DECIMAL(12, 2) COMMENT 'thuß║┐ tncn ─æ├ú khß║Ñu trß╗½', 
    `AverageTaxableIncome` DECIMAL(12, 2) COMMENT 'B├¼nh qu├ón TN t├¡nh thuß║┐', 
    `PersonalIncomeTax` DECIMAL(12, 2) COMMENT 'Sß╗æ thuß║┐ TN phß║úi ─æ├│ng
', 
    `Arrears(Payable&Collected)` DECIMAL(12, 2) COMMENT 'Truy thu (phß║úi nß╗Öp - ─æ├ú thu)
', 
    `TaxRefund(Collected&Payable)` DECIMAL(12, 2) COMMENT 'Ho├án thuß║┐ (─æ├ú thu-phß║úi nß╗Öp)
', 
    `TaxableIncome(12/22)` DECIMAL(12, 2) COMMENT 'Thu nhß║¡p chß╗ïu thuß║┐ 12/22
', 
    `AssessableIncome(12/22)` DECIMAL(12, 2) COMMENT 'TN t├¡nh thuß║┐ 12/22
', 
    `TaxDeducted(12/22)` DECIMAL(12, 2) COMMENT 'Thuß║┐ ─æ├ú khß║Ñu trß╗½ 12/22
', 
    `TaxableIncome1` DECIMAL(12, 2) COMMENT 'Thu nhß║¡p chß╗ïu thuß║┐ 1
', 
    `AssessableIncome1` DECIMAL(12, 2) COMMENT 'TN t├¡nh thuß║┐ 1
', 
    `TaxDeducted1` DECIMAL(12, 2) COMMENT 'Thuß║┐ ─æ├ú khß║Ñu trß╗½ 1
', 
    `TaxableIncome2` DECIMAL(12, 2) COMMENT 'Thu nhß║¡p chß╗ïu thuß║┐ 2
', 
    `AssessableIncome2` DECIMAL(12, 2) COMMENT 'TN t├¡nh thuß║┐ 2
', 
    `TaxDeducted2` DECIMAL(12, 2) COMMENT 'Thuß║┐ ─æ├ú khß║Ñu trß╗½ 2
', 
    `TaxableIncome3` DECIMAL(12, 2) COMMENT 'Thu nhß║¡p chß╗ïu thuß║┐ 3
', 
    `AssessableIncome3` DECIMAL(12, 2) COMMENT 'TN t├¡nh thuß║┐ 3
', 
    `TaxDeducted3` DECIMAL(12, 2) COMMENT 'Thuß║┐ ─æ├ú khß║Ñu trß╗½ 3
', 
    `TaxableIncome4` DECIMAL(12, 2) COMMENT 'Thu nhß║¡p chß╗ïu thuß║┐ 4', 
    `AssessableIncome4` DECIMAL(12, 2) COMMENT 'TN t├¡nh thuß║┐ 4', 
    `TaxDeducted4` DECIMAL(12, 2) COMMENT 'Thuß║┐ ─æ├ú khß║Ñu trß╗½ 4', 
    `TaxableIncome5` DECIMAL(12, 2) COMMENT 'Thu nhß║¡p chß╗ïu thuß║┐ 5', 
    `AssessableIncome5` DECIMAL(12, 2) COMMENT 'TN t├¡nh thuß║┐ 5', 
    `TaxDeducted5` DECIMAL(12, 2) COMMENT 'Thuß║┐ ─æ├ú khß║Ñu trß╗½ 5', 
    `TaxableIncome6` DECIMAL(12, 2) COMMENT 'Thu nhß║¡p chß╗ïu thuß║┐ 6', 
    `AssessableIncome6` DECIMAL(12, 2) COMMENT 'TN t├¡nh thuß║┐ 6', 
    `TaxDeducted6` DECIMAL(12, 2) COMMENT 'Thuß║┐ ─æ├ú khß║Ñu trß╗½ 6', 
    `TaxableIncome7` DECIMAL(12, 2) COMMENT 'Thu nhß║¡p chß╗ïu thuß║┐ 7', 
    `AssessableIncome7` DECIMAL(12, 2) COMMENT 'TN t├¡nh thuß║┐ 7', 
    `TaxDeducted7` DECIMAL(12, 2) COMMENT 'Thuß║┐ ─æ├ú khß║Ñu trß╗½ 7', 
    `TaxableIncome8` DECIMAL(12, 2) COMMENT 'Thu nhß║¡p chß╗ïu thuß║┐ 8', 
    `AssessableIncome8` DECIMAL(12, 2) COMMENT 'TN t├¡nh thuß║┐ 8', 
    `TaxDeducted8` DECIMAL(12, 2) COMMENT 'Thuß║┐ ─æ├ú khß║Ñu trß╗½ 8', 
    `TaxableIncome9` DECIMAL(12, 2) COMMENT 'Thu nhß║¡p chß╗ïu thuß║┐ 9', 
    `AssessableIncome9` DECIMAL(12, 2) COMMENT 'TN t├¡nh thuß║┐ 9', 
    `TaxDeducted9` DECIMAL(12, 2) COMMENT 'Thuß║┐ ─æ├ú khß║Ñu trß╗½ 9', 
    `TaxableIncome10` DECIMAL(12, 2) COMMENT 'Thu nhß║¡p chß╗ïu thuß║┐ 10', 
    `AssessableIncome10` DECIMAL(12, 2) COMMENT 'TN t├¡nh thuß║┐ 10', 
    `TaxDeducted10` DECIMAL(12, 2) COMMENT 'Thuß║┐ ─æ├ú khß║Ñu trß╗½ 10', 
    `TaxableIncome11` DECIMAL(12, 2) COMMENT 'Thu nhß║¡p chß╗ïu thuß║┐ 11', 
    `AssessableIncome11` DECIMAL(12, 2) COMMENT 'TN t├¡nh thuß║┐ 11', 
    `TaxDeducted11` DECIMAL(12, 2) COMMENT 'Thuß║┐ ─æ├ú khß║Ñu trß╗½ 11', 
    `Note` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'Ghi ch├║
', 
    `Tax` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 't├¡nh thuß║┐
', 
    `TaxCollection` INTEGER(11) COMMENT 'thu thuß║┐
', 
    `Empty1` INTEGER(11), 
    `Empty2` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    `WorkedAtNKKMonths` VARCHAR(45) COLLATE utf8mb4_unicode_ci COMMENT 'Sß╗æ th├íng l├ám NNK
', 
    `WorkedAtRHMMonths` VARCHAR(45) COLLATE utf8mb4_unicode_ci COMMENT 'Sß╗æ th├íng l├ám ß╗ƒ RHM
', 
    `12/2022` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    `January` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    `February` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    `March` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    `April` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    `May` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    `June` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    `July` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    `August` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    `September` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    `October` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    `November` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    PRIMARY KEY (`StaffSalaryTaxSettlementId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `NotificationLike` (
    `NotificationLikeId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `NotificationId` INTEGER(11), 
    `StaffId` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`NotificationLikeId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `PermissionWorkProfilePosition` (
    `PermissionWorkProfilePositionId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `WorkProfilePositionId` INTEGER(11) NOT NULL, 
    `PermissionCode` VARCHAR(128) NOT NULL, 
    `Filter` VARCHAR(128) NOT NULL COMMENT 'None: Lß║Ñy data theo tß║Ñt cß║ú chi nh├ính | IP: Lß║Ñy data theo IP cß╗ºa chi nh├ính | OrgChart: Lß║Ñy data c├íc chi nh├ính theo OrgChart | KimCompanyGroup: Lß║Ñy danh s├ích data theo c├íc c├┤ng ty cß╗ºa KIM ─æ╞░ß╗úc cß║Ñu h├¼nh trong ParamConfig' DEFAULT 'None', 
    `ActionValue` VARCHAR(256), 
    `Priority` INTEGER(10) UNSIGNED DEFAULT '1', 
    `IsActive` INTEGER(11) DEFAULT '1', 
    `UpdatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `UpdatedBy` INTEGER(11), 
    PRIMARY KEY (`PermissionWorkProfilePositionId`)
)DEFAULT CHARSET=latin1 ENGINE=InnoDB;

CREATE UNIQUE INDEX `idx_WorkProfilePositionId_PermissionCode` ON `PermissionWorkProfilePosition` (`WorkProfilePositionId`, `PermissionCode`);

CREATE TABLE `StaffInterviewType` (
    `StaffInterviewTypeId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `StaffInterviewId` INTEGER(10) UNSIGNED NOT NULL, 
    `InterviewType` TINYINT(1) COMMENT 'H├¼nh th?c ph?ng v?n - 1: Online, 2: T?i NKK, 3: Ngo├ái NKK', 
    `InterviewPlace` VARCHAR(1000) CHARACTER SET utf8mb4 COMMENT '??a ?i?m / link ph?ng v?n, N?u InterviewType = 2 l?u OrgId', 
    PRIMARY KEY (`StaffInterviewTypeId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `IX_StaffInterviewId` ON `StaffInterviewType` (`StaffInterviewId`);

CREATE TABLE `StaffLeaveTransaction` (
    `StaffLeaveTransactionId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `TransactionDate` DATETIME, 
    `TransactionTypeId` TINYINT(4) COMMENT '1: deposit, 2: withdrawal', 
    `AbsenceTypeId` INTEGER(11), 
    `AbsenceRequestId` INTEGER(11), 
    `LeaveDays` DECIMAL(5, 1), 
    `Note` VARCHAR(2000) COLLATE utf8mb4_unicode_ci, 
    `StaffId` INTEGER(11), 
    `CreatedBy` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`StaffLeaveTransactionId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `idx_StaffId` ON `StaffLeaveTransaction` (`StaffId`, `CreatedDate`);

CREATE TABLE `ExtensionHistory` (
    `ExtensionId` INTEGER(11) UNSIGNED NOT NULL, 
    `AppId` INTEGER(11) UNSIGNED NOT NULL, 
    `Type` VARCHAR(50) CHARACTER SET utf8 NOT NULL COMMENT 'Module
Widget
Theme
Plugin
', 
    `Dir` VARCHAR(128) CHARACTER SET utf8 NOT NULL, 
    `Name` VARCHAR(128) CHARACTER SET utf8 NOT NULL, 
    `Author` VARCHAR(128) CHARACTER SET utf8, 
    `VersionCode` VARCHAR(32) CHARACTER SET utf8 NOT NULL, 
    `VersionName` VARCHAR(32) CHARACTER SET utf8 NOT NULL, 
    `Description` TEXT CHARACTER SET utf8, 
    `Config` TEXT CHARACTER SET utf8, 
    `AutoUpdate` TINYINT(1) DEFAULT '0', 
    `AutoUpdateLink` VARCHAR(196) CHARACTER SET utf8, 
    `AddedAt` INTEGER(11) NOT NULL, 
    PRIMARY KEY (`ExtensionId`, `AppId`, `AddedAt`), 
    CONSTRAINT `fk_ExtensionHistory_Extension1` FOREIGN KEY(`ExtensionId`, `AppId`) REFERENCES `Extension` (`ExtensionId`, `AppId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_ExtensionHistory_Extension_idx` ON `ExtensionHistory` (`ExtensionId`, `AppId`);

CREATE TABLE `WorkContractAnnex` (
    `WorkContractAnnexId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `WorkContractId` INTEGER(11), 
    `Code` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    `SignedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `SignedBy` INTEGER(11), 
    `ExpiredDate` DATETIME, 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    `WorkContractScheduleId` INTEGER(11), 
    `AvailableDate` DATETIME, 
    `DepartmentId` INTEGER(11), 
    `TeamId` INTEGER(11), 
    `WorkPosition` INTEGER(11), 
    `WorkTimeMode` VARCHAR(20) COLLATE utf8mb4_unicode_ci, 
    `SalaryAmount` DECIMAL(18, 2), 
    `SocialInsuranceSalary` DECIMAL(18, 2), 
    `AdditionalSalaryAmount` DECIMAL(18, 2), 
    `WorkPositionNote` VARCHAR(128) COLLATE utf8mb4_unicode_ci, 
    `StaffLevelId` INTEGER(11), 
    `WorkProfilePositionId` INTEGER(11), 
    `UpdatedDate` DATETIME, 
    `UpdatedBy` INTEGER(11), 
    `SyncDate` DATETIME, 
    `Type` TINYINT(4), 
    `IsCurrent` TINYINT(4) DEFAULT '0', 
    PRIMARY KEY (`WorkContractAnnexId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `IX_WorkContractAnnex_WorkContractId` ON `WorkContractAnnex` (`WorkContractId`);

CREATE TABLE `Certificate` (
    `CertificateId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `CertificateGroupId` INTEGER(10) UNSIGNED NOT NULL, 
    `VerifiedType` TINYINT(1) UNSIGNED COMMENT 'Loß║íi thß║⌐m ─æß╗ïnh: 1 - Tß║íi NKK, 2 - Ngo├ái NKK, 3 - ─É─âng k├╜ tß║íi NKK, 4- Ch╞░a ─æ─âng k├╜' DEFAULT '0', 
    `Name` VARCHAR(128) CHARACTER SET utf8mb4, 
    `CertificateSuggestionId` INTEGER(10) UNSIGNED DEFAULT '0', 
    `Note` TEXT CHARACTER SET utf8mb4, 
    `Type` TINYINT(1) UNSIGNED COMMENT 'Ph├ón loß║íi: 1 - ─É├ú c├│ chß╗⌐ng chß╗ë, 2: Chuß║⌐n bß╗ï c├│ chß╗⌐ng chß╗ë' DEFAULT '0', 
    `AttachFile` VARCHAR(128) CHARACTER SET utf8mb4, 
    `IssueDate` DATE, 
    `ExpiryDate` DATE, 
    `EstimatedIssueDate` DATE COMMENT 'Ng├áy chuß║⌐n bß╗ï c├│ chß╗⌐ng chß╗ë', 
    `VerifiedDate` DATE COMMENT 'Ng├áy thß║⌐m ─æß╗ïnh', 
    `StaffId` INTEGER(10) UNSIGNED NOT NULL, 
    `CreatedBy` INTEGER(10) UNSIGNED, 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `UpdatedBy` INTEGER(10) UNSIGNED, 
    `UpdatedDate` DATETIME, 
    `ScheduleRegister` TEXT COLLATE utf8mb4_unicode_ci, 
    `RegistrationDate` DATETIME, 
    `BranchId` INTEGER(11), 
    `IsDeleted` INTEGER(11) DEFAULT '0', 
    `CertificateNumber` VARCHAR(1024) COLLATE utf8mb4_unicode_ci, 
    `IssuedBy` VARCHAR(1024) COLLATE utf8mb4_unicode_ci, 
    `RegisterAt` VARCHAR(1024) COLLATE utf8mb4_unicode_ci, 
    PRIMARY KEY (`CertificateId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_Certificate_Staff_idx` ON `Certificate` (`StaffId`);

CREATE INDEX `fk_Certificate_CertificateGroup_idx` ON `Certificate` (`CertificateGroupId`);

CREATE TABLE `CertificateSuggestion` (
    `CertificateSuggestionId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `CertificateGroupId` INTEGER(11), 
    `Code` VARCHAR(20) COLLATE utf8mb4_unicode_ci, 
    `Name` VARCHAR(128) COLLATE utf8mb4_unicode_ci, 
    `SuggestionType` TINYINT(1) UNSIGNED COMMENT 'Ph├ón loß║íi: 0 - Tß║Ñt cß║ú, 1 - ─É├ú c├│ chß╗⌐ng chß╗ë, 2: Chuß║⌐n bß╗ï c├│ chß╗⌐ng chß╗ë' DEFAULT '0', 
    `IsDeleted` TINYINT(1) UNSIGNED DEFAULT '0', 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`CertificateSuggestionId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `WorkingReport` (
    `WorkingReportId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `StaffId` INTEGER(10) UNSIGNED NOT NULL, 
    `WorkProfileId` INTEGER(10) UNSIGNED NOT NULL, 
    `Year` INTEGER(4) NOT NULL, 
    `Month` INTEGER(2) UNSIGNED NOT NULL, 
    `Day` INTEGER(2) UNSIGNED NOT NULL, 
    `ActualWorkingHours` DECIMAL(4, 2) NOT NULL COMMENT 'sß╗æ giß╗¥ thß╗▒c l├ám ─æ╞░ß╗úc t├¡nh theo thao t├íc chß║Ñm c├┤ng', 
    `ScheduleWorkingHours` DECIMAL(4, 2) NOT NULL COMMENT 'sß╗æ giß╗¥ l├ám t├¡nh theo lß╗ïch c├┤ng viß╗çc cß╗ºa nh├ón vi├¬n', 
    `AdminExecuteId` INTEGER(10) UNSIGNED NOT NULL, 
    PRIMARY KEY (`WorkingReportId`)
)COMMENT='Nß║┐u l├ám ca: lß║Ñy sß╗æ lß║ºn check ─æß║ºu ti├¬n t╞░╞íng ß╗⌐ng vß╗¢i sß╗æ ca trong ng├áy

Nß║┐u l├ám fulltime: lß║Ñy lß║ºn check-in ─æß║ºu ti├¬n v├á lß║ºn check-out cuß╗æi c├╣ng' DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_WorkingReport_WorkProfile_idx` ON `WorkingReport` (`WorkProfileId`);

CREATE INDEX `fk_WorkingReport_Staff_idx` ON `WorkingReport` (`StaffId`);

CREATE INDEX `fk_WorkingReport_AdminExecute_idx` ON `WorkingReport` (`AdminExecuteId`);

CREATE TABLE `RelationshipGroup` (
    `RelationshipGroupId` INTEGER(10) UNSIGNED NOT NULL COMMENT 'Gia ?├¼nh
C├╣ng c├┤ng ty
B?n b├¿' AUTO_INCREMENT, 
    `Name` VARCHAR(64) COLLATE utf8mb4_unicode_ci, 
    `Ordering` INTEGER(10) UNSIGNED DEFAULT '0', 
    PRIMARY KEY (`RelationshipGroupId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `TeamLeader` (
    `TeamId` INTEGER(10) UNSIGNED NOT NULL, 
    `WorkProfileId` INTEGER(10) UNSIGNED NOT NULL, 
    `StaffId` INTEGER(10) UNSIGNED NOT NULL, 
    `Title` VARCHAR(64) CHARACTER SET utf8mb4, 
    `FromDate` DATE NOT NULL, 
    `ToDate` DATE, 
    `IsCurrentManager` INTEGER(1) UNSIGNED NOT NULL DEFAULT '1'
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_TeamLeader_WorkProfile_idx` ON `TeamLeader` (`WorkProfileId`, `StaffId`);

CREATE INDEX `fk_TeamLeader_Team_idx` ON `TeamLeader` (`TeamId`);

CREATE TABLE `TrainingEventParticipant` (
    `TrainingEventParticipantId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `TrainingEventId` INTEGER(11), 
    `StaffId` INTEGER(11), 
    `State` INTEGER(11), 
    `CreatedDate` DATETIME, 
    `CreatedBy` INTEGER(11), 
    `UpdatedDate` DATETIME, 
    `UpdatedBy` INTEGER(11), 
    `CheckIn` INTEGER(11), 
    `CheckInDate` DATETIME, 
    PRIMARY KEY (`TrainingEventParticipantId`), 
    CONSTRAINT `fk_TrainingEventId` FOREIGN KEY(`TrainingEventId`) REFERENCES `TrainingEvent` (`TrainingEventId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_TrainingEventId_idx` ON `TrainingEventParticipant` (`TrainingEventId`);

CREATE TABLE `DocsAndForms` (
    `DocsAndFormsId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `DocsAndFormsName` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `DocsAndFormsLink` VARCHAR(1000) COLLATE utf8mb4_unicode_ci, 
    `Status` INTEGER(11), 
    `CreatedBy` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `UpdatedBy` INTEGER(11), 
    `UpdatedDate` DATETIME, 
    PRIMARY KEY (`DocsAndFormsId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `SalaryAllowances` (
    `SalaryAllowancesId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `ObjectSourceType` VARCHAR(45) COLLATE utf8mb4_unicode_ci COMMENT 'WorkContract, WorkContractAnnex', 
    `ObjectSourceId` INTEGER(11), 
    `SalaryAllowancesTypeId` INTEGER(11), 
    `SalaryAllowancesTypeNote` VARCHAR(256) COLLATE utf8mb4_unicode_ci, 
    `Amount` DECIMAL(18, 2), 
    `IsDeleted` SMALLINT(6) DEFAULT '0', 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    `StaffId` INTEGER(11), 
    PRIMARY KEY (`SalaryAllowancesId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `ScoreCriterion` (
    `ScoreCriterionId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `Code` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    `Name` VARCHAR(512) COLLATE utf8mb4_unicode_ci, 
    `Description` VARCHAR(8000) COLLATE utf8mb4_unicode_ci, 
    `ScoreCriterionCategoryId` INTEGER(11), 
    `DefaultScore` TINYINT(4) DEFAULT '0', 
    `Type` TINYINT(4) COMMENT '1 Text
2 Meida' DEFAULT '0', 
    `IsDeleted` TINYINT(4) DEFAULT '0', 
    `Priority` INTEGER(11) DEFAULT '0', 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    `UpdatedDate` DATETIME, 
    `UpdatedBy` INTEGER(11), 
    PRIMARY KEY (`ScoreCriterionId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `ResponsiblePersion` (
    `ResponsiblePersionId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `FullName` VARCHAR(64) CHARACTER SET latin1 NOT NULL, 
    `PhoneNumber` VARCHAR(16) CHARACTER SET latin1 NOT NULL, 
    `StaffId` INTEGER(10) UNSIGNED NOT NULL, 
    PRIMARY KEY (`ResponsiblePersionId`), 
    CONSTRAINT `fk_ResponsiblePersion_Staff` FOREIGN KEY(`StaffId`) REFERENCES `Staff` (`StaffId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_ResponsiblePersion_Staff_idx` ON `ResponsiblePersion` (`StaffId`);

CREATE TABLE `MenuItemViewing` (
    `MenuItemId` INTEGER(11) UNSIGNED NOT NULL, 
    `ViewingId` INTEGER(11) UNSIGNED NOT NULL, 
    CONSTRAINT `fk_MenuItemViewing_MenuItem` FOREIGN KEY(`MenuItemId`) REFERENCES `MenuItem` (`MenuItemId`), 
    CONSTRAINT `fk_MenuItemViewing_Viewing` FOREIGN KEY(`ViewingId`) REFERENCES `Viewing` (`ViewingId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_MenuItemViewing_ViewingId_idx` ON `MenuItemViewing` (`ViewingId`);

CREATE INDEX `fk_MenuItemViewing_MenuItemId_idx` ON `MenuItemViewing` (`MenuItemId`);

CREATE TABLE `StaffDocument` (
    `StaffDocumentId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `StaffId` INTEGER(11), 
    `DocumentType` INTEGER(11) COMMENT '1) PersonalIncomeTax', 
    `Name` VARCHAR(2024) COLLATE utf8mb4_unicode_ci, 
    `CDNURL` VARCHAR(2048) COLLATE utf8mb4_unicode_ci, 
    `Priority` INTEGER(11) DEFAULT '0', 
    `State` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    PRIMARY KEY (`StaffDocumentId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `ScoreCampaignImpact` (
    `ScoreCampaignImpactId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `ScoreCampaignId` INTEGER(11), 
    `Code` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    `Name` VARCHAR(512) COLLATE utf8mb4_unicode_ci, 
    `ActionByObject` INTEGER(11) COMMENT '1 Org\\n2 Staff', 
    `ActionById` INTEGER(11), 
    `ApplyToObject` TINYINT(4) COMMENT '1 nguoi ch?m\\n2 l├á ???c ch?m' DEFAULT '0', 
    `ApplyToId` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    `UpdatedDate` DATETIME, 
    `UpdatedBy` INTEGER(11), 
    PRIMARY KEY (`ScoreCampaignImpactId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `TimeKeepingRequestStatusTracking` (
    `TimeKeepingRequestStatusTrackingId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `TimeKeepingRequestId` INTEGER(11) NOT NULL, 
    `Status` TINYINT(4) NOT NULL, 
    `StatusNote` VARCHAR(200) COLLATE utf8mb4_unicode_ci, 
    `CreatedBy` INTEGER(11) NOT NULL, 
    `CreatedDate` DATETIME NOT NULL, 
    PRIMARY KEY (`TimeKeepingRequestStatusTrackingId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `IX_TimeKeepingRequestStatusTracking_Id` ON `TimeKeepingRequestStatusTracking` (`TimeKeepingRequestId`);

CREATE TABLE `MaritalStatus` (
    `MaritalStatusId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `Name` VARCHAR(50) COLLATE utf8mb4_bin NOT NULL, 
    `Ordering` INTEGER(1) NOT NULL DEFAULT '0', 
    PRIMARY KEY (`MaritalStatusId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_bin;

CREATE TABLE `Holiday` (
    `Date` DATE NOT NULL, 
    `Name` VARCHAR(100) COLLATE utf8mb4_unicode_ci, 
    `IsHoliday` TINYINT(4) COMMENT '\\n=1 l├á ng├áy l? th?c\\n\\n0 l├á r?i v├áo cu?i tu?n, m├¼nh b? ra khi t├¡nh l??ng, Dung de tinh cong chuan nen neu ngay le trung thu 7 cn khong duoc bat len la 1', 
    `Description` VARCHAR(200) CHARACTER SET utf8mb4, 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`Date`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `ScoreCard` (
    `ScoreCardId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `ScoreCampaignId` INTEGER(11), 
    `Status` INTEGER(11) COMMENT '1 New
2 Working
3 Completed', 
    `ActionDate` DATETIME, 
    `DueDate` DATETIME, 
    `ActionByObject` INTEGER(11) COMMENT '1 Org, 
2 Staff', 
    `ActionBy` INTEGER(11), 
    `ApplyToObject` INTEGER(11) COMMENT '1 Org, 
2 Staff', 
    `ApplyToId` INTEGER(11), 
    `TotalScore` TINYINT(4) DEFAULT '0', 
    `ScoreAchieved` INTEGER(11), 
    `IsIncludeSubNode` TINYINT(4) DEFAULT '0', 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    `UpdatedDate` DATETIME, 
    `UpdatedBy` INTEGER(11), 
    `CompletedByStaff` INTEGER(11), 
    `CompletedDate` DATETIME, 
    PRIMARY KEY (`ScoreCardId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `HiringRequirement` (
    `HiringRequirementId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `DepartmentId` INTEGER(10) UNSIGNED, 
    `WorkProfilePositionId` INTEGER(10) UNSIGNED, 
    `RequiredDate` DATE, 
    `ExpiredDate` DATE, 
    `TotalRequirement` INTEGER(10) UNSIGNED COMMENT 'S? l??ng y├¬u c?u t?ng c?ng', 
    `ObtainingRequirement` INTEGER(10) UNSIGNED COMMENT 'S? l??ng y├¬u c?u ??t ???c', 
    `Description` VARCHAR(1000) CHARACTER SET utf8mb4, 
    `Status` TINYINT(2) UNSIGNED COMMENT 'Tr?ng th├íi', 
    `StatusNote` VARCHAR(1000) CHARACTER SET utf8mb4, 
    `CreatedBy` INTEGER(10) UNSIGNED, 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `UpdatedBy` INTEGER(10) UNSIGNED, 
    `UpdatedDate` DATETIME, 
    PRIMARY KEY (`HiringRequirementId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `IX_RequiredDate` ON `HiringRequirement` (`RequiredDate`);

CREATE TABLE `BranchManager` (
    `BranchId` INTEGER(10) UNSIGNED NOT NULL, 
    `WorkProfileId` INTEGER(10) UNSIGNED NOT NULL, 
    `StaffId` INTEGER(10) UNSIGNED NOT NULL, 
    `Title` VARCHAR(128) CHARACTER SET utf8mb4, 
    `FromDate` DATE NOT NULL, 
    `ToDate` DATE, 
    `IsCurrentManager` INTEGER(1) UNSIGNED NOT NULL DEFAULT '1', 
    CONSTRAINT fk_branch_manager FOREIGN KEY(`BranchId`) REFERENCES `Branch` (`BranchId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_BranchManager_WorkProfile_idx` ON `BranchManager` (`WorkProfileId`, `StaffId`);

CREATE INDEX `fk_BranchManager_Branch_idx` ON `BranchManager` (`BranchId`);

CREATE TABLE `StaffSignatureTracking` (
    `StaffSignaturetTrackingId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `StaffId` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `UpdatedBy` INTEGER(11), 
    `UpdatedDate` DATETIME, 
    `SignatureType` INTEGER(11) COMMENT '0: update 1: enable signature 2: disable signature', 
    PRIMARY KEY (`StaffSignaturetTrackingId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `StaffModifyTracking` (
    `StaffModifyTrackingId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `AbsenceRequestId` INTEGER(11), 
    `StaffId` INTEGER(11), 
    `ModifyType` INTEGER(11) COMMENT '1) Th?i gian nghi viec
2) Thai S?n
', 
    `Note` VARCHAR(2000) COLLATE utf8mb4_unicode_ci, 
    `OldJsonData` VARCHAR(4000) COLLATE utf8mb4_unicode_ci, 
    `CreatedBy` INTEGER(11), 
    `CreatedDate` DATETIME, 
    PRIMARY KEY (`StaffModifyTrackingId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `idx_StaffId` ON `StaffModifyTracking` (`StaffId`);

CREATE TABLE `ContactPoint` (
    `ContactPointId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `Desc` TEXT COLLATE utf8mb4_unicode_ci, 
    `State` INTEGER(1) UNSIGNED NOT NULL DEFAULT '1', 
    `CompanyId` INTEGER(10) UNSIGNED NOT NULL, 
    `DepartmentId` INTEGER(10) UNSIGNED NOT NULL, 
    `TeamId` INTEGER(10) UNSIGNED NOT NULL, 
    `BranchId` INTEGER(10) UNSIGNED NOT NULL, 
    PRIMARY KEY (`ContactPointId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `InfrequentIncludeWorkShift` (
    `InfrequentIncludeWorkShiftId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `WorkScheduleId` INTEGER(10) UNSIGNED NOT NULL, 
    `Date` DATE NOT NULL, 
    `WorkShiftId` INTEGER(10) UNSIGNED NOT NULL, 
    `BranchId` INTEGER(10) UNSIGNED NOT NULL, 
    `AddedAt` INTEGER(10) UNSIGNED NOT NULL, 
    `AddedBy` INTEGER(10) UNSIGNED NOT NULL, 
    PRIMARY KEY (`InfrequentIncludeWorkShiftId`), 
    CONSTRAINT `fk_InfrequentIncludeWorkShift_AddedBy` FOREIGN KEY(`AddedBy`) REFERENCES `User` (`UserId`), 
    CONSTRAINT `fk_InfrequentIncludeWorkShift_WorkSchedule` FOREIGN KEY(`WorkScheduleId`) REFERENCES `WorkSchedule` (`WorkScheduleId`), 
    CONSTRAINT `fk_InfrequentIncludeWorkShift_WorkShift` FOREIGN KEY(`WorkShiftId`) REFERENCES `WorkShift` (`WorkShiftId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_InfrequentIncludeWorkShift_WorkShift_idx` ON `InfrequentIncludeWorkShift` (`WorkShiftId`);

CREATE INDEX `fk_InfrequentIncludeWorkShift_WorkSchedule_idx` ON `InfrequentIncludeWorkShift` (`WorkScheduleId`);

CREATE INDEX `fk_InfrequentIncludeWorkShift_WorkLocation_idx` ON `InfrequentIncludeWorkShift` (`BranchId`);

CREATE INDEX `fk_InfrequentIncludeWorkShift_AddedBy_idx` ON `InfrequentIncludeWorkShift` (`AddedBy`);

CREATE INDEX `IX_InfrequentIncludeWorkShift_Date` ON `InfrequentIncludeWorkShift` (`Date`, `WorkScheduleId`);

CREATE TABLE `Contact` (
    `ContactId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `Email` VARCHAR(64) COLLATE utf8mb4_unicode_ci, 
    `Phone` VARCHAR(30) COLLATE utf8mb4_unicode_ci, 
    `Desc` TEXT COLLATE utf8mb4_unicode_ci, 
    `State` INTEGER(1) UNSIGNED NOT NULL DEFAULT '1', 
    `ContactPointId` INTEGER(10) UNSIGNED NOT NULL, 
    PRIMARY KEY (`ContactId`), 
    CONSTRAINT `fk_Contact_ContactPoint1` FOREIGN KEY(`ContactPointId`) REFERENCES `ContactPoint` (`ContactPointId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_Contact_ContactPoint_idx` ON `Contact` (`ContactPointId`);

CREATE TABLE `AppViewing` (
    `AppId` INTEGER(11) UNSIGNED NOT NULL, 
    `ViewingId` INTEGER(11) UNSIGNED NOT NULL, 
    CONSTRAINT `fk_AppViewing_App` FOREIGN KEY(`AppId`) REFERENCES `App` (`AppId`), 
    CONSTRAINT `fk_AppViewing_Viewing` FOREIGN KEY(`ViewingId`) REFERENCES `Viewing` (`ViewingId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_AppViewing_ViewingId_idx` ON `AppViewing` (`ViewingId`);

CREATE INDEX `fk_AppViewing_AppId_idx` ON `AppViewing` (`AppId`);

CREATE TABLE `StaffAddress` (
    `StaffAddressId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `Address` VARCHAR(196) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL, 
    `ProvinceId` INTEGER(10) UNSIGNED NOT NULL, 
    `DistrictId` INTEGER(10) UNSIGNED, 
    `WardId` INTEGER(10) UNSIGNED, 
    `AddedAt` INTEGER(10) UNSIGNED NOT NULL, 
    `AddressTypeId` INTEGER(10) UNSIGNED NOT NULL, 
    `StaffId` INTEGER(10) UNSIGNED NOT NULL, 
    PRIMARY KEY (`StaffAddressId`), 
    CONSTRAINT `fk_StaffAddress_AddressType` FOREIGN KEY(`AddressTypeId`) REFERENCES `AddressType` (`AddressTypeId`), 
    CONSTRAINT `fk_StaffAddress_District` FOREIGN KEY(`DistrictId`) REFERENCES `VnDistrict` (`VnDistrictId`), 
    CONSTRAINT `fk_StaffAddress_Province` FOREIGN KEY(`ProvinceId`) REFERENCES `VnProvince` (`VnProvinceId`), 
    CONSTRAINT `fk_StaffAddress_Staff` FOREIGN KEY(`StaffId`) REFERENCES `Staff` (`StaffId`), 
    CONSTRAINT `fk_StaffAddress_Ward` FOREIGN KEY(`WardId`) REFERENCES `VnWard` (`VnWardId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_StaffAddress_Ward_idx` ON `StaffAddress` (`WardId`);

CREATE INDEX `fk_StaffAddress_Staff_idx` ON `StaffAddress` (`StaffId`);

CREATE INDEX `fk_StaffAddress_Province_idx` ON `StaffAddress` (`ProvinceId`);

CREATE INDEX `fk_StaffAddress_District_idx` ON `StaffAddress` (`DistrictId`);

CREATE INDEX `fk_StaffAddress_AddressType_idx` ON `StaffAddress` (`AddressTypeId`);

CREATE TABLE `VnWard` (
    `VnWardId` INTEGER(10) UNSIGNED NOT NULL, 
    `VnDistrictId` INTEGER(10) UNSIGNED NOT NULL, 
    `WardCode` VARCHAR(8) CHARACTER SET utf8mb4, 
    `WardPostalCode` VARCHAR(8) CHARACTER SET utf8mb4, 
    `NameVi` VARCHAR(64) CHARACTER SET utf8mb4 NOT NULL, 
    `NameEn` VARCHAR(64) CHARACTER SET utf8mb4, 
    `LabelVi` VARCHAR(32) CHARACTER SET utf8mb4 NOT NULL COMMENT 'Ph??ng
X├ú
Th? tr?n', 
    `LabelEn` VARCHAR(32) CHARACTER SET utf8mb4 COMMENT 'Commune
Ward
Township', 
    `Ordering` INTEGER(10) UNSIGNED, 
    `isDeleted` TINYINT(4), 
    `State` INTEGER(11) DEFAULT '1', 
    PRIMARY KEY (`VnWardId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_VnWard_VnDistrict_idx` ON `VnWard` (`VnDistrictId`);

CREATE TABLE `ValidProcessedTimeRecorder` (
    `WorkingReportId` INTEGER(10) UNSIGNED NOT NULL, 
    `CheckInAt` INTEGER(11), 
    `CheckOutAt` INTEGER(11), 
    `TimeKeeperId` INTEGER(10) UNSIGNED NOT NULL, 
    `CheckInLocationId` INTEGER(10) UNSIGNED NOT NULL, 
    `CheckOutLocationId` INTEGER(10) UNSIGNED NOT NULL, 
    `TotalBreakTimeInMinute` INTEGER(11) NOT NULL, 
    `IsCheckinValid` INTEGER(10) UNSIGNED NOT NULL DEFAULT '1', 
    `InvalidCheckinMessage` VARCHAR(64) COLLATE utf8mb4_unicode_ci, 
    `IsCheckoutValid` INTEGER(10) UNSIGNED NOT NULL DEFAULT '1', 
    `InvalidCheckoutMessage` VARCHAR(64) COLLATE utf8mb4_unicode_ci, 
    `ValidCheckInTime` TIME, 
    `ValidCheckOutTime` TIME, 
    `IsShiftRecorder` INTEGER(1) NOT NULL COMMENT 'ch?m c├┤ng theo workshift hay kh├┤ng' DEFAULT '0', 
    `WorkShiftName` VARCHAR(32) COLLATE utf8mb4_unicode_ci COMMENT 't├¬n workshift l?y t? b?ng workshift. ?? ph├▓ng t├¼nh hu?ng thay ??i t├¬n workshift th├¼ t├¬n c? ?├ú ???c l?u l?i ? ?├óy', 
    `WorkingDayEquality` DECIMAL(4, 2) NOT NULL, 
    CONSTRAINT `fk_ValidTimeRecorder_TimeKeeper` FOREIGN KEY(`TimeKeeperId`) REFERENCES `TimeKeeper` (`TimeKeeperId`), 
    CONSTRAINT `fk_ValidTimeRecorder_WorkingReport` FOREIGN KEY(`WorkingReportId`) REFERENCES `WorkingReport` (`WorkingReportId`)
)COMMENT='b?ng l?u d? li?u c├íc record ch?m c├┤ng ???c r├║t' DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_ValidTimeRecorder_WorkingReport_idx` ON `ValidProcessedTimeRecorder` (`WorkingReportId`);

CREATE INDEX `fk_ValidTimeRecorder_TimeKeeper_idx` ON `ValidProcessedTimeRecorder` (`TimeKeeperId`);

CREATE TABLE `OrgManagerResp` (
    `OrgId` INTEGER(10) UNSIGNED NOT NULL, 
    `WorkProfileId` INTEGER(10) UNSIGNED NOT NULL, 
    `RespOrgId` INTEGER(10) UNSIGNED NOT NULL, 
    `CreatedDate` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    `CreatedStaffId` INTEGER(10) UNSIGNED NOT NULL DEFAULT '0', 
    `UpdatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `UpdatedStaffId` INTEGER(10) UNSIGNED DEFAULT '0', 
    PRIMARY KEY (`OrgId`, `WorkProfileId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `RolePermission` (
    `RolePermissionId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `RoleId` INTEGER(11) NOT NULL, 
    `PermissionId` INTEGER(11) NOT NULL, 
    `Filter` VARCHAR(128) COLLATE utf8mb4_unicode_ci DEFAULT 'None', 
    `ActionValue` VARCHAR(128) COLLATE utf8mb4_unicode_ci DEFAULT '100000', 
    `Priority` TINYINT(4) DEFAULT '1', 
    `State` TINYINT(4) NOT NULL DEFAULT '1', 
    `CreatedBy` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`RolePermissionId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `EmailStaffSignature` (
    `EmailStaffSignatureId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `StaffId` INTEGER(11), 
    `Signature` TEXT COLLATE utf8mb4_unicode_ci, 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`EmailStaffSignatureId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `ActivityTrackingSystem` (
    `Id` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `URLPath` VARCHAR(256) COLLATE utf8mb4_unicode_ci, 
    `UserId` INTEGER(11), 
    `StaffId` INTEGER(11), 
    `IPAddress` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    `AgentInfo` VARCHAR(1024) COLLATE utf8mb4_unicode_ci, 
    `TrackingTime` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `Note` LONGTEXT COLLATE utf8mb4_unicode_ci, 
    `WorkProfilePositionId` INTEGER(11), 
    `TypePermission` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    PRIMARY KEY (`Id`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `Idx_StaffId` ON `ActivityTrackingSystem` (`StaffId`);

CREATE TABLE `District` (
    `DistrictId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `DistrictName` VARCHAR(100) COLLATE utf8mb4_unicode_ci, 
    `Label` VARCHAR(20) COLLATE utf8mb4_unicode_ci, 
    `ProvinceId` INTEGER(10) UNSIGNED, 
    `State` TINYINT(1) DEFAULT '1', 
    `VnDistrictId` INTEGER(11), 
    PRIMARY KEY (`DistrictId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `TrainingEvent` (
    `TrainingEventId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `EventName` VARCHAR(510) COLLATE utf8mb4_unicode_ci COMMENT 'T├¬n sß╗▒ kiß╗çn', 
    `EventLocation` INTEGER(11) COMMENT 'Khu vß╗▒c tß╗ò chß╗⌐c sß╗▒ kiß╗çn', 
    `StartDate` DATETIME, 
    `EndDate` DATETIME, 
    `EventLevel` INTEGER(11) COMMENT '1: PK, 10: Khu vß╗▒c; 20: To├án hß╗ç thß╗æng', 
    `Attendee` VARCHAR(510) COLLATE utf8mb4_unicode_ci COMMENT '─Éß╗æi t╞░ß╗úng tham gia', 
    `Content` LONGTEXT COLLATE utf8mb4_unicode_ci COMMENT 'Nß╗Öi dung', 
    `State` TINYINT(4) COMMENT '0: deleted, 1: active' DEFAULT '1', 
    `CreatedBy` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `UpdatedBy` INTEGER(11), 
    `UpdatedDate` DATETIME, 
    `OtherLocation` VARCHAR(45) COLLATE utf8mb4_unicode_ci COMMENT 'Khu vß╗▒c kh├íc', 
    `QuantityOfParticipants` INTEGER(11) COMMENT 'Sß╗æ l╞░ß╗úng ng╞░ß╗¥i ─æ─âng k├╜' DEFAULT '0', 
    `QuantityOfSubscribers` INTEGER(11) COMMENT 'sß╗æ l╞░╞íng ng╞░ß╗¥i tham gia' DEFAULT '0', 
    `Room` VARCHAR(510) COLLATE utf8mb4_unicode_ci, 
    PRIMARY KEY (`TrainingEventId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `Extension` (
    `ExtensionId` INTEGER(11) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `AppId` INTEGER(11) UNSIGNED NOT NULL, 
    `Type` VARCHAR(50) CHARACTER SET utf8 NOT NULL COMMENT 'Module
Widget
Theme
Plugin
', 
    `Dir` VARCHAR(32) CHARACTER SET utf8 NOT NULL, 
    `Name` VARCHAR(128) CHARACTER SET utf8 NOT NULL, 
    `IsGlobal` INTEGER(1) DEFAULT '0', 
    `Author` VARCHAR(128) CHARACTER SET utf8, 
    `VersionCode` VARCHAR(32) CHARACTER SET utf8 NOT NULL, 
    `VersionName` VARCHAR(32) CHARACTER SET utf8 NOT NULL, 
    `Description` TEXT CHARACTER SET utf8, 
    `Config` TEXT CHARACTER SET utf8, 
    `AutoUpdate` INTEGER(1) DEFAULT '0', 
    `AutoUpdateUrl` VARCHAR(196) CHARACTER SET utf8, 
    PRIMARY KEY (`ExtensionId`, `AppId`), 
    CONSTRAINT `fk_Extension_App` FOREIGN KEY(`AppId`) REFERENCES `App` (`AppId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_Extension_App_idx` ON `Extension` (`AppId`);

CREATE TABLE `Module` (
    `ModuleId` INTEGER(11) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `ExtensionId` INTEGER(11) UNSIGNED NOT NULL, 
    `AppId` INTEGER(11) UNSIGNED NOT NULL, 
    `Name` VARCHAR(128) CHARACTER SET utf8 NOT NULL, 
    `Dir` VARCHAR(32) CHARACTER SET utf8 NOT NULL, 
    `State` INTEGER(1) DEFAULT '1', 
    `Config` TEXT CHARACTER SET utf8, 
    PRIMARY KEY (`ModuleId`), 
    CONSTRAINT `fk_Module_Extension` FOREIGN KEY(`ExtensionId`, `AppId`) REFERENCES `Extension` (`ExtensionId`, `AppId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_Module_Extension_idx` ON `Module` (`ExtensionId`, `AppId`);

CREATE TABLE `WorkShift` (
    `WorkShiftId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `Name` VARCHAR(32) CHARACTER SET utf8mb4 NOT NULL, 
    `ShortName` VARCHAR(20) CHARACTER SET utf8mb4 NOT NULL, 
    `RGBColor` VARCHAR(6) CHARACTER SET utf8mb4 NOT NULL, 
    `Ordering` INTEGER(2) UNSIGNED NOT NULL DEFAULT '0', 
    `StartTime` TIME COMMENT 'Giß╗¥ bß║»t ─æß║ºu ca l├ám viß╗çc', 
    `EndTime` TIME COMMENT 'giß╗¥ kß║┐t th├║c ca l├ám viß╗çc', 
    `TotalBreakTimeInMinute` INTEGER(10) UNSIGNED NOT NULL, 
    `WorkingDayEquality` DECIMAL(4, 2) UNSIGNED, 
    `State` INTEGER(11), 
    PRIMARY KEY (`WorkShiftId`)
)COMMENT='ca l├ám viß╗çc' DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `VnDistrict` (
    `VnDistrictId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `VnProvinceId` INTEGER(10) UNSIGNED NOT NULL, 
    `DistrictCode` VARCHAR(8) CHARACTER SET utf8mb4, 
    `DistrictPostalCode` VARCHAR(8) CHARACTER SET utf8mb4, 
    `NameVi` VARCHAR(64) CHARACTER SET utf8mb4 NOT NULL, 
    `NameEn` VARCHAR(64) CHARACTER SET utf8mb4, 
    `LabelVi` VARCHAR(32) CHARACTER SET utf8mb4 NOT NULL COMMENT 'Qu?n
Th? x├ú
Huy?n
Th├ánh ph?', 
    `LabelEn` VARCHAR(32) CHARACTER SET utf8mb4 COMMENT 'Urban District
Town
Rural District
Provincial City', 
    `Ordering` INTEGER(10) UNSIGNED, 
    `isDeleted` TINYINT(4), 
    `State` INTEGER(11) DEFAULT '1', 
    PRIMARY KEY (`VnDistrictId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_VnDistrict_VnProvince_idx` ON `VnDistrict` (`VnProvinceId`);

CREATE TABLE `StaffAcademicLevel` (
    `StaffAcademicLevelId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `StaffId` INTEGER(11), 
    `DegreeId` INTEGER(11), 
    `IsDeleted` INTEGER(11) DEFAULT '0', 
    `SchoolName` VARCHAR(128) COLLATE utf8mb4_unicode_ci, 
    `Majors` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `FromDate` DATE, 
    `ToDate` DATE, 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    PRIMARY KEY (`StaffAcademicLevelId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `IX_StaffAcademicLevel_StaffId` ON `StaffAcademicLevel` (`StaffId`);

CREATE TABLE `EmailSenderGroupPermission` (
    `EmailSenderGroupPermissionId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `EmailReceiverGroupId` INTEGER(11), 
    `StaffId` INTEGER(11), 
    `IsActive` INTEGER(11), 
    `CreatedBy` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`EmailSenderGroupPermissionId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `IncomeBaseClosedOfMonth` (
    `IncomeBaseClosedOfMonthId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `ClosedTime` DATE, 
    `StaffId` INTEGER(11), 
    `WorkHours` DECIMAL(10, 2), 
    `IncomePerHour` DECIMAL(10, 2), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    PRIMARY KEY (`IncomeBaseClosedOfMonthId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `StaffGroup` (
    `StaffGroupId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `CompanyId` INTEGER(10) UNSIGNED NOT NULL, 
    `NameVi` VARCHAR(32) CHARACTER SET utf8mb4 NOT NULL, 
    `NameEn` VARCHAR(32) CHARACTER SET utf8mb4 NOT NULL, 
    `Ordering` INTEGER(10) UNSIGNED DEFAULT '0', 
    `RootId` INTEGER(10) UNSIGNED NOT NULL, 
    `ParentId` INTEGER(10) UNSIGNED NOT NULL, 
    `Lft` INTEGER(10) UNSIGNED NOT NULL, 
    `Rgt` INTEGER(10) UNSIGNED NOT NULL, 
    `Level` INTEGER(10) UNSIGNED NOT NULL, 
    PRIMARY KEY (`StaffGroupId`)
)COMMENT='gom c?m c├íc nh├│m ng??i d├╣ng theo t├¡nh n?ng thao t├íc h? th?ng. V├¡ d?: b├íc s?, l? t├ón, nh├ón vi├¬n tuy?n d?ng, nh├ón vi├¬n nh├ón s?...' DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_StaffGroup_Root_idx` ON `StaffGroup` (`RootId`);

CREATE INDEX `fk_StaffGroup_Parent_idx` ON `StaffGroup` (`ParentId`);

CREATE INDEX `fk_StaffGroup_Company_idx` ON `StaffGroup` (`CompanyId`);

CREATE TABLE `StaffSalaryDetailsTracking` (
    `StaffSalaryDetailsTrackingId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `TotalImport` INTEGER(11), 
    `TotalSucceed` INTEGER(11), 
    `TotalError` INTEGER(11), 
    `FilePath` VARCHAR(250) COLLATE utf8mb4_unicode_ci, 
    `ExportPath` VARCHAR(250) COLLATE utf8mb4_unicode_ci, 
    `PayPeriod` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    `CreatedDate` DATETIME, 
    `CreatedBy` INTEGER(11), 
    PRIMARY KEY (`StaffSalaryDetailsTrackingId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `NotificationReadInfo` (
    `NotificationReadInfoId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `NoticationId` INTEGER(11), 
    `StaffId` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`NotificationReadInfoId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `TrainingEventCheckInTracking` (
    `TrainingEventCheckInTrackingId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `TrainingEventId` INTEGER(11), 
    `StaffId` INTEGER(11), 
    `CreatedBy` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `isCheckIn` INTEGER(11) COMMENT '0 is checkout & 1 is checkin' DEFAULT '0', 
    PRIMARY KEY (`TrainingEventCheckInTrackingId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `TimeKeepingRequestDetail` (
    `TimeKeepingRequestDetailId` INTEGER(11) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `TimeKeepingRequestId` INTEGER(11) NOT NULL, 
    `RequestedTime` DATETIME NOT NULL, 
    `RequestedDate` DATE, 
    `OldTime` DATETIME, 
    `Type` TINYINT(4) NOT NULL, 
    `WorkShiftId` INTEGER(11), 
    `TimeKeeperId` INTEGER(11) UNSIGNED, 
    `TimeKeeperChangingId` INTEGER(11), 
    `WorkScheduleId` INTEGER(11) UNSIGNED, 
    `CreatedDate` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11) NOT NULL, 
    `UpdatedDate` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    `UpdatedBy` INTEGER(11), 
    `ApprovedTime` DATETIME, 
    PRIMARY KEY (`TimeKeepingRequestDetailId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `IX_TimeKeepingRequestDetail_TimeKeepingRequestId` ON `TimeKeepingRequestDetail` (`TimeKeepingRequestId`);

CREATE TABLE `Ethnic` (
    `EthnicId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `Name` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `Description` VARCHAR(512) COLLATE utf8mb4_unicode_ci, 
    `Priority` INTEGER(11), 
    `State` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`EthnicId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `WorkContractSchedule` (
    `WorkContractScheduleId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `Name` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    `Priority` INTEGER(11), 
    `IsDeleted` SMALLINT(6), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    `Level` VARCHAR(25) COLLATE utf8mb4_unicode_ci, 
    PRIMARY KEY (`WorkContractScheduleId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `OrgBranch` (
    `OrgId` INTEGER(10) UNSIGNED, 
    `BranchId` INTEGER(10), 
    `IsVirtual` INTEGER(1) NOT NULL DEFAULT '1', 
    `CreatedDate` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    `CreatedStaffId` INTEGER(10) UNSIGNED NOT NULL DEFAULT '0', 
    `UpdatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `UpdatedStaffId` INTEGER(10) UNSIGNED DEFAULT '0', 
    `OrgBranchId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    PRIMARY KEY (`OrgBranchId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE UNIQUE INDEX `uq_Branch_Org` ON `OrgBranch` (`BranchId`, `OrgId`);

CREATE TABLE `TaskAssignUser` (
    `TaskId` INTEGER(10) UNSIGNED NOT NULL, 
    `AssignedAt` INTEGER(10) UNSIGNED NOT NULL, 
    `AssignedBy` INTEGER(10) UNSIGNED NOT NULL, 
    `AssignedTo` INTEGER(10) UNSIGNED NOT NULL, 
    CONSTRAINT `fk_TaskAssignUser_AssignedBy` FOREIGN KEY(`AssignedBy`) REFERENCES `User` (`UserId`), 
    CONSTRAINT `fk_TaskAssignUser_AssignedTo` FOREIGN KEY(`AssignedTo`) REFERENCES `User` (`UserId`), 
    CONSTRAINT `fk_TaskAssignUser_Task` FOREIGN KEY(`TaskId`) REFERENCES `Task` (`TaskId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_TaskAssignUser_Task_idx` ON `TaskAssignUser` (`TaskId`);

CREATE INDEX `fk_TaskAssignUser_AssignedTo_idx` ON `TaskAssignUser` (`AssignedTo`);

CREATE INDEX `fk_TaskAssignUser_AssignedBy_idx` ON `TaskAssignUser` (`AssignedBy`);

CREATE TABLE `AAAAA1111` (
    `StaffSalaryDetailsId` INTEGER(11), 
    `StaffId` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `FullName` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `CompanyId` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `WorkProfilePositionId` VARCHAR(100) COLLATE utf8mb4_unicode_ci, 
    `ContractType` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `BranchId` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `StartDate` DOUBLE(10, 3), 
    `Shift` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Total` INTEGER(11), 
    `NoTimekeeping` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Actual Hours Worked` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `AnnualLeave` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `PaidLeave` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `PublicHolidaysLeave` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `TotalStandardHours` DOUBLE(10, 3), 
    `StandardWage` INTEGER(11), 
    `BasicSalary` INTEGER(11), 
    `PerformanceBonus` INTEGER(11), 
    `LunchAllowance` INTEGER(11), 
    `UniformAllowance` INTEGER(11), 
    `TotalIncomeWorkingDays` INTEGER(11), 
    `CRM/CSBonus` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `ServiceQualityBonus` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `GeneralManagermentBonus` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `EfficiencyManagementBonus` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `EbitdaBonus` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `VinmecBonus` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `SecurityBonus` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `HolidayBonus` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `TotalBonus` INTEGER(11), 
    `ParkingTravelAllowance` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `ProfessionalCertificateAllowance` INTEGER(11), 
    `OtherAllowances` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `TotalAllowances` INTEGER(11), 
    `OtherDeductions` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `TotalIncomeBeforeTax` INTEGER(11), 
    `ParticipatingSalaryInSocialInsurance` INTEGER(11), 
    `PersonalHealthInsurance` INTEGER(11), 
    `PersonalSocialInsurance` INTEGER(11), 
    `PersonalUnemploymentInsurance` INTEGER(11), 
    `EmployeeSocialInsurance` INTEGER(11), 
    `EmployeeUnionFee` INTEGER(11), 
    `CompanySocialInsurance` INTEGER(11), 
    `CompanyOccupaitionalAccidentOrDisease` INTEGER(11), 
    `CompanyHealthInsurance` INTEGER(11), 
    `CompanyUnemploymentInsurance` INTEGER(11), 
    `EnterpriseSocialInsurance` INTEGER(11), 
    `EnterpriseUnionFee` INTEGER(11), 
    `LunchOrUniformAllowanceNoTax` INTEGER(11), 
    `TotalTaxableIncome` INTEGER(11), 
    `TaxableIncomeObject` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Commitment` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Dependents` INTEGER(11), 
    `TotalAssessableIncome` INTEGER(11), 
    `PersonalIncomeTaxCollection` INTEGER(11), 
    `ActualPayment` INTEGER(11), 
    `CompanyPaysSocialInsurance` INTEGER(11), 
    `WithholdSocialInsurance` INTEGER(11), 
    `BankTransfer` INTEGER(11), 
    `Name` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `AccountNumber` DOUBLE(15, 3), 
    `Bank` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Email` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `TransferAmount` INTEGER(11), 
    `Additional` INTEGER(11), 
    `Notes` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `PaymentDate` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Level` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `SalaryPerHour` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `CompensatoryLeave` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `TotalLunchAllowance` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `FixedIncomeWithLunchAllowance` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `FixedIncomeAmountWithLunchAllowance` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `TaskBonus` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `ClinicsAchievingKPIRevenueBonus` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `AssistantManagerAndConcurrentBonus` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `GuaranteedIncomeAllowance` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `DentalTour` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `WarehouseAllowance` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `OtherTotalIncome` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `CertificateAllowance` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `DoctorBonus` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `AdjustmentForDecemberShortfall` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `PayPeriod` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Template` VARCHAR(50) COLLATE utf8mb4_unicode_ci
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `UserUserGroup` (
    `UserGroupId` INTEGER(11) UNSIGNED NOT NULL, 
    `UserId` INTEGER(11) UNSIGNED NOT NULL, 
    CONSTRAINT `fk_UserUserGroup_Group` FOREIGN KEY(`UserGroupId`) REFERENCES `UserGroup` (`UserGroupId`), 
    CONSTRAINT `fk_UserUserGroup_User` FOREIGN KEY(`UserId`) REFERENCES `User` (`UserId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_UserUserGroup_User_idx` ON `UserUserGroup` (`UserId`);

CREATE INDEX `fk_UserUserGroup_UserGroup_idx` ON `UserUserGroup` (`UserGroupId`);

CREATE TABLE `WorkContractType` (
    `WorkContractTypeId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `Name` VARCHAR(128) CHARACTER SET utf8mb4 NOT NULL, 
    `Description` TEXT CHARACTER SET utf8mb4, 
    `State` TINYINT(4), 
    `Group` INTEGER(11), 
    `IsEndTime` TINYINT(4), 
    PRIMARY KEY (`WorkContractTypeId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `BranchPhoneExtension` (
    `BranchPhoneExtensionId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `BranchId` INTEGER(11), 
    `PhoneExtension` INTEGER(11), 
    `Status` INTEGER(11) COMMENT '0 InActive
1 Active', 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`BranchPhoneExtensionId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `UserRaw` (
    `UserId` INTEGER(11) NOT NULL, 
    `Email` VARCHAR(128) CHARACTER SET utf8mb4 NOT NULL, 
    `Password` VARCHAR(256) COLLATE utf8mb4_unicode_ci NOT NULL, 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `UpdatedDate` DATETIME, 
    PRIMARY KEY (`UserId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `Email` (
    `EmailId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `Subject` VARCHAR(2048) COLLATE utf8mb4_unicode_ci, 
    `SenderStaffId` INTEGER(11), 
    `ShortContent` VARCHAR(2048) COLLATE utf8mb4_unicode_ci, 
    `Priority` INTEGER(11) COMMENT '1 normal
2 Hight' DEFAULT '1', 
    `Status` INTEGER(11) COMMENT '1 Draff
2 Sent
3 Hidden', 
    `IsAttachFile` TINYINT(2), 
    `PrimaryEmailId` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    `UpdatedDate` DATETIME, 
    `UpdatedBy` INTEGER(11), 
    PRIMARY KEY (`EmailId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `WorkLocationStaff` (
    `StaffId` INTEGER(10) UNSIGNED NOT NULL, 
    `WorkProfileId` INTEGER(10) UNSIGNED NOT NULL, 
    `WorkLocationId` INTEGER(10) UNSIGNED NOT NULL, 
    CONSTRAINT `fk_WorkLocationStaff_Staff` FOREIGN KEY(`StaffId`) REFERENCES `Staff` (`StaffId`), 
    CONSTRAINT `fk_WorkLocationStaff_WorkLocation` FOREIGN KEY(`WorkLocationId`) REFERENCES `WorkLocation` (`WorkLocationId`), 
    CONSTRAINT `fk_WorkLocationStaff_WorkProfile` FOREIGN KEY(`WorkProfileId`) REFERENCES `WorkProfile` (`WorkProfileId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_WorkLocationStaff_WorkProfile_idx` ON `WorkLocationStaff` (`WorkProfileId`);

CREATE INDEX `fk_WorkLocationStaff_WorkLocation_idx` ON `WorkLocationStaff` (`WorkLocationId`);

CREATE INDEX `fk_WorkLocationStaff_Staff_idx` ON `WorkLocationStaff` (`StaffId`);

CREATE TABLE `DepartmentManager` (
    `DepartmentId` INTEGER(10) UNSIGNED NOT NULL, 
    `WorkProfileId` INTEGER(10) UNSIGNED NOT NULL, 
    `StaffId` INTEGER(10) UNSIGNED NOT NULL, 
    `Title` VARCHAR(64) CHARACTER SET utf8mb4, 
    `FromDate` DATE NOT NULL, 
    `ToDate` DATE, 
    `IsCurrentManager` INTEGER(1) UNSIGNED NOT NULL DEFAULT '1', 
    CONSTRAINT fk_department_manager FOREIGN KEY(`DepartmentId`) REFERENCES `Department` (`DepartmentId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_DepartmentManager_WorkProfile_idx` ON `DepartmentManager` (`WorkProfileId`, `StaffId`);

CREATE INDEX `fk_DepartmentManager_Department_idx` ON `DepartmentManager` (`DepartmentId`);

CREATE TABLE `StaffPhone` (
    `StaffPhoneId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `PhoneNumber` VARCHAR(16) CHARACTER SET utf8mb4 NOT NULL, 
    `Label` VARCHAR(16) CHARACTER SET utf8mb4 DEFAULT 'Work', 
    `IsPrimary` INTEGER(1) NOT NULL, 
    `StaffId` INTEGER(10) UNSIGNED NOT NULL, 
    PRIMARY KEY (`StaffPhoneId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `idx_PhoneNumber` ON `StaffPhone` (`PhoneNumber`);

CREATE INDEX `fk_StaffPhone_Staff_idx` ON `StaffPhone` (`StaffId`);

CREATE TABLE `WorkSchedule` (
    `WorkScheduleId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `StaffId` INTEGER(10) UNSIGNED NOT NULL, 
    `WorkProfileId` INTEGER(10) UNSIGNED, 
    `StartDate` DATE COMMENT 'lß╗ïch n├áy ├íp dß╗Ñng tß╗½ ng├áy n├áo', 
    `EndDate` DATE COMMENT 'lß╗ïch n├áy ├íp dß╗Ñng ─æß║┐n ng├áy n├áo', 
    `Count` INTEGER(10) UNSIGNED DEFAULT '0', 
    `Frequency` INTEGER(10) UNSIGNED, 
    `Interval` INTEGER(10) UNSIGNED, 
    `ByWeekDay` INTEGER(1) UNSIGNED COMMENT 'ByWeekDay, ByMonthDay, ByMonth l├á c├íc field d├╣ng ─æß╗â control viß╗çc set lß╗ïch theo kiß╗âu n├áo.
Trong mß╗Öt d├▓ng chß╗ë c├│ 1 trong sß╗æ 3 field n├áy mang gi├í trß╗ï 1. C├▓n lß║íi 2 c├íi kia mang gi├í trß╗ï 0.
(xem lß║íi t├¼nh huß╗æng l├ám viß╗çc theo th├íng nh╞░ng chß╗ë mß╗Öt sß╗æ ng├áy nhß║Ñt ─æß╗ïnh - kß║┐t hß╗úp ng├áy tuß║ºn hoß║╖c ng├áy th├íng)
' DEFAULT '0', 
    `ByMonthDay` INTEGER(1) UNSIGNED COMMENT 'ByWeekDay, ByMonthDay, ByMonth l├á c├íc field d├╣ng ─æß╗â control viß╗çc set lß╗ïch theo kiß╗âu n├áo.Trong mß╗Öt d├▓ng chß╗ë c├│ 1 trong sß╗æ 3 field n├áy mang gi├í trß╗ï 1. C├▓n lß║íi 2 c├íi kia mang gi├í trß╗ï 0.(xem lß║íi t├¼nh huß╗æng l├ám viß╗çc theo th├íng nh╞░ng chß╗ë mß╗Öt sß╗æ ng├áy nhß║Ñt ─æß╗ïnh - kß║┐t hß╗úp ng├áy tuß║ºn hoß║╖c ng├áy th├íng)' DEFAULT '0', 
    `ExceptMonths` VARCHAR(128) CHARACTER SET utf8mb4 COMMENT 'l╞░u c├íc th├íng loß║íi trß╗½ theo ─æß╗ïnh dß║íng json, v├¡ dß╗Ñ [''2018/07'',''2018/08'',''2018/09'']', 
    `ExceptDates` VARCHAR(128) CHARACTER SET utf8mb4 COMMENT 'l╞░u c├íc ng├áy loß║íi trß╗½ theo ─æß╗ïnh dß║íng json, v├¡ dß╗Ñ [''2018/07/30'',''2018/08/30'',''2018/09/30'']', 
    `ByWorkShift` INTEGER(1) NOT NULL DEFAULT '0', 
    `Trashed` INTEGER(1) NOT NULL DEFAULT '0', 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `Migrate` INTEGER(11), 
    `OldEndDate` DATE, 
    PRIMARY KEY (`WorkScheduleId`), 
    CONSTRAINT `fk_WorkSchedule_Staff` FOREIGN KEY(`StaffId`) REFERENCES `Staff` (`StaffId`), 
    CONSTRAINT `fk_WorkSchedule_WorkProfile` FOREIGN KEY(`WorkProfileId`) REFERENCES `WorkProfile` (`WorkProfileId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_WorkSchedule_WorkProfile_idx` ON `WorkSchedule` (`WorkProfileId`);

CREATE INDEX `fk_WorkSchedule_Staff_idx` ON `WorkSchedule` (`StaffId`);

CREATE TABLE `MonthlyBonusImportDetail` (
    `Id` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `MonthlyBonusImportId` INTEGER(11), 
    `MonthSalaryPeriod` DATE, 
    `StaffCode` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    `Amount` DECIMAL(18, 2), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    PRIMARY KEY (`Id`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `IX_MonthlyBonusImportId` ON `MonthlyBonusImportDetail` (`MonthlyBonusImportId`);

CREATE TABLE `RentalContractType` (
    `RentalContractTypeId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `Name` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL, 
    `Code` VARCHAR(25) COLLATE utf8mb4_unicode_ci, 
    `Priority` TINYINT(4) DEFAULT '0', 
    `IsDelete` TINYINT(4) DEFAULT '0', 
    PRIMARY KEY (`RentalContractTypeId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `RentalContract` (
    `RentalContractId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `RentalContractTypeId` INTEGER(11) NOT NULL, 
    `Name` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL, 
    `Code` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `Representative` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `BranchId` INTEGER(11), 
    `SignedDate` DATE, 
    `FromDate` DATE, 
    `ToDate` DATE, 
    `TerminationDate` DATE, 
    `TerminationReason` TEXT COLLATE utf8mb4_unicode_ci, 
    `ProcessContent` TEXT COLLATE utf8mb4_unicode_ci, 
    `IsTermination` TINYINT(4) DEFAULT '0', 
    `IsProcessed` TINYINT(4) DEFAULT '0', 
    `IsAlert` TINYINT(4) DEFAULT '1', 
    `State` INTEGER(11) COMMENT '1: active, 0: expired' DEFAULT '1', 
    `AlertType` VARCHAR(255) COLLATE utf8mb4_unicode_ci DEFAULT 'Day', 
    `AlertBeforeTime` INTEGER(11) DEFAULT '0', 
    `PartnerCompany` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `PartnerAddress` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `PartnerRepresentative` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `PartnerEmail` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `PartnerPhone` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Comment` TEXT COLLATE utf8mb4_unicode_ci, 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    `UpdatedDate` DATETIME, 
    `UpdatedBy` INTEGER(11), 
    PRIMARY KEY (`RentalContractId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `StaffSalaryDetails_bk` (
    `StaffSalaryDetailsId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `StaffId` INTEGER(11), 
    `StaffCode` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `FullName` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'hß╗ì t├¬n', 
    `Company` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'C├┤ng ty', 
    `WorkProfilePosition` VARCHAR(100) COLLATE utf8mb4_unicode_ci COMMENT 'Chß╗⌐c danh', 
    `ContractType` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'Loß║íi hß╗úp ─æß╗ông', 
    `Branch` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'Chi nh├ính', 
    `StartDate` DATETIME, 
    `Shift` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'ca l├ám viß╗çc', 
    `Total` INTEGER(11) COMMENT 'Tß╗òng cß╗Öng', 
    `NoTimekeeping` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'ko chß║Ñm c├┤ng', 
    `ActualHoursWorked` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'sß╗æ giß╗¥ lv thß╗▒c tß║┐ HIS', 
    `AnnualLeave` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'nghß╗ë ph├⌐p', 
    `PaidLeave` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'nghß╗ë chß║┐ ─æß╗Ö', 
    `PublicHolidaysLeave` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'nghß╗ë lß╗à/tß║┐t', 
    `TotalStandardHours` DOUBLE(10, 3) COMMENT 'tß╗òng c├┤ng t├¡nh l╞░╞íng', 
    `StandardWage` INTEGER(11) COMMENT 'c├┤ng chuß║⌐n', 
    `BasicSalary` INTEGER(11) COMMENT 'l╞░╞íng c╞í bß║ún', 
    `PerformanceBonus` INTEGER(11) COMMENT 'Th╞░ß╗ƒng ├¥ thß╗⌐c v├á Tu├ón thß╗º/Th╞░ß╗ƒng Hiß╗çß╗Ñ quß║ú hoß║ít ─æß╗Öng', 
    `LunchAllowance` INTEGER(11) COMMENT 'Phß╗Ñ cß║Ñp c╞ím tr╞░a', 
    `UniformAllowance` INTEGER(11) COMMENT 'Phß╗Ñ cß║Ñp ─æß╗ông phß╗Ñc', 
    `TotalIncomeWorkingDays` INTEGER(11) COMMENT 'Tß╗òng thu nhß║¡p theo ng├áy c├┤ng', 
    `CRM/CSBonus` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'Th╞░ß╗ƒng CRM/CS (C.Mai)', 
    `ServiceQualityBonus` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'Th╞░ß╗ƒng CLDV', 
    `GeneralManagermentBonus` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'Th╞░ß╗ƒng quß║ún l├╜ chung', 
    `EfficiencyManagementBonus` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'Th╞░ß╗ƒng hiß╗çu quß║ú quß║ún l├╜', 
    `EbitdaBonus` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'Th╞░ß╗ƒng Ebitda', 
    `VinmecBonus` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'th╞░ß╗ƒng vinmec', 
    `SecurityBonus` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'th╞░ß╗ƒng an ninh', 
    `HolidayBonus` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'th╞░ß╗ƒng lß╗à/tß║┐t', 
    `TotalBonus` DECIMAL(12, 2) COMMENT 'tß╗òng th╞░ß╗ƒng', 
    `ParkingTravelAllowance` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'PC gß╗¡i xe/c├┤ng t├íc', 
    `ProfessionalCertificateAllowance` INTEGER(11) COMMENT 'Phß╗Ñ cß║Ñp chß╗⌐ng chß╗ë h├ánh nghß╗ü', 
    `OtherAllowances` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'phß╗Ñ cß║Ñp kh├íc', 
    `TotalAllowances` INTEGER(11) COMMENT 'Tß╗òng phß╗Ñ cß║Ñp', 
    `OtherDeductions` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'trß╗½ kh├íc', 
    `TotalIncomeBeforeTax` INTEGER(11) COMMENT 'tß╗òng thu nhß║¡p tr╞░ß╗¢c thuß║┐', 
    `ParticipatingSalaryInSocialInsurance` INTEGER(11) COMMENT 'Mß╗⌐c l╞░╞íng tham gia BHXH', 
    `PersonalHealthInsurance` INTEGER(11) COMMENT 'BHYT 1,5%', 
    `PersonalSocialInsurance` INTEGER(11) COMMENT 'BHXH 8%', 
    `PersonalUnemploymentInsurance` INTEGER(11) COMMENT 'BHTN 1%', 
    `EmployeeSocialInsurance` INTEGER(11) COMMENT 'NLD ─æ├│ng BHXH 10,5%', 
    `EmployeeUnionFee` INTEGER(11) COMMENT 'NL─É ─æ├│ng ph├¡ c├┤ng ─æo├án 1%', 
    `CompanySocialInsurance` INTEGER(11) COMMENT 'BHXH 17%', 
    `CompanyOccupaitionalAccidentOrDisease` INTEGER(11) COMMENT 'TNL─É / BNN 0.5%', 
    `CompanyHealthInsurance` INTEGER(11) COMMENT 'BHYT 3%', 
    `CompanyUnemploymentInsurance` INTEGER(11) COMMENT 'BHTN 1%', 
    `EnterpriseSocialInsurance` INTEGER(11) COMMENT 'doanh nghiß╗çp ─æ├│ng BHXH 21.5%', 
    `EnterpriseUnionFee` INTEGER(11) COMMENT 'Doanh nghiß╗çp ─æ├│ng c├┤ng ─æo├án 2%', 
    `LunchOrUniformAllowanceNoTax` INTEGER(11) COMMENT 'Kh├┤ng t├¡nh thuß║┐ ( phß╗Ñ cß║Ñp c╞ím tr╞░a/ ─Éß╗ông phß╗Ñc)', 
    `TotalTaxableIncome` INTEGER(11) COMMENT 'Tß╗òng thu nhß║¡p chß╗ïu thuß║┐', 
    `TaxableIncomeObject` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT '─Éß╗æi t╞░ß╗úng t├¡nh thuß║┐ TNCN', 
    `Commitment` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'Cam kß║┐t', 
    `Dependents` INTEGER(11) COMMENT 'Sß╗æ ng╞░ß╗¥i phß╗Ñ thuß╗Öc', 
    `TotalAssessableIncome` INTEGER(11) COMMENT 'Tß╗òng thu nhß║¡p t├¡nh thuß║┐', 
    `PersonalIncomeTaxCollection` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'Thu tiß╗ün thuß║┐ TNCN', 
    `ActualPayment` DECIMAL(12, 2) COMMENT 'Thß╗▒c l├únh', 
    `CompanyPaysSocialInsurance` INTEGER(11) COMMENT 'Cty ─æ├│ng hß╗ì BHXH', 
    `WithholdSocialInsurance` INTEGER(11) COMMENT 'thu hß╗Ö tiß╗ün BHXH 21.5%', 
    `BankTransfer` DECIMAL(12, 2) COMMENT 'chuyß╗ân khoß║ún', 
    `Name` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'T├¬n t├ái khoß║ún', 
    `AccountNumber` VARCHAR(255) COLLATE utf8mb4_unicode_ci COMMENT 'sß╗æ t├ái khoß║ún', 
    `Bank` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'ng├ón h├áng', 
    `Email` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'email', 
    `TransferAmount` DECIMAL(13, 2) COMMENT 'sß╗æ tiß╗ün chuyß╗ân khoß║ún', 
    `Additional` INTEGER(11) COMMENT 'bß╗ò sung', 
    `Notes` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'ghi ch├║/ l├╜ do', 
    `PaymentDate` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'ng├áy thanh to├ín', 
    `Level` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'bß║¡c', 
    `SalaryPerHour` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT '─æ╞ín gi├í giß╗¥', 
    `CompensatoryLeave` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'nghß╗ë b├╣', 
    `TotalLunchAllowance` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'Th├ánh tiß╗ün PC c╞ím theo c├┤ng', 
    `FixedIncomeWithLunchAllowance` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT '─æß╗ïnh mß╗⌐c thu nhß║¡p cß╗æ ─æß╗ïnh (─æ├ú  bao gß╗ôm Pc c╞ím)', 
    `FixedIncomeAmountWithLunchAllowance` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'Th├ánh tiß╗ün thu nhß║¡p cß╗æ ─æß╗ïnh theo c├┤ng chuß║⌐n (─æ├ú bao gß╗ôm PC c╞ím)', 
    `TaskBonus` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'Th╞░ß╗ƒng c├┤ng viß╗çc', 
    `ClinicsAchievingKPIRevenueBonus` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'Th╞░ß╗ƒng ph├▓ng kh├ím ─æß║ít KPI thu tiß╗ün', 
    `AssistantManagerAndConcurrentBonus` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'PC Phß╗Ñ t├í tr╞░ß╗ƒng v├á ki├¬m nhiß╗çm', 
    `GuaranteedIncomeAllowance` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'Phß╗Ñ cß║Ñp ─æß║úm bß║úo thu nhß║¡p', 
    `DentalTour` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `WarehouseAllowance` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'Phß╗Ñ cß║Ñp kho', 
    `OtherTotalIncome` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'Tß╗òng thu nhß║¡p kh├íc', 
    `DoctorBonus` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'Th╞░ß╗ƒng b├íc s─⌐', 
    `AdjustmentForDecemberShortfall` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'Cß╗Öng thiß║┐u th├íng 12', 
    `PayPeriod` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'kß╗│ l╞░╞íng', 
    `Template` INTEGER(11) COMMENT '1-BO\\n2-Phu ta\\n3-Bac Si\\n4-Bao ve', 
    PRIMARY KEY (`StaffSalaryDetailsId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `NgayCong2` (
    `Stt` INTEGER(11), 
    `M├ú NV` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Hß╗ì t├¬n` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `C├┤ng ty` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Chß╗⌐c danh` VARCHAR(100) COLLATE utf8mb4_unicode_ci, 
    `Loß║íi H─É` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Chi nh├ính` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Ng├áy v├áo l├ám` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Ca l├ám viß╗çc` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Tß╗òng cß╗Öng` INTEGER(11), 
    `Ghi ch├║ k chß║Ñm c├┤ng` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Sß╗æ giß╗¥ lv thß╗▒c tß║┐ (HIS)` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Nghß╗ë ph├⌐p` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Nghß╗ë chß║┐ ─æß╗Ö` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Nghß╗ë lß╗à/tß║┐t` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Tß╗òng c├┤ng t├¡nh l╞░╞íng` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `C├┤ng chuß║⌐n` INTEGER(11), 
    `L╞░╞íng c╞í bß║ún` DOUBLE(10, 3), 
    `Th╞░ß╗ƒng ├¥ thß╗⌐c v├á Tu├ón thß╗º/Th╞░ß╗ƒng Hiß╗çß╗Ñ quß║ú hoß║ít ─æß╗Öng` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Phß╗Ñ cß║Ñp C╞ím tr╞░a` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Phß╗Ñ cß║Ñp ─Éß╗ông phß╗Ñc` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Tß╗òng thu nhß║¡p theo ng├áy c├┤ng` DOUBLE(10, 3), 
    `Th╞░ß╗ƒng CRM/CS (C.Mai)` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Th╞░ß╗ƒng CLDV` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Th╞░ß╗ƒng Quß║ún l├╜ chung` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Th╞░ß╗ƒng hiß╗çu quß║ú quß║ún l├╜` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Th╞░ß╗ƒng Ebitda` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Th╞░ß╗ƒng Vinmec` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Th╞░ß╗ƒng an ninh` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Th╞░ß╗ƒng Lß╗à/Tß║┐t` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Tß╗òng th╞░ß╗ƒng` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `PC Gß╗¡i xe/C├┤ng t├íc` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Phß╗Ñ cß║Ñp chß╗⌐ng chß╗ë h├ánh nghß╗ü` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Phß╗Ñ cß║Ñp kh├íc` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Tß╗òng phß╗Ñ cß║Ñp` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Trß╗½ kh├íc` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Tß╗òng thu nhß║¡p tr╞░ß╗¢c thuß║┐` DOUBLE(10, 3), 
    `Mß╗⌐c l╞░╞íng tham gia BHXH` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `BHYT (1,5%)` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `BHXH (8%)` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `BHTN (1%)` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `NL─É ─æ├│ng BHXH (10.5%)` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `NL─É ─æ├│ng ph├¡ C├┤ng ─æo├án (1%)` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `BHXH (17%` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `TNL─É / BNN (0.5%)` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `BHYT (3%)` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `BHTN 1%` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Doanh nghiß╗çp ─æ├│ng BHXH 21.5%` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Doanh nghiß╗çp ─æ├│ng C├┤ng ─æo├án 2%` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Kh├┤ng t├¡nh thuß║┐ (Phß╗Ñ cß║Ñp c╞ím tr╞░a/ ─Éß╗ông phß╗Ñc)` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Tß╗öNG THU NHß║¼P CHß╗èU THUß║╛` DOUBLE(10, 3), 
    `─Éß╗æi t╞░ß╗úng t├¡nh Thuß║┐ TNCN` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Cam kß║┐t` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Sß╗æ ng╞░ß╗¥i phß╗Ñ thuß╗Öc` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Tß╗öNG THU NHß║¼P T├ìNH THUß║╛` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Thu Tiß╗ün thuß║┐ TNCN` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Thß╗▒c l├únh` INTEGER(11), 
    `Cty ─æ├│ng hß╗Ö BHXH` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Thu hß╗Ö tiß╗ün BHXH (21.5%` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Chuyß╗ân khoß║ún` INTEGER(11)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `SubsidizeStaff` (
    `SubsidizeId` INTEGER(10) UNSIGNED NOT NULL, 
    `WorkProfileId` INTEGER(10) UNSIGNED NOT NULL, 
    `StaffId` INTEGER(10) UNSIGNED NOT NULL, 
    `IssueDate` DATE NOT NULL, 
    `Desc` TEXT CHARACTER SET latin1, 
    `Amount` DECIMAL(12, 2) UNSIGNED NOT NULL, 
    `TaxInclude` INTEGER(1) NOT NULL COMMENT 'c├│ t├¡nh thu? hay kh├┤ng' DEFAULT '1', 
    `EndDate` DATE, 
    CONSTRAINT `fk_SubsidizeStaff_Subsidize` FOREIGN KEY(`SubsidizeId`) REFERENCES `Subsidize` (`SubsidizeId`), 
    CONSTRAINT `fk_SubsidizeStaff_WorkProfile` FOREIGN KEY(`WorkProfileId`, `StaffId`) REFERENCES `WorkProfile` (`WorkProfileId`, `StaffId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_SubsidizeStaff_WorkProfile_idx` ON `SubsidizeStaff` (`WorkProfileId`, `StaffId`);

CREATE INDEX `fk_SubsidizeStaff_Subsidize_idx` ON `SubsidizeStaff` (`SubsidizeId`);

CREATE TABLE `Staff` (
    `StaffId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `StaffCode` VARCHAR(16) CHARACTER SET utf8mb4 NOT NULL, 
    `IdNumber` VARCHAR(16) CHARACTER SET utf8mb4, 
    `IdNumberIssuedAt` DATE, 
    `IdNumberIssuedBy` INTEGER(11), 
    `PassportNumber` VARCHAR(16) CHARACTER SET utf8mb4, 
    `NationalInsuranceNumber` VARCHAR(16) CHARACTER SET utf8mb4, 
    `TaxNumber` VARCHAR(64) COLLATE utf8mb4_unicode_ci, 
    `UserId` INTEGER(10) UNSIGNED, 
    `FullName` VARCHAR(64) CHARACTER SET utf8mb4, 
    `FullNameNoSign` VARCHAR(64) CHARACTER SET utf8mb4, 
    `LastName` VARCHAR(16) CHARACTER SET utf8mb4, 
    `LastNameNoSign` VARCHAR(16) CHARACTER SET utf8mb4, 
    `DateOfBirth` DATE, 
    `PrimaryEmail` VARCHAR(255) CHARACTER SET utf8mb4, 
    `Photo` VARCHAR(128) CHARACTER SET utf8mb4 COMMENT 'h├¼nh ??i di?n c?a ng??i lao ??ng n?p cho c├┤ng ty', 
    `CreatedAt` INTEGER(10) UNSIGNED NOT NULL, 
    `CreatedBy` INTEGER(10) UNSIGNED NOT NULL, 
    `State` INTEGER(1) NOT NULL COMMENT 'tr?ng th├íi nh├ón vi├¬n n├áy1 - ?ang l├ám vi?c2- ?├ú ngh? vi?c 3- nh├ón vi├¬n t?m' DEFAULT '1', 
    `GenderId` INTEGER(10) UNSIGNED NOT NULL, 
    `DegreeId` INTEGER(10) UNSIGNED, 
    `InsuranceHospitalId` INTEGER(10) UNSIGNED, 
    `UpdatedAt` INTEGER(10) UNSIGNED, 
    `UpdatedBy` INTEGER(10) UNSIGNED, 
    `Nationality` INTEGER(10) UNSIGNED, 
    `StaffCodeKIM` VARCHAR(20) CHARACTER SET utf8mb4 COMMENT 'C?t Tmp ?? migrate d? li?u', 
    `MaritalStatusId` INTEGER(11), 
    `Note` TEXT COLLATE utf8mb4_unicode_ci, 
    `PlaceOfBirth` VARCHAR(128) COLLATE utf8mb4_unicode_ci, 
    `IsTimekeeping` SMALLINT(1) COMMENT '0: no checkin; 1 checkin; null get parent value (team)', 
    `EducationalLevel` VARCHAR(25) COLLATE utf8mb4_unicode_ci, 
    `GradeLevel` VARCHAR(25) COLLATE utf8mb4_unicode_ci, 
    `OldStaffCode` VARCHAR(25) COLLATE utf8mb4_unicode_ci, 
    `Migrate` VARCHAR(25) COLLATE utf8mb4_unicode_ci, 
    `ModifiedFormValue` INTEGER(11) COMMENT '0: Desibled All\\n1048576: Edit All' DEFAULT '1048575', 
    `PersonId` INTEGER(10) UNSIGNED, 
    `IsTest` TINYINT(4) DEFAULT '0', 
    `PINCode` CHAR(6) COLLATE utf8mb4_unicode_ci, 
    PRIMARY KEY (`StaffId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE UNIQUE INDEX `UserId_UNIQUE` ON `Staff` (`UserId`);

CREATE INDEX `IX_StaffCode` ON `Staff` (`StaffCode`);

CREATE INDEX `IX_PersonId` ON `Staff` (`PersonId`);

CREATE INDEX `IX_FullName` ON `Staff` (`FullName`);

CREATE TABLE `SessionLog` (
    `SessionId` INTEGER(11) UNSIGNED NOT NULL, 
    `AppId` INTEGER(11) NOT NULL, 
    `MenuItemId` INTEGER(11) NOT NULL, 
    `UserId` INTEGER(11) NOT NULL, 
    `Uri` VARCHAR(196) CHARACTER SET utf8, 
    `AuthenMethod` VARCHAR(32) CHARACTER SET utf8, 
    `Visited` INTEGER(11) DEFAULT '0', 
    `Config` TEXT CHARACTER SET utf8, 
    `Ip` VARCHAR(32) CHARACTER SET utf8 NOT NULL, 
    `Token` VARCHAR(64) CHARACTER SET utf8 NOT NULL, 
    `ClientInfo` TEXT CHARACTER SET utf8 COMMENT 'browser infomation', 
    `LogedOut` INTEGER(11) DEFAULT '0', 
    `AddedAt` INTEGER(11) NOT NULL, 
    CONSTRAINT `fk_SessionLog_Session` FOREIGN KEY(`SessionId`) REFERENCES `Session` (`SessionId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_SessionLog_Session_idx` ON `SessionLog` (`SessionId`);

CREATE TABLE `ABO2` (
    `Stt` INTEGER(11), 
    `M├ú NV` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Hß╗ì t├¬n` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `C├┤ng ty` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Chß╗⌐c danh` VARCHAR(100) COLLATE utf8mb4_unicode_ci, 
    `Loß║íi H─É` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Chi nh├ính` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Ng├áy v├áo l├ám` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Ca l├ám viß╗çc` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `L╞░╞íng c╞í bß║ún` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Th╞░ß╗ƒng ├¥ thß╗⌐c v├á Tu├ón thß╗º/Th╞░ß╗ƒng Hiß╗çß╗Ñ quß║ú hoß║ít ─æß╗Öng` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Tß╗òng cß╗Öng` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Ghi ch├║ k chß║Ñm c├┤ng` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Sß╗æ giß╗¥ lv thß╗▒c tß║┐ (HIS)` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Nghß╗ë ph├⌐p` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Nghß╗ë chß║┐ ─æß╗Ö` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Nghß╗ë lß╗à/tß║┐t` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Tß╗òng c├┤ng t├¡nh l╞░╞íng` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `C├┤ng chuß║⌐n` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `L╞░╞íng c╞í bß║ún1` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Th╞░ß╗ƒng ├¥ thß╗⌐c v├á Tu├ón thß╗º/Th╞░ß╗ƒng Hiß╗çß╗Ñ quß║ú hoß║ít ─æß╗Öng1` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Tß╗òng thu nhß║¡p theo ng├áy c├┤ng` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Th╞░ß╗ƒng CRM/CS (C.Mai)` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Th╞░ß╗ƒng CLDV` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Th╞░ß╗ƒng Quß║ún l├╜ chung` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Th╞░ß╗ƒng hiß╗çu quß║ú quß║ún l├╜` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Th╞░ß╗ƒng Ebitda` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Th╞░ß╗ƒng Vinmec` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Th╞░ß╗ƒng an ninh` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Th╞░ß╗ƒng Lß╗à/Tß║┐t` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Tß╗òng th╞░ß╗ƒng` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `PC Gß╗¡i xe/C├┤ng t├íc` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Phß╗Ñ cß║Ñp chß╗⌐ng chß╗ë h├ánh nghß╗ü` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Phß╗Ñ cß║Ñp kh├íc` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Tß╗òng phß╗Ñ cß║Ñp` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Trß╗½ kh├íc` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Tß╗òng thu nhß║¡p tr╞░ß╗¢c thuß║┐` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Mß╗⌐c l╞░╞íng tham gia BHXH` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `BHYT (1,5%)` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `BHXH (8%)` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `BHTN (1%)` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `NL─É ─æ├│ng BHXH (10.5%)` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `NL─É ─æ├│ng ph├¡ C├┤ng ─æo├án (1%)` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `BHXH (17%` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `TNL─É / BNN (0.5%)` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `BHYT (3%)` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `BHTN 1%` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Doanh nghiß╗çp ─æ├│ng BHXH 21.5%` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Doanh nghiß╗çp ─æ├│ng C├┤ng ─æo├án 2%` INTEGER(11), 
    `Kh├┤ng t├¡nh thuß║┐ (Phß╗Ñ cß║Ñp c╞ím tr╞░a/ ─Éß╗ông phß╗Ñc)` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Tß╗öNG THU NHß║¼P CHß╗èU THUß║╛` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `─Éß╗æi t╞░ß╗úng t├¡nh Thuß║┐ TNCN` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Cam kß║┐t` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Sß╗æ ng╞░ß╗¥i phß╗Ñ thuß╗Öc` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Tß╗öNG THU NHß║¼P T├ìNH THUß║╛` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Thu Tiß╗ün thuß║┐ TNCN` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Thß╗▒c l├únh` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Cty ─æ├│ng hß╗Ö BHXH` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Thu hß╗Ö tiß╗ün BHXH (21.5%` INTEGER(11), 
    `Chuyß╗ân khoß║ún` DOUBLE(10, 3), 
    `Column1` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Hß╗ì & t├¬n` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Sß╗æ t├ái khoß║ún` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Ng├ón h├áng` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Mail` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `─É├ú Chuyß╗ân khoß║ún 05/02/2024` DOUBLE(10, 3), 
    `Bß╗ò sung` INTEGER(11), 
    `Ghi ch├║` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Ng├áy thanh to├ín` VARCHAR(50) COLLATE utf8mb4_unicode_ci
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `Company` (
    `CompanyId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `NameVi` VARCHAR(128) CHARACTER SET utf8mb4 NOT NULL, 
    `NameEn` VARCHAR(128) CHARACTER SET utf8mb4, 
    `NameShortVi` VARCHAR(64) CHARACTER SET utf8mb4, 
    `NameShortEn` VARCHAR(64) CHARACTER SET utf8mb4, 
    `Address` VARCHAR(256) CHARACTER SET utf8mb4, 
    `Phone` VARCHAR(16) CHARACTER SET utf8mb4, 
    `Fax` VARCHAR(16) CHARACTER SET utf8mb4, 
    `Website` VARCHAR(64) CHARACTER SET utf8mb4, 
    `Email` VARCHAR(64) CHARACTER SET utf8mb4, 
    `State` INTEGER(1) UNSIGNED NOT NULL COMMENT '0  - kh├┤ng hoß║ít ─æß╗Öng
1 - hoß║ít ─æß╗Öng' DEFAULT '1', 
    `UpdateBy` INTEGER(11), 
    `UpdateAt` INTEGER(11), 
    `IsTimekeeping` SMALLINT(1) COMMENT '0: no checkin; 1 checkin', 
    `isSyncORC` INTEGER(11) DEFAULT '0', 
    `ORCRefCode` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `DomainEmail` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `Priority` INTEGER(11), 
    PRIMARY KEY (`CompanyId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `WorkShiftByMonthDay` (
    `WorkShiftId` INTEGER(10) UNSIGNED NOT NULL, 
    `WorkScheduleId` INTEGER(10) UNSIGNED NOT NULL, 
    `MonthDayId` INTEGER(10) UNSIGNED NOT NULL, 
    `BranchId` INTEGER(10) UNSIGNED NOT NULL, 
    `TotalBreakTimeInMinute` INTEGER(11) DEFAULT '0', 
    CONSTRAINT `fk_WorkShiftByMonthDay_MonthDay` FOREIGN KEY(`MonthDayId`) REFERENCES `MonthDay` (`MonthDayId`), 
    CONSTRAINT `fk_WorkShiftByMonthDay_WorkSchedule` FOREIGN KEY(`WorkScheduleId`) REFERENCES `WorkSchedule` (`WorkScheduleId`), 
    CONSTRAINT `fk_WorkShiftByMonthDay_WorkShift` FOREIGN KEY(`WorkShiftId`) REFERENCES `WorkShift` (`WorkShiftId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_WorkShiftByMonthDay_WorkShift_idx` ON `WorkShiftByMonthDay` (`WorkShiftId`);

CREATE INDEX `fk_WorkShiftByMonthDay_WorkSchedule_idx` ON `WorkShiftByMonthDay` (`WorkScheduleId`);

CREATE INDEX `fk_WorkShiftByMonthDay_WorkLocationId_idx` ON `WorkShiftByMonthDay` (`BranchId`);

CREATE INDEX `fk_WorkShiftByMonthDay_MonthDay_idx` ON `WorkShiftByMonthDay` (`MonthDayId`);

CREATE TABLE `rptStaffSalary_t` (
    `MonthDate` DATE, 
    `GroupId` TINYINT(4), 
    `StatusId` TINYINT(4), 
    `StaffId` INTEGER(11), 
    `WorkProfileId` INTEGER(11), 
    `WorkContractId` INTEGER(11), 
    `WorkContractTypeId` INTEGER(11), 
    `WorkContractAnnexId` INTEGER(11), 
    `IsFullTime` TINYINT(4), 
    `IsTimekeeping` TINYINT(4), 
    `FromDate` DATE, 
    `ToDate` DATE, 
    `StandardWorkingHours` DECIMAL(8, 1) DEFAULT '0.0', 
    `StandardWorkingDays` DECIMAL(5, 1) DEFAULT '0.0', 
    `Holiday_ActualWorkingHours` DECIMAL(8, 1) DEFAULT '0.0', 
    `Holiday_ActualWorkingDays` DECIMAL(5, 1) DEFAULT '0.0', 
    `Weekend_ActualWorkingHours` DECIMAL(8, 1) DEFAULT '0.0', 
    `Weekend_ActualWorkingDays` DECIMAL(5, 1) DEFAULT '0.0', 
    `ActualWorkingHours` DECIMAL(8, 1) DEFAULT '0.0', 
    `ActualWorkingDays` DECIMAL(5, 1) DEFAULT '0.0', 
    `ActualLeaveHours` DECIMAL(8, 1) DEFAULT '0.0', 
    `ActualLeaveDays` DECIMAL(5, 1) DEFAULT '0.0', 
    `PersonalDeductedAmount` DECIMAL(18, 2) DEFAULT '0.00', 
    `DependantNumber` INTEGER(11) DEFAULT '0', 
    `SocialInsuranceSalary` DECIMAL(18, 2) DEFAULT '0.00', 
    `ConcurrentlyAllowance` DECIMAL(18, 2) DEFAULT '0.00', 
    `OthersAllowance` DECIMAL(18, 2) DEFAULT '0.00', 
    `PositionAllowance` DECIMAL(18, 2) DEFAULT '0.00', 
    `AwarenessAllowance` DECIMAL(18, 2) DEFAULT '0.00', 
    `LunchAllowance` DECIMAL(18, 2) DEFAULT '0.00', 
    `UniformAllowance` DECIMAL(18, 2) DEFAULT '0.00', 
    `WorkBonusAmount` DECIMAL(18, 2) DEFAULT '0.00', 
    `WorkingPercent` DECIMAL(18, 10), 
    `ActualSocialInsuranceSalary` DECIMAL(18, 2), 
    `SocialInsuranceEmployee` DECIMAL(18, 2), 
    `HealthInsuranceEmployee` DECIMAL(18, 2), 
    `UnemploymentInsuranceEmployee` DECIMAL(18, 2), 
    `UnionDueEmployee` DECIMAL(18, 2), 
    `SocialInsuranceCompany` DECIMAL(18, 2), 
    `HealthInsuranceCompany` DECIMAL(18, 2), 
    `UnemploymentInsuranceCompany` DECIMAL(18, 2), 
    `UnionDueCompany` DECIMAL(18, 2), 
    `OccupationalDiseaseInsuranceCompany` DECIMAL(18, 2), 
    `DependantDeductedAmount` DECIMAL(18, 2), 
    `TotalTaxableInCome` DECIMAL(18, 2), 
    `PersonalIncomeTax` DECIMAL(18, 2), 
    `NetSalary` DECIMAL(18, 2), 
    `CreatedBy` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `UpdatedBy` INTEGER(11), 
    `UpdatedDate` DATETIME
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `ID2` ON `rptStaffSalary_t` (`MonthDate`, `GroupId`);

CREATE INDEX `ID1` ON `rptStaffSalary_t` (`StaffId`, `MonthDate`, `FromDate`);

CREATE TABLE `MenuNavbar` (
    `MenuNavbarId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `NameVI` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `NameEN` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `MenuNavbarGroupId` INTEGER(11), 
    `Action` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `Alias` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `Icon` VARCHAR(1024) COLLATE utf8mb4_unicode_ci, 
    `NavPath` VARCHAR(1024) COLLATE utf8mb4_unicode_ci, 
    `Route` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `Link` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `Url` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `Priority` INTEGER(11), 
    `CreatedDate` DATETIME, 
    `Status` INTEGER(11) DEFAULT '1', 
    `CrmFullAccess` INTEGER(11), 
    `IconURL` VARCHAR(1024) COLLATE utf8mb4_unicode_ci, 
    `IsDisplay` INTEGER(11) DEFAULT '1', 
    `CreatedBy` INTEGER(11), 
    `UpdatedDate` DATETIME, 
    `UpdatedBy` INTEGER(11), 
    PRIMARY KEY (`MenuNavbarId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `WorkProfile` (
    `WorkProfileId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `StaffId` INTEGER(10) UNSIGNED NOT NULL, 
    `FromDate` DATE NOT NULL, 
    `ToDate` DATE, 
    `IsCurrentProfile` INTEGER(1) UNSIGNED NOT NULL DEFAULT '0', 
    `WorkPositionId` INTEGER(10) DEFAULT '0', 
    `CompanyId` INTEGER(10) UNSIGNED NOT NULL, 
    `DepartmentId` INTEGER(10) UNSIGNED, 
    `TeamId` INTEGER(10) UNSIGNED NOT NULL, 
    `WorkContractId` INTEGER(10) UNSIGNED, 
    `StaffLevelId` INTEGER(10) UNSIGNED NOT NULL, 
    `BranchId` INTEGER(10), 
    `DegreeId` INTEGER(10) UNSIGNED NOT NULL, 
    `UpdatedAt` INTEGER(10) UNSIGNED, 
    `UpdatedBy` INTEGER(10) UNSIGNED, 
    `CreatedBy` INTEGER(11), 
    `CreatedAt` INTEGER(11), 
    `BaseSalary` DECIMAL(20, 2) UNSIGNED NOT NULL COMMENT 'mß╗⌐c n├áy c├│ thß╗â lookup tß╗½ bß║úng StaffLevel qua', 
    `ExtraMonthlyIncome` DECIMAL(20, 2) NOT NULL COMMENT 'th╞░ß╗ƒng theo n─âng xuß║Ñt', 
    `BankId` INTEGER(10) UNSIGNED, 
    `BankBranchId` INTEGER(10) UNSIGNED, 
    `BankAccountName` VARCHAR(64) CHARACTER SET utf8mb4, 
    `BankAccountId` VARCHAR(16) CHARACTER SET utf8mb4, 
    `IsFullTime` INTEGER(1) COMMENT '1 l├á l├ám fulltime 2 l├á l├ám theo ca', 
    `WorkPositionNote` VARCHAR(128) COLLATE utf8mb4_unicode_ci, 
    `WorkPositionNote2` VARCHAR(25) COLLATE utf8mb4_unicode_ci, 
    `Migrate` VARCHAR(25) COLLATE utf8mb4_unicode_ci, 
    `WorkProfilePositionId` INTEGER(11), 
    `IncomeTypeId` INTEGER(11), 
    `IncomeTypeLevelId` INTEGER(11), 
    `CurrentBranchId` INTEGER(11), 
    `IsAvailable` INTEGER(1) DEFAULT '1', 
    PRIMARY KEY (`WorkProfileId`, `StaffId`), 
    CONSTRAINT `fk_workprofile_staffId` FOREIGN KEY(`StaffId`) REFERENCES `Staff` (`StaffId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_WorkProfile_Staff_idx` ON `WorkProfile` (`StaffId`);

CREATE INDEX `IX_WorkProfile_WorkContractId` ON `WorkProfile` (`WorkContractId`);

CREATE TABLE `TeleServiceProvider` (
    `TeleServiceProviderId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `Name` VARCHAR(32) COLLATE utf8mb4_unicode_ci NOT NULL, 
    `NumberWildcard` VARCHAR(128) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '097* 098* ...', 
    `State` INTEGER(1) DEFAULT '1', 
    `Ordering` INTEGER(10) UNSIGNED DEFAULT '0', 
    PRIMARY KEY (`TeleServiceProviderId`)
)COMMENT='h├úng cung c?p d?ch v? tho?i: Viettel, Mobilephone, Vinaphone' DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `WidgetAssign` (
    `WidgetId` INTEGER(11) UNSIGNED NOT NULL, 
    `MenuItemId` INTEGER(11) UNSIGNED NOT NULL
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `WorkPositionHistory` (
    `WorkPositionHistoryId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `OrgId` INTEGER(10) UNSIGNED NOT NULL, 
    `WorkProfilePositionId` INTEGER(10) NOT NULL, 
    `IsMainPosition` TINYINT(4) NOT NULL DEFAULT '0', 
    `FromDate` DATE NOT NULL, 
    `ToDate` DATE, 
    `WorkContractHistoryId` INTEGER(11) NOT NULL, 
    `CreatedDate` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`WorkPositionHistoryId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `MobileApp` (
    `MobileAppId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `Name` VARCHAR(64) CHARACTER SET utf8mb4 NOT NULL, 
    `Description` TEXT CHARACTER SET utf8mb4, 
    `AddedAt` INTEGER(10) UNSIGNED NOT NULL, 
    `AppMarketId` VARCHAR(128) CHARACTER SET utf8mb4, 
    `AppToken` VARCHAR(32) CHARACTER SET utf8mb4 NOT NULL, 
    PRIMARY KEY (`MobileAppId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `InsuranceSession` (
    `InsuranceSessionId` INTEGER(10) UNSIGNED NOT NULL, 
    `InsuranceType` SMALLINT(6) NOT NULL, 
    `FilePath` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL, 
    `UploadedDate` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    `TotalRecord` INTEGER(11) NOT NULL, 
    `TotalAmount` DECIMAL(15, 2) NOT NULL, 
    `Note` VARCHAR(500) COLLATE utf8mb4_unicode_ci, 
    `ErrorNote` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `IsActive` TINYINT(1) NOT NULL DEFAULT '1', 
    `CreatedDate` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    `CreatedStaffId` INTEGER(11) NOT NULL, 
    `UpdatedDate` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    `UpdatedStaffId` INTEGER(11) NOT NULL
)ROW_FORMAT=DYNAMIC DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `PK_InsuranceSession` ON `InsuranceSession` (`InsuranceSessionId`);

CREATE TABLE `ScoreCardTicketMedia` (
    `ScoreCardTicketMediaId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `ScoreCardTicketId` INTEGER(11), 
    `CDNURL` VARCHAR(1024) COLLATE utf8mb4_unicode_ci, 
    `Priority` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`ScoreCardTicketMediaId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `WorkContract` (
    `WorkContractId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `WorkContractCode` VARCHAR(32) CHARACTER SET utf8mb4, 
    `FromDate` DATE NOT NULL, 
    `ToDate` DATE, 
    `SignedDate` DATE, 
    `SignedBy` INTEGER(11) UNSIGNED, 
    `WorkContractTypeId` INTEGER(10) UNSIGNED NOT NULL, 
    `AttachFile` VARCHAR(128) CHARACTER SET utf8mb4, 
    `WorkingHoursPerDay` FLOAT DEFAULT '8', 
    `IsExitInterview` INTEGER(11) DEFAULT '0', 
    `TerminationDate` DATETIME, 
    `TerminationReasonId` INTEGER(11), 
    `TerminationReasonNote` VARCHAR(512) COLLATE utf8mb4_unicode_ci, 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    `UpdatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `UpdatedBy` INTEGER(11), 
    `WorkContractScheduleId` INTEGER(11), 
    `WorkTimeMode` VARCHAR(20) COLLATE utf8mb4_unicode_ci COMMENT 'Hour, Month', 
    `SalaryAmount` DECIMAL(18, 2), 
    `AdditionalSalaryAmount` DECIMAL(18, 2), 
    `SalaryNote` VARCHAR(256) COLLATE utf8mb4_unicode_ci, 
    `Migrate` VARCHAR(25) COLLATE utf8mb4_unicode_ci, 
    `SocialInsuranceSalary` INTEGER(11), 
    `PriorityLevel` VARCHAR(25) COLLATE utf8mb4_unicode_ci, 
    `WorkPriorityLevelId` INTEGER(11), 
    `MonthlySalary` DECIMAL(15, 2), 
    PRIMARY KEY (`WorkContractId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_WorkContract_WorkContractType_idx` ON `WorkContract` (`WorkContractTypeId`);

CREATE INDEX `fk_WorkContract_SignedBy_idx` ON `WorkContract` (`SignedBy`);

CREATE TABLE `Ward` (
    `WardId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `WardName` VARCHAR(100) COLLATE utf8mb4_unicode_ci, 
    `Label` VARCHAR(20) COLLATE utf8mb4_unicode_ci, 
    `DistrictId` INTEGER(10) UNSIGNED, 
    `State` TINYINT(1) DEFAULT '1', 
    `VnWardId` INTEGER(11), 
    PRIMARY KEY (`WardId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `ScoreCardDetail` (
    `ScoreCardDetailId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `ScoreCardId` INTEGER(11), 
    `ScoreCriterionId` INTEGER(11), 
    `Score` TINYINT(4) DEFAULT '0', 
    `Priority` INTEGER(11) DEFAULT '1', 
    `IsPass` TINYINT(4), 
    `Content` TEXT COLLATE utf8mb4_unicode_ci, 
    `DueDate` DATETIME, 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    `UpdatedDate` DATETIME, 
    `UpdatedBy` INTEGER(11), 
    PRIMARY KEY (`ScoreCardDetailId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `SalaryAllowancesType` (
    `SalaryAllowancesTypeId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `Name` VARCHAR(1024) COLLATE utf8mb4_unicode_ci, 
    `IsDeleted` SMALLINT(6) DEFAULT '0', 
    `CreatedBy` INTEGER(11), 
    `CreateDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`SalaryAllowancesTypeId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `MonthlyBonusImport` (
    `Id` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `MonthSalaryPeriod` DATE, 
    `ImportType` INTEGER(11) COMMENT '1) monthlybonus
2)TetHoliday
3)Additional', 
    `FilePath` VARCHAR(2048) COLLATE utf8mb4_unicode_ci, 
    `ExportPath` VARCHAR(2048) COLLATE utf8mb4_unicode_ci, 
    `Total` INTEGER(11) DEFAULT '0', 
    `Success` INTEGER(11) DEFAULT '0', 
    `Error` INTEGER(11) DEFAULT '0', 
    `DeletedDate` DATETIME, 
    `DeletedBy` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    PRIMARY KEY (`Id`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `IX_MonthSalaryPeriod` ON `MonthlyBonusImport` (`MonthSalaryPeriod`);

CREATE TABLE `OrgPosistionType` (
    `PosistionTypeId` INTEGER(11) NOT NULL, 
    `PosistionTypeName` VARCHAR(32) COLLATE utf8mb4_unicode_ci, 
    `CreatedTime` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
    PRIMARY KEY (`PosistionTypeId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `EmailContent` (
    `EmailContentId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `EmailId` INTEGER(11), 
    `Content` LONGTEXT COLLATE utf8mb4_unicode_ci, 
    PRIMARY KEY (`EmailContentId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `DependantRelationship` (
    `DependantRelationshipId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `Name` VARCHAR(64) CHARACTER SET utf8mb4 NOT NULL, 
    `Ordering` INTEGER(11), 
    `IsPromotionApply` INTEGER(11) DEFAULT '1', 
    PRIMARY KEY (`DependantRelationshipId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `StaffSalaryDetails_t` (
    `StaffSalaryDetailsId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `StaffId` INTEGER(11), 
    `StaffCode` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `FullName` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'hß╗ì t├¬n', 
    `Company` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'C├┤ng ty', 
    `WorkProfilePosition` VARCHAR(100) COLLATE utf8mb4_unicode_ci COMMENT 'Chß╗⌐c danh', 
    `ContractType` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'Loß║íi hß╗úp ─æß╗ông', 
    `Branch` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'Chi nh├ính', 
    `StartDate` DATETIME COMMENT 'ng├áy v├áo l├ám', 
    `Shift` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'ca l├ám viß╗çc', 
    `Level` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'bß║¡c', 
    `SalaryPerHour` DECIMAL(7, 2) COMMENT '─æ╞ín gi├í giß╗¥' DEFAULT '0.00', 
    `ActualHoursWorked` DECIMAL(5, 2) COMMENT 'sß╗æ giß╗¥ lv thß╗▒c tß║┐ HIS' DEFAULT '0.00', 
    `AnnualLeave` DECIMAL(5, 2) COMMENT 'nghß╗ë ph├⌐p' DEFAULT '0.00', 
    `PaidLeave` DECIMAL(5, 2) COMMENT 'nghß╗ë chß║┐ ─æß╗Ö' DEFAULT '0.00', 
    `PublicHolidaysLeave` DECIMAL(5, 2) COMMENT 'nghß╗ë lß╗à/tß║┐t' DEFAULT '0.00', 
    `TotalStandardHours` DECIMAL(5, 2) COMMENT 'tß╗òng c├┤ng t├¡nh l╞░╞íng' DEFAULT '0.00', 
    `StandardWage` DECIMAL(5, 2) COMMENT 'c├┤ng chuß║⌐n' DEFAULT '0.00', 
    `TotalIncomeWorkingDays` DECIMAL(13, 3) COMMENT 'Th├ánh tiß╗ün l╞░╞íng theo c├┤ng chuß║⌐n' DEFAULT '0.000', 
    `TaskBonus1` DECIMAL(15, 3) COMMENT 'Th╞░ß╗ƒng c├┤ng viß╗çc' DEFAULT '0.000', 
    `ServiceQualityBonus1` DECIMAL(13, 3) COMMENT 'Th╞░ß╗ƒng CLDV' DEFAULT '0.000', 
    `GeneralManagermentBonus1` DECIMAL(13, 3) COMMENT 'Th╞░ß╗ƒng quß║ún l├╜ chung' DEFAULT '0.000', 
    `EfficiencyManagementBonus` DECIMAL(13, 3) COMMENT 'Th╞░ß╗ƒng hiß╗çu quß║ú quß║ún l├╜' DEFAULT '0.000', 
    `EbitdaBonus` DECIMAL(13, 3) COMMENT 'Th╞░ß╗ƒng Ebitda' DEFAULT '0.000', 
    `OtherBonus` DECIMAL(13, 3) COMMENT 'th╞░ß╗ƒng kh├íc nß║┐u c├│' DEFAULT '0.000', 
    `SecurityBonus` DECIMAL(13, 3) COMMENT 'th╞░ß╗ƒng an ninh' DEFAULT '0.000', 
    `PerformanceBonus` DECIMAL(13, 3) COMMENT 'Th╞░ß╗ƒng n─âng suß║Ñt' DEFAULT '0.000', 
    `TaskBonus2` DECIMAL(15, 3) COMMENT 'Th╞░ß╗ƒng c├┤ng viß╗çc' DEFAULT '0.000', 
    `ServiceQualityBonus2` DECIMAL(13, 3) COMMENT 'Th╞░ß╗ƒng CLDV' DEFAULT '0.000', 
    `GeneralManagermentBonus2` DECIMAL(13, 3) COMMENT 'Th╞░ß╗ƒng quß║ún l├╜ chung' DEFAULT '0.000', 
    `KPIBonus` DECIMAL(15, 3) COMMENT 'Th╞░ß╗ƒng KPI' DEFAULT '0.000', 
    `VinmecBonus` DECIMAL(13, 3) COMMENT 'th╞░ß╗ƒng vinmec' DEFAULT '0.000', 
    `DoctorBonus` DECIMAL(15, 3) COMMENT 'Th╞░ß╗ƒng b├íc s─⌐' DEFAULT '0.000', 
    `OtherBonus3(vinmec)` DECIMAL(13, 3) COMMENT 'Th╞░ß╗ƒng kh├íc (vinmec)' DEFAULT '0.000', 
    `HolidayBonus` DECIMAL(13, 3) COMMENT 'th╞░ß╗ƒng lß╗à/tß║┐t' DEFAULT '0.000', 
    `TotalBonus` DECIMAL(12, 2) COMMENT 'tß╗òng th╞░ß╗ƒng' DEFAULT '0.00', 
    `AssistantManagerAndConcurrentBonus` DECIMAL(15, 3) COMMENT 'PC Phß╗Ñ t├í tr╞░ß╗ƒng v├á ki├¬m nhiß╗çm' DEFAULT '0.000', 
    `GuaranteedIncomeAllowance` DECIMAL(15, 3) COMMENT 'Phß╗Ñ cß║Ñp ─æß║úm bß║úo thu nhß║¡p' DEFAULT '0.000', 
    `ParkingTravelAllowance` DECIMAL(13, 3) COMMENT 'PC gß╗¡i xe/c├┤ng t├íc' DEFAULT '0.000', 
    `ProfessionalCertificateAllowance` DECIMAL(13, 3) COMMENT 'Phß╗Ñ cß║Ñp chß╗⌐ng chß╗ë h├ánh nghß╗ü' DEFAULT '0.000', 
    `OtherAllowances` DECIMAL(13, 3) COMMENT 'phß╗Ñ cß║Ñp kh├íc' DEFAULT '0.000', 
    `DentalTour` DECIMAL(15, 3) DEFAULT '0.000', 
    `WarehouseAllowance` DECIMAL(15, 3) COMMENT 'Phß╗Ñ cß║Ñp kho' DEFAULT '0.000', 
    `OtherTotalIncome` DECIMAL(15, 3) COMMENT 'Tß╗òng thu nhß║¡p kh├íc' DEFAULT '0.000', 
    `OtherAddition` DECIMAL(13, 3) COMMENT 'cß╗Öng kh├íc' DEFAULT '0.000', 
    `OtherDeductions` DECIMAL(13, 3) COMMENT 'trß╗½ kh├íc' DEFAULT '0.000', 
    `TotalIncomeBeforeTax` DECIMAL(13, 3) COMMENT 'tß╗òng thu nhß║¡p tr╞░ß╗¢c thuß║┐' DEFAULT '0.000', 
    `ParticipatingSalaryInSocialInsurance` DECIMAL(13, 3) COMMENT 'Mß╗⌐c l╞░╞íng tham gia BHXH' DEFAULT '0.000', 
    `PersonalHealthInsurance` DECIMAL(13, 3) COMMENT 'BHYT 1,5%' DEFAULT '0.000', 
    `PersonalSocialInsurance` DECIMAL(13, 3) COMMENT 'BHXH 8%' DEFAULT '0.000', 
    `PersonalUnemploymentInsurance` DECIMAL(13, 3) COMMENT 'BHTN 1%' DEFAULT '0.000', 
    `EmployeeSocialInsurance` DECIMAL(13, 3) COMMENT 'NLD ─æ├│ng BHXH 10,5%' DEFAULT '0.000', 
    `EmployeeUnionFee` DECIMAL(13, 3) COMMENT 'NL─É ─æ├│ng ph├¡ c├┤ng ─æo├án 1%' DEFAULT '0.000', 
    `CompanySocialInsurance` DECIMAL(13, 3) COMMENT 'BHXH 17%' DEFAULT '0.000', 
    `CompanyOccupaitionalAccidentOrDisease` DECIMAL(13, 3) COMMENT 'TNL─É / BNN 0.5%' DEFAULT '0.000', 
    `CompanyHealthInsurance` DECIMAL(13, 3) COMMENT 'BHYT 3%' DEFAULT '0.000', 
    `CompanyUnemploymentInsurance` DECIMAL(13, 3) COMMENT 'BHTN 1%' DEFAULT '0.000', 
    `EnterpriseSocialInsurance` DECIMAL(13, 3) COMMENT 'doanh nghiß╗çp ─æ├│ng BHXH 21.5%' DEFAULT '0.000', 
    `EnterpriseUnionFee` DECIMAL(13, 3) COMMENT 'Doanh nghiß╗çp ─æ├│ng c├┤ng ─æo├án 2%' DEFAULT '0.000', 
    `LunchOrUniformAllowanceNoTax` DECIMAL(13, 3) COMMENT 'Kh├┤ng t├¡nh thuß║┐ ( phß╗Ñ cß║Ñp c╞ím tr╞░a/ ─Éß╗ông phß╗Ñc)' DEFAULT '0.000', 
    `TotalTaxableIncome` DECIMAL(13, 3) COMMENT 'Tß╗òng thu nhß║¡p chß╗ïu thuß║┐' DEFAULT '0.000', 
    `TaxableIncomeObject` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT '─Éß╗æi t╞░ß╗úng t├¡nh thuß║┐ TNCN', 
    `Commitment` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'Cam kß║┐t', 
    `Dependents` INTEGER(11) COMMENT 'Sß╗æ ng╞░ß╗¥i phß╗Ñ thuß╗Öc' DEFAULT '0', 
    `TotalAssessableIncome` DECIMAL(13, 3) COMMENT 'Tß╗òng thu nhß║¡p t├¡nh thuß║┐' DEFAULT '0.000', 
    `PersonalIncomeTaxCollection` DECIMAL(13, 3) COMMENT 'Thu tiß╗ün thuß║┐ TNCN' DEFAULT '0.000', 
    `ActualPayment` DECIMAL(12, 2) COMMENT 'Thß╗▒c l├únh' DEFAULT '0.00', 
    `CompanyPaysSocialInsurance` DECIMAL(13, 3) COMMENT 'Cty ─æ├│ng hß╗ì BHXH' DEFAULT '0.000', 
    `WithholdSocialInsurance` DECIMAL(13, 3) COMMENT 'thu hß╗Ö tiß╗ün BHXH 21.5%' DEFAULT '0.000', 
    `PaidHolidayBonus` DECIMAL(11, 2) COMMENT '─É├ú thanh to├ín th╞░ß╗ƒng Lß╗à/tß║┐t\\n' DEFAULT '0.00', 
    `PaidOthers` DECIMAL(11, 2) COMMENT '─É├ú thanh to├ín kh├íc\\n' DEFAULT '0.00', 
    `BankTransfer` DECIMAL(12, 2) COMMENT 'chuyß╗ân khoß║ún' DEFAULT '0.00', 
    `NoteOtherAdditions` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'Ghi ch├║ cß╗Öt cß╗Öng kh├íc\\n', 
    `PayPeriod` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT 'kß╗│ l╞░╞íng', 
    `Template` VARCHAR(50) COLLATE utf8mb4_unicode_ci COMMENT '1-BO\\\\n2-Phu ta\\\\n3-Bac Si\\\\n4-Bao ve', 
    PRIMARY KEY (`StaffSalaryDetailsId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `WorkProfileIncomeTypeTracking` (
    `Id` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `WorkProfileId` INTEGER(10), 
    `IncomeTypeId` INTEGER(11), 
    `IncomeTypeLevelId` INTEGER(11), 
    `CreatedBy` INTEGER(11), 
    `ObjectSource` INTEGER(11) COMMENT '1 H?p ??ng, 2 ph? l?c,3 ?i?u chuy?n' DEFAULT '1', 
    `ObjectId` INTEGER(11), 
    `TrackingDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`Id`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `EmailRead` (
    `EmailReadId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `EmailId` INTEGER(11), 
    `Subject` VARCHAR(2048) COLLATE utf8mb4_unicode_ci, 
    `PrimaryEmailId` INTEGER(11), 
    `StaffId` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `ReadDate` DATETIME, 
    `DeletedDate` DATETIME, 
    `ReCallDate` DATETIME, 
    `Type` TINYINT(4) COMMENT '1 :To
2:CC
3:BCC
4:Forward', 
    PRIMARY KEY (`EmailReadId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `ScoreCampaignCriterionDetail` (
    `ScoreCampaignCriterionDetailld` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `ScoreCampaignId` INTEGER(11), 
    `ScoreCriterionId` INTEGER(11), 
    `Score` TINYINT(4) DEFAULT '0', 
    `Priority` INTEGER(11) DEFAULT '1', 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    `UpdatedDate` DATETIME, 
    `UpdatedBy` INTEGER(11), 
    PRIMARY KEY (`ScoreCampaignCriterionDetailld`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `CustomerCareRatingRecommend` (
    `Id` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `RatingId` INTEGER(11) NOT NULL, 
    `Content` TEXT COLLATE utf8mb4_unicode_ci, 
    `OrgId` INTEGER(11), 
    `CreatedBy` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `UpdatedBy` INTEGER(11), 
    `UpdatedDate` DATETIME, 
    PRIMARY KEY (`Id`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX fk_rating_id ON `CustomerCareRatingRecommend` (`RatingId`);

CREATE TABLE `CertificateTracking` (
    `CertificateTrackingId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `CertificateId` INTEGER(11), 
    `TrackingType` INTEGER(11) COMMENT '1:create;2:update;3:remove', 
    `CreatedDate` DATETIME, 
    `CreatedBy` INTEGER(11), 
    `AccumulatedHours` INTEGER(11) NOT NULL DEFAULT '0', 
    `Note` VARCHAR(1000) COLLATE utf8mb4_unicode_ci, 
    `DateOfOccurrence` DATE NOT NULL, 
    PRIMARY KEY (`CertificateTrackingId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `BranchWorkLocation` (
    `Id` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `CompanyId` INTEGER(11) NOT NULL, 
    `BranchId` INTEGER(10) UNSIGNED NOT NULL, 
    `WorkLocationId` INTEGER(10) UNSIGNED NOT NULL, 
    PRIMARY KEY (`Id`), 
    CONSTRAINT fl_bw_worklocation FOREIGN KEY(`WorkLocationId`) REFERENCES `WorkLocation` (`WorkLocationId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `CronUpdateWorkProfileHistory` (
    `CronUpdateWorkProfileHistoryId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `CreatedAt` INTEGER(11) NOT NULL, 
    `WorkProfileId` TEXT COLLATE utf8mb4_unicode_ci NOT NULL, 
    `StaffId` TEXT COLLATE utf8mb4_unicode_ci NOT NULL, 
    PRIMARY KEY (`CronUpdateWorkProfileHistoryId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `StaffInterview` (
    `StaffInterviewId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `InterviewDate` DATETIME COMMENT 'Ng├áy ph?ng v?n', 
    `CandidateId` INTEGER(10) UNSIGNED, 
    `InterviewerId` INTEGER(10) UNSIGNED COMMENT 'Ng??i ph?ng v?n ch├¡nh - StaffId', 
    `InterviewerBoard` VARCHAR(1000) CHARACTER SET utf8mb4 COMMENT 'Ng??i ph?ng v?n - ?ng vi├¬n', 
    `WorkProfilePositionId` INTEGER(10) UNSIGNED COMMENT 'V? tr├¡ c├┤ng vi?c', 
    `CompanyId` INTEGER(11) COMMENT 'C├┤ng ty', 
    `BranchId` INTEGER(11) COMMENT 'Chi nh├ính', 
    `DepartmentId` INTEGER(11) COMMENT 'Ph├▓ng ban', 
    `TeamId` INTEGER(11) COMMENT 'B? ph?n', 
    `StaffLevelId` INTEGER(11) COMMENT 'C?p b?c', 
    `Status` TINYINT(2) COMMENT 'Tr?ng th├íi - 1: M?i, 2: ?├ú h?y, 3: ??t, 4: Kh├┤ng ??t', 
    `StatusNote` VARCHAR(1000) CHARACTER SET utf8mb4 COMMENT 'Ghi ch├║ tr?ng th├íi', 
    `CreatedBy` INTEGER(10) UNSIGNED, 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `UpdatedBy` INTEGER(10) UNSIGNED, 
    `UpdatedDate` DATETIME, 
    PRIMARY KEY (`StaffInterviewId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `IX_InterviewDate` ON `StaffInterview` (`InterviewDate`);

CREATE INDEX `IX_CandidateId` ON `StaffInterview` (`CandidateId`);

CREATE TABLE `RentalContractDocument` (
    `RentalContractDocumentId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `RentalContractId` INTEGER(11) NOT NULL, 
    `CDN` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL, 
    `IsDelete` TINYINT(4) DEFAULT '0', 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    PRIMARY KEY (`RentalContractDocumentId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `Language` (
    `LanguageId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `Name` VARCHAR(32) CHARACTER SET latin1 NOT NULL, 
    `Ordering` INTEGER(11) NOT NULL DEFAULT '0', 
    PRIMARY KEY (`LanguageId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `ScoreCardDetailMedia` (
    `ScoreCardDetailMediaId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `ScoreCardId` INTEGER(11), 
    `ScoreCardDetailId` INTEGER(11), 
    `URL` VARCHAR(1024) COLLATE utf8mb4_unicode_ci, 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    `UpdatedDate` DATETIME, 
    `UpdatedBy` INTEGER(11), 
    PRIMARY KEY (`ScoreCardDetailMediaId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `ImportLuong` (
    `MaNV` VARCHAR(50) CHARACTER SET utf8mb4, 
    `Column1` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Column2` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `BHXH` INTEGER(11), 
    `Capbac` VARCHAR(50) COLLATE utf8mb4_unicode_ci, 
    `Ythuc` INTEGER(11), 
    `Comtrua` INTEGER(11), 
    `DongPhuc` INTEGER(11), 
    `Column3` INTEGER(11), 
    `KN` INTEGER(11), 
    `Khac` INTEGER(11), 
    `StaffId` INTEGER(11), 
    `WorkContractId` INTEGER(11), 
    `WorkProfileId` INTEGER(11)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `PhoneNumber` (
    `PhoneNumber` VARCHAR(16) COLLATE utf8mb4_unicode_ci NOT NULL, 
    `TeleServiceProviderId` INTEGER(10) UNSIGNED NOT NULL, 
    PRIMARY KEY (`PhoneNumber`), 
    CONSTRAINT `fk_PhoneNumber_TeleServiceProvider` FOREIGN KEY(`TeleServiceProviderId`) REFERENCES `TeleServiceProvider` (`TeleServiceProviderId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE INDEX `fk_PhoneNumber_TeleServiceProvider_idx` ON `PhoneNumber` (`TeleServiceProviderId`);

CREATE TABLE `VnProvince_BK_20230710` (
    `VnProvinceId` INTEGER(10) UNSIGNED NOT NULL, 
    `ProvinceCode` VARCHAR(8) CHARACTER SET utf8mb4, 
    `ProvincePostalCode` VARCHAR(8) CHARACTER SET utf8mb4, 
    `NameVi` VARCHAR(64) CHARACTER SET utf8mb4 NOT NULL, 
    `NameEn` VARCHAR(64) CHARACTER SET utf8mb4, 
    `LabelVi` VARCHAR(32) CHARACTER SET utf8mb4 NOT NULL COMMENT 'Th├ánh ph?
T?nh', 
    `LabelEn` VARCHAR(32) CHARACTER SET utf8mb4 COMMENT 'Municipality
Province', 
    `Ordering` INTEGER(10) UNSIGNED
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `TimeKeeperChanging` (
    `TimeKeeperChanging` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `TimeKeeperId` INTEGER(11) UNSIGNED, 
    `OldCheckInAt` DATETIME, 
    `OldCheckOutAt` DATETIME, 
    `CheckInAt` DATETIME, 
    `CheckOutAt` DATETIME, 
    `ReasonId` INTEGER(11), 
    `ReasonNote` VARCHAR(128) COLLATE utf8mb4_unicode_ci, 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    PRIMARY KEY (`TimeKeeperChanging`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `IncomeServiceQualityConfig` (
    `IncomeServiceQualityConfigId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `Name` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `Code` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    `IncomeTypeId` INTEGER(11), 
    `IncomeTypeLevelId` INTEGER(11), 
    `EffectFromDate` DATE, 
    `EffectToDate` DATE, 
    `FromRating` FLOAT, 
    `ToRating` FLOAT, 
    `Value` DECIMAL(18, 2), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    PRIMARY KEY (`IncomeServiceQualityConfigId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `TaskStatus` (
    `TaskStatusId` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT, 
    `Name` VARCHAR(16) COLLATE utf8mb4_unicode_ci NOT NULL, 
    `Ordering` INTEGER(10) UNSIGNED NOT NULL, 
    PRIMARY KEY (`TaskStatusId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `ScoreCriterionCategory` (
    `ScoreCriterionCategoryId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `Code` VARCHAR(45) COLLATE utf8mb4_unicode_ci, 
    `Name` VARCHAR(512) COLLATE utf8mb4_unicode_ci, 
    `Description` VARCHAR(512) COLLATE utf8mb4_unicode_ci, 
    `IsDeleted` TINYINT(4) DEFAULT '0', 
    `Priority` TINYINT(4) DEFAULT '0', 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    `UpdatedDate` DATETIME, 
    `UpdatedBy` INTEGER(11), 
    PRIMARY KEY (`ScoreCriterionCategoryId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `OrgOffice` (
    `OrgOfficeId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `NameVi` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `NameEn` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL, 
    `OrgId` INTEGER(11) DEFAULT '0', 
    `Priority` INTEGER(11) DEFAULT '0', 
    `Status` INTEGER(11) COMMENT '1 active
0 deactice' DEFAULT '1', 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`OrgOfficeId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `Org2` (
    `OrgId` INTEGER(10) UNSIGNED NOT NULL DEFAULT '0', 
    `OrgCode` VARCHAR(200) COLLATE utf8mb4_unicode_ci NOT NULL, 
    `OrgName` VARCHAR(200) COLLATE utf8mb4_unicode_ci NOT NULL, 
    `CompanyId` INTEGER(10) UNSIGNED NOT NULL, 
    `ParentId` INTEGER(11) NOT NULL DEFAULT '0', 
    `DefaultBranchId` INTEGER(10) UNSIGNED, 
    `NumAnnualLeaveTraining` INTEGER(5) NOT NULL, 
    `IsViewAllBranch` INTEGER(1) NOT NULL, 
    `IsTimekeeping` INTEGER(1) NOT NULL, 
    `IsActive` INTEGER(1) NOT NULL, 
    `PosLeft` INTEGER(5) NOT NULL DEFAULT '0', 
    `PosRight` INTEGER(5) NOT NULL DEFAULT '0', 
    `RoleCode` VARCHAR(32) COLLATE utf8mb4_unicode_ci, 
    `CreatedDate` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    `CreatedStaffId` INTEGER(11) UNSIGNED NOT NULL DEFAULT '0', 
    `UpdatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `UpdatedStaffId` INTEGER(11) UNSIGNED DEFAULT '0', 
    `ParentDeleteOrgId` INTEGER(11), 
    `Level` INTEGER(11), 
    `BranchId` INTEGER(11)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `IncomeByJob` (
    `IncomeByJobId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `StaffId` INTEGER(11), 
    `IncomeTypeId` INTEGER(11), 
    `BusinessType` INTEGER(11) COMMENT '1\\\\\\\\\\\\\\\\n AllocatedRevenueTracking, 2\\\\\\\\\\\\\\\\n Appoinment, 3\\\\\\\\\\\\\\\\n Phonecall, 4\\\\\\\\\\\\\\\\n Chat', 
    `BusinessId` INTEGER(11), 
    `ActionType` INTEGER(11) COMMENT '1\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n Checkin, 2\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n Checkout, 3\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n Phonecall, 4\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n Treatment, 5\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n Chat', 
    `CustomerId` INTEGER(11), 
    `CustomerPhone` VARCHAR(20) COLLATE utf8mb4_unicode_ci, 
    `Note` VARCHAR(256) COLLATE utf8mb4_unicode_ci, 
    `Amount` DECIMAL(18, 2), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    `StaffBranchId` INTEGER(11), 
    PRIMARY KEY (`IncomeByJobId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `NotificationRequestApproved` (
    `NotificationRequestApprovedtId` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `NotificationId` INTEGER(11), 
    `ObjectSource` INTEGER(11) COMMENT '1 Org\\n2 Staff', 
    `ObjectId` INTEGER(11), 
    `Status` INTEGER(11) COMMENT '1 waiting, 2 approved, 3 Reject, 4 Cancel', 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `CreatedBy` INTEGER(11), 
    `UpdatedDate` DATETIME, 
    `UpdatedBy` INTEGER(11), 
    PRIMARY KEY (`NotificationRequestApprovedtId`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `RoleWorkProfilePosition_formapping` (
    `RoleId` INTEGER(11), 
    `RoleName` VARCHAR(255) COLLATE utf8mb4_unicode_ci, 
    `WorkProfilePositionId` INTEGER(11), 
    `State` TINYINT(4) DEFAULT '1', 
    `CreatedBy` INTEGER(11), 
    `CreatedDate` DATETIME DEFAULT CURRENT_TIMESTAMP, 
    `UpdatedBy` INTEGER(11), 
    `UpdatedDate` DATETIME
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

CREATE TABLE `InComeByJobConfig` (
    `InComeByJobConfig` INTEGER(11) NOT NULL AUTO_INCREMENT, 
    `BusinessTypeId` INTEGER(11) COMMENT '1) Appointment\\\\n2) Receipt', 
    `ActionTypeId` INTEGER(11) COMMENT '1) Checkin\\\\n2) Checkout\\\\n3) Phonecall\\\\n4) Chat\\\\n5) CashCollection', 
    `InComeTypeId` INTEGER(11), 
    `Price` DECIMAL(18, 2), 
    `EffectFormDate` DATE DEFAULT '1990-01-01', 
    `EffectToDate` DATE DEFAULT '2099-12-31', 
    PRIMARY KEY (`InComeByJobConfig`)
)DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_unicode_ci;

UPDATE alembic_version SET version_num='8b3baedae2d1' WHERE alembic_version.version_num = 'd927d132458a';

