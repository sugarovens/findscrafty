import replaydl



class ReplayR:
    
    linknumber = 0
    replay = []
    pokelist = []
    linenumber = 0

    def findAdd(self, list, link, replaytext, target):
        print(link)
        nenasel = False
        for t in target:
            x = str(replaytext).find(t)
            if x == -1:
                nenasel = True
        if nenasel == False:        
            list.append(link)
        return list
    
    def find_add(self, linkset, targetsets):
        ReplayDL = replaydl.ReplayDL()
        output=""
        linklists=list(range(len(targetsets)))
        for i in range(0,len(targetsets)):
            linklists[i]=[str(targetsets[i])]

        self.linknumber = 0

        for link in linkset: 
            replaytext = ReplayDL.getReplay(link)#replay download
            print(link+" "+str(self.linknumber))#kontrola
            self.linknumber += 1

            self.read_replay(replaytext)
            tn =0
            for target in targetsets:
                for pokeset in self.pokelist:
                    targetfound = True
                    if target["name"] != "ANY" and not (target["name"] in pokeset["name"]):
                        targetfound = False
                    if target["item"] != "ANY" and not (target["item"] in pokeset["item"]):
                        targetfound = False
                    if target["moves"][0] != "ANY":
                        for move in target["moves"]:
                            if not (move in pokeset["moves"]):
                                targetfound = False
                    if targetfound:
                        linklists[tn].append(link)
                        break
                tn+=1
        for ll in linklists:
            for el in ll:
                output += el
                output += "\n"
            output += "\n______________________________\n"

        return output

    def read_replay(self, replaytext):
        self.replay=replaytext.splitlines()
        i = 0 #oddělání figní na konci řádků + na string + kontrola zorua
        for lines in self.replay:
            self.replay[i] = str(lines).replace("'", "")
            i+=1
        self.linenumber = 0
        self.pokelist = []
        #čtení replaye řádek po řádku
        for line in self.replay:
            l = line.split("|")
            if len(l) > 3 and l[1] == "poke" and (l[3].find("Zorua") != -1 or l[3].find("Zorua-Hisui") != -1 or l[3].find("Zoroark") != -1 or l[3].find("Zoroark-Hisui") != -1):
                return []
            try:
                self.event_switch(line, l) #identifikuje akci a volá odpovídající funkci
            except Exception:
                print(f"{self.linenumber} {l}")
                raise Exception
            self.linenumber+=1
        #for pk in self.Field.pokelist: #kontrola... pak smazat
           # print(pk.name+"  "+pk.nickname+"  "+str(pk.switchPOC)+" "+str(pk.attackPOC))
        
    def event_switch(self, line, l):
        if "|switch|" in line or "|drag|" in line:
            self.switch(l)
        elif "|move|" in line:
            self.move(l)
        elif "[from] item: " in line:
            self.from_item(l)
        elif "|enditem|" in line:
            self.end_item(l)


    def switch(self, l):
        #zápis nových poké do seznamu
        pokevseznamu = False
        for pokeset in self.pokelist:
            if pokeset["nickname"] == l[2]:
                pokevseznamu= True
                break
        if not pokevseznamu:
            pokeset = {
                "name": l[3],
                "nickname": l[2],
                "moves": set(),
                "item": "unknown"
            }
            self.pokelist.append(pokeset)

    def move(self, l):
        #zápis útoku do setu
        for pokeset in self.pokelist:
            if pokeset["nickname"] == l[2]:
                pokeset["moves"].add(l[3])
                break

    def from_item(self, l):
        item = "unknown"
        for t in l:
            if "[from] item: " in t:
                item = t.replace("[from] item: ", "")
                break
        for pokeset in self.pokelist:
            if pokeset["nickname"] == l[2]:
                pokeset["item"] = item
                break

    def end_item(self, l):
        for pokeset in self.pokelist:
            if pokeset["nickname"] == l[2]:
                pokeset["item"] = l[3]
                break