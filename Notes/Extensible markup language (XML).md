
# Extensible markup language (XML)

XML (eXtensible Markup Language) is a language and a format used for storing and transmitting data. XML is a native file format used in Windows systems. XML syntax uses the following:

- Tags
- Elements
- Attributes

## Tags

XML uses tags to store and identify data. Tags are pairs that must contain a start tag and an end tag. The start tag encloses data with angle brackets, for example `<tag>`,  whereas the end of a tag encloses data with angle brackets and a forward slash like this: `</tag>`.

## Elements

XML elements include both the data contained inside of a tag and the tags itself. All XML entries must contain at least one root element. Root elements contain other elements that sit underneath them, known as child elements.

Here is an example:

```
<Event>
	<EventID>4688</EventID>
	<Version>5</Version>
</Event>
```

In this example, `<Event>` is the root element and contains two child elements `<EventID>` and `<Version>`. There is data contained in each respective child element.

## Attributes

XML elements can also contain attributes. Attributes are used to provide additional information about elements. Attributes are included as the second part of the tag itself and must always be quoted using either single or double quotes.

For example:

```
<EventData> 
	<Data Name='SubjectUserSid'>S-2-3-11-160321</Data> 
	<Data Name='SubjectUserName'>JSMITH</Data> 
	<Data Name='SubjectDomainName'>ADCOMP</Data> 
	<Data Name='SubjectLogonId'>0x1cf1c12</Data> 
	<Data Name='NewProcessId'>0x1404</Data> 
</EventData>
```

In the first line for this example, the tag is `<Data>` and it uses the attribute  `Name='SubjectUserSid'` to describe the data enclosed in the tag `S-2-3-11-160321`.