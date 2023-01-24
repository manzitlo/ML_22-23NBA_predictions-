import pandas as pd
df = pd.read_csv('dataset/new 22-23 result.csv')

print(df['WEST_TEAMS'][:10])
print(df['EAST_TEAMS'][:10])

