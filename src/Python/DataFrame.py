dict = {
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area": [8.156, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98],
}
import pandas as pd
list = pd.DataFrame(dict)
'''using DataFrame from pandas'''
print(list)
list.index = ["BR", "RU", "IN", "CH", "SA"]
print(list)
'''Using panda.read_csv to visualize a csv file'''
insurance = pd.read_csv('FL_insurance_sample.csv')
print(insurance)
print(list['country'])
print(list[['country']])
dates = pd.date_range('20130101', periods = 10)
print(dates)
print(list[['country', 'area']])
insurance = pd.read_csv('FL_insurance_sample.csv', index_col = 0)
print(insurance[0:10])