from pathlib import Path
from typing import Tuple

class Note():
    def __init__(self, type: str, message: str):
        self.type = type
        self.message = message

class Collector():
    def __init__(self):
        self.collection = {}

    def add(self, notice: Note):
        t = notice.type
        msg = notice.message
        if t in self.collection:
            self.collection[t].append(msg)
        else:
            self.collection[t] = [msg]

def validate_path(*paths) -> list:

    message_list = []

    for p in paths:
        if not p.exists():
            message_list.append(p)

    return message_list

    