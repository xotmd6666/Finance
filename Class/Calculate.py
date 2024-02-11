import pandas as pd
import numpy as np
import locale

class Risk_Asset_Calculate:    
    def intermediary_ISA_domestic(self, df):
        value_1 = df.loc['NAVER']['평가 금액(원)']
        value_2 = df.loc['카카오']['평가 금액(원)']
        value_3 = df.loc['삼성전자']['평가 금액(원)']
        value_4 = df.loc['SK하이닉스']['평가 금액(원)']
        value_5 = df.loc['레인보우로보틱스']['평가 금액(원)']
        value_6 = df.loc['두산로보틱스']['평가 금액(원)']

        value = value_1 + value_2 + value_3 + value_4 + value_5 + value_6

        return value

    def intermediary_ISA_advanced(self, df):
        value_1 = df.loc['TIGER 미국S&P500']['평가 금액(원)']
        value_2 = df.loc['TIGER 미국나스닥100']['평가 금액(원)']
        value_3 = df.loc['KODEX 미국S&P500(H)']['평가 금액(원)']
        value_4 = df.loc['KODEX 미국나스닥100(H)']['평가 금액(원)']

        value = value_1 + value_2 + value_3 + value_4

        return value

    def intermediary_ISA_emerging(self, df):
        value_1 = df.loc['TIGER 차이나CSI300']['평가 금액(원)']
        value_2 = df.loc['KOSEF 인도Nifty50(합성)']['평가 금액(원)']

        value = value_1 + value_2

        return value