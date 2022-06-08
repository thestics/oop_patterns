from enum import Enum, auto
from typing import Dict


class Event(Enum):
    LINE = auto()
    WORD = auto()
    WORD_IN_LINE = auto()


class EventListener:
    def update(self, data: str):
        pass


class MaxLineEventListener(EventListener):
    def __init__(self):
        self.val = ""

    def update(self, data: str):
        if len(data) > len(self.val):
            self.val = data


# effectively, the same logic, no
MaxWordEventListener = MaxLineEventListener

# Stub for empty event listener. Handy to use as a default
NULL_EVENT_LISTENER = EventListener()


class LineWithMaxWordEventListener(EventListener):
    def __init__(self):
        self.row = ""
        self.word = ""

    def update(self, data: str):
        words = data.split()
        if not words:
            return
        max_word = max(words, key=len)
        if len(max_word) > len(self.word):
            self.row = data
            self.word = max_word


class FileReader:
    def __init__(self, path):
        self.path = path
        self.listeners: Dict[Event, EventListener] = {}

    def subscribe(self, event_type: Event, listener: EventListener):
        self.listeners[event_type] = listener

    def unsubscribe(self, event_type: Event, listener: EventListener):
        self.listeners.pop(event_type)

    def publish(self, event_type: Event, data: str):
        self.listeners.get(event_type, NULL_EVENT_LISTENER).update(data)

    def read(self):
        with open(self.path) as f:
            lines = f.readlines()
            for line in lines:
                for word in line.split():
                    self.publish(Event.WORD, word)
                self.publish(Event.LINE, line)
                self.publish(Event.WORD_IN_LINE, line)


if __name__ == "__main__":
    reader = FileReader('src.txt')
    
    word_listener = MaxWordEventListener()
    line_listener = MaxLineEventListener()
    line_with_max_word_listener = LineWithMaxWordEventListener()
    
    reader.subscribe(Event.WORD, word_listener)
    reader.subscribe(Event.LINE, line_listener)
    reader.subscribe(Event.WORD_IN_LINE, line_with_max_word_listener)
    
    reader.read()
    
    print(f'Max word: {word_listener.val}')
    print(f'Max line: {line_listener.val}')
    print(f'Line with max word: {line_with_max_word_listener.row=} {line_with_max_word_listener.word=}')
