# Using urlParser
This module takes any properly formatted url, parses it, and returns the results (either by printing or returning a dictionary).

For example

```urlParser("https://google.com")```

will print

```
url: [https://google.com](https://google.com/)

protocol: https
FQDN: google.com
domain: google
TLD: .com
path: /
```

The parser can parse all parts of a url including protocol, subdomain(s), domain, all 13k+ SLDs, all TLDs, port, path, query, and fragment. 

For example, see

```
urlParser("http://b.bhs.beaverton.k12.or.us:80/about/?class=math#schedule")
```

will print

```
url: http://b.bhs.beaverton.k12.or.us:80/about/?class=math#schedule

protocol: http
port: 80
FQDN: b.bhs.beaverton.k12.or.us
domain: beaverton
TLD: .us
SLD: .k12.or.us
subdomain: b.bhs
path: /about/
query: class=math
parameters: {'class': 'math'}
fragment: schedule
```

You can also return the result as a dict by using 

```
urlParser(url,json=True)
```

For example, see

```
urlParser("https://www.spectator.co.uk/",json=True)["SLD"] == ".co.uk"
>>> True
```
