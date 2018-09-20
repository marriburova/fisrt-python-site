import mysql.connector
from mysql.connector import Error
from config import MYSQL_DB_HOST, MYSQL_DB_NAME, MYSQL_DB_USER, MYSQL_DB_PASS

def connectDB():
    try:
        conn = mysql.connector.connect(host = MYSQL_DB_HOST,
                                       database = MYSQL_DB_NAME,
                                       user = MYSQL_DB_USER,
                                       password = MYSQL_DB_PASS)
        if conn.is_connected():
            print('Connected to MySQL database!')
            return conn
    
    except Error as e:
        print(e)
                
#Выборка пользователей из БД с введенным username ----- РАБОТАЕТ
def selectUsernameFromDB(s_user):
    query = "SELECT * from loginUser where `username` = '%s'" % (s_user.username.data)      
    print(query)
    try:
        conn = connectDB()
        
        cursor = conn.cursor()
        cursor.execute(query)     
        cursor.fetchall()
        result = cursor.rowcount
        
        cursor.close()
        conn.close()
        
        print("Result=",result)
        return(result)
        
    except Error as e:
        print ('Error: ', e)
        return(-1)

#Выборка пользователей из БД с введенным email ----- РАБОТАЕТ
def selectEmailFromDB(s_user):
    query = "SELECT * from loginUser where `email` = '%s'" % (s_user.email.data)      
    print(query)
    try:
        conn = connectDB()
        
        cursor = conn.cursor()
        cursor.execute(query)     
        cursor.fetchall()
        result = cursor.rowcount
        
        cursor.close()
        conn.close()
        
        print("Result=",result)
        return(result)
        
    except Error as e:
        print ('Error: ', e)
        return(-1)

                            
class User:
    
    def __init__(self, username, email, password, role):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.role = role
    
    def signUpUser(self):
        query = "INSERT INTO loginUser (`username`, `email`, `password`) VALUES (%s, %s, %s)"       
        try:
            conn = connectDB()
            cursor = conn.cursor()
            cursor.execute(query, (self.username, self.email, self.password))
            conn.commit()
            print ("Commit!")
            
        except Error as e:
            print ('Error: ', e)
            return(1)
        
        finally:
            cursor.close()
            conn.close()       
    