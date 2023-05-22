import pandas as pd

def main():
    df = pd.read_csv('gender2.csv', encoding='cp949', index_col=0)
    
    new_df = df[['2022년_계_총인구수','2022년_남_총인구수', '2022년_여_총인구수']]
    
    new_df.columns = ['Total','Male', 'Female']
    
    print(new_df)

if __name__ == '__main__':
    main()
