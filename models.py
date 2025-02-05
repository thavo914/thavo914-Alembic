from typing import Any, List, Optional

from sqlalchemy import CHAR, Column, DECIMAL, Date, DateTime, Double, Float, ForeignKeyConstraint, Index, String, Table, Text, Time, text
from sqlalchemy.dialects.mysql import BIGINT, BIT, DECIMAL, INTEGER, LONGTEXT, MEDIUMTEXT, SMALLINT, TEXT, TINYINT, VARCHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import datetime
import decimal

class Base(DeclarativeBase):
    pass

class ASalaryPTa(Base):
    __tablename__ = 'ASalaryPTa'

    Stt: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    Mã_NV: Mapped[Optional[str]] = mapped_column('Mã NV', String(50, 'utf8mb4_unicode_ci'))
    FullName: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'))
    Công_ty: Mapped[Optional[str]] = mapped_column('Công ty', String(50, 'utf8mb4_unicode_ci'))
    PositionProfile: Mapped[Optional[str]] = mapped_column(String(100, 'utf8mb4_unicode_ci'))
    Lo_i_HÐ: Mapped[Optional[str]] = mapped_column('Lo?i HÐ', String(50, 'utf8mb4_unicode_ci'))
    Chi_nhánh: Mapped[Optional[str]] = mapped_column('Chi nhánh', String(50, 'utf8mb4_unicode_ci'))
    Ca_làm_vi_c: Mapped[Optional[str]] = mapped_column('Ca làm vi?c', String(50, 'utf8mb4_unicode_ci'))
    Bac: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'))
    Don_Gia_Gio: Mapped[Optional[int]] = mapped_column('Don Gia Gio', INTEGER(11))
    So_Gio_lam_viec_HIS: Mapped[Optional[int]] = mapped_column('So Gio lam viec HIS', INTEGER(11))
    Ngh__phép: Mapped[Optional[int]] = mapped_column('Ngh? phép', INTEGER(11))
    Ngh__bù: Mapped[Optional[str]] = mapped_column('Ngh? bù', String(50, 'utf8mb4_unicode_ci'))
    Ngh__ch__d__có_luong: Mapped[Optional[str]] = mapped_column('Ngh? ch? d? có luong', String(50, 'utf8mb4_unicode_ci'))
    Ngh__l_: Mapped[Optional[str]] = mapped_column('Ngh? l?', String(50, 'utf8mb4_unicode_ci'))
    T_ng_công_tính_luong: Mapped[Optional[int]] = mapped_column('T?ng công tính luong', INTEGER(11))
    Công_chu_n: Mapped[Optional[int]] = mapped_column('Công chu?n', INTEGER(11))
    Thành_ti_n_luong_theo_t_ng_công: Mapped[Optional[int]] = mapped_column('Thành ti?n luong theo t?ng công', INTEGER(11))
    Ð_nh_m_c_PC_com: Mapped[Optional[int]] = mapped_column('Ð?nh m?c PC com', INTEGER(11))
    Thành_ti_n_PC_com_theo_công: Mapped[Optional[int]] = mapped_column('Thành ti?n PC com theo công', INTEGER(11))
    Ð_nh_m_c_thu_nh_p_c__d_nh__dã_bao_g_m_PC_com_: Mapped[Optional[int]] = mapped_column('Ð?nh m?c thu nh?p c? d?nh (dã bao g?m PC com)', INTEGER(11))
    Thành_ti_n_thu_nh_p_c__d_nh_theo_công_chu_n__dã_bao_g_m_PC_c: Mapped[Optional[int]] = mapped_column('Thành ti?n thu nh?p c? d?nh theo công chu?n (dã bao g?m PC c', INTEGER(11))
    Thu_ng_nang_su_t: Mapped[Optional[int]] = mapped_column('Thu?ng nang su?t', INTEGER(11))
    Thu_ng_công_vi_c: Mapped[Optional[str]] = mapped_column('Thu?ng công vi?c', String(50, 'utf8mb4_unicode_ci'))
    Thu_ng_ch_t_lu_ng_d_ch_v_: Mapped[Optional[str]] = mapped_column('Thu?ng ch?t lu?ng d?ch v?', String(50, 'utf8mb4_unicode_ci'))
    Thu_ng_qu_n_lý__giám_sát: Mapped[Optional[str]] = mapped_column('Thu?ng qu?n lý, giám sát', String(50, 'utf8mb4_unicode_ci'))
    Thu_ng_phòng_khám_d_t_KPI_Thu_Ti_n: Mapped[Optional[str]] = mapped_column('Thu?ng phòng khám d?t KPI Thu Ti?n', String(50, 'utf8mb4_unicode_ci'))
    Thu_ng_L__T_t: Mapped[Optional[str]] = mapped_column('Thu?ng L?/T?t', String(50, 'utf8mb4_unicode_ci'))
    T_ng_thu_ng: Mapped[Optional[int]] = mapped_column('T?ng thu?ng', INTEGER(11))
    PC_Ph__tá_tru_ng___Kiêm_nhi_m: Mapped[Optional[int]] = mapped_column('PC Ph? tá tru?ng & Kiêm nhi?m', INTEGER(11))
    Ph__c_p_d_m_b_o_thu_nh_p: Mapped[Optional[str]] = mapped_column('Ph? c?p d?m b?o thu nh?p', String(50, 'utf8mb4_unicode_ci'))
    PC_G_i_xe_Công_tác: Mapped[Optional[str]] = mapped_column('PC G?i xe/Công tác', String(50, 'utf8mb4_unicode_ci'))
    Ph__c_p_ch_ng_ch__hành_ngh_: Mapped[Optional[int]] = mapped_column('Ph? c?p ch?ng ch? hành ngh?', INTEGER(11))
    Ph__c_p_khác: Mapped[Optional[int]] = mapped_column('Ph? c?p khác', INTEGER(11))
    Dental_tour: Mapped[Optional[str]] = mapped_column('Dental tour', String(50, 'utf8mb4_unicode_ci'))
    Ph__c_p_kho: Mapped[Optional[str]] = mapped_column('Ph? c?p kho', String(50, 'utf8mb4_unicode_ci'))
    T_ng_thu_nh_p_khác: Mapped[Optional[int]] = mapped_column('T?ng thu nh?p khác', INTEGER(11))
    T_ng_thu_nh_p_tru_c_thu_: Mapped[Optional[int]] = mapped_column('T?ng thu nh?p tru?c thu?', INTEGER(11))
    M_c_luong_tham_gia_BHXH: Mapped[Optional[int]] = mapped_column('M?c luong tham gia BHXH', INTEGER(11))
    BHYT__1_5__: Mapped[Optional[int]] = mapped_column('BHYT (1,5%)', INTEGER(11))
    BHXH__8__: Mapped[Optional[int]] = mapped_column('BHXH (8%)', INTEGER(11))
    BHTN__1__: Mapped[Optional[int]] = mapped_column('BHTN (1%)', INTEGER(11))
    NLÐ_dóng_BHXH__10_5__: Mapped[Optional[int]] = mapped_column('NLÐ dóng BHXH (10.5%)', INTEGER(11))
    NLÐ_dóng_phí_Công_doàn__1__: Mapped[Optional[int]] = mapped_column('NLÐ dóng phí Công doàn (1%)', INTEGER(11))
    BHXH__17_: Mapped[Optional[int]] = mapped_column('BHXH (17%', INTEGER(11))
    TNLÐ___BNN__0_5__: Mapped[Optional[int]] = mapped_column('TNLÐ / BNN (0.5%)', INTEGER(11))
    BHYT__3__: Mapped[Optional[int]] = mapped_column('BHYT (3%)', INTEGER(11))
    BHTN_1_: Mapped[Optional[int]] = mapped_column('BHTN 1%', INTEGER(11))
    Doanh_nghi_p_dóng_BHXH_21_5_: Mapped[Optional[int]] = mapped_column('Doanh nghi?p dóng BHXH 21.5%', INTEGER(11))
    Doanh_nghi_p_dóng_Công_doàn_2_: Mapped[Optional[int]] = mapped_column('Doanh nghi?p dóng Công doàn 2%', INTEGER(11))
    Không_tính_thu___Ph__c_p_com_trua__Ð_ng_ph_c_: Mapped[Optional[int]] = mapped_column('Không tính thu? (Ph? c?p com trua/ Ð?ng ph?c)', INTEGER(11))
    T_NG_THU_NH_P_CH_U_THU_: Mapped[Optional[int]] = mapped_column('T?NG THU NH?P CH?U THU?', INTEGER(11))
    Ð_i_tu_ng_tính_Thu__TNCN: Mapped[Optional[str]] = mapped_column('Ð?i tu?ng tính Thu? TNCN', String(50, 'utf8mb4_unicode_ci'))
    Cam_k_t: Mapped[Optional[str]] = mapped_column('Cam k?t', String(50, 'utf8mb4_unicode_ci'))
    S__ngu_i_ph__thu_c: Mapped[Optional[int]] = mapped_column('S? ngu?i ph? thu?c', INTEGER(11))
    T_NG_THU_NH_P_TÍNH_THU_: Mapped[Optional[int]] = mapped_column('T?NG THU NH?P TÍNH THU?', INTEGER(11))
    Thu_Ti_n_thu__TNCN: Mapped[Optional[int]] = mapped_column('Thu Ti?n thu? TNCN', INTEGER(11))
    Th_c_lãnh: Mapped[Optional[int]] = mapped_column('Th?c lãnh', INTEGER(11))
    Cty_dóng_h__BHXH: Mapped[Optional[int]] = mapped_column('Cty dóng h? BHXH', INTEGER(11))
    Thu_h__ti_n_BHXH__21_5_: Mapped[Optional[int]] = mapped_column('Thu h? ti?n BHXH (21.5%', INTEGER(11))
    Chuy_n_kho_n: Mapped[Optional[int]] = mapped_column('Chuy?n kho?n', INTEGER(11))
    H____tên: Mapped[Optional[str]] = mapped_column('H? & tên', String(50, 'utf8mb4_unicode_ci'))
    S__tài_kho_n: Mapped[Optional[str]] = mapped_column('S? tài kho?n', String(50, 'utf8mb4_unicode_ci'))
    Ngân_hàng: Mapped[Optional[str]] = mapped_column('Ngân hàng', String(50, 'utf8mb4_unicode_ci'))
    Mail: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'))
    Chuy_n_kho_n1: Mapped[Optional[int]] = mapped_column('Chuy?n kho?n1', INTEGER(11))
    B__sung: Mapped[Optional[int]] = mapped_column('B? sung', INTEGER(11))
    Lý_do: Mapped[Optional[str]] = mapped_column('Lý do', String(100, 'utf8mb4_unicode_ci'))
    Ghi_chú_ngày_thanh_toán: Mapped[Optional[str]] = mapped_column('Ghi chú ngày thanh toán', String(50, 'utf8mb4_unicode_ci'))


class AbsenceRequestChangeHistory(Base):
    __tablename__ = 'AbsenceRequestChangeHistory'

    AbsenceRequestChangeHistoryId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    AbsenceRequestId: Mapped[int] = mapped_column(INTEGER(11))
    Note: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    AbsenceFrom: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    AbsenceTo: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)


class AbsenceRequestDetail(Base):
    __tablename__ = 'AbsenceRequestDetail'
    __table_args__ = (
        Index('Index', 'WorkScheduleId', 'Date'),
        Index('fk_AbsenceRequestDetail_AbsenceRequest_idx', 'AbsenceRequestId'),
        Index('ix_AbsenceRequestDetail_Date_RequestedBy', 'Date', 'RequestedBy')
    )

    AbsenceRequestId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    Date_: Mapped[datetime.date] = mapped_column('Date', Date, primary_key=True)
    AbsenceFromTime: Mapped[datetime.time] = mapped_column(Time, primary_key=True)
    AbsenceToTime: Mapped[datetime.time] = mapped_column(Time)
    WorkScheduleId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    WorkShiftId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    TotalDays: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(6, 2), server_default=text("'0.00'"))
    RequestedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class AbsenceRequestDetailByLeave(Base):
    __tablename__ = 'AbsenceRequestDetailByLeave'
    __table_args__ = (
        Index('idx_AbsenceRequestId', 'AbsenceRequestId'),
    )

    Id: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    AbsenceRequestId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UsedLastAnnualLeave: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 1), server_default=text("'0.0'"))
    UsedLastSeniorityLeave: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 1), server_default=text("'0.0'"))
    UsedLastRankLeave: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 1), server_default=text("'0.0'"))
    UsedLastTrainingLeave: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 1), server_default=text("'0.0'"))
    UsedAnnualLeave: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 1), server_default=text("'0.0'"))
    UsedSeniorityLeave: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 1), server_default=text("'0.0'"))
    UsedRankLeave: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 1), server_default=text("'0.0'"))
    UsedTrainingLeave: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 1), server_default=text("'0.0'"))


class AbsenceType(Base):
    __tablename__ = 'AbsenceType'

    AbsenceTypeId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    AbsenceTypeCode: Mapped[str] = mapped_column(VARCHAR(8))
    Name: Mapped[str] = mapped_column(VARCHAR(128))
    Ordering: Mapped[int] = mapped_column(INTEGER(10))
    AbsenceGroupType: Mapped[Optional[int]] = mapped_column(TINYINT(4), comment='1: Ngh? phép có h??ng l??ng c?a công ty, 2: Ngh? phép không h??ng l??ng c?a công ty')
    Note: Mapped[Optional[str]] = mapped_column(TEXT)
    GroupType: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))
    Value: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    MaxValue: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    AppliedDate: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))
    IsHidden: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'0'"))

    AbsenceRequest: Mapped[List['AbsenceRequest']] = relationship('AbsenceRequest', back_populates='AbsenceType_')


class ActivityLog(Base):
    __tablename__ = 'ActivityLog'

    ActivityLogId: Mapped[int] = mapped_column(BIGINT(15), primary_key=True)
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    ActionType: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='1) LockProfile\n2) UnlockProfile\n')
    Data: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))


class ActivityTrackingSystem(Base):
    __tablename__ = 'ActivityTrackingSystem'
    __table_args__ = (
        Index('Idx_StaffId', 'StaffId'),
    )

    Id: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    URLPath: Mapped[Optional[str]] = mapped_column(String(256, 'utf8mb4_unicode_ci'))
    UserId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IPAddress: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))
    AgentInfo: Mapped[Optional[str]] = mapped_column(String(1024, 'utf8mb4_unicode_ci'))
    TrackingTime: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    Note: Mapped[Optional[str]] = mapped_column(LONGTEXT)
    WorkProfilePositionId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    TypePermission: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))


class AddressType(Base):
    __tablename__ = 'AddressType'

    AddressTypeId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    Name: Mapped[str] = mapped_column(String(32, 'utf8mb4_unicode_ci'))
    Ordering: Mapped[int] = mapped_column(INTEGER(10))

    StaffAddress: Mapped[List['StaffAddress']] = relationship('StaffAddress', back_populates='AddressType_')


class AdminExecute(Base):
    __tablename__ = 'AdminExecute'
    __table_args__ = (
        Index('fk_AdminExecute_ExecutedBy_idx', 'ExecutedBy'),
    )

    AdminExecuteId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    ExecutedBy: Mapped[int] = mapped_column(INTEGER(10))
    ExecutedAt: Mapped[int] = mapped_column(INTEGER(10))


class Allowance(Base):
    __tablename__ = 'Allowance'

    AllowanceId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    Name: Mapped[str] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    DefaultAmount: Mapped[decimal.Decimal] = mapped_column(DECIMAL(12, 2))
    Ordering: Mapped[int] = mapped_column(INTEGER(10))
    State: Mapped[int] = mapped_column(INTEGER(1), server_default=text("'1'"))
    RepeatBy: Mapped[Optional[int]] = mapped_column(INTEGER(1), server_default=text("'2'"), comment='Chi l?p l?i theo:\n1 - theo tu?n\n2 - theo tháng\n3 - theo n?m')
    LimitUse: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'1'"))


class AllowanceStaff(Base):
    __tablename__ = 'AllowanceStaff'
    __table_args__ = (
        Index('IX_AllowanceStaff_StaffId', 'StaffId'),
        Index('fk_AllowanceStaff_Allowance_idx', 'AllowanceId'),
        Index('fk_AllowanceStaff_WorkProfile_idx', 'WorkProfileId', 'StaffId')
    )

    Id: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    WorkProfileId: Mapped[int] = mapped_column(INTEGER(10))
    AllowanceId: Mapped[int] = mapped_column(INTEGER(10))
    StaffId: Mapped[int] = mapped_column(INTEGER(10))
    Amount: Mapped[decimal.Decimal] = mapped_column(DECIMAL(12, 2))
    TaxInclude: Mapped[int] = mapped_column(INTEGER(1), server_default=text("'1'"), comment='có tính thu? không')
    IssueFromDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    IssueToDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    Note: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_unicode_ci'), comment='ghi chú')


class AllowanceStaffHistory(Base):
    __tablename__ = 'AllowanceStaffHistory'

    AllowanceStaffHistoryId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    Amount: Mapped[decimal.Decimal] = mapped_column(DECIMAL(18, 2), server_default=text("'0.00'"))
    FromDate: Mapped[datetime.date] = mapped_column(Date)
    WorkContractHistoryId: Mapped[int] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    Type: Mapped[Optional[str]] = mapped_column(String(128, 'utf8mb4_unicode_ci'))
    ToDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    Note: Mapped[Optional[str]] = mapped_column(String(1000, 'utf8mb4_unicode_ci'))


class App(Base):
    __tablename__ = 'App'

    AppId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    Name: Mapped[str] = mapped_column(VARCHAR(128))
    Dir: Mapped[str] = mapped_column(VARCHAR(32))
    Desc: Mapped[Optional[str]] = mapped_column(TEXT)

    Viewing: Mapped[List['Viewing']] = relationship('Viewing', secondary='AppViewing', back_populates='App_')
    Extension: Mapped[List['Extension']] = relationship('Extension', back_populates='App_')
    Session: Mapped[List['Session']] = relationship('Session', back_populates='App_')
    File: Mapped[List['File']] = relationship('File', back_populates='App_')
    Menu: Mapped[List['Menu']] = relationship('Menu', back_populates='App_')


class Bank(Base):
    __tablename__ = 'Bank'

    BankId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    State: Mapped[int] = mapped_column(INTEGER(10), server_default=text("'1'"))
    NameVi: Mapped[Optional[str]] = mapped_column(VARCHAR(64))
    NameEn: Mapped[Optional[str]] = mapped_column(VARCHAR(64))
    Address: Mapped[Optional[str]] = mapped_column(VARCHAR(128))
    Priority: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'99999'"))
    Type: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='1) Internal\n2) ForCustomer\n999) All')


class BankBranch(Base):
    __tablename__ = 'BankBranch'
    __table_args__ = (
        Index('fk_BankBranch_Bank_idx', 'BankId'),
    )

    BankBranchId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    BankId: Mapped[int] = mapped_column(INTEGER(10))
    NameVi: Mapped[Optional[str]] = mapped_column(VARCHAR(64))
    NameEn: Mapped[Optional[str]] = mapped_column(VARCHAR(64))
    State: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Address: Mapped[Optional[str]] = mapped_column(VARCHAR(45))


class BranchExecutiveTarget(Base):
    __tablename__ = 'BranchExecutiveTarget'
    __table_args__ = (
        Index('fk_BranchExecutiveTarget_Branch_idx', 'BranchId'),
        {'comment': 'bảng lưu target hoạt động của các chi nhánh'}
    )

    BranchExecutiveTargetId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    Revenue: Mapped[decimal.Decimal] = mapped_column(DECIMAL(20, 2), comment='target về doanh thu của chi nhánh')
    FromDate: Mapped[datetime.date] = mapped_column(Date)
    BranchId: Mapped[int] = mapped_column(INTEGER(10))
    CompanyId: Mapped[int] = mapped_column(INTEGER(11))
    Appointment: Mapped[Optional[int]] = mapped_column(INTEGER(10), comment='target về số lịch hẹn của chi nhánh')
    Checkin: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    Treatment: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    ToDate: Mapped[Optional[datetime.date]] = mapped_column(Date)


class BranchPhoneExtension(Base):
    __tablename__ = 'BranchPhoneExtension'

    BranchPhoneExtensionId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    BranchId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    PhoneExtension: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Status: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='0 InActive\n1 Active')
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))


class BranchServiceQuality(Base):
    __tablename__ = 'BranchServiceQuality'

    Year: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    Month: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    AVGStar: Mapped[Optional[float]] = mapped_column(Float)
    QuantityRating: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    ScoreCardMark: Mapped[Optional[float]] = mapped_column(Float)
    CRVAssistant: Mapped[Optional[float]] = mapped_column(Float)
    CRVManager: Mapped[Optional[float]] = mapped_column(Float)
    CRVCoordinatingDoctor: Mapped[Optional[float]] = mapped_column(Float)
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))


t_ByMonth = Table(
    'ByMonth', Base.metadata,
    Column('WorkScheduleId', INTEGER(10), nullable=False),
    Column('MonthId', INTEGER(10), nullable=False),
    Index('fk_ByMonth_Month_idx', 'MonthId'),
    Index('fk_ByMonth_WorkSchedule_idx', 'WorkScheduleId')
)


class Candidate(Base):
    __tablename__ = 'Candidate'
    __table_args__ = (
        Index('IX_PersonId', 'PersonId'),
    )

    CandidateId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    PersonId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    PositionId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    PositionText: Mapped[Optional[str]] = mapped_column(VARCHAR(300))
    Location: Mapped[Optional[str]] = mapped_column(VARCHAR(300))
    ApplyDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CDNCV: Mapped[Optional[str]] = mapped_column(VARCHAR(1024))
    RowInterview: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Status: Mapped[Optional[int]] = mapped_column(TINYINT(2), server_default=text("'1'"), comment='1: ?ng viên m?i, 2: ?ng viên không ??t, 3: ?ã có l?ch ph?ng v?n, 4: ?ã có offer, 5: ?ã là nhân viên, 6: ?ã ngh? vi?c')
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    DiscussionFromHR: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_unicode_ci'))
    DiscussionFromCandidate: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_unicode_ci'))
    EvaluationFromHR: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_unicode_ci'))
    LastFolowByStaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    LastFolowDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    StatusNote: Mapped[Optional[str]] = mapped_column(String(1000, 'utf8mb4_unicode_ci'))


class CandidateOffer(Base):
    __tablename__ = 'CandidateOffer'

    CandidateOfferId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    CandidateId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Code: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))
    Status: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='1 new, 2 finished,3 cancel')
    StatusNote: Mapped[Optional[str]] = mapped_column(String(4096, 'utf8mb4_unicode_ci'))
    OfferExpiredDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    CompanyId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    DepartmentId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    TeamId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    WorkPositionId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    StaffLevelId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    BranchId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Location: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    WorkTimeMode: Mapped[Optional[str]] = mapped_column(String(20, 'utf8mb4_unicode_ci'))
    SalaryAmount: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(18, 2))
    ProbationFromDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ProbationToDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ProbationWorkLocationId: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment="  Json [{'Type':'Ph? c?p ??m b?o thu nh?p','Amount':200000},{'Type':'Ph? c?p ch?ng ch? hành ngh?','Amount':500000}]")
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Type: Mapped[Optional[int]] = mapped_column(TINYINT(4))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Note: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_unicode_ci'))


class CandidateTracking(Base):
    __tablename__ = 'CandidateTracking'

    CandidateTrackingId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    CandidateId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    TrackingTypeId: Mapped[Optional[int]] = mapped_column(TINYINT(4), comment='1)Pickup\\n2)Exchange Content\\n3)Change Interview4)UpdateCV')
    JsonDetail: Mapped[Optional[str]] = mapped_column(String(8000, 'utf8mb4_unicode_ci'))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class Certificate(Base):
    __tablename__ = 'Certificate'
    __table_args__ = (
        Index('fk_Certificate_CertificateGroup_idx', 'CertificateGroupId'),
        Index('fk_Certificate_Staff_idx', 'StaffId')
    )

    CertificateId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    CertificateGroupId: Mapped[int] = mapped_column(INTEGER(10))
    StaffId: Mapped[int] = mapped_column(INTEGER(10))
    VerifiedType: Mapped[Optional[int]] = mapped_column(TINYINT(1), server_default=text("'0'"), comment='Loại thẩm định: 1 - Tại NKK, 2 - Ngoài NKK, 3 - Đăng ký tại NKK, 4- Chưa đăng ký')
    Name: Mapped[Optional[str]] = mapped_column(VARCHAR(128))
    CertificateSuggestionId: Mapped[Optional[int]] = mapped_column(INTEGER(10), server_default=text("'0'"))
    Note: Mapped[Optional[str]] = mapped_column(TEXT)
    Type: Mapped[Optional[int]] = mapped_column(TINYINT(1), server_default=text("'0'"), comment='Phân loại: 1 - Đã có chứng chỉ, 2: Chuẩn bị có chứng chỉ')
    AttachFile: Mapped[Optional[str]] = mapped_column(VARCHAR(128))
    IssueDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ExpiryDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    EstimatedIssueDate: Mapped[Optional[datetime.date]] = mapped_column(Date, comment='Ngày chuẩn bị có chứng chỉ')
    VerifiedDate: Mapped[Optional[datetime.date]] = mapped_column(Date, comment='Ngày thẩm định')
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    ScheduleRegister: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_unicode_ci'))
    RegistrationDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    BranchId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IsDeleted: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    CertificateNumber: Mapped[Optional[str]] = mapped_column(String(1024, 'utf8mb4_unicode_ci'))
    IssuedBy: Mapped[Optional[str]] = mapped_column(String(1024, 'utf8mb4_unicode_ci'))
    RegisterAt: Mapped[Optional[str]] = mapped_column(String(1024, 'utf8mb4_unicode_ci'))


class CertificateDetail(Base):
    __tablename__ = 'CertificateDetail'

    CertificateDetailId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    CertificateId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    WorkDay: Mapped[Optional[str]] = mapped_column(String(10, 'utf8mb4_unicode_ci'))
    startTime: Mapped[Optional[datetime.time]] = mapped_column(Time)
    endTime: Mapped[Optional[datetime.time]] = mapped_column(Time)
    BranchId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    IsDeleted: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))


class CertificateGroup(Base):
    __tablename__ = 'CertificateGroup'

    CertificateGroupId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    Ordering: Mapped[int] = mapped_column(INTEGER(10))
    Name: Mapped[Optional[str]] = mapped_column(String(300, 'utf8mb4_unicode_ci'))
    Code: Mapped[Optional[str]] = mapped_column(String(100, 'utf8mb4_unicode_ci'))
    State: Mapped[Optional[int]] = mapped_column(TINYINT(1), server_default=text("'1'"), comment='Trạng thái: 0 - Inactive, 1 - Active')


class CertificateSuggestion(Base):
    __tablename__ = 'CertificateSuggestion'

    CertificateSuggestionId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    CertificateGroupId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Code: Mapped[Optional[str]] = mapped_column(String(20, 'utf8mb4_unicode_ci'))
    Name: Mapped[Optional[str]] = mapped_column(String(128, 'utf8mb4_unicode_ci'))
    SuggestionType: Mapped[Optional[int]] = mapped_column(TINYINT(1), server_default=text("'0'"), comment='Phân loại: 0 - Tất cả, 1 - Đã có chứng chỉ, 2: Chuẩn bị có chứng chỉ')
    IsDeleted: Mapped[Optional[int]] = mapped_column(TINYINT(1), server_default=text("'0'"))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))


class CertificateTracking(Base):
    __tablename__ = 'CertificateTracking'

    CertificateTrackingId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    AccumulatedHours: Mapped[int] = mapped_column(INTEGER(11), server_default=text("'0'"))
    DateOfOccurrence: Mapped[datetime.date] = mapped_column(Date)
    CertificateId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    TrackingType: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='1:create;2:update;3:remove')
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Note: Mapped[Optional[str]] = mapped_column(String(1000, 'utf8mb4_unicode_ci'))


class Company(Base):
    __tablename__ = 'Company'

    CompanyId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    NameVi: Mapped[str] = mapped_column(VARCHAR(128))
    State: Mapped[int] = mapped_column(INTEGER(1), server_default=text("'1'"), comment='0  - không hoạt động\n1 - hoạt động')
    NameEn: Mapped[Optional[str]] = mapped_column(VARCHAR(128))
    NameShortVi: Mapped[Optional[str]] = mapped_column(VARCHAR(64))
    NameShortEn: Mapped[Optional[str]] = mapped_column(VARCHAR(64))
    Address: Mapped[Optional[str]] = mapped_column(VARCHAR(256))
    Phone: Mapped[Optional[str]] = mapped_column(VARCHAR(16))
    Fax: Mapped[Optional[str]] = mapped_column(VARCHAR(16))
    Website: Mapped[Optional[str]] = mapped_column(VARCHAR(64))
    Email: Mapped[Optional[str]] = mapped_column(VARCHAR(64))
    UpdateBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UpdateAt: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IsTimekeeping: Mapped[Optional[int]] = mapped_column(SMALLINT(1), comment='0: no checkin; 1 checkin')
    isSyncORC: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    ORCRefCode: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    DomainEmail: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    Priority: Mapped[Optional[int]] = mapped_column(INTEGER(11))

    AbsenceConfig: Mapped[List['AbsenceConfig']] = relationship('AbsenceConfig', back_populates='Company_')
    Branch: Mapped[List['Branch']] = relationship('Branch', back_populates='Company_')
    Department: Mapped[List['Department']] = relationship('Department', back_populates='Company_')


t_ComplaintAboutReason = Table(
    'ComplaintAboutReason', Base.metadata,
    Column('ComplaintAboutReasonId', INTEGER(10), nullable=False),
    Column('ComplaintReasonGroupId', INTEGER(11), nullable=False),
    Column('Ordering', INTEGER(10), nullable=False),
    Column('Reason', String(128, 'utf8mb4_unicode_ci'), nullable=False),
    Column('State', INTEGER(1), nullable=False, server_default=text("'0'")),
    Column('CreatedAt', INTEGER(10), nullable=False),
    Column('CreatedBy', INTEGER(10), nullable=False),
    Column('LanguageId', INTEGER(10), nullable=False)
)


t_ComplaintChannel = Table(
    'ComplaintChannel', Base.metadata,
    Column('ComplaintChannelId', INTEGER(10), nullable=False),
    Column('Name', String(32, 'utf8mb4_unicode_ci'), nullable=False),
    Column('State', INTEGER(1), nullable=False, server_default=text("'1'")),
    comment='callcenter, app, web, reception...'
)


t_ComplaintReasonGroup = Table(
    'ComplaintReasonGroup', Base.metadata,
    Column('ComplaintReasonGroupId', INTEGER(10), nullable=False),
    Column('Name', String(32, 'utf8mb4_unicode_ci'), nullable=False),
    Column('State', INTEGER(1), nullable=False, server_default=text("'1'")),
    comment='Gom nhóm các complaint. Các nhóm không chồng lấn.'
)


class ContactPoint(Base):
    __tablename__ = 'ContactPoint'

    ContactPointId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    State: Mapped[int] = mapped_column(INTEGER(1), server_default=text("'1'"))
    CompanyId: Mapped[int] = mapped_column(INTEGER(10))
    DepartmentId: Mapped[int] = mapped_column(INTEGER(10))
    TeamId: Mapped[int] = mapped_column(INTEGER(10))
    BranchId: Mapped[int] = mapped_column(INTEGER(10))
    Desc: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_unicode_ci'))

    Contact: Mapped[List['Contact']] = relationship('Contact', back_populates='ContactPoint_')


class Country(Base):
    __tablename__ = 'Country'

    CountryId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    Name: Mapped[str] = mapped_column(VARCHAR(64))
    Code: Mapped[str] = mapped_column(VARCHAR(8))
    Ordering: Mapped[int] = mapped_column(INTEGER(11), server_default=text("'0'"))
    NationalityLabel: Mapped[Optional[str]] = mapped_column(String(128, 'utf8mb4_unicode_ci'))


class CronJobHistory(Base):
    __tablename__ = 'CronJobHistory'

    Id: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    JobName: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    Message: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))


class CronUpdateWorkProfileHistory(Base):
    __tablename__ = 'CronUpdateWorkProfileHistory'

    CronUpdateWorkProfileHistoryId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    CreatedAt: Mapped[int] = mapped_column(INTEGER(11))
    WorkProfileId: Mapped[str] = mapped_column(Text(collation='utf8mb4_unicode_ci'))
    StaffId: Mapped[str] = mapped_column(Text(collation='utf8mb4_unicode_ci'))


class CustomHolidayByYear(Base):
    __tablename__ = 'CustomHolidayByYear'
    __table_args__ = (
        Index('HolidayDate_UNIQUE', 'HolidayDate', unique=True),
        {'comment': 'b?ng l?u (ngày d??ng) các ngày l? thi?t l?p theo t?ng n?m. Ví d?: '
                't?t âm l?ch, gi? t? Hùng V??ng...'}
    )

    HolidayDate: Mapped[datetime.date] = mapped_column(Date, primary_key=True)
    Name: Mapped[str] = mapped_column(VARCHAR(32))


class CustomerCareRatingRecommend(Base):
    __tablename__ = 'CustomerCareRatingRecommend'
    __table_args__ = (
        Index('fk_rating_id', 'RatingId'),
    )

    Id: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    RatingId: Mapped[int] = mapped_column(INTEGER(11))
    Content: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_unicode_ci'))
    OrgId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)


class DayInfo(Base):
    __tablename__ = 'DayInfo'
    __table_args__ = (
        Index('idx_dayinfo_date', 'Date'),
        Index('idx_dayinfo_isweekend', 'IsWeekend')
    )

    Id: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    Date_: Mapped[Optional[datetime.date]] = mapped_column('Date', Date)
    DayOfWeek: Mapped[Optional[str]] = mapped_column(String(10, 'utf8mb4_unicode_ci'))
    IsWeekend: Mapped[Optional[int]] = mapped_column(TINYINT(1))
    IsHoliday: Mapped[Optional[int]] = mapped_column(TINYINT(1))
    HolidayName: Mapped[Optional[str]] = mapped_column(String(100, 'utf8mb4_unicode_ci'))


class Degree(Base):
    __tablename__ = 'Degree'

    DegreeId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    NameVi: Mapped[str] = mapped_column(VARCHAR(32))
    NameEn: Mapped[str] = mapped_column(VARCHAR(32))
    Ordering: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class DependantRelationship(Base):
    __tablename__ = 'DependantRelationship'

    DependantRelationshipId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    Name: Mapped[str] = mapped_column(VARCHAR(64))
    Ordering: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IsPromotionApply: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'1'"))

    DependantPeople: Mapped[List['DependantPeople']] = relationship('DependantPeople', back_populates='DependantRelationship_')


class District(Base):
    __tablename__ = 'District'

    DistrictId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    DistrictName: Mapped[Optional[str]] = mapped_column(String(100, 'utf8mb4_unicode_ci'))
    Label: Mapped[Optional[str]] = mapped_column(String(20, 'utf8mb4_unicode_ci'))
    ProvinceId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    State: Mapped[Optional[int]] = mapped_column(TINYINT(1), server_default=text("'1'"))
    VnDistrictId: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class DocsAndForms(Base):
    __tablename__ = 'DocsAndForms'

    DocsAndFormsId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    DocsAndFormsName: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    DocsAndFormsLink: Mapped[Optional[str]] = mapped_column(String(1000, 'utf8mb4_unicode_ci'))
    Status: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)


class Email(Base):
    __tablename__ = 'Email'

    EmailId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    Subject: Mapped[Optional[str]] = mapped_column(String(2048, 'utf8mb4_unicode_ci'))
    SenderStaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    ShortContent: Mapped[Optional[str]] = mapped_column(String(2048, 'utf8mb4_unicode_ci'))
    Priority: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'1'"), comment='1 normal\n2 Hight')
    Status: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='1 Draff\n2 Sent\n3 Hidden')
    IsAttachFile: Mapped[Optional[int]] = mapped_column(TINYINT(2))
    PrimaryEmailId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class EmailAttachFile(Base):
    __tablename__ = 'EmailAttachFile'

    EmailAttachFileId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    EmailId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CDNURL: Mapped[Optional[str]] = mapped_column(String(2048, 'utf8mb4_unicode_ci'))
    FileType: Mapped[Optional[str]] = mapped_column(String(20, 'utf8mb4_unicode_ci'))
    FileName: Mapped[Optional[str]] = mapped_column(String(128, 'utf8mb4_unicode_ci'))
    FileSize: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))


class EmailContent(Base):
    __tablename__ = 'EmailContent'

    EmailContentId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    EmailId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Content: Mapped[Optional[str]] = mapped_column(LONGTEXT)


class EmailRead(Base):
    __tablename__ = 'EmailRead'

    EmailReadId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    EmailId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Subject: Mapped[Optional[str]] = mapped_column(String(2048, 'utf8mb4_unicode_ci'))
    PrimaryEmailId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    ReadDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    DeletedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    ReCallDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    Type: Mapped[Optional[int]] = mapped_column(TINYINT(4), comment='1 :To\n2:CC\n3:BCC\n4:Forward')


class EmailReceiver(Base):
    __tablename__ = 'EmailReceiver'

    EmailReceiverlId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    EmailId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    ReceiverId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    ReceiverType: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'1'"), comment='1 Staff; 2 Group;3 Org')
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    Type: Mapped[Optional[int]] = mapped_column(TINYINT(4), comment='1:To\n2:CC\n3:BCC\n4:Forward')


class EmailReceiverGroup(Base):
    __tablename__ = 'EmailReceiverGroup'

    EmailReceiverGroupId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    GroupName: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    IsActived: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))


class EmailReceiverGroupDetail(Base):
    __tablename__ = 'EmailReceiverGroupDetail'

    EmailReceiverGroupDetailId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    EmailReceiverGroupId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))


class EmailSenderGroupPermission(Base):
    __tablename__ = 'EmailSenderGroupPermission'

    EmailSenderGroupPermissionId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    EmailReceiverGroupId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IsActive: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))


class EmailStaffSignature(Base):
    __tablename__ = 'EmailStaffSignature'

    EmailStaffSignatureId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Signature: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_unicode_ci'))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))


class EmailStatusTracking(Base):
    __tablename__ = 'EmailStatusTracking'

    EmailStatusTrackingId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    EmailId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Status: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class Ethnic(Base):
    __tablename__ = 'Ethnic'

    EthnicId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    Name: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    Description: Mapped[Optional[str]] = mapped_column(String(512, 'utf8mb4_unicode_ci'))
    Priority: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    State: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))


class ExecuteValidConfig(Base):
    __tablename__ = 'ExecuteValidConfig'

    ExecuteValidConfigId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    CheckinValidAfter: Mapped[int] = mapped_column(INTEGER(10), server_default=text("'20'"), comment='kho?ng th?i gian gi?i h?n l?n checkin v?n còn hi?u l?c. Tính theo phút')
    CheckoutValidBefore: Mapped[int] = mapped_column(INTEGER(10), server_default=text("'20'"), comment='kho?ng th?i gian gi?i h?n l?n checkout v?n còn hi?u l?c. Tính theo phút')
    State: Mapped[int] = mapped_column(INTEGER(10), server_default=text("'1'"))
    InvalidCheckinMessage: Mapped[Optional[str]] = mapped_column(String(64, 'utf8mb4_unicode_ci'))
    InvalidCheckoutMessage: Mapped[Optional[str]] = mapped_column(String(64, 'utf8mb4_unicode_ci'))
    IsShiftConfig: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"), comment='Config dùng cho rút công theo ca hay rút công the ngày fulltime')


class Gender(Base):
    __tablename__ = 'Gender'

    GenderId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    GenderVi: Mapped[str] = mapped_column(VARCHAR(8))
    GenderEn: Mapped[str] = mapped_column(VARCHAR(8))
    Ordering: Mapped[int] = mapped_column(INTEGER(10))


class HiringRequirement(Base):
    __tablename__ = 'HiringRequirement'
    __table_args__ = (
        Index('IX_RequiredDate', 'RequiredDate'),
    )

    HiringRequirementId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    DepartmentId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    WorkProfilePositionId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    RequiredDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ExpiredDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    TotalRequirement: Mapped[Optional[int]] = mapped_column(INTEGER(10), comment='S? l??ng yêu c?u t?ng c?ng')
    ObtainingRequirement: Mapped[Optional[int]] = mapped_column(INTEGER(10), comment='S? l??ng yêu c?u ??t ???c')
    Description: Mapped[Optional[str]] = mapped_column(VARCHAR(1000))
    Status: Mapped[Optional[int]] = mapped_column(TINYINT(2), comment='Tr?ng thái')
    StatusNote: Mapped[Optional[str]] = mapped_column(VARCHAR(1000))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)


class Holiday(Base):
    __tablename__ = 'Holiday'

    Date_: Mapped[datetime.date] = mapped_column('Date', Date, primary_key=True)
    Name: Mapped[Optional[str]] = mapped_column(String(100, 'utf8mb4_unicode_ci'))
    IsHoliday: Mapped[Optional[int]] = mapped_column(TINYINT(4), comment='\\n=1 là ngày l? th?c\\n\\n0 là r?i vào cu?i tu?n, mình b? ra khi tính l??ng, Dung de tinh cong chuan nen neu ngay le trung thu 7 cn khong duoc bat len la 1')
    Description: Mapped[Optional[str]] = mapped_column(VARCHAR(200))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))


t_ImportLuong = Table(
    'ImportLuong', Base.metadata,
    Column('MaNV', VARCHAR(50)),
    Column('Column1', String(50, 'utf8mb4_unicode_ci')),
    Column('Column2', String(50, 'utf8mb4_unicode_ci')),
    Column('BHXH', INTEGER(11)),
    Column('Capbac', String(50, 'utf8mb4_unicode_ci')),
    Column('Ythuc', INTEGER(11)),
    Column('Comtrua', INTEGER(11)),
    Column('DongPhuc', INTEGER(11)),
    Column('Column3', INTEGER(11)),
    Column('KN', INTEGER(11)),
    Column('Khac', INTEGER(11)),
    Column('StaffId', INTEGER(11)),
    Column('WorkContractId', INTEGER(11)),
    Column('WorkProfileId', INTEGER(11))
)


class InComeByJobConfig(Base):
    __tablename__ = 'InComeByJobConfig'

    InComeByJobConfig: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    BusinessTypeId: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='1) Appointment\\\\n2) Receipt')
    ActionTypeId: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='1) Checkin\\\\n2) Checkout\\\\n3) Phonecall\\\\n4) Chat\\\\n5) CashCollection')
    InComeTypeId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Price: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(18, 2))
    EffectFormDate: Mapped[Optional[datetime.date]] = mapped_column(Date, server_default=text("'1990-01-01'"))
    EffectToDate: Mapped[Optional[datetime.date]] = mapped_column(Date, server_default=text("'2099-12-31'"))


class IncludeHolidayDate(Base):
    __tablename__ = 'IncludeHolidayDate'

    WorkScheduleId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    HolidayDate: Mapped[datetime.date] = mapped_column(Date, primary_key=True)


class IncomeBaseClosedOfMonth(Base):
    __tablename__ = 'IncomeBaseClosedOfMonth'

    IncomeBaseClosedOfMonthId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    ClosedTime: Mapped[Optional[datetime.date]] = mapped_column(Date)
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    WorkHours: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2))
    IncomePerHour: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class IncomeBaseDaily(Base):
    __tablename__ = 'IncomeBaseDaily'

    IncomeBaseDailyId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IncomeTypeId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IncomeTypeLevelId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    WorkDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    TimeKeeperId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IncomePerHour: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(18, 2))
    WorkHourStandard: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2))


class IncomeBonusClosedOfMonth(Base):
    __tablename__ = 'IncomeBonusClosedOfMonth'

    IncomeBonusClosedOfMonthId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    ClosedTime: Mapped[Optional[datetime.date]] = mapped_column(Date)
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    BonnusType: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'), comment='1\n Th??ng Giám Sát Chung ,2\n th??ng Ch?t l??ng D?ch v?, 3\n Th??ng Kinh doanh')
    Value: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2))
    ValueType: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='1\n Amount, 2\n Percent')
    RatingAVG: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2))
    BranchId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class IncomeBonusDaily(Base):
    __tablename__ = 'IncomeBonusDaily'

    IncomeBonusDailyId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    ClosedTime: Mapped[Optional[datetime.date]] = mapped_column(Date)
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IncomeTypeId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IncomeTypeLevelId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    BonnusType: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'), comment='1\n Th??ng Giám Sát Chung ,2\n th??ng Ch?t l??ng D?ch v?, 3\n Th??ng Kinh doanh')
    IncomeJob: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(18, 6))
    Value: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2))
    ValueType: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='1\n Amount, 2\n Percent')
    RatingAVG: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2))
    BranchId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IsCurrent: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'1'"))


class IncomeByJob(Base):
    __tablename__ = 'IncomeByJob'

    IncomeByJobId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IncomeTypeId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    BusinessType: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='1\\\\\\\\\\\\\\\\n AllocatedRevenueTracking, 2\\\\\\\\\\\\\\\\n Appoinment, 3\\\\\\\\\\\\\\\\n Phonecall, 4\\\\\\\\\\\\\\\\n Chat')
    BusinessId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    ActionType: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='1\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n Checkin, 2\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n Checkout, 3\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n Phonecall, 4\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n Treatment, 5\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n Chat')
    CustomerId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CustomerPhone: Mapped[Optional[str]] = mapped_column(String(20, 'utf8mb4_unicode_ci'))
    Note: Mapped[Optional[str]] = mapped_column(String(256, 'utf8mb4_unicode_ci'))
    Amount: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(18, 2))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    StaffBranchId: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class IncomeByJobClosedOfMonth(Base):
    __tablename__ = 'IncomeByJobClosedOfMonth'

    IncomeByJobClosedOfMonthId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    ClosedTime: Mapped[Optional[datetime.date]] = mapped_column(Date)
    BusinessType: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    NumberCases: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IncomePerCase: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class IncomeServiceConfig(Base):
    __tablename__ = 'IncomeServiceConfig'

    IncomeServiceConfigId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    ServiceId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IncomeTypeId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IncomeTypeLevelId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    EffectFromDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    EffectToDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    Value: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(18, 2))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class IncomeServiceQualityConfig(Base):
    __tablename__ = 'IncomeServiceQualityConfig'

    IncomeServiceQualityConfigId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    Name: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    Code: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))
    IncomeTypeId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IncomeTypeLevelId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    EffectFromDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    EffectToDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    FromRating: Mapped[Optional[float]] = mapped_column(Float)
    ToRating: Mapped[Optional[float]] = mapped_column(Float)
    Value: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(18, 2))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class IncomeType(Base):
    __tablename__ = 'IncomeType'

    IncomeTypeId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    Name: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'), comment='1\n Ph? tá, 2\n T? v?n viên, 3\n T? v?n viên, 4\n Giám sát v?n hành, 5\n OAM, 6\n CC Agent')
    IsDeleted: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    WorkHourPerMonth: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class IncomeTypeLevel(Base):
    __tablename__ = 'IncomeTypeLevel'

    IncomeTypeLevelId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    IncomeTypeId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Name: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    IsDeleted: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IncomePerHour: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2))
    IsIncomeByService: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IsIncomeByServiceQuality: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class IncomeTypeLevelHistory(Base):
    __tablename__ = 'IncomeTypeLevelHistory'

    Id: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    IncomeTypeLevelId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IncomeTypeId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Name: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    IsDeleted: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IncomePerHour: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2))
    IsIncomeByService: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IsIncomeByServiceQuality: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    TrackingDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))


class InsuranceHospital(Base):
    __tablename__ = 'InsuranceHospital'

    InsuranceHospitalId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    InsuranceHospitalName: Mapped[str] = mapped_column(VARCHAR(500))
    Ordering: Mapped[int] = mapped_column(INTEGER(10), server_default=text("'1'"))


t_InsuranceSession = Table(
    'InsuranceSession', Base.metadata,
    Column('InsuranceSessionId', INTEGER(10), nullable=False),
    Column('InsuranceType', SMALLINT(6), nullable=False),
    Column('FilePath', String(255, 'utf8mb4_unicode_ci'), nullable=False),
    Column('UploadedDate', DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP')),
    Column('TotalRecord', INTEGER(11), nullable=False),
    Column('TotalAmount', DECIMAL(15, 2), nullable=False),
    Column('Note', String(500, 'utf8mb4_unicode_ci')),
    Column('ErrorNote', String(255, 'utf8mb4_unicode_ci')),
    Column('IsActive', TINYINT(1), nullable=False, server_default=text("'1'")),
    Column('CreatedDate', DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP')),
    Column('CreatedStaffId', INTEGER(11), nullable=False),
    Column('UpdatedDate', DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP')),
    Column('UpdatedStaffId', INTEGER(11), nullable=False),
    Index('PK_InsuranceSession', 'InsuranceSessionId')
)


class Language(Base):
    __tablename__ = 'Language'

    LanguageId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    Name: Mapped[str] = mapped_column(VARCHAR(32))
    Ordering: Mapped[int] = mapped_column(INTEGER(11), server_default=text("'0'"))


class LanguageLevel(Base):
    __tablename__ = 'LanguageLevel'
    __table_args__ = (
        Index('fk_LanguageLevel_language', 'LanguageId'),
    )

    LanguageLevelId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    LanguageId: Mapped[int] = mapped_column(INTEGER(10))
    Ordering: Mapped[int] = mapped_column(INTEGER(10), server_default=text("'0'"))
    Level: Mapped[Optional[str]] = mapped_column(VARCHAR(255))


class MaritalStatus(Base):
    __tablename__ = 'MaritalStatus'

    MaritalStatusId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    Name: Mapped[str] = mapped_column(String(50, 'utf8mb4_bin'))
    Ordering: Mapped[int] = mapped_column(INTEGER(1), server_default=text("'0'"))


class MenuNavbar(Base):
    __tablename__ = 'MenuNavbar'

    MenuNavbarId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    NameVI: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    NameEN: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    MenuNavbarGroupId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Action: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    Alias: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    Icon: Mapped[Optional[str]] = mapped_column(String(1024, 'utf8mb4_unicode_ci'))
    NavPath: Mapped[Optional[str]] = mapped_column(String(1024, 'utf8mb4_unicode_ci'))
    Route: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    Link: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    Url: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    Priority: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    Status: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'1'"))
    CrmFullAccess: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IconURL: Mapped[Optional[str]] = mapped_column(String(1024, 'utf8mb4_unicode_ci'))
    IsDisplay: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'1'"))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class MenuNavbarGroup(Base):
    __tablename__ = 'MenuNavbarGroup'

    MenuNavbarGroupId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    NameVI: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    NameEN: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    Priority: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    Status: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'1'"))


class MenuNavbarOrgMapping(Base):
    __tablename__ = 'MenuNavbarOrgMapping'

    MenuNavbarOrgMappingId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    MenuNavbarId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    OrgId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IsDeleted: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))


class MenuNavbarPermission(Base):
    __tablename__ = 'MenuNavbarPermission'

    MenuNavbarId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    PermissionCode: Mapped[str] = mapped_column(String(128, 'utf8mb4_unicode_ci'), primary_key=True)


class MobileApp(Base):
    __tablename__ = 'MobileApp'

    MobileAppId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    Name: Mapped[str] = mapped_column(VARCHAR(64))
    AddedAt: Mapped[int] = mapped_column(INTEGER(10))
    AppToken: Mapped[str] = mapped_column(VARCHAR(32))
    Description: Mapped[Optional[str]] = mapped_column(TEXT)
    AppMarketId: Mapped[Optional[str]] = mapped_column(VARCHAR(128))


class Month(Base):
    __tablename__ = 'Month'

    MonthId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    Name: Mapped[str] = mapped_column(VARCHAR(16))
    Ordering: Mapped[int] = mapped_column(INTEGER(2))


class MonthDay(Base):
    __tablename__ = 'MonthDay'

    MonthDayId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    Name: Mapped[str] = mapped_column(VARCHAR(8))
    Ordering: Mapped[int] = mapped_column(INTEGER(2))
    StartTime: Mapped[datetime.time] = mapped_column(Time)
    EndTime: Mapped[datetime.time] = mapped_column(Time)
    TotalBreakTimeInMinute: Mapped[int] = mapped_column(INTEGER(10))


class MonthlyBonusImport(Base):
    __tablename__ = 'MonthlyBonusImport'
    __table_args__ = (
        Index('IX_MonthSalaryPeriod', 'MonthSalaryPeriod'),
    )

    Id: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    MonthSalaryPeriod: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ImportType: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='1) monthlybonus\n2)TetHoliday\n3)Additional')
    FilePath: Mapped[Optional[str]] = mapped_column(String(2048, 'utf8mb4_unicode_ci'))
    ExportPath: Mapped[Optional[str]] = mapped_column(String(2048, 'utf8mb4_unicode_ci'))
    Total: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    Success: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    Error: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    DeletedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    DeletedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class MonthlyBonusImportDetail(Base):
    __tablename__ = 'MonthlyBonusImportDetail'
    __table_args__ = (
        Index('IX_MonthlyBonusImportId', 'MonthlyBonusImportId'),
    )

    Id: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    MonthlyBonusImportId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    MonthSalaryPeriod: Mapped[Optional[datetime.date]] = mapped_column(Date)
    StaffCode: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))
    Amount: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(18, 2))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


t_NgayCong2 = Table(
    'NgayCong2', Base.metadata,
    Column('Stt', INTEGER(11)),
    Column('Mã NV', String(50, 'utf8mb4_unicode_ci')),
    Column('Họ tên', String(50, 'utf8mb4_unicode_ci')),
    Column('Công ty', String(50, 'utf8mb4_unicode_ci')),
    Column('Chức danh', String(100, 'utf8mb4_unicode_ci')),
    Column('Loại HĐ', String(50, 'utf8mb4_unicode_ci')),
    Column('Chi nhánh', String(50, 'utf8mb4_unicode_ci')),
    Column('Ngày vào làm', String(50, 'utf8mb4_unicode_ci')),
    Column('Ca làm việc', String(50, 'utf8mb4_unicode_ci')),
    Column('Tổng cộng', INTEGER(11)),
    Column('Ghi chú k chấm công', String(50, 'utf8mb4_unicode_ci')),
    Column('Số giờ lv thực tế (HIS)', String(50, 'utf8mb4_unicode_ci')),
    Column('Nghỉ phép', String(50, 'utf8mb4_unicode_ci')),
    Column('Nghỉ chế độ', String(50, 'utf8mb4_unicode_ci')),
    Column('Nghỉ lễ/tết', String(50, 'utf8mb4_unicode_ci')),
    Column('Tổng công tính lương', String(50, 'utf8mb4_unicode_ci')),
    Column('Công chuẩn', INTEGER(11)),
    Column('Lương cơ bản', Double(10, True)),
    Column('Thưởng Ý thức và Tuân thủ/Thưởng Hiệụ quả hoạt động', String(50, 'utf8mb4_unicode_ci')),
    Column('Phụ cấp Cơm trưa', String(50, 'utf8mb4_unicode_ci')),
    Column('Phụ cấp Đồng phục', String(50, 'utf8mb4_unicode_ci')),
    Column('Tổng thu nhập theo ngày công', Double(10, True)),
    Column('Thưởng CRM/CS (C.Mai)', String(50, 'utf8mb4_unicode_ci')),
    Column('Thưởng CLDV', String(50, 'utf8mb4_unicode_ci')),
    Column('Thưởng Quản lý chung', String(50, 'utf8mb4_unicode_ci')),
    Column('Thưởng hiệu quả quản lý', String(50, 'utf8mb4_unicode_ci')),
    Column('Thưởng Ebitda', String(50, 'utf8mb4_unicode_ci')),
    Column('Thưởng Vinmec', String(50, 'utf8mb4_unicode_ci')),
    Column('Thưởng an ninh', String(50, 'utf8mb4_unicode_ci')),
    Column('Thưởng Lễ/Tết', String(50, 'utf8mb4_unicode_ci')),
    Column('Tổng thưởng', String(50, 'utf8mb4_unicode_ci')),
    Column('PC Gửi xe/Công tác', String(50, 'utf8mb4_unicode_ci')),
    Column('Phụ cấp chứng chỉ hành nghề', String(50, 'utf8mb4_unicode_ci')),
    Column('Phụ cấp khác', String(50, 'utf8mb4_unicode_ci')),
    Column('Tổng phụ cấp', String(50, 'utf8mb4_unicode_ci')),
    Column('Trừ khác', String(50, 'utf8mb4_unicode_ci')),
    Column('Tổng thu nhập trước thuế', Double(10, True)),
    Column('Mức lương tham gia BHXH', String(50, 'utf8mb4_unicode_ci')),
    Column('BHYT (1,5%)', String(50, 'utf8mb4_unicode_ci')),
    Column('BHXH (8%)', String(50, 'utf8mb4_unicode_ci')),
    Column('BHTN (1%)', String(50, 'utf8mb4_unicode_ci')),
    Column('NLĐ đóng BHXH (10.5%)', String(50, 'utf8mb4_unicode_ci')),
    Column('NLĐ đóng phí Công đoàn (1%)', String(50, 'utf8mb4_unicode_ci')),
    Column('BHXH (17%', String(50, 'utf8mb4_unicode_ci')),
    Column('TNLĐ / BNN (0.5%)', String(50, 'utf8mb4_unicode_ci')),
    Column('BHYT (3%)', String(50, 'utf8mb4_unicode_ci')),
    Column('BHTN 1%', String(50, 'utf8mb4_unicode_ci')),
    Column('Doanh nghiệp đóng BHXH 21.5%', String(50, 'utf8mb4_unicode_ci')),
    Column('Doanh nghiệp đóng Công đoàn 2%', String(50, 'utf8mb4_unicode_ci')),
    Column('Không tính thuế (Phụ cấp cơm trưa/ Đồng phục)', String(50, 'utf8mb4_unicode_ci')),
    Column('TỔNG THU NHẬP CHỊU THUẾ', Double(10, True)),
    Column('Đối tượng tính Thuế TNCN', String(50, 'utf8mb4_unicode_ci')),
    Column('Cam kết', String(50, 'utf8mb4_unicode_ci')),
    Column('Số người phụ thuộc', String(50, 'utf8mb4_unicode_ci')),
    Column('TỔNG THU NHẬP TÍNH THUẾ', String(50, 'utf8mb4_unicode_ci')),
    Column('Thu Tiền thuế TNCN', String(50, 'utf8mb4_unicode_ci')),
    Column('Thực lãnh', INTEGER(11)),
    Column('Cty đóng hộ BHXH', String(50, 'utf8mb4_unicode_ci')),
    Column('Thu hộ tiền BHXH (21.5%', String(50, 'utf8mb4_unicode_ci')),
    Column('Chuyển khoản', INTEGER(11))
)


class Notification(Base):
    __tablename__ = 'Notification'

    NotificationId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    Code: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))
    Name: Mapped[Optional[str]] = mapped_column(String(512, 'utf8mb4_unicode_ci'))
    Summary: Mapped[Optional[str]] = mapped_column(String(1024, 'utf8mb4_unicode_ci'))
    Content: Mapped[Optional[str]] = mapped_column(LONGTEXT)
    ContentType: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='1 Text\n2 Video\n3 Link')
    Priority: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='1 High, \n2 Nomal,\n3 Low')
    Status: Mapped[Optional[int]] = mapped_column(TINYINT(4), comment='1 New, \n2 Waiiting,\n3 Approved,\n4 Rejected,\n5 Recall')
    StatusNote: Mapped[Optional[str]] = mapped_column(String(1024, 'utf8mb4_unicode_ci'))
    NotificationTemplateId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IsComment: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'1'"))
    Position: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'0'"), comment='1 Normal\n2 Banner')
    PublishedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    FromDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text("'2001-01-01 00:00:00'"))
    ToDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text("'2999-01-01 00:00:00'"))
    KIMHuman: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'0'"))


class NotificationBanner(Base):
    __tablename__ = 'NotificationBanner'

    NotificationBannerId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    NotificationId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CDNURL: Mapped[Optional[str]] = mapped_column(String(1024, 'utf8mb4_unicode_ci'))
    Type: Mapped[Optional[int]] = mapped_column(TINYINT(4))
    Duration: Mapped[Optional[int]] = mapped_column(INTEGER(4))
    Link: Mapped[Optional[str]] = mapped_column(String(1024, 'utf8mb4_unicode_ci'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))


class NotificationComment(Base):
    __tablename__ = 'NotificationComment'

    NotificationCommentId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    NotificationId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Comment: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_unicode_ci'))
    ParentNoticationCommentId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    RemovedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    RemovedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)


class NotificationLike(Base):
    __tablename__ = 'NotificationLike'

    NotificationLikeId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    NotificationId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))


class NotificationReadInfo(Base):
    __tablename__ = 'NotificationReadInfo'

    NotificationReadInfoId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    NoticationId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))


class NotificationRecipient(Base):
    __tablename__ = 'NotificationRecipient'

    NotificationRecipientId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    NotificationId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    RecipientId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    RecipientType: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='1 Org\\n2 Staff')
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IsIncludeSubNode: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'0'"))


class NotificationRequestApproved(Base):
    __tablename__ = 'NotificationRequestApproved'

    NotificationRequestApprovedtId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    NotificationId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    ObjectSource: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='1 Org\\n2 Staff')
    ObjectId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Status: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='1 waiting, 2 approved, 3 Reject, 4 Cancel')
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class NotificationStatus(Base):
    __tablename__ = 'NotificationStatus'

    NotificationStatusId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    NotificationId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Status: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='1 New\n2 Waiiting\n3 Approved\n4 Waiiting\n5 Rejected\n6 Recall')
    StatusNote: Mapped[Optional[str]] = mapped_column(String(256, 'utf8mb4_unicode_ci'))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class NotificationTemplate(Base):
    __tablename__ = 'NotificationTemplate'

    NotificationTemplateId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    NotificationTemplateCode: Mapped[Optional[str]] = mapped_column(String(1024, 'utf8mb4_unicode_ci'))
    Content: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_unicode_ci'))
    IsDeleted: Mapped[Optional[int]] = mapped_column(TINYINT(4))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Priority: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    IsIncludeSubNode: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'0'"))


class NotificationTemplateConfig(Base):
    __tablename__ = 'NotificationTemplateConfig'

    NotificationTemplateConfigId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    NotificationTemplateId: Mapped[int] = mapped_column(INTEGER(11))
    ImpactType: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='1 Receiver\n2 ApprovedBy')
    ObjectSource: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    ObjectId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IsIncludeSubNode: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'0'"))


class Org(Base):
    __tablename__ = 'Org'

    OrgId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    OrgCode: Mapped[str] = mapped_column(String(200, 'utf8mb4_unicode_ci'))
    OrgName: Mapped[str] = mapped_column(String(200, 'utf8mb4_unicode_ci'))
    CompanyId: Mapped[int] = mapped_column(INTEGER(10))
    ParentId: Mapped[int] = mapped_column(INTEGER(11), server_default=text("'0'"))
    NumAnnualLeaveTraining: Mapped[int] = mapped_column(INTEGER(5))
    IsViewAllBranch: Mapped[int] = mapped_column(INTEGER(1))
    IsTimekeeping: Mapped[int] = mapped_column(INTEGER(1))
    IsActive: Mapped[int] = mapped_column(INTEGER(1))
    PosLeft: Mapped[int] = mapped_column(INTEGER(5), server_default=text("'0'"))
    PosRight: Mapped[int] = mapped_column(INTEGER(5), server_default=text("'0'"))
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedStaffId: Mapped[int] = mapped_column(INTEGER(11), server_default=text("'0'"))
    DefaultBranchId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    RoleCode: Mapped[Optional[str]] = mapped_column(String(32, 'utf8mb4_unicode_ci'))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    UpdatedStaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    ParentDeleteOrgId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Level: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    BranchId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IsSolvingTicket: Mapped[Optional[int]] = mapped_column(SMALLINT(2))


t_Org2 = Table(
    'Org2', Base.metadata,
    Column('OrgId', INTEGER(10), nullable=False, server_default=text("'0'")),
    Column('OrgCode', String(200, 'utf8mb4_unicode_ci'), nullable=False),
    Column('OrgName', String(200, 'utf8mb4_unicode_ci'), nullable=False),
    Column('CompanyId', INTEGER(10), nullable=False),
    Column('ParentId', INTEGER(11), nullable=False, server_default=text("'0'")),
    Column('DefaultBranchId', INTEGER(10)),
    Column('NumAnnualLeaveTraining', INTEGER(5), nullable=False),
    Column('IsViewAllBranch', INTEGER(1), nullable=False),
    Column('IsTimekeeping', INTEGER(1), nullable=False),
    Column('IsActive', INTEGER(1), nullable=False),
    Column('PosLeft', INTEGER(5), nullable=False, server_default=text("'0'")),
    Column('PosRight', INTEGER(5), nullable=False, server_default=text("'0'")),
    Column('RoleCode', String(32, 'utf8mb4_unicode_ci')),
    Column('CreatedDate', DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP')),
    Column('CreatedStaffId', INTEGER(11), nullable=False, server_default=text("'0'")),
    Column('UpdatedDate', DateTime, server_default=text('CURRENT_TIMESTAMP')),
    Column('UpdatedStaffId', INTEGER(11), server_default=text("'0'")),
    Column('ParentDeleteOrgId', INTEGER(11)),
    Column('Level', INTEGER(11)),
    Column('BranchId', INTEGER(11))
)


t_Org20230228 = Table(
    'Org20230228', Base.metadata,
    Column('OrgId', INTEGER(10), nullable=False, server_default=text("'0'")),
    Column('OrgCode', VARCHAR(200), nullable=False),
    Column('OrgName', VARCHAR(200), nullable=False),
    Column('CompanyId', INTEGER(10), nullable=False),
    Column('ParentId', INTEGER(11), nullable=False, server_default=text("'0'")),
    Column('DefaultBranchId', INTEGER(10)),
    Column('NumAnnualLeaveTraining', INTEGER(5), nullable=False),
    Column('IsViewAllBranch', INTEGER(1), nullable=False),
    Column('IsTimekeeping', INTEGER(1), nullable=False),
    Column('IsActive', INTEGER(1), nullable=False),
    Column('PosLeft', INTEGER(5), nullable=False, server_default=text("'0'")),
    Column('PosRight', INTEGER(5), nullable=False, server_default=text("'0'")),
    Column('RoleCode', VARCHAR(32)),
    Column('CreatedDate', DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP')),
    Column('CreatedStaffId', INTEGER(11), nullable=False, server_default=text("'0'")),
    Column('UpdatedDate', DateTime, server_default=text('CURRENT_TIMESTAMP')),
    Column('UpdatedStaffId', INTEGER(11), server_default=text("'0'")),
    Column('ParentDeleteOrgId', INTEGER(11)),
    Column('Level', INTEGER(11))
)


class OrgBranch(Base):
    __tablename__ = 'OrgBranch'
    __table_args__ = (
        Index('uq_Branch_Org', 'BranchId', 'OrgId', unique=True),
    )

    IsVirtual: Mapped[int] = mapped_column(INTEGER(1), server_default=text("'1'"))
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedStaffId: Mapped[int] = mapped_column(INTEGER(10), server_default=text("'0'"))
    OrgBranchId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    OrgId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    BranchId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    UpdatedStaffId: Mapped[Optional[int]] = mapped_column(INTEGER(10), server_default=text("'0'"))


class OrgBranchAudit(Base):
    __tablename__ = 'OrgBranchAudit'

    revision: Mapped[int] = mapped_column(INTEGER(6), primary_key=True)
    ActionDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    OrgId: Mapped[int] = mapped_column(INTEGER(10))
    IsVirtual: Mapped[int] = mapped_column(INTEGER(1))
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedStaffId: Mapped[int] = mapped_column(INTEGER(10), server_default=text("'0'"))
    action: Mapped[Optional[str]] = mapped_column(String(8, 'utf8mb4_unicode_ci'), server_default=text("'insert'"))
    BranchId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    UpdatedStaffId: Mapped[Optional[int]] = mapped_column(INTEGER(10), server_default=text("'0'"))


class OrgHierarchy(Base):
    __tablename__ = 'OrgHierarchy'

    OrgHierarchyId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    NameEn: Mapped[str] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    NameVi: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    Priority: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    Status: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'1'"), comment='1 active\n0 deactice')
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))


class OrgManagerResp(Base):
    __tablename__ = 'OrgManagerResp'

    OrgId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    WorkProfileId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    RespOrgId: Mapped[int] = mapped_column(INTEGER(10))
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedStaffId: Mapped[int] = mapped_column(INTEGER(10), server_default=text("'0'"))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    UpdatedStaffId: Mapped[Optional[int]] = mapped_column(INTEGER(10), server_default=text("'0'"))


class OrgOffice(Base):
    __tablename__ = 'OrgOffice'

    OrgOfficeId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    NameEn: Mapped[str] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    NameVi: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    OrgId: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    Priority: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    Status: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'1'"), comment='1 active\n0 deactice')
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))


class OrgPosistionType(Base):
    __tablename__ = 'OrgPosistionType'

    PosistionTypeId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    PosistionTypeName: Mapped[Optional[str]] = mapped_column(String(32, 'utf8mb4_unicode_ci'))
    CreatedTime: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))


class OrgWorkProfile(Base):
    __tablename__ = 'OrgWorkProfile'
    __table_args__ = (
        Index('Idx_StaffId', 'StaffId'),
        Index('Idx_UserId', 'UserId'),
        Index('idx_OrgId', 'OrgId'),
        Index('idx_WorkProfileID', 'WorkProfileId')
    )

    OrgWorkProfileId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    OrgId: Mapped[int] = mapped_column(INTEGER(11))
    IsMainPosition: Mapped[int] = mapped_column(TINYINT(4), server_default=text("'0'"))
    WorkProfileId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Status: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='0: Deleted | 1: Active')
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    PosistionType: Mapped[Optional[int]] = mapped_column(TINYINT(3), server_default=text("'1'"), comment='1 Normal,2 Manager, 3 Concurrently')
    FromDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    ToDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    ObjectType: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='1:WorkContractAnnex, 2:WorkPlaceChanging')
    ObjectId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    ExpectedToDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='when update Todate move ToDate data to ExpectedToDate')
    IsProcess: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    RefWorkProfileId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IsHidden: Mapped[Optional[int]] = mapped_column(TINYINT(1))
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UserId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    WorkProfilePositionId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    AutoRenew: Mapped[Optional[int]] = mapped_column(TINYINT(1), server_default=text("'1'"))


class PaidHoliday(Base):
    __tablename__ = 'PaidHoliday'
    __table_args__ = (
        Index('Date_UNIQUE', 'Date', unique=True),
    )

    Id: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    Date_: Mapped[Optional[datetime.date]] = mapped_column('Date', Date)
    Name: Mapped[Optional[str]] = mapped_column(String(128, 'utf8mb4_unicode_ci'))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))


class ParamConfig(Base):
    __tablename__ = 'ParamConfig'

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    ObjectCode: Mapped[str] = mapped_column(String(50), primary_key=True)
    ObjectValue: Mapped[str] = mapped_column(String(100), primary_key=True)
    Priority: Mapped[int] = mapped_column(SMALLINT(6), server_default=text("'1'"))
    DisplayName: Mapped[Optional[str]] = mapped_column(String(100))
    ExtendedData: Mapped[Optional[str]] = mapped_column(TEXT)
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))


class Permission(Base):
    __tablename__ = 'Permission'
    __table_args__ = (
        Index('UNIQUE', 'PermissionCode', unique=True),
    )

    PermissionCodeId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    PermissionCode: Mapped[str] = mapped_column(String(128))
    TypeCode: Mapped[str] = mapped_column(String(256))
    Name: Mapped[Optional[str]] = mapped_column(String(256))
    Description: Mapped[Optional[str]] = mapped_column(String(1048))
    Priority: Mapped[Optional[int]] = mapped_column(INTEGER(10), server_default=text("'1'"))
    IsActive: Mapped[Optional[int]] = mapped_column(TINYINT(1), server_default=text("'1'"))
    Parent: Mapped[Optional[str]] = mapped_column(String(255))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class PermissionGeneral(Base):
    __tablename__ = 'PermissionGeneral'

    PermissionGeneralId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    GroupCode: Mapped[Optional[str]] = mapped_column(String(128), server_default=text("'PK'"))
    PermissionCode: Mapped[Optional[str]] = mapped_column(String(128))
    ActionValue: Mapped[Optional[str]] = mapped_column(String(128))
    IsActive: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'1'"))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class PermissionWorkProfilePosition(Base):
    __tablename__ = 'PermissionWorkProfilePosition'
    __table_args__ = (
        Index('idx_WorkProfilePositionId_PermissionCode', 'WorkProfilePositionId', 'PermissionCode', unique=True),
    )

    PermissionWorkProfilePositionId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    WorkProfilePositionId: Mapped[int] = mapped_column(INTEGER(11))
    PermissionCode: Mapped[str] = mapped_column(String(128))
    Filter: Mapped[str] = mapped_column(String(128), server_default=text("'None'"), comment='None: Lấy data theo tất cả chi nhánh | IP: Lấy data theo IP của chi nhánh | OrgChart: Lấy data các chi nhánh theo OrgChart | KimCompanyGroup: Lấy danh sách data theo các công ty của KIM được cấu hình trong ParamConfig')
    ActionValue: Mapped[Optional[str]] = mapped_column(String(256))
    Priority: Mapped[Optional[int]] = mapped_column(INTEGER(10), server_default=text("'1'"))
    IsActive: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'1'"))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class Person(Base):
    __tablename__ = 'Person'

    PersonId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    FullName: Mapped[str] = mapped_column(VARCHAR(300))
    Gender_: Mapped[Optional[int]] = mapped_column('Gender', TINYINT(1))
    Birthday: Mapped[Optional[datetime.date]] = mapped_column(Date)
    Address: Mapped[Optional[str]] = mapped_column(VARCHAR(1000))
    PhoneNumber: Mapped[Optional[str]] = mapped_column(VARCHAR(15))
    Email_: Mapped[Optional[str]] = mapped_column('Email', VARCHAR(255))
    Note: Mapped[Optional[str]] = mapped_column(TEXT)
    CountryId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    ProvinceId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    DistrictId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    WardId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    FromChannelId: Mapped[Optional[int]] = mapped_column(TINYINT(2))
    Status: Mapped[Optional[int]] = mapped_column(TINYINT(2), server_default=text("'0'"), comment='1 ?ng Viên\\n10 ?ã lên l?ch phong v?n\\n20) Pass Ph?ng v?n\\n30) R?t ph?ng v?n\\n40) ?ã nh?n Offer\\n50) Nhân Viên\\n60) Ngh? vi?c')
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(10))


class Province(Base):
    __tablename__ = 'Province'

    ProvinceId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    ProviceCode: Mapped[Optional[str]] = mapped_column(String(5, 'utf8mb4_unicode_ci'))
    ProvinceName: Mapped[Optional[str]] = mapped_column(String(100, 'utf8mb4_unicode_ci'))
    Label: Mapped[Optional[str]] = mapped_column(String(20, 'utf8mb4_unicode_ci'))
    State: Mapped[Optional[int]] = mapped_column(TINYINT(1), server_default=text("'1'"))
    VnProvinceId: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class PublicAsset(Base):
    __tablename__ = 'PublicAsset'
    __table_args__ = {'comment': 'Các tài s?n công c?p cho nhân viên'}

    PublicAssetId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    Name: Mapped[str] = mapped_column(String(32, 'utf8mb4_unicode_ci'))
    Ordering: Mapped[int] = mapped_column(INTEGER(11), server_default=text("'0'"))
    State: Mapped[int] = mapped_column(INTEGER(1), server_default=text("'1'"))

    StaffPublicAsset: Mapped[List['StaffPublicAsset']] = relationship('StaffPublicAsset', back_populates='PublicAsset_')


class Reason(Base):
    __tablename__ = 'Reason'

    ReasonId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    ReasonGroupId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Name: Mapped[Optional[str]] = mapped_column(String(512))
    Code: Mapped[Optional[str]] = mapped_column(String(255))
    Priority: Mapped[Optional[int]] = mapped_column(SMALLINT(6))
    State: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    LastUpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    LastUpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))


class ReasonGroup(Base):
    __tablename__ = 'ReasonGroup'

    ReasonGroupId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    Name: Mapped[Optional[str]] = mapped_column(String(255))
    Code: Mapped[Optional[str]] = mapped_column(String(45))
    Priority: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    State: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    LastUpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    LastUpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class RegistedMobileDevice(Base):
    __tablename__ = 'RegistedMobileDevice'
    __table_args__ = (
        Index('fk_RegistedMobileDevice_RegistedBy_idx', 'RegistedBy'),
        Index('fk_RegistedMobileDevice_Staff_idx', 'StaffId')
    )

    RegistedMobileDeviceId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    RegistedAt: Mapped[int] = mapped_column(INTEGER(10), comment='th?i ?i?m ??ng kí thi?t b? v?i h? th?ng')
    RegistedBy: Mapped[int] = mapped_column(INTEGER(10), comment='ng??i th?c hi?n ??ng kí mobile v?i h? th?ng')
    StaffId: Mapped[int] = mapped_column(INTEGER(10))
    State: Mapped[int] = mapped_column(INTEGER(1), server_default=text("'0'"), comment='tr?ng thái c?a device:\n-1: deactivated\n0: pending\n1: active')
    MobileDeviceInfo: Mapped[Optional[str]] = mapped_column(VARCHAR(188))
    ApprovedAt: Mapped[Optional[int]] = mapped_column(INTEGER(10), server_default=text("'0'"))
    ApprovedBy: Mapped[Optional[int]] = mapped_column(INTEGER(10), server_default=text("'0'"))


class RegularGroup(Base):
    __tablename__ = 'RegularGroup'

    RegularGroupId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    CompanyId: Mapped[int] = mapped_column(INTEGER(10))
    NameVi: Mapped[str] = mapped_column(String(32, 'utf8mb4_unicode_ci'))
    NameEn: Mapped[str] = mapped_column(String(32, 'utf8mb4_unicode_ci'))
    Ordering: Mapped[int] = mapped_column(INTEGER(10), server_default=text("'0'"))
    RootId: Mapped[int] = mapped_column(INTEGER(10))
    ParentId: Mapped[int] = mapped_column(INTEGER(10))
    Lft: Mapped[int] = mapped_column(INTEGER(10))
    Rgt: Mapped[int] = mapped_column(INTEGER(10))
    Level: Mapped[int] = mapped_column(INTEGER(10))


class RegulationsAndPolicies(Base):
    __tablename__ = 'RegulationsAndPolicies'

    Id: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    Title: Mapped[Optional[str]] = mapped_column(String(4096, 'utf8mb4_unicode_ci'))
    Path: Mapped[Optional[str]] = mapped_column(String(4096, 'utf8mb4_unicode_ci'))
    Priority: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'99999'"))
    IsDeleted: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class Relationship(Base):
    __tablename__ = 'Relationship'
    __table_args__ = (
        Index('fk_Relationship_RelationshipGroup_idx', 'RelationshipGroupId'),
    )

    RelationshipId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    RelationshipGroupId: Mapped[int] = mapped_column(INTEGER(10))
    Name: Mapped[Optional[str]] = mapped_column(String(64, 'utf8mb4_unicode_ci'))
    Ordering: Mapped[Optional[int]] = mapped_column(INTEGER(10), server_default=text("'0'"))


class RelationshipGroup(Base):
    __tablename__ = 'RelationshipGroup'

    RelationshipGroupId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True, comment='Gia ?ình\nCùng công ty\nB?n bè')
    Name: Mapped[Optional[str]] = mapped_column(String(64, 'utf8mb4_unicode_ci'))
    Ordering: Mapped[Optional[int]] = mapped_column(INTEGER(10), server_default=text("'0'"))


class RentalContract(Base):
    __tablename__ = 'RentalContract'

    RentalContractId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    RentalContractTypeId: Mapped[int] = mapped_column(INTEGER(11))
    Name: Mapped[str] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    Code: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    Representative: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    BranchId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    SignedDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    FromDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ToDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    TerminationDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    TerminationReason: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_unicode_ci'))
    ProcessContent: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_unicode_ci'))
    IsTermination: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'0'"))
    IsProcessed: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'0'"))
    IsAlert: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'1'"))
    State: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'1'"), comment='1: active, 0: expired')
    AlertType: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'), server_default=text("'Day'"))
    AlertBeforeTime: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    PartnerCompany: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    PartnerAddress: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    PartnerRepresentative: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    PartnerEmail: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    PartnerPhone: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'))
    Comment: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_unicode_ci'))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class RentalContractDocument(Base):
    __tablename__ = 'RentalContractDocument'

    RentalContractDocumentId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    RentalContractId: Mapped[int] = mapped_column(INTEGER(11))
    CDN: Mapped[str] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    IsDelete: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'0'"))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class RentalContractTracking(Base):
    __tablename__ = 'RentalContractTracking'

    RentalContractTrackingId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    RentalContractId: Mapped[int] = mapped_column(INTEGER(11))
    RentalContractTypeId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Name: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    Code: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    Representative: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    BranchId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    SignedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    FromDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    ToDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    TerminationDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    TerminationReason: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_unicode_ci'))
    ProcessContent: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_unicode_ci'))
    IsTermination: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'0'"))
    IsProcessed: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'0'"))
    IsAlert: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'1'"))
    State: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'1'"), comment='1: active, 2: expired, 3: alert')
    AlertType: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'), server_default=text("'Day'"))
    AlertBeforeTime: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    PartnerCompany: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    PartnerAddress: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    PartnerRepresentative: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    PartnerEmail: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    PartnerPhone: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'))
    Comment: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_unicode_ci'))
    ActionName: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class RentalContractType(Base):
    __tablename__ = 'RentalContractType'

    RentalContractTypeId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    Name: Mapped[str] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    Code: Mapped[Optional[str]] = mapped_column(String(25, 'utf8mb4_unicode_ci'))
    Priority: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'0'"))
    IsDelete: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'0'"))


class RewardDiscipline(Base):
    __tablename__ = 'RewardDiscipline'

    RewardDisciplineId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Type: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='1:Reward\n2:Discipline')
    Content: Mapped[Optional[str]] = mapped_column(String(8000, 'utf8mb4_unicode_ci'))
    Method: Mapped[Optional[str]] = mapped_column(String(4000, 'utf8mb4_unicode_ci'))
    RecordedDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ApprovedByStaff: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Status: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    UpadtedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)


class Role(Base):
    __tablename__ = 'Role'

    RoleId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    RoleName: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    State: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'1'"))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)


class RoleMenuNavbar(Base):
    __tablename__ = 'RoleMenuNavbar'

    RoleMenuNavbarId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    RoleId: Mapped[int] = mapped_column(INTEGER(11))
    MenuNavbarId: Mapped[int] = mapped_column(INTEGER(11))
    State: Mapped[int] = mapped_column(TINYINT(4), server_default=text("'1'"))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))


class RolePermission(Base):
    __tablename__ = 'RolePermission'

    RolePermissionId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    RoleId: Mapped[int] = mapped_column(INTEGER(11))
    PermissionId: Mapped[int] = mapped_column(INTEGER(11))
    State: Mapped[int] = mapped_column(TINYINT(4), server_default=text("'1'"))
    Filter: Mapped[Optional[str]] = mapped_column(String(128, 'utf8mb4_unicode_ci'), server_default=text("'None'"))
    ActionValue: Mapped[Optional[str]] = mapped_column(String(128, 'utf8mb4_unicode_ci'), server_default=text("'100000'"))
    Priority: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'1'"))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))


t_RoleWorkProfilePosition_formapping = Table(
    'RoleWorkProfilePosition_formapping', Base.metadata,
    Column('RoleId', INTEGER(11)),
    Column('RoleName', String(255, 'utf8mb4_unicode_ci')),
    Column('WorkProfilePositionId', INTEGER(11)),
    Column('State', TINYINT(4), server_default=text("'1'")),
    Column('CreatedBy', INTEGER(11)),
    Column('CreatedDate', DateTime, server_default=text('CURRENT_TIMESTAMP')),
    Column('UpdatedBy', INTEGER(11)),
    Column('UpdatedDate', DateTime)
)


class SalaryAllowances(Base):
    __tablename__ = 'SalaryAllowances'

    SalaryAllowancesId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    ObjectSourceType: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'), comment='WorkContract, WorkContractAnnex')
    ObjectSourceId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    SalaryAllowancesTypeId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    SalaryAllowancesTypeNote: Mapped[Optional[str]] = mapped_column(String(256, 'utf8mb4_unicode_ci'))
    Amount: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(18, 2))
    IsDeleted: Mapped[Optional[int]] = mapped_column(SMALLINT(6), server_default=text("'0'"))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class SalaryAllowancesType(Base):
    __tablename__ = 'SalaryAllowancesType'

    SalaryAllowancesTypeId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    Name: Mapped[Optional[str]] = mapped_column(String(1024, 'utf8mb4_unicode_ci'))
    IsDeleted: Mapped[Optional[int]] = mapped_column(SMALLINT(6), server_default=text("'0'"))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreateDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))


class SalaryPerHour(Base):
    __tablename__ = 'SalaryPerHour'
    __table_args__ = (
        Index('IX_StaffId', 'StaffId', 'StartDate', 'EndDate'),
        Index('IX_StartDate_EndDate', 'StartDate', 'EndDate')
    )

    Id: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    StartDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    EndDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    PositionId: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='1: T? v?n viên, 2: Ph? tá, 3: Qu?n lý phòng khám')
    WorkProfilePositionId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    WorkProfilePositionLevel: Mapped[Optional[str]] = mapped_column(VARCHAR(50))
    Amount: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(15, 5))


class ScoreCampaign(Base):
    __tablename__ = 'ScoreCampaign'

    ScoreCampaignId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    Code: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))
    Name: Mapped[Optional[str]] = mapped_column(String(512, 'utf8mb4_unicode_ci'))
    Description: Mapped[Optional[str]] = mapped_column(String(512, 'utf8mb4_unicode_ci'))
    MinScoreToPass: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'10'"))
    IsCycle: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'1'"))
    ScoreMethod: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'1'"), comment='1 Arrived\n2 Camera')
    AlertMethod: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'1'"), comment='1 SMS \n2 Email \n 3 Ticket')
    FromDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    ToDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    NumerTime: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'1'"))
    Unit: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"), comment='1 Ngày\n2 tuan\n3 thang')
    MinimunToNextTime: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"), comment='hour')
    IsIncludeSubNode: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'1'"))
    TicketProcessingTime: Mapped[Optional[int]] = mapped_column(TINYINT(4), comment='hour')
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class ScoreCampaignBranch(Base):
    __tablename__ = 'ScoreCampaignBranch'

    ScoreCampaignBranchId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    BranchId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    NumberTreatmentRoom: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    NumberXRAYRoom: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    ScoreCampaignBranchcol1: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class ScoreCampaignCriterionDetail(Base):
    __tablename__ = 'ScoreCampaignCriterionDetail'

    ScoreCampaignCriterionDetailld: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    ScoreCampaignId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    ScoreCriterionId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Score: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'0'"))
    Priority: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'1'"))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class ScoreCampaignImpact(Base):
    __tablename__ = 'ScoreCampaignImpact'

    ScoreCampaignImpactId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    ScoreCampaignId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Code: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))
    Name: Mapped[Optional[str]] = mapped_column(String(512, 'utf8mb4_unicode_ci'))
    ActionByObject: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='1 Org\\n2 Staff')
    ActionById: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    ApplyToObject: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'0'"), comment='1 nguoi ch?m\\n2 là ???c ch?m')
    ApplyToId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class ScoreCampaignType(Base):
    __tablename__ = 'ScoreCampaignType'

    ScoreCampaignTypeId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    Name: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))


class ScoreCard(Base):
    __tablename__ = 'ScoreCard'

    ScoreCardId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    ScoreCampaignId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Status: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='1 New\n2 Working\n3 Completed')
    ActionDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    DueDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    ActionByObject: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='1 Org, \n2 Staff')
    ActionBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    ApplyToObject: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='1 Org, \n2 Staff')
    ApplyToId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    TotalScore: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'0'"))
    ScoreAchieved: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IsIncludeSubNode: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'0'"))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CompletedByStaff: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CompletedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)


class ScoreCardDetail(Base):
    __tablename__ = 'ScoreCardDetail'

    ScoreCardDetailId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    ScoreCardId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    ScoreCriterionId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Score: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'0'"))
    Priority: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'1'"))
    IsPass: Mapped[Optional[int]] = mapped_column(TINYINT(4))
    Content: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_unicode_ci'))
    DueDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class ScoreCardDetailMedia(Base):
    __tablename__ = 'ScoreCardDetailMedia'

    ScoreCardDetailMediaId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    ScoreCardId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    ScoreCardDetailId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    URL: Mapped[Optional[str]] = mapped_column(String(1024, 'utf8mb4_unicode_ci'))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class ScoreCardTicket(Base):
    __tablename__ = 'ScoreCardTicket'

    ScoreCardTicketId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    ScoreCardId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    ScoreCardDetailId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Code: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))
    Name: Mapped[Optional[str]] = mapped_column(String(512, 'utf8mb4_unicode_ci'))
    Status: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='1 New\n2 Working\n3 Completed,4 Reject')
    StatusNote: Mapped[Optional[str]] = mapped_column(String(512, 'utf8mb4_unicode_ci'))
    DueDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    MediaURL: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    FinalResult: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"), comment='1 ??t\\n2 không ?atk')
    RefCode: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))
    PeriodDueTime: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='tính theo phút')
    IsCurrent: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'1'"))
    CompletedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    CompletedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class ScoreCardTicketMedia(Base):
    __tablename__ = 'ScoreCardTicketMedia'

    ScoreCardTicketMediaId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    ScoreCardTicketId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CDNURL: Mapped[Optional[str]] = mapped_column(String(1024, 'utf8mb4_unicode_ci'))
    Priority: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))


class ScoreCriterion(Base):
    __tablename__ = 'ScoreCriterion'

    ScoreCriterionId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    Code: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))
    Name: Mapped[Optional[str]] = mapped_column(String(512, 'utf8mb4_unicode_ci'))
    Description: Mapped[Optional[str]] = mapped_column(String(8000, 'utf8mb4_unicode_ci'))
    ScoreCriterionCategoryId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    DefaultScore: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'0'"))
    Type: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'0'"), comment='1 Text\n2 Meida')
    IsDeleted: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'0'"))
    Priority: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class ScoreCriterionCategory(Base):
    __tablename__ = 'ScoreCriterionCategory'

    ScoreCriterionCategoryId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    Code: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))
    Name: Mapped[Optional[str]] = mapped_column(String(512, 'utf8mb4_unicode_ci'))
    Description: Mapped[Optional[str]] = mapped_column(String(512, 'utf8mb4_unicode_ci'))
    IsDeleted: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'0'"))
    Priority: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'0'"))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class ServiceBranchMappingExclude(Base):
    __tablename__ = 'ServiceBranchMappingExclude'

    ServiceBranchMappingExcludeId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    ServiceId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    BranchId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))


class Staff(Base):
    __tablename__ = 'Staff'
    __table_args__ = (
        Index('IX_FullName', 'FullName'),
        Index('IX_PersonId', 'PersonId'),
        Index('IX_StaffCode', 'StaffCode'),
        Index('UserId_UNIQUE', 'UserId', unique=True)
    )

    StaffId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    StaffCode: Mapped[str] = mapped_column(VARCHAR(16))
    CreatedAt: Mapped[int] = mapped_column(INTEGER(10))
    CreatedBy: Mapped[int] = mapped_column(INTEGER(10))
    State: Mapped[int] = mapped_column(INTEGER(1), server_default=text("'1'"), comment='tr?ng thái nhân viên này1 - ?ang làm vi?c2- ?ã ngh? vi?c 3- nhân viên t?m')
    GenderId: Mapped[int] = mapped_column(INTEGER(10))
    IdNumber: Mapped[Optional[str]] = mapped_column(VARCHAR(16))
    IdNumberIssuedAt: Mapped[Optional[datetime.date]] = mapped_column(Date)
    IdNumberIssuedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    PassportNumber: Mapped[Optional[str]] = mapped_column(VARCHAR(16))
    NationalInsuranceNumber: Mapped[Optional[str]] = mapped_column(VARCHAR(16))
    TaxNumber: Mapped[Optional[str]] = mapped_column(String(64, 'utf8mb4_unicode_ci'))
    UserId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    FullName: Mapped[Optional[str]] = mapped_column(VARCHAR(64))
    FullNameNoSign: Mapped[Optional[str]] = mapped_column(VARCHAR(64))
    LastName: Mapped[Optional[str]] = mapped_column(VARCHAR(16))
    LastNameNoSign: Mapped[Optional[str]] = mapped_column(VARCHAR(16))
    DateOfBirth: Mapped[Optional[datetime.date]] = mapped_column(Date)
    PrimaryEmail: Mapped[Optional[str]] = mapped_column(VARCHAR(255))
    Photo: Mapped[Optional[str]] = mapped_column(VARCHAR(128), comment='hình ??i di?n c?a ng??i lao ??ng n?p cho công ty')
    DegreeId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    InsuranceHospitalId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    UpdatedAt: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    Nationality: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    StaffCodeKIM: Mapped[Optional[str]] = mapped_column(VARCHAR(20), comment='C?t Tmp ?? migrate d? li?u')
    MaritalStatusId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Note: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_unicode_ci'))
    PlaceOfBirth: Mapped[Optional[str]] = mapped_column(String(128, 'utf8mb4_unicode_ci'))
    IsTimekeeping: Mapped[Optional[int]] = mapped_column(SMALLINT(1), comment='0: no checkin; 1 checkin; null get parent value (team)')
    EducationalLevel: Mapped[Optional[str]] = mapped_column(String(25, 'utf8mb4_unicode_ci'))
    GradeLevel: Mapped[Optional[str]] = mapped_column(String(25, 'utf8mb4_unicode_ci'))
    OldStaffCode: Mapped[Optional[str]] = mapped_column(String(25, 'utf8mb4_unicode_ci'))
    Migrate: Mapped[Optional[str]] = mapped_column(String(25, 'utf8mb4_unicode_ci'))
    ModifiedFormValue: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'1048575'"), comment='0: Desibled All\\n1048576: Edit All')
    PersonId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    IsTest: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'0'"))
    PINCode: Mapped[Optional[str]] = mapped_column(CHAR(6, 'utf8mb4_unicode_ci'))

    DependantPeople: Mapped[List['DependantPeople']] = relationship('DependantPeople', back_populates='Staff_')
    ResponsiblePersion: Mapped[List['ResponsiblePersion']] = relationship('ResponsiblePersion', back_populates='Staff_')
    StaffAddress: Mapped[List['StaffAddress']] = relationship('StaffAddress', back_populates='Staff_')
    StaffAttendanceRecord: Mapped[List['StaffAttendanceRecord']] = relationship('StaffAttendanceRecord', back_populates='Staff_')
    StaffPublicAsset: Mapped[List['StaffPublicAsset']] = relationship('StaffPublicAsset', back_populates='Staff_')
    WorkProfile: Mapped[List['WorkProfile']] = relationship('WorkProfile', back_populates='Staff_')
    AbsenceRequest: Mapped[List['AbsenceRequest']] = relationship('AbsenceRequest', back_populates='Staff_')
    WorkSchedule: Mapped[List['WorkSchedule']] = relationship('WorkSchedule', back_populates='Staff_')
    AbsenceRequestSendTo: Mapped[List['AbsenceRequestSendTo']] = relationship('AbsenceRequestSendTo', back_populates='Staff_')


class StaffAcademicLevel(Base):
    __tablename__ = 'StaffAcademicLevel'
    __table_args__ = (
        Index('IX_StaffAcademicLevel_StaffId', 'StaffId'),
    )

    StaffAcademicLevelId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    DegreeId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IsDeleted: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    SchoolName: Mapped[Optional[str]] = mapped_column(String(128, 'utf8mb4_unicode_ci'))
    Majors: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'))
    FromDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ToDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))


class StaffAnnualLeave(Base):
    __tablename__ = 'StaffAnnualLeave'

    YearNumber: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    StaffId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    Total: Mapped[decimal.Decimal] = mapped_column(Double(asdecimal=True), server_default=text("'0'"))
    Pending: Mapped[decimal.Decimal] = mapped_column(Double(asdecimal=True), server_default=text("'0'"))
    Available: Mapped[decimal.Decimal] = mapped_column(Double(asdecimal=True), server_default=text("'0'"))
    AnnualYear: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(8, 2))
    LockedAnnualYear: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(8, 2))
    ByRank: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(8, 2))
    LockedByRank: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(8, 2))
    ToSeniority: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(8, 2))
    Training: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(8, 2))
    IsPaidTraining: Mapped[Optional[int]] = mapped_column(TINYINT(4))
    ApprovedNumber: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    WaitingNumberInMonth: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)


class StaffAnnualLeaveTransaction(Base):
    __tablename__ = 'StaffAnnualLeaveTransaction'

    Id: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    AbsenceTypeId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    AbsenceRequestId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Quantity: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    TransactionType: Mapped[Optional[str]] = mapped_column(String(20, 'utf8mb4_unicode_ci'), comment='100 import\n101 Deposit Monthly')
    TransactionDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    Note: Mapped[Optional[str]] = mapped_column(String(128, 'utf8mb4_unicode_ci'))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class StaffDocument(Base):
    __tablename__ = 'StaffDocument'

    StaffDocumentId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    DocumentType: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='1) PersonalIncomeTax')
    Name: Mapped[Optional[str]] = mapped_column(String(2024, 'utf8mb4_unicode_ci'))
    CDNURL: Mapped[Optional[str]] = mapped_column(String(2048, 'utf8mb4_unicode_ci'))
    Priority: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    State: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class StaffEmail(Base):
    __tablename__ = 'StaffEmail'
    __table_args__ = (
        Index('fk_StaffEmail_Staff_idx', 'StaffId'),
    )

    StaffEmailId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    Email_: Mapped[str] = mapped_column('Email', VARCHAR(64))
    IsWorkMail: Mapped[int] = mapped_column(INTEGER(1))
    StaffId: Mapped[int] = mapped_column(INTEGER(10))
    IsBackupEmail: Mapped[Optional[int]] = mapped_column(INTEGER(1), server_default=text("'0'"))


class StaffEvaluation(Base):
    __tablename__ = 'StaffEvaluation'

    StaffEvaluationId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    WorkProfileId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    StaffEvaluationContent: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_unicode_ci'), comment='DataJon:"{CreatedBy:\'1\',CreatedDate=\'2024-01-12 23:58:14\', \'Content\':\'\'}')
    ManagerEvaluationContent: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_unicode_ci'), comment='DataJon:"{CreatedBy:\'1\',CreatedDate=\'2024-01-12 23:58:14\', \'Content\':\'\'}')
    IsPass: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='1/0 : đạt/ không đạt')
    IsSign: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='1/0 : ký/ không ký')
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class StaffGroup(Base):
    __tablename__ = 'StaffGroup'
    __table_args__ = (
        Index('fk_StaffGroup_Company_idx', 'CompanyId'),
        Index('fk_StaffGroup_Parent_idx', 'ParentId'),
        Index('fk_StaffGroup_Root_idx', 'RootId'),
        {'comment': 'gom c?m các nhóm ng??i dùng theo tính n?ng thao tác h? th?ng. Ví '
                'd?: bác s?, l? tân, nhân viên tuy?n d?ng, nhân viên nhân s?...'}
    )

    StaffGroupId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    CompanyId: Mapped[int] = mapped_column(INTEGER(10))
    NameVi: Mapped[str] = mapped_column(VARCHAR(32))
    NameEn: Mapped[str] = mapped_column(VARCHAR(32))
    RootId: Mapped[int] = mapped_column(INTEGER(10))
    ParentId: Mapped[int] = mapped_column(INTEGER(10))
    Lft: Mapped[int] = mapped_column(INTEGER(10))
    Rgt: Mapped[int] = mapped_column(INTEGER(10))
    Level: Mapped[int] = mapped_column(INTEGER(10))
    Ordering: Mapped[Optional[int]] = mapped_column(INTEGER(10), server_default=text("'0'"))


t_StaffHistory = Table(
    'StaffHistory', Base.metadata,
    Column('StaffId', INTEGER(10), nullable=False),
    Column('StaffCode', VARCHAR(16), nullable=False),
    Column('IdNumber', VARCHAR(16)),
    Column('IdNumberIssuedAt', Date),
    Column('IdNumberIssuedBy', INTEGER(11)),
    Column('PassportNumber', VARCHAR(16)),
    Column('NationalInsuranceNumber', VARCHAR(16)),
    Column('TaxNumber', VARCHAR(16)),
    Column('UserId', INTEGER(10)),
    Column('FullName', VARCHAR(64)),
    Column('FullNameNoSign', VARCHAR(64)),
    Column('LastName', VARCHAR(16)),
    Column('LastNameNoSign', VARCHAR(16)),
    Column('DateOfBirth', Date),
    Column('Photo', VARCHAR(128)),
    Column('PrimaryEmail', VARCHAR(255)),
    Column('CreatedAt', INTEGER(10), nullable=False),
    Column('CreatedBy', INTEGER(10), nullable=False),
    Column('State', INTEGER(1), nullable=False, server_default=text("'1'")),
    Column('GenderId', INTEGER(10), nullable=False),
    Column('DegreeId', INTEGER(10)),
    Column('UpdatedAt', INTEGER(10)),
    Column('UpdatedBy', INTEGER(10)),
    Column('Nationality', INTEGER(10)),
    Column('FlushedAt', INTEGER(11), nullable=False)
)


class StaffIdentityPaper(Base):
    __tablename__ = 'StaffIdentityPaper'
    __table_args__ = (
        Index('IX_StaffIdentityPaper_StaffId', 'StaffId'),
    )

    StaffIdentityPaperId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Type: Mapped[Optional[int]] = mapped_column(SMALLINT(6), comment='1: CMND, 2: CCCD, 3: Passport')
    Code: Mapped[Optional[str]] = mapped_column(String(20, 'utf8mb4_unicode_ci'))
    IssuedDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    IssuedBy: Mapped[Optional[str]] = mapped_column(String(128, 'utf8mb4_unicode_ci'))
    IsOld: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='used UserId')
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='used UserId')


class StaffInterview(Base):
    __tablename__ = 'StaffInterview'
    __table_args__ = (
        Index('IX_CandidateId', 'CandidateId'),
        Index('IX_InterviewDate', 'InterviewDate')
    )

    StaffInterviewId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    InterviewDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Ngày ph?ng v?n')
    CandidateId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    InterviewerId: Mapped[Optional[int]] = mapped_column(INTEGER(10), comment='Ng??i ph?ng v?n chính - StaffId')
    InterviewerBoard: Mapped[Optional[str]] = mapped_column(VARCHAR(1000), comment='Ng??i ph?ng v?n - ?ng viên')
    WorkProfilePositionId: Mapped[Optional[int]] = mapped_column(INTEGER(10), comment='V? trí công vi?c')
    CompanyId: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='Công ty')
    BranchId: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='Chi nhánh')
    DepartmentId: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='Phòng ban')
    TeamId: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='B? ph?n')
    StaffLevelId: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='C?p b?c')
    Status: Mapped[Optional[int]] = mapped_column(TINYINT(2), comment='Tr?ng thái - 1: M?i, 2: ?ã h?y, 3: ??t, 4: Không ??t')
    StatusNote: Mapped[Optional[str]] = mapped_column(VARCHAR(1000), comment='Ghi chú tr?ng thái')
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)


class StaffInterviewType(Base):
    __tablename__ = 'StaffInterviewType'
    __table_args__ = (
        Index('IX_StaffInterviewId', 'StaffInterviewId'),
    )

    StaffInterviewTypeId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    StaffInterviewId: Mapped[int] = mapped_column(INTEGER(10))
    InterviewType: Mapped[Optional[int]] = mapped_column(TINYINT(1), comment='Hình th?c ph?ng v?n - 1: Online, 2: T?i NKK, 3: Ngoài NKK')
    InterviewPlace: Mapped[Optional[str]] = mapped_column(VARCHAR(1000), comment='??a ?i?m / link ph?ng v?n, N?u InterviewType = 2 l?u OrgId')


t_StaffLanguage = Table(
    'StaffLanguage', Base.metadata,
    Column('LanguageId', INTEGER(10), nullable=False),
    Column('StaffId', INTEGER(10), nullable=False),
    Column('LanguageLevelId', INTEGER(10), nullable=False),
    Column('UpdatedAt', INTEGER(10), nullable=False),
    Index('fk_StaffLanguage_LanguageLevel_idx', 'LanguageLevelId'),
    Index('fk_StaffLanguage_Language_idx', 'LanguageId'),
    Index('fk_StaffLanguage_Staff_idx', 'StaffId')
)


t_StaffLeave = Table(
    'StaffLeave', Base.metadata,
    Column('StaffId', INTEGER(11), nullable=False),
    Column('YearNumber', SMALLINT(6), nullable=False),
    Column('TotalLeave', DECIMAL(5, 1), server_default=text("'0.0'"), comment='Tổng số ngày phép'),
    Column('AvailableTotalLeave', DECIMAL(5, 1), server_default=text("'0.0'"), comment='Tổng số ngày phép khả dụng'),
    Column('PendingTotalLeave', DECIMAL(5, 1), server_default=text("'0.0'"), comment='Tổng số ngày phép đang chờ duyệt'),
    Column('AnnualLeave', DECIMAL(5, 1), server_default=text("'0.0'"), comment='Tổng số ngày phép năm'),
    Column('AvailableAnnualLeave', DECIMAL(5, 1), server_default=text("'0.0'"), comment='Tổng số ngày phép năm khả dụng'),
    Column('PendingAnnualLeave', DECIMAL(5, 1), server_default=text("'0.0'"), comment='Tổng số ngày phép năm đang chờ duyệt'),
    Column('LastAnnualLeave', DECIMAL(5, 1), server_default=text("'0.0'"), comment='Tổng số ngày phép năm (tồn năm cũ)'),
    Column('AvailableLastAnnualLeave', DECIMAL(5, 1), server_default=text("'0.0'"), comment='Tổng số ngày phép năm (tồn năm cũ) khả dụng'),
    Column('PendingLastAnnualLeave', DECIMAL(5, 1), server_default=text("'0.0'"), comment='Tổng số ngày phép năm (tồn năm cũ) đang chờ duyệt'),
    Column('SeniorityLeave', DECIMAL(5, 1), server_default=text("'0.0'"), comment='Tổng số ngày phép thâm niên'),
    Column('AvailableSeniorityLeave', DECIMAL(5, 1), server_default=text("'0.0'"), comment='Tổng số ngày phép thâm niên khả dụng'),
    Column('PendingSeniorityLeave', DECIMAL(5, 1), server_default=text("'0.0'"), comment='Tổng số ngày phép thâm niên đang chờ duyệt'),
    Column('RankLeave', DECIMAL(5, 1), server_default=text("'0.0'"), comment='Tổng số ngày phép cấp bậc'),
    Column('AvailableRankLeave', DECIMAL(5, 1), server_default=text("'0.0'"), comment='Tổng số ngày phép cấp bậc khả dụng'),
    Column('PendingRankLeave', DECIMAL(5, 1), server_default=text("'0.0'"), comment='Tổng số ngày phép cấp bậc đang chờ duyệt'),
    Column('TrainingLeave', DECIMAL(5, 1), server_default=text("'0.0'"), comment='Tổng số ngày phép đào tạo'),
    Column('AvailableTrainingLeave', DECIMAL(5, 1), server_default=text("'0.0'"), comment='Tổng số ngày phép đào tạo khả dụng'),
    Column('PendingTrainingLeave', DECIMAL(5, 1), server_default=text("'0.0'"), comment='Tổng số ngày phép đào tạo đang chờ duyệt'),
    Column('UsedUnpaidLeave', DECIMAL(5, 1), server_default=text("'0.0'"), comment='Tổng số ngày phép không hưởng lương đã dùng'),
    Column('PendingUnpaidLeave', DECIMAL(5, 1), server_default=text("'0.0'"), comment='Tổng số ngày phép không hưởng lương đang chờ duyệt'),
    Column('UsedSickLeave', DECIMAL(5, 1), server_default=text("'0.0'"), comment='Tổng số ngày phép ốm/bệnh đã dùng'),
    Column('PendingSickLeave', DECIMAL(5, 1), server_default=text("'0.0'"), comment='Tổng số ngày phép ốm/bệnh đang chờ duyệt'),
    Column('UsedMarriageLeave', DECIMAL(5, 1), server_default=text("'0.0'"), comment='Tổng số ngày phép hiếu hỉ (kết hôn) đã dùng'),
    Column('PendingMarriageLeave', DECIMAL(5, 1), server_default=text("'0.0'"), comment='Tổng số ngày phép hiếu hỉ (kết hôn) đang chờ duyệt'),
    Column('UsedCompassionateLeave', DECIMAL(5, 1), server_default=text("'0.0'"), comment='Tổng số ngày phép tang gia/tang chế đã dùng'),
    Column('PendingCompassionateLeave', DECIMAL(5, 1), server_default=text("'0.0'"), comment='Tổng số ngày phép tang gia/tang chế đang chờ duyệt'),
    Column('UsedMaternityLeave', DECIMAL(5, 1), server_default=text("'0.0'"), comment='Tổng số ngày phép vì thai sản đã dùng'),
    Column('PendingMaternityLeave', DECIMAL(5, 1), server_default=text("'0.0'"), comment='Tổng số ngày phép vì thai sản đang chờ duyệt'),
    Column('LastTotalLeave', DECIMAL(5, 1), server_default=text("'0.0'"), comment='Tổng số ngày phép tồn năm cũ'),
    Column('LastAvailableTotalLeave', DECIMAL(5, 1), server_default=text("'0.0'"), comment='Tổng số ngày phép tồn năm cũ khả dụng'),
    Index('uid_StaffLeaveDays', 'StaffId', 'YearNumber', unique=True)
)


class StaffLeaveTransaction(Base):
    __tablename__ = 'StaffLeaveTransaction'
    __table_args__ = (
        Index('idx_StaffId', 'StaffId', 'CreatedDate'),
    )

    StaffLeaveTransactionId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TransactionDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    TransactionTypeId: Mapped[Optional[int]] = mapped_column(TINYINT(4), comment='1: deposit, 2: withdrawal')
    AbsenceTypeId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    AbsenceRequestId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    LeaveDays: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 1))
    Note: Mapped[Optional[str]] = mapped_column(String(2000, 'utf8mb4_unicode_ci'))
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))


class StaffLevel(Base):
    __tablename__ = 'StaffLevel'

    StaffLevelId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    StaffLevelGroupId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Name: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))
    Ordering: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    State: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class StaffLevelGroup(Base):
    __tablename__ = 'StaffLevelGroup'
    __table_args__ = (
        Index('fk_StaffLevel_Company_idx', 'CompanyId'),
    )

    StaffLevelGroupId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    Name: Mapped[str] = mapped_column(VARCHAR(64))
    Ordering: Mapped[int] = mapped_column(INTEGER(11), server_default=text("'0'"))
    State: Mapped[int] = mapped_column(INTEGER(1), server_default=text("'1'"))
    CompanyId: Mapped[int] = mapped_column(INTEGER(10))
    BaseSalary: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(20, 2))
    NameVI: Mapped[Optional[str]] = mapped_column(String(256, 'utf8mb4_unicode_ci'))
    AnnualLeavePerYear: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))


class StaffModifyTracking(Base):
    __tablename__ = 'StaffModifyTracking'
    __table_args__ = (
        Index('idx_StaffId', 'StaffId'),
    )

    StaffModifyTrackingId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    AbsenceRequestId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    ModifyType: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='1) Th?i gian nghi viec\n2) Thai S?n\n')
    Note: Mapped[Optional[str]] = mapped_column(String(2000, 'utf8mb4_unicode_ci'))
    OldJsonData: Mapped[Optional[str]] = mapped_column(String(4000, 'utf8mb4_unicode_ci'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)


class StaffNationality(Base):
    __tablename__ = 'StaffNationality'

    StaffNationalityId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CountryId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IsActive: Mapped[Optional[Any]] = mapped_column(BIT(1))
    Priority: Mapped[Optional[int]] = mapped_column(SMALLINT(6))


class StaffPasswordTracking(Base):
    __tablename__ = 'StaffPasswordTracking'
    __table_args__ = (
        Index('IX_StaffId', 'StaffId'),
    )

    StaffPasswordTrackingId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    ChangedType: Mapped[Optional[int]] = mapped_column(TINYINT(2), comment='1: T? ??i m?t kh?u, 2: Nhân s? ??i m?t kh?u, 3: Quên m?t kh?u')
    ChangedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    ChangedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class StaffPhone(Base):
    __tablename__ = 'StaffPhone'
    __table_args__ = (
        Index('fk_StaffPhone_Staff_idx', 'StaffId'),
        Index('idx_PhoneNumber', 'PhoneNumber')
    )

    StaffPhoneId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    PhoneNumber: Mapped[str] = mapped_column(VARCHAR(16))
    IsPrimary: Mapped[int] = mapped_column(INTEGER(1))
    StaffId: Mapped[int] = mapped_column(INTEGER(10))
    Label: Mapped[Optional[str]] = mapped_column(VARCHAR(16), server_default=text("'Work'"))


class StaffProbationaryEvaluation(Base):
    __tablename__ = 'StaffProbationaryEvaluation'

    StaffProbationaryEvaluationId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Content: Mapped[Optional[str]] = mapped_column(String(8000, 'utf8mb4_unicode_ci'))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class StaffPublicAssetTracking(Base):
    __tablename__ = 'StaffPublicAssetTracking'

    StaffPublicAssetTrackingId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    ActionName: Mapped[str] = mapped_column(String(250, 'utf8mb4_unicode_ci'), server_default=text("'Create'"))
    StaffPublicAssetId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    BranchId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Note: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_unicode_ci'), comment='Ghi chú')
    PublicAssetId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    DeviceSerialNumber: Mapped[Optional[str]] = mapped_column(String(250, 'utf8mb4_unicode_ci'))
    DeviceCode: Mapped[Optional[str]] = mapped_column(String(250, 'utf8mb4_unicode_ci'))
    DeviceName: Mapped[Optional[str]] = mapped_column(String(250, 'utf8mb4_unicode_ci'))
    IssueDate: Mapped[Optional[datetime.date]] = mapped_column(Date, comment='Ngày cấp thiết bị')
    RetrievalDate: Mapped[Optional[datetime.date]] = mapped_column(Date, comment='Ngày thu hồi thiết bị')
    State: Mapped[Optional[int]] = mapped_column(INTEGER(1), server_default=text("'1'"), comment='Trạng thái: 1 - Đang sử dụng, 2 - Thu hồi')
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)


class StaffResignationRequest(Base):
    __tablename__ = 'StaffResignationRequest'
    __table_args__ = (
        Index('idx_StaffId', 'StaffId'),
    )

    StaffResignationRequestId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    LastestWorkingDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ApprovedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    ApprovedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    Status: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='1: New\n2:Approved\n3:Cancel')
    Reason_: Mapped[Optional[str]] = mapped_column('Reason', Text(collation='utf8mb4_unicode_ci'))
    ReasonNote: Mapped[Optional[str]] = mapped_column(String(1024, 'utf8mb4_unicode_ci'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    Completed: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))


class StaffSalaryDetails(Base):
    __tablename__ = 'StaffSalaryDetails'

    StaffSalaryDetailsId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    StaffCode: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'))
    FullName: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='họ tên')
    Company_: Mapped[Optional[str]] = mapped_column('Company', String(50, 'utf8mb4_unicode_ci'), comment='Công ty')
    WorkProfilePosition: Mapped[Optional[str]] = mapped_column(String(100, 'utf8mb4_unicode_ci'), comment='Chức danh')
    ContractType: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='Loại hợp đồng')
    Branch: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='Chi nhánh')
    StartDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='ngày vào làm')
    Shift: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='ca làm việc')
    Level: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='bậc')
    SalaryPerHour_: Mapped[Optional[decimal.Decimal]] = mapped_column('SalaryPerHour', DECIMAL(7, 2), server_default=text("'0.00'"), comment='đơn giá giờ')
    ActualHoursWorked: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 2), server_default=text("'0.00'"), comment='số giờ lv thực tế HIS')
    AnnualLeave: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 2), server_default=text("'0.00'"), comment='nghỉ phép')
    PaidLeave: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 2), server_default=text("'0.00'"), comment='nghỉ chế độ')
    PublicHolidaysLeave: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 2), server_default=text("'0.00'"), comment='nghỉ lễ/tết')
    TotalStandardHours: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 2), server_default=text("'0.00'"), comment='tổng công tính lương')
    StandardWage: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 2), server_default=text("'0.00'"), comment='công chuẩn')
    TotalIncomeWorkingDays: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='Thành tiền lương theo công chuẩn')
    TaskBonus1: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(15, 3), server_default=text("'0.000'"), comment='Thưởng công việc')
    ServiceQualityBonus1: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='Thưởng CLDV')
    GeneralManagermentBonus1: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='Thưởng quản lý chung')
    EfficiencyManagementBonus: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='Thưởng hiệu quả quản lý')
    EbitdaBonus: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='Thưởng Ebitda')
    OtherBonus: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='thưởng khác nếu có')
    SecurityBonus: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='thưởng an ninh')
    PerformanceBonus: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='Thưởng năng suất')
    TaskBonus2: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(15, 3), server_default=text("'0.000'"), comment='Thưởng công việc')
    ServiceQualityBonus2: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='Thưởng CLDV')
    GeneralManagermentBonus2: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='Thưởng quản lý chung')
    KPIBonus: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(15, 3), server_default=text("'0.000'"), comment='Thưởng KPI')
    VinmecBonus: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='thưởng vinmec')
    DoctorBonus: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(15, 3), server_default=text("'0.000'"), comment='Thưởng bác sĩ')
    OtherBonus3_vinmec_: Mapped[Optional[decimal.Decimal]] = mapped_column('OtherBonus3(vinmec)', DECIMAL(13, 3), server_default=text("'0.000'"), comment='Thưởng khác (vinmec)')
    HolidayBonus: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='thưởng lễ/tết')
    TotalBonus: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), server_default=text("'0.00'"), comment='tổng thưởng')
    AssistantManagerAndConcurrentBonus: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(15, 3), server_default=text("'0.000'"), comment='PC Phụ tá trưởng và kiêm nhiệm')
    GuaranteedIncomeAllowance: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(15, 3), server_default=text("'0.000'"), comment='Phụ cấp đảm bảo thu nhập')
    ParkingTravelAllowance: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='PC gửi xe/công tác')
    ProfessionalCertificateAllowance: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='Phụ cấp chứng chỉ hành nghề')
    OtherAllowances: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='phụ cấp khác')
    DentalTour: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(15, 3), server_default=text("'0.000'"))
    WarehouseAllowance: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(15, 3), server_default=text("'0.000'"), comment='Phụ cấp kho')
    OtherTotalIncome: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(15, 3), server_default=text("'0.000'"), comment='Tổng thu nhập khác')
    OtherAddition: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='cộng khác')
    OtherDeductions: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='trừ khác')
    TotalIncomeBeforeTax: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='tổng thu nhập trước thuế')
    ParticipatingSalaryInSocialInsurance: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='Mức lương tham gia BHXH')
    PersonalHealthInsurance: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='BHYT 1,5%')
    PersonalSocialInsurance: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='BHXH 8%')
    PersonalUnemploymentInsurance: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='BHTN 1%')
    EmployeeSocialInsurance: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='NLD đóng BHXH 10,5%')
    EmployeeUnionFee: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='NLĐ đóng phí công đoàn 1%')
    CompanySocialInsurance: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='BHXH 17%')
    CompanyOccupaitionalAccidentOrDisease: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='TNLĐ / BNN 0.5%')
    CompanyHealthInsurance: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='BHYT 3%')
    CompanyUnemploymentInsurance: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='BHTN 1%')
    EnterpriseSocialInsurance: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='doanh nghiệp đóng BHXH 21.5%')
    EnterpriseUnionFee: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='Doanh nghiệp đóng công đoàn 2%')
    LunchOrUniformAllowanceNoTax: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='Không tính thuế ( phụ cấp cơm trưa/ Đồng phục)')
    TotalTaxableIncome: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='Tổng thu nhập chịu thuế')
    TaxableIncomeObject: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='Đối tượng tính thuế TNCN')
    Commitment: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='Cam kết')
    Dependents: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"), comment='Số người phụ thuộc')
    TotalAssessableIncome: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='Tổng thu nhập tính thuế')
    PersonalIncomeTaxCollection: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='Thu tiền thuế TNCN')
    ActualPayment: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), server_default=text("'0.00'"), comment='Thực lãnh')
    CompanyPaysSocialInsurance: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='Cty đóng họ BHXH')
    WithholdSocialInsurance: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='thu hộ tiền BHXH 21.5%')
    PaidHolidayBonus: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(11, 2), server_default=text("'0.00'"), comment='Đã thanh toán thưởng Lễ/tết\\n')
    PaidOthers: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(11, 2), server_default=text("'0.00'"), comment='Đã thanh toán khác\\n')
    BankTransfer: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), server_default=text("'0.00'"), comment='chuyển khoản')
    NoteOtherAdditions: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='Ghi chú cột cộng khác\\n')
    PayPeriod: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='kỳ lương')
    Template: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='1-BO\\\\n2-Phu ta\\\\n3-Bac Si\\\\n4-Bao ve')


class StaffSalaryDetailsTracking(Base):
    __tablename__ = 'StaffSalaryDetailsTracking'

    StaffSalaryDetailsTrackingId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TotalImport: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    TotalSucceed: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    TotalError: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    FilePath: Mapped[Optional[str]] = mapped_column(String(250, 'utf8mb4_unicode_ci'))
    ExportPath: Mapped[Optional[str]] = mapped_column(String(250, 'utf8mb4_unicode_ci'))
    PayPeriod: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


t_StaffSalaryDetails_backup = Table(
    'StaffSalaryDetails_backup', Base.metadata,
    Column('StaffSalaryDetailsId', INTEGER(11), nullable=False, server_default=text("'0'")),
    Column('StaffId', INTEGER(11)),
    Column('StaffCode', String(50, 'utf8mb4_unicode_ci')),
    Column('FullName', String(50, 'utf8mb4_unicode_ci'), comment='họ tên'),
    Column('Company', String(50, 'utf8mb4_unicode_ci'), comment='Công ty'),
    Column('WorkProfilePosition', String(100, 'utf8mb4_unicode_ci'), comment='Chức danh'),
    Column('ContractType', String(50, 'utf8mb4_unicode_ci'), comment='Loại hợp đồng'),
    Column('Branch', String(50, 'utf8mb4_unicode_ci'), comment='Chi nhánh'),
    Column('StartDate', DateTime),
    Column('Shift', String(50, 'utf8mb4_unicode_ci'), comment='ca làm việc'),
    Column('Total', DECIMAL(13, 3), server_default=text("'0.000'"), comment='Tổng cộng'),
    Column('NoTimekeeping', String(50, 'utf8mb4_unicode_ci'), comment='ko chấm công'),
    Column('Level', String(50, 'utf8mb4_unicode_ci'), comment='bậc'),
    Column('SalaryPerHour', DECIMAL(7, 2), server_default=text("'0.00'"), comment='đơn giá giờ'),
    Column('ActualHoursWorked', DECIMAL(5, 2), server_default=text("'0.00'"), comment='số giờ lv thực tế HIS'),
    Column('AnnualLeave', DECIMAL(5, 2), server_default=text("'0.00'"), comment='nghỉ phép'),
    Column('CompensatoryLeave', DECIMAL(7, 2), server_default=text("'0.00'"), comment='nghỉ bù'),
    Column('PaidLeave', DECIMAL(5, 2), server_default=text("'0.00'"), comment='nghỉ chế độ'),
    Column('PublicHolidaysLeave', DECIMAL(5, 2), server_default=text("'0.00'"), comment='nghỉ lễ/tết'),
    Column('TotalHour', DECIMAL(5, 2), server_default=text("'0.00'"), comment='Tổng công'),
    Column('TotalStandardHours', DECIMAL(5, 2), server_default=text("'0.00'"), comment='tổng công tính lương'),
    Column('StandardWage', DECIMAL(5, 2), server_default=text("'0.00'"), comment='công chuẩn'),
    Column('BasicSalary', DECIMAL(13, 3), server_default=text("'0.000'"), comment='lương cơ bản'),
    Column('PerformanceBonus', DECIMAL(13, 3), server_default=text("'0.000'"), comment='Thưởng Ý thức và Tuân thủ/Thưởng Hiệụ quả hoạt động'),
    Column('LunchAllowance', DECIMAL(13, 3), server_default=text("'0.000'"), comment='Phụ cấp cơm trưa'),
    Column('UniformAllowance', DECIMAL(13, 3), server_default=text("'0.000'"), comment='Phụ cấp đồng phục'),
    Column('TotalLunchAllowance', DECIMAL(10, 2), server_default=text("'0.00'"), comment='Thành tiền PC cơm theo công'),
    Column('FixedIncomeWithLunchAllowance', DECIMAL(15, 3), server_default=text("'0.000'"), comment='định mức thu nhập cố định (đã  bao gồm Pc cơm)'),
    Column('FixedIncomeAmountWithLunchAllowance', DECIMAL(15, 3), server_default=text("'0.000'"), comment='Thành tiền thu nhập cố định theo công chuẩn (đã bao gồm PC cơm)'),
    Column('TotalIncomeWorkingDays', DECIMAL(13, 3), server_default=text("'0.000'"), comment='Tổng thu nhập theo ngày công'),
    Column('CRM/CSBonus', DECIMAL(13, 3), server_default=text("'0.000'"), comment='Thưởng CRM/CS (C.Mai)'),
    Column('DoctorBonus', DECIMAL(15, 3), server_default=text("'0.000'"), comment='Thưởng bác sĩ'),
    Column('TaskBonus', DECIMAL(15, 3), server_default=text("'0.000'"), comment='Thưởng công việc'),
    Column('ServiceQualityBonus', DECIMAL(13, 3), server_default=text("'0.000'"), comment='Thưởng CLDV'),
    Column('GeneralManagermentBonus', DECIMAL(13, 3), server_default=text("'0.000'"), comment='Thưởng quản lý chung'),
    Column('EfficiencyManagementBonus', DECIMAL(13, 3), server_default=text("'0.000'"), comment='Thưởng hiệu quả quản lý'),
    Column('ClinicsAchievingKPIRevenueBonus', DECIMAL(15, 3), server_default=text("'0.000'"), comment='Thưởng phòng khám đạt KPI thu tiền'),
    Column('EbitdaBonus', DECIMAL(13, 3), server_default=text("'0.000'"), comment='Thưởng Ebitda'),
    Column('VinmecBonus', DECIMAL(13, 3), server_default=text("'0.000'"), comment='thưởng vinmec'),
    Column('SecurityBonus', DECIMAL(13, 3), server_default=text("'0.000'"), comment='thưởng an ninh'),
    Column('HolidayBonus', DECIMAL(13, 3), server_default=text("'0.000'"), comment='thưởng lễ/tết'),
    Column('TotalBonus', DECIMAL(12, 2), server_default=text("'0.00'"), comment='tổng thưởng'),
    Column('AssistantManagerAndConcurrentBonus', DECIMAL(15, 3), server_default=text("'0.000'"), comment='PC Phụ tá trưởng và kiêm nhiệm'),
    Column('GuaranteedIncomeAllowance', DECIMAL(15, 3), server_default=text("'0.000'"), comment='Phụ cấp đảm bảo thu nhập'),
    Column('ParkingTravelAllowance', DECIMAL(13, 3), server_default=text("'0.000'"), comment='PC gửi xe/công tác'),
    Column('ProfessionalCertificateAllowance', DECIMAL(13, 3), server_default=text("'0.000'"), comment='Phụ cấp chứng chỉ hành nghề'),
    Column('OtherAllowances', DECIMAL(13, 3), server_default=text("'0.000'"), comment='phụ cấp khác'),
    Column('DentalTour', DECIMAL(15, 3), server_default=text("'0.000'")),
    Column('WarehouseAllowance', DECIMAL(15, 3), server_default=text("'0.000'"), comment='Phụ cấp kho'),
    Column('TotalAllowances', DECIMAL(13, 3), comment='Tổng phụ cấp'),
    Column('OtherTotalIncome', DECIMAL(15, 3), server_default=text("'0.000'"), comment='Tổng thu nhập khác'),
    Column('OtherAddition', DECIMAL(13, 3), server_default=text("'0.000'"), comment='cộng khác'),
    Column('OtherDeductions', DECIMAL(13, 3), server_default=text("'0.000'"), comment='trừ khác'),
    Column('TotalIncomeBeforeTax', DECIMAL(13, 3), server_default=text("'0.000'"), comment='tổng thu nhập trước thuế'),
    Column('ParticipatingSalaryInSocialInsurance', DECIMAL(13, 3), server_default=text("'0.000'"), comment='Mức lương tham gia BHXH'),
    Column('PersonalHealthInsurance', DECIMAL(13, 3), server_default=text("'0.000'"), comment='BHYT 1,5%'),
    Column('PersonalSocialInsurance', DECIMAL(13, 3), server_default=text("'0.000'"), comment='BHXH 8%'),
    Column('PersonalUnemploymentInsurance', DECIMAL(13, 3), server_default=text("'0.000'"), comment='BHTN 1%'),
    Column('EmployeeSocialInsurance', DECIMAL(13, 3), server_default=text("'0.000'"), comment='NLD đóng BHXH 10,5%'),
    Column('EmployeeUnionFee', DECIMAL(13, 3), server_default=text("'0.000'"), comment='NLĐ đóng phí công đoàn 1%'),
    Column('CompanySocialInsurance', DECIMAL(13, 3), server_default=text("'0.000'"), comment='BHXH 17%'),
    Column('CompanyOccupaitionalAccidentOrDisease', DECIMAL(13, 3), server_default=text("'0.000'"), comment='TNLĐ / BNN 0.5%'),
    Column('CompanyHealthInsurance', DECIMAL(13, 3), server_default=text("'0.000'"), comment='BHYT 3%'),
    Column('CompanyUnemploymentInsurance', DECIMAL(13, 3), server_default=text("'0.000'"), comment='BHTN 1%'),
    Column('EnterpriseSocialInsurance', DECIMAL(13, 3), server_default=text("'0.000'"), comment='doanh nghiệp đóng BHXH 21.5%'),
    Column('EnterpriseUnionFee', DECIMAL(13, 3), server_default=text("'0.000'"), comment='Doanh nghiệp đóng công đoàn 2%'),
    Column('LunchOrUniformAllowanceNoTax', DECIMAL(13, 3), server_default=text("'0.000'"), comment='Không tính thuế ( phụ cấp cơm trưa/ Đồng phục)'),
    Column('TotalTaxableIncome', DECIMAL(13, 3), server_default=text("'0.000'"), comment='Tổng thu nhập chịu thuế'),
    Column('TaxableIncomeObject', String(50, 'utf8mb4_unicode_ci'), comment='Đối tượng tính thuế TNCN'),
    Column('Commitment', String(50, 'utf8mb4_unicode_ci'), comment='Cam kết'),
    Column('Dependents', INTEGER(11), server_default=text("'0'"), comment='Số người phụ thuộc'),
    Column('TotalAssessableIncome', DECIMAL(13, 3), server_default=text("'0.000'"), comment='Tổng thu nhập tính thuế'),
    Column('PersonalIncomeTaxCollection', DECIMAL(13, 3), server_default=text("'0.000'"), comment='Thu tiền thuế TNCN'),
    Column('ActualPayment', DECIMAL(12, 2), server_default=text("'0.00'"), comment='Thực lãnh'),
    Column('CompanyPaysSocialInsurance', DECIMAL(13, 3), server_default=text("'0.000'"), comment='Cty đóng họ BHXH'),
    Column('WithholdSocialInsurance', DECIMAL(13, 3), server_default=text("'0.000'"), comment='thu hộ tiền BHXH 21.5%'),
    Column('PaidHolidayBonus', DECIMAL(11, 2), server_default=text("'0.00'"), comment='Đã thanh toán thưởng Lễ/tết\\n'),
    Column('PaidOthers', DECIMAL(11, 2), server_default=text("'0.00'"), comment='Đã thanh toán khác\\n'),
    Column('BankTransfer', DECIMAL(12, 2), server_default=text("'0.00'"), comment='chuyển khoản'),
    Column('NoteOtherAdditions', String(50, 'utf8mb4_unicode_ci'), comment='Ghi chú cột cộng khác\\n'),
    Column('Name', String(50, 'utf8mb4_unicode_ci'), comment='Tên tài khoản'),
    Column('AccountNumber', String(255, 'utf8mb4_unicode_ci'), comment='số tài khoản'),
    Column('Bank', String(50, 'utf8mb4_unicode_ci'), comment='ngân hàng'),
    Column('Email', String(50, 'utf8mb4_unicode_ci'), comment='email'),
    Column('TransferAmount', DECIMAL(13, 2), comment='số tiền chuyển khoản'),
    Column('Additional', DECIMAL(13, 3), server_default=text("'0.000'"), comment='bổ sung'),
    Column('Notes', String(50, 'utf8mb4_unicode_ci'), comment='ghi chú/ lý do'),
    Column('PaymentDate', String(50, 'utf8mb4_unicode_ci'), comment='ngày thanh toán'),
    Column('PayPeriod', String(50, 'utf8mb4_unicode_ci'), comment='kỳ lương'),
    Column('Template', INTEGER(11), comment='1-BO\\n2-Phu ta\\n3-Bac Si\\n4-Bao ve')
)


class StaffSalaryDetailsBk(Base):
    __tablename__ = 'StaffSalaryDetails_bk'

    StaffSalaryDetailsId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    StaffCode: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'))
    FullName: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='họ tên')
    Company_: Mapped[Optional[str]] = mapped_column('Company', String(50, 'utf8mb4_unicode_ci'), comment='Công ty')
    WorkProfilePosition: Mapped[Optional[str]] = mapped_column(String(100, 'utf8mb4_unicode_ci'), comment='Chức danh')
    ContractType: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='Loại hợp đồng')
    Branch: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='Chi nhánh')
    StartDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    Shift: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='ca làm việc')
    Total: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='Tổng cộng')
    NoTimekeeping: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='ko chấm công')
    ActualHoursWorked: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='số giờ lv thực tế HIS')
    AnnualLeave: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='nghỉ phép')
    PaidLeave: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='nghỉ chế độ')
    PublicHolidaysLeave: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='nghỉ lễ/tết')
    TotalStandardHours: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(10, True), comment='tổng công tính lương')
    StandardWage: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='công chuẩn')
    BasicSalary: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='lương cơ bản')
    PerformanceBonus: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='Thưởng Ý thức và Tuân thủ/Thưởng Hiệụ quả hoạt động')
    LunchAllowance: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='Phụ cấp cơm trưa')
    UniformAllowance: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='Phụ cấp đồng phục')
    TotalIncomeWorkingDays: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='Tổng thu nhập theo ngày công')
    CRM_CSBonus: Mapped[Optional[str]] = mapped_column('CRM/CSBonus', String(50, 'utf8mb4_unicode_ci'), comment='Thưởng CRM/CS (C.Mai)')
    ServiceQualityBonus: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='Thưởng CLDV')
    GeneralManagermentBonus: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='Thưởng quản lý chung')
    EfficiencyManagementBonus: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='Thưởng hiệu quả quản lý')
    EbitdaBonus: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='Thưởng Ebitda')
    VinmecBonus: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='thưởng vinmec')
    SecurityBonus: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='thưởng an ninh')
    HolidayBonus: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='thưởng lễ/tết')
    TotalBonus: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='tổng thưởng')
    ParkingTravelAllowance: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='PC gửi xe/công tác')
    ProfessionalCertificateAllowance: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='Phụ cấp chứng chỉ hành nghề')
    OtherAllowances: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='phụ cấp khác')
    TotalAllowances: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='Tổng phụ cấp')
    OtherDeductions: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='trừ khác')
    TotalIncomeBeforeTax: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='tổng thu nhập trước thuế')
    ParticipatingSalaryInSocialInsurance: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='Mức lương tham gia BHXH')
    PersonalHealthInsurance: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='BHYT 1,5%')
    PersonalSocialInsurance: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='BHXH 8%')
    PersonalUnemploymentInsurance: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='BHTN 1%')
    EmployeeSocialInsurance: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='NLD đóng BHXH 10,5%')
    EmployeeUnionFee: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='NLĐ đóng phí công đoàn 1%')
    CompanySocialInsurance: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='BHXH 17%')
    CompanyOccupaitionalAccidentOrDisease: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='TNLĐ / BNN 0.5%')
    CompanyHealthInsurance: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='BHYT 3%')
    CompanyUnemploymentInsurance: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='BHTN 1%')
    EnterpriseSocialInsurance: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='doanh nghiệp đóng BHXH 21.5%')
    EnterpriseUnionFee: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='Doanh nghiệp đóng công đoàn 2%')
    LunchOrUniformAllowanceNoTax: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='Không tính thuế ( phụ cấp cơm trưa/ Đồng phục)')
    TotalTaxableIncome: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='Tổng thu nhập chịu thuế')
    TaxableIncomeObject: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='Đối tượng tính thuế TNCN')
    Commitment: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='Cam kết')
    Dependents: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='Số người phụ thuộc')
    TotalAssessableIncome: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='Tổng thu nhập tính thuế')
    PersonalIncomeTaxCollection: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='Thu tiền thuế TNCN')
    ActualPayment: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='Thực lãnh')
    CompanyPaysSocialInsurance: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='Cty đóng họ BHXH')
    WithholdSocialInsurance: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='thu hộ tiền BHXH 21.5%')
    BankTransfer: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='chuyển khoản')
    Name: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='Tên tài khoản')
    AccountNumber: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'), comment='số tài khoản')
    Bank_: Mapped[Optional[str]] = mapped_column('Bank', String(50, 'utf8mb4_unicode_ci'), comment='ngân hàng')
    Email_: Mapped[Optional[str]] = mapped_column('Email', String(50, 'utf8mb4_unicode_ci'), comment='email')
    TransferAmount: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 2), comment='số tiền chuyển khoản')
    Additional: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='bổ sung')
    Notes: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='ghi chú/ lý do')
    PaymentDate: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='ngày thanh toán')
    Level: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='bậc')
    SalaryPerHour_: Mapped[Optional[str]] = mapped_column('SalaryPerHour', String(50, 'utf8mb4_unicode_ci'), comment='đơn giá giờ')
    CompensatoryLeave: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='nghỉ bù')
    TotalLunchAllowance: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='Thành tiền PC cơm theo công')
    FixedIncomeWithLunchAllowance: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='định mức thu nhập cố định (đã  bao gồm Pc cơm)')
    FixedIncomeAmountWithLunchAllowance: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='Thành tiền thu nhập cố định theo công chuẩn (đã bao gồm PC cơm)')
    TaskBonus: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='Thưởng công việc')
    ClinicsAchievingKPIRevenueBonus: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='Thưởng phòng khám đạt KPI thu tiền')
    AssistantManagerAndConcurrentBonus: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='PC Phụ tá trưởng và kiêm nhiệm')
    GuaranteedIncomeAllowance: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='Phụ cấp đảm bảo thu nhập')
    DentalTour: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'))
    WarehouseAllowance: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='Phụ cấp kho')
    OtherTotalIncome: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='Tổng thu nhập khác')
    DoctorBonus: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='Thưởng bác sĩ')
    AdjustmentForDecemberShortfall: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='Cộng thiếu tháng 12')
    PayPeriod: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='kỳ lương')
    Template: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='1-BO\\n2-Phu ta\\n3-Bac Si\\n4-Bao ve')


class StaffSalaryDetailsT(Base):
    __tablename__ = 'StaffSalaryDetails_t'

    StaffSalaryDetailsId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    StaffCode: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'))
    FullName: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='họ tên')
    Company_: Mapped[Optional[str]] = mapped_column('Company', String(50, 'utf8mb4_unicode_ci'), comment='Công ty')
    WorkProfilePosition: Mapped[Optional[str]] = mapped_column(String(100, 'utf8mb4_unicode_ci'), comment='Chức danh')
    ContractType: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='Loại hợp đồng')
    Branch: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='Chi nhánh')
    StartDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='ngày vào làm')
    Shift: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='ca làm việc')
    Level: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='bậc')
    SalaryPerHour_: Mapped[Optional[decimal.Decimal]] = mapped_column('SalaryPerHour', DECIMAL(7, 2), server_default=text("'0.00'"), comment='đơn giá giờ')
    ActualHoursWorked: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 2), server_default=text("'0.00'"), comment='số giờ lv thực tế HIS')
    AnnualLeave: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 2), server_default=text("'0.00'"), comment='nghỉ phép')
    PaidLeave: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 2), server_default=text("'0.00'"), comment='nghỉ chế độ')
    PublicHolidaysLeave: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 2), server_default=text("'0.00'"), comment='nghỉ lễ/tết')
    TotalStandardHours: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 2), server_default=text("'0.00'"), comment='tổng công tính lương')
    StandardWage: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 2), server_default=text("'0.00'"), comment='công chuẩn')
    TotalIncomeWorkingDays: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='Thành tiền lương theo công chuẩn')
    TaskBonus1: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(15, 3), server_default=text("'0.000'"), comment='Thưởng công việc')
    ServiceQualityBonus1: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='Thưởng CLDV')
    GeneralManagermentBonus1: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='Thưởng quản lý chung')
    EfficiencyManagementBonus: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='Thưởng hiệu quả quản lý')
    EbitdaBonus: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='Thưởng Ebitda')
    OtherBonus: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='thưởng khác nếu có')
    SecurityBonus: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='thưởng an ninh')
    PerformanceBonus: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='Thưởng năng suất')
    TaskBonus2: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(15, 3), server_default=text("'0.000'"), comment='Thưởng công việc')
    ServiceQualityBonus2: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='Thưởng CLDV')
    GeneralManagermentBonus2: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='Thưởng quản lý chung')
    KPIBonus: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(15, 3), server_default=text("'0.000'"), comment='Thưởng KPI')
    VinmecBonus: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='thưởng vinmec')
    DoctorBonus: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(15, 3), server_default=text("'0.000'"), comment='Thưởng bác sĩ')
    OtherBonus3_vinmec_: Mapped[Optional[decimal.Decimal]] = mapped_column('OtherBonus3(vinmec)', DECIMAL(13, 3), server_default=text("'0.000'"), comment='Thưởng khác (vinmec)')
    HolidayBonus: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='thưởng lễ/tết')
    TotalBonus: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), server_default=text("'0.00'"), comment='tổng thưởng')
    AssistantManagerAndConcurrentBonus: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(15, 3), server_default=text("'0.000'"), comment='PC Phụ tá trưởng và kiêm nhiệm')
    GuaranteedIncomeAllowance: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(15, 3), server_default=text("'0.000'"), comment='Phụ cấp đảm bảo thu nhập')
    ParkingTravelAllowance: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='PC gửi xe/công tác')
    ProfessionalCertificateAllowance: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='Phụ cấp chứng chỉ hành nghề')
    OtherAllowances: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='phụ cấp khác')
    DentalTour: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(15, 3), server_default=text("'0.000'"))
    WarehouseAllowance: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(15, 3), server_default=text("'0.000'"), comment='Phụ cấp kho')
    OtherTotalIncome: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(15, 3), server_default=text("'0.000'"), comment='Tổng thu nhập khác')
    OtherAddition: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='cộng khác')
    OtherDeductions: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='trừ khác')
    TotalIncomeBeforeTax: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='tổng thu nhập trước thuế')
    ParticipatingSalaryInSocialInsurance: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='Mức lương tham gia BHXH')
    PersonalHealthInsurance: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='BHYT 1,5%')
    PersonalSocialInsurance: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='BHXH 8%')
    PersonalUnemploymentInsurance: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='BHTN 1%')
    EmployeeSocialInsurance: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='NLD đóng BHXH 10,5%')
    EmployeeUnionFee: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='NLĐ đóng phí công đoàn 1%')
    CompanySocialInsurance: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='BHXH 17%')
    CompanyOccupaitionalAccidentOrDisease: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='TNLĐ / BNN 0.5%')
    CompanyHealthInsurance: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='BHYT 3%')
    CompanyUnemploymentInsurance: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='BHTN 1%')
    EnterpriseSocialInsurance: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='doanh nghiệp đóng BHXH 21.5%')
    EnterpriseUnionFee: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='Doanh nghiệp đóng công đoàn 2%')
    LunchOrUniformAllowanceNoTax: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='Không tính thuế ( phụ cấp cơm trưa/ Đồng phục)')
    TotalTaxableIncome: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='Tổng thu nhập chịu thuế')
    TaxableIncomeObject: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='Đối tượng tính thuế TNCN')
    Commitment: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='Cam kết')
    Dependents: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"), comment='Số người phụ thuộc')
    TotalAssessableIncome: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='Tổng thu nhập tính thuế')
    PersonalIncomeTaxCollection: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='Thu tiền thuế TNCN')
    ActualPayment: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), server_default=text("'0.00'"), comment='Thực lãnh')
    CompanyPaysSocialInsurance: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='Cty đóng họ BHXH')
    WithholdSocialInsurance: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 3), server_default=text("'0.000'"), comment='thu hộ tiền BHXH 21.5%')
    PaidHolidayBonus: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(11, 2), server_default=text("'0.00'"), comment='Đã thanh toán thưởng Lễ/tết\\n')
    PaidOthers: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(11, 2), server_default=text("'0.00'"), comment='Đã thanh toán khác\\n')
    BankTransfer: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), server_default=text("'0.00'"), comment='chuyển khoản')
    NoteOtherAdditions: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='Ghi chú cột cộng khác\\n')
    PayPeriod: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='kỳ lương')
    Template: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='1-BO\\\\n2-Phu ta\\\\n3-Bac Si\\\\n4-Bao ve')


class StaffSalaryTaxSettlement(Base):
    __tablename__ = 'StaffSalaryTaxSettlement'

    StaffSalaryTaxSettlementId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TaxNumber: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'), comment='Mã số thuế')
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    StaffCode: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='mã nhân viên')
    FullName: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='họ tên')
    Company_: Mapped[Optional[str]] = mapped_column('Company', String(50, 'utf8mb4_unicode_ci'), comment='công ty')
    Branch: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='chi nhánh')
    WorkPosition: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='chức danh')
    StartDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='ngày bắt đầu')
    EndDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='ngày nghỉ việc')
    MaternityLeave: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='nghỉ thai sản')
    WorkContractType: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'), comment='loại hợp đồng')
    IdentityNumber: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'), comment='cccd')
    WorkedMonths: Mapped[Optional[int]] = mapped_column(INTEGER(3), comment='số tháng làm việc')
    Authority: Mapped[Optional[str]] = mapped_column(String(60, 'utf8mb4_unicode_ci'), comment='ủy quyền')
    TotalTaxableIncome: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='tổng thu nhập chịu thuế')
    TotalTaxDeducted: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='tổng tiền thuế đã khấu trừ')
    IncomeOutsideOfSalary: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='thu nhập ngoài bảng lương')
    TaxCollectionOutsideSalary: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='thu thuế ngoài bảng lương 10%')
    TaxableIncome: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='thu nhập chịu thuế')
    SocialInsuranceDeduction: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='giảm trừ bhxh')
    SelfDeduction: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='giảm trừ bản thân')
    Dependents: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 2), comment='số người phụ thuộc')
    NPTDeduction: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='giảm trừ npt')
    TotalFamilyDeduction: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='giảm trừ gia cảnh')
    AssessableIncome: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='thu nhập tính thuế')
    PersonalIncomeTaxDeduction: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='thuế tncn đã khấu trừ')
    AverageTaxableIncome: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='Bình quân TN tính thuế')
    PersonalIncomeTax: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='Số thuế TN phải đóng\n')
    Arrears_Payable_Collected_: Mapped[Optional[decimal.Decimal]] = mapped_column('Arrears(Payable&Collected)', DECIMAL(12, 2), comment='Truy thu (phải nộp - đã thu)\n')
    TaxRefund_Collected_Payable_: Mapped[Optional[decimal.Decimal]] = mapped_column('TaxRefund(Collected&Payable)', DECIMAL(12, 2), comment='Hoàn thuế (đã thu-phải nộp)\n')
    TaxableIncome_12_22_: Mapped[Optional[decimal.Decimal]] = mapped_column('TaxableIncome(12/22)', DECIMAL(12, 2), comment='Thu nhập chịu thuế 12/22\n')
    AssessableIncome_12_22_: Mapped[Optional[decimal.Decimal]] = mapped_column('AssessableIncome(12/22)', DECIMAL(12, 2), comment='TN tính thuế 12/22\n')
    TaxDeducted_12_22_: Mapped[Optional[decimal.Decimal]] = mapped_column('TaxDeducted(12/22)', DECIMAL(12, 2), comment='Thuế đã khấu trừ 12/22\n')
    TaxableIncome1: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='Thu nhập chịu thuế 1\n')
    AssessableIncome1: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='TN tính thuế 1\n')
    TaxDeducted1: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='Thuế đã khấu trừ 1\n')
    TaxableIncome2: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='Thu nhập chịu thuế 2\n')
    AssessableIncome2: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='TN tính thuế 2\n')
    TaxDeducted2: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='Thuế đã khấu trừ 2\n')
    TaxableIncome3: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='Thu nhập chịu thuế 3\n')
    AssessableIncome3: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='TN tính thuế 3\n')
    TaxDeducted3: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='Thuế đã khấu trừ 3\n')
    TaxableIncome4: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='Thu nhập chịu thuế 4')
    AssessableIncome4: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='TN tính thuế 4')
    TaxDeducted4: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='Thuế đã khấu trừ 4')
    TaxableIncome5: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='Thu nhập chịu thuế 5')
    AssessableIncome5: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='TN tính thuế 5')
    TaxDeducted5: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='Thuế đã khấu trừ 5')
    TaxableIncome6: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='Thu nhập chịu thuế 6')
    AssessableIncome6: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='TN tính thuế 6')
    TaxDeducted6: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='Thuế đã khấu trừ 6')
    TaxableIncome7: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='Thu nhập chịu thuế 7')
    AssessableIncome7: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='TN tính thuế 7')
    TaxDeducted7: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='Thuế đã khấu trừ 7')
    TaxableIncome8: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='Thu nhập chịu thuế 8')
    AssessableIncome8: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='TN tính thuế 8')
    TaxDeducted8: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='Thuế đã khấu trừ 8')
    TaxableIncome9: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='Thu nhập chịu thuế 9')
    AssessableIncome9: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='TN tính thuế 9')
    TaxDeducted9: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='Thuế đã khấu trừ 9')
    TaxableIncome10: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='Thu nhập chịu thuế 10')
    AssessableIncome10: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='TN tính thuế 10')
    TaxDeducted10: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='Thuế đã khấu trừ 10')
    TaxableIncome11: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='Thu nhập chịu thuế 11')
    AssessableIncome11: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='TN tính thuế 11')
    TaxDeducted11: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 2), comment='Thuế đã khấu trừ 11')
    Note: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='Ghi chú\n')
    Tax: Mapped[Optional[str]] = mapped_column(String(50, 'utf8mb4_unicode_ci'), comment='tính thuế\n')
    TaxCollection: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='thu thuế\n')
    Empty1: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Empty2: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))
    WorkedAtNKKMonths: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'), comment='Số tháng làm NNK\n')
    WorkedAtRHMMonths: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'), comment='Số tháng làm ở RHM\n')
    _12_2022: Mapped[Optional[str]] = mapped_column('12/2022', String(45, 'utf8mb4_unicode_ci'))
    January: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))
    February: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))
    March: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))
    April: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))
    May: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))
    June: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))
    July: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))
    August: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))
    September: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))
    October: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))
    November: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))


class StaffSelfAssessment(Base):
    __tablename__ = 'StaffSelfAssessment'

    StaffSelfAssessmentId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    PeriodTime: Mapped[Optional[datetime.date]] = mapped_column(Date, comment='2023')
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    SelfAssessmentContent: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_unicode_ci'), comment='DataJon:"{CreatedBy:\'1\',CreatedDate=\'2024-01-12 23:58:14\', \'Content\':\'\'}')
    ManagerAssessmentContent: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_unicode_ci'), comment='DataJon:"{CreatedBy:\'1\',CreatedDate=\'2024-01-12 23:58:14\', \'Content\':\'\'}')
    DoctorAssistantContent: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_unicode_ci'), comment='DataJon:"{CreatedBy:\'1\',CreatedDate=\'2024-01-12 23:58:14\', \'Content\':\'\'}')
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class StaffSignature(Base):
    __tablename__ = 'StaffSignature'

    StaffSignatureId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Signature: Mapped[Optional[str]] = mapped_column(LONGTEXT)
    State: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class StaffSignatureTracking(Base):
    __tablename__ = 'StaffSignatureTracking'

    StaffSignaturetTrackingId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    SignatureType: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='0: update 1: enable signature 2: disable signature')


t_StaffWorkPlace = Table(
    'StaffWorkPlace', Base.metadata,
    Column('StaffId', INTEGER(11), nullable=False),
    Column('WorkContractId', INTEGER(11)),
    Column('CompanyId', INTEGER(11)),
    Column('DepartmentId', INTEGER(11)),
    Column('TeamId', INTEGER(11)),
    Column('EffectiveDate', Date),
    Column('CreatedDate', DateTime, server_default=text('CURRENT_TIMESTAMP')),
    Column('UpdatedDate', DateTime),
    Index('id_StaffId', 'StaffId'),
    Index('id_WorkContractId', 'WorkContractId')
)


class Subsidize(Base):
    __tablename__ = 'Subsidize'

    SubsidizeId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    Name: Mapped[str] = mapped_column(String(64, 'utf8mb4_unicode_ci'))
    DefaultAmount: Mapped[decimal.Decimal] = mapped_column(DECIMAL(12, 2))
    Ordering: Mapped[int] = mapped_column(INTEGER(10))
    State: Mapped[int] = mapped_column(INTEGER(1), server_default=text("'1'"))


t_SubsidizeStaffHistory = Table(
    'SubsidizeStaffHistory', Base.metadata,
    Column('SubsidizeId', INTEGER(10), nullable=False),
    Column('WorkProfileId', INTEGER(10), nullable=False),
    Column('StaffId', INTEGER(10), nullable=False),
    Column('IssueDate', Date, nullable=False),
    Column('Desc', MEDIUMTEXT),
    Column('Amount', DECIMAL(12, 2), nullable=False),
    Column('TaxInclude', INTEGER(1), nullable=False, server_default=text("'1'")),
    Column('FlushedAt', INTEGER(11), nullable=False),
    Column('EndDate', Date)
)


class TaskPriority(Base):
    __tablename__ = 'TaskPriority'

    TaskPriorityId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    Name: Mapped[str] = mapped_column(String(16, 'utf8mb4_unicode_ci'))
    Ordering: Mapped[int] = mapped_column(INTEGER(11))
    ColorRGB: Mapped[str] = mapped_column(String(6, 'utf8mb4_unicode_ci'))

    Task: Mapped[List['Task']] = relationship('Task', back_populates='TaskPriority_')


class TaskStatus(Base):
    __tablename__ = 'TaskStatus'

    TaskStatusId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    Name: Mapped[str] = mapped_column(String(16, 'utf8mb4_unicode_ci'))
    Ordering: Mapped[int] = mapped_column(INTEGER(10))

    Task: Mapped[List['Task']] = relationship('Task', back_populates='TaskStatus_')


class TaskTag(Base):
    __tablename__ = 'TaskTag'
    __table_args__ = (
        Index('Tag_UNIQUE', 'Tag', unique=True),
    )

    Tag: Mapped[str] = mapped_column(String(32, 'utf8mb4_unicode_ci'), primary_key=True)
    IsCore: Mapped[int] = mapped_column(INTEGER(1), server_default=text("'0'"), comment='tag m?c ??nh c?a h? th?ng')
    CreatedAt: Mapped[int] = mapped_column(INTEGER(10))
    CreatedBy: Mapped[int] = mapped_column(INTEGER(10))
    ApprovedAt: Mapped[int] = mapped_column(INTEGER(10), server_default=text("'0'"))
    Hits: Mapped[int] = mapped_column(INTEGER(10), server_default=text("'1'"))
    ColorRGB: Mapped[str] = mapped_column(String(6, 'utf8mb4_unicode_ci'))
    ApprovedBy: Mapped[Optional[int]] = mapped_column(INTEGER(10))


class Team(Base):
    __tablename__ = 'Team'

    TeamId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    NameVi: Mapped[str] = mapped_column(VARCHAR(128))
    CompanyId: Mapped[int] = mapped_column(INTEGER(10))
    DepartmentId: Mapped[int] = mapped_column(INTEGER(10))
    State: Mapped[int] = mapped_column(INTEGER(1), server_default=text("'1'"), comment='0  - không ho?t ??ng\n1 - ho?t ??ng')
    NameEn: Mapped[Optional[str]] = mapped_column(VARCHAR(128))
    AnnualLeaveTranning: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    IsTimekeeping: Mapped[Optional[int]] = mapped_column(SMALLINT(1), server_default=text("'1'"), comment='0: no checkin; 1 checkin; null get parent value (Company)')


t_TeamLeader = Table(
    'TeamLeader', Base.metadata,
    Column('TeamId', INTEGER(10), nullable=False),
    Column('WorkProfileId', INTEGER(10), nullable=False),
    Column('StaffId', INTEGER(10), nullable=False),
    Column('Title', VARCHAR(64)),
    Column('FromDate', Date, nullable=False),
    Column('ToDate', Date),
    Column('IsCurrentManager', INTEGER(1), nullable=False, server_default=text("'1'")),
    Index('fk_TeamLeader_Team_idx', 'TeamId'),
    Index('fk_TeamLeader_WorkProfile_idx', 'WorkProfileId', 'StaffId')
)


class TeleServiceProvider(Base):
    __tablename__ = 'TeleServiceProvider'
    __table_args__ = {'comment': 'hãng cung c?p d?ch v? tho?i: Viettel, Mobilephone, Vinaphone'}

    TeleServiceProviderId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    Name: Mapped[str] = mapped_column(String(32, 'utf8mb4_unicode_ci'))
    NumberWildcard: Mapped[str] = mapped_column(String(128, 'utf8mb4_unicode_ci'), comment='097* 098* ...')
    State: Mapped[Optional[int]] = mapped_column(INTEGER(1), server_default=text("'1'"))
    Ordering: Mapped[Optional[int]] = mapped_column(INTEGER(10), server_default=text("'0'"))

    PhoneNumber: Mapped[List['PhoneNumber']] = relationship('PhoneNumber', back_populates='TeleServiceProvider_')


class TicketSupport(Base):
    __tablename__ = 'TicketSupport'
    __table_args__ = (
        Index('idx_StaffId', 'CreatedBy'),
    )

    TicketSupportId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    ReceivingOrgId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    TicketCategoryId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Content: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_unicode_ci'))
    Status: Mapped[Optional[int]] = mapped_column(TINYINT(4), comment='1 New\n5  Received\n10 Completed')
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    ResultBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    ResultDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    ResultContent: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_unicode_ci'))
    RatingContent: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_unicode_ci'))
    RatingDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    CancelDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    ReceiveBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    ReceiveDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    ReceiveContent: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_unicode_ci'))
    RejectedBy: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    RejectedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    RejectedContent: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_unicode_ci'))
    SendingOrgId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    JsonContent: Mapped[Optional[str]] = mapped_column(String(4000, 'utf8mb4_unicode_ci'))
    IsPublic: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'1'"))
    CustomerId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    RelatedStaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    SpecificationText: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    TicketSupportSpecificationDetailId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    MethodSupport: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='1 offline\n2) Online')
    MethodSupportNote: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    IsSOS: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    TypeConsultation: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'0'"), comment='1: Tư vấn | 2: Điều trị | 3: Bảo hành')


class TicketSupportCategory(Base):
    __tablename__ = 'TicketSupportCategory'

    TicketSupportCategoryId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    Name: Mapped[Optional[str]] = mapped_column(String(1024, 'utf8mb4_unicode_ci'))
    TicketSupportReceivingOrgId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Priority: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    JsonData: Mapped[Optional[str]] = mapped_column(String(1000, 'utf8mb4_unicode_ci'))


class TicketSupportComment(Base):
    __tablename__ = 'TicketSupportComment'
    __table_args__ = (
        Index('idx_Staff', 'CreatedBy'),
        Index('idx_Ticket', 'TicketSupportId')
    )

    TicketSupportCommentId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TicketSupportId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Content: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_unicode_ci'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))


class TicketSupportCustomerCashback(Base):
    __tablename__ = 'TicketSupportCustomerCashback'
    __table_args__ = (
        Index('idx_CustomerId', 'CustomerId'),
        Index('idx_StaffId', 'RelatedStaffId'),
        Index('idx_TicketId', 'TicketSupportId')
    )

    TicketSupportCustomerCashbackId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TicketSupportId: Mapped[int] = mapped_column(INTEGER(11))
    CustomerId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Amount: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(18, 2))
    RelatedStaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    RelatedBranchId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))


class TicketSupportImage(Base):
    __tablename__ = 'TicketSupportImage'
    __table_args__ = (
        Index('IDX_TicketId', 'TicketSupportId'),
    )

    TicketSupportImageId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TicketSupportId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CDNURL: Mapped[Optional[str]] = mapped_column(String(1024, 'utf8mb4_unicode_ci'))
    IsDeleted: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    Priority: Mapped[Optional[int]] = mapped_column(TINYINT(4))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class TicketSupportReceivingOrg(Base):
    __tablename__ = 'TicketSupportReceivingOrg'
    __table_args__ = (
        Index('IDX_OrId', 'OrgId'),
    )

    TicketSupportReceivingOrg: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    Name: Mapped[Optional[str]] = mapped_column(String(1024, 'utf8mb4_unicode_ci'))
    Priority: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IsDeleted: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    OrgId: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class TicketSupportRelatedObject(Base):
    __tablename__ = 'TicketSupportRelatedObject'
    __table_args__ = (
        Index('idx_ObjectId', 'ObjectId'),
    )

    TicketSupportObjectRelatedId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TicketSupportId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    ObjectType: Mapped[Optional[int]] = mapped_column(TINYINT(4), comment='1: Org\n2:Person')
    ObjectId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    DeletedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)


class TicketSupportSpecificationDetail(Base):
    __tablename__ = 'TicketSupportSpecificationDetail'

    TicketSupportSpecificationDetailId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    ParentCategoryCode: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))
    ParentCategoryName: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    CategoryName: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    Priority: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Status: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))
    GroupName: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'), server_default=text("'YCHC'"))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))


class TicketSupportTracking(Base):
    __tablename__ = 'TicketSupportTracking'

    TicketSupportTrackingId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    PushedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    TicketSupportId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    ReceivingOrgId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    TicketCategoryId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Content: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_unicode_ci'))
    Status: Mapped[Optional[int]] = mapped_column(TINYINT(4))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    ResultBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    ResultDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    ResultContent: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_unicode_ci'))
    RatingContent: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_unicode_ci'))
    RatingDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    CancelDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    ReceiveBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    ReceiveDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    ReceiveContent: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_unicode_ci'))
    RejectedBy: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    RejectedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    RejectedContent: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_unicode_ci'))
    SendingOrgId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    JsonContent: Mapped[Optional[str]] = mapped_column(String(4000, 'utf8mb4_unicode_ci'))
    IsPublic: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class TimeKeeper(Base):
    __tablename__ = 'TimeKeeper'
    __table_args__ = (
        Index('fk_TimeKeeper_Day', 'Day'),
        Index('fk_TimeKeeper_EditUser', 'EditedBy'),
        Index('fk_TimeKeeper_MobileApp_idx', 'MobileAppId'),
        Index('fk_TimeKeeper_RegistedMobileDevice_idx', 'RegistedMobileDeviceId'),
        Index('fk_TimeKeeper_Staff_idx', 'StaffId', 'Day'),
        Index('fk_TimeKeeper_WorkLocation_idx', 'CheckInLocationId'),
        Index('fk_TimeKeeper_WorkProfile_idx', 'WorkProfileId')
    )

    TimeKeeperId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    StaffId: Mapped[int] = mapped_column(INTEGER(10))
    WorkProfileId: Mapped[int] = mapped_column(INTEGER(10))
    Day: Mapped[datetime.date] = mapped_column(Date)
    WeekDayTotalBreakTimeInMunite: Mapped[int] = mapped_column(INTEGER(11), server_default=text("'0'"))
    WorkShiftTotalBreakTimeInMinute: Mapped[int] = mapped_column(INTEGER(11), server_default=text("'0'"))
    CheckInAt: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    CheckOutAt: Mapped[Optional[int]] = mapped_column(INTEGER(10), server_default=text("'0'"))
    FromIp: Mapped[Optional[str]] = mapped_column(VARCHAR(16))
    RegistedMobileDeviceId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    MobileAppId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    CheckInLocationId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    CheckOutLocationId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    WorkShiftId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    WorkShiftStartTime: Mapped[Optional[datetime.time]] = mapped_column(Time)
    WorkShiftEndTime: Mapped[Optional[datetime.time]] = mapped_column(Time)
    EditedAt: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    EditedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    WorkScheduleId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Status: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'1'"))
    ExpectedCheckInAt: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    ExpectedCheckOutAt: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    ReasonNote: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    UpdatedStatusDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    UpdatedStatusById: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IsDeleted: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'0'"))
    ConfirmCheckIn: Mapped[Optional[datetime.time]] = mapped_column(Time)
    ConfirmCheckOut: Mapped[Optional[datetime.time]] = mapped_column(Time)
    IsEdited: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'0'"))
    ApprovedAt: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    ApprovedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    TotalHour: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(3, 1))
    TotalPaidHour: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(3, 1))
    ShiftStart: Mapped[Optional[datetime.time]] = mapped_column(Time)
    ShiftEnd: Mapped[Optional[datetime.time]] = mapped_column(Time)
    TotalBreakTimeInMinute: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    StaffConfirmNote: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    Order: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    LastCheckOut: Mapped[Optional[datetime.time]] = mapped_column(Time)
    TimeKeepingRequestId: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class TimeKeeperChanging(Base):
    __tablename__ = 'TimeKeeperChanging'

    TimeKeeperChanging: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TimeKeeperId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    OldCheckInAt: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    OldCheckOutAt: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    CheckInAt: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    CheckOutAt: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    ReasonId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    ReasonNote: Mapped[Optional[str]] = mapped_column(String(128, 'utf8mb4_unicode_ci'))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


t_TimeKeeperHistory = Table(
    'TimeKeeperHistory', Base.metadata,
    Column('TimeKeeperId', INTEGER(10), nullable=False),
    Column('StaffId', INTEGER(10), nullable=False),
    Column('WorkProfileId', INTEGER(10), nullable=False),
    Column('Day', Date, nullable=False),
    Column('CheckInAt', INTEGER(10)),
    Column('CheckOutAt', INTEGER(10), server_default=text("'0'")),
    Column('FromIp', VARCHAR(16)),
    Column('RegistedMobileDeviceId', INTEGER(10)),
    Column('MobileAppId', INTEGER(10)),
    Column('CheckInLocationId', INTEGER(10)),
    Column('CheckOutLocationId', INTEGER(11)),
    Column('WorkShiftId', INTEGER(11)),
    Column('WorkShiftStartTime', Time),
    Column('WorkShiftEndTime', Time),
    Column('WeekDayTotalBreakTimeInMunite', INTEGER(11), nullable=False, server_default=text("'0'")),
    Column('WorkShiftTotalBreakTimeInMinute', INTEGER(11), nullable=False, server_default=text("'0'")),
    Column('EditedAt', INTEGER(11)),
    Column('EditedBy', INTEGER(11)),
    Column('IsDeleted', TINYINT(4), server_default=text("'0'")),
    Column('FlushedAt', INTEGER(11), nullable=False)
)


class TimeKeepingRequestDetail(Base):
    __tablename__ = 'TimeKeepingRequestDetail'
    __table_args__ = (
        Index('IX_TimeKeepingRequestDetail_TimeKeepingRequestId', 'TimeKeepingRequestId'),
    )

    TimeKeepingRequestDetailId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TimeKeepingRequestId: Mapped[int] = mapped_column(INTEGER(11))
    RequestedTime: Mapped[datetime.datetime] = mapped_column(DateTime)
    Type: Mapped[int] = mapped_column(TINYINT(4))
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[int] = mapped_column(INTEGER(11))
    UpdatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    RequestedDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    OldTime: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    WorkShiftId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    TimeKeeperId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    TimeKeeperChangingId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    WorkScheduleId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    ApprovedTime: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)


class TimeKeepingRequestStatusTracking(Base):
    __tablename__ = 'TimeKeepingRequestStatusTracking'
    __table_args__ = (
        Index('IX_TimeKeepingRequestStatusTracking_Id', 'TimeKeepingRequestId'),
    )

    TimeKeepingRequestStatusTrackingId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TimeKeepingRequestId: Mapped[int] = mapped_column(INTEGER(11))
    Status: Mapped[int] = mapped_column(TINYINT(4))
    CreatedBy: Mapped[int] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime)
    StatusNote: Mapped[Optional[str]] = mapped_column(String(200, 'utf8mb4_unicode_ci'))


class TimekeepingRequest(Base):
    __tablename__ = 'TimekeepingRequest'
    __table_args__ = (
        Index('IX_CreatedDate', 'CreatedDate'),
        Index('IX_WorkProfileId', 'WorkProfileId')
    )

    TimeKeepingRequestId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    WorkProfileId: Mapped[int] = mapped_column(INTEGER(11))
    Status: Mapped[int] = mapped_column(TINYINT(4))
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[int] = mapped_column(INTEGER(11))
    UpdatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    StatusNote: Mapped[Optional[str]] = mapped_column(String(200, 'utf8mb4_unicode_ci'))
    ApprovedStaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    ApprovedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    ReasonId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    OtherReason: Mapped[Optional[str]] = mapped_column(String(200, 'utf8mb4_unicode_ci'))
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    ReasonNote: Mapped[Optional[str]] = mapped_column(String(200, 'utf8mb4_unicode_ci'))


class TrainingEvent(Base):
    __tablename__ = 'TrainingEvent'

    TrainingEventId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    EventName: Mapped[Optional[str]] = mapped_column(String(510, 'utf8mb4_unicode_ci'), comment='Tên sự kiện')
    EventLocation: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='Khu vực tổ chức sự kiện')
    StartDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    EndDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    EventLevel: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='1: PK, 10: Khu vực; 20: Toàn hệ thống')
    Attendee: Mapped[Optional[str]] = mapped_column(String(510, 'utf8mb4_unicode_ci'), comment='Đối tượng tham gia')
    Content: Mapped[Optional[str]] = mapped_column(LONGTEXT, comment='Nội dung')
    State: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'1'"), comment='0: deleted, 1: active')
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    OtherLocation: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'), comment='Khu vực khác')
    QuantityOfParticipants: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"), comment='Số lượng người đăng ký')
    QuantityOfSubscribers: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"), comment='số lương người tham gia')
    Room: Mapped[Optional[str]] = mapped_column(String(510, 'utf8mb4_unicode_ci'))

    TrainingEventParticipant: Mapped[List['TrainingEventParticipant']] = relationship('TrainingEventParticipant', back_populates='TrainingEvent_')


class TrainingEventCheckInTracking(Base):
    __tablename__ = 'TrainingEventCheckInTracking'

    TrainingEventCheckInTrackingId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TrainingEventId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    isCheckIn: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"), comment='0 is checkout & 1 is checkin')


class User(Base):
    __tablename__ = 'User'

    UserId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    Email_: Mapped[str] = mapped_column('Email', VARCHAR(128))
    Mobile: Mapped[Optional[str]] = mapped_column(VARCHAR(16))
    Password: Mapped[Optional[str]] = mapped_column(VARCHAR(196))
    Avatar: Mapped[Optional[str]] = mapped_column(VARCHAR(196))
    DateOfBirth: Mapped[Optional[datetime.date]] = mapped_column(Date)
    Gender_: Mapped[Optional[int]] = mapped_column('Gender', INTEGER(1), server_default=text("'0'"))
    Name: Mapped[Optional[str]] = mapped_column(VARCHAR(64))
    ReferentId: Mapped[Optional[str]] = mapped_column(VARCHAR(128))
    ConnectedTo: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    AuthenMethod: Mapped[Optional[str]] = mapped_column(VARCHAR(32))
    ChangedPassword: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    ChangedPasswordToken: Mapped[Optional[str]] = mapped_column(VARCHAR(32))
    RegistedAt: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    CreatedAt: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    BlockedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    BlockedAt: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    BlockedNote: Mapped[Optional[str]] = mapped_column(TEXT)
    ActivatedAt: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    ActivatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    LastLogedIn: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    LastUpdated: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    Trashed: Mapped[Optional[int]] = mapped_column(INTEGER(1), server_default=text("'0'"), comment='dùng ?? l?u tr?ng thái b? xoá, m?t user không bao gi? b? xoá "th?t s?" kh?i b?ng')

    UserGroup: Mapped[List['UserGroup']] = relationship('UserGroup', secondary='UserUserGroup', back_populates='User_')
    Task: Mapped[List['Task']] = relationship('Task', foreign_keys='[Task.CreatedBy]', back_populates='User_')
    Task_: Mapped[List['Task']] = relationship('Task', foreign_keys='[Task.UpdatedBy]', back_populates='User1')
    File: Mapped[List['File']] = relationship('File', back_populates='User_')
    InfrequentExcludeWorkShift: Mapped[List['InfrequentExcludeWorkShift']] = relationship('InfrequentExcludeWorkShift', back_populates='User_')
    InfrequentIncludeWorkShift: Mapped[List['InfrequentIncludeWorkShift']] = relationship('InfrequentIncludeWorkShift', back_populates='User_')
    Menu: Mapped[List['Menu']] = relationship('Menu', back_populates='User_')
    Widget: Mapped[List['Widget']] = relationship('Widget', back_populates='User_')
    MenuItem: Mapped[List['MenuItem']] = relationship('MenuItem', back_populates='User_')


class UserGroup(Base):
    __tablename__ = 'UserGroup'

    UserGroupId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    RootId: Mapped[int] = mapped_column(INTEGER(11), server_default=text("'0'"))
    ParentId: Mapped[int] = mapped_column(INTEGER(11), server_default=text("'0'"))
    Name: Mapped[str] = mapped_column(VARCHAR(128))
    Lft: Mapped[int] = mapped_column(INTEGER(11), server_default=text("'1'"))
    Rgt: Mapped[int] = mapped_column(INTEGER(11), server_default=text("'2'"))
    CheckedOutBy: Mapped[int] = mapped_column(INTEGER(11), server_default=text("'0'"))
    Level: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    Description: Mapped[Optional[str]] = mapped_column(TEXT)
    CheckedOutAt: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    DftGuest: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))

    Viewing: Mapped[List['Viewing']] = relationship('Viewing', secondary='UserGroupViewing', back_populates='UserGroup_')
    User_: Mapped[List['User']] = relationship('User', secondary='UserUserGroup', back_populates='UserGroup')


class UserRaw(Base):
    __tablename__ = 'UserRaw'

    UserId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    Email_: Mapped[str] = mapped_column('Email', VARCHAR(128))
    Password: Mapped[str] = mapped_column(String(256, 'utf8mb4_unicode_ci'))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)


class Viewing(Base):
    __tablename__ = 'Viewing'

    ViewingId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    Name: Mapped[str] = mapped_column(VARCHAR(32))
    Ordering: Mapped[int] = mapped_column(INTEGER(11))
    Description: Mapped[Optional[str]] = mapped_column(TEXT)

    App_: Mapped[List['App']] = relationship('App', secondary='AppViewing', back_populates='Viewing')
    UserGroup_: Mapped[List['UserGroup']] = relationship('UserGroup', secondary='UserGroupViewing', back_populates='Viewing')
    Widget: Mapped[List['Widget']] = relationship('Widget', secondary='WidgetViewing', back_populates='Viewing_')
    Module: Mapped[List['Module']] = relationship('Module', secondary='ModuleViewing', back_populates='Viewing_')
    MenuItem: Mapped[List['MenuItem']] = relationship('MenuItem', secondary='MenuItemViewing', back_populates='Viewing_')


class VnDistrict(Base):
    __tablename__ = 'VnDistrict'
    __table_args__ = (
        Index('fk_VnDistrict_VnProvince_idx', 'VnProvinceId'),
    )

    VnDistrictId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    VnProvinceId: Mapped[int] = mapped_column(INTEGER(10))
    NameVi: Mapped[str] = mapped_column(VARCHAR(64))
    LabelVi: Mapped[str] = mapped_column(VARCHAR(32), comment='Qu?n\nTh? xã\nHuy?n\nThành ph?')
    DistrictCode: Mapped[Optional[str]] = mapped_column(VARCHAR(8))
    DistrictPostalCode: Mapped[Optional[str]] = mapped_column(VARCHAR(8))
    NameEn: Mapped[Optional[str]] = mapped_column(VARCHAR(64))
    LabelEn: Mapped[Optional[str]] = mapped_column(VARCHAR(32), comment='Urban District\nTown\nRural District\nProvincial City')
    Ordering: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    isDeleted: Mapped[Optional[int]] = mapped_column(TINYINT(4))
    State: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'1'"))

    StaffAddress: Mapped[List['StaffAddress']] = relationship('StaffAddress', back_populates='VnDistrict_')


t_VnDistrictBK = Table(
    'VnDistrictBK', Base.metadata,
    Column('VnDistrictId', INTEGER(10), nullable=False, server_default=text("'0'")),
    Column('VnProvinceId', INTEGER(10), nullable=False),
    Column('DistrictCode', VARCHAR(8)),
    Column('DistrictPostalCode', VARCHAR(8)),
    Column('NameVi', VARCHAR(64), nullable=False),
    Column('NameEn', VARCHAR(64)),
    Column('LabelVi', VARCHAR(32), nullable=False, comment='Qu?n\nTh? xã\nHuy?n\nThành ph?'),
    Column('LabelEn', VARCHAR(32), comment='Urban District\nTown\nRural District\nProvincial City'),
    Column('Ordering', INTEGER(10)),
    Column('IsDeleted', TINYINT(4))
)


class VnDistrictUpdate(Base):
    __tablename__ = 'VnDistrictUpdate'
    __table_args__ = (
        Index('fk_VnDistrict_VnProvince_idx', 'VnProvinceId'),
    )

    VnDistrictId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    VnProvinceId: Mapped[int] = mapped_column(INTEGER(10))
    NameVi: Mapped[str] = mapped_column(String(64))
    LabelVi: Mapped[str] = mapped_column(String(32), comment='Qu?n\nTh? xã\nHuy?n\nThành ph?')
    DistrictCode: Mapped[Optional[str]] = mapped_column(String(8))
    DistrictPostalCode: Mapped[Optional[str]] = mapped_column(String(8))
    NameEn: Mapped[Optional[str]] = mapped_column(String(64))
    LabelEn: Mapped[Optional[str]] = mapped_column(String(32), comment='Urban District\nTown\nRural District\nProvincial City')
    Ordering: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    NameViOld: Mapped[Optional[str]] = mapped_column(String(64))


t_VnDistrict_BK_20230710 = Table(
    'VnDistrict_BK_20230710', Base.metadata,
    Column('VnDistrictId', INTEGER(10), nullable=False, server_default=text("'0'")),
    Column('VnProvinceId', INTEGER(10), nullable=False),
    Column('DistrictCode', VARCHAR(8)),
    Column('DistrictPostalCode', VARCHAR(8)),
    Column('NameVi', VARCHAR(64), nullable=False),
    Column('NameEn', VARCHAR(64)),
    Column('LabelVi', VARCHAR(32), nullable=False, comment='Qu?n\nTh? xã\nHuy?n\nThành ph?'),
    Column('LabelEn', VARCHAR(32), comment='Urban District\nTown\nRural District\nProvincial City'),
    Column('Ordering', INTEGER(10)),
    Column('isDeleted', TINYINT(4))
)


class VnProvince(Base):
    __tablename__ = 'VnProvince'

    VnProvinceId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    NameVi: Mapped[str] = mapped_column(VARCHAR(64))
    LabelVi: Mapped[str] = mapped_column(VARCHAR(32), comment='Thành ph?\nT?nh')
    ProvinceCode: Mapped[Optional[str]] = mapped_column(VARCHAR(8))
    ProvincePostalCode: Mapped[Optional[str]] = mapped_column(VARCHAR(8))
    NameEn: Mapped[Optional[str]] = mapped_column(VARCHAR(64))
    LabelEn: Mapped[Optional[str]] = mapped_column(VARCHAR(32), comment='Municipality\nProvince')
    Ordering: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    State: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'1'"))

    StaffAddress: Mapped[List['StaffAddress']] = relationship('StaffAddress', back_populates='VnProvince_')


t_VnProvince_BK_20230710 = Table(
    'VnProvince_BK_20230710', Base.metadata,
    Column('VnProvinceId', INTEGER(10), nullable=False),
    Column('ProvinceCode', VARCHAR(8)),
    Column('ProvincePostalCode', VARCHAR(8)),
    Column('NameVi', VARCHAR(64), nullable=False),
    Column('NameEn', VARCHAR(64)),
    Column('LabelVi', VARCHAR(32), nullable=False, comment='Thành ph?\nT?nh'),
    Column('LabelEn', VARCHAR(32), comment='Municipality\nProvince'),
    Column('Ordering', INTEGER(10))
)


class VnWard(Base):
    __tablename__ = 'VnWard'
    __table_args__ = (
        Index('fk_VnWard_VnDistrict_idx', 'VnDistrictId'),
    )

    VnWardId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    VnDistrictId: Mapped[int] = mapped_column(INTEGER(10))
    NameVi: Mapped[str] = mapped_column(VARCHAR(64))
    LabelVi: Mapped[str] = mapped_column(VARCHAR(32), comment='Ph??ng\nXã\nTh? tr?n')
    WardCode: Mapped[Optional[str]] = mapped_column(VARCHAR(8))
    WardPostalCode: Mapped[Optional[str]] = mapped_column(VARCHAR(8))
    NameEn: Mapped[Optional[str]] = mapped_column(VARCHAR(64))
    LabelEn: Mapped[Optional[str]] = mapped_column(VARCHAR(32), comment='Commune\nWard\nTownship')
    Ordering: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    isDeleted: Mapped[Optional[int]] = mapped_column(TINYINT(4))
    State: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'1'"))

    StaffAddress: Mapped[List['StaffAddress']] = relationship('StaffAddress', back_populates='VnWard_')


t_VnWardBK = Table(
    'VnWardBK', Base.metadata,
    Column('VnWardId', INTEGER(10), nullable=False),
    Column('VnDistrictId', INTEGER(10), nullable=False),
    Column('WardCode', VARCHAR(8)),
    Column('WardPostalCode', VARCHAR(8)),
    Column('NameVi', VARCHAR(64), nullable=False),
    Column('NameEn', VARCHAR(64)),
    Column('LabelVi', VARCHAR(32), nullable=False, comment='Ph??ng\nXã\nTh? tr?n'),
    Column('LabelEn', VARCHAR(32), comment='Commune\nWard\nTownship'),
    Column('Ordering', INTEGER(10))
)


class VnWardUpdate(Base):
    __tablename__ = 'VnWardUpdate'
    __table_args__ = (
        Index('fk_VnWard_VnDistrict_idx', 'VnDistrictId'),
    )

    VnWardId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    VnDistrictId: Mapped[int] = mapped_column(INTEGER(10))
    NameVi: Mapped[str] = mapped_column(String(64))
    LabelVi: Mapped[str] = mapped_column(String(32), comment='Ph??ng\nXã\nTh? tr?n')
    WardCode: Mapped[Optional[str]] = mapped_column(String(8))
    WardPostalCode: Mapped[Optional[str]] = mapped_column(String(8))
    NameEn: Mapped[Optional[str]] = mapped_column(String(64))
    LabelEn: Mapped[Optional[str]] = mapped_column(String(32), comment='Commune\nWard\nTownship')
    Ordering: Mapped[Optional[int]] = mapped_column(INTEGER(10))


t_VnWard_BK_20230710 = Table(
    'VnWard_BK_20230710', Base.metadata,
    Column('VnWardId', INTEGER(10), nullable=False),
    Column('VnDistrictId', INTEGER(10), nullable=False),
    Column('WardCode', VARCHAR(8)),
    Column('WardPostalCode', VARCHAR(8)),
    Column('NameVi', VARCHAR(64), nullable=False),
    Column('NameEn', VARCHAR(64)),
    Column('LabelVi', VARCHAR(32), nullable=False, comment='Ph??ng\nXã\nTh? tr?n'),
    Column('LabelEn', VARCHAR(32), comment='Commune\nWard\nTownship'),
    Column('Ordering', INTEGER(10)),
    Column('isDeleted', TINYINT(4))
)


class Ward(Base):
    __tablename__ = 'Ward'

    WardId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    WardName: Mapped[Optional[str]] = mapped_column(String(100, 'utf8mb4_unicode_ci'))
    Label: Mapped[Optional[str]] = mapped_column(String(20, 'utf8mb4_unicode_ci'))
    DistrictId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    State: Mapped[Optional[int]] = mapped_column(TINYINT(1), server_default=text("'1'"))
    VnWardId: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class WeekDay(Base):
    __tablename__ = 'WeekDay'

    WeekDayId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    Name: Mapped[str] = mapped_column(VARCHAR(16))
    Ordering: Mapped[int] = mapped_column(INTEGER(1))
    IsWeekEnd: Mapped[int] = mapped_column(INTEGER(1), server_default=text("'0'"))
    StartTime: Mapped[datetime.time] = mapped_column(Time)
    EndTime: Mapped[datetime.time] = mapped_column(Time)
    TotalBreakTimeInMinute: Mapped[int] = mapped_column(INTEGER(10))


t_WidgetAssign = Table(
    'WidgetAssign', Base.metadata,
    Column('WidgetId', INTEGER(11), nullable=False),
    Column('MenuItemId', INTEGER(11), nullable=False)
)


class WorkContract(Base):
    __tablename__ = 'WorkContract'
    __table_args__ = (
        Index('fk_WorkContract_SignedBy_idx', 'SignedBy'),
        Index('fk_WorkContract_WorkContractType_idx', 'WorkContractTypeId')
    )

    WorkContractId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    FromDate: Mapped[datetime.date] = mapped_column(Date)
    WorkContractTypeId: Mapped[int] = mapped_column(INTEGER(10))
    WorkContractCode: Mapped[Optional[str]] = mapped_column(VARCHAR(32))
    ToDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    SignedDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    SignedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    AttachFile: Mapped[Optional[str]] = mapped_column(VARCHAR(128))
    WorkingHoursPerDay: Mapped[Optional[float]] = mapped_column(Float, server_default=text("'8'"))
    IsExitInterview: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    TerminationDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    TerminationReasonId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    TerminationReasonNote: Mapped[Optional[str]] = mapped_column(String(512, 'utf8mb4_unicode_ci'))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    WorkContractScheduleId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    WorkTimeMode: Mapped[Optional[str]] = mapped_column(String(20, 'utf8mb4_unicode_ci'), comment='Hour, Month')
    SalaryAmount: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(18, 2))
    AdditionalSalaryAmount: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(18, 2))
    SalaryNote: Mapped[Optional[str]] = mapped_column(String(256, 'utf8mb4_unicode_ci'))
    Migrate: Mapped[Optional[str]] = mapped_column(String(25, 'utf8mb4_unicode_ci'))
    SocialInsuranceSalary: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    PriorityLevel: Mapped[Optional[str]] = mapped_column(String(25, 'utf8mb4_unicode_ci'))
    WorkPriorityLevelId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    MonthlySalary: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(15, 2))


class WorkContractAnnex(Base):
    __tablename__ = 'WorkContractAnnex'
    __table_args__ = (
        Index('IX_WorkContractAnnex_WorkContractId', 'WorkContractId'),
    )

    WorkContractAnnexId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    WorkContractId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Code: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))
    SignedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    SignedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    ExpiredDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    WorkContractScheduleId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    AvailableDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    DepartmentId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    TeamId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    WorkPosition: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    WorkTimeMode: Mapped[Optional[str]] = mapped_column(String(20, 'utf8mb4_unicode_ci'))
    SalaryAmount: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(18, 2))
    SocialInsuranceSalary: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(18, 2))
    AdditionalSalaryAmount: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(18, 2))
    WorkPositionNote: Mapped[Optional[str]] = mapped_column(String(128, 'utf8mb4_unicode_ci'))
    StaffLevelId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    WorkProfilePositionId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    SyncDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    Type: Mapped[Optional[int]] = mapped_column(TINYINT(4))
    IsCurrent: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'0'"))


class WorkContractAnnexDetail(Base):
    __tablename__ = 'WorkContractAnnexDetail'
    __table_args__ = (
        Index('IX_WorkContractAnnexDetail_WorkContractAnnexId', 'WorkContractAnnexId'),
    )

    WorkContractAnnexDetailid: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    WorkContractAnnexId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    WorkContractAnnexIntentId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IsDeleted: Mapped[Optional[int]] = mapped_column(SMALLINT(6), server_default=text("'0'"))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    DepartmentId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    TeamId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    WorkPosition: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    WorkTimeMode: Mapped[Optional[str]] = mapped_column(String(20, 'utf8mb4_unicode_ci'), comment='Hour, Month')
    SalaryAmount: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(18, 2))
    SocialInsuranceSalary: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(18, 2))
    AdditionalSalaryAmount: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(18, 2))
    WorkPositionNote: Mapped[Optional[str]] = mapped_column(String(128, 'utf8mb4_unicode_ci'))
    StaffLevelId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    WorkProfilePositionId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IncomeTypeId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IncomeTypeLevelId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    WorkProfilePositionSalaryAmountId: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class WorkContractAnnexHistory(Base):
    __tablename__ = 'WorkContractAnnexHistory'

    WorkContractAnnexHistoryId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    WorkContractAnnexId: Mapped[int] = mapped_column(INTEGER(10))
    WorkContractAnnexBonus: Mapped[decimal.Decimal] = mapped_column(DECIMAL(18, 2), server_default=text("'0.00'"))
    FromDate: Mapped[datetime.date] = mapped_column(Date)
    WorkContractHistoryId: Mapped[int] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    WorkContractAnnexCode: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))
    WorkContractAnnexType: Mapped[Optional[str]] = mapped_column(String(128, 'utf8mb4_unicode_ci'))
    AttachFile: Mapped[Optional[str]] = mapped_column(String(128, 'utf8mb4_unicode_ci'))
    ToDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    Note: Mapped[Optional[str]] = mapped_column(String(1000, 'utf8mb4_unicode_ci'))


class WorkContractAnnexIntent(Base):
    __tablename__ = 'WorkContractAnnexIntent'

    WorkContractAnnexIntentId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    Name: Mapped[Optional[str]] = mapped_column(String(128, 'utf8mb4_unicode_ci'))
    Description: Mapped[Optional[str]] = mapped_column(String(128, 'utf8mb4_unicode_ci'))
    IsActive: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'1'"))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class WorkContractDocuments(Base):
    __tablename__ = 'WorkContractDocuments'

    WorkContractDocumentId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    WorkContractId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    WorkContractAnnexId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    FileName: Mapped[Optional[str]] = mapped_column(String(1024, 'utf8mb4_unicode_ci'))
    CDNURL: Mapped[Optional[str]] = mapped_column(String(2048, 'utf8mb4_unicode_ci'))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    DeletedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    DeletedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class WorkContractHistory(Base):
    __tablename__ = 'WorkContractHistory'
    __table_args__ = (
        Index('IDX_WorkContractHistory_WorkContractId', 'WorkContractId'),
    )

    WorkContractHistoryId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    DateOfBirth: Mapped[datetime.date] = mapped_column(Date)
    StaffId: Mapped[int] = mapped_column(INTEGER(10))
    WorkContractId: Mapped[int] = mapped_column(INTEGER(10))
    WorkContractFromDate: Mapped[datetime.date] = mapped_column(Date)
    WorkContractTypeId: Mapped[int] = mapped_column(INTEGER(10))
    EmploymentType: Mapped[int] = mapped_column(INTEGER(10))
    GrossSalary: Mapped[decimal.Decimal] = mapped_column(DECIMAL(18, 2), server_default=text("'0.00'"))
    BaseSalary: Mapped[decimal.Decimal] = mapped_column(DECIMAL(18, 2), server_default=text("'0.00'"))
    JobAllowance: Mapped[decimal.Decimal] = mapped_column(DECIMAL(18, 2), server_default=text("'0.00'"))
    ComplianceBonus: Mapped[decimal.Decimal] = mapped_column(DECIMAL(18, 2), server_default=text("'0.00'"))
    LunchAllowance: Mapped[decimal.Decimal] = mapped_column(DECIMAL(18, 2), server_default=text("'0.00'"))
    UniformAllowance: Mapped[decimal.Decimal] = mapped_column(DECIMAL(18, 2), server_default=text("'0.00'"))
    CreatedBy: Mapped[int] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    IdNumber: Mapped[Optional[str]] = mapped_column(String(16, 'utf8mb4_unicode_ci'))
    FullName: Mapped[Optional[str]] = mapped_column(String(64, 'utf8mb4_unicode_ci'))
    Address: Mapped[Optional[str]] = mapped_column(String(196, 'utf8mb4_unicode_ci'))
    PhoneNumber: Mapped[Optional[str]] = mapped_column(String(16, 'utf8mb4_unicode_ci'))
    StaffCode: Mapped[Optional[str]] = mapped_column(String(16, 'utf8mb4_unicode_ci'))
    WorkContractCode: Mapped[Optional[str]] = mapped_column(String(32, 'utf8mb4_unicode_ci'))
    WorkContractToDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ContractAttachFile: Mapped[Optional[str]] = mapped_column(String(128, 'utf8mb4_unicode_ci'))
    OtherAgreements: Mapped[Optional[str]] = mapped_column(String(1000, 'utf8mb4_unicode_ci'))
    Action: Mapped[Optional[str]] = mapped_column(String(1000, 'utf8mb4_unicode_ci'))
    WorkContractAnnexCode: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))
    ContractAnnexAttachFile: Mapped[Optional[str]] = mapped_column(String(128, 'utf8mb4_unicode_ci'))
    Note: Mapped[Optional[str]] = mapped_column(String(1000, 'utf8mb4_unicode_ci'))


class WorkContractSchedule(Base):
    __tablename__ = 'WorkContractSchedule'

    WorkContractScheduleId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    Name: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))
    Priority: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IsDeleted: Mapped[Optional[int]] = mapped_column(SMALLINT(6))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Level: Mapped[Optional[str]] = mapped_column(String(25, 'utf8mb4_unicode_ci'))


class WorkContractType(Base):
    __tablename__ = 'WorkContractType'

    WorkContractTypeId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    Name: Mapped[str] = mapped_column(VARCHAR(128))
    Description: Mapped[Optional[str]] = mapped_column(TEXT)
    State: Mapped[Optional[int]] = mapped_column(TINYINT(4))
    Group: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IsEndTime: Mapped[Optional[int]] = mapped_column(TINYINT(4))


class WorkLocation(Base):
    __tablename__ = 'WorkLocation'
    __table_args__ = (
        Index('Name_UNIQUE', 'Name', unique=True),
        Index('fk_WorkLocation_VnDistrict_idx', 'VnDistrictId'),
        Index('fk_WorkLocation_VnProvince_idx', 'VnProvinceId'),
        Index('fk_WorkLocation_VnWard_idx', 'VnWardId'),
        {'comment': 'vị trí vật lý liên quan đến việc check chấm công. Ví dụ 33 Đinh '
                'Tiên Hoàng vừa gồm HO lại vừa gồm Nha Khoa'}
    )

    WorkLocationId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    Name: Mapped[str] = mapped_column(VARCHAR(128))
    State: Mapped[Optional[int]] = mapped_column(INTEGER(1), server_default=text("'1'"))
    Address: Mapped[Optional[str]] = mapped_column(VARCHAR(128))
    Lat: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 3))
    Lng: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(12, 3))
    VnProvinceId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    VnDistrictId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    VnWardId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    CompanyId: Mapped[Optional[int]] = mapped_column(INTEGER(11))

    BranchWorkLocation: Mapped[List['BranchWorkLocation']] = relationship('BranchWorkLocation', back_populates='WorkLocation_')
    NetworkConfig: Mapped[List['NetworkConfig']] = relationship('NetworkConfig', back_populates='WorkLocation_')


class WorkMultiProfilePosition(Base):
    __tablename__ = 'WorkMultiProfilePosition'

    WorkMultiProfilePositionId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    WorkContractId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    WorkContractAnnexId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    WorkProfilePositionId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    State: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class WorkPlaceChanging(Base):
    __tablename__ = 'WorkPlaceChanging'
    __table_args__ = (
        Index('IX_WorkPlaceChanging_WorkContractId', 'WorkContractId'),
    )

    WorkPlaceChangingId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    CompanyId: Mapped[int] = mapped_column(INTEGER(11), server_default=text("'0'"))
    DepartmentId: Mapped[int] = mapped_column(INTEGER(11), server_default=text("'0'"))
    TeamId: Mapped[int] = mapped_column(INTEGER(11), server_default=text("'0'"))
    WorkContractId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    BranchId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    WorkLocationId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    AvailableFrom: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    IsActived: Mapped[Optional[int]] = mapped_column(SMALLINT(6), server_default=text("'1'"))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    EndDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)


class WorkPosition(Base):
    __tablename__ = 'WorkPosition'
    __table_args__ = (
        Index('fk_WorkPosition_Company_idx', 'CompanyId'),
        {'comment': 'vị trí công việc trong công ty'}
    )

    WorkPositionId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    NameVi: Mapped[str] = mapped_column(VARCHAR(128))
    CompanyId: Mapped[int] = mapped_column(INTEGER(10))
    Ordering: Mapped[int] = mapped_column(INTEGER(11), server_default=text("'0'"))
    State: Mapped[int] = mapped_column(INTEGER(1), server_default=text("'1'"))
    NameEn: Mapped[Optional[str]] = mapped_column(VARCHAR(128))


class WorkPositionHistory(Base):
    __tablename__ = 'WorkPositionHistory'

    WorkPositionHistoryId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    OrgId: Mapped[int] = mapped_column(INTEGER(10))
    WorkProfilePositionId: Mapped[int] = mapped_column(INTEGER(10))
    IsMainPosition: Mapped[int] = mapped_column(TINYINT(4), server_default=text("'0'"))
    FromDate: Mapped[datetime.date] = mapped_column(Date)
    WorkContractHistoryId: Mapped[int] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    ToDate: Mapped[Optional[datetime.date]] = mapped_column(Date)


class WorkPriorityLevel(Base):
    __tablename__ = 'WorkPriorityLevel'

    WorkPriorityLevelId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    Name: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))
    ShortName: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))
    State: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))


class WorkProfileFulltimeTracking(Base):
    __tablename__ = 'WorkProfileFulltimeTracking'

    Id: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    StaffId: Mapped[int] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    WorkProfileId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    WorkContractId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    WorkScheduleId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IsFullTime: Mapped[Optional[int]] = mapped_column(INTEGER(1), comment='0 FullTime sang Ca, 1 Ca sang FullTime')
    FromDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    ToDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))


t_WorkProfileHistory = Table(
    'WorkProfileHistory', Base.metadata,
    Column('WorkProfileId', INTEGER(10), nullable=False),
    Column('StaffId', INTEGER(10), nullable=False),
    Column('FromDate', Date, nullable=False),
    Column('ToDate', Date),
    Column('IsCurrentProfile', INTEGER(1), nullable=False, server_default=text("'0'")),
    Column('WorkPositionId', INTEGER(10), nullable=False),
    Column('CompanyId', INTEGER(10), nullable=False),
    Column('DepartmentId', INTEGER(10)),
    Column('TeamId', INTEGER(10)),
    Column('WorkContractId', INTEGER(10), nullable=False),
    Column('StaffLevelId', INTEGER(10)),
    Column('BranchId', INTEGER(10)),
    Column('DegreeId', INTEGER(10), nullable=False),
    Column('UpdatedAt', INTEGER(10)),
    Column('UpdatedBy', INTEGER(10)),
    Column('BaseSalary', DECIMAL(20, 2), nullable=False),
    Column('ExtraMonthlyIncome', DECIMAL(20, 2), nullable=False),
    Column('BankId', INTEGER(10)),
    Column('BankBranchId', INTEGER(10)),
    Column('BankAccountName', VARCHAR(64)),
    Column('BankAccountId', VARCHAR(16)),
    Column('IsFullTime', INTEGER(1)),
    Column('CreatedBy', INTEGER(11)),
    Column('CreatedAt', INTEGER(11)),
    Column('FlushedAt', INTEGER(11), nullable=False),
    Column('ActionType', String(45, 'utf8mb4_unicode_ci')),
    Column('UpdatedDate', DateTime, server_default=text('CURRENT_TIMESTAMP'))
)


class WorkProfileIncomeTypeTracking(Base):
    __tablename__ = 'WorkProfileIncomeTypeTracking'

    Id: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    WorkProfileId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    IncomeTypeId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IncomeTypeLevelId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    ObjectSource: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'1'"), comment='1 H?p ??ng, 2 ph? l?c,3 ?i?u chuy?n')
    ObjectId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    TrackingDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))


class WorkProfilePosition(Base):
    __tablename__ = 'WorkProfilePosition'
    __table_args__ = {'comment': 'vị trí công việc trong công ty'}

    WorkProfilePositionId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    Ordering: Mapped[int] = mapped_column(INTEGER(11), server_default=text("'0'"))
    State: Mapped[int] = mapped_column(INTEGER(1), server_default=text("'1'"))
    GroupCode: Mapped[str] = mapped_column(String(128, 'utf8mb4_unicode_ci'), server_default=text("'PK'"))
    Name: Mapped[Optional[str]] = mapped_column(VARCHAR(128))
    Code: Mapped[Optional[str]] = mapped_column(VARCHAR(128))
    IsAllowAccessOutside: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'1'"))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)


class WorkProfilePositionMenuNavbar(Base):
    __tablename__ = 'WorkProfilePositionMenuNavbar'
    __table_args__ = (
        Index('idx_WorkProfilePositionId_MenuNavbarId', 'WorkProfilePositionId', 'MenuNavbarId', unique=True),
    )

    Id: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    WorkProfilePositionId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    MenuNavbarId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Alias: Mapped[Optional[str]] = mapped_column(String(45, 'utf8mb4_unicode_ci'))
    IsDeleted: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))


class WorkProfilePositionPriorityMapping(Base):
    __tablename__ = 'WorkProfilePositionPriorityMapping'

    WorkProfilePositionPriorityMappingId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    WorkProfilePositionId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    WorkPriorityLevelId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    State: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))


class WorkProfilePositionRole(Base):
    __tablename__ = 'WorkProfilePositionRole'

    Id: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    WorkProfilePositionId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    RoleId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    State: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)


class WorkProfilePositionSalaryAmount(Base):
    __tablename__ = 'WorkProfilePositionSalaryAmount'
    __table_args__ = (
        Index('idx_WorkProfilePositionSalaryAmount_WorkProfilePositionId', 'WorkProfilePositionId'),
    )

    Id: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    PositionId: Mapped[Optional[int]] = mapped_column(TINYINT(4), comment='1: Tư vấn viên, 2: Phụ tá, 3: Quản lý phòng khám')
    WorkProfilePositionId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    WorkProfilePositionName: Mapped[Optional[str]] = mapped_column(VARCHAR(1000))
    StartDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    EndDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    State: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'1'"))
    SalaryTypeId: Mapped[Optional[int]] = mapped_column(TINYINT(4), comment='1: giờ, 2: ngày, 3: tháng')
    SalaryAmount: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(18, 5))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)


t_WorkProfileStaffGroup = Table(
    'WorkProfileStaffGroup', Base.metadata,
    Column('StaffGroupId', INTEGER(10), nullable=False),
    Column('WorkProfileId', INTEGER(10), nullable=False),
    Column('StaffId', INTEGER(10), nullable=False),
    Index('fk_WorkProfileStaffGroup_StaffGroup1_idx', 'StaffGroupId'),
    Index('fk_WorkProfileStaffGroup_WorkProfile1_idx', 'WorkProfileId', 'StaffId')
)


class WorkShift(Base):
    __tablename__ = 'WorkShift'
    __table_args__ = {'comment': 'ca làm việc'}

    WorkShiftId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    Name: Mapped[str] = mapped_column(VARCHAR(32))
    ShortName: Mapped[str] = mapped_column(VARCHAR(20))
    RGBColor: Mapped[str] = mapped_column(VARCHAR(6))
    Ordering: Mapped[int] = mapped_column(INTEGER(2), server_default=text("'0'"))
    TotalBreakTimeInMinute: Mapped[int] = mapped_column(INTEGER(10))
    StartTime: Mapped[Optional[datetime.time]] = mapped_column(Time, comment='Giờ bắt đầu ca làm việc')
    EndTime: Mapped[Optional[datetime.time]] = mapped_column(Time, comment='giờ kết thúc ca làm việc')
    WorkingDayEquality: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(4, 2))
    State: Mapped[Optional[int]] = mapped_column(INTEGER(11))

    InfrequentExcludeWorkShift: Mapped[List['InfrequentExcludeWorkShift']] = relationship('InfrequentExcludeWorkShift', back_populates='WorkShift_')
    InfrequentIncludeWorkShift: Mapped[List['InfrequentIncludeWorkShift']] = relationship('InfrequentIncludeWorkShift', back_populates='WorkShift_')


class WorkingReport(Base):
    __tablename__ = 'WorkingReport'
    __table_args__ = (
        Index('fk_WorkingReport_AdminExecute_idx', 'AdminExecuteId'),
        Index('fk_WorkingReport_Staff_idx', 'StaffId'),
        Index('fk_WorkingReport_WorkProfile_idx', 'WorkProfileId'),
        {'comment': 'Nếu làm ca: lấy số lần check đầu tiên tương ứng với số ca trong '
                'ngày\n'
                '\n'
                'Nếu làm fulltime: lấy lần check-in đầu tiên và lần check-out cuối '
                'cùng'}
    )

    WorkingReportId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    StaffId: Mapped[int] = mapped_column(INTEGER(10))
    WorkProfileId: Mapped[int] = mapped_column(INTEGER(10))
    Year: Mapped[int] = mapped_column(INTEGER(4))
    Month_: Mapped[int] = mapped_column('Month', INTEGER(2))
    Day: Mapped[int] = mapped_column(INTEGER(2))
    ActualWorkingHours: Mapped[decimal.Decimal] = mapped_column(DECIMAL(4, 2), comment='số giờ thực làm được tính theo thao tác chấm công')
    ScheduleWorkingHours: Mapped[decimal.Decimal] = mapped_column(DECIMAL(4, 2), comment='số giờ làm tính theo lịch công việc của nhân viên')
    AdminExecuteId: Mapped[int] = mapped_column(INTEGER(10))


class YearlyRepeatHoliday(Base):
    __tablename__ = 'YearlyRepeatHoliday'
    __table_args__ = {'comment': 'b?ng l?u các ngày l? l?p l?i m?i n?m theo l?ch d??ng: Ví d? T?t '
                'D??ng L?ch, Qu?c Khánh...'}

    Month_: Mapped[int] = mapped_column('Month', INTEGER(2), primary_key=True)
    Day: Mapped[int] = mapped_column(INTEGER(2), primary_key=True)
    Name: Mapped[str] = mapped_column(VARCHAR(32))


class AlembicVersionHistory(Base):
    __tablename__ = 'alembic_version_history'

    id: Mapped[int] = mapped_column(BIGINT(20), primary_key=True)
    operation_type: Mapped[str] = mapped_column(String(32, 'utf8mb4_unicode_ci'))
    operation_direction: Mapped[str] = mapped_column(String(32, 'utf8mb4_unicode_ci'))
    alembic_version: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    prev_alembic_version: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    user_version: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    changed_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)


t_rptStaffSalary = Table(
    'rptStaffSalary', Base.metadata,
    Column('MonthDate', Date, nullable=False),
    Column('StaffId', INTEGER(11), nullable=False),
    Column('GroupId', TINYINT(1), comment='1: BO, 2: PK'),
    Column('IsFullTime', TINYINT(1), nullable=False),
    Column('StatusId', TINYINT(1)),
    Column('SeniorityInMonth', INTEGER(11)),
    Column('SocialInsuranceSalary', DECIMAL(18, 2)),
    Column('PositionAllowance', DECIMAL(18, 2)),
    Column('AwarenessAllowance', DECIMAL(18, 2)),
    Column('LunchAllowance', DECIMAL(18, 2)),
    Column('UniformAllowance', DECIMAL(18, 2)),
    Column('ConcurrentlyAllowance', DECIMAL(18, 2)),
    Column('OthersAllowance', DECIMAL(18, 2)),
    Column('StandardWorkingHours', DECIMAL(8, 2)),
    Column('StandardWorkingDays', DECIMAL(8, 2)),
    Column('Holiday_ActualWorkingHours', DECIMAL(8, 2)),
    Column('Holiday_ActualWorkingDays', DECIMAL(8, 2)),
    Column('Weekend_ActualWorkingHours', DECIMAL(8, 2)),
    Column('Weekend_ActualWorkingDays', DECIMAL(8, 2)),
    Column('ActualWorkingHours', DECIMAL(8, 2)),
    Column('ActualWorkingDays', DECIMAL(8, 2)),
    Column('ActualLeaveHours', DECIMAL(8, 2)),
    Column('ActualLeaveDays', DECIMAL(8, 2)),
    Column('WorkingPercent', DECIMAL(20, 8)),
    Column('ActualSalary', DECIMAL(18, 2)),
    Column('ActualPositionAllowance', DECIMAL(18, 2)),
    Column('ActualAwarenessAllowance', DECIMAL(18, 2)),
    Column('ActualLunchAllowance', DECIMAL(18, 2)),
    Column('ActualUniformAllowance', DECIMAL(18, 2)),
    Column('ActualConcurrentlyAllowance', DECIMAL(18, 2)),
    Column('ActualOthersAllowance', DECIMAL(18, 2)),
    Column('WorkBonusAmount', DECIMAL(18, 2)),
    Column('HolidayBonusAmount', DECIMAL(18, 2)),
    Column('OthersBonusAmount', DECIMAL(18, 2)),
    Column('AddAmount', DECIMAL(18, 2)),
    Column('SubAmount', DECIMAL(18, 2)),
    Column('SocialInsuranceCompany', DECIMAL(18, 2)),
    Column('HealthInsuranceCompany', DECIMAL(18, 2)),
    Column('UnemploymentInsuranceCompany', DECIMAL(18, 2)),
    Column('UnionDueCompany', DECIMAL(18, 2)),
    Column('OccupationalDiseaseInsuranceCompany', DECIMAL(18, 2)),
    Column('SocialInsuranceEmployee', DECIMAL(18, 2)),
    Column('HealthInsuranceEmployee', DECIMAL(18, 2)),
    Column('UnemploymentInsuranceEmployee', DECIMAL(18, 2)),
    Column('UnionDueEmployee', DECIMAL(18, 2)),
    Column('PersonalDeductedAmount', DECIMAL(18, 2)),
    Column('DependantNumber', INTEGER(11)),
    Column('DependantDeductedAmount', DECIMAL(18, 2)),
    Column('TotalTaxableInCome', DECIMAL(18, 2)),
    Column('PersonalIncomeTax', DECIMAL(18, 2)),
    Column('NetSalary', DECIMAL(18, 2)),
    Column('CreatedBy', INTEGER(11)),
    Column('CreatedDate', DateTime, server_default=text('CURRENT_TIMESTAMP')),
    Column('UpdatedBy', INTEGER(11)),
    Column('UpdatedDate', DateTime),
    Index('IX_MonthDate', 'MonthDate', 'IsFullTime'),
    Index('IX_StaffId', 'StaffId', 'MonthDate')
)


t_rptStaffSalary_t = Table(
    'rptStaffSalary_t', Base.metadata,
    Column('MonthDate', Date),
    Column('GroupId', TINYINT(4)),
    Column('StatusId', TINYINT(4)),
    Column('StaffId', INTEGER(11)),
    Column('WorkProfileId', INTEGER(11)),
    Column('WorkContractId', INTEGER(11)),
    Column('WorkContractTypeId', INTEGER(11)),
    Column('WorkContractAnnexId', INTEGER(11)),
    Column('IsFullTime', TINYINT(4)),
    Column('IsTimekeeping', TINYINT(4)),
    Column('FromDate', Date),
    Column('ToDate', Date),
    Column('StandardWorkingHours', DECIMAL(8, 1), server_default=text("'0.0'")),
    Column('StandardWorkingDays', DECIMAL(5, 1), server_default=text("'0.0'")),
    Column('Holiday_ActualWorkingHours', DECIMAL(8, 1), server_default=text("'0.0'")),
    Column('Holiday_ActualWorkingDays', DECIMAL(5, 1), server_default=text("'0.0'")),
    Column('Weekend_ActualWorkingHours', DECIMAL(8, 1), server_default=text("'0.0'")),
    Column('Weekend_ActualWorkingDays', DECIMAL(5, 1), server_default=text("'0.0'")),
    Column('ActualWorkingHours', DECIMAL(8, 1), server_default=text("'0.0'")),
    Column('ActualWorkingDays', DECIMAL(5, 1), server_default=text("'0.0'")),
    Column('ActualLeaveHours', DECIMAL(8, 1), server_default=text("'0.0'")),
    Column('ActualLeaveDays', DECIMAL(5, 1), server_default=text("'0.0'")),
    Column('PersonalDeductedAmount', DECIMAL(18, 2), server_default=text("'0.00'")),
    Column('DependantNumber', INTEGER(11), server_default=text("'0'")),
    Column('SocialInsuranceSalary', DECIMAL(18, 2), server_default=text("'0.00'")),
    Column('ConcurrentlyAllowance', DECIMAL(18, 2), server_default=text("'0.00'")),
    Column('OthersAllowance', DECIMAL(18, 2), server_default=text("'0.00'")),
    Column('PositionAllowance', DECIMAL(18, 2), server_default=text("'0.00'")),
    Column('AwarenessAllowance', DECIMAL(18, 2), server_default=text("'0.00'")),
    Column('LunchAllowance', DECIMAL(18, 2), server_default=text("'0.00'")),
    Column('UniformAllowance', DECIMAL(18, 2), server_default=text("'0.00'")),
    Column('WorkBonusAmount', DECIMAL(18, 2), server_default=text("'0.00'")),
    Column('WorkingPercent', DECIMAL(18, 10)),
    Column('ActualSocialInsuranceSalary', DECIMAL(18, 2)),
    Column('SocialInsuranceEmployee', DECIMAL(18, 2)),
    Column('HealthInsuranceEmployee', DECIMAL(18, 2)),
    Column('UnemploymentInsuranceEmployee', DECIMAL(18, 2)),
    Column('UnionDueEmployee', DECIMAL(18, 2)),
    Column('SocialInsuranceCompany', DECIMAL(18, 2)),
    Column('HealthInsuranceCompany', DECIMAL(18, 2)),
    Column('UnemploymentInsuranceCompany', DECIMAL(18, 2)),
    Column('UnionDueCompany', DECIMAL(18, 2)),
    Column('OccupationalDiseaseInsuranceCompany', DECIMAL(18, 2)),
    Column('DependantDeductedAmount', DECIMAL(18, 2)),
    Column('TotalTaxableInCome', DECIMAL(18, 2)),
    Column('PersonalIncomeTax', DECIMAL(18, 2)),
    Column('NetSalary', DECIMAL(18, 2)),
    Column('CreatedBy', INTEGER(11)),
    Column('CreatedDate', DateTime, server_default=text('CURRENT_TIMESTAMP')),
    Column('UpdatedBy', INTEGER(11)),
    Column('UpdatedDate', DateTime),
    Index('ID1', 'StaffId', 'MonthDate', 'FromDate'),
    Index('ID2', 'MonthDate', 'GroupId')
)


t_rptTimekeeping = Table(
    'rptTimekeeping', Base.metadata,
    Column('rptDate', Date),
    Column('StaffId', INTEGER(11)),
    Column('IsFullTime', TINYINT(4)),
    Column('WorkShiftId', INTEGER(11)),
    Column('StartTime', Time),
    Column('EndTime', Time),
    Column('CheckIn', Time),
    Column('CheckOut', Time),
    Column('RequestedCheckIn', Time),
    Column('RequestedCheckOut', Time),
    Column('RequestedNote', String(2000, 'utf8mb4_unicode_ci')),
    Column('Status', TINYINT(4), comment='1: New, 2: Approved, 3: Rejected, 4: Cancelled'),
    Column('UpdatedStatusBy', INTEGER(11)),
    Column('UpdatedStatusDate', DateTime),
    Column('UpdatedStatusNote', String(2000, 'utf8mb4_unicode_ci')),
    Column('LeaveCountType', TINYINT(4), comment='1: ngh? nguyên ngày, 2: ngh? bu?i sáng, 3: ngh? bu?i chi?u'),
    Column('ActualWorkingHours', DECIMAL(5, 2)),
    Column('ActualWorkingDays', DECIMAL(5, 2)),
    Column('PaidWorkingHours', DECIMAL(5, 2)),
    Column('PaidWorkingDays', DECIMAL(5, 2)),
    Index('idx_rptTimekeeping_StaffId', 'StaffId', 'rptDate'),
    Index('idx_rptTimekeeping_rptDate', 'rptDate')
)


class AbsenceConfig(Base):
    __tablename__ = 'AbsenceConfig'
    __table_args__ = (
        ForeignKeyConstraint(['CompanyId'], ['Company.CompanyId'], name='fk_AbsenceConfig_Company'),
        Index('fk_AbsenceConfig_Company_idx', 'CompanyId')
    )

    AbsenceConfigId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    CompanyId: Mapped[int] = mapped_column(INTEGER(10))
    ApplyFromDate: Mapped[datetime.date] = mapped_column(Date)
    ApplyToDate: Mapped[datetime.date] = mapped_column(Date)
    State: Mapped[int] = mapped_column(INTEGER(1), server_default=text("'1'"))
    WorkDayEndAt: Mapped[datetime.time] = mapped_column(Time)
    WorkDayStartAt: Mapped[datetime.time] = mapped_column(Time)
    CreatedBy: Mapped[int] = mapped_column(INTEGER(10))
    CreatedAt: Mapped[int] = mapped_column(INTEGER(10))
    EditedBy: Mapped[int] = mapped_column(INTEGER(10))
    EditedAt: Mapped[int] = mapped_column(INTEGER(10))
    MaximumOffDaysPerYear: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='s? ngày ngh? t?i ?a (làm theo ngày)')
    MaximumOffHoursPerYear: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='s? gi? ngh? t?i ?a (làm bán th?i gian, theo ca)')
    MaximumOfShiftsPerYear: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='s? ca ngh? t?i ?a (làm bán th?i gian, theo ca)')

    Company_: Mapped['Company'] = relationship('Company', back_populates='AbsenceConfig')
    AbsenceRequest: Mapped[List['AbsenceRequest']] = relationship('AbsenceRequest', back_populates='AbsenceConfig_')


t_AppViewing = Table(
    'AppViewing', Base.metadata,
    Column('AppId', INTEGER(11), nullable=False),
    Column('ViewingId', INTEGER(11), nullable=False),
    ForeignKeyConstraint(['AppId'], ['App.AppId'], name='fk_AppViewing_App'),
    ForeignKeyConstraint(['ViewingId'], ['Viewing.ViewingId'], name='fk_AppViewing_Viewing'),
    Index('fk_AppViewing_AppId_idx', 'AppId'),
    Index('fk_AppViewing_ViewingId_idx', 'ViewingId')
)


class Branch(Base):
    __tablename__ = 'Branch'
    __table_args__ = (
        ForeignKeyConstraint(['CompanyId'], ['Company.CompanyId'], name='fk_Branch_Company'),
        Index('IX_LatestUpdated', 'LatestUpdated'),
        Index('fk_Branch_Company_idx', 'CompanyId'),
        Index('fk_Branch_Country_idx', 'CountryId')
    )

    BranchId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    BranchCode: Mapped[str] = mapped_column(VARCHAR(16))
    Name: Mapped[str] = mapped_column(VARCHAR(128))
    CompanyId: Mapped[int] = mapped_column(INTEGER(10))
    CountryId: Mapped[int] = mapped_column(INTEGER(10))
    State: Mapped[int] = mapped_column(INTEGER(1), server_default=text("'1'"), comment='trạng thái:\n- sắp hoạt động (0)\n- đang hoạt động (1)\n- ngưng hoạt động (-1)')
    Ordering: Mapped[int] = mapped_column(INTEGER(11), server_default=text("'0'"), comment='Sắp xếp')
    Address: Mapped[Optional[str]] = mapped_column(VARCHAR(256))
    ProvinceId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    DistrictId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    WardId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    BusinessLicenseCode: Mapped[Optional[str]] = mapped_column(String(10, 'utf8mb4_unicode_ci'))
    BusinessLicenseName: Mapped[Optional[str]] = mapped_column(String(200, 'utf8mb4_unicode_ci'))
    PublicPhoneNumber: Mapped[Optional[str]] = mapped_column(VARCHAR(16))
    PrivatePhoneNumber: Mapped[Optional[str]] = mapped_column(VARCHAR(16))
    PhoneExts: Mapped[Optional[str]] = mapped_column(VARCHAR(64))
    OpenAt: Mapped[Optional[str]] = mapped_column(VARCHAR(8), server_default=text("'8:00'"))
    CloseAt: Mapped[Optional[str]] = mapped_column(VARCHAR(8), server_default=text("'20:00'"))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    ExcludeReport: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    ORCRefCode: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    ORCExtraTime: Mapped[Optional[int]] = mapped_column(INTEGER(10), comment='Hệ thống sẽ tự động xác nhận đơn hàng nếu thời gian xác nhận vượt quá số ngày ORCExtraTime')
    Old_Address: Mapped[Optional[str]] = mapped_column(String(500, 'utf8mb4_unicode_ci'))
    GoogleMapIFrame: Mapped[Optional[str]] = mapped_column(String(4000, 'utf8mb4_unicode_ci'))
    ImageCDN: Mapped[Optional[str]] = mapped_column(String(4000, 'utf8mb4_unicode_ci'))
    WorkingTime: Mapped[Optional[str]] = mapped_column(String(4000, 'utf8mb4_unicode_ci'))
    LatestUpdated: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    Priority: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    GrandOpening: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    IsFilterReport: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text("'1'"))

    Company_: Mapped['Company'] = relationship('Company', back_populates='Branch')


class BranchWorkLocation(Base):
    __tablename__ = 'BranchWorkLocation'
    __table_args__ = (
        ForeignKeyConstraint(['WorkLocationId'], ['WorkLocation.WorkLocationId'], name='fl_bw_worklocation'),
        Index('fl_bw_worklocation', 'WorkLocationId')
    )

    Id: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    CompanyId: Mapped[int] = mapped_column(INTEGER(11))
    BranchId: Mapped[int] = mapped_column(INTEGER(10))
    WorkLocationId: Mapped[int] = mapped_column(INTEGER(10))

    WorkLocation_: Mapped['WorkLocation'] = relationship('WorkLocation', back_populates='BranchWorkLocation')


t_CompanyManager = Table(
    'CompanyManager', Base.metadata,
    Column('CompanyId', INTEGER(10), nullable=False),
    Column('WorkProfileId', INTEGER(10), nullable=False),
    Column('StaffId', INTEGER(10), nullable=False, comment='đang là người quản lý hiện tại'),
    Column('Title', VARCHAR(128)),
    Column('FromDate', Date, nullable=False),
    Column('ToDate', Date),
    Column('IsCurrentManager', INTEGER(1), nullable=False, server_default=text("'1'")),
    ForeignKeyConstraint(['CompanyId'], ['Company.CompanyId'], name='fk_company_manager'),
    Index('fk_CompanyManager_Company_idx', 'CompanyId'),
    Index('fk_CompanyManager_WorkProfile_idx', 'WorkProfileId', 'StaffId')
)


class Contact(Base):
    __tablename__ = 'Contact'
    __table_args__ = (
        ForeignKeyConstraint(['ContactPointId'], ['ContactPoint.ContactPointId'], name='fk_Contact_ContactPoint1'),
        Index('fk_Contact_ContactPoint_idx', 'ContactPointId')
    )

    ContactId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    State: Mapped[int] = mapped_column(INTEGER(1), server_default=text("'1'"))
    ContactPointId: Mapped[int] = mapped_column(INTEGER(10))
    Email_: Mapped[Optional[str]] = mapped_column('Email', String(64, 'utf8mb4_unicode_ci'))
    Phone: Mapped[Optional[str]] = mapped_column(String(30, 'utf8mb4_unicode_ci'))
    Desc: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_unicode_ci'))

    ContactPoint_: Mapped['ContactPoint'] = relationship('ContactPoint', back_populates='Contact')


t_ContactFavorite = Table(
    'ContactFavorite', Base.metadata,
    Column('UserId', INTEGER(10), nullable=False),
    Column('ContactId', INTEGER(10), nullable=False),
    Column('StaffPhoneId', INTEGER(10), nullable=False),
    ForeignKeyConstraint(['UserId'], ['User.UserId'], name='fk_ContactFavorite_User'),
    Index('fk_ContactFavorite_User_idx', 'UserId')
)


class Department(Base):
    __tablename__ = 'Department'
    __table_args__ = (
        ForeignKeyConstraint(['CompanyId'], ['Company.CompanyId'], name='fk_department_company'),
        Index('fk_Department_Company_idx', 'CompanyId')
    )

    DepartmentId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    CompanyId: Mapped[int] = mapped_column(INTEGER(10))
    NameVi: Mapped[str] = mapped_column(VARCHAR(128))
    State: Mapped[int] = mapped_column(INTEGER(1), server_default=text("'1'"), comment='0  - không ho?t ??ng\n1 - ho?t ??ng')
    NameEn: Mapped[Optional[str]] = mapped_column(VARCHAR(128))

    Company_: Mapped['Company'] = relationship('Company', back_populates='Department')


class DependantPeople(Base):
    __tablename__ = 'DependantPeople'
    __table_args__ = (
        ForeignKeyConstraint(['DependantRelationshipId'], ['DependantRelationship.DependantRelationshipId'], name='fk_DependantPeople_DependantPeopleRelationshipId'),
        ForeignKeyConstraint(['StaffId'], ['Staff.StaffId'], name='fk_dependantPeople_staff'),
        Index('IX_FullName', 'FullName'),
        Index('IX_PhoneNumber', 'PhoneNumber'),
        Index('fk_DependantPeople_DependantRelationship_idx', 'DependantRelationshipId'),
        Index('fk_DependantPeople_Staff_idx', 'StaffId'),
        {'comment': 'quan h? gi?m tr? gia c?nh'}
    )

    DependantPeopleId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    FullName: Mapped[str] = mapped_column(VARCHAR(64))
    State: Mapped[int] = mapped_column(INTEGER(1))
    Nationality: Mapped[int] = mapped_column(INTEGER(10))
    StaffId: Mapped[int] = mapped_column(INTEGER(10))
    DependantRelationshipId: Mapped[int] = mapped_column(INTEGER(10))
    IsDependant: Mapped[int] = mapped_column(INTEGER(1), server_default=text("'0'"))
    IsUrgentContact: Mapped[int] = mapped_column(INTEGER(1), server_default=text("'0'"))
    EthnicId: Mapped[int] = mapped_column(INTEGER(11), server_default=text("'1'"), comment='dân tôc')
    IdNumber: Mapped[Optional[str]] = mapped_column(VARCHAR(16))
    PassportNumber: Mapped[Optional[str]] = mapped_column(VARCHAR(16))
    NationalInsuranceNumber: Mapped[Optional[str]] = mapped_column(VARCHAR(16))
    TaxNumber: Mapped[Optional[str]] = mapped_column(VARCHAR(16))
    DateOfBirth: Mapped[Optional[datetime.date]] = mapped_column(Date)
    IssuedDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ReleasedDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    PhoneNumber: Mapped[Optional[str]] = mapped_column(String(11, 'utf8mb4_unicode_ci'))
    Address: Mapped[Optional[str]] = mapped_column(String(196, 'utf8mb4_unicode_ci'))
    Email_: Mapped[Optional[str]] = mapped_column('Email', String(128, 'utf8mb4_unicode_ci'))
    GenderId: Mapped[Optional[int]] = mapped_column(INTEGER(11), comment='1 Nam\n2 N?')
    ProvinceId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    WardId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    InsuranceHospitalId: Mapped[Optional[str]] = mapped_column(String(20, 'utf8mb4_unicode_ci'))
    DistrictId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    HealthInsuranceCode: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    IdentityIssuedDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    IdentityIssuedBy: Mapped[Optional[str]] = mapped_column(String(255, 'utf8mb4_unicode_ci'))
    DeductionFromDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    DeductionToDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))

    DependantRelationship_: Mapped['DependantRelationship'] = relationship('DependantRelationship', back_populates='DependantPeople')
    Staff_: Mapped['Staff'] = relationship('Staff', back_populates='DependantPeople')


class Extension(Base):
    __tablename__ = 'Extension'
    __table_args__ = (
        ForeignKeyConstraint(['AppId'], ['App.AppId'], name='fk_Extension_App'),
        Index('fk_Extension_App_idx', 'AppId')
    )

    ExtensionId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    AppId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    Type: Mapped[str] = mapped_column(VARCHAR(50), comment='Module\nWidget\nTheme\nPlugin\n')
    Dir: Mapped[str] = mapped_column(VARCHAR(32))
    Name: Mapped[str] = mapped_column(VARCHAR(128))
    VersionCode: Mapped[str] = mapped_column(VARCHAR(32))
    VersionName: Mapped[str] = mapped_column(VARCHAR(32))
    IsGlobal: Mapped[Optional[int]] = mapped_column(INTEGER(1), server_default=text("'0'"))
    Author: Mapped[Optional[str]] = mapped_column(VARCHAR(128))
    Description: Mapped[Optional[str]] = mapped_column(TEXT)
    Config: Mapped[Optional[str]] = mapped_column(TEXT)
    AutoUpdate: Mapped[Optional[int]] = mapped_column(INTEGER(1), server_default=text("'0'"))
    AutoUpdateUrl: Mapped[Optional[str]] = mapped_column(VARCHAR(196))

    App_: Mapped['App'] = relationship('App', back_populates='Extension')
    ExtensionHistory: Mapped[List['ExtensionHistory']] = relationship('ExtensionHistory', back_populates='Extension_')
    Module: Mapped[List['Module']] = relationship('Module', back_populates='Extension_')
    Plugin: Mapped[List['Plugin']] = relationship('Plugin', back_populates='Extension_')
    SysLanguage: Mapped[List['SysLanguage']] = relationship('SysLanguage', back_populates='Extension_')
    Theme: Mapped[List['Theme']] = relationship('Theme', back_populates='Extension_')
    Widget: Mapped[List['Widget']] = relationship('Widget', back_populates='Extension_')


class NetworkConfig(Base):
    __tablename__ = 'NetworkConfig'
    __table_args__ = (
        ForeignKeyConstraint(['WorkLocationId'], ['WorkLocation.WorkLocationId'], name='fk_NetworkConfig_WorkLocation'),
        Index('fk_NetworkConfig_WorkLocation_idx', 'WorkLocationId')
    )

    NetworkConfigId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    WanIp: Mapped[str] = mapped_column(VARCHAR(40))
    WorkLocationId: Mapped[int] = mapped_column(INTEGER(10))
    Description: Mapped[Optional[str]] = mapped_column(TEXT)
    State: Mapped[Optional[int]] = mapped_column(INTEGER(1), server_default=text("'1'"))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))

    WorkLocation_: Mapped['WorkLocation'] = relationship('WorkLocation', back_populates='NetworkConfig')


class PhoneNumber(Base):
    __tablename__ = 'PhoneNumber'
    __table_args__ = (
        ForeignKeyConstraint(['TeleServiceProviderId'], ['TeleServiceProvider.TeleServiceProviderId'], name='fk_PhoneNumber_TeleServiceProvider'),
        Index('fk_PhoneNumber_TeleServiceProvider_idx', 'TeleServiceProviderId')
    )

    PhoneNumber: Mapped[str] = mapped_column(String(16, 'utf8mb4_unicode_ci'), primary_key=True)
    TeleServiceProviderId: Mapped[int] = mapped_column(INTEGER(10))

    TeleServiceProvider_: Mapped['TeleServiceProvider'] = relationship('TeleServiceProvider', back_populates='PhoneNumber')


class ResponsiblePersion(Base):
    __tablename__ = 'ResponsiblePersion'
    __table_args__ = (
        ForeignKeyConstraint(['StaffId'], ['Staff.StaffId'], name='fk_ResponsiblePersion_Staff'),
        Index('fk_ResponsiblePersion_Staff_idx', 'StaffId')
    )

    ResponsiblePersionId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    FullName: Mapped[str] = mapped_column(VARCHAR(64))
    PhoneNumber_: Mapped[str] = mapped_column('PhoneNumber', VARCHAR(16))
    StaffId: Mapped[int] = mapped_column(INTEGER(10))

    Staff_: Mapped['Staff'] = relationship('Staff', back_populates='ResponsiblePersion')


class Session(Base):
    __tablename__ = 'Session'
    __table_args__ = (
        ForeignKeyConstraint(['AppId'], ['App.AppId'], name='fk_Session_App'),
        Index('fk_Session_App_idx', 'AppId')
    )

    SessionId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    AppId: Mapped[int] = mapped_column(INTEGER(11))
    UserId: Mapped[int] = mapped_column(INTEGER(11))
    MenuItemId: Mapped[int] = mapped_column(INTEGER(11))
    Ip: Mapped[str] = mapped_column(VARCHAR(32))
    Token: Mapped[str] = mapped_column(VARCHAR(64))
    Uri: Mapped[Optional[str]] = mapped_column(VARCHAR(196))
    AuthenMethod: Mapped[Optional[str]] = mapped_column(VARCHAR(32))
    VisitedAt: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    Config: Mapped[Optional[str]] = mapped_column(TEXT)
    ClientInfo: Mapped[Optional[str]] = mapped_column(TEXT, comment='browser infomation')
    LogedOutAt: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))

    App_: Mapped['App'] = relationship('App', back_populates='Session')


class StaffAddress(Base):
    __tablename__ = 'StaffAddress'
    __table_args__ = (
        ForeignKeyConstraint(['AddressTypeId'], ['AddressType.AddressTypeId'], name='fk_StaffAddress_AddressType'),
        ForeignKeyConstraint(['DistrictId'], ['VnDistrict.VnDistrictId'], name='fk_StaffAddress_District'),
        ForeignKeyConstraint(['ProvinceId'], ['VnProvince.VnProvinceId'], name='fk_StaffAddress_Province'),
        ForeignKeyConstraint(['StaffId'], ['Staff.StaffId'], name='fk_StaffAddress_Staff'),
        ForeignKeyConstraint(['WardId'], ['VnWard.VnWardId'], name='fk_StaffAddress_Ward'),
        Index('fk_StaffAddress_AddressType_idx', 'AddressTypeId'),
        Index('fk_StaffAddress_District_idx', 'DistrictId'),
        Index('fk_StaffAddress_Province_idx', 'ProvinceId'),
        Index('fk_StaffAddress_Staff_idx', 'StaffId'),
        Index('fk_StaffAddress_Ward_idx', 'WardId')
    )

    StaffAddressId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    Address: Mapped[str] = mapped_column(VARCHAR(196))
    ProvinceId: Mapped[int] = mapped_column(INTEGER(10))
    AddedAt: Mapped[int] = mapped_column(INTEGER(10))
    AddressTypeId: Mapped[int] = mapped_column(INTEGER(10))
    StaffId: Mapped[int] = mapped_column(INTEGER(10))
    DistrictId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    WardId: Mapped[Optional[int]] = mapped_column(INTEGER(10))

    AddressType_: Mapped['AddressType'] = relationship('AddressType', back_populates='StaffAddress')
    VnDistrict_: Mapped['VnDistrict'] = relationship('VnDistrict', back_populates='StaffAddress')
    VnProvince_: Mapped['VnProvince'] = relationship('VnProvince', back_populates='StaffAddress')
    Staff_: Mapped['Staff'] = relationship('Staff', back_populates='StaffAddress')
    VnWard_: Mapped['VnWard'] = relationship('VnWard', back_populates='StaffAddress')


class StaffAttendanceRecord(Base):
    __tablename__ = 'StaffAttendanceRecord'
    __table_args__ = (
        ForeignKeyConstraint(['StaffId'], ['Staff.StaffId'], name='fk_StaffAttendanceRecord_staffId'),
        Index('fk_StaffAttendanceRecord_staffId_idx', 'StaffId')
    )

    StaffAttendanceRecordId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    StaffId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    StaffName: Mapped[str] = mapped_column(String(64))
    StandardWorkingDay: Mapped[float] = mapped_column(Float)
    WorkProfilePositionId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    NumberOfAttendanceDays: Mapped[Optional[float]] = mapped_column(Float)
    NumberOfAnnualLeave: Mapped[Optional[float]] = mapped_column(Float)
    NumberOfPaidWorkingDay: Mapped[Optional[float]] = mapped_column(Float)
    PayrollPeriod: Mapped[Optional[str]] = mapped_column(String(6))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    ApprovedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    ApprovedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    Note: Mapped[Optional[str]] = mapped_column(String(64))

    Staff_: Mapped['Staff'] = relationship('Staff', back_populates='StaffAttendanceRecord')


class StaffPublicAsset(Base):
    __tablename__ = 'StaffPublicAsset'
    __table_args__ = (
        ForeignKeyConstraint(['PublicAssetId'], ['PublicAsset.PublicAssetId'], name='fk_StaffPublicAsset_PublicAsset'),
        ForeignKeyConstraint(['StaffId'], ['Staff.StaffId'], name='fk_StaffPublicAsset_Staff'),
        Index('fk_StaffPublicAsset_PublicAsset_idx', 'PublicAssetId'),
        Index('fk_StaffPublicAsset_Staff_idx', 'StaffId'),
        {'comment': 'tài s?n c?p cho nhân viên nào'}
    )

    StaffPublicAssetId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    StaffId: Mapped[int] = mapped_column(INTEGER(10))
    IssueDate: Mapped[datetime.date] = mapped_column(Date, comment='Ngày cấp thiết bị')
    State: Mapped[int] = mapped_column(INTEGER(1), server_default=text("'1'"), comment='Trạng thái: 1 - Đang sử dụng, 2 - Thu hồi')
    BranchId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Note: Mapped[Optional[str]] = mapped_column(Text(collation='utf8mb4_unicode_ci'), comment='Ghi chú')
    PublicAssetId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    DeviceSerialNumber: Mapped[Optional[str]] = mapped_column(String(250, 'utf8mb4_unicode_ci'))
    DeviceCode: Mapped[Optional[str]] = mapped_column(String(250, 'utf8mb4_unicode_ci'))
    DeviceName: Mapped[Optional[str]] = mapped_column(String(250, 'utf8mb4_unicode_ci'))
    RetrievalDate: Mapped[Optional[datetime.date]] = mapped_column(Date, comment='Ngày thu hồi thiết bị')
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)

    PublicAsset_: Mapped['PublicAsset'] = relationship('PublicAsset', back_populates='StaffPublicAsset')
    Staff_: Mapped['Staff'] = relationship('Staff', back_populates='StaffPublicAsset')


class Task(Base):
    __tablename__ = 'Task'
    __table_args__ = (
        ForeignKeyConstraint(['CreatedBy'], ['User.UserId'], name='fk_Task_CreatedBy'),
        ForeignKeyConstraint(['PriorityId'], ['TaskPriority.TaskPriorityId'], name='fk_Task_Priority'),
        ForeignKeyConstraint(['StatusId'], ['TaskStatus.TaskStatusId'], name='fk_Task_Status'),
        ForeignKeyConstraint(['UpdatedBy'], ['User.UserId'], name='fk_Task_EditedBy'),
        Index('fk_Task_CreatedBy_idx', 'CreatedBy'),
        Index('fk_Task_EditedBy_idx', 'UpdatedBy'),
        Index('fk_Task_Priority_idx', 'PriorityId'),
        Index('fk_Task_Status_idx', 'StatusId')
    )

    TaskId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    Content: Mapped[str] = mapped_column(Text(collation='utf8mb4_unicode_ci'))
    DueTime: Mapped[int] = mapped_column(INTEGER(11))
    StatusId: Mapped[int] = mapped_column(INTEGER(10))
    PriorityId: Mapped[int] = mapped_column(INTEGER(10))
    CreatedAt: Mapped[int] = mapped_column(INTEGER(11))
    CreatedBy: Mapped[int] = mapped_column(INTEGER(10))
    UpdatedBy: Mapped[int] = mapped_column(INTEGER(10), server_default=text("'0'"))
    UpdatedAt: Mapped[int] = mapped_column(INTEGER(11), server_default=text("'0'"))

    User_: Mapped['User'] = relationship('User', foreign_keys=[CreatedBy], back_populates='Task')
    TaskPriority_: Mapped['TaskPriority'] = relationship('TaskPriority', back_populates='Task')
    TaskStatus_: Mapped['TaskStatus'] = relationship('TaskStatus', back_populates='Task')
    User1: Mapped['User'] = relationship('User', foreign_keys=[UpdatedBy], back_populates='Task_')


class TrainingEventParticipant(Base):
    __tablename__ = 'TrainingEventParticipant'
    __table_args__ = (
        ForeignKeyConstraint(['TrainingEventId'], ['TrainingEvent.TrainingEventId'], name='fk_TrainingEventId'),
        Index('fk_TrainingEventId_idx', 'TrainingEventId')
    )

    TrainingEventParticipantId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TrainingEventId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    StaffId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    State: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    UpdatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CheckIn: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CheckInDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)

    TrainingEvent_: Mapped['TrainingEvent'] = relationship('TrainingEvent', back_populates='TrainingEventParticipant')


t_UserGroupViewing = Table(
    'UserGroupViewing', Base.metadata,
    Column('UserGroupId', INTEGER(11), nullable=False),
    Column('ViewingId', INTEGER(11), nullable=False),
    ForeignKeyConstraint(['UserGroupId'], ['UserGroup.UserGroupId'], name='fk_UserGroupViewing_UserGroup'),
    ForeignKeyConstraint(['ViewingId'], ['Viewing.ViewingId'], name='fk_UserGroupViewing_Viewing'),
    Index('fk_UserGroupViewing_UserGroupId_idx', 'UserGroupId'),
    Index('fk_UserGroupViewing_ViewingId_idx', 'ViewingId')
)


t_UserUserGroup = Table(
    'UserUserGroup', Base.metadata,
    Column('UserGroupId', INTEGER(11), nullable=False),
    Column('UserId', INTEGER(11), nullable=False),
    ForeignKeyConstraint(['UserGroupId'], ['UserGroup.UserGroupId'], name='fk_UserUserGroup_Group'),
    ForeignKeyConstraint(['UserId'], ['User.UserId'], name='fk_UserUserGroup_User'),
    Index('fk_UserUserGroup_UserGroup_idx', 'UserGroupId'),
    Index('fk_UserUserGroup_User_idx', 'UserId')
)


t_ValidProcessedTimeRecorder = Table(
    'ValidProcessedTimeRecorder', Base.metadata,
    Column('WorkingReportId', INTEGER(10), nullable=False),
    Column('CheckInAt', INTEGER(11)),
    Column('CheckOutAt', INTEGER(11)),
    Column('TimeKeeperId', INTEGER(10), nullable=False),
    Column('CheckInLocationId', INTEGER(10), nullable=False),
    Column('CheckOutLocationId', INTEGER(10), nullable=False),
    Column('TotalBreakTimeInMinute', INTEGER(11), nullable=False),
    Column('IsCheckinValid', INTEGER(10), nullable=False, server_default=text("'1'")),
    Column('InvalidCheckinMessage', String(64, 'utf8mb4_unicode_ci')),
    Column('IsCheckoutValid', INTEGER(10), nullable=False, server_default=text("'1'")),
    Column('InvalidCheckoutMessage', String(64, 'utf8mb4_unicode_ci')),
    Column('ValidCheckInTime', Time),
    Column('ValidCheckOutTime', Time),
    Column('IsShiftRecorder', INTEGER(1), nullable=False, server_default=text("'0'"), comment='ch?m công theo workshift hay không'),
    Column('WorkShiftName', String(32, 'utf8mb4_unicode_ci'), comment='tên workshift l?y t? b?ng workshift. ?? phòng tình hu?ng thay ??i tên workshift thì tên c? ?ã ???c l?u l?i ? ?ây'),
    Column('WorkingDayEquality', DECIMAL(4, 2), nullable=False),
    ForeignKeyConstraint(['TimeKeeperId'], ['TimeKeeper.TimeKeeperId'], name='fk_ValidTimeRecorder_TimeKeeper'),
    ForeignKeyConstraint(['WorkingReportId'], ['WorkingReport.WorkingReportId'], name='fk_ValidTimeRecorder_WorkingReport'),
    Index('fk_ValidTimeRecorder_TimeKeeper_idx', 'TimeKeeperId'),
    Index('fk_ValidTimeRecorder_WorkingReport_idx', 'WorkingReportId'),
    comment='b?ng l?u d? li?u các record ch?m công ???c rút'
)


class WorkProfile(Base):
    __tablename__ = 'WorkProfile'
    __table_args__ = (
        ForeignKeyConstraint(['StaffId'], ['Staff.StaffId'], name='fk_workprofile_staffId'),
        Index('IX_WorkProfile_WorkContractId', 'WorkContractId'),
        Index('fk_WorkProfile_Staff_idx', 'StaffId')
    )

    WorkProfileId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    StaffId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    FromDate: Mapped[datetime.date] = mapped_column(Date)
    IsCurrentProfile: Mapped[int] = mapped_column(INTEGER(1), server_default=text("'0'"))
    CompanyId: Mapped[int] = mapped_column(INTEGER(10))
    TeamId: Mapped[int] = mapped_column(INTEGER(10))
    StaffLevelId: Mapped[int] = mapped_column(INTEGER(10))
    DegreeId: Mapped[int] = mapped_column(INTEGER(10))
    BaseSalary: Mapped[decimal.Decimal] = mapped_column(DECIMAL(20, 2), comment='mức này có thể lookup từ bảng StaffLevel qua')
    ExtraMonthlyIncome: Mapped[decimal.Decimal] = mapped_column(DECIMAL(20, 2), comment='thưởng theo năng xuất')
    ToDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    WorkPositionId: Mapped[Optional[int]] = mapped_column(INTEGER(10), server_default=text("'0'"))
    DepartmentId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    WorkContractId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    BranchId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    UpdatedAt: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    UpdatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CreatedAt: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    BankId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    BankBranchId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    BankAccountName: Mapped[Optional[str]] = mapped_column(VARCHAR(64))
    BankAccountId: Mapped[Optional[str]] = mapped_column(VARCHAR(16))
    IsFullTime: Mapped[Optional[int]] = mapped_column(INTEGER(1), comment='1 là làm fulltime 2 là làm theo ca')
    WorkPositionNote: Mapped[Optional[str]] = mapped_column(String(128, 'utf8mb4_unicode_ci'))
    WorkPositionNote2: Mapped[Optional[str]] = mapped_column(String(25, 'utf8mb4_unicode_ci'))
    Migrate: Mapped[Optional[str]] = mapped_column(String(25, 'utf8mb4_unicode_ci'))
    WorkProfilePositionId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IncomeTypeId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IncomeTypeLevelId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CurrentBranchId: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IsAvailable: Mapped[Optional[int]] = mapped_column(INTEGER(1), server_default=text("'1'"))

    Staff_: Mapped['Staff'] = relationship('Staff', back_populates='WorkProfile')
    WorkSchedule: Mapped[List['WorkSchedule']] = relationship('WorkSchedule', back_populates='WorkProfile_')


class AbsenceRequest(Base):
    __tablename__ = 'AbsenceRequest'
    __table_args__ = (
        ForeignKeyConstraint(['AbsenceConfigId'], ['AbsenceConfig.AbsenceConfigId'], name='fk_AbsenceRequest_AbsenceConfig'),
        ForeignKeyConstraint(['AbsenceTypeId'], ['AbsenceType.AbsenceTypeId'], name='fk_AbsenceRequest_AbsenceType'),
        ForeignKeyConstraint(['RequestedBy'], ['Staff.StaffId'], name='fk_AbsenceRequest_RequestedBy'),
        Index('fk_AbsenceRequest_AbsenceConfig_idx', 'AbsenceConfigId'),
        Index('fk_AbsenceRequest_AbsenceType_idx', 'AbsenceTypeId'),
        Index('fk_AbsenceRequest_RequestedBy_idx', 'RequestedBy')
    )

    AbsenceRequestId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    AbsenceTypeId: Mapped[int] = mapped_column(INTEGER(10))
    RequestedBy: Mapped[int] = mapped_column(INTEGER(10))
    RequestedAt: Mapped[int] = mapped_column(INTEGER(10))
    RequestStatus: Mapped[int] = mapped_column(INTEGER(10), server_default=text("'0'"), comment='tr?ng thái c?a request ngh?\n1: ??ng ý\n2: t? ch?i\n3: h?y phi?u')
    AbsenceConfigId: Mapped[int] = mapped_column(INTEGER(10))
    CreatedBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Note: Mapped[Optional[str]] = mapped_column(TEXT)
    ProcessedBy: Mapped[Optional[int]] = mapped_column(INTEGER(10), comment='???c x? lý b?i ai (approved, denied,cancel...)')
    ProcessedAt: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    AbsenceFrom: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    AbsenceTo: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    ProcessedNote: Mapped[Optional[str]] = mapped_column(TEXT)
    ActualStartDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    ActualEndDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    ActualTotalDays: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(6, 2), server_default=text("'0.00'"))

    AbsenceConfig_: Mapped['AbsenceConfig'] = relationship('AbsenceConfig', back_populates='AbsenceRequest')
    AbsenceType_: Mapped['AbsenceType'] = relationship('AbsenceType', back_populates='AbsenceRequest')
    Staff_: Mapped['Staff'] = relationship('Staff', back_populates='AbsenceRequest')
    AbsenceRequestSendTo: Mapped[List['AbsenceRequestSendTo']] = relationship('AbsenceRequestSendTo', back_populates='AbsenceRequest_')


t_BranchManager = Table(
    'BranchManager', Base.metadata,
    Column('BranchId', INTEGER(10), nullable=False),
    Column('WorkProfileId', INTEGER(10), nullable=False),
    Column('StaffId', INTEGER(10), nullable=False),
    Column('Title', VARCHAR(128)),
    Column('FromDate', Date, nullable=False),
    Column('ToDate', Date),
    Column('IsCurrentManager', INTEGER(1), nullable=False, server_default=text("'1'")),
    ForeignKeyConstraint(['BranchId'], ['Branch.BranchId'], name='fk_branch_manager'),
    Index('fk_BranchManager_Branch_idx', 'BranchId'),
    Index('fk_BranchManager_WorkProfile_idx', 'WorkProfileId', 'StaffId')
)


t_DepartmentManager = Table(
    'DepartmentManager', Base.metadata,
    Column('DepartmentId', INTEGER(10), nullable=False),
    Column('WorkProfileId', INTEGER(10), nullable=False),
    Column('StaffId', INTEGER(10), nullable=False),
    Column('Title', VARCHAR(64)),
    Column('FromDate', Date, nullable=False),
    Column('ToDate', Date),
    Column('IsCurrentManager', INTEGER(1), nullable=False, server_default=text("'1'")),
    ForeignKeyConstraint(['DepartmentId'], ['Department.DepartmentId'], name='fk_department_manager'),
    Index('fk_DepartmentManager_Department_idx', 'DepartmentId'),
    Index('fk_DepartmentManager_WorkProfile_idx', 'WorkProfileId', 'StaffId')
)


class ExtensionHistory(Base):
    __tablename__ = 'ExtensionHistory'
    __table_args__ = (
        ForeignKeyConstraint(['ExtensionId', 'AppId'], ['Extension.ExtensionId', 'Extension.AppId'], name='fk_ExtensionHistory_Extension1'),
        Index('fk_ExtensionHistory_Extension_idx', 'ExtensionId', 'AppId')
    )

    ExtensionId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    AppId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    Type: Mapped[str] = mapped_column(VARCHAR(50), comment='Module\nWidget\nTheme\nPlugin\n')
    Dir: Mapped[str] = mapped_column(VARCHAR(128))
    Name: Mapped[str] = mapped_column(VARCHAR(128))
    VersionCode: Mapped[str] = mapped_column(VARCHAR(32))
    VersionName: Mapped[str] = mapped_column(VARCHAR(32))
    AddedAt: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    Author: Mapped[Optional[str]] = mapped_column(VARCHAR(128))
    Description: Mapped[Optional[str]] = mapped_column(TEXT)
    Config: Mapped[Optional[str]] = mapped_column(TEXT)
    AutoUpdate: Mapped[Optional[int]] = mapped_column(TINYINT(1), server_default=text("'0'"))
    AutoUpdateLink: Mapped[Optional[str]] = mapped_column(VARCHAR(196))

    Extension_: Mapped['Extension'] = relationship('Extension', back_populates='ExtensionHistory')


class Module(Base):
    __tablename__ = 'Module'
    __table_args__ = (
        ForeignKeyConstraint(['ExtensionId', 'AppId'], ['Extension.ExtensionId', 'Extension.AppId'], name='fk_Module_Extension'),
        Index('fk_Module_Extension_idx', 'ExtensionId', 'AppId')
    )

    ModuleId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    ExtensionId: Mapped[int] = mapped_column(INTEGER(11))
    AppId: Mapped[int] = mapped_column(INTEGER(11))
    Name: Mapped[str] = mapped_column(VARCHAR(128))
    Dir: Mapped[str] = mapped_column(VARCHAR(32))
    State: Mapped[Optional[int]] = mapped_column(INTEGER(1), server_default=text("'1'"))
    Config: Mapped[Optional[str]] = mapped_column(TEXT)

    Extension_: Mapped['Extension'] = relationship('Extension', back_populates='Module')
    Viewing_: Mapped[List['Viewing']] = relationship('Viewing', secondary='ModuleViewing', back_populates='Module')
    File: Mapped[List['File']] = relationship('File', back_populates='Module_')


class Plugin(Base):
    __tablename__ = 'Plugin'
    __table_args__ = (
        ForeignKeyConstraint(['ExtensionId', 'AppId'], ['Extension.ExtensionId', 'Extension.AppId'], name='fk_Plugin_Extension'),
        Index('fk_Plugin_Extension_idx', 'ExtensionId', 'AppId')
    )

    PluginId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    ExtensionId: Mapped[int] = mapped_column(INTEGER(11))
    AppId: Mapped[int] = mapped_column(INTEGER(11))
    Dir: Mapped[str] = mapped_column(VARCHAR(32))
    Name: Mapped[str] = mapped_column(VARCHAR(128))
    Scope: Mapped[Optional[str]] = mapped_column(VARCHAR(32))
    Ordering: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    Description: Mapped[Optional[str]] = mapped_column(TEXT)
    Config: Mapped[Optional[str]] = mapped_column(TEXT)
    State: Mapped[Optional[int]] = mapped_column(INTEGER(1), server_default=text("'0'"))

    Extension_: Mapped['Extension'] = relationship('Extension', back_populates='Plugin')


t_SessionLog = Table(
    'SessionLog', Base.metadata,
    Column('SessionId', INTEGER(11), nullable=False),
    Column('AppId', INTEGER(11), nullable=False),
    Column('MenuItemId', INTEGER(11), nullable=False),
    Column('UserId', INTEGER(11), nullable=False),
    Column('Uri', VARCHAR(196)),
    Column('AuthenMethod', VARCHAR(32)),
    Column('Visited', INTEGER(11), server_default=text("'0'")),
    Column('Config', TEXT),
    Column('Ip', VARCHAR(32), nullable=False),
    Column('Token', VARCHAR(64), nullable=False),
    Column('ClientInfo', TEXT, comment='browser infomation'),
    Column('LogedOut', INTEGER(11), server_default=text("'0'")),
    Column('AddedAt', INTEGER(11), nullable=False),
    ForeignKeyConstraint(['SessionId'], ['Session.SessionId'], name='fk_SessionLog_Session'),
    Index('fk_SessionLog_Session_idx', 'SessionId')
)


t_SubsidizeStaff = Table(
    'SubsidizeStaff', Base.metadata,
    Column('SubsidizeId', INTEGER(10), nullable=False),
    Column('WorkProfileId', INTEGER(10), nullable=False),
    Column('StaffId', INTEGER(10), nullable=False),
    Column('IssueDate', Date, nullable=False),
    Column('Desc', TEXT),
    Column('Amount', DECIMAL(12, 2), nullable=False),
    Column('TaxInclude', INTEGER(1), nullable=False, server_default=text("'1'"), comment='có tính thu? hay không'),
    Column('EndDate', Date),
    ForeignKeyConstraint(['SubsidizeId'], ['Subsidize.SubsidizeId'], name='fk_SubsidizeStaff_Subsidize'),
    ForeignKeyConstraint(['WorkProfileId', 'StaffId'], ['WorkProfile.WorkProfileId', 'WorkProfile.StaffId'], name='fk_SubsidizeStaff_WorkProfile'),
    Index('fk_SubsidizeStaff_Subsidize_idx', 'SubsidizeId'),
    Index('fk_SubsidizeStaff_WorkProfile_idx', 'WorkProfileId', 'StaffId')
)


class SysLanguage(Base):
    __tablename__ = 'SysLanguage'
    __table_args__ = (
        ForeignKeyConstraint(['ExtensionId', 'AppId'], ['Extension.ExtensionId', 'Extension.AppId'], name='fk_Language_Extension'),
        Index('fk_Language_Extension_idx', 'ExtensionId', 'AppId')
    )

    SysLanguageId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    ExtensionId: Mapped[int] = mapped_column(INTEGER(11))
    AppId: Mapped[int] = mapped_column(INTEGER(11))
    Code: Mapped[Optional[str]] = mapped_column(VARCHAR(2))
    Name: Mapped[Optional[str]] = mapped_column(VARCHAR(32))
    Ordering: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    State: Mapped[Optional[int]] = mapped_column(INTEGER(1), server_default=text("'1'"))
    IsGlobal: Mapped[Optional[int]] = mapped_column(INTEGER(1), server_default=text("'0'"), comment='ngôn ng? này ???c th?y b?i t?t c? các app')
    IsDefault: Mapped[Optional[int]] = mapped_column(INTEGER(1), server_default=text("'0'"), comment='ngôn ng? default c?a app t??ng ?ng')

    Extension_: Mapped['Extension'] = relationship('Extension', back_populates='SysLanguage')
    Menu: Mapped[List['Menu']] = relationship('Menu', back_populates='SysLanguage_')
    Widget: Mapped[List['Widget']] = relationship('Widget', back_populates='SysLanguage_')


t_TaskAssignUser = Table(
    'TaskAssignUser', Base.metadata,
    Column('TaskId', INTEGER(10), nullable=False),
    Column('AssignedAt', INTEGER(10), nullable=False),
    Column('AssignedBy', INTEGER(10), nullable=False),
    Column('AssignedTo', INTEGER(10), nullable=False),
    ForeignKeyConstraint(['AssignedBy'], ['User.UserId'], name='fk_TaskAssignUser_AssignedBy'),
    ForeignKeyConstraint(['AssignedTo'], ['User.UserId'], name='fk_TaskAssignUser_AssignedTo'),
    ForeignKeyConstraint(['TaskId'], ['Task.TaskId'], name='fk_TaskAssignUser_Task'),
    Index('fk_TaskAssignUser_AssignedBy_idx', 'AssignedBy'),
    Index('fk_TaskAssignUser_AssignedTo_idx', 'AssignedTo'),
    Index('fk_TaskAssignUser_Task_idx', 'TaskId')
)


t_TaskTagTask = Table(
    'TaskTagTask', Base.metadata,
    Column('TaskId', INTEGER(10), nullable=False),
    Column('Tag', String(32, 'utf8mb4_unicode_ci'), nullable=False),
    ForeignKeyConstraint(['TaskId'], ['Task.TaskId'], name='fk_TaskTagTask_Task'),
    Index('fk_TaskTagTask_Task_idx', 'TaskId')
)


class Theme(Base):
    __tablename__ = 'Theme'
    __table_args__ = (
        ForeignKeyConstraint(['ExtensionId', 'AppId'], ['Extension.ExtensionId', 'Extension.AppId'], name='fk_Theme_Extension'),
        Index('fk_Theme_Extension_idx', 'ExtensionId', 'AppId')
    )

    ThemeId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    ExtensionId: Mapped[int] = mapped_column(INTEGER(11))
    AppId: Mapped[int] = mapped_column(INTEGER(11))
    Name: Mapped[str] = mapped_column(VARCHAR(128))
    Dir: Mapped[str] = mapped_column(VARCHAR(32))
    State: Mapped[int] = mapped_column(INTEGER(1), server_default=text("'1'"))
    Config: Mapped[Optional[str]] = mapped_column(TEXT)
    IsDefault: Mapped[Optional[int]] = mapped_column(INTEGER(1), server_default=text("'0'"))

    Extension_: Mapped['Extension'] = relationship('Extension', back_populates='Theme')
    MenuItem: Mapped[List['MenuItem']] = relationship('MenuItem', back_populates='Theme_')


t_WorkLocationStaff = Table(
    'WorkLocationStaff', Base.metadata,
    Column('StaffId', INTEGER(10), nullable=False),
    Column('WorkProfileId', INTEGER(10), nullable=False),
    Column('WorkLocationId', INTEGER(10), nullable=False),
    ForeignKeyConstraint(['StaffId'], ['Staff.StaffId'], name='fk_WorkLocationStaff_Staff'),
    ForeignKeyConstraint(['WorkLocationId'], ['WorkLocation.WorkLocationId'], name='fk_WorkLocationStaff_WorkLocation'),
    ForeignKeyConstraint(['WorkProfileId'], ['WorkProfile.WorkProfileId'], name='fk_WorkLocationStaff_WorkProfile'),
    Index('fk_WorkLocationStaff_Staff_idx', 'StaffId'),
    Index('fk_WorkLocationStaff_WorkLocation_idx', 'WorkLocationId'),
    Index('fk_WorkLocationStaff_WorkProfile_idx', 'WorkProfileId')
)


class WorkSchedule(Base):
    __tablename__ = 'WorkSchedule'
    __table_args__ = (
        ForeignKeyConstraint(['StaffId'], ['Staff.StaffId'], name='fk_WorkSchedule_Staff'),
        ForeignKeyConstraint(['WorkProfileId'], ['WorkProfile.WorkProfileId'], name='fk_WorkSchedule_WorkProfile'),
        Index('fk_WorkSchedule_Staff_idx', 'StaffId'),
        Index('fk_WorkSchedule_WorkProfile_idx', 'WorkProfileId')
    )

    WorkScheduleId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    StaffId: Mapped[int] = mapped_column(INTEGER(10))
    ByWorkShift: Mapped[int] = mapped_column(INTEGER(1), server_default=text("'0'"))
    Trashed: Mapped[int] = mapped_column(INTEGER(1), server_default=text("'0'"))
    WorkProfileId: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    StartDate: Mapped[Optional[datetime.date]] = mapped_column(Date, comment='lịch này áp dụng từ ngày nào')
    EndDate: Mapped[Optional[datetime.date]] = mapped_column(Date, comment='lịch này áp dụng đến ngày nào')
    Count: Mapped[Optional[int]] = mapped_column(INTEGER(10), server_default=text("'0'"))
    Frequency: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    Interval: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    ByWeekDay: Mapped[Optional[int]] = mapped_column(INTEGER(1), server_default=text("'0'"), comment='ByWeekDay, ByMonthDay, ByMonth là các field dùng để control việc set lịch theo kiểu nào.\nTrong một dòng chỉ có 1 trong số 3 field này mang giá trị 1. Còn lại 2 cái kia mang giá trị 0.\n(xem lại tình huống làm việc theo tháng nhưng chỉ một số ngày nhất định - kết hợp ngày tuần hoặc ngày tháng)\n')
    ByMonthDay: Mapped[Optional[int]] = mapped_column(INTEGER(1), server_default=text("'0'"), comment='ByWeekDay, ByMonthDay, ByMonth là các field dùng để control việc set lịch theo kiểu nào.Trong một dòng chỉ có 1 trong số 3 field này mang giá trị 1. Còn lại 2 cái kia mang giá trị 0.(xem lại tình huống làm việc theo tháng nhưng chỉ một số ngày nhất định - kết hợp ngày tuần hoặc ngày tháng)')
    ExceptMonths: Mapped[Optional[str]] = mapped_column(VARCHAR(128), comment="lưu các tháng loại trừ theo định dạng json, ví dụ ['2018/07','2018/08','2018/09']")
    ExceptDates: Mapped[Optional[str]] = mapped_column(VARCHAR(128), comment="lưu các ngày loại trừ theo định dạng json, ví dụ ['2018/07/30','2018/08/30','2018/09/30']")
    CreatedDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    Migrate: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    OldEndDate: Mapped[Optional[datetime.date]] = mapped_column(Date)

    Staff_: Mapped['Staff'] = relationship('Staff', back_populates='WorkSchedule')
    WorkProfile_: Mapped['WorkProfile'] = relationship('WorkProfile', back_populates='WorkSchedule')
    InfrequentExcludeWorkShift: Mapped[List['InfrequentExcludeWorkShift']] = relationship('InfrequentExcludeWorkShift', back_populates='WorkSchedule_')
    InfrequentIncludeWorkShift: Mapped[List['InfrequentIncludeWorkShift']] = relationship('InfrequentIncludeWorkShift', back_populates='WorkSchedule_')


class AbsenceRequestSendTo(Base):
    __tablename__ = 'AbsenceRequestSendTo'
    __table_args__ = (
        ForeignKeyConstraint(['AbsenceRequestId'], ['AbsenceRequest.AbsenceRequestId'], name='fk_AbsenceRequestSendTo_AbsenceRequest'),
        ForeignKeyConstraint(['SendToStaffId'], ['Staff.StaffId'], name='fk_AbsenceRequestSendTo_SendToStaffId'),
        Index('fk_AbsenceRequestSendTo_AbsenceRequest_idx', 'AbsenceRequestId'),
        Index('fk_AbsenceRequestSendTo_SendToStaffId_idx', 'SendToStaffId')
    )

    AbsenceRequestId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    SendToStaffId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    SentAt: Mapped[int] = mapped_column(INTEGER(10))
    ProcessedAt: Mapped[Optional[int]] = mapped_column(INTEGER(10))
    Note: Mapped[Optional[str]] = mapped_column(TEXT)

    AbsenceRequest_: Mapped['AbsenceRequest'] = relationship('AbsenceRequest', back_populates='AbsenceRequestSendTo')
    Staff_: Mapped['Staff'] = relationship('Staff', back_populates='AbsenceRequestSendTo')


t_ByMonthDay = Table(
    'ByMonthDay', Base.metadata,
    Column('WorkScheduleId', INTEGER(10), nullable=False),
    Column('MonthDayId', INTEGER(10), nullable=False),
    Column('BranchId', INTEGER(10)),
    Column('StartTime', Time, nullable=False),
    Column('EndTime', Time, nullable=False),
    Column('TotalBreakTimeInMinute', INTEGER(11), nullable=False),
    ForeignKeyConstraint(['MonthDayId'], ['MonthDay.MonthDayId'], name='fk_ByMonthDay_MonthDay'),
    ForeignKeyConstraint(['WorkScheduleId'], ['WorkSchedule.WorkScheduleId'], name='fk_ByMonthDay_WorkSchedule'),
    Index('fk_ByMonthDay_MonthDay_idx', 'MonthDayId'),
    Index('fk_ByMonthDay_WorkLocationId_idx', 'BranchId'),
    Index('fk_ByMonthDay_WorkSchedule_idx', 'WorkScheduleId')
)


t_ByWeekDay = Table(
    'ByWeekDay', Base.metadata,
    Column('WorkScheduleId', INTEGER(10), nullable=False),
    Column('WeekDayId', INTEGER(10), nullable=False),
    Column('BranchId', INTEGER(10)),
    Column('StartTime', Time, nullable=False),
    Column('EndTime', Time, nullable=False),
    Column('TotalBreakTimeInMinute', INTEGER(11), nullable=False, server_default=text("'0'")),
    ForeignKeyConstraint(['WeekDayId'], ['WeekDay.WeekDayId'], name='fk_ByWeekDay_WeekDay'),
    ForeignKeyConstraint(['WorkScheduleId'], ['WorkSchedule.WorkScheduleId'], name='fk_ByWeekDay_WorkSchedule'),
    Index('fk_ByWeekDay_WeekDay_idx', 'WeekDayId'),
    Index('fk_ByWeekDay_WorkLocationId_idx', 'BranchId'),
    Index('fk_ByWeekDay_WorkSchedule_idx', 'WorkScheduleId')
)


class File(Base):
    __tablename__ = 'File'
    __table_args__ = (
        ForeignKeyConstraint(['CreatedBy'], ['User.UserId'], name='fk_File_CreatedBy'),
        ForeignKeyConstraint(['FromApp'], ['App.AppId'], name='fk_File_App'),
        ForeignKeyConstraint(['FromModule'], ['Module.ModuleId'], name='fk_File_Module'),
        Index('fk_File_App_idx', 'FromApp'),
        Index('fk_File_CreatedBy_idx', 'CreatedBy'),
        Index('fk_File_Module_idx', 'FromModule')
    )

    FileId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    FromModule: Mapped[int] = mapped_column(INTEGER(11))
    FromApp: Mapped[int] = mapped_column(INTEGER(11))
    CreatedBy: Mapped[int] = mapped_column(INTEGER(11), server_default=text("'0'"))
    CreatedAt: Mapped[int] = mapped_column(INTEGER(11), server_default=text("'0'"))
    Name: Mapped[Optional[str]] = mapped_column(VARCHAR(196))
    FileName: Mapped[Optional[str]] = mapped_column(VARCHAR(196))
    FileThumbnail: Mapped[Optional[str]] = mapped_column(VARCHAR(196))
    FileExt: Mapped[Optional[str]] = mapped_column(VARCHAR(5))
    FileMine: Mapped[Optional[str]] = mapped_column(VARCHAR(128))
    FileSize: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IsImage: Mapped[Optional[int]] = mapped_column(INTEGER(1), server_default=text("'0'"))

    User_: Mapped['User'] = relationship('User', back_populates='File')
    App_: Mapped['App'] = relationship('App', back_populates='File')
    Module_: Mapped['Module'] = relationship('Module', back_populates='File')


class InfrequentExcludeWorkShift(Base):
    __tablename__ = 'InfrequentExcludeWorkShift'
    __table_args__ = (
        ForeignKeyConstraint(['ExcludedBy'], ['User.UserId'], name='fk_InfrequentExcludeWorkShift_ExcludedBy'),
        ForeignKeyConstraint(['WorkScheduleId'], ['WorkSchedule.WorkScheduleId'], name='fk_InfrequentExcludeWorkShift_WorkSchedule'),
        ForeignKeyConstraint(['WorkShiftId'], ['WorkShift.WorkShiftId'], name='fk_InfrequentExcludeWorkShift_WorkShift'),
        Index('IX_InfrequentExcludeWorkShift_Date', 'Date'),
        Index('fk_InfrequentExcludeWorkShift_ExcludedBy_idx', 'ExcludedBy'),
        Index('fk_InfrequentExcludeWorkShift_WorkSchedule_idx', 'WorkScheduleId'),
        Index('fk_InfrequentExcludeWorkShift_WorkShift_idx', 'WorkShiftId')
    )

    InfrequentExcludeWorkShiftId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    WorkScheduleId: Mapped[int] = mapped_column(INTEGER(10))
    Date_: Mapped[datetime.date] = mapped_column('Date', Date)
    WorkShiftId: Mapped[int] = mapped_column(INTEGER(10))
    ExcludedAt: Mapped[int] = mapped_column(INTEGER(11))
    ExcludedBy: Mapped[int] = mapped_column(INTEGER(10))

    User_: Mapped['User'] = relationship('User', back_populates='InfrequentExcludeWorkShift')
    WorkSchedule_: Mapped['WorkSchedule'] = relationship('WorkSchedule', back_populates='InfrequentExcludeWorkShift')
    WorkShift_: Mapped['WorkShift'] = relationship('WorkShift', back_populates='InfrequentExcludeWorkShift')


class InfrequentIncludeWorkShift(Base):
    __tablename__ = 'InfrequentIncludeWorkShift'
    __table_args__ = (
        ForeignKeyConstraint(['AddedBy'], ['User.UserId'], name='fk_InfrequentIncludeWorkShift_AddedBy'),
        ForeignKeyConstraint(['WorkScheduleId'], ['WorkSchedule.WorkScheduleId'], name='fk_InfrequentIncludeWorkShift_WorkSchedule'),
        ForeignKeyConstraint(['WorkShiftId'], ['WorkShift.WorkShiftId'], name='fk_InfrequentIncludeWorkShift_WorkShift'),
        Index('IX_InfrequentIncludeWorkShift_Date', 'Date', 'WorkScheduleId'),
        Index('fk_InfrequentIncludeWorkShift_AddedBy_idx', 'AddedBy'),
        Index('fk_InfrequentIncludeWorkShift_WorkLocation_idx', 'BranchId'),
        Index('fk_InfrequentIncludeWorkShift_WorkSchedule_idx', 'WorkScheduleId'),
        Index('fk_InfrequentIncludeWorkShift_WorkShift_idx', 'WorkShiftId')
    )

    InfrequentIncludeWorkShiftId: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    WorkScheduleId: Mapped[int] = mapped_column(INTEGER(10))
    Date_: Mapped[datetime.date] = mapped_column('Date', Date)
    WorkShiftId: Mapped[int] = mapped_column(INTEGER(10))
    BranchId: Mapped[int] = mapped_column(INTEGER(10))
    AddedAt: Mapped[int] = mapped_column(INTEGER(10))
    AddedBy: Mapped[int] = mapped_column(INTEGER(10))

    User_: Mapped['User'] = relationship('User', back_populates='InfrequentIncludeWorkShift')
    WorkSchedule_: Mapped['WorkSchedule'] = relationship('WorkSchedule', back_populates='InfrequentIncludeWorkShift')
    WorkShift_: Mapped['WorkShift'] = relationship('WorkShift', back_populates='InfrequentIncludeWorkShift')


class Menu(Base):
    __tablename__ = 'Menu'
    __table_args__ = (
        ForeignKeyConstraint(['AppId'], ['App.AppId'], name='fk_Menu_AppId'),
        ForeignKeyConstraint(['CreatedBy'], ['User.UserId'], name='fk_Menu_CreatedBy'),
        ForeignKeyConstraint(['SysLanguageId'], ['SysLanguage.SysLanguageId'], name='fk_Menu_SysLanguage'),
        Index('fk_Menu_App_idx', 'AppId'),
        Index('fk_Menu_CreatedBy_idx', 'CreatedBy'),
        Index('fk_Menu_SysLanguage_idx', 'SysLanguageId')
    )

    MenuId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    SysLanguageId: Mapped[int] = mapped_column(INTEGER(11))
    AppId: Mapped[int] = mapped_column(INTEGER(11))
    Name: Mapped[str] = mapped_column(VARCHAR(128))
    CreatedBy: Mapped[int] = mapped_column(INTEGER(11))
    Description: Mapped[Optional[str]] = mapped_column(TEXT)
    CreatedAt: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CheckedOutBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CheckedOutAt: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    State: Mapped[Optional[int]] = mapped_column(INTEGER(1), server_default=text("'1'"))

    App_: Mapped['App'] = relationship('App', back_populates='Menu')
    User_: Mapped['User'] = relationship('User', back_populates='Menu')
    SysLanguage_: Mapped['SysLanguage'] = relationship('SysLanguage', back_populates='Menu')
    MenuItem: Mapped[List['MenuItem']] = relationship('MenuItem', back_populates='Menu_')


t_ModuleViewing = Table(
    'ModuleViewing', Base.metadata,
    Column('ViewingId', INTEGER(11), nullable=False),
    Column('ModuleId', INTEGER(11), nullable=False),
    ForeignKeyConstraint(['ModuleId'], ['Module.ModuleId'], name='fk_ModuleViewing_Module'),
    ForeignKeyConstraint(['ViewingId'], ['Viewing.ViewingId'], name='fk_ModuleViewing_Viewing'),
    Index('fk_ModuleViewing_ModuleId_idx', 'ModuleId'),
    Index('fk_ModuleViewing_ViewingId_idx', 'ViewingId')
)


class Widget(Base):
    __tablename__ = 'Widget'
    __table_args__ = (
        ForeignKeyConstraint(['CreatedBy'], ['User.UserId'], name='fk_Widget_CreatedBy'),
        ForeignKeyConstraint(['ExtensionId', 'AppId'], ['Extension.ExtensionId', 'Extension.AppId'], name='fk_Widget_Extension'),
        ForeignKeyConstraint(['SysLanguageId'], ['SysLanguage.SysLanguageId'], name='fk_Widget_SysLanguage'),
        Index('fk_Widget_CreatedBy_idx', 'CreatedBy'),
        Index('fk_Widget_Extension_idx', 'ExtensionId', 'AppId'),
        Index('fk_Widget_SysLanguage_idx', 'SysLanguageId')
    )

    WidgetId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    ExtensionId: Mapped[int] = mapped_column(INTEGER(11))
    AppId: Mapped[int] = mapped_column(INTEGER(11))
    SysLanguageId: Mapped[int] = mapped_column(INTEGER(11))
    Name: Mapped[str] = mapped_column(VARCHAR(128))
    Dir: Mapped[str] = mapped_column(VARCHAR(32))
    State: Mapped[int] = mapped_column(INTEGER(1), server_default=text("'1'"))
    Title: Mapped[str] = mapped_column(VARCHAR(128))
    Position: Mapped[str] = mapped_column(VARCHAR(32))
    Ordering: Mapped[int] = mapped_column(INTEGER(11), server_default=text("'0'"))
    Config: Mapped[str] = mapped_column(TEXT)
    CreatedBy: Mapped[int] = mapped_column(INTEGER(11))
    CreatedAt: Mapped[int] = mapped_column(INTEGER(11))
    Description: Mapped[str] = mapped_column(TEXT)
    IsShowTitle: Mapped[Optional[int]] = mapped_column(INTEGER(1), server_default=text("'1'"))
    CheckedOutBy: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CheckedOutAt: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    ShowUp: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    PutDown: Mapped[Optional[int]] = mapped_column(INTEGER(11))

    Viewing_: Mapped[List['Viewing']] = relationship('Viewing', secondary='WidgetViewing', back_populates='Widget')
    User_: Mapped['User'] = relationship('User', back_populates='Widget')
    Extension_: Mapped['Extension'] = relationship('Extension', back_populates='Widget')
    SysLanguage_: Mapped['SysLanguage'] = relationship('SysLanguage', back_populates='Widget')


t_WorkShiftByMonthDay = Table(
    'WorkShiftByMonthDay', Base.metadata,
    Column('WorkShiftId', INTEGER(10), nullable=False),
    Column('WorkScheduleId', INTEGER(10), nullable=False),
    Column('MonthDayId', INTEGER(10), nullable=False),
    Column('BranchId', INTEGER(10), nullable=False),
    Column('TotalBreakTimeInMinute', INTEGER(11), server_default=text("'0'")),
    ForeignKeyConstraint(['MonthDayId'], ['MonthDay.MonthDayId'], name='fk_WorkShiftByMonthDay_MonthDay'),
    ForeignKeyConstraint(['WorkScheduleId'], ['WorkSchedule.WorkScheduleId'], name='fk_WorkShiftByMonthDay_WorkSchedule'),
    ForeignKeyConstraint(['WorkShiftId'], ['WorkShift.WorkShiftId'], name='fk_WorkShiftByMonthDay_WorkShift'),
    Index('fk_WorkShiftByMonthDay_MonthDay_idx', 'MonthDayId'),
    Index('fk_WorkShiftByMonthDay_WorkLocationId_idx', 'BranchId'),
    Index('fk_WorkShiftByMonthDay_WorkSchedule_idx', 'WorkScheduleId'),
    Index('fk_WorkShiftByMonthDay_WorkShift_idx', 'WorkShiftId')
)


t_WorkShiftByWeekDay = Table(
    'WorkShiftByWeekDay', Base.metadata,
    Column('WorkShiftId', INTEGER(10), nullable=False),
    Column('WorkScheduleId', INTEGER(10), nullable=False),
    Column('WeekDayId', INTEGER(10), nullable=False),
    Column('BranchId', INTEGER(10), nullable=False),
    Column('TotalBreakTimeInMinute', INTEGER(11), nullable=False, server_default=text("'0'")),
    ForeignKeyConstraint(['WeekDayId'], ['WeekDay.WeekDayId'], name='fk_WorkShiftByWeekDay_WeekDay'),
    ForeignKeyConstraint(['WorkScheduleId'], ['WorkSchedule.WorkScheduleId'], name='fk_WorkShiftByWeekDay_WorkSchedule'),
    ForeignKeyConstraint(['WorkShiftId'], ['WorkShift.WorkShiftId'], name='fk_WorkShiftByWeekDay_WorkShift'),
    Index('fk_WorkShiftByWeekDay_WeekDay_idx', 'WeekDayId'),
    Index('fk_WorkShiftByWeekDay_WorkLocationId_idx', 'BranchId'),
    Index('fk_WorkShiftByWeekDay_WorkSchedule_idx', 'WorkScheduleId'),
    Index('fk_WorkShiftByWeekDay_WorkShift_idx', 'WorkShiftId')
)


class MenuItem(Base):
    __tablename__ = 'MenuItem'
    __table_args__ = (
        ForeignKeyConstraint(['CreatedBy'], ['User.UserId'], name='fk_MenuItem_CreatedBy'),
        ForeignKeyConstraint(['MenuId'], ['Menu.MenuId'], name='fk_MenuItem_Menu'),
        ForeignKeyConstraint(['ThemeId'], ['Theme.ThemeId'], name='fk_MenuItem_Theme'),
        Index('fk_MenuItem_CreatedBy_idx', 'CreatedBy'),
        Index('fk_MenuItem_Menu_idx', 'MenuId'),
        Index('fk_MenuItem_Theme_idx', 'ThemeId')
    )

    MenuItemId: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    RootId: Mapped[int] = mapped_column(INTEGER(11), server_default=text("'0'"))
    MenuId: Mapped[int] = mapped_column(INTEGER(11))
    ParentId: Mapped[int] = mapped_column(INTEGER(11), server_default=text("'0'"))
    ThemeId: Mapped[int] = mapped_column(INTEGER(11))
    CreatedBy: Mapped[int] = mapped_column(INTEGER(11))
    CreatedAt: Mapped[int] = mapped_column(INTEGER(11))
    CheckedOutBy: Mapped[int] = mapped_column(INTEGER(11), server_default=text("'0'"))
    Name: Mapped[Optional[str]] = mapped_column(VARCHAR(128))
    Alias: Mapped[Optional[str]] = mapped_column(VARCHAR(128))
    State: Mapped[Optional[int]] = mapped_column(INTEGER(1), server_default=text("'1'"))
    Type: Mapped[Optional[int]] = mapped_column(INTEGER(1))
    App_: Mapped[Optional[str]] = mapped_column('App', VARCHAR(32))
    Mod: Mapped[Optional[str]] = mapped_column(VARCHAR(32))
    Description: Mapped[Optional[str]] = mapped_column(TEXT)
    Level: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    Lft: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'1'"))
    Rgt: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'2'"))
    Link: Mapped[Optional[str]] = mapped_column(VARCHAR(196))
    Path: Mapped[Optional[str]] = mapped_column(VARCHAR(196))
    ViewingId: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    IsDefault: Mapped[Optional[int]] = mapped_column(INTEGER(1), server_default=text("'0'"))
    CheckedOutAt: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))
    Config: Mapped[Optional[str]] = mapped_column(TEXT)
    Ordering: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text("'0'"))

    User_: Mapped['User'] = relationship('User', back_populates='MenuItem')
    Menu_: Mapped['Menu'] = relationship('Menu', back_populates='MenuItem')
    Theme_: Mapped['Theme'] = relationship('Theme', back_populates='MenuItem')
    Viewing_: Mapped[List['Viewing']] = relationship('Viewing', secondary='MenuItemViewing', back_populates='MenuItem')


t_WidgetViewing = Table(
    'WidgetViewing', Base.metadata,
    Column('WidgetId', INTEGER(11), nullable=False),
    Column('ViewingId', INTEGER(11), nullable=False),
    ForeignKeyConstraint(['ViewingId'], ['Viewing.ViewingId'], name='fk_WidgetViewing_Viewing'),
    ForeignKeyConstraint(['WidgetId'], ['Widget.WidgetId'], name='fk_WidgetViewing_Widget'),
    Index('fk_WidgetViewing_ViewingId_idx', 'ViewingId'),
    Index('fk_WidgetViewing_WidgetId_idx', 'WidgetId')
)


t_MenuItemViewing = Table(
    'MenuItemViewing', Base.metadata,
    Column('MenuItemId', INTEGER(11), nullable=False),
    Column('ViewingId', INTEGER(11), nullable=False),
    ForeignKeyConstraint(['MenuItemId'], ['MenuItem.MenuItemId'], name='fk_MenuItemViewing_MenuItem'),
    ForeignKeyConstraint(['ViewingId'], ['Viewing.ViewingId'], name='fk_MenuItemViewing_Viewing'),
    Index('fk_MenuItemViewing_MenuItemId_idx', 'MenuItemId'),
    Index('fk_MenuItemViewing_ViewingId_idx', 'ViewingId')
)
