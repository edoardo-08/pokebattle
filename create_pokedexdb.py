import pandas as pd
import sqlite3

#pok = pd.read_csv(r'C:\Users\edoar\Downloads\archive\pokedex_(Update_04.21).csv')

#pok.drop(pok.columns[24:],axis=1,inplace=True)

#pok.drop(columns = ['Unnamed: 0', 'german_name', 'species' ,
#'japanese_name', 'type_number', 'type_2', 
#'abilities_number', 'ability_2', 'ability_hidden'], inplace = True )
#pok = pok.loc[pok["pokedex_number"].shift() != pok["pokedex_number"]]

#pok.rename(columns = {'type_1':'type','ability_1':'ability'},inplace=True)


#pok.to_csv('pokedex.csv',index = False,header=False)

db = sqlite3.connect('pokedex.db')
my_cursor = db.cursor()

sql = '''
        CREATE TABLE  pokemons (
            pokedex_number INTEGER,
            name TEXT,
            generation INTEGER,
            status TEXT,
            type TEXT,
            height_m REAL,
            weight_kg REAL,
            ability TEXT,
            total_points INTEGER,
            hp INTEGER,
            attack INTEGER,
            defense INTEGER,
            sp_attack INTEGER,
            sp_defense INTEGER,
            speed INTEGER,
            PRIMARY KEY (pokedex_number)        
            ) '''

my_cursor.execute(sql)
db.commit()

with open('pokedex.csv') as file:       
    for row in file:
        my_cursor.execute("INSERT INTO pokemons VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", row.split(','))
        db.commit()
           
   
db.close()