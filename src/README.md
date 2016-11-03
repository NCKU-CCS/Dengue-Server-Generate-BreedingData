# 執行
```
$ python3 auto_generate_data.py
```

# 檔案說明
- auto_generate_data.py: 主要用來生成視覺話需要的資料
- s3_setting.py: 用來設定 AWS S3 服務
- credentials.py: 設定 AWS 服務的 access key
- db_config.py: 撰寫 DB 操作相關

# 怎麼使用？
在 db_config.py 設定資料庫以及資料庫的使用者
在 credentials.py 設定 AWS API 所需的使用權限和 KEY
在使用 s3 服務之前，先執行 s3_setting.py 設定 s3
然後執行 auto_generate_data.py 來產生 json data
