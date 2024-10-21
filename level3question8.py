def parse_string(encoded_string):
    parts = encoded_string.split('0')
    parts = [part for part in parts if part]
    return {
        "first_name": parts[0],
        "last_name": parts[1],
        "id": parts[2]
    }

encoded_string = "Robert000Smith000123"
result = parse_string(encoded_string)
print(result)
