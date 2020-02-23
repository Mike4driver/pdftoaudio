import os
import re
import sys
import requests
from SapiHelper import Sapi
from selenium import webdriver


def pdfToText(pdfFile):
        os.system(f"node pdftext.js {pdfFile}")
        pdfFileName = pdfFile
        pdfFile = pdfFile.split(".")
        pdfFile.pop()
        newFileName = pdfFile
        newFileName = ''.join(newFileName)
        # newFilename = pdfFile.split(".")[0]
        with open(f"{newFileName}.txt", 'r', encoding='ascii', errors='ignore') as f:
            text = f.readlines()

        text = ' '.join(text)
        return [newFileName, text, pdfFileName]

if __name__ == "__main__":
    
    # may take the following as arguments
    # url to download a pdf file
    # wiki page 
    # pdf file
    argType = sys.argv[1]

    if argType == "-u":
        print("Downloading pdf....")
        url = sys.argv[2]
        r = requests.get(url)
        fileName = url.split("/")[-1]
        with open(fileName, 'wb') as f:
            f.write(r.content)
        print(r.status_code)
        print(r.headers['content-type'])
        print(r.encoding)
        fileName, text, pdfFileName = pdfToText(fileName)

    elif argType == "-w":
        wikiLink = sys.argv[2]
        if wikiLink == "-r":
            wikiLink = 'https://en.wikipedia.org/wiki/Special:Random'
        os.environ["LANG"] = "en_US.UTF-8"
        browser = webdriver.Chrome(executable_path='Driver\chromedriver.exe')
        browser.get(wikiLink)
        bodyContent = browser.find_element_by_id('bodyContent')
        ptags = bodyContent.find_elements_by_tag_name('p')
        text = " ".join([ptag.text for ptag in ptags])
        fileName = browser.find_element_by_id('firstHeading').text
        browser.close()


    if argType == "-f":
        pdfFile = sys.argv[2]
        fileName, text, pdfFileName = pdfToText(pdfFile)



    text = re.sub("\[A-Za-z0-9]",'', text)
        
    speaker = Sapi()
    speaker.set_rate(4)
    voices = speaker.get_voices()
    speaker.set_voice(voices[1])
    if not os.path.exists(f"audio"):
        os.makedirs(f"audio")
    speaker.create_recording(f"audio\{fileName}.wav", text)
    if argType != "-w":
        os.system(f"rm {fileName}.txt {pdfFileName}")