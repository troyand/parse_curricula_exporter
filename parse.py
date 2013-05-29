#!/usr/bin/env python

import csv
import sys
import codecs
import re

def unicode_csv_reader(unicode_csv_data, dialect=csv.excel, **kwargs):
    # csv.py doesn't do Unicode; encode temporarily as UTF-8:
    csv_reader = csv.reader(utf_8_encoder(unicode_csv_data),
                            dialect=dialect, **kwargs)
    for row in csv_reader:
        # decode UTF-8 back to Unicode, cell by cell:
        yield [unicode(cell, 'utf-8') for cell in row]

def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line.encode('utf-8')

def parse(fileobject):
    result = []
    for line in unicode_csv_reader(fileobject):
        result.append(line)
    return result

def write_html(filename, header, rows):
    out_file = codecs.open(filename, 'w', 'utf8')
    out_file.write('<!DOCTYPE html><html><head><meta charset="utf-8"></head>')
    out_file.write('<body><table border="1">')
    out_file.write('<tr>')
    for field in header:
        out_file.write('<th>%s</th>' % field)
    out_file.write('</tr>\n')
    for row in rows:
        out_file.write('<tr>')
        for field in row:
            out_file.write('<td>%s</td>' % re.sub('\n\r?', '<br>', field))
        out_file.write('</tr>\n')
    out_file.write('</table></body>')
    out_file.close()

def main():
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    rows = parse(codecs.open(input_filename, 'r', 'utf8'))
    courses_fields = ['level','code','program','course_code','course','type','rank','credits','term','description']
    write_html(output_filename, courses_fields, rows)


if __name__ == '__main__':
    main()
