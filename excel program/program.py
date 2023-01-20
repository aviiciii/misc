from pandas import read_excel


def main():
    # read input.xlsx
    try:
        df = read_excel("input.xlsx")
    except:
        print("Error: input.xlsx not found")
        return
    
    # create empty lists
    tm, qopt, qt, qu, eff=[], [], [], [], []
    


    for i in range(0, len(df)):
        
        # compute tm
        temp_tm = (df['inlet'].iloc[i] + df['outlet'].iloc[i]) / 2
        tm.append(round(temp_tm))
        
        # compute qopt
        temp_qopt = df['insol'].iloc[i] - df['Qa'].iloc[i]
        qopt.append(round(temp_qopt))

        # compute qt
        temp_qt = 3 * ( temp_tm - 35 )
        qt.append(round(temp_qt))

        # compute qu
        temp_qu = df['Qa'].iloc[i] - temp_qt
        qu.append(round(temp_qu))

        # compute eff
        temp_eff = temp_qu / df['insol'].iloc[i]
        eff.append(round(temp_eff))

    
    # add new columns to dataframe
    df['Tm'] = tm
    df['Qopt'] = qopt
    df['Qt'] = qt
    df['Qu'] = qu
    df['Eff'] = eff

    # write output.xlsx
    try:
        df.to_excel("output.xlsx", index=False)
    except:
        print("Error: Error in writing output.xlsx")
        return
    print("Done")



if __name__ == "__main__":
    main()