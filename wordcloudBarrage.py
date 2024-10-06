import numpy as np
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd


file_path = 'freq29.csv'
df = pd.read_csv(file_path)

# convert the DataFrame to a NumPy array
sorted_word_freq= df.to_numpy()

# choose the top 100 words
top_words = sorted_word_freq[:100]

# open a image as a mask
mask = np.array(Image.open("nimao1.png"))

# create a WordCloud instance with some parameters
wordcloud = WordCloud(font_path=r'NotoSansSC-Medium.ttf', background_color='white', mask=mask, contour_width=3, contour_color='steelblue')

# generate word cloud
wordcloud.generate_from_frequencies(dict(top_words))

# save image to file
wordcloud.to_file(r"lstt29.png")

# show the word cloud
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()