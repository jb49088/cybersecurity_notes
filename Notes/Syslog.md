
# Syslog

Syslog is a standard for logging and transmitting data. It can be used to refer to any of its three different capabilities: 

1. **Protocol**: The syslog protocol is used to transport logs to a centralized log server for log management. It uses port 514 for plaintext logs and port 6514 for encrypted logs.
   <br>
2. **Service**: The syslog service acts as a log forwarding service that consolidates logs from multiple sources into a single location. The service works by receiving and then forwarding any syslog log entries to a remote server.
   <br>
3. **Log format**: The syslog log format is one of the most commonly used log formats that you will be focusing on. It is the native logging format used in  Unix® systems. It consists of three components: a header, structured-data, and a message.

## Syslog log example

Here is an example of a syslog entry that contains all three components: a header, followed by structured-data, and a message:

```
<236>1 2022-03-21T01:11:11.003Z virtual.machine.com evntslog - ID01
[user@32473 iut="1" eventSource="Application" eventID="9999"]
This is a log entry!
```

### Header

The header contains details like the timestamp; the hostname, which is the name of the machine that sends the log; the application name; and the message ID.

- **Timestamp**: The timestamp in this example is `2022-03-21T01:11:11.003Z`, where `2022-03-21` is the date in YYYY-MM-DD format. T is used to separate the date and the time. `01:11:11.003` is the 24-hour format of the time and includes the number of milliseconds 003. Z indicates the timezone, which is Coordinated Universal Time (UTC).
  <br>
- **Hostname**: `virtual.machine.com`
  <br>
- **Application**: `evntslog`
  <br>
- **Message** **ID**: `ID01`

### Structured-data

The structured-data portion of the log entry contains additional logging information. This information is enclosed in square brackets and structured in key-value pairs. Here, there are three keys with corresponding values: `[user@32473 iut="1" eventSource="Application" eventID="9999"]`.

### Message

The message contains a detailed log message about the event. Here, the message is `This is a log entry!`.

### Priority (PRI)

The priority (PRI) field indicates the urgency of the logged event and is contained with angle brackets. In this example, the priority value is `<236>` . Generally, the lower the priority level, the more urgent the event is.

> [!Note]
> Syslog headers can be combined with JSON, and XML formats. Custom log formats also exist.

