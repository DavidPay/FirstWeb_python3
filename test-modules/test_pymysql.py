#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author: David Pay
#date: 06-21-2018

'''
1.why i create this test?
because it doesn't work.
by now, pymysql 0.8.1 didn't support mysql 8.0+,.
https://dev.mysql.com/doc/refman/8.0/en/upgrading-from-previous-series.html#upgrade-caching-sha2-password-replication
caching_sha2_password
the other reason is that if you want use some module, please write a simple test about the module
for comprehending and learning. simple is for the complex.
over

2.learned vscode setting about debuging the library code. 
set “debugOptions” "DebugStdLib". they are snippet? out come out.
https://code.visualstudio.com/docs/python/debugging
because of my bad english reading. i can't quick view the page and find the solution liking reading chinese.
that should be done - "using english easily as chinese"
'''
import pymysql.cursors

connection = pymysql.connect(
    host='localhost',
    user='localuser',
    password = 'local',
    db='awesome',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:
        cursor.close()
finally:
    cursor.close()