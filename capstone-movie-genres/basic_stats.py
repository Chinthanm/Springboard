import csv
from io import BytesIO
import numpy as np
import os
import pandas as pd
from PIL import Image
import requests

current_path = os.path.join('/', 'Users', 'Chinthan', 'Desktop', 'Springboard')
FILE_LOCATION = os.path.join(current_path, 'movie-genre-from-its-poster', 'MovieGenre.csv')
print(FILE_LOCATION)
df = pd.read_csv(FILE_LOCATION)

'''
# Index([u'imdbId', u'Imdb Link', u'Title', u'IMDB Score', u'Genre', u'Poster'], dtype='object')

img_sizes = []
err_count = 0

for index, movie in df.iterrows():
    try:
        response = requests.get(movie['Poster'])
        img = Image.open(BytesIO(response.content))
        img_sizes.append(np.asarray(img).shape)
    except:
        err_count += 1
        print('Index: ', index, '\t', 'Cumulative Error Count: ', err_count, '\n', movie['Title'], '\t', movie['Poster'])
        continue
'''

