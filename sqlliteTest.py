import sqlite3
conn = sqlite3.connect("js_test.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE js_data(
                noOfEvalFunc int,
                noOfSetTimeOutFunc int,
                noOfiframe int,
                noOfUnescapeFunc int,
                noOfEscapeFunc int,
                noOfClassid int,
                noOfParseIntFunc int,
                noOfFromCharCodeFunc int,
                noOfActiveXObjectFunc int,
                noOfStringAssigments int,
                noOfConcatFunc int,
                noOfIndexOfFunc int,
                noOfSubstringFunc int,
                noOfReplaceFunc int,
                noOfEventListenerFunc int,
                noOfAttachEventFunc int,
                noOfCreateElementFunc int,
                noOfGetElementByIdFunc int,
                noOfDocumentWriteFunc int,
                noOfWords int,
                noOfKeyWords int,
                noOfCharacters int,
                ratioOfKeywordsAndWords real,
                entropyOfJS real,
                longestWord int,
                noOfLongStirngs int,
                shortestWord int,
                entropyOfLongestWord real,
                noOfBlankSpaces int,
                avgLenOfWords real,
                noOfHexValues int,
                shareOfSpaceChar real,
                isBenign int
                )""")

#cursor.execute("INSERT INTO ids VALUES ( 'test1', 'test2', 10.5 )")

#cursor.execute("SELECT * FROM ids WHERE last='test2'")

#print(cursor.fetchall())

conn.commit()

conn.close()
