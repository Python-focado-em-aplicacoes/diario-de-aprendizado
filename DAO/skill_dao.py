from database import connector

def create_skills_table():
    connector.run_db_operation(lambda cursor: cursor.execute('''
        CREATE TABLE IF NOT EXISTS skills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL
        )
        '''
    ))

def add_skill(name, category):
    return connector.run_db_operation(lambda cursor: cursor.execute('INSERT INTO skills (name, category) VALUES (?, ?)', (name, category)))

def get_skills():
    def get_skills_closure(cursor):
        cursor.execute('SELECT * FROM skills')
        return cursor.fetchall() #retorna as skills
    
    return connector.run_db_operation(get_skills_closure)