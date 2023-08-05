#!/usr/bin/env python3
"""
filtered_logger module
"""

import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscates the log message by replacing specified fields with the redaction string.

    Arguments:
    fields: List of strings representing all fields to obfuscate.
    redaction: String representing by what the field will be obfuscated.
    message: String representing the log line.
    separator: String representing by which character is separating all fields in the log line (message).

    Returns:
    String: Obfuscated log message.
    """
    sep_pattern = f'(?:{re.escape(separator)}|$)'
    fields_pattern = '|'.join(map(re.escape, fields))
    pattern = r'({fields})=[^;]*'.format(fields=fields_pattern)
    return re.sub(pattern, f'\\1={redaction}', message)
