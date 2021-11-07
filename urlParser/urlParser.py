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
    
    if "://" in url:
        if re.search(":\d{2,5}", url): 
            if "?" in url:
                if "#" in url:
                    # --- protocol, port, query, fragment --- 
                    parsedUrl["protocol"] = strRegexMatch(".+?(?=:\/\/)",url)
                    parsedUrl["port"] = strRegexMatch(":\d{2,5}",url)[1:]
                    parsedUrl["FQDN"] = strRegexMatch(":\/\/.+?(?=:)",url)[3:]
                    parsedUrl["path"] = strRegexMatch("\d\/.*\?",url)[1:-1]
                    parsedUrl["query"] = strRegexMatch("\?.*?(?=#)",url)[1:]
                    parsedUrl["fragment"] = strRegexMatch("#.*",url)[1:]
                
                else:
                    # --- protocol, port, query --- 
                    parsedUrl["protocol"] = strRegexMatch(".+?(?=:\/\/)",url)
                    parsedUrl["port"] = strRegexMatch(":\d{2,5}",url)[1:]
                    parsedUrl["FQDN"] = strRegexMatch(":\/\/.+?(?=:)",url)[3:]
                    parsedUrl["path"] = strRegexMatch("\d\/.*\?",url)[1:-1]
                    parsedUrl["query"] = strRegexMatch("(\?.*)",url)[1:]
                   
            else:
                if "#" in url:
                    # --- protocol, port, fragment ---- 
                    parsedUrl["protocol"] = strRegexMatch(".+?(?=:\/\/)",url) 
                    parsedUrl["port"] = strRegexMatch(":\d{2,5}",url)[1:]
                    parsedUrl["FQDN"] = strRegexMatch(":\/\/.+?(?=:)",url)[3:] 
                    parsedUrl["path"] = strRegexMatch("\d\/.*#",url)[1:-1] 
                    parsedUrl["fragment"] = strRegexMatch("#.*",url)[1:]
                    
                    
                else:
                    # --- protocol, port --- 
                    parsedUrl["protocol"] = strRegexMatch(".+?(?=:\/\/)",url) 
                    parsedUrl["port"] = strRegexMatch(":\d{2,5}",url)[1:] 
                    parsedUrl["FQDN"] = strRegexMatch(":\/\/.+?(?=:)",url)[3:] 
                    parsedUrl["path"] = strRegexMatch("\d\/.*$",url)[1:] 
                    
        else:
            if "?" in url:
                if "#" in url:
                    # --- protocol, query, fragment --- 
                    parsedUrl["protocol"] = strRegexMatch(".+?(?=:\/\/)",url) 
                    parsedUrl["FQDN"] = strRegexMatch(":\/\/.+?(?=((\/|$)|(\?|#)))",url)[3:] 
                    parsedUrl["path"] = strRegexMatch("[a-z]\/.*\?",url)[1:-1] 
                    parsedUrl["query"] = strRegexMatch("\?.*?(?=#)",url)[1:] 
                    parsedUrl["fragment"] = strRegexMatch("#.*",url)[1:] 
                    
                    
                else:
                    # --- protocol, query --- 
                    parsedUrl["protocol"] = strRegexMatch(".+?(?=:\/\/)",url) 
                    parsedUrl["FQDN"] = strRegexMatch(":\/\/.+?(?=((\/|$)|(\?|#)))",url)[3:] 
                    parsedUrl["path"] = strRegexMatch("[a-z]\/.*\?",url)[1:-1] 
                    parsedUrl["query"] = strRegexMatch("\?.*",url)[1:] 
                           
            else:
                if "#" in url:
                    # --- protocol, fragment --- 
                    parsedUrl["protocol"] = strRegexMatch(".+?(?=:\/\/)",url) 
                    parsedUrl["FQDN"] = strRegexMatch(":\/\/.+?(?=((\/|$)|(\?|#)))",url)[3:] 
                    parsedUrl["path"] = strRegexMatch("[a-z]\/.*#",url)[1:-1] 
                    parsedUrl["fragment"] = strRegexMatch("#.*",url)[1:] 
                    
                    
                else:
                    # --- protocol --- 
                    parsedUrl["protocol"] = strRegexMatch(".+?(?=:\/\/)",url) 
                    parsedUrl["FQDN"] = strRegexMatch(":\/\/.+?(?=((\/|$)|(\?|#)))",url)[3:] 
                    parsedUrl["path"] = strRegexMatch("[a-z]\/.*$",url)[1:] 
            
    else:
        if re.search(":\d{2,5}", url): 
            if "?" in url:
                if "#" in url:
                    # --- port, query, fragment --- 
                    parsedUrl["port"] = strRegexMatch(":\d{2,5}",url)[1:]
                    parsedUrl["FQDN"] = strRegexMatch(".+?(?=:)",url)
                    parsedUrl["path"] = strRegexMatch("\d\/.*\?",url)[1:-1] 
                    parsedUrl["query"] = strRegexMatch("\?.*?(?=#)",url)[1:] 
                    parsedUrl["fragment"] = strRegexMatch("#.*",url)[1:] 
                    
                else:
                    # --- port, query --- 
                    parsedUrl["port"] = strRegexMatch(":\d{2,5}",url)[1:]
                    parsedUrl["FQDN"] = strRegexMatch(".+?(?=:)",url)
                    parsedUrl["path"] = strRegexMatch("\d\/.*\?",url)[1:-1] 
                    parsedUrl["query"] = strRegexMatch("(\?.*)",url)[1:] 
                        
            else:
                if "#" in url:
                    # --- port, fragement --- 
                    parsedUrl["port"] = strRegexMatch(":\d{2,5}",url)[1:]
                    parsedUrl["FQDN"] = strRegexMatch(".+?(?=:)",url) 
                    parsedUrl["path"] = strRegexMatch("\d\/.*#",url)[1:-1] 
                    parsedUrl["fragment"] = strRegexMatch("#.*",url)[1:] 
                    
                else:
                    # --- port --- 
                    parsedUrl["port"] = strRegexMatch(":\d{2,5}",url)[1:]
                    parsedUrl["FQDN"] = strRegexMatch(".+?(?=:)",url) 
                    parsedUrl["path"] = strRegexMatch("\d\/.*$",url)[1:] 
                     
        else:
            if "?" in url:
                if "#" in url:
                    # --- query, fragment --- 
                    parsedUrl["FQDN"] = strRegexMatch(".+?(?=\?)",url) 
                    parsedUrl["path"] = strRegexMatch("[a-z]\/.*\?",url)[1:-1] 
                    parsedUrl["query"] = strRegexMatch("\?.*?(?=#)",url)[1:] 
                    parsedUrl["fragment"] = strRegexMatch("#.*",url)[1:] 
                    
                else:
                    # --- query --- 
                    parsedUrl["FQDN"] = strRegexMatch(".+?(?=\?)",url) 
                    parsedUrl["path"] = strRegexMatch("[a-z]\/.*\?",url)[1:-1] 
                    parsedUrl["query"] = strRegexMatch("\?.*",url)[1:] 
                           
            else:
                if "#" in url:
                    # --- fragement ---
                    parsedUrl["FQDN"] = strRegexMatch(".+?(?=(\/|#))",url) 
                    parsedUrl["path"] = strRegexMatch("[a-z]\/.*#",url)[1:-1] 
                    parsedUrl["fragment"] = strRegexMatch("#.*",url)[1:] 
                    
                else:
                    # --- ---
                    parsedUrl["FQDN"] = strRegexMatch(".+?(?=\/)",url) 
                    parsedUrl["path"] = strRegexMatch("[a-z]\/.*$",url)[1:] 
                    
    # --- parameters ---
    if parsedUrl["query"]:
        parameter_split = parsedUrl["query"].split("&")
        parameter_pairs = [(strRegexMatch(".+?(?=\=)",i),strRegexMatch("\=(.*)",i)[1:]) for i in parameter_split]
        parsedUrl["parameters"] = {key:val for (key,val) in parameter_pairs}
        
    # --- path correction ---
    if parsedUrl["path"] == "":
        parsedUrl["path"] = "/"
        
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
    
    # --- return ---
    if json:
        return parsedUrl
    else:
        print(f"url: {url}\n")
        for key in parsedUrl:
            if parsedUrl[key]:
                print(f"{key}: {parsedUrl[key]}")   
