import pandas as pd

Finaldatabes = pd.read_csv(r'../ResultsDatabase/FinalStatusdata2.csv', index_col = False)
Predatabase = pd.read_csv(r'../PreStatusdata.csv', index_col = False)


submain= Finaldatabes[['Marks']]
Predatabase.insert(12,"FinalMarks",submain,True)
Predatabase.to_excel(r'MainDatabase.xlsx', index=False)
