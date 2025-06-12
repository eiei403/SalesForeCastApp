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

![image](https://github.com/user-attachments/assets/0f075500-a7f0-420a-a601-bad5df79f0b1)

หลังจากกด run forecast
![image](https://github.com/user-attachments/assets/56ac3360-53ea-4d06-b259-c0e4dc534c99)
![image](https://github.com/user-attachments/assets/92a1d8e3-21c2-4fa2-a0d0-e16de33c36f4)


หลังconfirmed ข้อมูลจะถูกส่งไปที่ mssql
