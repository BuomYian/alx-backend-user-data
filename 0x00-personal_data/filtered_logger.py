#!/usr/bin/env python3
"""
filtered_logger module
"""

import re

def filter_datum(fields, redaction, message, separator):
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
    return re.sub(r'({sep}|^)({fields})=[^;]*'.format(sep=f'(?:{re.escape(separator)}|$)', fields='|'.join(map(re.escape, fields))), f'\\1{fields}={redaction}', message)
