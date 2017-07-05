import numpy as np
import math

def sim_euclid(one,two):
    summary = 0;
    for item_one,item_two in zip(one,two):
        try:
            1/(item_one*item_two)
        except:
            summary += math.pow(item_one-item_two,2)
    return math.pow(summary,0.5) 
