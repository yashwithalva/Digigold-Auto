from helpers.helpers import randomword
from constants import warehouse_load_config

create_addr_req = {
    'address1': warehouse_load_config.NAMING_PREFIX + ' ADDR ' + randomword(10),
    'city': 'Bangalore',
    'state': 'Karnataka',
    'pinCode': '574239',
    'country': 'India'
}

create_company_req = {
    'name': warehouse_load_config.NAMING_PREFIX,
    'email': f'{randomword(5)}@devtest.in',
    'phoneNumber': '+918971201447',
    'addressId': 'id',
    'gstDetails': {
        'gstNumber': 'GST - 123',
        'tanNumber': 'TAN - 123',
        'panNumber': 'PAN - 123',
        'cinNumber': 'CIN - 123'
    },
    'bankDetails': {
        'bankAccountNumber': '12345678910',
        'bankIfscCode': 'UBIN0654321',
        'accountName': 'generated'
    }
}

create_warehouse_req = {
    'name': warehouse_load_config.NAMING_PREFIX,
    'addressId': 'ADD-01HM1XS1Z0W5KQ190PCMFB2BEA',
    'companyId': 'COM-01HPHAVCWDMMM49A9E3C8SXEST',
    'type': 'TRANSIT',
    'parentWarehouseId': '',
    'isParentWarehouse': False,
    'capacity': warehouse_load_config.WAREHOUSE_CAPACITY
}

create_po_req = {
    'description': warehouse_load_config.NAMING_PREFIX,
    'companyId': '',
    'targetWarehouseId': '',
    'supplierId': warehouse_load_config.MATERIAL_SUPPLIER,
    'type': 'COMPANY',
    'purchaseOrderItems': [
        {
            'materialCode': warehouse_load_config.MATERIAL_CODE,
            'quantity': warehouse_load_config.MATERIAL_LOAD_QUANTITY,
            'rate': warehouse_load_config.MATERIAL_LOAD_PRICE
        }
    ],
    'orderNo': '123',
    'orderDate': '2023-12-08',
    'isDeliveredBySupplier': True,
    'deliveryOrderNo': '',
    'deliveryOrderDate': '',
    'deliveryBy': ''
}

create_pi_req = {
    'description': warehouse_load_config.NAMING_PREFIX,
    'purchaseOrderId': '',
    'paymentType': 'ADVANCE',
    'txnReferenceNumber': '123',
    'paymentMadeAt': '2023-12-11',
    'purchaseInvoiceItems': [
        {
            'materialCode': warehouse_load_config.MATERIAL_CODE,
            'quantity': warehouse_load_config.MATERIAL_LOAD_QUANTITY,
            'rate': warehouse_load_config.MATERIAL_LOAD_PRICE
        }
    ],
    'deliveryOrderNo': '123',
    'deliveryOrderDate': '2023-12-11'
}

create_gr_req = {
    'purchaseInvoiceId': '',
    'purchaseOrderId': '',
    'deliveryDate': '2023-12-24',
    'deliveryType': 'SELF',
    'deliveryPartnerId': warehouse_load_config.MATERIAL_VENDOR,
    'deliveryBy': 'Myself'
}

parent_to_child_mt_req = {
    'description': warehouse_load_config.NAMING_PREFIX,
    'isApprovalRequired': False,
    'type': 'WAREHOUSE_PARENT_TO_CHILD_TRANSFER',
    'companyId': '',
    'materialTransferItems': [
        {
            'materialCode': warehouse_load_config.MATERIAL_CODE,
            'quantity': warehouse_load_config.MATERIAL_LOAD_QUANTITY
        }
    ],
    'sourceWarehouseId': '',
    'targetWarehouseId': '',
    'sourceRackId': '',
    'targetRackId': ''
}

create_racks_req = {
    'description': warehouse_load_config.NAMING_PREFIX,
    'warehouseId': '',
    'count': warehouse_load_config.NUMBER_OF_RACKS,
    'type': '',
    'capacity': warehouse_load_config.RACK_CAPACITY,
    'materialCode': warehouse_load_config.MATERIAL_CODE
}
