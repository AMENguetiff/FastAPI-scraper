import sqlite3

def database(post_data):
    # Connect to SQLite database
    conn = sqlite3.connect('facebook_data.db')
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute('''CREATE TABLE IF NOT EXISTS facebook_data
                    (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Content TEXT,
                    Likes TEXT,
                    Shares TEXT,
                    Comments INTEGER,
                    Users INTEGER)''')

    # Insert data into the table
    for post in post_data:
        # Insert post data
        cursor.execute('''INSERT INTO facebook_data (Content, Likes, Shares, Comments, Users) 
                       VALUES (?, ?, ?, ?, ?)''', 
                       (post['Post Content'], post['Likes'], post['Shares'], post['Comments Count'], post['Users Commented']))

    # Commit changes and close the database connection
    conn.commit()
    conn.close()
