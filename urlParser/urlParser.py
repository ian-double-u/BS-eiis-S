import re

def strRegexMatch(p,s):
    search = re.search(p,s)
    
    if search:
        return s[(search.span()[0]):(search.span()[1])]
    else:
        return ""
      
with open("slds.txt", "r") as file:
    sld_lines = file.readlines() 
    
sld_lines = [i for i in sld_lines if i[0:2] != "//" ]
sld_lines = [i for i in sld_lines if i != "\n"]
sld_lines = [i[2:] if i[0:2] == "*." else i for i in sld_lines]
sld_lines = [i[1:] if i[0] == "!" else i for i in sld_lines]
sld = [i[:-1] for i in sld_lines]

with open("tlds.txt", "r") as file:
    tld_lines = file.readlines()
    
tld = [i[:-1].lower() for i in tld_lines]

def urlParser(url,json=False):
    # --- pre-define empty fields to preserve desired order ---
    parsedUrl = {"protocol": "", "port": "",
                     "FQDN": "",
                     "domain": "",
                     "TLD": "",
                     "SLD": "",
                     "subdomain": "",
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
                    parsedUrl["FQDN"] = strRegexMatch(".+?((?=(\/))|(?=$))",url) 
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
    parsedUrl["FQDN"] = parsedUrl["FQDN"].lower()
    if parsedUrl["FQDN"][-1] == "/":
        parsedUrl["FQDN"] = parsedUrl["FQDN"][:-1]
    
    domain_split = parsedUrl["FQDN"].split(".")    
    
    if len(domain_split) > 1:
        FQDN = parsedUrl["FQDN"]
        while FQDN not in sld:
            FQDN = FQDN[1:]

        parsedUrl["SLD"] = "." + FQDN

        tld_matches = [i for i in tld if i in parsedUrl["SLD"]]

        parsedUrl["TLD"] = "." + [d for d in domain_split if d in tld_matches][-1]
        parsedUrl["domain"] = [d for d in domain_split if d not in parsedUrl["SLD"]][-1]
        parsedUrl["subdomain"] = "".join([d for d in domain_split if d not in (parsedUrl["domain"]+parsedUrl["SLD"])])
    
    # --- SLD correction ---
    if parsedUrl["SLD"] == parsedUrl["TLD"]:
        parsedUrl["SLD"] = ""
    
    # --- return ---
    if json:
        return parsedUrl
    else:
        print(f"url: {url}\n")
        for key in parsedUrl:
            if parsedUrl[key]:
                print(f"{key}: {parsedUrl[key]}")
