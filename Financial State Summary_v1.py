import pandas as pd
import numpy as np
from datetime import date
import locale
from Class.Preprocessing import Finance_Preprocessing

# ----------파일 읽어오기----------
file_path = r'C:\Users\User\Desktop\Finance\investment_management'
df_intermediary_ISA = pd.read_excel(file_path + r'\intermediary_ISA_account_management.xlsx', sheet_name='자산 정리')
df_overseas_stock = pd.read_excel(file_path + r'\overseas_stock_management_v8.xlsx', sheet_name='자산 정리')
df_fund = pd.read_excel(file_path + r'\all_fund_management.xlsx', sheet_name='전체 총계')
df_pension = pd.read_excel(file_path + r'\pension_savings_account_management_v5.xlsm', sheet_name='예수금 및 자산합계')
df_gold = pd.read_excel(file_path + r'\(dollar,gold,cryptocurrency,the_yen)_finance.xlsx', sheet_name='금')
df_crytocurrency = pd.read_excel(file_path + r'\(dollar,gold,cryptocurrency,the_yen)_finance.xlsx', sheet_name='가상화폐')
df_yen = pd.read_excel(file_path + r'\(dollar,gold,cryptocurrency,the_yen)_finance.xlsx', sheet_name='엔화')
df_finance = pd.read_excel(r'C:\Users\User\Desktop\Finance\Monthly_Asset_Managemenet_v4.xlsx', sheet_name='월별 자산 금액')

# ----------파일 전처리----------
pre = Finance_Preprocessing()
df_intermediary_ISA = pre.stock(df_intermediary_ISA)
df_overseas_stock = pre.stock(df_overseas_stock)
df_fund = pre.fund(df_fund)
df_pension = pre.pension(df_pension)
df_finance = pre.finance(df_finance)

# ----------필요한 데이터 수집----------
value_intermediary_ISA = df_intermediary_ISA.iloc[-1]['전체 자산 합계(원)']
value_overseas_stock = int(round(df_overseas_stock.iloc[-1]['전체 자산 합계(원)'], 0))
value_fund = df_fund.loc[df_fund.index[-1], '평가금액']
value_pension = df_pension.loc[df_pension.index[-1], '날짜별 전체 자산 합계(원)']
value_gold = df_gold.iloc[-1]['Unnamed: 2']
value_crytocurrency = df_crytocurrency.iloc[-1]['Unnamed: 2']
value_yen = df_yen.iloc[-1]['Unnamed: 7']

# ----------재무 정리 파일 기록을 위한 데이터 정리----------
today = date.today()
formatted_date = today.strftime("%Y.%m") + '(월)'

df_finance[formatted_date] = np.nan
df_finance.fillna('', inplace=True)

# 천 단위 구분 기호 제거 후 숫자형 변환
def convert_to_int(value):
    try:
        return int(str(value).replace(',', '')) if isinstance(value, str) and value.strip().replace(',', '').isdigit() else value
    except ValueError:
        return value

df_finance = df_finance.map(convert_to_int)

df_finance.replace({'^\s*$': np.nan}, regex=True, inplace=True)
df_finance.fillna(0, inplace=True)
df_finance = df_finance.astype(int, errors='ignore')

df_finance.at['적립식 펀드', formatted_date] = value_fund
df_finance.at['국내 주식(중개형ISA)', formatted_date] = value_intermediary_ISA
df_finance.at['해외 주식', formatted_date] = value_overseas_stock
df_finance.at['연금저축', formatted_date] = value_pension
df_finance.at['금 현물(krx 금 계좌)', formatted_date] = value_gold
df_finance.at['가상화폐', formatted_date] = value_crytocurrency
df_finance.at['엔화(우리은행 외화보통예금)', formatted_date] = value_yen

# 숫자를 천 단위 구분 기호(,)가 있는 문자열로 변환
def format_with_commas(value):
    try:
        return f"{int(value):,}"
    except (ValueError, TypeError):
        return value

df_finance = df_finance.map(format_with_commas)

# 엑셀 파일 저장
df_finance.to_excel('output.xlsx', sheet_name='월별 자산 금액')

print('Code run completion')