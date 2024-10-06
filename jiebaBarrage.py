# Chinese text segmentation library
import jieba
import csv
from pyspark.sql import SparkSession
from collections import defaultdict
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np 




# Create SparkSession
spark = SparkSession.builder.appName("SparkSQL").getOrCreate()
# Read CSV File
df = spark.read.csv("29epi.csv", header=True, inferSchema=True)

# create a new DataFrame through selecting column from DataFrame
df_new= df.select('content')
df_new.printSchema()

# Retrieve data from DataFrame
dataCollect = df_new.collect()

# load stop words from multiple resources 
cn_words = np.loadtxt("cn_stopwords.txt", skiprows=1, dtype='str') 
hit_words = np.loadtxt("hit_stopwords.txt", skiprows=1, dtype='str')
scu_words = np.loadtxt("scu_stopwords.txt", skiprows=1, dtype='str')
baidu_words = np.loadtxt("baidu_stopwords.txt", skiprows=1, dtype='str')

# combine to a collection of stop words
stop_words= np.concatenate((cn_words, hit_words, scu_words, baidu_words))

# word segmentation array
word_list= []

for row in dataCollect:
    result= []
    seg_list = jieba.cut(row["content"])
    for w in seg_list: # loop in segmentation list
        if len(w) >1:  # remove the words with only one Chinese character
            if w not in stop_words:
                result.append(w)
    word_list.append(result)

# create a defaultdict with a default value of int
word_freq = defaultdict(int)

# count the word frequency
for row in word_list:
    for word in row:
        word_freq[word]+= 1

# sort the result according to reversed frequency
sorted_word_freq = sorted(word_freq.items(), key = lambda x:x[1], reverse=True)


# save the top 200 result into csv file
with open('freq29.csv','w', encoding='utf-8',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Word","Frequency"])
    for word, freq in sorted_word_freq[:200]:
        writer.writerow(([word, freq]))

spark.stop()
