#!/usr/bin/env python3
"""
filtered_logger module
"""

import csv
import logging
import re
from typing import List
from datetime import datetime


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscates the log message by replacing specified fields
    with the redaction string.

    Args:
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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize RedactingFormatter.

        Args:
            fields (List[str]): List of strings representing the fields to obfuscate.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log message with sensitive values obfuscated.

        Args:
            record (logging.LogRecord): The log record to be formatted.

        Returns:
            str: The formatted log message with obfuscated values.
        """
        log_message = super().format(record)
        return filter_datum(self.fields, self.REDACTION, log_message, self.SEPARATOR)


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def get_logger() -> logging.Logger:
    """
    Returns a logging.Logger object named "user_data" that logs up to logging.INFO level.
    The logger does not propagate messages to other loggers.
    It has a StreamHandler with RedactingFormatter as formatter.

    Returns:
        logging.Logger: The "user_data" logger.
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
