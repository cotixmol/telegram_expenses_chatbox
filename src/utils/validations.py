import re


def validate_json_structure(open_ai_answer):
    """This function checks for two different types of JSON structures:
    1. A structure with {'description': key, 'amount': key, 'category':key}.
    2. A structure {'error': key}"""
    pattern = (
        r'\{"description":\s*".*?",\s*"amount":\s*\d+,\s*"category":\s*".*?"\}'
        r'|'
        r'\{\s*"error"\s*:\s*".*?"\s*\}'
    )
    return bool(re.match(pattern, open_ai_answer))
