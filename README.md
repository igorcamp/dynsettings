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

2. Define your initial settings values (optional):

	DYNSETTINGS = {
		'my_initial_data': 12345
	}

2. Use dynamic settings like a dictionary:
    from dynsettings.models import dynsettings
    import datetime
    
    dynsettings['my_data_name'] = u'Today is'
    dynsettings['my_data_name2'] = datetime.datetime.now()
    
    print dynsettings['my_data_name'], dynsettings['my_data_name2'].strftime("%d/%m/%Y")
    print dynsettings['my_initial_data']
    
    dynsettings['my_initial_data'] = "abcd"
    
    print dynsettings['my_initial_data']
    
The code above will print the following output:
    >>> Today is 18/01/2013
    >>> 12345
    >>> abcd
