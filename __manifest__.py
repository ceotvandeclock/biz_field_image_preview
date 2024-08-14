{
    'name': 'Bizapps - Widget image preview',
    'summary': """Adds functional preview (open/popup) image in original size 
    Enlarge image Enlarge images product images preview product images picture
    foto product photo product preview enlarge """,
    'description': """
This is extension for <field widget="image"> widget image
==============================================
* STOCK and CONTACT example:
    * open image on click in original size in popup
    * close on close button
    * close on click on/out image

""",
    "author": "support@bizapps.vn",
    "maintainer": "support@bizapps.vn",
    "contributors": ["support@bizapps.vn"],
    "website": "https://bizapps.vn/ung-dung",
    'company': 'Bizapps',
    'support': 'support@bizapps.vn',

    'category': "Tools",
    'version': '16.1.0.3',
    'depends': ['web', 'mail'],
    'license': 'OPL-1',
    'assets': {
        'web.assets_backend': [
            'biz_field_image_preview/static/**/*',
        ],
        'web.assets_qweb': [
            'biz_field_image_preview/static/src/xml/image.xml',
        ],
    },
    "images": ["static/description/background.png", ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
