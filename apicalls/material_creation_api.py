import json
import requests

from constants.api_constants import *
from models import material_setup_dto


####################################################
# BASIC API CALLS
# API calls for individual api
####################################################

def create_material_type() -> str:
    json_body = json.dumps(material_setup_dto.create_material_type)
    res = requests.post(HOST + CREATE_MATERIAL_TYPE_URL, data=json_body, headers=HEADER_INFO)
    print(res.json())
    material_id = res.json()['data']['id']
    print(f"Created Material Type: {material_id}")
    return material_id


def commission_material_type(material_type_id) -> bool:
    req_param = get_request_param(material_type_id)
    res = requests.post(HOST + COMMISSION_MATERIAL_TYPE_URL, headers=HEADER_INFO, params=req_param, data=json.dumps({}))
    print(res.json())
    return res.json()['success']


def create_supplier(addr_id, name='Supplier') -> str:
    material_setup_dto.create_supplier['name'] += name
    material_setup_dto.create_supplier['addressId'] = addr_id
    json_body = json.dumps(material_setup_dto.create_supplier)
    res = requests.post(HOST + CREATE_SUPPLIER_URL, data=json_body, headers=HEADER_INFO)
    print(res.json())
    supplier_id = res.json()['data']['id']
    print(f"Created Supplier: {supplier_id}")
    return supplier_id


def commission_supplier(supplier_id) -> bool:
    res = requests.post(HOST + COMMISSION_SUPPLIER_URL, headers=HEADER_INFO, params=get_request_param(supplier_id),
                        data=json.dumps({}))
    print(res.json())
    return res.json()['success']


def create_material(supplier_id) -> str:
    print("Supplier Id: ", supplier_id)
    material_setup_dto.create_material['supplierIds'] = [supplier_id]
    print(material_setup_dto.create_material)
    print("")
    json_body = json.dumps(material_setup_dto.create_material)
    res = requests.post(HOST + CREATE_MATERIAL_URL, data=json_body, headers=HEADER_INFO)
    print(res.json())
    material_id = res.json()['data']['id']
    print(f"Created Material: {material_id}")
    return material_id


def commission_material(material_id) -> bool:
    res = requests.get(HOST + COMMISSION_MATERIAL_URL, headers=HEADER_INFO, params=get_request_param(material_id),
                        data=json.dumps({}))
    print(res.json())
    return res.json()['success']


def create_tax_template(name='tax template', tax1=0, tax2=0) -> str:
    material_setup_dto.create_tax_template['name'] = name
    material_setup_dto.create_tax_template['taxTemplateItems'][0]['value'] = tax1
    material_setup_dto.create_tax_template['taxTemplateItems'][1]['value'] = tax2
    json_body = json.dumps(material_setup_dto.create_tax_template)
    res = requests.post(HOST + CREATE_TAX_TEMPLATE_URL, data=json_body, headers=HEADER_INFO)
    print(res.json())
    tax_template_id = res.json()['data']['id']
    print(f"Created Tax Template with id: {tax_template_id}")
    return tax_template_id


def commission_tax_template(tax_template_id) -> bool:
    res = requests.post(HOST + COMMISSION_TAX_TEMPLATE_URL, headers=HEADER_INFO,
                        params=get_request_param(tax_template_id), data=json.dumps({}))
    print(res.json())
    return res.json()['success']


def create_tax_template_mapping(tax_template_id, material_code, tax_type, trade_type) -> str:
    tax_template_dict = material_setup_dto.create_tax_template_mapping

    tax_template_dict['taxTemplateId'] = tax_template_id
    tax_template_dict['materialCode'] = material_code
    tax_template_dict['type'] = tax_type
    if tax_type == 'BUY':
        tax_template_dict.pop('saleType')
        tax_template_dict['purchaseType'] = trade_type
    else:
        tax_template_dict.pop('purchaseType')
        tax_template_dict['saleType'] = trade_type

    json_body = json.dumps(tax_template_dict)
    res = requests.post(HOST + CREATE_TAX_TEMPLATE_MAPPING_URL, data=json_body, headers=HEADER_INFO)
    print(res.json())
    print("Created Tax Template Mapping id: ", res.json()['data']['id'])
    return res.json()['data']['id']


def commission_tax_template_mapping(tax_template_mapping_id) -> bool:
    res = requests.post(HOST + COMMISSION_TAX_TEMPLATE_MAPPING_URL, headers=HEADER_INFO,
                        params=get_request_param(tax_template_mapping_id), data=json.dumps({}))
    print(res.json())
    return res.json()['success']


def get_request_param(req_param_id) -> dict:
    req_param = {
        "id": req_param_id
    }
    return req_param


####################################################
# COMPOSITE API CALLS
# API calls for multiple api
####################################################

def create_and_commission_material_type() -> str:
    material_type_id = create_material_type()
    commission_material_type(material_type_id)
    return material_type_id


def create_and_commission_supplier(supplier_name, addr_id) -> str:
    supplier_id = create_supplier(addr_id, supplier_name)
    commission_supplier(supplier_id)
    return supplier_id


def create_and_commission_material(supplier_id) -> str:
    material_id = create_material(supplier_id)
    commission_material(material_id)
    return material_id


def create_and_commission_tax_template(tax_template_name, tax1, tax2) -> str:
    tax_template_id = create_tax_template(tax_template_name, tax1, tax2)
    commission_tax_template(tax_template_id)
    return tax_template_id


def create_and_commission_tax_template_mapping(tax_template_id, material_code, tax_type, trade_type) -> str:
    tax_template_mapping_id = create_tax_template_mapping(tax_template_id, material_code, tax_type, trade_type)
    commission_tax_template_mapping(tax_template_mapping_id)
    return tax_template_mapping_id
