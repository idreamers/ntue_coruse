#!/usr/bin/python
# -*- encoding: utf-8-*-

import codecs
import sys
import re
from bs4 import BeautifulSoup
import json
import io
import sqlite3 as lite
def main():
    query = "insert into Course values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    items = []
    item = {}
    con = lite.connect('test.db')  
    for page in range(0,30):
        with open('class_%d.html' % page,'r') as f:
            data = f.read()
        soup = BeautifulSoup(''.join(data))
        counter = 0
        for each_div in soup.find_all('font'):
            if counter == 0:
                id = each_div.get_text()
            elif counter == 2:
                name = each_div.get_text()
            elif counter == 3:
                must = each_div.get_text()
            elif counter == 4:
                course = each_div.get_text()
            elif counter == 5:
                m_class = each_div.get_text()
            elif counter == 6:
                department = each_div.get_text()
            elif counter == 7:
                school = each_div.get_text()
            elif counter == 8:
                teacher = each_div.get_text()
            elif counter == 9:
                time = each_div.get_text()
            elif counter == 10:
                room = each_div.get_text()
            elif counter == 11:
                credits = each_div.get_text()
            elif counter == 12:
                min = each_div.get_text()
            elif counter == 13:
                max = each_div.get_text()
            elif counter == 14:
                have_chose = each_div.get_text()
            elif counter == 15:
                chosen = each_div.get_text()
            elif counter == 16:
                note = each_div.get_text()
            counter+=1
            #print each_div.get_text()
                        
            if counter == 17:
                #print "-"*17
                counter = 0
                t_item = (school, name,room, chosen, max, min, str(id), note,course,teacher, have_chose, time, department,credits, m_class, must)
                with con:
                    try:
                        cur = con.cursor()
                        cur.execute(query, t_item)

                    except lite.Error, e:
                        print "Error %s." % e.args[0]

                t_item = []
                item = {}
            
if __name__ == '__main__':
	main()


