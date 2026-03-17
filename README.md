# 📋 Attendance Manager — Setup Guide (Termux / Android)

## 1. Install packages in Termux

```bash
pkg update && pkg upgrade -y
pkg install python mariadb
pip install flask pandas openpyxl pymysql werkzeug
```

## 2. Start MariaDB

```bash
# First time only — initialise the database
mysql_install_db

# Start the server
mysqld_safe &

# Wait 3-4 seconds, then secure it (optional but recommended)
mysql_secure_installation
```

## 3. Configure DB password in app.py

Open `app.py` and find this section near the top:

```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',        # ← put your MariaDB password here
    'database': 'attendance_db',
    ...
}
```

## 4. Run the app

```bash
cd attendance_app
python app.py
```

You will see:
```
* Running on http://0.0.0.0:5000
```

## 5. Access the app

| Device | URL |
|--------|-----|
| Same phone browser | http://localhost:5000 |
| Another device on same WiFi | http://<your-phone-ip>:5000 |

To find your phone's IP in Termux:
```bash
ifconfig | grep 'inet '
# Look for something like 192.168.1.xx
```

---

## 📊 Excel Sheet Format

Your weekly Excel sheet should look like this:

| Reg No | Student Name | 2024-01-15 | 2024-01-16 | 2024-01-17 |
|--------|-------------|------------|------------|------------|
| CS001  | Alice       | P          | P          | A          |
| CS002  | Bob         | A          | P          | P          |

- **Column 1** — Registration / Roll Number
- **Column 2** — Student Name
- **Columns 3+** — Dates (any recognizable date format) with **P** or **A** values
- Multiple sheets in one workbook are all processed
- Upload the same subject multiple weeks — data is cumulative, duplicates are updated

---

## 🧪 Generate a test Excel file

```bash
python generate_sample.py
# Creates sample_attendance.xlsx in current folder
```

---

## 📡 JSON API

Get attendance data as JSON:
```
http://localhost:5000/api/report
http://localhost:5000/api/report?subject=Mathematics
```
