''' This is a Pythorn + SQL code that can sort and check all the datas in the games.db database
Made by Wilson Tong on the 22/05/24'''

# Gains acess to Sql codes and data
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

def Print_All_Data_Only_Genre_Sandbox():
    db=sqlite3.connect(DATABASE)
    cursor=db.cursor()
    sql="SELECT Games.game_name, Genres.genre_name, Makers.maker_name, Games.IGN_rating, Games.release_year FROM Games JOIN Genres ON Genres.genre_id = Games.genre_id JOIN Makers ON Makers.maker_id=Games.maker_id WHERE Genre.genre_name='Sandbox';"
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
        Which Information would u like to see?
        Enter '1' To See All of The Information 
        Enter '2' To See All of The Maker Information
        Enter '3' To See All of The Genre Information
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
            print("This is not an option, Please choose again.")
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
        
        elif user_input3=="2":
        
        elif user_input3=="3":
        
        elif user_input3=="4":
        
        elif user_input3=="5":
            continue
        
        elif user_input3=="6":
            print("Ok, See You Next Time.")
            break
        
        else:
             print("This is not an option, please try again.\n")
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
            print("This is not an option, please try again.\n")
            continue

        
    elif user_input=="5":
        print("Ok, See You Next Time.")
        break
        
    else:
            print("This is not an option, please try again.\n")
            continue