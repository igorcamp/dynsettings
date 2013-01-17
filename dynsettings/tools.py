# -*- coding: utf-8 -*-
import datetime


def parse_value(value):
    if len(value) == 0 or value == 'None':
        return ('NoneType', 'None')

    elif len(value) > 2 and value[0] == 'u' and \
            ((value[1] == "'" and value[-1] == "'") or \
             (value[1] == '"' and value[-1] == '"')):
        return ('unicode', value[2:-1])

    elif len(value) > 1 and ((value[0] == '"' and value[-1] == '"') or \
                             (value[0] == "'" and value[-1] == "'")):
        return ('str', value[1:-1])

    elif len(value) > 8 and value[0:9] == 'datetime(' and value[-1] == ')':
        args = value[9:-1].split(',')
        i_args = []
        for arg in args:
            try:
                i_args.append(int(arg))
            except:
                # Invalid value
                return False
        try:
            d = datetime.datetime(*args)
            return ('datetime', d.strftime('%d/%m/%Y %H:%M:%S'))
        except:
            # Invalid value
            return False

    elif value == 'True' or value == 'False':
        return ('bool', value)

    try:
        v = float(value)
        return ('float', str(v))
    except:
        try:
            v = int(value)
            return ('int', str(v))
        except:
            # Invalid value
            return False
