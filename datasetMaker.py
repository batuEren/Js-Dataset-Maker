import jsFinder
import jsParser

url_list = []
js_list = []

for url in url_list:
    tempList = jsFinder.findJsFiles(url)
    js_list.append(tempList)
print(js_list)
for url in js_list:
    for js in url:
        data = jsParser.parseJavascript(js)
        print(data)
