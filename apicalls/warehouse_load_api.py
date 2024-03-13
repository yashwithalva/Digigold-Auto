import json
import requests

from constants import warehouse_load_config
from constants.api_constants import *
from models import warehouse_load_dto


####################################################
# BASIC API CALLS
# API calls for individual api
####################################################

def create_address() -> str:
    """
    Create Address
    Returns:
        str: the address id
    """
    json_body = json.dumps(warehouse_load_dto.create_addr_req)
    res = requests.post(HOST + CREATE_ADDRESS_URL, data=json_body, headers=HEADER_INFO)
    address_id = res.json()['data']['id']
    print(f'Created address with address_id: {address_id}')
    return address_id


def create_company(address_id, name=warehouse_load_config.COMPANY_NAME, acc_name='Account name') -> str:
    """
    Create a new Company
    Args:
        address_id (str): the address id of the company
        name (str, optional): Name of the company. Defaults to 'Auto Create'.
        acc_name (str, optional): Name of the bank account. Defaults to 'Account name'.

    Returns:
        string: the company id
    """
    warehouse_load_dto.create_company_req['name'] = f'{warehouse_load_config.NAMING_PREFIX}{name}'
    warehouse_load_dto.create_company_req['bankDetails']['accountName'] = acc_name
    warehouse_load_dto.create_company_req['addressId'] = address_id

    json_body = json.dumps(warehouse_load_dto.create_company_req)
    res = requests.post(HOST + CREATE_COMPANY_URL, data=json_body, headers=HEADER_INFO)
    company_id = res.json()['data']['id']
    print(f'Created Company with company id: {company_id}')
    return company_id


def commission_company(company_id) -> bool:
    """
    Commission a Company
    Args:
        company_id (str): the id of company

    Returns:
        bool: true if successfully commissioned
    """

    request_params = {
        'id': company_id
    }
    res = requests.post(HOST + COMMISSION_COMPANY_URL, headers=HEADER_INFO, params=request_params, data=json.dumps({}))
    msg = res.json()['data']
    print(f'[MESSAGE]: {msg}')
    return res.json()['success']


def create_warehouse(is_transit, name, company_id, address_id, is_parent=True, parent_id="") -> str:
    """
    Create a warehouse
    Args:
        is_transit (bool): True if a transit warehouse
        name (str): Name of the warehouse
        company_id (str): The company id
        address_id (str): The address id
        is_parent (bool, optional): Is a parent warehouse. Defaults to True.
        parent_id (str, optional): Parent warehouse id. Defaults to "".

    Returns:
        str: Warehouse ID
    """
    warehouse_load_dto.create_warehouse_req['addressId'] = address_id
    warehouse_load_dto.create_warehouse_req['companyId'] = company_id

    if not is_transit:
        warehouse_load_dto.create_warehouse_req['name'] = f'{warehouse_load_config.NAMING_PREFIX}{name}'
        warehouse_load_dto.create_warehouse_req['parentWarehouseId'] = parent_id
        warehouse_load_dto.create_warehouse_req['type'] = "STORE"
        warehouse_load_dto.create_warehouse_req['isParentWarehouse'] = False
    else:
        warehouse_load_dto.create_warehouse_req['name'] = f'{warehouse_load_config.NAMING_PREFIX}{name}'
        warehouse_load_dto.create_warehouse_req['isParentWarehouse'] = is_parent
        warehouse_load_dto.create_warehouse_req['parentWarehouseId'] = parent_id

    json_body = json.dumps(warehouse_load_dto.create_warehouse_req)
    res = requests.post(HOST + CREATE_WAREHOUSE_URL, headers=HEADER_INFO, data=json_body)
    warehouse_id = res.json()['data']['id']
    print(f'Created Warehouse with id: {warehouse_id}')
    return warehouse_id


def commission_warehouse(warehouse_id) -> bool:
    """
    Commission warehouse
    Args:
        warehouse_id (str): The warehouse id

    Returns:
        bool: True if commissioned successfully 
    """
    req_param = {
        "id": warehouse_id
    }
    res = requests.post(HOST + COMMISSION_WAREHOUSE_URL, headers=HEADER_INFO, params=req_param)
    msg = res.json()['data']
    print(f'[MESSAGE]: {msg}')
    return res.json()['success']


def create_warehouse_material_transfer_type(transfer_type):
    req_body = {
        'type': transfer_type
    }
    res = requests.post(HOST + CREATE_MATERIAL_TRANSFER_TYPE_URL, headers=HEADER_INFO, data=json.dumps(req_body))
    material_transfer_id = res.json()['data']['id']
    print(f'Created Warehouse with id: {material_transfer_id}')
    return material_transfer_id


def commission_warehouse_material_transfer_type(material_transfer_id):
    req_param = {
        "id": material_transfer_id
    }
    res = requests.post(HOST + COMMISSION_MATERIAL_TRANSFER_TYPE_URL, headers=HEADER_INFO, params=req_param)
    msg = res.json()['data']
    print(f'[MESSAGE]: {msg}')
    return res.json()['success']


def create_po(company_id, target_warehouse) -> str:
    """
    Create a Purchase Order
    Args:
        company_id (str): The company id
        target_warehouse (str): The target warehouse id

    Returns:
        str: The purchase order id
    """
    warehouse_load_dto.create_po_req['companyId'] = company_id
    warehouse_load_dto.create_po_req['targetWarehouseId'] = target_warehouse

    json_body = json.dumps(warehouse_load_dto.create_po_req)
    res = requests.post(HOST + CREATE_PURCHASE_ORDER_URL, headers=HEADER_INFO, data=json_body)
    print(res.json())
    po_id = res.json()['data']['id']
    print(po_id)
    return po_id


def submit_po(po_id) -> bool:
    """
    Submit the Purchase Order
    Args:
        po_id (str): The purchase order id

    Returns:
        bool: True if success
    """
    req_params = {
        'id': po_id
    }
    res = requests.post(HOST + SUBMIT_PURCHASE_ORDER_URL, headers=HEADER_INFO, params=req_params)
    msg = res.json()['data']
    print(f'[MESSAGE]: {msg}')
    return res.json()['success']


def create_pi(po_id) -> str:
    """
    Create a Purchase Invoice
    Args:
        po_id (str): The purchase order id

    Returns:
        str: The purchase invoice id
    """
    warehouse_load_dto.create_pi_req['purchaseOrderId'] = po_id

    json_body = json.dumps(warehouse_load_dto.create_pi_req)
    res = requests.post(HOST + CREATE_PURCHASE_INVOICE_URL, headers=HEADER_INFO, data=json_body)
    print(res.json())
    pi_id = res.json()['data']['id']
    print(pi_id)
    return pi_id


def submit_pi(pi_id) -> bool:
    """
    Submit the purchase invoice
    Args:
        pi_id (str): The purchase invoice id

    Returns:
        bool: True if successfully submitted
    """
    req_params = {
        'id': pi_id
    }
    res = requests.post(HOST + SUBMIT_PURCHASE_INVOICE_URL, headers=HEADER_INFO, params=req_params)
    msg = res.json()['data']
    print(f'[MESSAGE]: {msg}')
    return res.json()['success']


def create_gr(po_id, pi_id) -> str:
    """
    Create Good Receipt
    Args:
        po_id (str): The purchase order id
        pi_id (str): The purchase invoice id

    Returns:
        str: The Good Receipt id
    """
    warehouse_load_dto.create_gr_req['purchaseInvoiceId'] = pi_id
    warehouse_load_dto.create_gr_req['purchaseOrderId'] = po_id

    json_body = json.dumps(warehouse_load_dto.create_gr_req)
    res = requests.post(HOST + CREATE_GOOD_RECEIPT_URL, headers=HEADER_INFO, data=json_body)
    gr_id = res.json()['data']['id']
    print(gr_id)
    return gr_id


def submit_gr(gr_id) -> bool:
    """
    Submit the Good Receipt
    Args:
        gr_id (str): Good Receipt id

    Returns:
        bool: True if successfully submitted
    """
    req_params = {
        'id': gr_id
    }
    res = requests.post(HOST + SUBMIT_GOOD_RECEIPT_URL, headers=HEADER_INFO, params=req_params)
    print(res.json())
    msg = res.json()['data']
    print(f'[MESSAGE]: {msg}')
    return res.json()['success']


def complete_gr(gr_id) -> bool:
    """
    Complete the Good Receipt successfully
    Args:
        gr_id (str): The Good Receipt id

    Returns:
        bool: True if completed successfully
    """
    req_params = {
        'id': gr_id
    }
    res = requests.post(HOST + COMPLETE_GOOD_RECEIPT_URL, headers=HEADER_INFO, params=req_params)
    print(res.json())
    msg = res.json()['data']
    print(f'[MESSAGE]: {msg}')
    return res.json()['success']


def create_material_transfer(company_id, source, target) -> str:
    """
    Create a material transfer from parent to child

    Args:
        company_id (str): The company id
        source (str): The source warehouse id
        target (str): The target warehouse id

    Returns:
        str: Material Transfer ID
    """
    warehouse_load_dto.parent_to_child_mt_req['companyId'] = company_id
    warehouse_load_dto.parent_to_child_mt_req['sourceWarehouseId'] = source
    warehouse_load_dto.parent_to_child_mt_req['targetWarehouseId'] = target

    json_body = json.dumps(warehouse_load_dto.parent_to_child_mt_req)
    res = requests.post(HOST + CREATE_MATERIAL_TRANSFER_URL, headers=HEADER_INFO, data=json_body)
    mt_id = res.json()['data']['id']
    print('Created material Transfer of id: ' + mt_id)
    return mt_id


def complete_material_transfer(mt_id) -> bool:
    """
    Complete Material Transfer
    Args:
        mt_id (str): The material transfer id

    Returns:
        bool: True if completed successfully
    """
    req_params = {
        'id': mt_id
    }
    res = requests.post(HOST + COMPLETE_MATERIAL_TRANSFER_URL, headers=HEADER_INFO, params=req_params)
    msg = res.json()['data']
    print(f'[MESSAGE]: {msg}')
    return res.json()['success']


def create_racks(warehouse_id, rack_type) -> bool:
    """
    Create Racks
    Args:
        warehouse_id (str): The warehouse id
        rack_type (str): The type -> IN or OUT

    Returns:
        bool: True if racks successfully created
    """
    warehouse_load_dto.create_racks_req['warehouseId'] = warehouse_id
    warehouse_load_dto.create_racks_req['type'] = rack_type

    json_body = json.dumps(warehouse_load_dto.create_racks_req)
    res = requests.post(HOST + CREATE_RACK_URL, headers=HEADER_INFO, data=json_body)
    print("Created a Rack with ID: " + warehouse_id)
    return res.json()['success']


def commission_racks(warehouse_id) -> bool:
    """
    Commission the racks
    Args:
        warehouse_id (str): The warehouse id

    Returns:
        bool: True if successfully commissioned
    """
    req_body = {
        'warehouseId': warehouse_id
    }
    res = requests.post(HOST + COMMISSION_RACK_URL, headers=HEADER_INFO, data=json.dumps(req_body))
    msg = res.json()['success']
    print(f'[MESSAGE]: {msg}')
    return res.json()['success']


def load_racks(warehouse_id) -> bool:
    """
    Load Out Rack with material
    Args:
        warehouse_id (str): Load the warehouse id

    Returns:
        bool: True if loaded successfully
    """
    req_params = {
        'warehouseId': warehouse_id
    }
    res = requests.post(HOST + LOAD_RACK_URL, headers=HEADER_INFO, params=req_params)
    print(res.json())
    msg = res.json()['success']
    print(f'[MESSAGE]: {msg}')
    return res.json()['success']


####################################################
# COMPOSITE API CALLS
# Consist of multiple api calls grouped Together
#################################################### 

def create_and_commission_company(addr_id, company_name):
    """
    Create and Commission Company
    Args:
        addr_id (str): The address id
        company_name (str): The company name
    
    Returns:
        str: The company id
    """
    company_id = create_company(addr_id, company_name)
    commission_company(company_id)
    return company_id


def create_and_commission_warehouse(is_transit, level, randstr, company_id, addr_id, parent_id=None) -> str:
    """
    Create a commissioned warehouse
    Args:
        is_transit (bool): Is a Transit warehouse
        level (int): Number of warehouses in the chain 
        randstr (str): Unique string added to the names
        company_id (str): The company id
        addr_id (str): The address id
        parent_id (str, optional): The parent warehouse. Defaults to None.

    Returns:
        str: The commissioned warehouse
    """
    warehouse_name = (
        f'{warehouse_load_config.WAREHOUSE_ROOT_NAME}{randstr}' if not parent_id else
        f'{warehouse_load_config.WAREHOUSE_INTERNAL_NODE_NAME}{level} {randstr}' if is_transit else
        f'{warehouse_load_config.WAREHOUSE_STORE_NAME}{randstr}'
    )

    warehouse_id = create_warehouse(is_transit, warehouse_name, company_id, addr_id, True, parent_id)
    commission_warehouse(warehouse_id)
    return warehouse_id


def create_warehouse_chain(warehouse_list, randstr, company_id, addr_id) -> list:
    """
    Create a chain of warehouses. Chain length determined by 
    Args:
        warehouse_list (list): List of the warehouses in chain
        randstr (str): Unique random string added to the end
        company_id (str): The company id
        addr_id (str): The address id

    Returns:
        list: The warehouse list
    """
    # Add Root node
    warehouse_list.append(create_and_commission_warehouse(True, 0, randstr, company_id, addr_id))

    # Add Internal Nodes
    for i in range(1, warehouse_load_config.WAREHOUSE_LEVELS - 1):
        warehouse_id = create_and_commission_warehouse(True, i, randstr, company_id, addr_id, warehouse_list[-1])
        warehouse_list.append(warehouse_id)

    # Add store nodes
    warehouse_list.append(create_and_commission_warehouse(False, 0, randstr, company_id, addr_id, warehouse_list[-1]))

    return warehouse_list


def load_material_to_parent(company_id, root_warehouse):
    """
    Load material to Main warehouse
    Args:
        company_id (str): The company id
        root_warehouse (str): Main warehouse id
    """
    po_id = create_po(company_id, root_warehouse)
    submit_po(po_id)

    pi_id = create_pi(po_id)
    submit_pi(pi_id)

    gr_id = create_gr(po_id, pi_id)
    submit_gr(gr_id)
    complete_gr(gr_id)


def material_transfer_from_root_to_store(warehouse_lst, company_id):
    """
    Transfer material from root to store warehouse
    Args:
        warehouse_lst (list[]): List of warehouse from root to store
        company_id (str): The company id
    """
    levels = len(warehouse_lst)
    for i in range(0, levels - 1):
        print(f'Material Transfer between {warehouse_lst[i]} and {warehouse_lst[i + 1]}')
        mt_id = create_material_transfer(company_id, warehouse_lst[i], warehouse_lst[i + 1])
        complete_material_transfer(mt_id)
        print(f'>> Material Transfer completed between {warehouse_lst[i]} and {warehouse_lst[i + 1]} \n')


def create_racks_and_load(warehouse_id):
    """
    Create Racks and Load material
    Args:
        warehouse_id (str): The Warehouse id
    """
    create_racks(warehouse_id, "IN")
    create_racks(warehouse_id, "OUT")
    commission_racks(warehouse_id)
    load_racks(warehouse_id)
    print("Racks loaded successfully")

def create_and_commission_all_material_transfer_types():
    transfer_types = [
        'PARENT_WAREHOUSE_LOAD',
        'PARENT_WAREHOUSE_UNLOAD',
        'WAREHOUSE_PARENT_TO_CHILD_TRANSFER',
        'WAREHOUSE_CHILD_TO_PARENT_TRANSFER',
        'WAREHOUSE_IN_TO_OUT_RACK_MATERIAL_TRANSFER',
        'WAREHOUSE_OUT_TO_IN_RACK_MATERIAL_TRANSFER',
        'WAREHOUSE_IN_RACK_REBALANCING_MATERIAL_TRANSFER',
        'WAREHOUSE_IN_RACK_REBALANCEING_REVERSE_MATERIAL_TRANSFER',
        'WAREHOUSE_OUT_RACK_REBALANCING_MATERIAL_TRANSFER',
        'WAREHOUSE_OUT_RACK_REBALANCEING_REVERSE_MATERIAL_TRANSFER',
        'WAREHOUSE_OUT_RACK_LOAD_MATERIAL_TRANSFER',
        'WAREHOUSE_OUT_RACK_UNLOAD_MATERIAL_TRANSFER']

    for type_name in transfer_types:
        material_transfer_id = create_warehouse_material_transfer_type(type_name)
        commission_warehouse_material_transfer_type(material_transfer_id)

    return True

