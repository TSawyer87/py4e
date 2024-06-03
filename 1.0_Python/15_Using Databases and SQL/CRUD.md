#Databases 

- Structured Query Language is the language we use to issue commands to the database. It is basically an API between us and the DB.
- CRUD:
- Create a table
- Retrieve some data
- Insert data
- Delete data

```sql
CREATE TABLE Users(
  name VARCHAR(128),
  email VARCHAR(128)
)
```

- Maximum size 128 Characters per variable

# SQL Insert

- The insert statement inserts a row into a table
```sql
INSERT INTO Users(name,email) VALUES('Kristin','kf@umich.edu') 
```

# SQL Delete

- Deletes a row in a table based on a selection criteria
```sql
DELETE FROM Users WHERE email='sawyerjr.25@gmail.com'
```
- You can copy and paste these in the Execute SQL section of db browser and they work..

# SQL Update

- Allows the updating of a field with a where clause.
```sql
UPDATE Users SET name='chucky' WHERE email='csev@umich.com'
```

# SQL Select(Retrieving Records)

- The select statement retrieves a group of records - you can either retrieve all the records or a subset of the records with a WHERE clause.
```sql
SELECT * FROM Users  
```

```sql
SELECT * FROM Users WHERE email='csev@umich.com'
```

# Sorting with ORDER BY

- You can add an ORDER BY clause to SELECT statements to get the results sorted in ascending or descending order
```sql
SELECT * FROM Users ORDER BY email
SELECT * FROM Users ORDER BY name
```
- DB's sort very well!
