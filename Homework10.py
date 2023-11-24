import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup



url = 'https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html'
headers = {'User-Agent': 'Mozilla/5.0 ('}
re = requests.get(url, headers=headers)
print(re)

if re.status_code!=200:
    print('не удалось получить ответ от сайта')
else:
    soup = BeautifulSoup(re.text, 'html.parser')
    pre_matrix = soup.find(class_='doctest highlight-default notranslate').find_all('span', class_='go')
    pre_matrix = pd.DataFrame(pre_matrix)
    num_matrix1 = np.array(pre_matrix.iloc[1])
    num_matrix2 = np.array(pre_matrix.iloc[2])
    two_dimens_matrix = np.array([num_matrix1, num_matrix2])
    print(two_dimens_matrix)
