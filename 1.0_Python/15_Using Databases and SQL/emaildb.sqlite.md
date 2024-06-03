#Databases 
```python
import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
```

Out:
```python
Enter file name: mbox-short.txt
cwen@iupui.edu 5
zqian@umich.edu 4
david.horwitz@uct.ac.za 4
louis@media.berkeley.edu 3
gsilver@umich.edu 3
stephen.marquard@uct.ac.za 2
rjlowe@iupui.edu 2
wagnermr@iupui.edu 1
antranig@caret.cam.ac.uk 1
gopal.ramasammycook@gmail.com 1
```

1. Importing and Connection:

    import sqlite3: Imports the sqlite3 module for working with SQLite databases.
    conn = sqlite3.connect('emaildb.sqlite'): Connects to a database named emaildb.sqlite. If it doesn't exist, a new one will be created.
    cur = conn.cursor(): Creates a cursor object to execute SQL statements on the database.

2. Table Management:

    cur.execute('DROP TABLE IF EXISTS Counts'): Drops the Counts table if it already exists. This ensures a clean slate for the new data.
    cur.execute('''CREATE TABLE Counts (email TEXT, count INTEGER)'''): Creates a new table named Counts with two columns:
        email (text): Stores the email address.
        count (integer): Stores the count of emails for that address's organization (domain name).

3. Processing Email File:

    fname = input('Enter file name: '): Prompts the user to enter the email file name.
    if (len(fname) < 1): fname = 'mbox-short.txt': If the user enters an empty string, the script defaults to using a file named mbox-short.txt.
    fh = open(fname): Opens the specified email file for reading.
    The loop iterates through each line in the file:
        if not line.startswith('From: '): continue: Skips lines that don't start with "From: " (assuming email addresses follow this format).
        pieces = line.split(): Splits the line into words (assuming the email address is the second word).
        email = pieces[1]: Extracts the email address from the line.
        Counting and Updating:
            The script attempts to select the count for the current email address using SELECT.
            If the email doesn't exist in the table (row is None):
                An INSERT statement adds a new row with the email and a count of 1.
            If the email already exists:
                An UPDATE statement increments the count for that email by 1.
            conn.commit(): Commits the changes to the database after each email is processed (this can be slow for large datasets).

4. Retrieving and Printing Top 10:

    sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10': Creates a query to select the email and count from the Counts table, ordered by count in descending order (most frequent first) and limited to the top 10 results.
    for row in cur.execute(sqlstr): Iterates through the results of the query.
    print(str(row[0]), row[1]): Prints the email address and its corresponding count for each row.

5. Closing Connection:

    cur.close(): Closes the database cursor object.

Running the Script:

    Save the code as a Python script (e.g., emaildb_optimized.py).
    Make sure you have Python and the sqlite3 module installed.
    Run the script from your terminal using python emaildb_optimized.py.
    If prompted, enter the email file name (or press Enter to use the default mbox-short.txt).
    The script will process the email data and print the top 10 email organizations and their corresponding message counts.

Optimization:

While the provided code works, it commits the changes to the database after each email is processed. This can be slow for large datasets. In the assignment prompt, it's mentioned that you can optimize the code by moving the conn.commit() statement outside the loop. This will significantly improve performance.
