# 目標
定時，自動化抓取資料庫資料，並上傳到儲存空間，應用於資料視覺化。

# 定時處理
利用 crontab
$ crontab -e
然後設定時間與執行指令

為了確保資訊的正確以及 crontab 能夠
如預期的執行，我們必須要重新設置系統時間。
在 ubuntu 上，重新設定系統時間可以：
$ sudo dpkg-reconfigure tzdata
記得，重新設置完後要 reboot 讓系統生效。

#Script
使用 python 撰寫，上傳到 S3
S3 的 bucket 預計採取特殊設定，允許特定 domain 存取資料。

在 GPS 的地方要做模糊化處理
