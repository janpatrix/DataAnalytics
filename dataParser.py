from datetime import datetime as dT

def parse_to_int(s):
    if s == '':
        return None
    else:
        return int(s)

def parse_to_date(s):
    if s == '':
        return None
    else:
        return (dT.strptime(s, '%Y-%m-%d'))

def parse_to_bool(s):
    if s == '':
        return None
    if s == "True":
        return True
    else:
        return False