## Abstract

The information contained in "barrage" comments (often real-time comments or feedback overlaid on videos) reflects the subjective emotions of users. Understanding this data can help in improving user engagement, optimizing content strategies, and enhancing the overall viewing experience.

### Technology used: 
python, pySpark, Jieba(Chinese text segmentation), wordCloud


## Process
### 1. Analyze the Network Traffic and Use requests to Retrieve Barrage Data:
Find the specified URL for requesting barrage data in the website's network. Use the GET method from the requestslibrary to retrieve data from the serialized JSON content in the response when calling this specified URL. The total number of barrage comments for one episode is around 60,000. Select the required fields from the result and save them into a CSV file.

<img width="600" alt="network" src="https://github.com/user-attachments/assets/64c57e47-c806-4e5a-bb5c-802a8c517717">


### 2. Segmentation and Word Counting:
Using Jieba to segment each line of barrage data into individual words. Single-character words and stop words were removed from the results. This gave us a dictionary of words sorted by frequency. The top 200 most frequent words were saved into a CSV file.



### 3. Word Cloud Generation:
Using the WordCloud library, we generated a visual representation of the word frequency data. Customizations included using a mask image to shape the cloud, a Chinese font to handle non-Latin characters, and a white background. The word cloud was then displayed using matplotlib and saved as an image.

## Output

<picture>
  <img width="300" alt="cat" src="https://github.com/user-attachments/assets/313fec68-916b-420c-ac16-f3b3c0c499db">
</picture>
