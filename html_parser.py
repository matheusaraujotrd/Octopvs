from bs4 import BeautifulSoup
from bs4 import SoupStrainer

def parser(content):

    # Hockey stats, no need to understand those.
    name=[]
    played_season=[]
    team=[]
    gp=[]
    g=[]
    a=[]
    p=[]
    pm=[]
    pim=[]
    ppg=[]
    ppp=[]
    shg=[]
    shp=[]
    gwg=[]
    otg=[]
    s=[]
    sp=[]
    fop=[]
    # Hockey stats, no need to understand those.
    data_table = SoupStrainer("div", attrs={"id":"careerTable"})
    player_bio_label = SoupStrainer("span", attrs={"class":"player-bio__label"})
    soup = BeautifulSoup(content, "lxml", parse_only=player_bio_label)
    name=soup.find("span", attrs={"class":"player-bio__label"})
    name=name.get_text(strip=True)
    soup = BeautifulSoup(content, "lxml", parse_only=data_table)
    seasons = [
        item.get_text(strip=False).split() for item in soup.div.div.div.div.table.tbody.contents
            ]
    seasons_cleaned = [x for x in seasons if x]
    for season in range(len(seasons_cleaned)):
        current_season = seasons_cleaned[season]
        played_season.append(current_season[0])
        team.append(current_season[1])
        gp.append(current_season[2])
        g.append(current_season[3])
        a.append(current_season[4])
        p.append(current_season[5])
        pm.append(current_season[6])
        pim.append(current_season[7])
        ppg.append(current_season[8])
        ppp.append(current_season[9])
        shg.append(current_season[10])
        shp.append(current_season[11])
        gwg.append(current_season[12])
        otg.append(current_season[13])
        s.append(current_season[14])
        sp.append(current_season[15])
        fop.append(current_season[16])
    player_data = (name, played_season, team, gp, g, a, p, pim, pm, ppg, ppp, shg, shp, gwg, otg, s, sp, fop)

    return player_data