#Safe lookup, else return "-"
def safe_lookup(i):
    try:
        return i.ip, i.port
    except:
        return '-','-'