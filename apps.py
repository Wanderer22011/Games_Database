''' This is a Pythorn + SQL code that can sort and check all the datas in the games.db database
Made by Wilson Tong on the 22/05/24'''

import sqlite3

# Variable Declarations:
DATABASE="Game_Database.db"

#Functions
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




while True:
    user_input=input("\nWhat would you like to see from this games database?\n 1.Show all data of the games\n 2.Show all the data of the games ordered by game name\n 3.Show all the data of the games ordered by Maker name\n")
    if user_input=="1":
        Print_All_Data()
    elif user_input =="2":
        Print_All_Data_Sorted_by_Game_Name()
    elif user_input == "3":
        Print_All_Data_Sorted_by_Maker_Name()
    else:
            print("This is not an option, please try again.")
            continue
 