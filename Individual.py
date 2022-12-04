#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def strok():
    def ol(spisok):
        li = '</li>\n<li>'.join(spisok)
        return f"<ol>\n<li>{li}</li>\n</ol>"
    return ol


if __name__ == '__main__':
    my_list = [
        'строка_1',
        'строка_2',
        'строка_3',
        'строка_4'
    ]
    result = strok()
    print(result(my_list))