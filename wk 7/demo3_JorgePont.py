# Foothill College
# CS 03C - DS&A in Python
# Lab 3
# Prepared by Jorge Pont
# Email: jorgefpont@gmail.com
# Student ID: 10949994

from html.parser import HTMLParser
from JorgePontLab3 import listCollector

input_file = 'test_html_file_2'
res = listCollector.getLists(input_file)
print('res: ', res)

"""
Output:
res:  [['Web for All', 'Web on Everything']]
"""