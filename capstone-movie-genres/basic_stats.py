import csv
from io import BytesIO
import numpy as np
import os
import pandas as pd
from PIL import Image
import requests
import time

current_path = os.path.join('/', 'Users', 'Chinthan', 'Desktop', 'Springboard')
FILE_LOCATION = os.path.join(current_path, 'movie-genre-from-its-poster', 'MovieGenre.csv')
df = pd.read_csv(FILE_LOCATION, encoding='latin-1')

#start_time = time.time()
# Index([u'imdbId', u'Imdb Link', u'Title', u'IMDB Score', u'Genre', u'Poster'], dtype='object')

img_sizes = []
err_count = 0

def url_to_np_array(url):
    try:
        response = requests.get(url)
        img = np.asarray(Image.open(BytesIO(response.content)))
        img_size = img.shape
        return img_size
    except:
        #print(time.time() - start_time)
        #start_time = time.time()
        return None

df2 = df.iloc[:10]
df2['img_size'] = df2['Poster'].apply(url_to_np_array)
print(df2)
#df['img_size'] = df['Poster'].apply(url_to_np_array)
#print(df['img_size'])
'''
for index, movie in df.iterrows():
    if index % 100 == 0:
        print 'Index: ', '\t', index
    try:
        response = requests.get(movie['Poster'])
        img = Image.open(BytesIO(response.content))
        img_sizes.append(np.asarray(img).shape)
    except:
        err_count += 1
        # print 'Index: ', index, '\t', 'Cumulative Error Count: ', err_count, '\n', movie['Title'], '\t', movie['Poster']
        continue

print 'Error count: ', err_count, '\n', img_sizes
'''
