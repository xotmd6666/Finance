import pandas as pd
import numpy as np
from datetime import date
import locale
from Class.Preprocessing import Finance_Preprocessing

# ----------파일 읽어오기----------
# 엑셀 파일 경로 설정
file_path = r'C:\Users\User\Desktop\Finance\investment_management'
# 각 자산 관리 파일 읽어오기
df_intermediary_ISA = pd.read_excel(file_path + r'\intermediary_ISA_account_management.xlsx', sheet_name = '자산 정리')
df_overseas_stock = pd.read_excel(file_path + r'\overseas_stock_management_v8.xlsx', sheet_name = '자산 정리')
df_fund = pd.read_excel(file_path + r'\all_fund_management.xlsx', sheet_name = '전체 총계')
df_pension = pd.read_excel(file_path + r'\pension_savings_account_management_v4.xlsm', sheet_name = '예수금 및 자산합계')
df_gold = pd.read_excel(file_path + r'\(dollar,gold,cryptocurrency,the_yen)_finance.xlsx', sheet_name = '금')
df_crytocurrency = pd.read_excel(file_path + r'\(dollar,gold,cryptocurrency,the_yen)_finance.xlsx', sheet_name = '가상화폐')
df_yen = pd.read_excel(file_path + r'\(dollar,gold,cryptocurrency,the_yen)_finance.xlsx', sheet_name = '엔화')
df_finance = pd.read_excel(r'C:\Users\User\Desktop\Finance\Monthly_Asset_Managemenet_v4.xlsx', sheet_name = '월별 자산 금액')

# ----------파일 전처리----------
pre = Finance_Preprocessing()
df_intermediary_ISA = pre.stock(df_intermediary_ISA)
df_overseas_stock = pre.stock(df_overseas_stock)
df_fund = pre.fund(df_fund)
df_pension = pre.pension(df_pension)
df_finance = pre.finance(df_finance)

# ----------필요한 데이터 수집----------
# loc/iloc 인덱서를 사용하여 마지막 행의 특정 컬럼 값 가져오기
value_intermediary_ISA = df_intermediary_ISA.iloc[-1]['전체 자산 합계(원)']
value_overseas_stock = int(round(df_overseas_stock.iloc[-1]['전체 자산 합계(원)'], 0))
value_fund = df_fund.loc[df_fund.index[-1], '평가금액']
value_pension = df_pension.loc[df_pension.index[-1], '날짜별 전체 자산 합계(원)']
value_gold = df_gold.iloc[-1]['Unnamed: 2']
value_crytocurrency = df_crytocurrency.iloc[-1]['Unnamed: 2']
value_yen = df_yen.iloc[-1]['Unnamed: 7']

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

# 천 단위 표시용 쉼표(,) 제거 후 데이터 타입을 숫자형으로 변경
df_finance = df_finance.map(lambda x: x.replace(',', '') if isinstance(x, str) else x)

# 문자형 공백을 숫자형 공백으로 변환
pd.set_option('future.no_silent_downcasting', True)
df_finance = df_finance.replace({'^\\s*$': np.nan}, regex=True)
df_finance = df_finance.fillna(0).astype(int)  
df_finance = df_finance.replace({'^\\s*$': np.nan}, regex=True).astype(int)

# 데이터 타입을 문자형에서 숫자형으로 변경
df_finance = df_finance.astype(int)

# 수집한 값 입력
df_finance.at['적립식 펀드', insert_column_name] = value_fund
df_finance.at['국내 주식(중개형ISA)', insert_column_name] = value_intermediary_ISA
df_finance.at['해외 주식', insert_column_name] = value_overseas_stock
df_finance.at['연금저축', insert_column_name] = value_pension
df_finance.at['금 현물(krx 금 계좌)', insert_column_name] = value_gold
df_finance.at['가상화폐', insert_column_name] = value_crytocurrency
df_finance.at['엔화(우리은행 외화보통예금)', insert_column_name] = value_yen

# 소수점 0번째 자리까지 나타내기
df_finance[insert_column_name] = df_finance[insert_column_name].map('{:.0f}'.format)

# 데이터 타입을 문자형에서 숫자형으로 변경
df_finance = df_finance.astype(int)

# 가져온 파일 내 숫자가 천 단위 구분 기호(,)가 있도록 변경
def format_with_commas(value):
    locale.setlocale(locale.LC_ALL, '')  # 현재 시스템의 로케일 설정
    return locale.format_string('%d', value, grouping=True)
df_finance = df_finance.map(format_with_commas)

# 엑셀 파일에 입력
df_finance.to_excel('output.xlsx', sheet_name = '월별 자산 금액')

# 코드 실행 완료 알림
print('Code run completion') 