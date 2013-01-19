====================
Django Dynamic Settings
====================

Installation
============

1. Add ``dynsettings`` to your ``INSTALLED_APPS``::

       INSTALLED_APPS = (
           ...
           'dynsettings',
       )
       
2. Run syncdb to create dynsettings table.

Usage
=============

1. Import config object to manipulate your settings:
    from dynsettings.models import config

2. Use dynamic settings like a dictionary:
    import datetime
    
    config['my_data_name'] = u'Today is'
    config['my_data_name2'] = datetime.datetime.now()
    
    print config['my_data_name'], config['my_data_name2'].strftime("%d/%m/%Y")
