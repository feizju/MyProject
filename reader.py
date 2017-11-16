# -*- coding: utf-8 -*-
"""
Cheak data

Created on Thu Nov 16 11:02:13 2017

@author: tengfei.tengfei
"""
import codecs

with codecs.open('file_name',encoding='utf-8') as file:
    record_id = 0
    for line in file:
        fields = line.strip().split('\u0001')
        if len(fields) != 99:
            print('record %d has %d fields'%(record_id, len(fields)))
        record_id += 1
