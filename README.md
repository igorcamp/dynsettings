====================
Django Dynamic Settings
====================

Installation
============

1. Add ``dynsettings`` to your ``INSTALLED_APPS``:
<pre>
       INSTALLED_APPS = (
           ...
           'dynsettings',
       )
</pre>
       
2. Run syncdb to create dynsettings table.

Usage
=============

1. Import dynsettings object to manipulate your settings:
	<pre>
	from dynsettings.models import dynsettings
	</pre>

2. Define your initial settings values in your settings.py (optional):
	<pre>
	DYNSETTINGS = {
		'my_initial_data': 12345
	}
	</pre>

3. Use dynamic settings like a dictionary:
	<pre>
    import datetime
    
    dynsettings['my_data_name'] = u'Today is'
    dynsettings['my_data_name2'] = datetime.datetime.now()
    
    print dynsettings['my_data_name'], dynsettings['my_data_name2'].strftime("%d/%m/%Y")
    print dynsettings['my_initial_data']
    
    dynsettings['my_initial_data'] = "abcd"
    
    print dynsettings['my_initial_data']
	</pre>
    
	The code above will print the following output: <br />
\>\>\> Today is 18/01/2013 <br />
\>\>\> 12345<br />
\>\>\> abcd