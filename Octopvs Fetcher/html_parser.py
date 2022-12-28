from bs4 import BeautifulSoup
from bs4 import SoupStrainer

def player_parser(content):
    # Hockey stats, no need to understand those.
    name=[]
    position=[]
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

    # For goalies only:
    gs=[]
    w=[]
    l=[]
    t=[]
    ot=[]
    sa=[]
    ga=[]
    gaa=[]
    s=[]
    svp=[]
    so=[]
    _min=[]

    # Hockey stats, no need to understand those.
    soup = BeautifulSoup(content, "lxml")
    player_bio_label = soup.find("span", attrs={"class":"player-bio__label"})
    name=player_bio_label.get_text(strip=True)
    position=soup.find("span", attrs={"class":"player-jumbotron-vitals--attr"})
    position=position.get_text(strip=True)
    data_table = soup.find("div", attrs={"id":"careerTable"})
    tbody = data_table.div.div.div.div.table.tbody
    seasons = [
        item.get_text(strip=False).split() for item in tbody.find_all("tr")
            ]
    seasons_stripped = [x for x in seasons if x]
    if position != "G":
        for season in range(len(seasons_stripped)):
            current_season = seasons_stripped[season]
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
        player_data = (name, position, played_season, team, gp, g, a, p, pm, pim, ppg, ppp, shg, shp, gwg, otg, s, sp, fop)
    else:
        for season in range(len(seasons_stripped)):
            current_season = seasons_stripped[season]
            played_season.append(current_season[0])
            team.append(current_season[1])
            gp.append(current_season[2])
            gs.append(current_season[3])
            w.append(current_season[4])
            l.append(current_season[5])
            t.append(current_season[6])
            ot.append(current_season[7])
            sa.append(current_season[8])
            ga.append(current_season[9])
            gaa.append(current_season[10])
            s.append(current_season[11])
            svp.append(current_season[12])
            so.append(current_season[13])
            _min.append(current_season[14])
        player_data = (name, position, played_season, team, gp, gs, w, l, t, ot, sa, ga, gaa, s, svp, so, _min)

    return player_data