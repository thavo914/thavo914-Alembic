import pandas as pd
import numpy as np
from datetime import datetime, date, time, timedelta

def usp_timekeeper_detail_manual(p_from_date, p_to_date):
    """
    Python implementation of usp_TimeKeeper_Detail_Manual stored procedure
    
    Parameters:
    -----------
    p_from_date : str or datetime.date
        Start date for the time period to analyze
    p_to_date : str or datetime.date
        End date for the time period to analyze
        
    Returns:
    --------
    pandas.DataFrame
        Final timekeeper detail report
    """
    # Convert string dates to datetime.date if needed
    if isinstance(p_from_date, str):
        p_from_date = pd.to_datetime(p_from_date).date()
    if isinstance(p_to_date, str):
        p_to_date = pd.to_datetime(p_to_date).date()
    
    # Step 1: Create temporary TimeKeeper_Detail DataFrame
    # Simulating the initial query that joins TimeKeeper with WorkProfile
    # Note: You would replace these with actual database queries
    
    # Example of how you would load data from your database
    # timekeeper_df = pd.read_sql("SELECT * FROM TimeKeeper WHERE Day BETWEEN %s AND %s", 
    #                           connection, params=[p_from_date, p_to_date])
    # workprofile_df = pd.read_sql("SELECT * FROM WorkProfile", connection)
    
    # For demonstration, we'll create empty DataFrames with the right structure
    timekeeper_df = pd.DataFrame()  # Replace with actual query
    workprofile_df = pd.DataFrame()  # Replace with actual query
    
    # Initial query logic - in a real implementation, this would use actual data
    temp_timekeeper_detail = pd.DataFrame({
        'StaffId': [],
        'Date': [],
        'WeekDayId': [],
        'MonthDayId': [],
        'IsFullTime': [],
        'CompanyId': [],
        'BranchId': [],
        'WorkProfilePositionId': [],
        'WorkProfileId': [],
        'WorkShift': [],
        'WorkScheduleId': [],
        'ByWeekDay': [],
        'ByMonthDay': [],
        'ByWorkShift': [],
        'TimeKeeperId': [],
        'ShiftStart': [],
        'ShiftEnd': [],
        'CheckIn': [],
        'CheckOut': [],
        'TotalBreakTimeInHour': [],
        'ConfirmCheckIn': [],
        'ConfirmCheckOut': [],
        'IsEdited': [],
        'TotalHour': [],
        'TotalPaidHour': []
    })
    
    # In a real implementation, you would execute the SQL equivalent:
    # SELECT k.StaffId, k.`Day` as Date, ...
    # FROM TimeKeeper k
    # INNER JOIN WorkProfile wp ON k.WorkProfileId = wp.WorkProfileId
    # WHERE k.`Day` BETWEEN p_from_date AND p_to_date
    # AND (wp.IsFullTime <> 2 OR k.`Status` = 3)
    # GROUP BY k.StaffId, k.`Day`, wp.IsFullTime, wp.CompanyId, k.IsEdited
    
    # Step 2: Remove edited days with IsEdited = 0 (avoid duplication)
    if not temp_timekeeper_detail.empty:
        # Get all StaffId, Date combinations where IsEdited = 1
        edited_records = pd.DataFrame()  # Replace with actual query for edited records
        
        # Filter out records that would be duplicated
        if not edited_records.empty:
            merge_key = temp_timekeeper_detail.merge(
                edited_records, 
                on=['StaffId', 'Date'], 
                how='inner'
            )
            temp_timekeeper_detail = temp_timekeeper_detail[
                ~((temp_timekeeper_detail['StaffId'].isin(merge_key['StaffId'])) & 
                  (temp_timekeeper_detail['Date'].isin(merge_key['Date'])) & 
                  (temp_timekeeper_detail['IsEdited'] == 0))
            ]
    
    # Step 3: Update WorkProfileId
    # In real implementation, get the max WorkProfileId for each StaffId
    # from TimeKeeper where Day is between p_from_date and p_to_date
    
    # Step 4: Update various fields by joining with other tables
    # WorkProfile, WorkContract, WorkContractAnnex, WorkPlaceChanging
    
    # Step 5: Update WorkSchedule information
    
    # Step 6: Create and populate tempWorkShift_ListTimeKeeper
    temp_workshift_list = pd.DataFrame({
        'Id': [],
        'Date': [],
        'StaffId': [],
        'WorkScheduleId': [],
        'WorkShiftId': [],
        'WorkShift': [],
        'StartTime': [],
        'EndTime': [],
        'TotalBreakTimeInHour': []
    })
    
    # Insert data for work shift by week
    # Insert data for work shift by month
    # Delete exclude work shifts
    # Insert include work shifts
    # Update start time and end time of work shifts
    
    # Step 7: Calculate break times between broken shifts
    if not temp_workshift_list.empty:
        # Sort by StaffId, Date, StartTime and assign Id
        temp_workshift_list = temp_workshift_list.sort_values(['StaffId', 'Date', 'StartTime'])
        temp_workshift_list['Id'] = range(1, len(temp_workshift_list) + 1)
        
        # Initialize variables for break time calculation
        prev_staff_id = None
        prev_date = None
        prev_end_time = None
        
        # Calculate break times - equivalent to the WHILE loop in SQL
        break_times = []
        
        for idx, row in temp_workshift_list.iterrows():
            curr_staff_id = row['StaffId']
            curr_date = row['Date']
            curr_start_time = row['StartTime']
            curr_end_time = row['EndTime']
            
            break_time = 0
            if prev_date == curr_date and curr_staff_id == prev_staff_id and prev_end_time is not None:
                # Calculate break time in hours
                start_seconds = pd.Timestamp(curr_start_time).hour * 3600 + pd.Timestamp(curr_start_time).minute * 60
                end_seconds = pd.Timestamp(prev_end_time).hour * 3600 + pd.Timestamp(prev_end_time).minute * 60
                break_time = round((start_seconds - end_seconds) / 3600, 2)
                if break_time < 0:
                    break_time = 0
            
            break_times.append(break_time)
            
            prev_staff_id = curr_staff_id
            prev_date = curr_date
            prev_end_time = curr_end_time
        
        temp_workshift_list['TotalBreakTimeInHour'] = break_times
    
    # Step 8: Insert work shifts for Back Office 40h and 48h
    # Create standard shifts for administrative staff
    admin_shifts = []
    
    # For each relevant staff member and date, add morning and afternoon shifts
    if not temp_timekeeper_detail.empty:
        for idx, row in temp_timekeeper_detail[
            (temp_timekeeper_detail['IsFullTime'] == 1) & 
            (temp_timekeeper_detail['WeekDayId'].between(2, 6))
        ].iterrows():
            # Morning shift
            admin_shifts.append({
                'Date': row['Date'],
                'StaffId': row['StaffId'],
                'WorkScheduleId': row['WorkScheduleId'],
                'WorkShiftId': 0,
                'WorkShift': 'Ca hành chính',
                'StartTime': time(8, 0),
                'EndTime': time(12, 0),
                'TotalBreakTimeInHour': 0
            })
            # Afternoon shift
            admin_shifts.append({
                'Date': row['Date'],
                'StaffId': row['StaffId'],
                'WorkScheduleId': row['WorkScheduleId'],
                'WorkShiftId': 1,
                'WorkShift': 'Ca hành chính',
                'StartTime': time(13, 30),
                'EndTime': time(17, 30),
                'TotalBreakTimeInHour': 0
            })
        
        # Similar logic for 48h staff (IsFullTime = 3)
        for idx, row in temp_timekeeper_detail[temp_timekeeper_detail['IsFullTime'] == 3].iterrows():
            # Morning shift
            admin_shifts.append({
                'Date': row['Date'],
                'StaffId': row['StaffId'],
                'WorkScheduleId': row['WorkScheduleId'],
                'WorkShiftId': 0,
                'WorkShift': 'Ca hành chính',
                'StartTime': time(8, 0),
                'EndTime': time(12, 0),
                'TotalBreakTimeInHour': 0
            })
            # Afternoon shift
            admin_shifts.append({
                'Date': row['Date'],
                'StaffId': row['StaffId'],
                'WorkScheduleId': row['WorkScheduleId'],
                'WorkShiftId': 1,
                'WorkShift': 'Ca hành chính',
                'StartTime': time(13, 30),
                'EndTime': time(17, 30),
                'TotalBreakTimeInHour': 0
            })
    
    # Append admin shifts to temp_workshift_list
    if admin_shifts:
        admin_shifts_df = pd.DataFrame(admin_shifts)
        temp_workshift_list = pd.concat([temp_workshift_list, admin_shifts_df], ignore_index=True)
    
    # Step 9: Update WorkShift information in temp_timekeeper_detail
    if not temp_workshift_list.empty and not temp_timekeeper_detail.empty:
        # Group by Date and StaffId to get consolidated shift information
        shift_summary = temp_workshift_list.groupby(['Date', 'StaffId']).agg({
            'WorkShift': lambda x: ', '.join([f"{s} ({start.strftime('%H:%M')} - {end.strftime('%H:%M')})" 
                                            for s, start, end in zip(x, 
                                                                    temp_workshift_list.loc[x.index, 'StartTime'],
                                                                    temp_workshift_list.loc[x.index, 'EndTime'])]),
            'StartTime': 'min',
            'EndTime': 'max',
            'TotalBreakTimeInHour': 'sum'
        }).reset_index()
        
        # Update temp_timekeeper_detail with shift information
        for idx, row in shift_summary.iterrows():
            mask = (temp_timekeeper_detail['Date'] == row['Date']) & (temp_timekeeper_detail['StaffId'] == row['StaffId'])
            
            temp_timekeeper_detail.loc[mask, 'WorkShift'] = np.where(
                temp_timekeeper_detail.loc[mask, 'IsFullTime'] != 2,
                'Ca hành chính (08:00 - 17:30)',
                row['WorkShift']
            )
            
            temp_timekeeper_detail.loc[mask, 'ShiftStart'] = np.where(
                temp_timekeeper_detail.loc[mask, 'IsFullTime'] != 2,
                time(8, 0),
                row['StartTime']
            )
            
            temp_timekeeper_detail.loc[mask, 'ShiftEnd'] = np.where(
                temp_timekeeper_detail.loc[mask, 'IsFullTime'] != 2,
                time(17, 30),
                row['EndTime']
            )
            
            temp_timekeeper_detail.loc[mask, 'TotalBreakTimeInHour'] = np.where(
                temp_timekeeper_detail.loc[mask, 'IsFullTime'] != 2,
                0,
                row['TotalBreakTimeInHour']
            )
    
    # Step 10: Final query to get the report
    # Assuming we have Staff, Branch, and WorkProfilePosition tables
    staff_df = pd.DataFrame()  # Replace with actual query
    branch_df = pd.DataFrame()  # Replace with actual query
    wpp_df = pd.DataFrame()  # Replace with actual query
    
    # Join with Staff, Branch, and WorkProfilePosition
    if not temp_timekeeper_detail.empty:
        # Merge with Staff
        result = pd.merge(
            temp_timekeeper_detail,
            staff_df[staff_df['IsTest'] == 0],
            on='StaffId',
            how='inner'
        )
        
        # Merge with Branch
        result = pd.merge(
            result,
            branch_df,
            on='BranchId',
            how='left'
        )
        
        # Merge with WorkProfilePosition
        result = pd.merge(
            result,
            wpp_df,
            on='WorkProfilePositionId',
            how='left'
        )
        
        # Calculate fields for final output
        
        # Function to create timestamp from date and time
        def create_timestamp(row, date_col, time_col):
            if pd.isna(row[time_col]):
                return None
            return pd.Timestamp.combine(row[date_col], row[time_col])
        
        # Create check-in and check-out timestamps
        result['Thời gian CheckIn'] = result.apply(
            lambda row: create_timestamp(
                row, 
                'Date', 
                'ConfirmCheckIn' if row['IsEdited'] == 1 else 'CheckIn'
            ), 
            axis=1
        )
        
        result['Thời gian CheckOut'] = result.apply(
            lambda row: create_timestamp(
                row, 
                'Date', 
                'ConfirmCheckOut' if row['IsEdited'] == 1 else 'CheckOut'
            ), 
            axis=1
        )
        
        # Calculate 'Tổng số giờ theo ca'
        result['Tổng số giờ theo ca'] = result.apply(
            lambda row: 9.5 if row['IsFullTime'] != 2 else max(
                0, 
                (pd.Timestamp.combine(date.today(), row['ShiftEnd']) - 
                 pd.Timestamp.combine(date.today(), row['ShiftStart'])).total_seconds() / 3600 - 
                (row['TotalBreakTimeInHour'] or 0)
            ),
            axis=1
        )
        
        # Calculate 'Thời gian làm thực tế'
        result['Thời gian làm thực tế'] = result.apply(
            lambda row: calculate_working_time(row),
            axis=1
        )
        
        # Map IsFullTime to 'Khối'
        result['Khối'] = result['IsFullTime'].map({
            1: 'VP 40h',
            2: 'PK',
            3: 'VP 48h'
        }).fillna('')
        
        # Calculate 'Ngày công'
        result['Ngày công'] = result.apply(
            lambda row: calculate_work_day(row),
            axis=1
        )
        
        # Select and rename columns for final output
        final_result = result[[
            'Date', 'StaffId', 'StaffCode', 'FullName', 'Name', 'BranchCode',
            'Thời gian CheckIn', 'Thời gian CheckOut', 'WorkShift',
            'TotalBreakTimeInHour', 'ShiftStart', 'ShiftEnd',
            'Tổng số giờ theo ca', 'Thời gian làm thực tế', 'Khối', 'Ngày công'
        ]].rename(columns={
            'Date': 'Ngày',
            'StaffId': 'ID nhân viên',
            'StaffCode': 'Mã nhân viên',
            'FullName': 'Tên nhân viên',
            'Name': 'Chức danh',
            'WorkShift': 'Ca làm việc',
            'TotalBreakTimeInHour': 'Giờ trống ca gãy',
            'ShiftStart': 'Thời gian bắt đầu ca',
            'ShiftEnd': 'Thời gian kết thúc ca'
        })
        
        # Sort by StaffId and Date
        final_result = final_result.sort_values(['ID nhân viên', 'Ngày'])
        
        return final_result
    
    # Return empty DataFrame if no data
    return pd.DataFrame()

def calculate_working_time(row):
    """Helper function to calculate actual working time based on complex business rules"""
    if row['IsEdited'] == 1:
        # For edited records, use confirmed times
        working_time = (
            (pd.Timestamp.combine(date.today(), row['ConfirmCheckOut']) - 
             pd.Timestamp.combine(date.today(), row['ConfirmCheckIn'])).total_seconds() / 3600 - 
            (row['TotalBreakTimeInHour'] or 0)
        )
    
    # Special case for doctors/cleaners or LABO company staff
    elif (row['WorkProfilePositionId'] in [478, 580]) or (row['CompanyId'] == 12 and row['IsFullTime'] == 2):
        confirm_in = row['ConfirmCheckIn'] or row['CheckIn']
        confirm_out = row['ConfirmCheckOut'] or row['CheckOut']
        
        if confirm_in is not None and confirm_out is not None:
            working_time = (
                (pd.Timestamp.combine(date.today(), confirm_out) - 
                 pd.Timestamp.combine(date.today(), confirm_in))).total_seconds() / 3600
        else:
            working_time = 0
    
    # For normal records, use actual check times bounded by shift times
    else:
        confirm_in = row['ConfirmCheckIn'] or row['CheckIn']
        confirm_out = row['ConfirmCheckOut'] or row['CheckOut']
        
        # Bound check times by shift times
        effective_in = max(confirm_in, row['ShiftStart']) if confirm_in else row['ShiftStart']
        effective_out = min(confirm_out, row['ShiftEnd']) if confirm_out else row['ShiftEnd']
        
        working_time = (
            (pd.Timestamp.combine(date.today(), effective_out) - 
             pd.Timestamp.combine(date.today(), effective_in))).total_seconds() / 3600 - (row['TotalBreakTimeInHour'] or 0)
    
    return max(0, working_time)

def calculate_work_day(row):
    """Helper function to calculate workday value based on complex business rules"""
    working_time = row['Thời gian làm thực tế']
    
    # LABO company with IsFullTime = 2
    if row['CompanyId'] == 12 and row['IsFullTime'] == 2:
        if working_time >= 8:
            return 1
        elif working_time < 8 and working_time >= 3:
            return round(working_time / 8, 2)
        else:
            return 0
    
    # Special positions
    elif row['WorkProfilePositionId'] == 580:
        return round(working_time / 8, 2)
    
    # Other specific positions with minimum 3 hours
    elif working_time >= 3 and row['WorkProfilePositionId'] in [586, 582, 592, 632, 686, 690]:
        return round(working_time / 8, 2)
    
    # Other specific positions with less than 3 hours
    elif working_time < 3 and row['WorkProfilePositionId'] in [586, 582, 592, 632, 686, 690]:
        return 0.00
    
    # Remaining positions
    elif row['WorkProfilePositionId'] not in [586, 582, 592, 632, 686, 580, 690]:
        if working_time > 5:
            return 1
        elif working_time > 0:
            return 0.5
    
    # Default case
    return 0

# Example usage
if __name__ == "__main__":
    # Example dates
    from_date = "2025-02-01"
    to_date = "2025-02-28"
    
    # Get timekeeper details
    result = usp_timekeeper_detail_manual(from_date, to_date)
    
    # Display first few rows
    if not result.empty:
        print(result.head())
    else:
        print("No data found for the specified date range.")
