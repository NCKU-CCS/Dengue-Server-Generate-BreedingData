# Dengue Server GenerateBreedingData

定時、自動化抓取資料庫資料，並上傳到儲存空間，應用於資料視覺化。

## 安裝套件
```sh
pipenv install
```

## 執行
```sh
$ pipenv run python src/auto_generate_data.py
```

## 檔案說明
* `src/auto_generate_data.py`: 主要用來生成視覺化需要的資料
* `src/s3_setting.py`: 用來設定 AWS S3 服務
* `src/credentials.py`: 設定 AWS 服務的 access key
* `src/db_config.py`: 撰寫 DB 操作相關

## Usage
在 db_config.py 設定資料庫以及資料庫的使用者  
在 credentials.py 設定 AWS API 所需的使用權限和 KEY  
在使用 s3 服務之前，先執行 s3_setting.py 設定 s3  
然後執行 auto_generate_data.py 來產生 json data

## 定時處理
利用 crontab

```sh
$ crontab -e
```

設定時間與執行指令

為了確保資訊的正確以及 crontab 能夠如預期的執行，我們必須要重新設置系統時間。  
在 ubuntu 上，重新設定系統時間可以：

```sh
$ sudo dpkg-reconfigure tzdata
$ reboot
```

## License
MIT @theMosquitoMan team

