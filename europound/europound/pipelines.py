# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector


class EuropoundPipeline:
    def process_item(self, item, spider):
        return item

# class SavetoMySQL:
#     def __init__(self):
#         self.conn = mysql.connector.connect(
#             host = "localhost",
#             user = "root",
#             password = "junior06",
#             database = "europound"
#             )
#         self.cur = self.conn.cursor()
#         self.cur.execute("""
#         CREATE TABLE IF NOT EXISTS europound(
#             id int NOT NULL auto_increment, 
#             nombre VARCHAR(255),
#             importe VARCHAR(255),
#             PRIMARY KEY (id)
#             )
#         """)

#     def process_item(self, item, spider):
#         self.cur.execute(
#             """INSERT INTO europound (
#             nombre,
#             importe
#             ) VALUES (
#                 %s, 
#                 %s
#                 )""",
#             (item["nombre"],
#             item["importe"])
#             )
#         self.conn.commit()
#         return item
    
#     def close_spider(self, spider):
#         self.cur.close()
#         self.conn.close()