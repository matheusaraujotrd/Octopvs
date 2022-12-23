from bs4 import BeautifulSoup

def parser(content):
    soup = BeautifulSoup(content, "lxml")
    
    # Hockey stats, no need to understand those.
    name=[]
    player_seasons=[]
    seasons=[]
    team=[]
    gp=[]
    g=[]
    a=[]
    p=[]
    pm=[]
    ppg=[]
    ppp=[]
    shg=[]
    shp=[]
    gwg=[]
    otg=[]
    s=[]
    sp=[]
    # Hockey stats, no need to understand those.

    name=soup.find("span", attrs={"class":"player-bio__label"})
    seasons=[]
    for x in range(6):
        season = [
            item.get_text(strip=True).split() for item in soup.select(selector)
        seasons.append(season)
    for y in range(6):
        player_seasons.append(seasons[0])
        team.append(seasons[1])
        gp.append(seasons[2])
        g.append(seasons[3])
        a.append(seasons[4])
        p.append(seasons[5])
        pm.append(seasons[6])
        ppg.append(seasons[7])
        ppp.append(seasons[8])
        shg.append(seasons[9])
        shp.append(seasons[10])
        gwg.append(seasons[11])
        otg.append(seasons[12])
        s.append(seasons[13])
        sp.append(seasons[14])
    player_data = (name, seasons, team, gp, g, a, p, pm, ppg, ppp, shg, shp, gwg, otg, s, sp)

    return player_data