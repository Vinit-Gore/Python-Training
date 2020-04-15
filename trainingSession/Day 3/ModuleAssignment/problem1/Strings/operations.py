def Concat(string1, string2):
    return string1 + string2


def Substring(child_string, parent_string):
    if child_string in parent_string:
        return True
    else:
        return False


def Trim(trimstring):
    return trimstring.strip()


def Length(string):
    return len(string)


def Pallindrome(string):
    if string[::-1] == string:
        return True
    else:
        return False


def Uppercase(string):
    return string.upper()


def Lowercase(string):
    return string.lower()


def Capitalize(string):
    return string.capitalize()
