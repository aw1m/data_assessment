
def remove_missing(string:str):
    if string is None:
        return string
    string = string.strip()
    if string =="" or string=="none":
        string =None
    return string

def clean_element(element:dict):
    for key, value in element.items():
        element[key] = remove_missing(value)
    return element
