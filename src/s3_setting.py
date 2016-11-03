# ALLOWED_ORIGIN 可以設定允許跨域請求的網域來源
# STORAGE_BUCKET 是你的 bucket 名稱

from boto.s3.connection import S3Connection 
from boto.s3.key import Key
from boto.s3.cors import CORSConfiguration

import credentials

STORAGE_BUCKET = "dengue-test"
ALLOWED_ORIGIN = '*'
UPLOAD_BLURRED_FILE = 'breeding-sources/heatmap_blurred.json'

if __name__ == "__main__":
    s3con = S3Connection(credentials.ACCESS_KEY, credentials.PRIVATE_KEY)
    bucket = s3con.get_bucket(STORAGE_BUCKET)
    
    cors_cfg = CORSConfiguration()
    cors_cfg.add_rule('GET', ALLOWED_ORIGIN)
    bucket.set_cors(cors_cfg)


