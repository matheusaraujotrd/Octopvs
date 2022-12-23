import pandas as pd

def write_player_data_to_df(player_data):
    player_df = pd.DataFrame({"Name":player_data[0][0],"Season":player_data[0][1],"Team":player_data[0][2],"Games Played":player_data[0][3],"Goals":player_data[0][4],\
    "Assists":player_data[0][5],"Points":player_data[0][6],"Plus / Minus":player_data[0][7],"Penalty Minutes":player_data[0][8],"Power Play Goals":player_data[0][9],\
    "Power Play Points":player_data[0][10],"Shorthanded Goals":player_data[0][11],"Shorthanded Points":player_data[0][12],"Game Winning Goals":player_data[0][13],\
    "Overtime Goals":player_data[0][14],"Shots":player_data[0][15],"Shooting Percentage":player_data[0][16],"Face-Off Win Percentage":player_data[0][17]})
    return player_df