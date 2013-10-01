#!/usr/bin/python
# -*- encoding: utf-8-*-

import codecs
import sys
import re
from bs4 import BeautifulSoup
import json
import io

def main():
    items = []
    item = {}
    for page in range(0,30):
        with open('class_%d.html' % page,'r') as f:
            data = f.read()
        soup = BeautifulSoup(''.join(data))
        counter = 0
        for each_div in soup.find_all('font'):
            if counter == 0:
                item['id'] = each_div.get_text()
            elif counter == 2:
                item['name'] = each_div.get_text()
            elif counter == 3:
                item['must'] = each_div.get_text()
            elif counter == 4:
                item['course'] = each_div.get_text()
            elif counter == 5:
                item['class'] = each_div.get_text()
            elif counter == 6:
                item['department'] = each_div.get_text()
            elif counter == 7:
                item['school'] = each_div.get_text()
            elif counter == 8:
                item['teacher'] = each_div.get_text()
            elif counter == 9:
                item['time'] = each_div.get_text()
            elif counter == 10:
                item['room'] = each_div.get_text()
            elif counter == 11:
                item['credits'] = each_div.get_text()
            elif counter == 12:
                item['min'] = each_div.get_text()
            elif counter == 13:
                item['max'] = each_div.get_text()
            elif counter == 14:
                item['have_chose'] = each_div.get_text()
            elif counter == 15:
                item['chosen'] = each_div.get_text()
            elif counter == 16:
                item['note'] = each_div.get_text()
                
            counter+=1
            print each_div.get_text()
                        
            if counter == 17:
                print "-"*17
                counter = 0
                items.append(item)

                item = {}


    with codecs.open('/Users/tengyouwei/Downloads/fuck/result.json', 'w', 'utf-8') as f:
        f.write(json.dumps(items, ensure_ascii=False, indent = 4))

if __name__ == '__main__':
	main()


