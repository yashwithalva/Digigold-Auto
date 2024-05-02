from apicalls.warehouse_load_api import *
from apicalls.material_creation_api import *
from helpers.helpers import randomword
from constants.material_setup_config import MATERIAL_CODE


def material_setup_script() -> bool:
    """
    A script to create a new material.
    """
    print("Creating Material Type: ")
    address_id = create_address()
    create_and_commission_material_type()

    print("\nCreating Supplier: ")
    supplier_id = create_and_commission_supplier('Supplier', address_id)

    print("\nCreating Material: ")
    material_id = create_and_commission_material(supplier_id)

    print("\nCreate Tax Template: ")
    tax_template_150_id = create_and_commission_tax_template("FLOW TEST Tax-Template", 1.5, 1.5)
    tax_template_00_id = create_and_commission_tax_template("Tax-Template Individual Buy", 0, 0)

    print("\nCreating Tax Template Mapping: ")
    create_and_commission_tax_template_mapping(tax_template_150_id,
                                               MATERIAL_CODE,
                                               "SELL",
                                               "INDIVIDUAL")

    create_and_commission_tax_template_mapping(tax_template_00_id,
                                               MATERIAL_CODE,
                                               "BUY",
                                               "INDIVIDUAL")

    create_and_commission_tax_template_mapping(tax_template_150_id,
                                               MATERIAL_CODE,
                                               "SELL",
                                               "COMPANY")

    create_and_commission_tax_template_mapping(tax_template_150_id,
                                               MATERIAL_CODE,
                                               "BUY",
                                               "COMPANY")
    return True


def warehouse_load_script() -> bool:
    """
    A Default script to Load material to warehouse
    """
    create_and_commission_all_material_transfer_types()

    warehouse_lst = []
    randstr = ' ' + randomword(3)
    print(randstr)

    # Create Address
    print("\n>> ADDRESS")
    addr_id = create_address()

    # Create Company
    print("\n>> COMPANY")
    company_name = f'{warehouse_load_config.NAMING_PREFIX}Company {randstr}'
    company_id = create_and_commission_company(addr_id, company_name)

    print("\n>> WAREHOUSE")
    warehouse_lst = create_warehouse_chain(warehouse_lst, randstr, company_id, addr_id)
    print(f'Warehouse List: {warehouse_lst}\n')

    # PO, PI and GR
    print("\n>> PO, PI & GR")
    load_material_to_parent(company_id, warehouse_lst[0])

    # Material Transfer
    print("\n>> Material Transfer")
    material_transfer_from_root_to_store(warehouse_lst, company_id)

    # Creating rack
    print("\n>> Create Racks")
    create_racks_and_load(warehouse_lst[-1])

    return True


if __name__ == "__main__":
    """
    1. Setup material_setup_config before running material_setup_config.
    2. Call material_setup_script to setup Material and Tax. 
        -> Copy the supplier Id from console and set it in warehouse_load_config.
    3. Setup warehouse load config.
    4. Add run Warehouse load script.
        -> This script populates warehouse with material
        -> It also loads the warehouse racks with material
        -> Setup attributes for loading the warehouse racks with
           material in warehouse load config.
    """
    # material_setup_script()
    # warehouse_load_script()
    # temporary_script()
    # create_and_commission_all_material_transfer_types()
