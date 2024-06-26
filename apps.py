''' This is a Pythorn + SQL code that can sort and check all the datas in the games.db database
Made by Wilson Tong on the 22/05/24'''

# Gains acess to Sql codes and data
import sqlite3



# Variable Declarations:
DATABASE="Game_Database.db"

#Functions To Look At All The Games
def Print_All_Games():
    db=sqlite3.connect(DATABASE)
    cursor=db.cursor()
    sql="SELECT Games.id,Games.game_name FROM Games;"
    cursor.execute(sql)
    results=cursor.fetchall()
    print("          Game_Name\n")
    for final in results:
        print(f"{final[0]:<10}{final[1]}")
    db.close

#Functions To Order The Data
def Print_All_Data_Sorted_by_Game_Name():
    db=sqlite3.connect(DATABASE)
    cursor=db.cursor()
    sql="SELECT Games.game_name, Genres.genre_name, Makers.maker_name, Games.IGN_rating, Games.release_year FROM Games JOIN Genres ON Genres.genre_id = Games.genre_id JOIN Makers ON Makers.maker_id=Games.maker_id ORDER BY Games.game_name ASC;"
    cursor.execute(sql)
    results=cursor.fetchall()
    print("Game_Name                                         Genre                                   Maker                    IGN_Rating           Year_Released\n")
    for final in results:
        print(f"{final[0]:<50}{final[1]:<40}{final[2]:<30}{final[3]:<20}{final[4]}")
    db.close

def Print_All_Data_Sorted_by_Maker_Name():
    db=sqlite3.connect(DATABASE)
    cursor=db.cursor()
    sql="SELECT Games.game_name, Genres.genre_name, Makers.maker_name, Games.IGN_rating, Games.release_year FROM Games JOIN Genres ON Genres.genre_id = Games.genre_id JOIN Makers ON Makers.maker_id=Games.maker_id ORDER BY Makers.maker_name asc;"
    cursor.execute(sql)
    print("Game_Name                                         Genre                                   Maker                    IGN_Rating           Year_Released\n")
    results=cursor.fetchall()
    for final in results:
        print(f"{final[0]:<50}{final[1]:<40}{final[2]:<30}{final[3]:<20}{final[4]}")
    db.close

def Print_All_Data_Sorted_by_Release_year():
    db=sqlite3.connect(DATABASE)
    cursor=db.cursor()
    sql="SELECT Games.game_name, Genres.genre_name, Makers.maker_name, Games.IGN_rating, Games.release_year FROM Games JOIN Genres ON Genres.genre_id = Games.genre_id JOIN Makers ON Makers.maker_id=Games.maker_id ORDER BY Games.release_year asc;"
    cursor.execute(sql)
    print("Game_Name                                         Genre                                   Maker                    IGN_Rating           Year_Released\n")
    results=cursor.fetchall()
    for final in results:
        print(f"{final[0]:<50}{final[1]:<40}{final[2]:<30}{final[3]:<20}{final[4]}")
    db.close

def Print_All_Data_Sorted_by_IGN_Rating():
    db=sqlite3.connect(DATABASE)
    cursor=db.cursor()
    sql="SELECT Games.game_name, Genres.genre_name, Makers.maker_name, Games.IGN_rating, Games.release_year FROM Games JOIN Genres ON Genres.genre_id = Games.genre_id JOIN Makers ON Makers.maker_id=Games.maker_id ORDER BY Games.IGN_rating DESC;"
    cursor.execute(sql)
    print("Game_Name                                         Genre                                   Maker                    IGN_Rating           Year_Released\n")
    results=cursor.fetchall()
    for final in results:
        print(f"{final[0]:<50}{final[1]:<40}{final[2]:<30}{final[3]:<20}{final[4]}")
    db.close

def Print_All_Data_Sorted_by_Genre_Name():
    db=sqlite3.connect(DATABASE)
    cursor=db.cursor()
    sql="SELECT Games.game_name, Genres.genre_name, Makers.maker_name, Games.IGN_rating, Games.release_year FROM Games JOIN Genres ON Genres.genre_id = Games.genre_id JOIN Makers ON Makers.maker_id=Games.maker_id ORDER BY Genres.genre_name ASC;"
    cursor.execute(sql)
    print("Game_Name                                         Genre                                   Maker                    IGN_Rating           Year_Released\n")
    results=cursor.fetchall()
    for final in results:
        print(f"{final[0]:<50}{final[1]:<40}{final[2]:<30}{final[3]:<20}{final[4]}")
    db.close

#Functions To See The Different Tables
def Print_All_Data():
    db=sqlite3.connect(DATABASE)
    cursor=db.cursor()
    sql="SELECT Games.game_name, Genres.genre_name, Makers.maker_name, Games.IGN_rating, Games.release_year FROM Games JOIN Genres ON Genres.genre_id = Games.genre_id JOIN Makers ON Makers.maker_id=Games.maker_id;"
    cursor.execute(sql)
    results=cursor.fetchall()
    print("Game_Name                                         Genre                                   Maker                    IGN_Rating           Year_Released\n")
    for final in results:
        print(f"{final[0]:<50}{final[1]:<40}{final[2]:<30}{final[3]:<20}{final[4]}")
    db.close

def Print_All_Genres():
    db=sqlite3.connect(DATABASE)
    cursor=db.cursor()
    sql="SELECT * FROM Genres;"
    cursor.execute(sql)
    results=cursor.fetchall()
    print("          Genre_Name\n")
    for final in results:
        print(f"{final[0]:<10}{final[1]}")
    db.close

def Print_All_Makers():
    db=sqlite3.connect(DATABASE)
    cursor=db.cursor()
    sql="SELECT * FROM Makers;"
    cursor.execute(sql)
    results=cursor.fetchall()
    print("          Maker_Name\n")
    for final in results:
        print(f"{final[0]:<10}{final[1]}")
    db.close

#Functions To Pick The Different Genres
def Print_All_Data_Only_Genre_Sandbox():
    db=sqlite3.connect(DATABASE)
    cursor=db.cursor()
    sql="SELECT Games.game_name, Genres.genre_name, Makers.maker_name, Games.IGN_rating, Games.release_year FROM Games JOIN Genres ON Genres.genre_id = Games.genre_id JOIN Makers ON Makers.maker_id=Games.maker_id WHERE Genres.genre_name='Sandbox';"
    cursor.execute(sql)
    results=cursor.fetchall()
    print("Game_Name                                         Genre                                   Maker                    IGN_Rating           Year_Released\n")
    for final in results:
        print(f"{final[0]:<50}{final[1]:<40}{final[2]:<30}{final[3]:<20}{final[4]}")
    db.close

def Print_All_Data_Only_Genre_Battle_Royale():
    db=sqlite3.connect(DATABASE)
    cursor=db.cursor()
    sql="SELECT Games.game_name, Genres.genre_name, Makers.maker_name, Games.IGN_rating, Games.release_year FROM Games JOIN Genres ON Genres.genre_id = Games.genre_id JOIN Makers ON Makers.maker_id=Games.maker_id WHERE Genres.genre_name='Battle royale';"
    cursor.execute(sql)
    results=cursor.fetchall()
    print("Game_Name                                         Genre                                   Maker                    IGN_Rating           Year_Released\n")
    for final in results:
        print(f"{final[0]:<50}{final[1]:<40}{final[2]:<30}{final[3]:<20}{final[4]}")
    db.close

def Print_All_Data_Only_Genre_MOBA():
    db=sqlite3.connect(DATABASE)
    cursor=db.cursor()
    sql="SELECT Games.game_name, Genres.genre_name, Makers.maker_name, Games.IGN_rating, Games.release_year FROM Games JOIN Genres ON Genres.genre_id = Games.genre_id JOIN Makers ON Makers.maker_id=Games.maker_id WHERE Genres.genre_name='MOBA';"
    cursor.execute(sql)
    results=cursor.fetchall()
    print("Game_Name                                         Genre                                   Maker                    IGN_Rating           Year_Released\n")
    for final in results:
        print(f"{final[0]:<50}{final[1]:<40}{final[2]:<30}{final[3]:<20}{final[4]}")
    db.close

def Print_All_Data_Only_Genre_FPS():
    db=sqlite3.connect(DATABASE)
    cursor=db.cursor()
    sql="SELECT Games.game_name, Genres.genre_name, Makers.maker_name, Games.IGN_rating, Games.release_year FROM Games JOIN Genres ON Genres.genre_id = Games.genre_id JOIN Makers ON Makers.maker_id=Games.maker_id WHERE Genres.genre_name='FPS';"
    cursor.execute(sql)
    results=cursor.fetchall()
    print("Game_Name                                         Genre                                   Maker                    IGN_Rating           Year_Released\n")
    for final in results:
        print(f"{final[0]:<50}{final[1]:<40}{final[2]:<30}{final[3]:<20}{final[4]}")
    db.close

def Print_All_Data_Only_Genre_Sports():
    db=sqlite3.connect(DATABASE)
    cursor=db.cursor()
    sql="SELECT Games.game_name, Genres.genre_name, Makers.maker_name, Games.IGN_rating, Games.release_year FROM Games JOIN Genres ON Genres.genre_id = Games.genre_id JOIN Makers ON Makers.maker_id=Games.maker_id WHERE Genres.genre_name='Sports';"
    cursor.execute(sql)
    results=cursor.fetchall()
    print("Game_Name                                         Genre                                   Maker                    IGN_Rating           Year_Released\n")
    for final in results:
        print(f"{final[0]:<50}{final[1]:<40}{final[2]:<30}{final[3]:<20}{final[4]}")
    db.close

def Print_All_Data_Only_Genre_Fighting():
    db=sqlite3.connect(DATABASE)
    cursor=db.cursor()
    sql="SELECT Games.game_name, Genres.genre_name, Makers.maker_name, Games.IGN_rating, Games.release_year FROM Games JOIN Genres ON Genres.genre_id = Games.genre_id JOIN Makers ON Makers.maker_id=Games.maker_id WHERE Genres.genre_name='Fighting';"
    cursor.execute(sql)
    results=cursor.fetchall()
    print("Game_Name                                         Genre                                   Maker                    IGN_Rating           Year_Released\n")
    for final in results:
        print(f"{final[0]:<50}{final[1]:<40}{final[2]:<30}{final[3]:<20}{final[4]}")
    db.close

def Print_All_Data_Only_Genre_RPG():
    db=sqlite3.connect(DATABASE)
    cursor=db.cursor()
    sql="SELECT Games.game_name, Genres.genre_name, Makers.maker_name, Games.IGN_rating, Games.release_year FROM Games JOIN Genres ON Genres.genre_id = Games.genre_id JOIN Makers ON Makers.maker_id=Games.maker_id WHERE Genres.genre_name='RPG';"
    cursor.execute(sql)
    results=cursor.fetchall()
    print("Game_Name                                         Genre                                   Maker                    IGN_Rating           Year_Released\n")
    for final in results:
        print(f"{final[0]:<50}{final[1]:<40}{final[2]:<30}{final[3]:<20}{final[4]}")
    db.close

def Print_All_Data_Only_Genre_Social_Simulation():
    db=sqlite3.connect(DATABASE)
    cursor=db.cursor()
    sql="SELECT Games.game_name, Genres.genre_name, Makers.maker_name, Games.IGN_rating, Games.release_year FROM Games JOIN Genres ON Genres.genre_id = Games.genre_id JOIN Makers ON Makers.maker_id=Games.maker_id WHERE Genres.genre_name='Social Simulation';"
    cursor.execute(sql)
    results=cursor.fetchall()
    print("Game_Name                                         Genre                                   Maker                    IGN_Rating           Year_Released\n")
    for final in results:
        print(f"{final[0]:<50}{final[1]:<40}{final[2]:<30}{final[3]:<20}{final[4]}")
    db.close

def Print_All_Data_Only_Genre_Action_Adventure():
    db=sqlite3.connect(DATABASE)
    cursor=db.cursor()
    sql="SELECT Games.game_name, Genres.genre_name, Makers.maker_name, Games.IGN_rating, Games.release_year FROM Games JOIN Genres ON Genres.genre_id = Games.genre_id JOIN Makers ON Makers.maker_id=Games.maker_id WHERE Genres.genre_name='Action-Adventure';"
    cursor.execute(sql)
    results=cursor.fetchall()
    print("Game_Name                                         Genre                                   Maker                    IGN_Rating           Year_Released\n")
    for final in results:
        print(f"{final[0]:<50}{final[1]:<40}{final[2]:<30}{final[3]:<20}{final[4]}")
    db.close

def Print_All_Data_Only_Genre_Party_game():
    db=sqlite3.connect(DATABASE)
    cursor=db.cursor()
    sql="SELECT Games.game_name, Genres.genre_name, Makers.maker_name, Games.IGN_rating, Games.release_year FROM Games JOIN Genres ON Genres.genre_id = Games.genre_id JOIN Makers ON Makers.maker_id=Games.maker_id WHERE Genres.genre_name='Party Game';"
    cursor.execute(sql)
    results=cursor.fetchall()
    print("Game_Name                                         Genre                                   Maker                    IGN_Rating           Year_Released\n")
    for final in results:
        print(f"{final[0]:<50}{final[1]:<40}{final[2]:<30}{final[3]:<20}{final[4]}")
    db.close

#Function To Pick The Different Maker
def Print_All_Data_Only_Maker_Mojang_Studios():
    db=sqlite3.connect(DATABASE)
    cursor=db.cursor()
    sql="SELECT Games.game_name, Genres.genre_name, Makers.maker_name, Games.IGN_rating, Games.release_year FROM Games JOIN Genres ON Genres.genre_id = Games.genre_id JOIN Makers ON Makers.maker_id=Games.maker_id WHERE Makers.maker_name='Mojang Studios';"
    cursor.execute(sql)
    results=cursor.fetchall()
    print("Game_Name                                         Genre                                   Maker                    IGN_Rating           Year_Released\n")
    for final in results:
        print(f"{final[0]:<50}{final[1]:<40}{final[2]:<30}{final[3]:<20}{final[4]}")
    db.close

def Print_All_Data_Only_Maker_Riot_Games():
    db=sqlite3.connect(DATABASE)
    cursor=db.cursor()
    sql="SELECT Games.game_name, Genres.genre_name, Makers.maker_name, Games.IGN_rating, Games.release_year FROM Games JOIN Genres ON Genres.genre_id = Games.genre_id JOIN Makers ON Makers.maker_id=Games.maker_id WHERE Makers.maker_name='Riot Games';"
    cursor.execute(sql)
    results=cursor.fetchall()
    print("Game_Name                                         Genre                                   Maker                    IGN_Rating           Year_Released\n")
    for final in results:
        print(f"{final[0]:<50}{final[1]:<40}{final[2]:<30}{final[3]:<20}{final[4]}")
    db.close

def Print_All_Data_Only_Maker_Supercell():
    db=sqlite3.connect(DATABASE)
    cursor=db.cursor()
    sql="SELECT Games.game_name, Genres.genre_name, Makers.maker_name, Games.IGN_rating, Games.release_year FROM Games JOIN Genres ON Genres.genre_id = Games.genre_id JOIN Makers ON Makers.maker_id=Games.maker_id WHERE Makers.maker_name='Supercell';"
    cursor.execute(sql)
    results=cursor.fetchall()
    print("Game_Name                                         Genre                                   Maker                    IGN_Rating           Year_Released\n")
    for final in results:
        print(f"{final[0]:<50}{final[1]:<40}{final[2]:<30}{final[3]:<20}{final[4]}")
    db.close

def Print_All_Data_Only_Maker_Psyonix():
    db=sqlite3.connect(DATABASE)
    cursor=db.cursor()
    sql="SELECT Games.game_name, Genres.genre_name, Makers.maker_name, Games.IGN_rating, Games.release_year FROM Games JOIN Genres ON Genres.genre_id = Games.genre_id JOIN Makers ON Makers.maker_id=Games.maker_id WHERE Makers.maker_name='Psyonix';"
    cursor.execute(sql)
    results=cursor.fetchall()
    print("Game_Name                                         Genre                                   Maker                    IGN_Rating           Year_Released\n")
    for final in results:
        print(f"{final[0]:<50}{final[1]:<40}{final[2]:<30}{final[3]:<20}{final[4]}")
    db.close

def Print_All_Data_Only_Maker_Bandai_Namco_Studios():
    db=sqlite3.connect(DATABASE)
    cursor=db.cursor()
    sql="SELECT Games.game_name, Genres.genre_name, Makers.maker_name, Games.IGN_rating, Games.release_year FROM Games JOIN Genres ON Genres.genre_id = Games.genre_id JOIN Makers ON Makers.maker_id=Games.maker_id WHERE Makers.maker_name='Bandai Namco Studios';"
    cursor.execute(sql)
    results=cursor.fetchall()
    print("Game_Name                                         Genre                                   Maker                    IGN_Rating           Year_Released\n")
    for final in results:
        print(f"{final[0]:<50}{final[1]:<40}{final[2]:<30}{final[3]:<20}{final[4]}")
    db.close

def Print_All_Data_Only_Maker_Valve_Corporation():
    db=sqlite3.connect(DATABASE)
    cursor=db.cursor()
    sql="SELECT Games.game_name, Genres.genre_name, Makers.maker_name, Games.IGN_rating, Games.release_year FROM Games JOIN Genres ON Genres.genre_id = Games.genre_id JOIN Makers ON Makers.maker_id=Games.maker_id WHERE Makers.maker_name='Valve Corporation';"
    cursor.execute(sql)
    results=cursor.fetchall()
    print("Game_Name                                         Genre                                   Maker                    IGN_Rating           Year_Released\n")
    for final in results:
        print(f"{final[0]:<50}{final[1]:<40}{final[2]:<30}{final[3]:<20}{final[4]}")
    db.close

def Print_All_Data_Only_Maker_Nintendo_EPD():
    db=sqlite3.connect(DATABASE)
    cursor=db.cursor()
    sql="SELECT Games.game_name, Genres.genre_name, Makers.maker_name, Games.IGN_rating, Games.release_year FROM Games JOIN Genres ON Genres.genre_id = Games.genre_id JOIN Makers ON Makers.maker_id=Games.maker_id WHERE Makers.maker_name='Nintendo EPD';"
    cursor.execute(sql)
    results=cursor.fetchall()
    print("Game_Name                                         Genre                                   Maker                    IGN_Rating           Year_Released\n")
    for final in results:
        print(f"{final[0]:<50}{final[1]:<40}{final[2]:<30}{final[3]:<20}{final[4]}")
    db.close

def Print_All_Data_Only_Maker_miHoYo():
    db=sqlite3.connect(DATABASE)
    cursor=db.cursor()
    sql="SELECT Games.game_name, Genres.genre_name, Makers.maker_name, Games.IGN_rating, Games.release_year FROM Games JOIN Genres ON Genres.genre_id = Games.genre_id JOIN Makers ON Makers.maker_id=Games.maker_id WHERE Makers.maker_name='miHoYo';"
    cursor.execute(sql)
    results=cursor.fetchall()
    print("Game_Name                                         Genre                                   Maker                    IGN_Rating           Year_Released\n")
    for final in results:
        print(f"{final[0]:<50}{final[1]:<40}{final[2]:<30}{final[3]:<20}{final[4]}")
    db.close

def Print_All_Data_Only_FromSoftware():
    db=sqlite3.connect(DATABASE)
    cursor=db.cursor()
    sql="SELECT Games.game_name, Genres.genre_name, Makers.maker_name, Games.IGN_rating, Games.release_year FROM Games JOIN Genres ON Genres.genre_id = Games.genre_id JOIN Makers ON Makers.maker_id=Games.maker_id WHERE Makers.maker_name='FromSoftware';"
    cursor.execute(sql)
    results=cursor.fetchall()
    print("Game_Name                                         Genre                                   Maker                    IGN_Rating           Year_Released\n")
    for final in results:
        print(f"{final[0]:<50}{final[1]:<40}{final[2]:<30}{final[3]:<20}{final[4]}")
    db.close

def Print_All_Data_Only_Maker_The_Sims_Studio():
    db=sqlite3.connect(DATABASE)
    cursor=db.cursor()
    sql="SELECT Games.game_name, Genres.genre_name, Makers.maker_name, Games.IGN_rating, Games.release_year FROM Games JOIN Genres ON Genres.genre_id = Games.genre_id JOIN Makers ON Makers.maker_id=Games.maker_id WHERE Makers.maker_name='FromSoftware';"
    cursor.execute(sql)
    results=cursor.fetchall()
    print("Game_Name                                         Genre                                   Maker                    IGN_Rating           Year_Released\n")
    for final in results:
        print(f"{final[0]:<50}{final[1]:<40}{final[2]:<30}{final[3]:<20}{final[4]}")
    db.close

def Print_All_Data_Only_Maker_Rockstar_Games():
    db=sqlite3.connect(DATABASE)
    cursor=db.cursor()
    sql="SELECT Games.game_name, Genres.genre_name, Makers.maker_name, Games.IGN_rating, Games.release_year FROM Games JOIN Genres ON Genres.genre_id = Games.genre_id JOIN Makers ON Makers.maker_id=Games.maker_id WHERE Makers.maker_name='Rockstar Games';"
    cursor.execute(sql)
    results=cursor.fetchall()
    print("Game_Name                                         Genre                                   Maker                    IGN_Rating           Year_Released\n")
    for final in results:
        print(f"{final[0]:<50}{final[1]:<40}{final[2]:<30}{final[3]:<20}{final[4]}")
    db.close

def Print_All_Data_Only_Maker_Blizzard_Entertainment():
    db=sqlite3.connect(DATABASE)
    cursor=db.cursor()
    sql="SELECT Games.game_name, Genres.genre_name, Makers.maker_name, Games.IGN_rating, Games.release_year FROM Games JOIN Genres ON Genres.genre_id = Games.genre_id JOIN Makers ON Makers.maker_id=Games.maker_id WHERE Makers.maker_name='Blizzard Entertainment';"
    cursor.execute(sql)
    results=cursor.fetchall()
    print("Game_Name                                         Genre                                   Maker                    IGN_Rating           Year_Released\n")
    for final in results:
        print(f"{final[0]:<50}{final[1]:<40}{final[2]:<30}{final[3]:<20}{final[4]}")
    db.close

def Print_All_Data_Only_Maker_Respawn_Entertainment():
    db=sqlite3.connect(DATABASE)
    cursor=db.cursor()
    sql="SELECT Games.game_name, Genres.genre_name, Makers.maker_name, Games.IGN_rating, Games.release_year FROM Games JOIN Genres ON Genres.genre_id = Games.genre_id JOIN Makers ON Makers.maker_id=Games.maker_id WHERE Makers.maker_name='Respawn Entertainment';"
    cursor.execute(sql)
    results=cursor.fetchall()
    print("Game_Name                                         Genre                                   Maker                    IGN_Rating           Year_Released\n")
    for final in results:
        print(f"{final[0]:<50}{final[1]:<40}{final[2]:<30}{final[3]:<20}{final[4]}")
    db.close

def Print_All_Data_Only_Maker_CD_PROJEKT_RED():
    db=sqlite3.connect(DATABASE)
    cursor=db.cursor()
    sql="SELECT Games.game_name, Genres.genre_name, Makers.maker_name, Games.IGN_rating, Games.release_year FROM Games JOIN Genres ON Genres.genre_id = Games.genre_id JOIN Makers ON Makers.maker_id=Games.maker_id WHERE Makers.maker_name='CD PROJEKT RED';"
    cursor.execute(sql)
    results=cursor.fetchall()
    print("Game_Name                                         Genre                                   Maker                    IGN_Rating           Year_Released\n")
    for final in results:
        print(f"{final[0]:<50}{final[1]:<40}{final[2]:<30}{final[3]:<20}{final[4]}")
    db.close

def Print_All_Data_Only_Maker_InnerSlothLLC():
    db=sqlite3.connect(DATABASE)
    cursor=db.cursor()
    sql="SELECT Games.game_name, Genres.genre_name, Makers.maker_name, Games.IGN_rating, Games.release_year FROM Games JOIN Genres ON Genres.genre_id = Games.genre_id JOIN Makers ON Makers.maker_id=Games.maker_id WHERE Makers.maker_name='InnerSlothLLC';"
    cursor.execute(sql)
    results=cursor.fetchall()
    print("Game_Name                                         Genre                                   Maker                    IGN_Rating           Year_Released\n")
    for final in results:
        print(f"{final[0]:<50}{final[1]:<40}{final[2]:<30}{final[3]:<20}{final[4]}")
    db.close

def Print_All_Data_Only_Maker_Epic_Games():
    db=sqlite3.connect(DATABASE)
    cursor=db.cursor()
    sql="SELECT Games.game_name, Genres.genre_name, Makers.maker_name, Games.IGN_rating, Games.release_year FROM Games JOIN Genres ON Genres.genre_id = Games.genre_id JOIN Makers ON Makers.maker_id=Games.maker_id WHERE Makers.maker_name='Epic Games';"
    cursor.execute(sql)
    results=cursor.fetchall()
    print("Game_Name                                         Genre                                   Maker                    IGN_Rating           Year_Released\n")
    for final in results:
        print(f"{final[0]:<50}{final[1]:<40}{final[2]:<30}{final[3]:<20}{final[4]}")
    db.close

#Function to pick the specific year
def Print_All_Data_Only_Year_From_Input(name):
    db=sqlite3.connect(DATABASE)
    cursor=db.cursor()
    sql="SELECT Games.game_name, Genres.genre_name, Makers.maker_name, Games.IGN_rating, Games.release_year FROM Games JOIN Genres ON Genres.genre_id = Games.genre_id JOIN Makers ON Makers.maker_id=Games.maker_id WHERE Games.release_year="+name+";"
    cursor.execute(sql)
    results=cursor.fetchall()
    print("Game_Name                                         Genre                                   Maker                    IGN_Rating           Year_Released\n")
    for final in results:
        print(f"{final[0]:<50}{final[1]:<40}{final[2]:<30}{final[3]:<20}{final[4]}")
    db.close


#Functions to pick the specific IGN rating
def Print_All_Data_Only_IGN_Rating_From_Input( name ):
    db=sqlite3.connect(DATABASE)
    cursor=db.cursor()
    sql="SELECT Games.game_name, Genres.genre_name, Makers.maker_name, Games.IGN_rating, Games.release_year FROM Games JOIN Genres ON Genres.genre_id = Games.genre_id JOIN Makers ON Makers.maker_id=Games.maker_id WHERE Games.IGN_rating="+name+";"
    cursor.execute(sql)
    results=cursor.fetchall()
    print("Game_Name                                         Genre                                   Maker                    IGN_Rating           Year_Released\n")
    for final in results:
        print(f"{final[0]:<50}{final[1]:<40}{final[2]:<30}{final[3]:<20}{final[4]}")
    db.close

#Main code

while True:
    #Asks what the user wants to do
    user_input=input(
"""

Hello User, What Would You Like To Do Today In This Game Database?
Please Enter A Number From The Options Bellow:

Enter '1' To Look At All The Games In This Database
Enter '2' To Check Information About The Data
Enter '3' To Find Data
Enter '4' To Order Data
Enter '5' To Exit This Program
       
""")
    #prints the data the user wants
    if user_input=="1":
        Print_All_Games()
        continue
    
    elif user_input=="2":
        user_input2=input(
"""

Which Information Would You Like To See?
Enter '1' To See All Of The Information 
Enter '2' To See All Of The Maker Information
Enter '3' To See All Of The Genre Information
Enter '4' To Exit This Page
Enter '5' To Exit This Program

""")
        if user_input2=="1":
            Print_All_Data()
            print("\n")
            
        elif user_input2=="2":
            Print_All_Makers()
            print("\n")

        elif user_input2=="3":
            Print_All_Genres()
            print("\n")

        elif user_input2=="4":
            print("\n")
            continue
        elif user_input2=="5":
            print("\n")
            print("Ok, See You Next Time.")
            break
        
        else:
            print("\n")
            print("This Is Not An option, Please Choose Again\n")
            continue
    
    elif user_input=="3":
        user_input3=input(
'''
What Would You Like To Find?
Enter '1' To Find All The Games With The Specific Genre
Enter '2' To Find All The Games With The Specific Maker
Enter '3' To Find All The Games With The Specific Release Year
Enter '4' To Find All The Games With The Specific IGN Rating
Enter '5' To Exit This Page
Enter '6' To Exit This Program

'''
        )
        if user_input3=="1":
            user_input3A=input(
""" 
What Genre Would You Like To See?
Enter '1' To Look At Games That Have 'Sandbox' Genre
Enter '2' To Look At Games That Have 'Battle Royale' Genre
Enter '3' To Look At Games That Have 'MOBA' Genre
Enter '4' To Look At Games That Have 'FPS' Genre
Enter '5' To Look At Games That Have 'Sports' Genre
Enter '6' To Look At Games That Have 'Fighting' Genre
Enter '7' To Look At Games That Have 'RPG' Genre
Enter '8' To Look At Games That Have 'Social Simulation' Genre
Enter '9' To Look At Games That Have 'Action-Adventure' Genre
Enter '10' To Look At Games That Have 'Party Game' Genre
Enter '11' To Exit This Page
Enter '12' To Exit This Program

"""
            )
            if user_input3A=="1":
                print("\n")
                Print_All_Data_Only_Genre_Sandbox()
            
            elif user_input3A=="2":
                print("\n")
                Print_All_Data_Only_Genre_Battle_Royale()
            elif user_input3A=="3":
                print("\n")
                Print_All_Data_Only_Genre_MOBA()
            
            elif user_input3A=="4":
                print("\n")
                Print_All_Data_Only_Genre_FPS()
            
            elif user_input3A=="5":
                print("\n")
                Print_All_Data_Only_Genre_Sports()
            
            elif user_input3A=="6":
                print("\n")
                Print_All_Data_Only_Genre_Fighting()
            
            elif user_input3A=="7":
                print("\n")
                Print_All_Data_Only_Genre_RPG()
            
            elif user_input3A=="8":
                print("\n")
                Print_All_Data_Only_Genre_Social_Simulation()
            
            elif user_input3A=="9":
                print("\n")
                Print_All_Data_Only_Genre_Action_Adventure()
            
            elif user_input3A=="10":
                print("\n")
                Print_All_Data_Only_Genre_Party_game()
            
            elif user_input3A=="11":
                print("\n")
                continue
            
            elif user_input3A=="12":
                print("Ok, See You Next Time.")
                break

            else:
                print("This Is Not An Option, Please Try Again\n")
                continue
        
        elif user_input3=="2":
            user_input3B= input(
'''
Which Maker Would You Like To See?
Enter '1' To Find Game/s Made By 'Mojang Studios' In This Database
Enter '2' To Find Game/s Made By 'Riot Games' In This Database
Enter '3' To Find Game/s Made By 'Psyonix' In This Database
Enter '4' To Find Game/s Made By 'Supercell' In This Database
Enter '5' To Find Game/s Made By 'Bandai Namco Studios' In This Database
Enter '6' To Find Game/s Made By 'Valve Corporation' In This Database
Enter '7' To Find Game/s Made By 'Nintendo EPD' In This Database
Enter '8' To Find Game/s Made By 'miHoYo' In This Database
Enter '9' To Find Game/s Made By 'FromSoftware' In This Database
Enter '10' To Find Game/s Made By 'The Sims Studio' In This Database
Enter '11' To Find Game/s Made By 'Rockstar Games' In This Database
Enter '12' To Find Game/s Made By 'Blizzard Entertainment' In This Database
Enter '13' To Find Game/s Made By 'Respawn Entertainment' In This Database
Enter '14' To Find Game/s Made By 'CD PROJEKT RED' In This Database
Enter '15' To Find Game/s Made By 'InnerSlothLLC' In This Database
Enter '16' To Find Game/s Made By 'Epic Games' In This Database
Enter '17' To Exit This Page
Enter '18' To Exit This Program

''')
            if user_input3B=="1":
                print("\n")
                Print_All_Data_Only_Maker_Mojang_Studios()
            
            elif user_input3B=="2":
                print("\n")
                Print_All_Data_Only_Maker_Riot_Games()
            
            elif user_input3B=="3":
                print("\n")
                Print_All_Data_Only_Maker_Psyonix()
            
            elif user_input3B=="4":
                print("\n")
                Print_All_Data_Only_Maker_Supercell()
            
            elif user_input3B=="5":
                print("\n")
                Print_All_Data_Only_Maker_Bandai_Namco_Studios()

            elif user_input3B=="6":
                print("\n")  
                Print_All_Data_Only_Maker_Valve_Corporation()
            
            elif user_input3B=="7":
                print("\n")
                Print_All_Data_Only_Maker_Nintendo_EPD()
            
            elif user_input3B=="8":
                print("\n")
                Print_All_Data_Only_Maker_miHoYo()
            
            elif user_input3B=="9":
                print("\n")
                Print_All_Data_Only_FromSoftware()
            
            elif user_input3B=="10":
                print("\n")
                Print_All_Data_Only_Maker_The_Sims_Studio()
            
            elif user_input3B=="11":
                print("\n")
                Print_All_Data_Only_Maker_Rockstar_Games()
            
            elif user_input3B=="12":
                print("\n")
                Print_All_Data_Only_Maker_Blizzard_Entertainment()
            
            elif user_input3B=="13":
                print("\n")
                Print_All_Data_Only_Maker_Respawn_Entertainment()
            
            elif user_input3B=="14":
                print("\n")
                Print_All_Data_Only_Maker_CD_PROJEKT_RED()
            
            elif user_input3B=="15":
                print("\n")
                Print_All_Data_Only_Maker_InnerSlothLLC()
            
            elif user_input3B=="16":
                print("\n")
                Print_All_Data_Only_Maker_Epic_Games()
            
            elif user_input3B=="17":
                print("\n")
                continue

            elif user_input3B=="18":
                print("\n")
                print("Ok, See You Next Time.")
                break

            else:
                print("This Is Not An Option, Please Try Again\n")
                continue

        elif user_input3=="3":
            try:
                user_input3C= int(input(
'''
Which Year Would You Like To See?

Tip:
Enter The Years Between 2009 - 2023 To Find Data


'''
            ))
                if user_input3C >=2009:
                    if user_input3C <=2023:
                        finalYear=str(user_input3C)
                        Print_All_Data_Only_Year_From_Input(finalYear)
                    
                    else:
                        print("No Data Found For The Year:", user_input3C)
                else:
                        print("No Data Found For The Year:", user_input3C)
            except:
                print("This Is Not A Number, Please Try Again")
                continue
            

        elif user_input3=="4":
            try:
                user_input3D= int(input(
'''
Which IGN Rating Would You Like To See?
Enter The Rating You Wanted To See:


'''
    ))
                if user_input3D >=7:
                    if user_input3D <=10:
                        finalnum=str(user_input3D)
                        Print_All_Data_Only_IGN_Rating_From_Input(finalnum)
                    
                    else:
                        print("No Data Found For The Number:", user_input3D)
                else:
                    print("No Data Found For The Number:", user_input3D)
            except:
                print("This Is Not A Number, Please Try Again")
                continue

        elif user_input3=="5":
            continue
        
        elif user_input3=="6":
            print("Ok, See You Next Time.")
            break
        
        else:
            print("This Is Not An Option, Please Try Again\n")
            continue

    elif user_input=="4":
        user_input4= input(
""" 
Which Order Would You Like To Sort The Data?
Enter '1' To Order the Data By Game Name
Enter '2' To Order The Data By Genre Name
Enter '3' To Order The Data By Maker Name
Enter '4' To Order The Data By Release Year
Enter '5' To Order The Data By IGN Rating
Enter '6' To Exit This Page
Enter '7' To Exit This Program
            
""")
        if user_input4=="1":
            Print_All_Data_Sorted_by_Game_Name()
            print("\n")
        elif user_input4=="2":
            Print_All_Data_Sorted_by_Genre_Name()
            print("\n")
        elif user_input4=="3":
            Print_All_Data_Sorted_by_Maker_Name()
            print("\n")
        elif user_input4=="4":
            Print_All_Data_Sorted_by_Release_year()
            print("\n")
        elif user_input4=="5":
            Print_All_Data_Sorted_by_IGN_Rating()
            print("\n")
        elif user_input4=="6":
            print("\n")
            continue
        elif user_input4=="7":
            print("Ok, See You Next Time.")
            break
        else:
            print("This Is Not An Option, Please Try Again\n")
            continue

        
    elif user_input=="5":
        print("Ok, See You Next Time.")
        break
        
    else:
            print("This Is Not An Option, Please Try Again\n")
            continue