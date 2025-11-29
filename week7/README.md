## Assignment - Week 7

### 環境安裝

1. 安裝套件
pip install -r requirements.txt

2. 建立 config.py（需自行建立）<br>
DB_USER = " MySQL 帳號"<br>
DB_PASSWORD = " MySQL 密碼"<br>
SESSION_MIDDLEWARE_SECRET_KEY = "任意安全字串"

3. 匯入資料庫
mysql -u <DB_USER> -p < website.sql
