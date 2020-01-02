import re
import requests
import math

testUrl = "https://www.google-analytics.com/analytics.js"

def parseJavascript(url):
    r = requests.get(url, allow_redirects=False)
    js_code = r.content.decode("utf-8")
    #print(js_code)

    noOfEvalFunc = len(re.findall("eval\(", js_code))
    noOfSetTimeOutFunc = len(re.findall("setTimeout\(", js_code))
    noOfiframe = len(re.findall("iframe", js_code))
    noOfUnescapeFunc = len(re.findall("unescape\(", js_code))
    noOfEscapeFunc = len(re.findall("escape\(", js_code))
    noOfClassid = len(re.findall("classid", js_code))
    noOfParseIntFunc = len(re.findall("parseInt\(", js_code))
    noOfFromCharCodeFunc = len(re.findall("fromCharCode\(", js_code))
    noOfActiveXObjectFunc = len(re.findall("ActiveXObject\(", js_code))
    noOfStringAssigments = 0 #TODO Number of string direct assigments. I don't know what this means, yet.
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
    noOfKeyWords = 0 #TODO find the number of keywords
    noOfCharacters = len(js_code)
    ratioOfKeywordsAndWords = noOfKeyWords / noOfWords
    entropyOfJS = Entropy(js_code)
    longestWord = len(findTheLongestWord(js_code))
    noOfLongStirngs = 0 # TODO find strings longer than 200
    shortestWord = len(findTheShortestWord(js_code))
    entropyOfLongestWord = Entropy(findTheLongestWord(js_code))
    noOfBlankSpaces = len(re.findall(" ", js_code))
    avgLenOfWords = noOfCharacters / noOfWords
    noOfHexValues = 0 #TODO numbre of hex values in js
    shareOfSpaceChar = 0 #TODO share of space characters what does this means
    
    return (noOfCharacters, noOfEvalFunc, noOfSetTimeOutFunc, noOfiframe, noOfUnescapeFunc, noOfEscapeFunc, noOfClassid, noOfParseIntFunc, noOfFromCharCodeFunc, noOfActiveXObjectFunc,
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
