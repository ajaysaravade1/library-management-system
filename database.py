import pymysql

timeout = 10

# MySQL connection setup
connection = pymysql.connect(
    charset="utf8mb4",
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db="lms",
    host="mysql-23238b15-ajaysaravade1-058b.i.aivencloud.com",
    password="AVNS__gMfA8TKTBunbx6vVSa",
    read_timeout=timeout,
    port=12868,
    user="member",
    write_timeout=timeout,
)

def get_cursor():
    try:
        cursor = connection.cursor()
        return cursor
    except Exception as e:
        print("Error connecting to MySQL:", e)
        raise e
