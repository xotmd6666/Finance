import pandas as pd
import numpy as np
import locale

class Risk_Asset_Calculate:    
    def intermediary_ISA_domestic(self, df):
        value_1 = df.loc['삼성전자']['평가 금액(원)']

        value = value_1

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

    def overseas_stock_advanced(self, df):
        value_1 = df.loc['SPY']['평가 금액($)']
        value_2 = df.loc['QQQ']['평가 금액($)']
        value_3 = df.loc['ICLN']['평가 금액($)']
        value_4 = df.loc['ARKK']['평가 금액($)']
        value_5 = df.loc['XLV']['평가 금액($)']
        value_6 = df.loc['SCHD']['평가 금액($)']
        value_7 = df.loc['TQQQ']['평가 금액($)']
        value_8 = df.loc['JEPQ']['평가 금액($)']

        value = int(round((value_1 + value_2 + value_3 + value_4 + value_5 + value_6 + value_7 + value_8) * df.iloc[0]['평균 매수 단가\n기준 기대 수익금(원)'], 0))

        return value

    def overseas_stock_emerging(self, df):
        value_1 = df.loc['INDA']['평가 금액($)']
        value_2 = df.loc['MCHI']['평가 금액($)']

        value = int(round((value_1 + value_2) * df.iloc[0]['평균 매수 단가\n기준 기대 수익금(원)'], 0))

        return value