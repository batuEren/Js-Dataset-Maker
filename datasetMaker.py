import jsFinder
import jsParser
import requests
import sqlite3

conn = sqlite3.connect("js_test.db")
cursor = conn.cursor()

#url_list = ["http://google.com","http://microsoft.com","http://youtube.com"]
url_list = []

textFile = open("benignUrl.txt", "r")
urlText = textFile.readlines()
print(urlText)
for line in urlText:    
    url_list.append(line.replace("\n", ""))

print(url_list)

js_list = []

for url in url_list:
    tempList = jsFinder.findJsFiles(url)
    js_list.append(tempList)
print(js_list)
for url in js_list:
    for js in url:
        try :
            data = jsParser.parseJavascript(js)
            print(data)
            #cursor.execute("INSERT INTO js_data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? , ?)", (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13], data[14], data[15], data[16], data[17], data[18], data[19], data[20], data[21], data[22], data[23], data[24], data[25], data[26], data[27], data[28], data[29], data[30], data[31], 1))
        except requests.exceptions.RequestException:
            pass

conn.commit()
conn.close()
