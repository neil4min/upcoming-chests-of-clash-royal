#!/usr/bin/env python3

#
# Example:
#     python3 main.py <TAG>
# <TAG>: no leading '#' 
#

import sys
import requests
from bs4 import BeautifulSoup
import re

# retrieve TAG through command line
TAG = sys.argv[1]

# retrieve content of target web page
content = requests.get('http://statsroyale.com/profile/' + TAG).content

# parse content of target web page
soup = BeautifulSoup(content, "lxml")

# extract upcoming chests of target web page
upcoming_chest_list = []
for element in soup.find_all("div", "ui__tooltip ui__tooltipTop ui__tooltipMiddle chests__tooltip"):
    upcoming_chest_list.append(re.findall(pattern=r'\w+', string=element.get_text()))

# parse upcoming_chest_list

# parse next
print('Next Chest:\n     ', upcoming_chest_list[0][0], 'Chest')

# parse upcoming
print('Upcoming Chests:')
for i in range(1, len(upcoming_chest_list)):
    print('   ', upcoming_chest_list[i][0], end='    ')
    for j in range(1, len(upcoming_chest_list[i])):
        print(upcoming_chest_list[i][j], end=' ')
    print('\n')
