import pandas as pd
import numpy as np
from datetime import date
from Class.Preprocessing import Risk_Asset_Preprocessing
from Class.Calculate import Risk_Asset_Calculate

# ----------파일 읽어오기----------
# 엑셀 파일 경로 설정
file_path = r'C:\Users\User\Desktop\Finance\investment_management'
# 각 자산 관리 파일 읽어오기
df_intermediary_ISA_1 = pd.read_excel(file_path + r'\intermediary_ISA_account_management.xlsx', sheet_name = '자산 정리')
df_intermediary_ISA_2 = pd.read_excel(file_path + r'\intermediary_ISA_account_management.xlsx', sheet_name = '보유 주식')
df_overseas_stock_1 = pd.read_excel(file_path + r'\overseas_stock_management_v8.xlsx', sheet_name = '자산 정리')
df_overseas_stock_2 = pd.read_excel(file_path + r'\overseas_stock_management_v8.xlsx', sheet_name = '보유 종목 현황')
df_fund_1 = pd.read_excel(file_path + r'\all_fund_management.xlsx', sheet_name = '해외 선진국 펀드')
df_fund_2 = pd.read_excel(file_path + r'\all_fund_management.xlsx', sheet_name = '해외 신흥국 펀드')
df_pension = pd.read_excel(file_path + r'\pension_savings_account_management_v4.xlsm', sheet_name = '예수금 및 자산합계')
df_finance = pd.read_excel(r'C:\Users\User\Desktop\Finance\Monthly_Asset_Managemenet_v3.xlsx', sheet_name = '월별 자산 금액')

# ----------파일 전처리----------
pre = Risk_Asset_Preprocessing()
df_intermediary_ISA_1 = pre.intermediary_ISA_1(df_intermediary_ISA_1)
df_intermediary_ISA_2 = pre.intermediary_ISA_2(df_intermediary_ISA_2)
df_overseas_stock_1 = pre.overseas_stock_1(df_overseas_stock_1)
df_overseas_stock_2 = pre.overseas_stock_2(df_overseas_stock_2)
df_fund_1 = pre.fund(df_fund_1)
df_fund_2 = pre.fund(df_fund_2)
# df_pension = pre.pension(df_pension)
# df_finance = pre.finance(df_finance)

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
