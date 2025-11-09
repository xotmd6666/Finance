import pandas as pd
import numpy as np
from datetime import date
import locale
from Class.Preprocessing import Risk_Asset_Preprocessing
from Class.Calculate import Risk_Asset_Calculate

# ----------파일 읽어오기----------
# 엑셀 파일 경로 설정
file_path = r'C:\Users\User\Desktop\Finance\investment_management'
# 각 자산 관리 파일 읽어오기
df_intermediary_ISA_1 = pd.read_excel(file_path + r'\intermediary_ISA_account_management.xlsx', sheet_name = '자산 정리')
df_intermediary_ISA_2 = pd.read_excel(file_path + r'\intermediary_ISA_account_management.xlsx', sheet_name = '보유 주식')
df_overseas_stock_1 = pd.read_excel(file_path + r'\overseas_stock_management_v9.xlsx', sheet_name = '자산 정리')
df_overseas_stock_2 = pd.read_excel(file_path + r'\overseas_stock_management_v9.xlsx', sheet_name = '보유 종목 현황')
df_fund_1 = pd.read_excel(file_path + r'\all_fund_management.xlsx', sheet_name = '해외 선진국 펀드')
df_fund_2 = pd.read_excel(file_path + r'\all_fund_management.xlsx', sheet_name = '해외 신흥국 펀드')
df_pension_1 = pd.read_excel(file_path + r'\pension_savings_account_management_v5.xlsm', sheet_name = '예수금 및 자산합계')
df_pension_2 = pd.read_excel(file_path + r'\pension_savings_account_management_v5.xlsm', sheet_name = '나스닥(키움)')
df_pension_3 = pd.read_excel(file_path + r'\pension_savings_account_management_v5.xlsm', sheet_name = 'S&P(키움)')
df_pension_4 = pd.read_excel(file_path + r'\pension_savings_account_management_v5.xlsm', sheet_name = 'CSI300(키움)')
df_pension_5 = pd.read_excel(file_path + r'\pension_savings_account_management_v5.xlsm', sheet_name = '펀드(키움)')
df_pension_6 = pd.read_excel(file_path + r'\pension_savings_account_management_v5.xlsm', sheet_name = 'S&P(미래에셋)')
df_finance = pd.read_excel(r'C:\Users\User\Desktop\Finance\Monthly_Asset_Managemenet_v4.xlsx', sheet_name = '위험자산 월별 자산 금액(국가별)')

# ----------파일 전처리----------
pre = Risk_Asset_Preprocessing()
df_intermediary_ISA_1 = pre.intermediary_ISA_1(df_intermediary_ISA_1)
df_intermediary_ISA_2 = pre.intermediary_ISA_2(df_intermediary_ISA_2)
df_overseas_stock_1 = pre.overseas_stock_1(df_overseas_stock_1)
df_overseas_stock_2 = pre.overseas_stock_2(df_overseas_stock_2)
df_fund_1 = pre.fund(df_fund_1)
df_fund_2 = pre.fund(df_fund_2)
df_pension_1 = pre.pension(df_pension_1)
df_finance = pre.finance(df_finance)

# ----------필요한 데이터 수집----------
cal = Risk_Asset_Calculate()
# 중개형ISA
value_intermediary_ISA_domestic = cal.intermediary_ISA_domestic(df_intermediary_ISA_2)
value_intermediary_ISA_advanced = cal.intermediary_ISA_advanced(df_intermediary_ISA_2)
value_intermediary_ISA_emerging = cal.intermediary_ISA_emerging(df_intermediary_ISA_2)
value_intermediary_ISA_deposit = df_intermediary_ISA_1.iloc[-1]['예수금(원)']
# 해외 주식
value_overseas_stock_deposit = int(round(df_overseas_stock_1.iloc[-1]['예수금(원)'] + df_overseas_stock_1.iloc[-1]['예수금($)'] * df_overseas_stock_1.iloc[0]['전체 자산 합계(원)'], 0))
value_overseas_stock_advanced = cal.overseas_stock_advanced(df_overseas_stock_2)
value_overseas_stock_emerging = cal.overseas_stock_emerging(df_overseas_stock_2)
# 펀드
value_fund_advanced = df_fund_1.iloc[-1]['평가금액']
value_fund_emerging = df_fund_2.iloc[-1]['평가금액']
# 연금저축
value_pension_deposit = df_pension_1.iloc[-1]['D+2(원)']
value_pension_advanced = df_pension_2.loc[3]['Unnamed: 2'] + df_pension_3.loc[3]['Unnamed: 2'] + df_pension_6.loc[3]['Unnamed: 2']
value_pension_emerging = df_pension_4.loc[3]['Unnamed: 2']
value_pension_advanced_fund = int(round(df_pension_5.loc[3]['Unnamed: 2'], 0))


# ----------재무 정리 파일 기록을 위한 데이터 정리----------
# 오늘 날짜 가져오기
today = date.today()

# 기존 컬럼 형식과 동일한 형식으로 변경
formatted_date = today.strftime("%Y.%m")
month_expression = '(월)'
insert_column_name = formatted_date + month_expression

# 재무 정리 파일에 새로운 열 생성
df_finance[insert_column_name] = np.nan
df_finance = df_finance.fillna('')

# Replace empty strings or whitespace-only strings with NaN, fill NaN with 0, and convert to integers
df_finance = df_finance.replace({'^\s*$': np.nan}, regex=True)  # Replace empty/whitespace strings with NaN
df_finance = df_finance.fillna(0)                              # Replace NaN with 0
df_finance = df_finance.astype(int)                            # Convert to integers

# 수집한 값 입력
# 국내
df_finance.at['주식(중개형ISA)_국내', insert_column_name] = value_intermediary_ISA_domestic
# 선진국
df_finance.at['적립식 펀드_선진국', insert_column_name] = value_fund_advanced
df_finance.at['주식_선진국', insert_column_name] = value_overseas_stock_advanced
df_finance.at['연금저축(ETF)_선진국', insert_column_name] = value_pension_advanced
df_finance.at['연금저축(펀드)_선진국', insert_column_name] = value_pension_advanced_fund
df_finance.at['주식(중개형ISA)_선진국', insert_column_name] = value_intermediary_ISA_advanced
# 신흥국
df_finance.at['적립식 펀드_신흥국', insert_column_name] = value_fund_emerging
df_finance.at['주식_신흥국', insert_column_name] = value_overseas_stock_emerging
df_finance.at['연금저축_신흥국', insert_column_name] = value_pension_emerging
df_finance.at['주식(중개형ISA)_신흥국', insert_column_name] = value_intermediary_ISA_emerging
# 예수금
df_finance.at['주식(중개형ISA)_예수금', insert_column_name] = value_intermediary_ISA_deposit
df_finance.at['해외주식_예수금', insert_column_name] = value_overseas_stock_deposit
df_finance.at['연금저축_예수금', insert_column_name] = value_pension_deposit

# 소수점 0번째 자리까지 나타내기
df_finance[insert_column_name] = df_finance[insert_column_name].map('{:.0f}'.format)

# 데이터 타입을 문자형에서 숫자형으로 변경
df_finance = df_finance.astype(int)

# 가져온 파일 내 숫자가 천 단위 구분 기호(,)가 있도록 변경
def format_with_commas(value):
    locale.setlocale(locale.LC_ALL, '')  # 현재 시스템의 로케일 설정
    return locale.format_string('%d', value, grouping=True)
df_finance = df_finance.map(format_with_commas)

with pd.ExcelWriter('output.xlsx', mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
    # 데이터프레임을 새로운 시트에 추가
    df_finance.to_excel(writer, sheet_name='위험자산 월별 자산 금액(국가별)', index=True)

# 코드 실행 완료 알림
print('Code run completion')