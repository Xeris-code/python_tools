from pathlib import Path

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

def validate_paths(*paths, collector: Collector):

    for p in paths:
        if not p.exists(): collector.add(Note("error", f"{p} does not exist"))

    