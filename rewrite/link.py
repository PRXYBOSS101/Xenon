def linkRewrite(prefix, domain, requestURL, soup): 
    for link in soup.find_all('link', href=True): # find all links
        if link['href'][0:2] == "//": # if link starts with //
            link['href'] = f"http:{link['href']}" # add http:
            link['href'] = "https://" + domain  + prefix + link['href'] # add domain and prefix
        elif link['href'][0:1] == "/": # if link starts with /
            link['href'] = "https://" + domain  + prefix + requestURL + link['href'] # add domain and prefix
        elif link['href'][0:4] == "http"or link['href'][0:4] == "https": # if link starts with http or https
            link['href'] = "https://" + domain + prefix + link['href']  # add domain and prefix


