
# JavaScript Object Notation (JSON)

JavaScript Object Notation (JSON) is a file format that is used to store and transmit data. JSON is known for being lightweight and easy to read and write. It is used for transmitting data in web technologies and is also commonly used in cloud environments. JSON syntax is derived from JavaScript syntax. If you are familiar with JavaScript, you might recognize that JSON contains components from JavaScript including:

- Key-value pairs
- Commas
- Double quotes
- Curly brackets
- Square brackets

## Key-value pairs

A **key-value** **pair** is a set of data that represents two linked items: a key and its corresponding value. A key-value pair consists of a key followed by a colon, and then followed by a value. An example of a key-value pair is  "`Alert": "Malware"`.

> [!Note]
> For readability, it is recommended that key-value pairs contain a space before or after the colon that separates the key and value.

## Commas

Commas are used to separate data. For example: `"Alert": "Malware", "Alert code": 1090, "severity": 10`.

## Double quotes

Double quotes are used to enclose text data, which is also known as a string, for example:  `"Alert": "Malware"`. Data that contains numbers is not enclosed in quotes, like this: `"Alert code": 1090`.

## Curly brackets

Curly brackets enclose an **object**, which is a data type that stores data in a comma-separated list of key-value pairs. Objects are often used to describe multiple properties for a given key. JSON log entries start and end with a curly bracket. In this example, `User` is the object that contains multiple properties:

```
"User": 
{  
	"id": "1234",  
	"name": "user", 
	"role": "engineer" 
}
```

## Square brackets

Square brackets are used to enclose an **array**, which is a data type that stores data in a comma-separated ordered list. Arrays are useful when you want to store data as an ordered collection, for example: `["Administrators", "Users", "Engineering"]`.