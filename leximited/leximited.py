def to_leximited_int(number):
    """ Return the given number in leximited format with type int """
    num = int(number)
    if(num > 99999999):
        length = str(len(str(num)))
        lex_long_length = f'9{len(length)}'
        return int(f'{lex_long_length}{len(str(num))}{num}')
    return int(f'{len(str(num))}{num}')


def to_leximited_str(number):
    """ Return the given number in leximited format with type str """
    num = str(number).lstrip('0')
    if(num.isdigit()):
        if(int(num) > 99999999):
            length = str(len(str(num)))
            lex_long_length = f'9{len(length)}'
            return str(f'{lex_long_length}{len(str(num))}{num}')
    return f'{len(str(num))}{num}'


def to_leximited_arbitrary_str(in_string):
    length = len(in_string)
    if(length > 8):
        lex_long_length = f'9{len(str(length))}'
        return str(f'{lex_long_length}{str(length)}{in_string}')
    else:
        return str(f'{str(length)}{in_string}')


def list_as_leximited(in_list, convert_text=True):
    """ Return the given list where numbers, and optionally text, (str or int) are
    converted to their leximited forms"""
    out_list = []
    for item in in_list:
        if(type(item) is int):
            out_list.append(to_leximited_int(item))
        elif(type(item) is str and item.isdigit()):
            out_list.append(str(to_leximited_str(item)))
        elif(convert_text):
            out_list.append(to_leximited_arbitrary_str(item)) 
        else:
            out_list.append(item)
    return out_list


def list_as_leximited_int(in_list):
    """ Return the given list converted to a list of leximited int"""
    out_list = []
    for item in in_list:
        out_list.append(to_leximited_int(item))
    return out_list


def list_as_leximited_str(in_list):
    """ Return the given list converted to a list of leximited str"""
    out_list = []
    for item in in_list:
        out_list.append(to_leximited_str(item))
    return out_list


def tuple_as_leximited(in_tuple, convert_text=True):
    """ Return the given tuple where numbers (str or int) are
    converted to their leximited forms, and everything else 
    left the same"""
    out_tuple = ()
    for item in in_tuple:
        if(type(item) is int):
            out_tuple += (to_leximited_int(item), )
        elif(type(item) is str and item.isdigit()):
            out_tuple += (to_leximited_str(item), )
        elif(convert_text):
            out_tuple += (to_leximited_arbitrary_str(item), ) 
        else:
            out_tuple += (item, )
    return out_tuple


def tuple_as_leximited_int(in_tuple):
    """ Return the given tuple converted to a tuple of leximited int"""
    out_tuple = ()
    for item in in_tuple:
        out_tuple += (to_leximited_int(item), )
    return out_tuple


def tuple_as_leximited_str(in_tuple):
    """ Return the given tuple converted to a tuple of leximited str"""
    out_tuple = ()
    for item in in_tuple:
        out_tuple += (to_leximited_str(item), )
    return out_tuple


def to_leximited(number):
    if(type(number) is int):
        return to_leximited_int(number)
    elif(type(number) is str and number.isdigit()):
        return str(to_leximited_str(number))
    elif(type(number) is str):
        return to_leximited_arbitrary_str(number)   
    else:
        return "Error: what is this?"



