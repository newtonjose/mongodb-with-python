# BSON (Binary JSON)

- 1. Binary Format
- 2. Rich Data Types
> ObjectId
> Date
> Binary Data
> Regular Expressions
> Decimal128
> Embedded Documents
- 3. Size
- 4. Indexing 

# BSON Documents Structure
key-value pair
```bson
{
    "_id": ObjectId("60c72b2f9b1e8b001c8e4e1a"),
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com",
    "created_at": ISODate("2021-06-14T12:00:00Z"),
    "is_active": true,
    "tags": ["developer", "python", "mongodb"],
    "profile": {
        "bio": "Software developer with a passion for open source.",
        "location": "New York"
    }
}
```