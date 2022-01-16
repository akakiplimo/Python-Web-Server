# Web Server
> a basic HTTP web-server application which can listen on a configurable TCP port and serve both static HTML and dynamically generated HTML using Python programming language, 
  such as in the way Apache uses PHP. 
  Support only a restricted subset of HTTP, i.e. GET or POST requests, and the only headers it supports are Content-Type and Content-Length.

> Additionally implements a secure connection (HTTPS) using OpenSSL
  and a feature for URL rewriting, such as mod_rewrite in Apache.

## How To Run
- Generate key and cert files with OpenSSL use following command:
```  
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365___
```

- Run the pythone file using the command:
```
__python3 webServer.py__
```

- On the browser, check on the url below once running to access the index page
```
https://localhost:8000/index.html
```