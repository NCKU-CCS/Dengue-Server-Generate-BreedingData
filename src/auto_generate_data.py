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
import time 
import random

import psycopg2
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from boto.s3.cors import CORSConfiguration

import credentials
import db_config
import s3_setting

def extract_from_rows(rows, is_blurred=True):
    result = dict()
    db_data = list()
    for row in rows:
        row_data = dict()
        
        row_data['address'] = row[0]
        row_data['lat'] = row[1] + random.randint(-50, 50) * 0.00001 if is_blurred else 0
        row_data['lng'] = row[2] + random.randint(-50, 50) * 0.00001 if is_blurred else 0
        row_data['description'] = row[3]

        db_data.append(row_data)

    result = dict()
    result['generated_time'] = time.asctime() 
    result['data'] = db_data 
    
    return result


if __name__ == "__main__":

    # 設定模糊化的亂數種子
    # 為了讓下一次地圖的點不會消失，可以採用固定種子
    random.seed(1)
    
    conn = psycopg2.connect(database=db_config.DATABASE, user=db_config.ROLE, password=db_config.PASSWORD) 
    cur = conn.cursor()
    cur.execute(db_config.QUERY)
    rows = cur.fetchall()
    result = extract_from_rows(rows)
    
    # generate json file
    with open("breeding_source_blurred.json", "w") as fd:
        status = json.dump(result, fd, ensure_ascii=False, indent=4)
    
    
    s3con = S3Connection(credentials.ACCESS_KEY, credentials.PRIVATE_KEY)
    bucket = s3con.get_bucket(s3_setting.STORAGE_BUCKET)
    
    k = Key(bucket)
    k.key = s3_setting.UPLOAD_BLURRED_FILE
    k.set_contents_from_filename("./breeding_source_blurred.json")
    k.set_metadata("Content-Type", "application/json")
    k.set_acl("public-read")

    print (k.get_acl())
    print (k.generate_url(expires_in=0, query_auth=False))
