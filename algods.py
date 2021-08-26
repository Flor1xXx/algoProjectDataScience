import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Space_Corrected.csv')

print(df.info())

# print(df['Status Mission'].value_counts())
# print(df['Company Name'].value_counts())

# a = pd.isnull(df['Company Name'])
# print(len(df[a]))

def suc_com():

	df_filtered = df[(df['Status Mission'] == 'Success')]
	
	count_suc = df_filtered['Company Name'].value_counts()
	count_all = df['Company Name'].value_counts()


	sl = {'All': count_all,
		  'Success': count_suc}


	df1 = pd.DataFrame(sl)
	df1['Success'].fillna(0, inplace= True)
	df1['Coefficient'] = df1['Success'] / df1['All'] *100
	df1['Success'], df1['Coefficient'] = df1['Success'].apply(int), df1['Coefficient'].apply(int)

	df2 = df1[df1['All'] > 10]

	sort = df2.sort_values(by='Coefficient')

	sort['Coefficient'].plot(kind= 'bar')
	plt.show()


suc_com()