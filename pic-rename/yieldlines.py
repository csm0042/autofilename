__author__ = 'chris.maue'


def picklines(file, lines):
    return [x for i, x in enumerate(file) if i in lines]


def yieldlines(file, lines):
    return (x for i, x in enumerate(file) if i in lines)
