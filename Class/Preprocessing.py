import pandas as pd
import numpy as np
import locale

class Finance_Preprocessing:    
    def stock(self, df):
        # 첫 번째 행, 열 삭제
        df = df.drop(0)
        df = df.drop('Unnamed: 0', axis = 1)

        # 인덱스의 데이터 타입을 문자형으로 변경
        df.index = df.index.astype(str)

        # 첫 번째 인덱스 명을 공백으로 변경
        df.index.values[0] = ''

        # 첫 번째 행을 컬럼명으로 변경 후 첫 번째 행 삭제
        df.columns = df.iloc[0]
        df = df.drop(df.index[0])

        # '날짜' 항목이 '계산 결과'로 되어 있는 행 삭제
        df = df[~(df['날짜'] == '계산 결과')]

        # 인덱스 재설정
        df = df.reset_index(drop=True)

        return df

    def fund(self, df):
        # 첫 번째 행을 컬럼명으로 변경 후 첫 번째 행 삭제
        df.columns = df.iloc[0]
        df = df.drop(df.index[0])

        # '투자원금' 항목이 비어 있는 행 삭제
        df = df.drop(df[df['투자원금'].isna() == True].index)

        return df

    def pension(self, df):
        # 인덱스의 데이터 타입을 문자형으로 변경
        df.index = df.index.astype(str)

        # 네 번째 인덱스 명을 공백으로 변경
        df.index.values[3] = ''

        # 네 번째 행을 컬럼명으로 변경 후 필요 없는 행 삭제
        df.columns = df.iloc[3]
        df = df.drop(df.index[0:4])

        # 인덱스 재설정
        df = df.reset_index(drop=True)

        return df

    def finance(self, df):
        # 열 이름의 데이터 타입을 문자형으로 변경
        df.columns = df.columns.astype(str)

        # 첫 번째 열 이름을 공백으로 변경
        df.columns.values[0] = ''

        # 첫 번째 컬럼 내 Cell 값을 index명으로 변경 후 첫 번째 열 삭제
        df.set_index(df.iloc[:, 0], inplace=True)
        df = df.drop(df.columns[0], axis = 1)

        # DataFrame 내 Cell 데이터 타입을 문자형에서 숫자형으로 변경
        df = df.astype(int)

        # 가져온 파일 내 숫자가 천 단위 구분 기호(,)가 있도록 변경
        def format_with_commas(value):
            locale.setlocale(locale.LC_ALL, '')  # 현재 시스템의 로케일 설정
            return locale.format_string('%d', value, grouping=True)
        df = df.map(format_with_commas)

        return df

class Risk_Asset_Preprocessing:    
    # 메서드 정의
    def intermediary_ISA_1(self, df):
        # 첫 번째 행, 열 삭제
        df = df.drop(0)
        df = df.drop('Unnamed: 0', axis = 1)

        # 인덱스의 데이터 타입을 문자형으로 변경
        df.index = df.index.astype(str)

        # 첫 번째 인덱스 명을 공백으로 변경
        df.index.values[0] = ''

        # 첫 번째 행을 컬럼명으로 변경 후 첫 번째 행 삭제
        df.columns = df.iloc[0]
        df = df.drop(df.index[0])

        # '날짜' 항목이 '계산 결과'로 되어 있는 행 삭제
        df = df[~(df['날짜'] == '계산 결과')]

        # 인덱스 재설정
        df = df.reset_index(drop=True)

        return df

    def intermediary_ISA_2(self, df):
        # 첫 번째 행, 열 삭제
        df = df.drop(0)
        df = df.drop('Unnamed: 0', axis = 1)

        # 인덱스의 데이터 타입을 문자형으로 변경
        df.index = df.index.astype(str)

        # 첫 번째 인덱스 명을 공백으로 변경
        df.index.values[0] = ''

        # 첫 번째 행을 컬럼명으로 변경 후 첫 번째 행 삭제
        df.columns = df.iloc[0]
        df = df.drop(df.index[0])

        # '평가 금액(원)' 항목이 0으로 되어 있는 행 삭제
        df = df[~(df['평가 금액(원)'] == 0)]

        # '종목 명' 항목 열 이름을 공백으로 설정
        df = df.rename(columns={'종목 명': ''})

        # '종목명' 항목으로 행 이름 설정
        df.set_index(df.iloc[:, 2], inplace=True)

        # '종목 명' 항목 삭제
        df = df.drop("", axis = 1)

        return df

    def overseas_stock_1(self, df):
        # 첫 번째 열 삭제
        df = df.drop('Unnamed: 0', axis = 1)

        # 인덱스의 데이터 타입을 문자형으로 변경
        df.index = df.index.astype(str)

        # 두 번째 인덱스 명을 공백으로 변경
        df.index.values[1] = ''

        # 두 번째 행을 컬럼명으로 변경 후 필요 없는 행 삭제
        df.columns = df.iloc[1]
        df = df.drop(df.index[1:3])

        # 인덱스 재설정
        df = df.reset_index(drop=True)

        return df

    def overseas_stock_2(self, df):
        # 첫 번째 열 삭제
        df = df.drop('Unnamed: 0', axis = 1)

        # 인덱스의 데이터 타입을 문자형으로 변경
        df.index = df.index.astype(str)

        # 두 번째 인덱스 명을 공백으로 변경
        df.index.values[1] = ''

        # 두 번째 행을 컬럼명으로 변경 후 필요 없는 행 삭제
        df.columns = df.iloc[1]
        df = df.drop(df.index[1])

        # '평가 금액($)' 항목이 0으로 되어 있는 행 삭제
        df = df[~(df['평가 금액($)'] == 0)]

        # '티커(Ticker)' 항목 열 이름을 공백으로 설정
        df = df.rename(columns={'티커(Ticker)': ''})

        # '종목명' 항목으로 행 이름 설정
        df.set_index(df.iloc[:, 2], inplace=True)

        # '종목 명' 항목 삭제
        df = df.drop("", axis = 1)

        return df

    def fund(self, df):
        # 인덱스의 데이터 타입을 문자형으로 변경
        df.index = df.index.astype(str)

        # 첫 번째 인덱스 명을 공백으로 변경
        df.index.values[0] = ''

        # 첫 번째 행을 컬럼명으로 변경 후 첫 번째 행 삭제
        df.columns = df.iloc[0]
        df = df.drop(df.index[0])

        return df