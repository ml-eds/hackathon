import json

def dtob(d):
    b = json.dumps(d)
    d = "b'" + b
    return d.encode()