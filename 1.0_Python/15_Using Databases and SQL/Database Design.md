---
id: Database Design
aliases: []
tags: []
---

#Databases

- [Database Design](Database Design.md)

- Database design is an _art form_ of its own with particular skills & experience.

- Our goal is to avoid the really bad mistakes & design clean
  and easily understood databases.

- Others may performance tune things later.

- Database design starts with a picture (schema) of what you want the database
  to look like.

## Building a Data Model

- Drawing a picture of the data objects for our application and then figuring
  out how ro represent the objects & their relationships.
- Basic Rule: Don't put the same data in multiple tables. Use a relationship

- When there is one thing in the "real world" there should be one copy of
  that thing in the database.

### For each "piece of info"...

- Is the column an object or an attribute of another object?
- Once we define objects, we need to define the relationships between them.
- The structure of the data model creates the features of the application.

## Map logical to physical

- We add a primary key (a unique identifier) one key for every row.
- A primary key is a way for us to refer to a particular row, and so it's
  a unique number like 1, 2, 3, 4.

  - So each album is going to end up with a number.
  - We use that number in a column of a different table to point to it.

- The foreign key is one of these columns that we add to the starting point of
  the arrow.

- The Logical key is the unique identifier that we might use to look up
  this row from the outside world.
- So the logical key is really our way of saying we might use this
  in a WHERE clause or ORDER BY clause.

- Follow a Naming Convention.
- Create the ends of the arrows first, work from the outside in.
