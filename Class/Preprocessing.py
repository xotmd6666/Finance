# 클래스 정의
class Finance_Preprocessing:    
    # 메서드 정의
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