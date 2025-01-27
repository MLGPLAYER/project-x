#!/usr/bin/env python3.4

import os, sys
import cgi, cgitb

cgitb.enable()
sys.stderr = sys.stdout

print('Content-type: text/html;charset=windows-1251\n')

with open('../public_html/header.html', mode='r', encoding='utf-8') as file_read:
  for line in file_read:
    print(line)

with open('../public_html/about.html', mode='r', encoding='utf-8') as file_read:
  for line in file_read:
    print(line)

with open('../public_html/footer.html', mode='r', encoding='utf-8') as file_read:
  for line in file_read:
    print(line)
