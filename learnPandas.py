import pandas as pd
import numpy as np


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

    print('frame year is =================================================\n ',frame['year'])
    print('frame year is =================================================\n ',frame.year)

    print('frame the one row ============================================ \n',frame.loc[1])
    print('frame the one row ============================================ \n',frame.iloc[1])

    print('frame the one columns ========================================  \n',frame['year'])
    print('frame the one columns ======================================== \n',frame['year']==2001)


    opulations = {"Ohio": {2000: 1.5, 2001: 1.7, 2002: 3.6},
                   "Nevada": {2001: 2.4, 2002: 2.9}}
    frame3 = pd.DataFrame(opulations)
    print('dictionary format dataframe is==========================================  \n',frame3)
    
    #   essential functionality  under ============================================


    #   Data Aggregation and Group Operations======================================


        #     key1  key2  data1  data2
        # 0     a     1     10    100
        # 1     a     2     20    200
        # 2  None     1     30    300
        # 3     b     2     40    400
        # 4     b     1     50    500
        # 5     a  <NA>     60    600
        # 6  None     1     70    700

    df = pd.DataFrame({"key1" : ["a", "a", None, "b", "b", "a", None],
                       "key2" : pd.Series([1, 2, 1, 2, 1, None, 1],
                                          dtype="Int64"),
                       "data1" : [10,20,30,40,50,60,70],
                       "data2" : [100,200,300,400,500,600,700]})
    print('==============================this is aggregation and group ===============')
    print(df)

    means = df['data1'].groupby([df['key1'],df['key2']]).mean()
    print('=======================')
    print(means)

    mytest = df.groupby(([df['key1'],df['key2']])).mean()
    print(mytest)
    
    mytest2 = df.groupby(df['key1']).mean()
    print(mytest2)

    print('==========for i,j in df.groupby(\'key1\'):=================================')
    for i,j in df.groupby('key1'):
        print(i)
        print(j)
    print('=============for(i,j),k in df.groupby([\'key1\',\'key2\']): ================')
    for(i,j),k in df.groupby(['key1','key2']):
        print((i,j))
        print(k)
    print('============test4==========')
    test4 = df     
    test4.loc[0,'data1']=20
    print(test4)
    for(i,j,m),k in test4.groupby(['key1','key2','data1']):
        print((i,j,m))
        print(k)

    print('============================test5==========================================')
    test5 = pd.DataFrame({"key1" :['a','a','a','b','b','a'],
                       "key2" : [1,6,2,1,2,1],
                       'key3':[5,6,7,4,9,5],
                       'key4':[30,40,50,60,70,80]})   
    print(test5)
    # this is test5
    #     key1  key2  key3  key4
    # 0    a     1     5    30
    # 1    a     6     6    40
    # 2    a     2     7    50
    # 3    b     1     4    60
    # 4    b     2     9    70
    # 5    a     1     5    80


    for k in test5.groupby(['key1','key2','key3']):
        print(k)


    print('=================Data Aggregation===========================================')
    
    print(test5["key2"].nsmallest(2))
    print('this is test describe ====\n')
    print(test5.describe())
    
    test6 = test5.groupby('key1')
    print('this is test6 ====\n',test6)
    test7 = test6.agg(testFun)
    print('this is test7 \n',test7)


def testFun(arr):
    return arr.max()-arr.min()

if __name__ == '__main__':
    main()
    