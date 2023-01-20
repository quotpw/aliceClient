import os
import uuid

import pymorphy2


def get_names(words: list) -> list:
    names = set()
    for word in words:
        names.add(word)
        morph = pymorphy2.MorphAnalyzer()
        p = morph.parse(word)[0]
        for tag in p.lexeme:
            names.add(tag.word)
    return list(names)


def get_uid_of_device() -> str:
    path = os.path.dirname(os.path.realpath(__file__)) + "/uid.txt"
    if os.path.exists(path):
        with open(path, "r") as f:
            return f.read()
    else:
        uid = str(uuid.uuid4())
        with open(path, "w") as f:
            f.write(uid)
        return uid
