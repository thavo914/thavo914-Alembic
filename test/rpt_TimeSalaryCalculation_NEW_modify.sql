DROP PROCEDURE IF EXISTS `in`.rpt_TimeSalaryCalculation_NEW;
create
    definer = dba@`%` procedure `in`.rpt_TimeSalaryCalculation_NEW(IN pFromDate date, IN pToDate date)
sp:
BEGIN
    DECLARE vPrevDate DATE;
    DECLARE vCurrEndTime TIME;
    DECLARE vPrevEndTime TIME;
    DECLARE vCurrDate DATE;
    DECLARE vCurrStartTime TIME;
    DECLARE vCurrStaffId INT;
    DECLARE vPrevStaffId INT;
    DECLARE rowCount INT DEFAULT 0;
    DECLARE i INT DEFAULT 1;

    --  generate dates
    DROP TEMPORARY TABLE IF EXISTS tempData_ListTimeKeeper;
    CREATE TEMPORARY TABLE tempData_ListTimeKeeper
    (
        StaffId               INT,
        WorkProfileId         INT,
        FirstWorkingDay       DATE,
        TerminationDate       DATE,
        WorkContractId        INT,
        TimeKeeperId          INT,
        `Date`                DATE,
        WeekDayId             TINYINT,
        MonthDayId            TINYINT,
        WorkScheduleId        INT,
        WorkShift             VARCHAR(1000),
        IsFullTime            TINYINT,
        CompanyId             TINYINT,
        BranchId              TINYINT,
        FromIp                varchar(16),
        WorkProfilePositionId INT,
        ByWeekDay             TINYINT,
        ByMonthDay            TINYINT,
        ByWorkShift           TINYINT,
        TotalBreakTimeInHour  INT UNSIGNED,
        ShiftStart            TIME,
        ShiftEnd              TIME,
        CheckInAt             TIME,
        CheckOutAt            TIME,
        ConfirmCheckIn        TIME,
        ConfirmCheckOut       TIME,
        ActualWorkingHours    DECIMAL(10, 5),
        PaidWorkingHours      DECIMAL(10, 5),
        IsEdited              tinyint,
        AbsenceTypeId         int(10) unsigned,
        AbsenceGroupType      tinyint(4),
        LeaveDays             decimal(2, 1),
        INDEX ID (`Date`)
    );

    INSERT INTO tempData_ListTimeKeeper( Date
                                       , StaffId
                                       , WeekDayId
                                       , MonthDayId)
    SELECT pFromDate + INTERVAL a.N DAY                                                                AS Date
         , b.StaffId
         , IF(WEEKDAY(pFromDate + INTERVAL a.N DAY) = 6, 1, WEEKDAY(pFromDate + INTERVAL a.N DAY) + 2) AS WeekDayId
         , DAY(pFromDate + INTERVAL a.N DAY)                                                           AS MonthDayId
    FROM (SELECT @rownum := @rownum + 1 AS N
          FROM (SELECT 1
                UNION
                SELECT 2
                UNION
                SELECT 3
                UNION
                SELECT 4
                UNION
                SELECT 5
                UNION
                SELECT 6
                UNION
                SELECT 7
                UNION
                SELECT 8
                UNION
                SELECT 9
                UNION
                SELECT 10) a,
               (SELECT 1
                UNION
                SELECT 2
                UNION
                SELECT 3
                UNION
                SELECT 4
                UNION
                SELECT 5
                UNION
                SELECT 6
                UNION
                SELECT 7
                UNION
                SELECT 8
                UNION
                SELECT 9
                UNION
                SELECT 10) b,
               (SELECT @rownum := -1) r) a
             INNER JOIN (SELECT DISTINCT k.StaffId
                         FROM `in`.TimeKeeper k
                                  INNER JOIN WorkProfile wp ON k.WorkProfileId = wp.WorkProfileId
                         WHERE k.`Day` BETWEEN pFromDate AND pToDate
                           AND (wp.IsFullTime <> 2 OR k.`Status` = 3)) b
    WHERE pFromDate + INTERVAL a.N DAY <= pToDate
    ;

    UPDATE tempData_ListTimeKeeper t INNER JOIN (SELECT k.StaffId
                                                      , k.`Day`                                           AS Date
                                                      , MIN(k.TimeKeeperId)                               AS TimeKeeperId
                                                      , TIME(FROM_UNIXTIME(MIN(k.CheckInAt)))             AS CheckInAt
                                                      , TIME(FROM_UNIXTIME(MAX(NULLIF(k.CheckOutAt, 0)))) AS CheckOutAt
                                                      , MIN(k.ConfirmCheckIn)                             AS ConfirmCheckIn
                                                      , MAX(k.ConfirmCheckOut)                            AS ConfirmCheckOut
                                                      , MAX(IFNULL(k.IsEdited, 0)) AS IsEdited
                                                 FROM TimeKeeper k
                                                          LEFT JOIN WorkProfile wp ON k.WorkProfileId = wp.WorkProfileId
                                                 WHERE k.`Day` BETWEEN pFromDate AND pToDate
                                                   AND (wp.IsFullTime <> 2 OR k.`Status` = 3)
                                                 GROUP BY k.StaffId, k.`Day`) k ON t.StaffId = k.StaffId AND t.Date = k.Date LEFT JOIN (SELECT k.StaffId
                                                                                                                                             , k.`Day`           AS Date
                                                                                                                                             , k.ConfirmCheckIn  AS ConfirmCheckIn
                                                                                                                                             , k.ConfirmCheckOut AS ConfirmCheckOut
                                                                                                                                             , IsEdited
                                                                                                                                        FROM TimeKeeper k
                                                                                                                                        WHERE k.`Day` BETWEEN pFromDate AND pToDate
                                                                                                                                          AND IsEdited = 1) k1 ON t.StaffId = k1.StaffId AND t.Date = k1.Date
    SET t.TimeKeeperId    = k.TimeKeeperId
      , t.CheckInAt       = IFNULL(k1.ConfirmCheckIn, k.CheckInAt)
      , t.CheckOutAt      = IFNULL(k1.ConfirmCheckOut, k.CheckOutAt)
      , t.ConfirmCheckIn  = IFNULL(k1.ConfirmCheckIn, k.ConfirmCheckIn)
      , t.ConfirmCheckOut = IFNULL(k1.ConfirmCheckOut, k.ConfirmCheckOut)
      , t.IsEdited        = IFNULL(k1.IsEdited, k.IsEdited);


    -- delete the edited days that have IsEdited = 0, for preventing duplicated data
#     DELETE t1
#     FROM tempData_ListTimeKeeper t1
#              INNER JOIN (SELECT DISTINCT StaffId, Day AS Date
#                          FROM TimeKeeper
#                          WHERE IsEdited = 1 AND Day >= pFromDate AND Day <= pToDate) t2
#                         ON t1.StaffId = t2.StaffId AND t1.Date = t2.Date
#     WHERE IsEdited = 0;

    -- 240830 get CompanyId column for update
    -- 240830 Update TotalPaidHour for LABO company (CompanyId=12), working type is PK(IsFullTime = 2)


    UPDATE tempData_ListTimeKeeper t
        INNER JOIN (SELECT StaffId, MAX(WorkProfileId) AS WorkProfileId
                                                 FROM TimeKeeper
                                                 WHERE `Day` BETWEEN pFromDate AND pToDate
                                                 GROUP BY StaffId) k ON t.StaffId = k.StaffId
    SET t.WorkProfileId = k.WorkProfileId;


    -- Get the last time the staff Check in/out

    DROP TEMPORARY TABLE IF EXISTS tempData_LastChecking;
    CREATE TEMPORARY TABLE tempData_LastChecking AS
    SELECT StaffId, MAX(TimeKeeperId) AS TimeKeeperId FROM tempData_ListTimeKeeper GROUP BY StaffId;


    UPDATE tempData_ListTimeKeeper t INNER JOIN WorkProfile wp ON t.WorkProfileId = wp.WorkProfileId
        LEFT JOIN (SELECT WorkContractId, MAX(WorkContractAnnexId) AS WorkContractAnnexId
                   FROM WorkContractAnnex wca
                   WHERE wca.AvailableDate <= pToDate
                     AND IFNULL(wca.ExpiredDate, pToDate) >= pToDate
                   GROUP BY WorkContractId) wca1 ON wp.WorkContractId = wca1.WorkContractId
        LEFT JOIN WorkContractAnnex wca ON wca.WorkContractAnnexId = wca1.WorkContractAnnexId
        LEFT JOIN (SELECT WorkContractId, MAX(WorkPlaceChangingId) AS WorkPlaceChangingId
                   FROM WorkPlaceChanging wpc
                   WHERE wpc.AvailableFrom <= pToDate
                     AND IFNULL(wpc.EndDate, pToDate) >= pToDate
                   GROUP BY WorkContractId) wpc1 ON wp.WorkContractId = wpc1.WorkContractId
        LEFT JOIN WorkPlaceChanging wpc ON wpc.WorkPlaceChangingId = wpc1.WorkPlaceChangingId
    SET t.BranchId = IFNULL(wpc.BranchId, wp.BranchId),
        t.WorkProfilePositionId = IFNULL(wca.WorkProfilePositionId, wp.WorkProfilePositionId),
        t.IsFullTime            = wp.IsFullTime,
        t.CompanyId             = wp.CompanyId,
        t.WorkContractId        = wp.WorkContractId;

    -- Update type of contract, WorkSchedule for the Staff

    UPDATE tempData_ListTimeKeeper t INNER JOIN WorkSchedule ws ON ws.StaffId = t.StaffId
    SET t.WorkScheduleId = ws.WorkScheduleId
      , t.ByWeekDay      = ws.ByWeekDay
      , t.ByMonthDay     = ws.ByMonthDay
      , t.ByWorkShift    = ws.ByWorkShift
    WHERE t.`Date` BETWEEN ws.StartDate AND ws.EndDate;

    DROP TEMPORARY TABLE IF EXISTS tempWorkShift_ListTimeKeeper;
    CREATE TEMPORARY TABLE tempWorkShift_ListTimeKeeper
    (
        Id                   INT,
        `Date`               DATE,
        StaffId              INT,
        WorkScheduleId       INT,
        WorkShiftId          INT,
        WorkShift            VARCHAR(50),
        StartTime            TIME,
        EndTime              TIME,
        TotalBreakTimeInHour INT,
        UNIQUE INDEX IX_Date (`Date`, WorkScheduleId, WorkShiftId)
    );

    -- insert data for work shift by week if it has
    INSERT IGNORE INTO tempWorkShift_ListTimeKeeper (`Date`, StaffId, WorkScheduleId, WorkShiftId)
    SELECT DISTINCT t.`Date`, t.StaffId, t.WorkScheduleId, wsw.WorkShiftId
    FROM tempData_ListTimeKeeper t
             INNER JOIN WorkShiftByWeekDay wsw ON t.WorkScheduleId = wsw.WorkScheduleId AND t.WeekDayId = wsw.WeekDayId
    WHERE t.ByWeekDay = 1
      AND t.IsFullTime = 2;


    -- insert data for work shift by month if it has
    INSERT IGNORE INTO tempWorkShift_ListTimeKeeper (`Date`, StaffId, WorkScheduleId, WorkShiftId)
    SELECT DISTINCT t.`Date`, t.StaffId, t.WorkScheduleId, wsw.WorkShiftId
    FROM tempData_ListTimeKeeper t
             INNER JOIN WorkShiftByMonthDay wsw
                        ON t.WorkScheduleId = wsw.WorkScheduleId AND DAY(t.`Date`) = wsw.MonthDayId
    WHERE t.ByMonthDay = 1
      AND t.IsFullTime = 2;
    -- delete exclude work shift means that there are some work shifts that have planed, and we'd like to remove those
    DELETE t
    FROM tempWorkShift_ListTimeKeeper t
             INNER JOIN InfrequentExcludeWorkShift e ON t.WorkScheduleId = e.WorkScheduleId AND t.`Date` = e.`Date` AND
                                                        t.WorkShiftId = e.WorkShiftId;
    -- insert include work shift that means insert work shift that we don't plan as before
    INSERT IGNORE INTO tempWorkShift_ListTimeKeeper (`Date`, StaffId, WorkScheduleId, WorkShiftId)
    SELECT t.`Date`, t.StaffId, t.WorkScheduleId, i.WorkShiftId
    FROM tempData_ListTimeKeeper t
             INNER JOIN InfrequentIncludeWorkShift i ON t.WorkScheduleId = i.WorkScheduleId AND t.`Date` = i.`Date`;

    -- update start time and end tine of work shift
    UPDATE tempWorkShift_ListTimeKeeper t INNER JOIN WorkShift ws ON t.WorkShiftId = ws.WorkShiftId
    SET t.WorkShift = ws.`Name`
      , t.StartTime = ws.StartTime
      , t.EndTime   = ws.EndTime;

    -- calculate break time between broken shifts
    SET @row_number = 0;
    UPDATE tempWorkShift_ListTimeKeeper SET Id = (@row_number := @row_number + 1) ORDER BY StaffId, `Date`, StartTime;
    SELECT COUNT(*) INTO rowCount FROM tempWorkShift_ListTimeKeeper;
    WHILE i <= rowCount
        DO
            SELECT StaffId, Date, StartTime, EndTime
            INTO vCurrStaffId,vCurrDate, vCurrStartTime, vCurrEndTime
            FROM tempWorkShift_ListTimeKeeper
            WHERE Id = i;
            -- If the current row is on the same day as the previous row, calculate break time
#                 SELECT i, vPrevDate,vCurrDate,vCurrStaffId,vPrevStaffId;

            IF vPrevDate = vCurrDate AND vCurrStaffId = vPrevStaffId THEN
                UPDATE tempWorkShift_ListTimeKeeper
                SET TotalBreakTimeInHour = IFNULL(
                        ROUND((TIME_TO_SEC(vCurrStartTime) - TIME_TO_SEC(vPrevEndTime)) / 3600, 2), 0)
                WHERE  Id = i;
            END IF;

            SET vPrevStaffId = vCurrStaffId;
            SET vPrevDate = vCurrDate;
            SET vPrevEndTime = vCurrEndTime;
            SET i = i + 1;
        END WHILE;

    -- insert work shifts for Back Office 40h
    INSERT INTO tempWorkShift_ListTimeKeeper (`Date`, StaffId, WorkScheduleId, WorkShiftId, WorkShift, StartTime,
                                              EndTime,
                                              TotalBreakTimeInHour)
    SELECT t.`Date`,
           t.StaffId,
           t.WorkScheduleId,
           w.WorkShiftId,
           'Ca hành chính',
           w.StartTime,
           w.EndTime,
           0
    FROM tempData_ListTimeKeeper t
       , (SELECT 0 AS WorkShiftId, CAST('08:00' AS TIME) AS StartTime, CAST('12:00' AS TIME) AS EndTime
          UNION ALL
          SELECT 1, CAST('13:30' AS TIME), CAST('17:30' AS TIME)) w
    WHERE t.IsFullTime = 1
      AND t.WeekDayId BETWEEN 2 AND 6;

    -- insert work shifts for Back Office 48h
    INSERT INTO tempWorkShift_ListTimeKeeper (`Date`, StaffId, WorkScheduleId, WorkShiftId, WorkShift, StartTime,
                                              EndTime,
                                              TotalBreakTimeInHour)
    SELECT t.`Date`,
           t.StaffId,
           t.WorkScheduleId,
           w.WorkShiftId,
           'Ca hành chính',
           w.StartTime,
           w.EndTime,
           0
    FROM tempData_ListTimeKeeper t
       , (SELECT 0 AS WorkShiftId, CAST('08:00' AS TIME) AS StartTime, CAST('12:00' AS TIME) AS EndTime
          UNION ALL
          SELECT 1, CAST('13:30' AS TIME), CAST('17:30' AS TIME)) w
    WHERE t.IsFullTime = 3;

    UPDATE tempData_ListTimeKeeper t INNER JOIN (SELECT `Date`
                                                      , StaffId
                                                      , GROUP_CONCAT(WorkShift, ' (', TIME_FORMAT(StartTime, '%H:%i'),
                                                                     ' - ', TIME_FORMAT(EndTime, '%H:%i'), ')' SEPARATOR
                                                                     ', ')        AS WorkShift
                                                      , MIN(StartTime)            AS StartTime
                                                      , MAX(EndTime)              AS EndTime
                                                      , SUM(TotalBreakTimeInHour) AS TotalBreakTimeInHour
                                                 FROM tempWorkShift_ListTimeKeeper
                                                 GROUP BY `Date`, StaffId) k ON t.`Date` = k.`Date`  AND
                                                                                                t.StaffId = k.StaffId
    SET t.WorkShift  = IF(t.IsFullTime <> 2, 'Ca hành chính (08:00 - 17:30)', k.WorkShift)
      , t.ShiftStart = IF(t.IsFullTime <> 2, '08:00', k.StartTime)
      , t.ShiftEnd   = IF(t.IsFullTime <> 2, '17:30', k.EndTime)
      , t.TotalBreakTimeInHour = k.TotalBreakTimeInHour;


    DROP TEMPORARY TABLE IF EXISTS tempLeaveDay_Detail;
    CREATE TEMPORARY TABLE tempLeaveDay_Detail
    (
        StaffId          int(10) unsigned,
        Date             date,
        AbsenceTypeId    int(10) unsigned,
        AbsenceGroupType tinyint(4),
        LeaveDays        decimal(2, 1),
        UNIQUE INDEX UID (StaffId, `Date`)
    );
    INSERT INTO tempLeaveDay_Detail ( StaffId
                                    , Date
                                    , AbsenceTypeId
                                    , AbsenceGroupType
                                    , LeaveDays)
    SELECT r.RequestedBy                                                                          AS StaffId
         , d.`Date`
         , r.AbsenceTypeId
         , t.AbsenceGroupType
         , if(SUM(TIME_TO_SEC(TIMEDIFF(d.AbsenceToTime, d.AbsenceFromTime))) / 3600 >= 8, 1, 0.5) as LeaveDays
    FROM AbsenceRequest r
             INNER JOIN AbsenceType t ON r.AbsenceTypeId = t.AbsenceTypeId
             INNER JOIN AbsenceRequestDetail d ON r.AbsenceRequestId = d.AbsenceRequestId
    WHERE d.`Date` BETWEEN pFromDate AND pToDate
      AND r.RequestStatus = 1
    GROUP BY r.RequestedBy, d.`Date`, r.AbsenceTypeId, AbsenceGroupType
;
    -- some staffs didn't check in, but they have absence days, we have to insert these staffs
    DROP TEMPORARY TABLE IF EXISTS tempLeaveDay_Detail_NotCheckin;
    CREATE TEMPORARY TABLE tempLeaveDay_Detail_NotCheckin AS
    SELECT a.StaffId, a.`Date`, IFNULL(wca.WorkProfilePositionId, wp.WorkProfilePositionId) AS WorkProfilePositionId, wp.IsFullTime
    FROM tempLeaveDay_Detail a
             INNER JOIN WorkProfile wp ON a.StaffId = wp.StaffId
             INNER JOIN(SELECT StaffId, MAX(WorkProfileId) AS WorkProfileId FROM WorkProfile WHERE FromDate <= pToDate GROUP BY StaffId) wp1
                       ON a.StaffId = wp1.StaffId AND wp.WorkProfileId = wp1.WorkProfileId
             LEFT JOIN (SELECT WorkContractId, MAX(WorkContractAnnexId) AS WorkContractAnnexId
                        FROM WorkContractAnnex wca
                        WHERE wca.AvailableDate <= pToDate
                          AND IFNULL(wca.ExpiredDate, pToDate) >= pToDate
                        GROUP BY WorkContractId) wca1 ON wp.WorkContractId = wca1.WorkContractId
             LEFT JOIN WorkContractAnnex wca ON wca.WorkContractAnnexId = wca1.WorkContractAnnexId
             LEFT JOIN (SELECT DISTINCT StaffId FROM tempData_ListTimeKeeper) o ON a.StaffId = o.StaffId
    WHERE  o.StaffId IS NULL;

    INSERT INTO tempData_ListTimeKeeper(StaffId, `Date`, WorkProfilePositionId, IsFullTime)
    SELECT StaffId, `Date`, WorkProfilePositionId, IsFullTime
    FROM tempLeaveDay_Detail_NotCheckin;

    UPDATE tempData_ListTimeKeeper k INNER JOIN tempLeaveDay_Detail l ON k.StaffId = l.StaffId AND k.Date = l.Date
    SET k.AbsenceTypeId    = l.AbsenceTypeId,
        k.AbsenceGroupType = l.AbsenceGroupType,
        k.LeaveDays        = l.LeaveDays;
    -- calculate holiday leaves, count the days between FirstWorkingDay and TerminationDate(if it has)
    UPDATE tempData_ListTimeKeeper t INNER JOIN (SELECT wp.StaffId,
                                                        wc1.FromDate       AS FirstWorkingDay,
                                                        wc.TerminationDate AS TerminationDate
                                                 FROM WorkProfile wp
                                                          INNER JOIN (SELECT StaffId, MAX(WorkProfileId) AS WorkProfileId
                                                                      FROM WorkProfile
                                                                      WHERE FromDate <= pToDate
                                                                      GROUP BY StaffId) wp1
                                                                     ON wp.StaffId = wp1.StaffId AND wp.WorkProfileId = wp1.WorkProfileId
                                                          INNER JOIN (SELECT StaffId, MIN(wp.FromDate) AS FromDate
                                                                      FROM WorkProfile wp
                                                                               INNER JOIN WorkContract wc ON wp.WorkContractId = wc.WorkContractId
                                                                      WHERE WorkContractTypeId IN (1, 2, 3, 9, 14)
                                                                      GROUP BY StaffId) wc1 ON wc1.StaffId = wp.StaffId
                                                          INNER JOIN WorkContract wc ON wp.WorkContractId = wc.WorkContractId) wp ON t.StaffId = wp.StaffId
    SET t.FirstWorkingDay = wp.FirstWorkingDay,
        t.TerminationDate = wp.TerminationDate;

    DROP TEMPORARY TABLE IF EXISTS tempHolidays;
    CREATE TEMPORARY TABLE tempHolidays AS
    SELECT d.StaffId, COUNT(h.Date) AS Holidays
    FROM `in`.Holiday h
             INNER JOIN (SELECT DISTINCT StaffId, FirstWorkingDay, TerminationDate FROM tempData_ListTimeKeeper) d
    WHERE Date >= pFromDate
      AND Date <= pToDate
      AND h.IsHoliday=1
      AND h.Date >= FirstWorkingDay
      AND h.Date <= IFNULL(TerminationDate,pToDate)
    GROUP BY d.StaffId;


    -- If the data has been edited, PaidWorkingHour does not depend on the work shift.
    -- Otherwise, check-in times earlier than the shift's start time and check-out times later than the shift's end time are not allowed.
    UPDATE tempData_ListTimeKeeper t
    SET ActualWorkingHours = GREATEST(0, IFNULL(TIME_TO_SEC(TIMEDIFF(t.CheckOutAt, t.CheckInAt)) / 3600, 0) -
                             IFNULL(TotalBreakTimeInHour,0)) ,
        PaidWorkingHours = GREATEST(0, CASE
                                           WHEN IsEdited = 1 THEN
                                               IFNULL(TIME_TO_SEC(TIMEDIFF(t.ConfirmCheckOut, t.ConfirmCheckIn)) / 3600,
                                                      0) - IFNULL(TotalBreakTimeInHour,0)
            -- if the staff was a doctor or a cleaner or belongs to LABO company( CompanyId =12), check in check out aren't depend on the work shift.
                                           WHEN WorkProfilePositionId IN (478, 580) OR  (t.CompanyId = 12 AND t.IsFullTime = 2) THEN IFNULL(
                                                   TIME_TO_SEC(TIMEDIFF(IFNULL(t.ConfirmCheckOut, t.CheckOutAt),
                                                                        IFNULL(t.ConfirmCheckIn, t.CheckInAt))) / 3600,
                                                   0)
                                           WHEN IsEdited != 1 THEN IFNULL(TIME_TO_SEC(TIMEDIFF(
                                                   IF(IFNULL(t.ConfirmCheckOut, t.CheckOutAt) > t.ShiftEnd, t.ShiftEnd,
                                                      IFNULL(t.ConfirmCheckOut, t.CheckOutAt)),
                                                   IF(IFNULL(t.ConfirmCheckIn, t.CheckInAt) < t.ShiftStart,
                                                      t.ShiftStart, IFNULL(t.ConfirmCheckIn, t.CheckInAt)))) / 3600,
                                                                          0) - IFNULL(TotalBreakTimeInHour,0) END);



    DROP TEMPORARY TABLE IF EXISTS tempResult;
    CREATE TEMPORARY TABLE tempResult
    SELECT s.StaffId,
           s.StaffCode                                                                              AS StaffCode,
           s.FullName                                                                               AS FullName,
           wpp.Name                                                                                 AS WorkProfilePosition,
           CASE t.IsFullTime WHEN 1 THEN 'VP 40h' WHEN 2 THEN 'PK' WHEN 3 THEN 'VP 48h' ELSE '' END AS WorkingType,
           BranchCode                                                                               AS BranchCode,
           t.FirstWorkingDay,
           t.TerminationDate,
           SUM(PaidWorkingHours)                                                                    AS TotalPaidWorkingDays,
           SUM(CASE
               -- applies for LABO
                   WHEN t.CompanyId = 12 AND t.IsFullTime = 2 AND PaidWorkingHours >= 8 THEN 1
                   WHEN t.CompanyId = 12 AND t.IsFullTime = 2 AND PaidWorkingHours < 8 AND PaidWorkingHours >= 3
                       THEN ROUND(PaidWorkingHours / 8, 2)
                   WHEN t.CompanyId = 12 AND t.IsFullTime = 2 AND PaidWorkingHours < 3 THEN 0
               -- applies for Phụ tá, Phụ tá trưởng, QLPK, TVV, Quyền QLPK, Bác sĩ RHM
                   WHEN t.WorkProfilePositionId = 580 THEN ROUND(PaidWorkingHours / 8, 2)
                   WHEN PaidWorkingHours >= 3 AND t.WorkProfilePositionId IN (586, 582, 592, 632, 686, 690)
                       THEN ROUND(PaidWorkingHours / 8, 2)
                   WHEN PaidWorkingHours < 3 AND t.WorkProfilePositionId IN (586, 582, 592, 632, 686, 690) THEN 0.00

               -- remaining positions
                   WHEN t.WorkProfilePositionId NOT IN (586, 582, 592, 632, 686, 580, 690) AND PaidWorkingHours > 5
                       THEN 1
                   WHEN t.WorkProfilePositionId NOT IN (586, 582, 592, 632, 686, 580, 690) AND PaidWorkingHours > 0
                       THEN 0.5
                   ELSE 0 END)                                                                      AS WorkingDays,
           SUM(CASE WHEN AbsenceTypeId = 1 THEN LeaveDays ELSE 0 END)                               AS AnnualLeaves,
           SUM(CASE WHEN AbsenceTypeId IN (2, 3, 8) THEN LeaveDays ELSE 0 END)                      AS CompassionateFuneralLeaves,
           SUM(CASE WHEN AbsenceTypeId = 7 THEN LeaveDays ELSE 0 END)                               AS TrainingLeaves
#            h.Holidays                                                                               AS Holidays
    FROM tempData_ListTimeKeeper t
             INNER JOIN Staff s ON t.StaffId = s.StaffId
             LEFT JOIN Branch b ON t.BranchId = b.BranchId
             LEFT JOIN WorkProfilePosition wpp ON t.WorkProfilePositionId = wpp.WorkProfilePositionId
#     WHERE t.StaffId = 5798
    GROUP BY t.FirstWorkingDay, t.TerminationDate, s.StaffId, s.StaffCode, s.FullName, wpp.Name, t.IsFullTime,
             BranchCode;

    SELECT t.StaffId                                                                                        AS 'ID Nhân viên'
         , StaffCode                                                                                        AS 'Mã nhân viên'
         , FullName                                                                                         AS 'Họ tên nhân viên'
         , WorkProfilePosition                                                                              AS 'Chức danh'
         , WorkingType                                                                                      AS 'Khối'
         , FirstWorkingDay                                                                                  AS 'Ngày vào làm'
         , TerminationDate                                                                                  AS 'Ngày kết thúc'
         , BranchCode                                                                                       AS 'Bộ phận/phòng khám'
         , ROUND(TotalPaidWorkingDays, 1)                                                                   AS 'Tổng giờ làm việc thực tế trong tháng'
         , WorkingDays                                                                                      AS 'Tổng ngày làm việc thực tế trong tháng'
         , AnnualLeaves                                                                                     AS 'Nghỉ phép năm'
         , CompassionateFuneralLeaves                                                                       AS 'Nghỉ Hiếu hỉ/tang chế'
         , TrainingLeaves                                                                                   AS 'Nghỉ phép đào tạo'
         , IFNULL(h.Holidays, 0)                                                                            AS 'Ngày lễ'
         , WorkingDays + AnnualLeaves + CompassionateFuneralLeaves + TrainingLeaves +
           IFNULL(h.Holidays, 0)                                                                            AS 'Tổng công tính lương'
    FROM tempResult t
             LEFT JOIN tempHolidays h ON t.StaffId = h.StaffId;

END;

CALL rpt_TimeSalaryCalculation_NEW('2025-02-01', '2025-02-28');


# CALL rpt_TimeSalaryCalculation_NEW_modify('2024-12-01', '2024-12-05');

# Name,AbsenceGroupType,LeaveDays
# Nghỉ phép năm,1,0.5
# Nghỉ phép năm,1,1
# Nghỉ phép Hiếu Hỉ,1,2.0
# Nghỉ phép Hiếu Hỉ,1,1.0
#
# Nghỉ phép năm,Nghỉ phép Hiếu Hỉ
# 1.5,3.0
#

# NKK0001A

# SELECT * FROM Staff;

# NKK01900
# NKK02711
# NKK02734
# NKK03271
# NKK03426
