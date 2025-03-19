from extract import get_gene_info
from database import create_database

#set upthe database
create_database()

#example gene name
gene_name = "BRCA1"

#example species
species = "homo_sapiens"

#getting gene info
gene_info = get_gene_info(gene_name, species)

print(gene_info)