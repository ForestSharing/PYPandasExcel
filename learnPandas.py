import pandas as pd


def main():
    learnSeriesOne = pd.Series([1,'aa',3,4,5])
    print('learnSeriesOne=\n',learnSeriesOne)

    learnSeriesTwo = pd.Series([1,2,4,'Aa','Bb'],index=['one','two','three','4','five'])
    print('learnserivesTwo=\n',learnSeriesTwo)
    print('the learnseriesTwo index three is ',learnSeriesTwo['three'])
    print('the learnseriesTwo all index is',learnSeriesTwo.index)
    
    obj = learnSeriesTwo.to_dict
    print(obj)

    sdata = {"Ohio": 35000, "Texas": 71000, "Oregon": 16000, "Utah": 5000}
    states = ["California", "Ohio", "Oregon", "Texas"]

    obj2 = pd.Series(sdata,index=states)
    print(obj2)

    # DataFrame
    data = {"state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada", "Nevada"],
        "year": [2000, 2001, 2002, 2001, 2002, 2003],
        "pop": [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
    frame = pd.DataFrame(data)
    print(frame)

    frame2=pd.DataFrame(data, columns=["year", "state", "pop"])
    print(frame2)

    print('frame year is =======================================\n ',frame['year'])
    print('frame year is =======================================\n ',frame.year)

    print('frame the one row ======================================= \n',frame.loc[1])
    print('frame the one row ======================================= \n',frame.iloc[1])

    print('frame the one columns =======================================  \n',frame['year'])
    print('frame the one columns ======================================= \n',frame['year']==2001)


    opulations = {"Ohio": {2000: 1.5, 2001: 1.7, 2002: 3.6},
                   "Nevada": {2001: 2.4, 2002: 2.9}}
    frame3 = pd.DataFrame(opulations)
    print('dictionary format dataframe is==========================================  \n',frame3)
    
    # essential functionality  under ==============================

    



if __name__ == '__main__':
    main()
    
