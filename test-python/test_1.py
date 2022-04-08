""" 
  1) consulte la información del archivo data.py
  cree un objeto que contenga las empresas y dentro 
  las sucursales que corresponden para cada empresa
"""


from data import Data

companies = Data.get_companies()
branches = Data.get_branches()

for company in companies:
    branches_list = []
    for branch_id in company["branches"]:
        for branch in branches:
            branches_list.append(branch) if branch["id"] == branch_id else None

    company["branches"] = branches_list

# companies contiene la lista de objetos que dan solución a esta prueba.
