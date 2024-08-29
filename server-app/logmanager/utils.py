
def parse_projection(input_str):
    input_str = input_str.strip().strip('{}')
    pairs = input_str.split(',')
    
    projection_dict = {}
    
    for pair in pairs:
        key_value = pair.strip().split(':')
        
        if len(key_value) == 2:
            key = key_value[0].strip().strip("'").strip('"')
            value = key_value[1].strip().strip("'").strip('"').lower()
            
            if value == 'true':
                projection_dict[key] = True
            elif value == 'false':
                projection_dict[key] = False
            else:
                projection_dict[key] = int(value) if value.isdigit() else value
    
    return projection_dict

import json
import re

def parse_find_query(input_str):
    # Remove curly braces if present
    input_str = input_str.strip().strip('{}')
    
    # Split the string into key-value pairs
    pairs = input_str.split(',')
    
    # Create a dictionary
    query_dict = {}
    
    for pair in pairs:
        key_value = pair.strip().split(':')
        
        if len(key_value) == 2:
            key = key_value[0].strip().strip("'").strip('"').strip('$')
            value = key_value[1].strip().strip("'").strip('"')
            
            # Handle special operators
            if '$' in key:
                operator = '$' + key.split('$')[1]
                key = key.split('$')[0]
                query_dict[key] = {operator: parse_value(value)}
            else:
                query_dict[key] = parse_value(value)
    
    return query_dict

def parse_value(value):
    # Try to convert to int or float
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            pass
    
    # Handle regex patterns
    if value.startswith('/') and value.endswith('/'):
        return re.compile(value.strip('/'))
    
    # Handle boolean values
    if value.lower() == 'true':
        return True
    elif value.lower() == 'false':
        return False
    
    # Default to string
    return value
