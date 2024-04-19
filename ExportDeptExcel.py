import pandas as pd

file_path = 'ITSM.xlsx'  # 替换为你的Excel文件路径  
sheet_name = 'alldata'  # 替换为正确的工作表名  
df = pd.read_excel(file_path, sheet_name=sheet_name)  
print(df)

overall_avg_duration=df.groupby('流程')['AVG_TIME'].mean().reset_index(name='业务总体平均办理时长（天）')  
print(overall_avg_duration)
afterdf = pd.merge(df,overall_avg_duration,on='流程',how='left')

afterdf['差值']=afterdf['AVG_TIME']*24-afterdf['业务总体平均办理时长（天）']*24
afterdf['AVG_TIME']=afterdf['AVG_TIME']*24
afterdf['业务总体平均办理时长（天）']=afterdf['业务总体平均办理时长（天）']*24

afterdf = afterdf.rename(columns={'USER':'用户','FLOWNAME':'流程名称','DUR_DATE':'办理时长（小时）','业务总体平均办理时长（天）':'平均用时'})
output_file_path = 'j02.xlsx'  # 输出文件的路径  
afterdf.to_excel(output_file_path, index=True)
