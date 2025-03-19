import requests

ENSEMBL_API_URL = "https://rest.ensembl.org"

def get_gene_info(gene_name, species):
	url = f"{ENSEMBL_API_URL}/lookup/symbol/{species}/{gene_name}?content-type=application/json"
	response = requests.get(url)

	if response.status_code == 200:
		return response.json()
	else:
		print(f"Error {response.status_code}: {response.text}")
		return None
	