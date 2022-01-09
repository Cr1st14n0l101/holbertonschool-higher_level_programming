#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers"""
    if type(list_of_integers) != list or len(list_of_integers) == 0:
        return None

    if len(list_of_integers) > 1:
        if list_of_integers[0] >= list_of_integers[1]:
            return list_of_integers[0]
        if list_of_integers[-1] >= list_of_integers[-2]:
            return list_of_integers[-1]
        return deep_peak(list_of_integers, 0, len(list_of_integers))
    if not list_of_integers:
        return None
    return list_of_integers[0]


def deep_peak(lint, start, stop):
    """Finds a peak recursively"""
    if stop - start < 2:
        return None
    mid = (start + stop) // 2
    if lint[mid] >= lint[mid - 1] and lint[mid] >= lint[mid + 1]:
        return lint[mid]
    return deep_peak(lint, start, mid) or deep_peak(lint, mid, stop)
