0. แก้ [config.py](http://config.py/)
conn = pyodbc.connect(
'DRIVER={ODBC Driver 17 for SQL Server};'
'SERVER=IP address/port;'
'DATABASE=databasename;'
'UID=userid;'
'PWD=password',
timeout=10
)
1. ติดตั้งไลบรารี

```bash
pip install -r requirements.txt
```

2. รัน Streamlit App

```bash
streamlit run app.py
```

3. เข้าเว็บ:

```
<http://localhost:8501>
```

[](https://github.com/user-attachments/assets/14abb28a-aa95-4d62-8abf-bf2bf1a8083c)

after press run forecast

[](https://github.com/user-attachments/assets/15e09ff1-01f5-423d-98cc-e61706117596)

[](https://github.com/user-attachments/assets/9ee0bd2e-0d3c-457e-904a-39a2ef14fae3)

after confirmed ข้อมูลจะถูกส่งไปที่ mssql
