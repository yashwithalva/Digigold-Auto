from constants import material_setup_config

create_material_type = {
    "name": material_setup_config.METAL_NAME,
    "metalType": "GOLD",
    "purity": material_setup_config.METAL_PURITY,
    "materialCarate": material_setup_config.METAL_CARATE
}

create_supplier = {
    "name": material_setup_config.NAMING_PREFIX,
    "email": "auto@supplier.in",
    "phoneNumber": "+919039546421",
    "addressId": "",
    "gstDetails": {
        "gstNumber": "GST-123",
        "tanNumber": "TAN-123",
        "cinNumber": "CIN-123",
        "panNumber": "PAN-123"
    },
    "bankDetails": {
        "bankAccountNumber": "9988770987654",
        "bankIfscCode": "UBIN0987654",
        "accountName": "Supplier Account Name"
    }
}

create_material = {
    "code": material_setup_config.MATERIAL_CODE,
    "name": "Gold 24 Carat",
    "materialType": material_setup_config.METAL_NAME,
    "uom": "MICRO_GRAM",
    "hsnCode": "HSN1",
    "supplierIds": [""]
}

create_tax_template = {
    "name": "",
    "description": "Gold 24 Tax Template",
    "taxTemplateItems": [
        {
            "name": "CGST Tax",
            "description": "1.5% Tax",
            "value": 1.5,
            "valueType": "PERCENTAGE"
        },
        {
            "name": "SGST Tax",
            "description": "1.5% Tax",
            "value": 1.5,
            "valueType": "PERCENTAGE"
        }
    ]
}

create_tax_template_mapping = {
    "taxTemplateId": "",
    "materialCode": "",
    "type": "",
    "purchaseType": "",
    "saleType": ""
}
