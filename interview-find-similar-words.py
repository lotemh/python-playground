import sys
from bs4 import BeautifulSoup
from urllib import urlopen
import re

def find_joined_words(list1, list2):
    for word in list1:
        for word2 in list2:
            if word[0] == word2[0]:
                print(word[0] +": " + str(word[1]) +", "+ str(word2[1]))

def get_most_popular_words(words_dict, limit):
    return sorted(words_dict.items(), key=lambda k, v: v, reverse=True)[0:limit]

def get_url_content(url):
    print(url)
    html = urlopen(url).read()
    soup = BeautifulSoup(html, "html5lib")
    resp = soup.find_all("p")
    words_dict = {}
    for p in resp:
        text = p.text
        text = re.sub(r'[^A-Za-z ]+', '', text)
        text = text.split(" ")
        for word in text:
            word = word.strip().lower()
            if len(word) < 6:
                continue
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1
    return(words_dict)



def find_substring(words):
    substring_dict = []
    for word in words:
        index = 2
        while index < word.length:
            print(word[:index])



if __name__ == "__main__":
    dicts = []
    num_of_words = int(sys.argv[3])
    most_popular_words_list = []
    for url in sys.argv[1:3]:
        dicts.append(get_url_content(url))
    for words_dict in dicts:
        res = get_most_popular_words(words_dict, num_of_words)
        most_popular_words_list.append(res)
        print(res[:10])
    find_joined_words(most_popular_words_list[0], most_popular_words_list[1])
    find_substring(most_popular_words_list[0].append(most_popular_words_list[1]))