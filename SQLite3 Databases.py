import sqlite3
# VIEWING DATABASE TABLES DATA

def deleteTrack():
    music_conn =sqlite3.connect("Tracks.db")
    music_cur = music_conn.cursor()
    music_cur.execute("DELETE From Musiclist Where Plays=14")
    music_conn.commit()
    music_conn.close()
    print("done")
deleteTrack()

# def updateTrack():
#     music_conn =sqlite3.connect("Tracks.db")
#     music_cur = music_conn.cursor()
#     music_cur.execute("UPDATE Musiclist SET Plays=20 WHERE Title = 'My Way'")
#     music_cur.execute("UPDATE Musiclist SET Plays=18 WHERE Title = 'for days'")
#     music_cur.execute("UPDATE Musiclist SET Plays=14 WHERE Title = 'kenkele'")
#     music_conn.commit()
#     music_conn.close()
#     print("done")
# updateTrack()


# def viewStudentInfo():
#     conn =sqlite3.connect("Tracks.db")
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM Musiclist")
#     records = cur.fetchall()
#     conn.close()
#     print(records)
# viewStudentInfo()


# def musicChartCreate():
#     conn = sqlite3.connect("Tracks.db")
#     cur = conn.cursor()
#     cur.execute("DROP TABLE IF EXISTS Musiclist") # EXECUTES QUERY
#     cur.execute("CREATE TABLE Musiclist (Title TEXT, Artiste TEXT, Plays INTEGER)")
#     conn.commit()
#     conn.close()
#     print("Table created")
#
# def musicChart(Title,Artiste,Plays):
#     conn = sqlite3.connect("Tracks.db")
#     cur = conn.cursor()
#     cur.execute("INSERT INTO Musiclist VALUES (?,?,?)", (Title,Artiste,Plays))
#     conn.commit()
#     conn.close()
#     print("Data Inserted")
#
# # musicChart("My way", "Usher", 15)
# # musicChart("for days", "buju", 105)
# musicChart("kenkele", "buju fka bnxn", 10225)
#


# def viewStudentInfo():
#     conn =sqlite3.connect("College.db")
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM Student")
#     records = cur.fetchall()
#     conn.close()
#     print(records)
# viewStudentInfo()

input()
#
# conn =sqlite3.connect("Classwork.db")   #CREATE College.db DATABASES
# cur = conn.cursor()   # CREATE CURSOR OBJECT
# cur.execute("DROP TABLE IF EXISTS Student") # EXECUTES QUERY
# cur.execute("CREATE TABLE Student (StudentName TEXT, PhoneNumber INTEGER, Email TEXT)")
# conn.commit()               #COMIIT/SAVES TABLE CHANGES
# conn.close()                # CLOSES DATABASE CONNECTION
# print("Table Created")      # VALIDATING ACTIONS

#ADDING DATABASE TABLES DATA

# def addStudentInfo(StudentID, StudentName):
#     import sqlite3
#     conn = sqlite3.connect("College.db")
#     cur = conn.cursor()
#     cur.execute("INSERT INTO Student VALUES (?,?)", (StudentID, StudentName))
#     conn.commit()
#     conn.close()
#     print("Data Inserted")
# addStudentInfo(890, 'Miriam')
# addStudentInfo(891, 'Charles')
# addStudentInfo(892, 'Faith')

# def newStudentInfo():
#     import sqlite3
#     conn = sqlite3.connect("Classwork.db")
#     cur = conn.cursor()
#     for i in range(3):
#         StudentName = input("Enter Your Name: ")
#         PhoneNumber = input("Enter Your PhoneNumber: ")
#         Email = input("Enter Your Email: ")
#         cur.execute("INSERT INTO Student VALUES (?,?,?)", (StudentName, PhoneNumber, Email))
#         print("Data Inserted")
#     conn.commit()
#     conn.close()
#     print("All Data haa been Inserted")
#
# newStudentInfo()
