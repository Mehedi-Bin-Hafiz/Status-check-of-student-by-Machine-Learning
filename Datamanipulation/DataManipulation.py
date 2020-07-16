import pandas as pd

Finaldatabes = pd.read_csv(r'../SecondaryDatabases/FinalStatusdata2.csv', index_col = False)
Predatabase = pd.read_csv(r'../SecondaryDatabases/PreStatusdata.csv', index_col = False)

 ############MainDatabase Generator###########

# submain= Finaldatabes[['Marks']]
# Predatabase.insert(12,"FinalMarks",submain,True)
# Predatabase.to_excel(r'../MainDatabase/MainDatabase.xlsx', index=False)

############MainDatabase Generator###########



