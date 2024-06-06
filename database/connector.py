import sqlite3
from typing import Optional, Callable

# conn = None
# cursor = None

# def connect_to_db():
#     global conn, cursor
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
    
# def disconnect_from_db():
#     global conn, cursor
#     conn.close()
    
# def get_database_connection():
#     global conn
#     return conn

def create_connection():
    return sqlite3.connect('database.db')

def run_db_operation(operation: Callable[[sqlite3.Cursor], None], connection: Optional[sqlite3.Connection] = None) -> None:
    if connection is None:
        connection = create_connection()
    
    to_return = operation(connection.cursor())
    
    connection.commit()
    connection.close()
    
    return to_return
