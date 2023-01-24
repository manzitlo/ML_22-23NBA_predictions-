import pandas as pd

data = pd.read_csv('dataset/new 22-23 result.csv', encoding='utf-8')
data[u'probability'] = round(data[u'probability'], 4)
data.to_csv('dataset/new 22-23 result.csv', index=False, encoding='utf-8')
data_set = pd.read_csv('dataset/new 22-23 result.csv')

database = 0
index = 0
average = 0
for index, value in data_set.iterrows():
    database += data_set['probability'][index]
    index += 1

average = (database / index)
data_accuracy = round(0.624419002050581, 4)
data_AcWithAv = (data_accuracy + average) / 2

data_set['average'] = str(round(average, 4))
data_set['accuracy'] = str(data_accuracy)
data_set['accuracy with average'] = str(round(data_AcWithAv, 4))
data_set.to_csv('dataset/new 22-23 result.csv', index=False, sep=',')








