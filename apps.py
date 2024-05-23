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
    for final in results:
        print(final)
    db.close
user_input=input("What would you like to see from this games database?\n 1.Show all data about the games\n 2.Exit\n")
if user_input=="1":
    Print_All_Data()
elif user_input =="2":
    exit