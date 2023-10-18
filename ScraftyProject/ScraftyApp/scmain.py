import replaydl
import basicreplayr

ReplayDL = replaydl.ReplayDL()
ReplayR = basicreplayr.ReplayR()

threads = [
    #"https://www.smogon.com/forums/threads/pupl-ix-replays-and-usage-stats.3723912/",
    "https://www.smogon.com/forums/threads/adv-pu-tournament-3-swiss-edition-won-by-lily.3711157/",
    "https://www.smogon.com/forums/threads/pupl-ix-replays-and-usage-stats.3723912/",

    "https://www.smogon.com/forums/threads/adv-pu-cup-round-3-replays-mandatory.3717035/",
    "https://www.smogon.com/forums/threads/adv-pu-cup-round-4-replays-mandatory.3717489/",
    "https://www.smogon.com/forums/threads/adv-pu-cup-semifinals-replays-mandatory.3717946/",
    "https://www.smogon.com/forums/threads/adv-pu-cup-finals-won-by-medeia.3718141/",

]
items = [
    "Ancient Power"
    #"Doublade|Shadow Sneak"

]

rformat = [
    "gen3"
]

setReplay = set()


for URL in threads:
    setReplay.union(ReplayDL.getURLFromThread(URL, rformat, "https://replay.pokemonshowdown.com/", setReplay))

output = []
#for link in setReplay:
 #   ReplayR.findAdd(output, link, ReplayDL.getReplay(link),items)

targetsets = [
    {
        "name": "ANY",
        "moves": ["Spider Web","Baton Pass"],
        "item": "ANY"
    },
    {
        "name":"ANY",
        "moves": ["Baton Pass"],
        "item": "Petaya Berry"
    },
    {
        "name":"ANY",
        "moves": ["Baton Pass"],
        "item": "Liechi Berry"
    },
    {
        "name":"ANY",
        "moves": ["Baton Pass"],
        "item": "Salac Berry"
    },
    {
        "name":"ANY",
        "moves": ["Baton Pass"],
        "item": "ANY"
    },
    {
        "name":"Volbeat",
        "moves": ["Baton Pass"],
        "item": "ANY"
    },
    {
        "name":"Mawile",
        "moves": ["Baton Pass, Swords Dance"],
        "item": "ANY"
    },
    {
        "name":"Mawile",
        "moves": ["Baton Pass, Substitute"],
        "item": "ANY"
    },
    {
        "name":"Mawile",
        "moves": ["Baton Pass, Iron Def"],
        "item": "ANY"
    }


]

print(ReplayR.find_add(setReplay,targetsets))



