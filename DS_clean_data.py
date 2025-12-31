import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns   # type: ignore


df=pd.read_csv("F:/python/numpy/DS_job_project/Uncleaned_DS_jobs.csv")

df['Salary Estimate']=df['Salary Estimate'].apply(lambda x:x.split('(')[0])
df['Salary Estimate']=df['Salary Estimate'].str.replace('$','').str.replace('K','000')

df['Min_salary']=df['Salary Estimate'].apply(lambda x:int(x.split('-')[0]))
df['Max_salary']=df['Salary Estimate'].apply(lambda x:int(x.split('-')[1]))
df['Avg_salary']=(df['Min_salary']+df['Max_salary'])/2


df['Company Name']=df.apply(lambda x:x['Company Name'][:-3] if x['Rating'] != -1 else x['Company Name'] ,axis=1)
df['Company Name']=df['Company Name'].str.strip()

df['Job_state']=df['Location'].apply(lambda x:x.split(',')[0])
df['Job_state']=df['Job_state'].apply(lambda x:'Remote' if x.lower() == 'remote' else x)

df['Age']=df['Founded'].apply(lambda x:x if x<1 else 2025-x)

df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df['r_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
df['spark_yn'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df['aws_yn'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df['excel_yn'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df['sql_yn'] = df['Job Description'].apply(lambda x: 1 if 'sql' in x.lower() else 0)

cols_to_drop = ['Job Description', 'Salary Estimate', 'Location','index','Headquarters']
df = df.drop(columns=cols_to_drop)

cols_to_clean = ['Size', 'Type of ownership', 'Industry', 'Sector', 'Revenue', 'Competitors']
for col in cols_to_clean:
    df[col] = df[col].apply(lambda x: 'Unknown' if x == '-1' or x == -1 else x)

df = df.replace(['Unknown / Non-Applicable', '-1', -1], np.nan)

# df.to_csv('F:/python/numpy/DS_job_project/clean_data1.csv',index=False)
print(df['Revenue']) 

print(df.head(10))

#--data visulation---:
top_10_companies = df['Company Name'].value_counts().index[:10]
df_top = df[df['Company Name'].isin(top_10_companies)]

sns.barplot(x='Company Name', y='Rating', data=df_top)
plt.xticks(rotation=90,fontsize=10)

sns.histplot(df['Revenue'],kde=True)
plt.xticks(rotation=90,fontsize=10)
plt.tight_layout()

top_5=df['Job Title'].value_counts().index[:5]
value=df[df['Job Title'].isin(top_5)]
sns.violinplot(x='Job Title',y='Avg_salary',data=value,palette='coolwarm')
plt.xticks(rotation=45,fontsize=7.5)
plt.tight_layout()

skills=['python_yn','r_yn','spark_yn','aws_yn','excel_yn','sql_yn']
df['total_skils']=df[skills].sum(axis=1)
sector_skils=df.groupby('Job Title')['total_skils'].sum().sort_values(ascending=False).head(5)
plt.pie(sector_skils,autopct='%1.1f%%',startangle=140,colors=sns.color_palette('viridis'))
plt.pie(
    sector_skils, 
    labels=sector_skils.index, 
    autopct='%1.1f%%',      # Shows the percentage on the slice
    startangle=140,         # Rotates the start of the chart
    colors=sns.color_palette('viridis'), # Using a nice seaborn palette
    pctdistance=0.85    
        # Distance of the percentage text from center
)
plt.legend(bbox_to_anchor=(1.02, 1),loc='upper left')
plt.tight_layout()
plt.show()

