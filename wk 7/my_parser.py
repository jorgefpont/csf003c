"""
From: https://docs.python.org/3/library/html.parser.html
"""

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
    try:
        with open(input_file, 'r') as file:
            merged_lines = ''
            for line in file:
                merged_lines += line.strip()  # Strip any leading/trailing whitespaces

            # Write merged content to output file
            with open(output_file, 'w') as output:
                output.write(merged_lines)

            #print("Merged content saved to", output_file)

    except FileNotFoundError:
        print("File not found.")

def read_file_into_function(input_file):
    try:
        with open(input_file, 'r') as file:
            # Read the entire content of the file
            content = file.read()
            return content
    except FileNotFoundError:
        print("File not found.")
        return None

input_file = 'test_html_file_2'
output_file = 'test_html_file_2_no_cr'
merge_lines_and_save(input_file, output_file)

parser = listCollector()
parser.feed(read_file_into_function(output_file))
html_list = parser.return_list()
print(html_list)

