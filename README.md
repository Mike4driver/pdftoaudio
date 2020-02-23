# pdftoaudio
similar to my other webscraping projects however this one scrapes pdfs and wikipedia

If you wish to use the wikipedia functionality you will also need to have a Driver folder with a chromedriver.exe inside,
Because I could not find a good pdf parser for python at the time of writing this script (a few years ago) this also utilizes node 
so you will want to use run "npm i" before using

USAGE:

To Download pdf form url and change to audio

python main.py -u http://yoururl.pdf

To Convert local pdf file in root directory to audio

python main.py -f yourfile.pdf

To Grab wikipedia page

python main.py -w http://yoururl.com

To Grab random wikipedia page

python main.py -w -r
