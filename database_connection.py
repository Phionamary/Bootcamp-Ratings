import psycopg2

class DatabaseConnection():
    def __init__(self, mypassword):
        self.connection = psycopg2.connect(
            database="postgres",
            user="postgres",
            host="127.0.0.1",
            password=mypassword
        )
        self.cursor = self.connection.cursor()
        print("Connected to database")

    def create_user_table(self):
        sql = (
        	'''
        	CREATE TABLE IF NOT EXISTS "User"(
        		user_id serial PRIMARY KEY,
        		username varchar(50) NOT NULL,
        		email varchar(50) NOT NULL,
        		password varchar(20) NOT NULL,
        		role varchar(20) NOT NULL
        	);
        	'''
        )
        self.cursor.execute(sql)
        self.connection.commit()
        print("User table created")

password = input("Enter your password: ")
user = DatabaseConnection(password)
user.create_user_table()
