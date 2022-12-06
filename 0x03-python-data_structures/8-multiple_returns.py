#!/usr/bin/python3
def multiple_returns(sentence):
    sl = len(sentence)
    fchar = sentence[0] if sl > 0 else "None"
    form = sl, fchar
    return(form)
