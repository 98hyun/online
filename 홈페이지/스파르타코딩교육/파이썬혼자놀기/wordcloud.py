# load library
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# load text
with open("./kakaotalk/kakaotalk.txt","r",encoding='utf-8') as file:
    lines=file.readlines()
    text=""
    for line in lines:
        if '] [' in line:
            text += line.split('] ')[2].replace('ㅋ','').replace('ㅠ','').replace('ㅜ','').replace('사진\n','').replace('이모티콘\n','').replace('삭제된 메시지입니다','')

# wordcloud
font_path = 'C:/Windows/Fonts/malgunbd.ttf'
mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path=font_path, background_color="white", mask=mask)
wc.generate(text)
wc.to_file("result_masked.png")
