#!/usr/bin/env python
# coding: utf-8

if __name__ == '__main__':
    try:
        while True:
            print("Please enter the content: ")
            stopword = ':q'
            content = ''
            for line in iter(input, stopword):
                content += line
            print("Content length: " + str(len(content)))
    except KeyboardInterrupt:
        print()
        input('Please press any key to continue...')


