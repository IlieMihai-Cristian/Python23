import pandas as pd
# print(pd.__version__)
# var = {"x": 1, "y": 7, "z": 3}
# var_series = pd.Series(var)
# print(var_series)

# var_2 = [1, 4, 2]
# var_series = pd.Series(var_2)
# print(var_series)

# var_series = pd.Series(var, index=["x", "z"])
# print(var_series)

# data = {
#         "key1": [0, 1, 2],
#         "key2": [3, 4, 5]
# }
# var_3 = pd.DataFrame(data)
# print(var_3)

# var_3 = pd.DataFrame(data, index=['linia A', 'linia B', 'linia C'])
# print(var_3)

# print(var_3.loc['linia A'])
# print(var_3.loc['linia A', 'key2'])

# print(var_3.loc['linia B': 'linia C'])
# print(var_3.loc[['linia A', 'linia C']])


# taskuri = {
#         'zile': [2, 4, 5],
#         'durata': [50, 40, 45]
#         }

# var_df = pd.DataFrame(taskuri)
# print(var_df, 'inainte')
# taskuri['zile'][1] = 100
# print(taskuri)
# var_df.loc[1, 'zile'] = 100
# print(var_df, 'dupa')

# df = pd.read_excel('Curs_BNR_2023.xlsx')
# # print(df)
# for x in df.index:
#         # print(x)
#         # print(df.loc[x, 'EUR'])
#         if float(df.loc[x, 'EUR']) > 4.94:
#                 # df.drop(x, inplace=True)
#                 df.loc[x, 'EUR'] = 555
# df.to_csv('test_csv.csv')


""" Matricea de corelatie """
# df = pd.read_excel('Curs_BNR_2023.xlsx')
# df.drop(columns=df.columns[0], axis=1, inplace=True)
# print(df)
# print(df.corr())

""" descrierea tabelului """
df = pd.read_excel('Curs_BNR_2023.xlsx')
# print(df.describe())
df.describe().to_excel('Describe_BNR_2023.xlsx')

""" some atributes """
df = pd.read_csv('test.csv')
print(df)
# df.dropna(inplace=True)
# print(df)
# df.fillna(0, inplace=True)
# print(df)
# df.loc[7, 'AL'] = 45
# print(df)
# df.replace(':', 0, inplace=True)
# df.replace(': ', 0, inplace=True)
# print(df)
print(df.transpose())
df.transpose().to_excel('test1.xlsx')