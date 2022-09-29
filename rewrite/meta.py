def metaRewrite(prefix, domain, requestURL, soup): 
    for link in soup.find_all('meta', content=True): # find all links
        if link['content'][0:2] == "//": # if link starts with //
            link['content'] = f"http:{link['content']}" # add http:
            link['content'] = "https://" + domain  + prefix + link['content'] # add domain and prefix
        elif link['content'][0:1] == "/": # if link starts with /
            link['content'] = "https://" + domain  + prefix + requestURL + link['content'] # add domain and prefix
        elif link['content'][0:4] == "http"or link['content'][0:4] == "https": # if link starts with http or https
            link['content'] = "https://" + domain + prefix + link['content']  # add domain and prefix


