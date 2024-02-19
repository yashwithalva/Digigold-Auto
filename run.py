from apicalls.api_calls import *
from helpers.helpers import randomword

def default_script() -> bool:
    warehouse_lst = []
    randstr = ' ' + randomword(5)
    print(randstr)
    
    # Create Address 
    print("\n>> ADDRESS")
    addr_id = create_address()
    
    # Create Company
    print("\n>> COMPANY")
    company_name = f'Company {randstr}'
    company_id = create_and_commission_company(addr_id, company_name)
    
    print("\n>> WAREHOUSE")
    warehouse_lst = create_warehouse_chain(warehouse_lst, randstr, company_id, addr_id)
    print(f'Warehouse List: {warehouse_lst}\n')
    
    # PO, PI and GR
    print("\n>> PO, PI & GR")
    load_material_to_parent(company_id, warehouse_lst[0])    
        
    # Material Transfer
    print("\n>> Material Transfer")
    materail_transfer_from_root_to_store(warehouse_lst, company_id)

    # Creating rack
    print("\n>> Create Racks")
    create_racks_and_load(warehouse_lst[-1])
    
    return True
    

    
default_script()