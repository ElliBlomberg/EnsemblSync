from extract import get_gene_info
import database as db

#set upthe database
db.create_database()

#example gene name
gene_name = "BRCA1"

#example species
species = "homo_sapiens"

#getting gene info
gene_info = get_gene_info(gene_name, species)

print(gene_info)

db.insert_gene_data(gene_info)

column = ["gene_name", "gene_id", "species", "description", "location", "biotype"]
species = "homo_sapiens"
dbresult = db.get_genedata_from_db(column[2], species)
print(dbresult)