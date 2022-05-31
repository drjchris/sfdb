# sfdb - SINGLE FILE DATABASE

## Warning: this is quite possibly not the dabase you are looking for.

## Concept

A very lite database for python that stores everything in JSON files.

Key principles and specifications.

1. Single database per file. Each JSON file will only have one "table"
2. Doesn't really do much. Just make db, add entry, edit and search.
3. Bring your own ID. No automatic db ids, you make your own.
4. Simplicity over performance...for now.

---

## Table of Content

 - [Creating a new db](#creating-db)
 - [Loading existing sfdb database](#loading-db)
 - [Adding an entry to the db](#add-entry)
 - [Searching the db](#searching-db)
 - [Saving all changes made](#commit)

---

## Createing a new db<a name="creating-db"></a>

    import sfdb

    sfdb.mkdb('mynewdb', dbdirectory, overwrite=False)

- __dbname:__ the actual name of the db being created.
- __dbdirectory:__ where the JSON file will be saved.
- __overwrite:__ Checks to see if file exsits before overwriting. Default is `false`.

__sfdb file structure__

    {
        '_meta': {
            'type': 'sfdb',
            'name': 'mynewdb',
            'info': '',
        }
        'data': {}
    }

Meta data provides some info about the databse itself. The `'type': 'sfdb'` thing is there to check that the JSON file is formated properly. But this is a future thing - not really checking in v-0.0.1.

`_data` is where all the db data lives.

---

## Loading existing sfdb database <a name="loading-db"></a>

    mydb = sfdb.loaddb(filepath)

In the current version (0.0.1) this will pretty much just load any old JSON file.

---

## Adding an entry to the db

Only one entry at a time. You need to supply your own id. The ID can pretty much be anyting you want

    myid = '0079A'
    newdata = {'thekey1':'the val', 'thekey2': 'bad val'}

    mydb.add(myid, newdata)

The entry will appear as follows in the JSON file:

    "_data": {
        "0079A": {
            "_dbid": "0079A",
            "thekey1": "the val",
            "thekey2": "bad val"
            }
        }
    }

It does check to make sure the ID has not been used yet. If it has, it will say `ERROR: ID 0079A already exists`.

---

## Edit an existing entry <a name="add-entry"></a>

You need to know the ID of that specific entry. The edit function will only change the value of an existing key or add a new `key: value`.

    myid = "0079A"
    newkeyvals = {"thekey2": "good val", "thekey3": "new val"}

    mydb.edit(theid, newkeyvals)

The entry will now appear as follows in the JSON file:

    "_data": {
        "0079A": {
            "_dbid": "0079A",
            "thekey1": "the val",
            "thekey2": "good val"
            "thekey3": "new val"
            }
        }
    }

It does check to make sure the ID already exists. If it doesn't it will `ERROR: ID 0079A not found`.

---

## Searching the db <a name="searching-db"></a>

Search terms need to be constructed as a dictionary and can only do one at a time. Returns a list.

    results = mydb.find({"_dbid": "0079A"})

or... 
   
    results = mydb.find({"thekey": "good val"})

That's it for now.

---
## Saving all changes made<a name="#commit"></a>

NOTE: sfdb will NOT save changes to the db unless you tell it to!

    mydb.commit()

This will save everything, including changes to the `_meta` data.