# sfdb - SINGLE FILE DATABASE

## Warning: this is quite possibly not the database you are looking for.

## Concept

A very lite database for python that stores everything in JSON files.

Key principles and specifications.

1. Single database per file. Each JSON file will only have one "table"
2. Doesn't really do much. Just make db, add entry, edit and search.
3. Bring your own ID. No automatic db ids, you make your own.
4. Simplicity over performance...for now.

---

## Table of Content

 - [Installing](#install)
 - [Creating a new db](#creating-db)
 - [Loading existing sfdb database](#loading-db)
 - [Adding an entry to the db](#add-entry)
 - [Editing an existing entry](#edit-entry)
 - [Searching the db](#searching-db)
 - [Saving all changes made](#commit)

---
<a name="install"></a>

## Install

Make sure you have PIP installed.

    pip install "git+https://github.com/drjchris/sfdb.git#egg=sfdb"

To update to latest version you will have to uninstall first, then reinstall.

To check if you have the latest version

    pip show sfdb

---
<a name="creating-db"></a>

## Creating a new db

    import sfdb

    sfdb.mkdb('mynewdb', 'mydbfile.json', overwrite=False)


__sfdb file structure__

    {
        '_meta': {
            'type': 'sfdb',
            'name': 'mynewdb',
            'info': '',
        },
        'data': {}
    }

Meta data provides some info about the database itself. The `'type': 'sfdb'` thing is there to check that the JSON file is formatted properly. But this is a future thing - not really checking in v-0.0.2.

`_data` is where all the db data lives.

To add db information in the metadata

    mydb.addinfo("this is a nice table")

---
<a name="loading-db"></a>

## Loading existing sfdb database 

    mydb = sfdb.loaddb(filepath)

In the current version (0.0.2) this will pretty much just load any old JSON file.

---
<a name="add-entry"></a>

## Adding an entry to the db

Only one entry at a time. You need to supply your own id. The ID can pretty much be anything you want

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

It does check to make sure the ID has not been used yet. If it has, it will say `sfdb ERROR: ID "0079A" already exists`.

---
<a name="edit-entry"></a>

## Edit an existing entry 

You need to know the ID of that specific entry. The edit function will only change the value of an existing key or add a new `key: value`.

    myid = "0079A"
    newkeyvals = {"thekey2": "good val", "thekey3": "new val"}

    mydb.edit(myid, newkeyvals)

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

It does check to make sure the ID already exists. If it doesn't it will say `sfdb ERROR: ID "0079A" not found`.

---
<a name="searching-db"></a>

## Searching the db

Search terms need to be constructed as a dictionary and can only do one at a time. Returns a list.

    results = mydb.find({"_dbid": "0079A"})

or... 
   
    results = mydb.find({"thekey": "good val"})

That's it for now.

---
<a name="commit"></a> 

## Saving all changes made

NOTE: sfdb will NOT save changes to the db unless you tell it to!

    mydb.commit()

This will save everything, including changes to the `_meta` data.
