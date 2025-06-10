from __future__ import annotations

import warnings
from typing import List


class EasyError(Exception):
    """Wrapper class for an Exception Error."""

    def __init__(self, msg: str = "") -> None:
        super().__init__(msg)


def easyexception(origin: str, code: str, severity: str, msg: str) -> None:
    """
    Raise some kind of customized error/warning/message.
    :param origin: str, the caller file name
    :param code: str, the section (func, class, etc) where easyexception is
    called
    :param severity: str, options are "Error", "Warning", "Message"
    :param msg: str, the message to be printed
    :return: NA.
    """
    if severity.lower() == "error":
        message = "---Error: From " + origin + ": code " + code + "\n" + \
                  "Message: " + msg + "---\n"
        raise EasyError(message)
    elif severity.lower() == "warning":
        message = "---Warning: From " + origin + ": code " + code + "\n" + \
                  "Message: " + msg + "---\n"
        warnings.warn(message)
    elif severity.lower() == "message":
        message = "---Info: From " + origin + ": code " + code + "\n" + \
                  "Message: " + msg + "---\n"
        print(message)
    else:
        pass


__all__: List[str] = ["EasyError", "easyexception"]
