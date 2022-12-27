import pandas as pd
import os

def write_player_data_to_df(player_data):
    if player_data[0][1] != "G":
        player_df = pd.DataFrame({"Name":player_data[0][0],"Position":player_data[0][1],"Season":player_data[0][2],"Team":player_data[0][3],"Games Played":player_data[0][4],"Goals":player_data[0][5],\
        "Assists":player_data[0][6],"Points":player_data[0][7],"Plus / Minus":player_data[0][8],"Penalty Minutes":player_data[0][9],"Power Play Goals":player_data[0][10],\
        "Power Play Points":player_data[0][11],"Shorthanded Goals":player_data[0][12],"Shorthanded Points":player_data[0][13],"Game Winning Goals":player_data[0][14],\
        "Overtime Goals":player_data[0][15],"Shots":player_data[0][16],"Shooting Percentage":player_data[0][17],"Face-Off Win Percentage":player_data[0][18]})
    else:
        player_df = pd.DataFrame({"Name":player_data[0][0],"Position":player_data[0][1],"Season":player_data[0][2],"Team":player_data[0][3],"Games Played":player_data[0][4],"Games Started":player_data[0][5],\
        "Wins":player_data[0][6],"Losses":player_data[0][7],"Ties":player_data[0][8],"Overtime Losses":player_data[0][9],"Shots Against":player_data[0][10],\
        "Goals Against":player_data[0][11],"Goals Against Average":player_data[0][12],"Saves":player_data[0][13],"Save Percentage":player_data[0][14],\
        "Shutouts":player_data[0][15],"Minutes":player_data[0][16]})
    return player_df

def export_data_to_csv(player_data):
    root = "data"
    path = root + "/" + str(player_data.iloc[-1][3])
    filename = str(player_data.iloc[0][0]) + ".csv"
    for (roots, dirs, files) in os.walk(root):
        for names in files:
            if filename in names:
                update_file(player_data, path, filename, root, roots)
    else:
        check_directory(path)
        player_data.to_csv(f"{path}" + "/" + f"{filename}", encoding="utf-8")

def update_file(player_data, path, filename, root, roots):
    os.remove(roots + "/" + filename)
    actual_dir = str(player_data.iloc[-1][3])
    path = root + "/" + actual_dir
    check_directory(path)
    player_data.to_csv(f"{path}" + "/" + f"{filename}", encoding="utf-8")

def check_directory(path):
    if os.path.exists(path):
        pass
    else:
        os.makedirs(path)
        


    
        
