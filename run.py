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
    supplier_id = create_and_commission_supplier('Supplier-GS', address_id)
    material_id = create_and_commission_material(supplier_id)

    print("\nCreate Tax Template: ")
    tax_template_sell_id = create_and_commission_tax_template("Tax-Template Sell", 1.5, 1.5)
    tax_template_buy_id = create_and_commission_tax_template("Tax-Template Buy", 0, 0)
    tax_template_company_buy_id = create_and_commission_tax_template("Tax-Template Company Buy", 1.5, 1.5)
    tax_template_company_sell_id = create_and_commission_tax_template("Tax-Template Company Sell", 1.5, 1.5)

    create_and_commission_tax_template_mapping(tax_template_sell_id,
                                               MATERIAL_CODE,
                                               "SELL",
                                               "INDIVIDUAL")
    create_and_commission_tax_template_mapping(tax_template_buy_id,
                                               MATERIAL_CODE,
                                               "BUY",
                                               "INDIVIDUAL")

    create_and_commission_tax_template_mapping(tax_template_company_buy_id,
                                               MATERIAL_CODE,
                                               "SELL",
                                               "COMPANY")
    create_and_commission_tax_template_mapping(tax_template_company_sell_id,
                                               MATERIAL_CODE,
                                               "BUY",
                                               "COMPANY")
    return True


def tenant_users_add_script(number_of_users) -> bool:
    """
    A script to add tenant users
    """

    return True


def warehouse_load_script() -> bool:
    """
    A Default script to Load material to warehouse
    """
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
    material_transfer_from_root_to_store(warehouse_lst, company_id)

    # Creating rack
    print("\n>> Create Racks")
    create_racks_and_load(warehouse_lst[-1])

    return True


def material_transaction_script() -> bool:
    """
    A script to perform material transaction
    """

    return True


def temporary_script():
    address_id = "ADD-01HQB15ZY1S9V8W4HE4J4K2G1V"
    company_id = "COM-01HQB15ZZXNM0TRYA7KQYN00XS"
    gor_id = "GOR-01HQB160CM1MMJ12346KX7C337"
    transit_warehouse_id = "WAR-01HQB16014XSM46Z4CR0GS3HNF"
    store_warehouse_id = "WAR-01HQB1601VZH2XWMHSJNGAZ3SF"
    warehouse_lst = ["WAR-01HQB16014XSM46Z4CR0GS3HNF", "WAR-01HQB1601VZH2XWMHSJNGAZ3SF"]

    print(complete_gr(gor_id))

    # Material Transfer
    print("\n>> Material Transfer")
    material_transfer_from_root_to_store(warehouse_lst, company_id)

    # Creating rack
    print("\n>> Create Racks")
    create_racks_and_load(warehouse_lst[-1])


if __name__ == "__main__":
    # material_setup_script()
    # warehouse_load_script()
    temporary_script()
