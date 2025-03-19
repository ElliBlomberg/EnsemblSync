import sqlite3

def create_database():
	conn = sqlite3.connect('StreamLine.db') #Connect to SQLite DB (it creates DB if not exist)
	c = conn.cursor

	#create Genes table
	c.execute('''CREATE TABLE IF NOT EXISTS genes (
		   			id INTEGER PRIMARY KEY AUTOINCREMENT,
		   			gene_name TEXT,
		   			gene_id TEXT,
		   			species TEXT,
		   			description TEXT,
		   			location TEXT,
		   			biotype TEXT)''')
	
	conn.commit()
	conn.close()