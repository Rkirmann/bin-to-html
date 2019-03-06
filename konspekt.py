from bs4 import BeautifulSoup

with open("kysimused.bin", "rb") as f:
    contents = f.read()
    
soup = BeautifulSoup(contents, 'html.parser')
a = '0'
b = '0'
hulk = set()
sorditud = []
sonastik = {}
newfile = open('konspekt.html', 'wb+')

for tag in soup.find_all(["div", "span", "id", "p"]):
    if "id" in tag.attrs:
        del tag.attrs["id"]
    if tag.get('class') == ['qtext']:
        if tag not in hulk:
            newfile.write(str(tag).encode('UTF-8'))
            newfile.write(str(b).encode('UTF-8'))
            hulk.add(tag)
            tyhik = 0
            for i in tag.text:
                if str(i) in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','Š','Z','Ž','T','U','V','Õ','Ä','Ö','Ü','Q','X','Y','W']:
                    sonastik[tag.text[tyhik:]] = (tag, b)
                    break
                else:
                    tyhik += 1         
    if tag.get('class') == ['rightanswer']:
        b = tag

with open('sorditud2.html', 'wb+') as f:
    for key, item in sorted(sonastik.items()):
        for i in item:
            f.write(str(i).encode('UTF-8'))
           
newfile.close()