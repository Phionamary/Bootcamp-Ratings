import psycopg2

class DatabaseConnection():
    def __init__(self, mypassword):
        self.connection = psycopg2.connect(
            database="postgres",
            user="postgres",
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

    def create_scores_table(self):
       sql = (
           '''
           CREATE TABLE IF NOT EXISTS "Score"(
               user_id INTEGER NOT NULL,
               excellence INTEGER NOT NULL,
               passion INTEGER NOT NULL,
               integrity INTEGER NOT NULL,
               collaboration INTEGER NOT NULL,
               FOREIGN KEY(user_id) REFERENCES "User"(user_id) ON DELETE CASCADE
           );
           '''
       )
       self.cursor.execute(sql)
       self.connection.commit()
       print("Score table created")

user = DatabaseConnection("maria")
user.create_user_table()
user.create_scores_table()
