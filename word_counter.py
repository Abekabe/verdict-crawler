#!/usr/bin/env python
# coding: utf-8

if __name__ == '__main__':
    try:
        while True:
            content = input("Please enter the content: ")
            print("Content length: " + str(len(content)))
            #input('Please press any key to continue...')
    except KeyboardInterrupt:
        print()
        input('Please press any key to continue...')


