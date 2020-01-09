import re
import requests

js_finder_regex = r'src? *=? *"((?<=\\)"|([^"]))*."'

testUrl = "https://www.alexa.com/topsites"

domainEnds = [".com",".org",".xyz"]

def findJsFiles(url):
    js_files = []
    r = requests.get(url)
    html = r.content.decode("ISO-8859-1")
    #print(html)
    r = re.compile(r'src? *=? *"(((?<=\\)"|([^"]))*..js)"') #TODO if protocol is missing add it
    temp_files = [x[0] for x in r.findall(html)]# sadece / varsa adresi ekle, // varsa basina http ekle
    #print(temp_files)
    for file in temp_files:
        if file.startswith("//"):
            file = "http:" + file
            js_files.append(file)
        elif file.startswith("/"):
            file = url + file
            js_files.append(file)
        elif file.startswith("www"):
            file = "http://" + file
            js_files.append(file)
        else:
            js_files.append(file)
        #    fullFileId = url + file
        #    js_files.append(fullFileId)
    return js_files
    
#print(findJsFiles(testUrl))
