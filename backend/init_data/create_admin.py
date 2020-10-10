from passlib.context import CryptContext
from datetime import datetime
import psycopg2
from settings import settings

connection = psycopg2.connect(
    user=settings.DB_USER,
    password=settings.DB_PASSWORD,
    host=settings.DB_HOST,
    port="5432",
    database=settings.DB_NAME,
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Creating a cursor object using the cursor() method
cursor = connection.cursor()
USERNAME = "admin"
PASSWORD = "hocmang.net"
HASHED_PASSWORD = pwd_context.hash(PASSWORD)
EMAIL = "thangphan205@gmail.com"
FULL_USERNAME = "admin"
USER_ROLE = 100
IS_ACTIVE = True
DATETIME_NOW = datetime.now()
LOGIN_FAIL = 0
DEPARTMENT = "Admin"
# Preparing SQL queries to INSERT a record into the database.
query = """INSERT INTO users(
   username, hashed_password, 
   email, full_username, 
   user_role, is_active, 
   department, last_login,
   created_date,login_fail,
   description
   ) VALUES 
   ('{}','{}','{}','{}',{},{},'{}','{}','{}','{}','')""".format(
    USERNAME,
    HASHED_PASSWORD,
    EMAIL,
    FULL_USERNAME,
    USER_ROLE,
    IS_ACTIVE,
    DEPARTMENT,
    DATETIME_NOW,
    DATETIME_NOW,
    0,
)
print(query)
cursor.execute(query)

# Commit your changes in the database
connection.commit()
print("Inserted username/password : {}/{}".format(USERNAME, PASSWORD))

# Closing the connection
connection.close()
