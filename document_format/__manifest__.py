{
    "name": "Document Format",
    "summary": """Formato Factura agrupada""",
    "version": "16.1.0.0",
    "description": """Formato de Factura agrupada""",
    "author": "Dario Cruz Mauro, Daniel Dominguez, Manuel Calero Solis",
    "company": "Xtendoo",
    "website": "http://xtendoo.es",
    "category": "Extra Tools",
    "license": "AGPL-3",
    "depends": [
        "sale",
        "account_invoice_report_grouped_by_picking",
        "stock",
        "stock_picking_report_valued",
        "product",
        "account",
        "account_invoice_report_due_list",
        "account_payment_partner",
        "mail",
        "contacts",
    ],
    "data": [
        "views/invoice/invoice_gruped_by_picking.xml",
        "views/invoice/account_tax_template.xml",
    ],
    "installable": True,
    "auto_install": False,
}
