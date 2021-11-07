import re

def strRegexMatch(p,s):
    search = re.search(p,s)
    
    if search:
        return s[(search.span()[0]):(search.span()[1])]
    else:
        return ""
      
def urlParser(url,json=False):
    # --- pre-define empty fields to preserve desired order ---
    parsedUrl = {"protocol": "", "port": "",
                     "FQDN": "",
                     "domain": "",
                     "TLD": "",
                     "SLD": "",
                     "subdomin": "",
                     "path": "/",
                     "query": "",
                     "parameters": {},
                     "fragment": ""}
    
    # -- port --
    if re.search(":\d{2,5}", url): 
        parsedUrl["port"] = strRegexMatch(":\d{2,5}",url)[1:] 
    
    # -- query --
    if "?" in url: 
        
        # -- fragment --
        if "#" in url: 
            parsedUrl["query"] = strRegexMatch("\?.*?(?=#)",url)[1:] 
        else: 
            parsedUrl["query"] = strRegexMatch("(\?.*)",url)[1:]   
            
        # --- parameters ---
        parameter_split = parsedUrl["query"].split("&")
        parameter_pairs = [(strRegexMatch(".+?(?=\=)",i),strRegexMatch("\=(.*)",i)[1:]) for i in parameter_split]
        parsedUrl["parameters"] = {key:val for (key,val) in parameter_pairs}
    
    # -- fragment --
    if "#" in url: 
        parsedUrl["fragment"] = strRegexMatch("#.*",url)[1:] 
        
    # -- protocol --
    if re.search(".+?(?=:\/\/)", url): 
        parsedUrl["protocol"] = strRegexMatch(".+?(?=:\/\/)",url) 
        
    # --- domains ---
    if re.search(".+?(?=:\/\/)", url):
        if re.search(":\d{2,5}", url):
            parsedUrl["FQDN"] = strRegexMatch(":\/\/.+?(?=:)",url)[3:]
        else:
            if "?" in url:
                parsedUrl["FQDN"] = strRegexMatch(":\/\/.+?(?=\?)",url)[3:]
            else:
                parsedUrl["FQDN"] = strRegexMatch(":\/\/.+?(?=(\/|$))",url)[3:]
    else:
        if "?" in url:
            parsedUrl["FQDN"] = strRegexMatch(".+?(?=\?)",url)
        else:
            if "#" in url:
                parsedUrl["FQDN"] = strRegexMatch(".+?(?=#)",url)
            else:
                parsedUrl["FQDN"] = url
        
    # --- (subdomain(s)), domain, (SLD(s)), TLD ---
    domain_split = parsedUrl["FQDN"].split(".")
    
    TLDs = []
    SLDs = []     
    
    # 1. Identify and remove TLD
    # 2. Identify and remove any SLDs
    # 3. domain is [-1] subdomains are [0:-1]
    
    
    """
    "domain": "",
    "SLD": "",
    "TLD": "",
    "subdomin": "",
    """
    
    # --- path ---
    if re.search(":\d{2,5}", url):
        if "?" in url:
            parsedUrl["path"] = strRegexMatch("\d\/.*\?",url)[1:-1]
        else:
            if "#" in url:
                parsedUrl["path"] = strRegexMatch("\d\/.*#",url)[1:]
            else:
                parsedUrl["path"] = strRegexMatch("\d\/.*$",url)[1:]
    else:
        if "?" in url:
            parsedUrl["path"] = strRegexMatch("[a-z]\/.*\?",url)[1:-1]
        else:
            if "#" in url:
                parsedUrl["path"] = strRegexMatch("[a-z]\/.*#",url)[1:]
            else:
                if re.search("[a-z]\/.*$", url):
                    parsedUrl["path"] = parsedUrl["path"] = strRegexMatch("[a-z]\/.*$",url)[1:]
    
    # -- return --
    if json:
        return parsedUrl
    else:
        print(f"url: {url}\n")
        for key in parsedUrl:
            if parsedUrl[key]:
                print(f"{key}: {parsedUrl[key]}")
                
test_list = [
     "https://video.google.co.uk:443/videoplay?docid=-7246927612831078230&hl=en#00h02m30s",
     "https://video.google.co.uk",
     "https://video.youtube.co.uk/videoplay?docid=-7246927612831078230&hl=en#00h02m30s",
     "https://video.facebook.co.uk/videoplay?docid=-7246927612831078230&hl=en",
     "https://video.snapchat.co.uk/videoplay#00h02m30s",
     "https://video.twitter.co.uk/videoplay",
     "https://video.twitter.co.uk/videoplay/v",
     "https://bhs.beaverton.k12.or.us/",
]

for u in test_list:
    print("\n")
    urlParser(u)
