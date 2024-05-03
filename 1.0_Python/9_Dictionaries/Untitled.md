#Dictionaries

A *dictionary* is like a list, but more general. In a list, the index positions have to be integers; in a dictionary, the indices can be (almost) any type.
- You can think of a dictionary as a mapping between a set of indices (*keys*), and a set of values.
- Each key maps to a value.
- The association of a key and a value is called a *key-value pair* or sometimes an *item*.

In this example we'll map English to Spanish words in a dictionary, so the keys and the values are all strings.

The function **dict** creates a new dictionary with no items. 
```
eng2sp = dict()
print(eng2sp)
```
`Out:`
`{}`
- The curly brackets, {}, represent an empty dictionary.
- To add items to the dictionary, you can use square brackets:
- `eng2sp['one'] = 'uno'`
- This line creates an item that maps from key 'one' to the value "uno".
- If we print the dict again, we see a key-value pair with a colon between the key and the value:
- `print(eng2sp)`
- `Out:`
- `{'one' : 'uno'}`

This output format is also an input format. You can create a new dictionary with three items.
- But if you print eng 2 sp, you might be surprised:
```
 eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
 print(eng2sp)
```
`Out:`
`{'one': 'uno', 'three': 'tres', 'two': 'dos'}`
- The order of the key-value pairs is not the same.
- In general, the order of items in a dictionary are unpredictable.
- But it's not a problem because dictionaries are indexed with keys rather than integers:
```
print(eng2sp['two'])
```
`'dos'`
- The key **'two** always maps to the value "dos" so the order of the items doesn't matter.
If the key isn't in the dictionary, you get an exception:
```
print(eng2sp['four'])
KeyError: 'four'
```

The **len** function works on dictionaries; it returns the number of key-value pairs:
```
len(eng2sp)
3
```

The **in** operator works on dictionaries; it tells you whether something appears as a *key* in the dict (appearing as a value is not good enough):
```
'one' in eng 2 sp
True
'uno' in eng 2 sp
False```
```

The **values** method returns the values as a type that can be converted to a list, and then use the **in** operator:
```
vals = list(eng2sp.values())
'uno' in vals
True
```

The **in** operator uses different algorithms for lists and dictionaries.
- For lists, it uses a linear search algorithm. As the list gets longer, the search time gets longer...
- For dictionaries, Py uses an algorithm called a *hash table* that has a remarkable property: the **in** operator takes about the same time no matter how many items there are in a dict.