import requests
import bs4
import html5lib
import shutil
url= input("enter your url \n")
sonu= requests.get(url)
# print(sonu.text)
filename= "shahid.html"
bs=bs4.BeautifulSoup(sonu.text, 'html.parser')
pretty= bs.prettify()
# print(pretty)
try:
    with open(filename, "w+") as f:
        f.write(pretty)
except Exception as e:
    print(e)
shahid= bs.find_all("img")
no_of_img= len(shahid)
print(no_of_img)   
i=1
for imgtag in shahid:
    print(imgtag)    
    try:
        imglink=imgtag.get("src")
        absolute= url + imglink
        print(absolute)
        sha= imglink[imglink.rindex("."): ]
        if sha.startswith(".png"):
            sha=".png"
        elif sha.startswith(".jpeg"):
            sha=",jpeg"
        elif sha.startswith(".jpg"):
            sha=".jpg"
        elif sha.startswith(".svg"):
            sha=".svg" 
                   
        print(sha)
        filen= str(i)+sha
        res= requests.get (absolute, stream= True)
        with open(filen, "wb") as file:
            shutil.copyfileobj(res.raw, file)
    except Exception as e:
        print(e)
    i=i+1   

