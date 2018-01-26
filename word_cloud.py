#!coding:utf-8

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.misc import imread
import jieba
import jieba.posseg
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


# 从本地文件读取数据，并将数据进行过滤及格式化
def read_word_list():
	text = open("bak.html", "r").read();
	seg = jieba.posseg.cut(text);
	word_list = [];
	file = open("word_flag.txt", "a");
	for str in seg:
		if len(str.word) > 1 and str.word != "名红" and str.word != "没有" and str.word != "喜欢" and str.word != "时候":
			if str.flag == "n" or str.flag == "v" or str.flag == "a" or str.flag == "i" or str.flag == "nr" or str.flag == "ns" or str.flag == "z" or str.flag == "vn":
				word_list.append(str.word);
				file.write(str.word + "," + str.flag);
	file.close();
	cur_text = " ".join(word_list);
	return cur_text;


# 输入被格式化后的数据，生成词云
def generate_word_cloud(cur_text):
	cloud_bg = imread("cloud_bg.jpg");
	word_cloud = WordCloud(font_path="simfang.ttf", mask=cloud_bg, background_color="black", stopwords=STOPWORDS).generate(cur_text);
	image_color = ImageColorGenerator(cloud_bg);
	plt.imshow(word_cloud, interpolation = "bilinear");
	plt.axis("off");
	plt.show();
	word_cloud.to_file("word_cloud.jpg");


if __name__ == "__main__":
	cur_text = read_word_list();
	generate_word_cloud(cur_text);






