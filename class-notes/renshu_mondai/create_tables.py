# -*- coding: utf-8 -*-

import mysql.connector as mydb
# =============================================================================
#                                    コネクション
# =============================================================================
conn = mydb.connect(
        host = "localhost",
        port = "3306",
        user = "rhoen",
        password = "pass",
        database = 'nagoya_pop'
       
    )
cur = conn.cursor(buffered=True)


TABLES = {}

TABLES['nagoya_population'] = (
    "CREATE TABLE `nagoya_population` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `year` int(4) NOT NULL,"
    "  `population` int(11) NOT NULL,"
    "  `elderly` int(11) NOT NULL,"
    "  `young_old` int(11) NOT NULL,"
    "  `old_old` int(11) NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")


for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cur.execute(table_description)
    except mydb.Error as err:
        print(err.msg)
    else:
        print("OK")

# *****************************     データ挿入 *********************************


# # add_entry = ("INSERT INTO nagoya_population "
# #                "(year, population, elderly, young_old, old_old) "
# #                "VALUES (%s, %s, %s, %s, %s)")
# 
# 
# # data = ((2010, 2263894, 471879, 256719, 215160),
# #         (2011, 2248630, 474878, 251426, 223452),
# #         (2012, 2248985, 491461, 258646, 232815),
# #         (2013, 2253639, 511034, 270498, 240536),
# #         (2014, 2258958, 529837, 282399, 247438),
# #         (2015, 2266791, 542757, 286229, 256528),
# #         (2016, 2276121, 552255, 285242, 267013),
# #         (2017, 2285628, 559802, 282132, 277670),
# #         (2018, 2292160, 565551, 279471, 286080),
# #         (2019, 2299748, 568882, 273750, 295132)
# #         )
# 
# 
# # add_entry = ("INSERT INTO nagoya_population "
# #        "(year, population, elderly, young_old, old_old) "
# #        "VALUES (%s, %s, %s, %s, %s)")
# # cur.executemany(add_entry, data)
# # conn.commit()

cur.close()
conn.close()