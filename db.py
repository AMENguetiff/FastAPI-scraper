import sqlite3

def database(post_data):
    conn = sqlite3.connect('facebook_data.db')
    cursor = conn.cursor()

    # Create table
    cursor.execute('''CREATE TABLE IF NOT EXISTS facebook_data
                    (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Content TEXT,
                    Likes TEXT,
                    Shares TEXT,
                    Comments INTEGER,
                    Users INTEGER)''')

    # Insert data
    for post in post_data:
        # Insert post data
        cursor.execute('''INSERT INTO facebook_data (Content, Likes, Shares, Comments, Users) 
                       VALUES (?, ?, ?, ?, ?)''', 
                       (post['Post Content'], post['Likes'], post['Shares'], post['Comments Count'], post['Users Commented']))

    conn.commit()
    conn.close()
