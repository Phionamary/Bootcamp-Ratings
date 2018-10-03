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

    def signup(self, user_dict):
    	sql = (
    		'''
    		INSERT INTO "User"(user_id, username, email, password, role)
    		VALUES(DEFAULT, %s, %s, %s, %s) RETURNING user_id, username, email, password, role;
    		'''
    	)
    	self.cursor.execute(sql, [user_dict['username'], user_dict['email'], user_dict['password'], user_dict['role']])
    	self.connection.commit()
        print("User added")

    def rate_user(self, score_dict):
    	sql = (
    		'''
    		INSERT INTO "Score"(user_id, excellence, passion, integrity, collaboration)
    		VALUES(%s, %s, %s, %s, %s) RETURNING user_id, excellence, passion, integrity, collaboration;
    		'''
    	)
    	self.cursor.execute(sql, [score_dict['user_id'], score_dict['excellence'], score_dict['passion'], score_dict['integrity'], score_dict['collaboration']])
    	self.connection.commit()
    	print ("score updated")

user = DatabaseConnection("maria")
user.create_user_table()
user.create_scores_table()
