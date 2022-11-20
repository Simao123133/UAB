import sqlite3
con = sqlite3.connect("exercise4.db")
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS counter (
            id integer PRIMARY KEY,
            city text,
            active INTEGER
            )""")

cur.execute("""CREATE TABLE IF NOT EXISTS client (
            name text PRIMARY KEY,
            address text,
            city text
            )""")

cur.execute("""CREATE TABLE IF NOT EXISTS deposit (
            counter_id integer,
            account_id integer,
            client_name text,
            balance real,
            PRIMARY KEY (counter_id, account_id),
            FOREIGN KEY(client_name) REFERENCES client(name),
            FOREIGN KEY(counter_id) REFERENCES counter(id)
            )""")

cur.execute("""CREATE TABLE IF NOT EXISTS loan (
            counter_id integer,
            loan_id integer,
            client_name text,
            amount real,
            PRIMARY KEY (counter_id, loan_id),
            FOREIGN KEY(client_name) REFERENCES client(name),
            FOREIGN KEY(counter_id) REFERENCES counter(id)
            )""")



con.commit()
con.close()