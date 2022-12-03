import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

#Read Text
text = open('michelle_obama_speech.txt', mode='r', encoding='utf-8').read()
stopwords = STOPWORDS

wc = WordCloud(
            background_color='white',
            stopwords=stopwords,
            height = 600,
            width = 400 
)

wc.generate(text)

# store/save file to local

wc.to_file('wordcloud_output.png')