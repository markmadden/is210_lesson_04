#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" task 4 """

import data

MAX = None
MIN = None
DAYS = 0
TOTAL = 0

for DAY in data.TRANSACTIONS:
    DAYS += 1
    DAY_TOTAL = 0
    for TRANS in DAY:
        DAY_TOTAL += TRANS

    if DAY_TOTAL < MIN or MIN is None:
        print MIN, DAY_TOTAL 
        MIN = DAY_TOTAL      
        
    if DAY_TOTAL > MAX or MAX is None:
        print MAX, DAY_TOTAL
        MAX = DAY_TOTAL
        

    TOTAL += DAY_TOTAL
