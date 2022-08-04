import requests
from bs4 import BeautifulSoup as bs

a = 0

while True:
    url = "https://www.cmpe.boun.edu.tr/tid/?v={}".format(a)
    req = requests.get(url)
    
    #print(req) #response'da hata var mı diye kontrol eder

    soup = bs(req.content, "html.parser")

    vid_name = soup.find("option", { "value": a })
    
    #print(a) #videonun numarasını yazdırır
    #print(vid_name.text) #videonun adını yazdırır
    
    try:
        with open("{} - {}.mp4".format(a,vid_name.text),"wb") as vid:
            vid_url = "https://www.cmpe.boun.edu.tr/tid/videos/mp4/{}.mp4".format(a)
            req2 = requests.get(vid_url)
            vid.write(req2.content)
    except:
        pass        
        
    a += 1
    if a == 1356:
        break