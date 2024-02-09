import pandas as pd
import numpy as np
from Class.Preprocessing import Finance_Preprocessing

# 파일 읽어오기

# 엑셀 파일 경로 설정
file_path = r'C:\Users\User\Desktop\Finance\investment_management'
# 각 자산 관리 파일 읽어오기
df_intermediary_ISA = pd.read_excel(file_path + r'\intermediary_ISA_account_management.xlsx', sheet_name = '자산 정리')
df_fund = pd.read_excel(file_path + r'\all_fund_management.xlsx', sheet_name = '전체 총계')
df_overseas_stock = pd.read_excel(file_path + r'\overseas_stock_management_v8.xlsx', sheet_name = '자산 정리')
df_pension = pd.read_excel(file_path + r'\pension_savings_account_management_v4.xlsm', sheet_name = '예수금 및 자산합계')

# 파일 전처리
pre = Finance_Preprocessing()
df_intermediary_ISA = pre.intermediary_ISA(df_intermediary_ISA)

# 필요한 데이터 수집

# iloc 인덱서를 사용하여 마지막 행의 특정 컬럼 값 가져오기
value_intermediary_ISA = df_intermediary_ISA.iloc[-1]['전체 자산 합계(원)']
print(value_intermediary_ISA)

# 재무 정리 파일 기록을 위한 데이터 정리