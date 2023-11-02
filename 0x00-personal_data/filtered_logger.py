#!/usr/bin/env python3
""" log message obfustication in 5 lines"""
import re  # regex
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """ obfuscated logs """
    for field in fields:
        message = re.sub(field + "=.*?" + separator,
                         field + "=" + redaction + separator, message)
    return message
