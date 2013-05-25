#!/bin/bash

curl http://www.ukma.edu.ua/courses/ects/curricula/exporter2.php | iconv -f cp1251 -t utf-8 | sed -e 's/\\"/""/g' > input.csv
./parse.py input.csv output.html
