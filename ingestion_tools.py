import json
def remove_missing(string:str):
    if string is None or type(string)!=str:
        return string
    string = string.strip()
    if string =="" or string=="none":
        string =None
    return string

def clean_element(element:dict):
    for key, value in element.items():
        element[key] = remove_missing(value)
    return element


def write_not_proccessed(filename:str, not_processed_list:list):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(not_processed_list, f, ensure_ascii=False, indent=4)
        print("Errors Written to {}".format(filename))
    return
