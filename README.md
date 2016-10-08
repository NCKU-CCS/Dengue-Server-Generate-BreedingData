# 目標
定時，自動化抓取資料庫資料，並上傳到儲存空間，應用於資料視覺化。

# 定時處理
利用 crontab
$ crontab -e
然後設定時間與執行指令

# Script
使用 python 撰寫，上傳到 S3
S3 的 bucket 預計採取特殊設定，允許特定 domain 存取資料。

在 GPS 的地方要做模糊化處理
