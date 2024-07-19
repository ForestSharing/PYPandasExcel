import pandas as pd

file_path = 'OA  发领导.xlsx'  # 替换为你的Excel文件路径  
sheet_name = '5月份清单'  # 替换为正确的工作表名  
df = pd.read_excel(file_path, sheet_name=sheet_name)  
print(df)

print("###############################################")

print(df[df['是否待阅']=='待办'])

daibanDF = df[df['是否待阅']=='待办']
daiyueDF = df[df['是否待阅']=='待阅']


print("&&&&&&&&&&&&&&&&&&&")
bumendf = df[['办理用户','办理部门']].drop_duplicates() 
print(bumendf)
print("&&&&&&&&&&&&&&&&&&&")
zongshichangdf =  daibanDF.groupby('办理用户')['计算小时'].sum().reset_index(name='总待办时长')
daibanshuliang  = daibanDF.groupby('办理用户')['计算小时'].count().reset_index(name='总待办数')


zongdaiyuedf =  daiyueDF.groupby('办理用户')['计算小时'].sum().reset_index(name='总待阅时长')
daiyueshuliang  = daiyueDF.groupby('办理用户')['计算小时'].count().reset_index(name='总待阅数量')

afterdaibandf =  pd.merge(zongshichangdf,daibanshuliang,left_on='办理用户',right_on='办理用户')
afterdaiyuedf = pd.merge(zongdaiyuedf,daiyueshuliang,left_on='办理用户',right_on='办理用户')

t = pd.merge(afterdaibandf,afterdaiyuedf,left_on='办理用户',right_on='办理用户')

afteralldf = pd.merge(t,bumendf,left_on='办理用户',right_on='办理用户')
print(afteralldf)
output_file_path = 'j06.xlsx'  # 输出文件的路径  
afteralldf.groupby('办理用户').sum().to_excel(output_file_path, index=True)




print('test')
