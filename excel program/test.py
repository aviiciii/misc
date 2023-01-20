from pandas import read_excel


def main():
    df = read_excel("input.xlsx")
    # print first row of input.xlsx
    print(df.iloc[1])
    print(df.iloc[[0, 1, 2, 3]])

    print(df['A'])
    print(df['A'].iloc[0])





if __name__ == "__main__":
    main()