import pandas as pd

def main():
    data = {'unit price': [1000, 280, 900],
            'number': [25, 120, 30]}
    
    df = pd.DataFrame(data, index=['store1', 'store2', 'store3'])
    print('[Input Data]')
    print(df)
    print()
    
    df['total price'] = df['unit price'] * df['number']
    print('[Add Total Price]')
    print(df)
    print()
    
    sorted_df = df.sort_values('total price', ascending=False)
    top_2 = sorted_df.head(2)
    
    print('[Top 2]')
    print(top_2)

if __name__ == '__main__':
    main()
