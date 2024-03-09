# Foothill College
# CS 03C - DS&A in Python
# Lab 3
# Prepared by Jorge Pont
# Email: jorgefpont@gmail.com
# Student ID: 10949994
# From: https://docs.python.org/3/library/html.parser.html

# NOTE TO INSTRUCTOR
# I could not figure out how to properly read the html file
# produced by the parser into a non-binary tree,
# so i ended up doing it a different way,
# I realize it is not what is asked in the specification
# Also, I could not figure out how to build gelLists() as a method,
# so I built it as a function to get it to work

from html.parser import HTMLParser

class listCollector(HTMLParser):

    html_l = []
    def handle_starttag(self, tag, attrs):
        #print("Encountered a start tag:", tag)
        listCollector.html_l.append(tag)

    def handle_endtag(self, tag):
        #print("Encountered an end tag :", tag)
        listCollector.html_l.append(tag)

    def handle_data(self, data):
        #print("Encountered some data  :", data)
        listCollector.html_l.append(data)

    def return_list(self):
        return listCollector.html_l

    def merge_lines_and_save(input_file, output_file):
        """Merges all ines of a html file
        into one continuous line for later processing"""
        try:
            with open(input_file, 'r') as file:
                merged_lines = ''
                for line in file:
                    merged_lines += line.strip()  # Strip any leading/trailing whitespaces

                # Write merged content to output file
                with open(output_file, 'w') as output:
                    output.write(merged_lines)

        except FileNotFoundError:
            print("File not found.")

    def read_file_into_function(input_file):
        """Prepares file converting it into a file
        object to be processed"""
        try:
            with open(input_file, 'r') as file:
                # Read the entire content of the file
                content = file.read()
                return content
        except FileNotFoundError:
            print("File not found.")
            return None

    def parse_list(l):
        """Parses list of html attributes finding tables contained in the list
        and placing the elements of each table into a python list.
        Returns the python list"""
        ll = []
        i = 0
        while i < len(l):
            if l[i] == 'ul':
                # position of the next (closing) 'ul'
                end_tag = l.index('ul', i + 1)
                ll.append(l[i + 1: end_tag])
                i = end_tag + 1
            elif l[i] == 'ol':
                # position of the next (closing) 'ul'
                end_tag = l.index('ol', i + 1)
                ll.append(l[i + 1: end_tag])
                i = end_tag + 1
            else:
                i += 1
        return ll

    def remove_li(ll):
        """Removes <li> tags from the list"""
        for j in range(len(ll)):
            ll[j] = [x for x in ll[j] if x != 'li']

    def getLists(input_file):
        """Converts html file into a list,
        using parser from:
        https://docs.python.org/3/library/html.parser.html"""
        file_to_parse = 'file_to_parse'
        listCollector.merge_lines_and_save(input_file, file_to_parse)
        parser = listCollector()
        parser.feed(listCollector.read_file_into_function(file_to_parse))
        html_list = parser.return_list()
        #print('source html in list form:', html_list)
        ll = listCollector.parse_list(html_list)
        listCollector.remove_li(ll)
        return ll

# input_file = 'test_html_file_2'
# res = listCollector.getLists(input_file)
# print('res: ', res)
