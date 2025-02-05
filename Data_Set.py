
import pandas as pd
import numpy as np

columns = ['RowNumber', 'CustomerId', 'Surname', 'CreditScore', 'Geography', 'Gender', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary', 'qExited']
dataset = pd.DataFrame(columns=columns)

# Generate random data
n_rows = 100000
dataset['RowNumber'] = np.arange(1, n_rows+1)
dataset['CustomerId'] = np.random.randint(100000, 999999, size=n_rows)
dataset['Surname'] = ['Surname' + str(i+1) for i in range(n_rows)]
dataset['CreditScore'] = np.random.randint(300, 850, size=n_rows)
dataset['Geography'] = np.random.choice(['France', 'Spain', 'Germany'], size=n_rows)
dataset['Gender'] = np.random.choice(['Male', 'Female'], size=n_rows)
dataset['Age'] = np.random.randint(18, 80, size=n_rows)
dataset['Tenure'] = np.random.randint(0, 10, size=n_rows)
dataset['Balance'] = np.random.uniform(0, 100000, size=n_rows)
dataset['NumOfProducts'] = np.random.randint(1, 5, size=n_rows)
dataset['HasCrCard'] = np.random.choice([0, 1], size=n_rows)
dataset['IsActiveMember'] = np.random.choice([1, 0], size=n_rows)
dataset['EstimatedSalary'] = np.random.uniform(0, 200000, size=n_rows)
dataset['qExited'] = np.random.choice([0, 1], size=n_rows, p=[0.25, 0.75])
#dataset['Bank DOJ'] = pd.date_range(start='2016-01-01', end='2023-05-02', periods=n_rows)

# Print the dataset
print(dataset)

dataset.to_csv('Temporary_data.csv', index=False)