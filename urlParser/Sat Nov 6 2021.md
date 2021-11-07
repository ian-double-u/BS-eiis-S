# Build Something (even if it sucks) Saturday
Sat Nov 6 2021: The inagural edition
 
 ## Reflection
 I started this project on Saturday and continued it on Sunday to tie up some loose ends. Some but not all of the notes used to create the project can be found below. [Here](https://github.com/ian-double-u/BS-eiis-S/tree/main/urlParser) is the repo of the project, and [here](https://github.com/ian-double-u/BS-eiis-S/blob/main/urlParser/example.md) is an example of what it can do.
 
 The project also has local files at ```/Users/ian/jd/10-19 Code/22 BS-eiis-S/urlParser```.
 
 I think this was a great first project for BS(eiis)S, perhaps just BSS for short, because it was a totally doable project for a 1-2 day timeline. That being said it was not trivial and I spent a total of ~10 hours on it. It was short enough that I was able to actually start because I was not overwhelemed by all that I would have to do, but also long enough that after finishing I will be able ot look back on the weekend and feel proud of what I accomplished. 
 
 I originally wanted to write this in Haskell, but after a lot of frustration trying to get a requistie package with Cabal (because of an LLVM error) I gave up and decided to use Python. I am most familar with Python, and after reading *7 Languages in 7 Weeks* I can appretiate how everything just works as you would expect it to in Python. 
 
 This project did not require me to learn any new Python or regex, but it certinely was helpful to give me more experience with regex as well as to refamiliarize myself with Python, as it has been some time while I have been distracted with other languages.
 
 I am very much looking forward to whatever I tackle next weekend. I can also see, though the start of this tradition is fairly trivial (a url parser), how over the weeks I can start to expand what is possible for me to do and I can also build the muscle of building and not just vicariously living through other builders, as I often do when consumed with reading. 
 
 It will be a while before these Saturday projects approach something of the magnitude of what I currently attempt to live vicariously through, but you can only get there if you start. And I think it is very fair to say that this project was a great start.
 
 
 ## Scratch Notes
 
 [url parser](https://github.com/ian-double-u/BS-eiis-S/tree/main/urlParser) in ~~Haskell~~ Python (Cabal & LLVM will be the death of me)
 [example](https://github.com/ian-double-u/BS-eiis-S/blob/main/urlParser/example.md)
 
 The goal of the project is to take a url string and return each of it's eight (nine) parts in a reader friendly way (see [this](https://www.mattcutts.com/blog/seo-glossary-url-definitions/)).
 
 1. Protocol
	 1. on left of "://"
	 2. ```.+?(?=:\/\/)```
 2. Subdomain, Domain, TLD
	 1. "." seperated
	 2. ```:\/\/.+?(?=:)``` and ```:\/\/.+?(?=(\/|$))``` (depending on wether or not url has port, also grabs "://")
	 3. above grabs any subdomains, domain, any SLD, TLD. Split this on "." and look at two right most for SLD and TLD, then you can determine the domain, then you can determine any subdomains (remember to list subdomains in [order](https://en.wikipedia.org/wiki/Domain_Name_System#Domain_name_syntax,_internationalization))
	 4. look for first matches of SLD and TLD so you don't accidentally grab those that might be in the query of a url
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
	 2. ```\?.*?(?=#)``` and ```\?.*``` (depending on wether or not url has fragment, also grabs "?")
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
https://bhs.beaverton.k12.or.us/
http://localhost:8888/tree/jd/10-19%20Code/22%20BS-eiis-S/urlParser
 
 
Needed functions
- string has fragement √
- string has query √
- string has port √
	- use ```:\d{2,5}``` (includes ":")
- domains has sld
- tld of string
- sld of string
- take string and regex return match(es) √



 