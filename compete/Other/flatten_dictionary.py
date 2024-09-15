input={
    "key1": "value1",
    "key2": "value2",
    "key3": {
        "key1": "value1",
        "key2": "value2",
        "key3": {
            "key1": "value1",
            "key2": "value2"
        }
    }
}

def flatten_dict(inpt:dict)->dict:
    '''flattening dictionary'''
    res = {}
    for k, v in inpt.items():
        if isinstance(v, dict):
            #recursion
            p = flatten_dict(v)
            #append keys
            for ik, iv in p.items():
                res[f"{k}.{ik}"] = iv
        else:
            res[k] = v
    return res


print(flatten_dict(input))

# output:
# {
#     "key1": "value1",
#     "key2": "value2",
#     "key3.key1": "value1",
#     "key3.key2": "value2",
#     "key3.key3.key1": "value1",
#     "key3.key3.key2": "value2",
# }