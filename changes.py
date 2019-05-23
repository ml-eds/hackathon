def change_value(dicti, key, value):
    if key in dicti:
            dicti[key] = value
    print("changes", dicti)
    return dicti