import sqlite3

# connecting to database file
mycurs = sqlite3.connect('Fantasy.db')  
curs = mycurs.cursor()

#CREATING MATCH TABLE
curs.execute('''CREATE TABLE IF NOT EXISTS Match (Player TEXT NOT NULL,Scored INTEGER,Faced INTEGER,Fours INTEGER,Sixes INTEGER,Bowled INTEGER,Maiden INTEGER,Given INTEGER,Wkts INTEGER,Catches INTEGER,Stumping INTEGER,Run Out INTEGER);''')

#CREATING STATS TABLE
curs.execute('''CREATE TABLE IF NOT EXISTS Stats (Player PRIMARY KEY,Matches INTEGER,Runs INTEGER,Hundreds INTEGER,Fifty INTEGER,Value INTEGER,ctg TEXT NOT NULL);''')

#CREATING TEAMS TABLE
curs.execute('''CREATE TABLE IF NOT EXISTS Teams (Name TEXT NOT NULL,Players TEXT NOT NULL,Value INTEGER);''')

#DISPLAY DATA IF EXISTS IN DATABASE
sql="select * from Match"
curs.execute(sql)
result=curs.fetchall()
if(result):
    for i in result:
        print(i)
    opt=input("\n Want to add more Player's Details? (Y/N): ")
else:
    print("Player's data not found ")
    opt=input("\n Want to add Player's Data (Y/N) :")
    
#ADDING DATA FROM USER TO MATCH TABLE
while(opt=='y' or opt=='Y'):
    
    row=[input("Player name:")]
    row.append(int(input("Score:")))
    row.append(int(input("Faced: ")))
    row.append(int(input("Fours: ")))
    row.append(int(input("Sixes: ")))
    row.append(int(input("Bowled: ")))
    row.append(int(input("Maiden: ")))
    row.append(int(input("Given: ")))
    row.append(int(input("Wkts: ")))
    row.append(int(input("Catches: ")))
    row.append(int(input("Stumping: ")))
    row.append(int(input("Run Out: "))) 
    try:
        curs.execute("INSERT INTO Match (Player,Scored, Faced, Fours,Sixes,Bowled,Maiden,Given,Wkts,Catches,Stumping,Run Out) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", (row[0],row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]))
        mycurs.commit()
        print("Record added successfully in Match Table.")
    except:    # except block to handle exceptions
        print("Error in Operation.")
        mycurs.rollback()

#ADDING DATA TO STATS TABLE FROM USER 
    print("Player information for Stats table ")
    row.append(int(input("Total Matches: ")))
    row.append(int(input("Total Runs: ")))
    row.append(int(input("100s: ")))
    row.append(int(input("50s: ")))
    row.append(int(input("Value: ")))
    row.append(input("Category as (BAT,BWL,AR,WK): "))
    
    try:       #try block to catch exceptions
    
        curs.execute("INSERT INTO Stats (Player,Matches,Runs, Hundreds, Fifty,Value,ctg) VALUES (?,?,?,?,?,?,?)",(row[0],row[12], row[13], row[14],row[15],row[16],row[17]))
        mycurs.commit()
        print("Records added successfully for Stats table.")
    except:    # except block to handle exceptions
        print("Error in Operation.")
        mycurs.rollback()
    opt=input("Want to add more players ? (Y/N) : ")
print("Thank you")   
curs.close() #close database

    
    
    
    
    
    

    
    

    
    
    
    
    
 
                          
        

        
     
        
        
    
    
    
        

    
    
    
    
    

    
    
         
    
    
                          
        

    
    
        
        
        
    
    
        

    

