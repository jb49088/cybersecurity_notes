
# Proxy auto-configuration (PAC)

Proxy Auto-Configuration (PAC) is a mechanism used to automatically determine which proxy server, if any, a web browser should use to access the internet. PAC files help manage network traffic by directing client requests to the appropriate proxy servers based on the URL or other criteria.

Example PAC file:

```javascript
function FindProxyForURL(url, host) {
    if (shExpMatch(url, "*.example.com/*")) {
        return "PROXY proxy.example.com:8080";
    }
    if (shExpMatch(url, "*.anotherdomain.com/*")) {
        return "PROXY anotherproxy.example.com:8080";
    }
    return "DIRECT";
}
```
