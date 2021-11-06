# Build Something (even if it sucks) Saturday
Sat Nov 6 2021: The inagural edition
 
 [url parser in Haskell](https://github.com/ian-double-u/BS-eiis-S/tree/main/urlParser)
 
 The goal of the project is to take a url string and return each of it's eight (nine) parts in a reader friendly way (see [this](https://www.mattcutts.com/blog/seo-glossary-url-definitions/)).
 
 1. Protocol
	 1. on left of "://"
	 2. ```.+?(?=:\/\/)```
 2. Subdomain, Domain, TLD
	 1. "." seperated
	 2. ```:\/\/.+?(?=:)``` and ```:\/\/.+?(?=(\/|$))``` (depending on wether or not url has port, also grabs "://")
	 3. above grabs any subdomains, domain, any SLD, TLD. Split this on "." and look at two right most for SLD and TLD, then you can determine the domain, then you can determine any subdomains (remember to list subdomains in [order](https://en.wikipedia.org/wiki/Domain_Name_System#Domain_name_syntax,_internationalization))
 5. Port
	 1. on right of ":"
	 2. ```:\d{2,3}\/``` (grabs ":" before and "/" after)
 6. Path
	 1. "/" seperated
	 2. ```[a-z]\/.*$``` (no query or fragment), ```[a-z]\/.*\?``` (has query, w or w/o fragment), ```[a-z]\/.*#``` (no query with fragment)
	 3. above grab "[a-z]/" and/or "?" or "#"
	 4. above assume url has no port, if there is a port then replace ```[a-z]``` with ```\d``` in regex and "[a-z]/" with "\d" in match
	 5. above grabs all directories in path. Split on "/" and remember to list paths in order
 7. Query
	 1. on right of "?"
	 2. ```\?.*?(?=#)``` and ```(\?.*)``` (depending on wether or not url has fragment, also grabs "?")
 8. Parameter
	 1. "&" seperated, key-val related by "="
	 2. strip "?" then seperate based on "&"
	 3. use ```.+?(?=\=)``` and ```\=(.*)``` on each of the above, for key and val, respectively (latter grabs "=")
 9. Fragment
	 1. on right of "#"
	 2. ```#.*``` (grabs "#" before)
 
 
 Regex Test urls:
 https://video.google.co.uk:443/videoplay?docid=-7246927612831078230&hl=en#00h02m30s
 https://video.google.co.uk
https://video.youtube.co.uk/videoplay?docid=-7246927612831078230&hl=en#00h02m30s
https://video.facebook.co.uk/videoplay?docid=-7246927612831078230&hl=en
https://video.snapchat.co.uk/videoplay#00h02m30s
https://video.twitter.co.uk/videoplay
https://video.twitter.co.uk/videoplay/v
 
 
Needed functions
- string has fragement
- string has query
- string has port
- domains has sld
- tld of string
- sld of string
- take string and regex return match(es)
 
 (add this to github repo)