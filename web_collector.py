#!/usr/bin/python
# -*- encoding: utf-8 -*-

import re
from bs4 import BeautifulSoup
import splinter
import codecs

url = 'http://apstu.ntue.edu.tw/univweb/Secure/default.aspx'

def savePage(counter, content):
    print 'Save', counter
    with codecs.open('class_%d.html' % counter, 'w', 'utf-8') as f:
        f.write(content)

def main():
    with splinter.Browser('chrome') as browser:
        browser.visit(url)
        browser.find_by_id('LoginDefault_ibtLoginGuest').click()
        browser.visit('http://apstu.ntue.edu.tw/univweb/Message/MenuTree.aspx')
        browser.visit('http://apstu.ntue.edu.tw/univweb/Message/Main.aspx?MENU_ID=GST&MENU_CNAME=%E8%A8%AA%E5%AE%A2%E4%B8%BB%E9%81%B8%E5%96%AE')
        browser.click_link_by_text('各種課表查詢') 
        browser.find_by_id('A0425Q3_ibtQuery').click()
        
        counter = 0
        is_first = True
        while True:
            soup = BeautifulSoup(browser.html)
            links = [link['href'] for link in soup.findAll('a') if "__doPostBack('A0425S3$dgData$_ctl1$_ctl" in link['href']]
            
            if not is_first:
                links = links[1:]
            else:
                savePage(counter, browser.html)
                counter += 1

            for link in links:
                browser.execute_script(link)
                savePage(counter, browser.html)
                counter += 1

            if is_first:
                is_first = False
            else:
                if len(links) + 1 == 10:
                    break

if __name__ == '__main__':
    main()
