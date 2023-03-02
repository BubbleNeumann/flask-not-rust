import sqlite3

DB_FILE = 'database.db'

def run_select(query: str) -> list:
    connection = sqlite3.connect(DB_FILE)
    res = connection.cursor().execute(query).fetchall()
    connection.close()
    return res

def modify_table(query: str, con=None) -> int | None:
    """
    Performs queries which require table modification.
    Return new row id in case of insert. Otherwise return None.
    """
    con_was_passed = True if con is not None else False
    if con is None:
        con = sqlite3.connect(DB_FILE)
    cur = con.cursor()
    cur.execute(query)
    new_row_id = cur.lastrowid if query.split(' ')[0] == 'insert' else None
    con.commit()
    if not con_was_passed:
        con.close()

    return new_row_id

