#!coding:utf-8

import urllib2
from bs4 import BeautifulSoup
import math
import sys
reload(sys)
sys.setdefaultencoding="utf-8"

# 将获取到的html输出到文件中
def write_to_file(html_str):
	file = open("bak.html", "a");
	file.write(html_str);
	file.close();


# 通过url和page获取html数据
def get_html(url, page):
	response = urllib2.urlopen(url+page);
	html_str = response.read();
	return html_str;


# 通过解析html获取文章链接
def get_article_url(html_str):
	soup = BeautifulSoup(html_str, "html.parser");
	article_url_list = [];
	for content in soup.select(".content"):
		article_url_list.append(content.select(".title")[0].get("href"));
	return article_url_list;

		
# 获取并解析文章内容页
def parse_html_content(html_content_url):
	content_header = "https://www.jianshu.com";
	response = urllib2.urlopen(content_header + html_content_url);
	response.encoding = "utf-8";
	content_html = response.read();
	soup = BeautifulSoup(content_html, "html.parser");
	show_content = soup.select(".show-content");
	return show_content;


# 获取当前用户共有多少篇文章
def get_article_count(html_str):
	soup = BeautifulSoup(html_str, "html.parser");
	article_count = soup.select(".meta-block")[2].select("p")[0].text;
	return article_count;

def start_crawl(url_header):
	html_str = get_html(url_header, "1");
	article_count = get_article_count(html_str);
	page_count = int(math.ceil(int(article_count) / 9.0));
	for i in range(0, page_count):
		if i != 0:
			html_str = get_html(url_header, str(i+1));
		article_url_list = get_article_url(html_str);
		for url in article_url_list:
			show_content = parse_html_content(url);
			write_to_file(" ".join(str(content) for content in show_content));


if __name__ == "__main__":
	start_crawl("https://www.jianshu.com/u/93539be96624?order_by=shared_at&page=");

