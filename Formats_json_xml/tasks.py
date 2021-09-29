import collections
import json
import os
from pprint import pprint



def read_json(file_path,  max_len_word=6, top_words=10):
    dir = os.getcwd()
    dir = dir + '/Formats_json_xml/'
    with open(dir + file_path, encoding='utf-8') as new_file:
        news = json.load(new_file)
        decription_words = []
        for item in news['rss']['channel']['items']:
            #description  = item['description'].split(' ')
            description = [word for word in item['description'].split(' ') if len(word) > max_len_word]
            decription_words.extend(description)
            counter_words = collections.Counter(decription_words)
        pprint(counter_words.most_common(top_words)) 
        #pprint(decription_words)
        #pprint(dir)


if __name__ == '__main__':
    read_json('newsafr.json')