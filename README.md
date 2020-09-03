# tdb
A toy database with python

# Usage

## Connecting to db
```
db = tdb("test.tdb")
```

## Adding entry
```
db.put("name","soubhik")
db.put("class","Alpha")
```

## Getting value for key
```
name = db.get("name")
```

## Deleting an entry
```
db.rm("class")
```

## Saving the changes
```
db.commit()
```
