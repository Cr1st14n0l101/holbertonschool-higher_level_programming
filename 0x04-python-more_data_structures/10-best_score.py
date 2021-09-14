#!/usr/bin/python3
def best_score(a_dictionary):
    score, student = 0, ""
    if not a_dictionary:
        return None
    for i in sorted(a_dictionary):
        if a_dictionary[i] >= score:
            score = a_dictionary[i]
            student = i
    return student
