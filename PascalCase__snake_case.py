def to_snake_case(string):
    string = str(string)
    res = []
    res.append(string[0].lower())
    for ind, val in enumerate(string):
        if ind > 0:
            if val.isupper():
                res.append('_')
            res.append(val.lower())
    return ''.join(res)