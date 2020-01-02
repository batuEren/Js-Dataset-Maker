import re
import requests

js_finder_regex = r'src=\"http.*\.js\"' #TODO is not working if the js file adressed like /folder/name/test.js  

testUrl = "https://www.alexa.com/topsites"

def findJsFiles(url):
    js_files = []
    r = requests.get(url, allow_redirects=False)
    html = r.content.decode("utf-8")
    temp_files = re.findall(js_finder_regex, html)
    for file in temp_files:
        file = file.replace('\"', '')
        file = file.replace('src=', '')
        js_files.append(file)
    return js_files 
    
