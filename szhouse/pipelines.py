# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class QimoPipeline(object):
    def __init__(self):
        conn = pymysql.connect(host='localhost', user='root', passwd='root', db='mydb', port=3306, charset='utf8')
        cursor = conn.cursor()
        self.post = cursor


    def process_item(self, item, spider):
        cursor = self.post
        cursor.execute("insert into szhouse values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(item['title'],item['price'],item['unitprice'],item['maininfo'],item['subinfo'],item['area'],item['xiaoqu'],item['address'],item['brokername'],item['phone']))
        cursor.connection.commit()
# import pymysql
# #
# #
# class MysqlPipeline(object):
#
#     def __init__(self):
#         # 建立连接
#         self.conn = pymysql.connect(host='localhost', user='root', passwd='root', db='mydb', port=3306,charset='utf8')  # 有中文要存入数据库的话要加charset='utf8'
#         # 创建游标
#         self.cursor = self.conn.cursor()
#
#     def process_item(self, item, spider):
#         # sql语句
#         insert_sql = """insert into szhouse values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
#         # 执行插入数据到数据库操作
#         self.cursor.execute(insert_sql, (item['title'],item['price'],item['unitprice'],item['maininfo'],item['subinfo'],item['area'],item['xiaoqu'],item['address'],item['brokername'],item['phone']))
#         # 提交，不进行提交无法保存到数据库
#         self.conn.commit()
#         return item
#
#     def close_spider(self, spider):
#         # 关闭游标和连接
#         self.cursor.close()
#         self.conn.close()


