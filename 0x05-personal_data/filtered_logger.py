#!/usr/bin/env python3
"""
filtered_logger
"""

from typing import List
import re
import logging
import mysql.connector
import os

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """init"""
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """
        filter values in incoming log records using filter_datum
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """
    returns the log message obfuscated
    """
    for field in fields:
        message = re.sub(rf"{field}=.*?{separator}",
                         f"{field}={redaction}{separator}", message)
    return message


def get_logger() -> logging.Logger:
    """
    returns a logging.Logger object.
    """
    log = logging.getLogger("user_data")
    log.setLevel(logging.INFO)
    log.propagate = False
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(RedactingFormatter(PII_FIELDS))
    log.addHandler(streamHandler)
    return log


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    returns a connector to the database
    """
    user = os.environ.get('PERSONAL_DATA_DB_USERNAME', None)
    password = os.environ.get('PERSONAL_DATA_DB_PASSWORD', None)
    host = os.environ.get('PERSONAL_DATA_DB_HOST', None)
    database = os.environ.get('PERSONAL_DATA_DB_NAME', None)

    return mysql.connector.connect(user=user,
                                   password=password,
                                   host=host,
                                   database=database)
