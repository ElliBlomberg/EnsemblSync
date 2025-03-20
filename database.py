import sqlite3

def create_database():
	conn = sqlite3.connect('EnsemblSync.db') #Connect to SQLite DB (it creates DB if not exist)
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
	
	conn.commit()  # Save changes to the database
	conn.close()  # Close the database connection


def insert_gene_data(gene_data):
	conn = sqlite3.connect('EnsemblSync.db')
	c = conn.cursor

	gene_name = gene_data.get('display_name')
	gene_id = gene_data.get('id')
	species = gene_data.get('species')
	description = gene_data.get('decription')
	location = gene_data.get('seq_region_name') + ":" + str(gene_data.get('start')) + "-" + str(gene_data.get('end'))
	biotype = gene_data.get('biotype')

	c.execute('''INSERT INTO genes (gene_name, gene_id, species, description, location, biotype)
					VALUES (?, ?, ?, ?, ?, ?)''', 
					(gene_name, gene_id, species, description, location, biotype))
	
	conn.commit()
	conn.close()


def get_genedata_from_db(column, value):
	conn = sqlite3.connect('EnsemblSync.db')
	c = conn.cursor

	c.execute('''SELECT * FROM genes WHERE ? = ?''', (column, value))
	result = c.fetchall()

	conn.close()

	return result

