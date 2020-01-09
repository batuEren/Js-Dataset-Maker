import re
import requests
import math
import jsbeautifier

testUrl = "https://apple.com/metrics/target/scripts/1.0/at.js"

js_keywords = ["break", "case", "catch", "continue", "debugger", "default", "delete", "do", "else", "finally", "for", "function", "if", "in", "instanceof", "new", "return", "switch", "this", "throw", "try", "typeof", "var", "void", "while", "with"]


def parseJavascript(url):
    r = requests.get(url, allow_redirects=False)
    temp_code = r.content.decode("ISO-8859-1")
    js_code = jsbeautifier.beautify(temp_code)
    
    
    noOfEvalFunc = len(re.findall("eval\(", js_code))
    noOfSetTimeOutFunc = len(re.findall("setTimeout\(", js_code))
    noOfiframe = len(re.findall("iframe", js_code))
    noOfUnescapeFunc = len(re.findall("unescape\(", js_code))
    noOfEscapeFunc = len(re.findall("escape\(", js_code))
    noOfClassid = len(re.findall("classid", js_code))
    noOfParseIntFunc = len(re.findall("parseInt\(", js_code))
    noOfFromCharCodeFunc = len(re.findall("fromCharCode\(", js_code))
    noOfActiveXObjectFunc = len(re.findall("ActiveXObject\(", js_code))
    noOfStringAssigments = len(re.findall(r'"((?<=\\)"|([^"]))"', js_code))
    noOfConcatFunc = len(re.findall("concat\(", js_code))
    noOfIndexOfFunc = len(re.findall("indexOf\(", js_code))
    noOfSubstringFunc = len(re.findall("substring\(", js_code))
    noOfReplaceFunc = len(re.findall("replace\(", js_code))
    noOfEventListenerFunc = len(re.findall("document.addEventListener\(", js_code))
    noOfAttachEventFunc = len(re.findall("attachEvent\(", js_code))
    noOfCreateElementFunc = len(re.findall("createElement\(", js_code))
    noOfGetElementByIdFunc = len(re.findall("getElementById\(", js_code))
    noOfDocumentWriteFunc = len(re.findall("document.write\(", js_code))
    noOfWords = len(re.findall(r'\w+', js_code)) 
    noOfKeyWords = findKeyWords(js_code)
    noOfCharacters = len(js_code)
    try:
        ratioOfKeywordsAndWords = noOfKeyWords / noOfWords
    except ZeroDivisionError:
        ratioOfKeywordsAndWords = 0
    entropyOfJS = Entropy(js_code)
    longestWord = len(findTheLongestWord(js_code))
    noOfLongStirngs = len(re.findall(r'"((?<=\\)"|([^"])){200,}"', js_code))
    shortestWord = len(findTheShortestWord(js_code))
    entropyOfLongestWord = Entropy(findTheLongestWord(js_code))
    noOfBlankSpaces = len(re.findall(" ", js_code))
    try:
        avgLenOfWords = noOfCharacters / noOfWords
    except ZeroDivisionError:
        avgLenOfWords = 0
    noOfHexValues = findHexNumbers(js_code)
    try:
        shareOfSpaceChar = len(re.findall(" ", js_code)) / noOfCharacters
    except ZeroDivisionError:
        shareOfSpaceChar = 0
    #print(noOfHexValues)
    

    
    return (noOfEvalFunc, noOfSetTimeOutFunc, noOfiframe, noOfUnescapeFunc, noOfEscapeFunc, noOfClassid, noOfParseIntFunc, noOfFromCharCodeFunc, noOfActiveXObjectFunc,
    noOfStringAssigments, noOfConcatFunc, noOfIndexOfFunc, noOfSubstringFunc, noOfReplaceFunc, noOfEventListenerFunc, noOfAttachEventFunc, noOfCreateElementFunc, noOfGetElementByIdFunc,
    noOfDocumentWriteFunc, noOfWords, noOfKeyWords, noOfCharacters, ratioOfKeywordsAndWords, entropyOfJS, longestWord, noOfLongStirngs, shortestWord, entropyOfLongestWord, noOfBlankSpaces,
    avgLenOfWords, noOfHexValues, shareOfSpaceChar)


def Entropy(string,base = 2.0): # I copied this from net
    dct = dict.fromkeys(list(string))

    pkvec =  [float(string.count(c)) / len(string) for c in dct]

    H = -sum([pk  * math.log(pk) / math.log(base) for pk in pkvec ])
    return H

def findTheLongestWord(text):
  tempList = text.split(' ')
  return max(tempList, key=len)

def findTheShortestWord(text):
  tempList = text.split(' ')
  return min(tempList, key=len)

"""def findLongStings(text):
    longs = []
    temp = re.findall(r'var = .*\".*\"', text)
    for string in temp:
        if len(string) > 200:
            longs.append(string)"""

def findKeyWords(text):
    numberOfKeywords = 0
    temp = re.findall(r'\w+', text)
    for word in temp:
        if word in js_keywords:
            numberOfKeywords += 1
    temp = re.findall(r'"((?<=\\)"|([^"]))"', text)
    for word in temp:
        if word in js_keywords:
            numberOfKeywords += -1
    return numberOfKeywords

def findHexNumbers(text):
    number = len(re.findall(r'0x', text)) + len(re.findall(r'parseInt\([^,]*,? *16\)', text))
    return number

#print(parseJavascript(testUrl))
