from gettext import install
import requests
class ReplayDL:

    def getuserinput(self):
        
        kompletinput = input("Vložit URL, každý na novém řádku")
        seznamURL = kompletinput.splitlines
        for i in seznamURL:
            seznamURL[i] = (seznamURL[i]+".log")
        print(seznamURL)
        #todo

    def getThreads(self, URL):
        urlset = set()
        if "/forums/threads/" in URL:
            return urlset.add(URL)
        elif "/forums/forums/" in URL:
            pass

    def getReplay(self, URL):
        editURL = URL+".log"
        replay = requests.get(editURL).content
        return replay

    def getURLFromThread(self, thURL, rformat, contains, urlset):#vezme stránku a vysaje z ní replaye
        request = requests.get(thURL)
        print(thURL)
        page = 1
        while not request.history:
            website = str(request.content)
            index = 0                    
            while index < len(website):
                index = website.find(contains, index)
                if index == -1:
                    break
                a = ""
                index+=len(contains)-1
                rurl = contains
                while a != " " and a != "<" and a !="\"":
                    rurl += a
                    index+=1
                    a = website[index]
                for f in rformat: #kontrolae jestli URL replaye má správný formát
                    if f in rurl:                       
                        urlset.add(rurl)
            if ("page-"+str(page)) in thURL:               
                thURL = thURL.replace("page-"+str(page), "page-"+str(page+1))
            else:
                thURL = thURL+"page-2"
            page += 1
            request = requests.get(thURL)
        return urlset





