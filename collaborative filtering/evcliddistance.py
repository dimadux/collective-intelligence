from datamap import critics

def evclid_distance(critics,person_one,person_two):
    common_recomendations = {}
    for item in critics[person_one]:
        if item in critics[person_two]:
            common_recomendations[item]=(critics[person_one][item],critics[person_two][item])
    if len(common_recomendations) == 0: return 0
    else:
        sum_of_squares = sum([pow(item[0]-item[1],2) for item in common_recomendations.values()])
    return 1/(1+sum_of_squares)
