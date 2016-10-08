# 要使用這個 program 之前，為了確保資訊的正確以及 crontab 能夠
# 如預期的執行，我們必須要重新設置系統時間。
# 在 ubuntu 上，重新設定系統時間可以：
# $ sudo dpkg-reconfigure tzdata
# 記得，重新設置完後要 reboot 讓系統生效。
#
# credentials.py:
# ACCESS_KEY = "xxxxx"
# PRIVATE_KEY = "yyyy"
#
# db_config.py:
# DATABASE = "dbname"
# ROLE = "role"
# PASSWORD = "pw"
# QUERY = "query"
# 
# 在上傳資料到 bucket 時，因為 bucket 會設定容許的 domain name, 所以要注意一下

import json
import psycopg2
import time 
import random

from boto.s3.connection import S3Connection
from boto.s3.key import Key
from boto.s3.cors import CORSConfiguration

import credentials
import db_config

# connect to database
conn = psycopg2.connect(database=db_config.DATABASE, user=db_config.ROLE, password=db_config.PASSWORD)
cur = conn.cursor()

# 從 db 存取資料
# TODO 將 SQL query 寫到 db_config 裡面
cur.execute(db_config.QUERY)

# from database to json
rows = cur.fetchall()
db_result = list()
for row in rows:
    row_data = dict()
    row_data['address'] = row[0]
    
    # TODO 尚未模糊化 GPS
    # lat, lng will be floating number (class 'float')
    row_data['lat'] = row[1]
    row_data['lng'] = row[2]
    row_data['description'] = row[3]

    db_result.append(row_data)

result = dict()
result['generated_time'] = time.asctime() 
result['data'] = db_result

# generate json file
with open("breeding_source.json", "w") as fd:
    status = json.dump(result, fd, ensure_ascii=False, indent=4)

access_key = credentials.ACCESS_KEY
secret_key = credentials.PRIVATE_KEY
s3con = S3Connection(access_key, secret_key)

bucket = s3con.get_bucket('dengue-test')
# TODO 要修改 bucket 的 rule 縮限容許的 domain name
cors_cfg = CORSConfiguration()
cors_cfg.add_rule('GET', '*')
bucket.set_cors(cors_cfg)

k = Key(bucket)
k.key = 'breeding-sources/heatmap_blurred.json'
k.set_contents_from_filename("./breeding_source.json")
k.set_metadata("Content-Type", "application/json")
k.set_acl("public-read")

print (k.get_acl())
print (k.generate_url(expires_in=0, query_auth=False))
