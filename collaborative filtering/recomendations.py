from datamap import critics
from evcliddistance import evclid_distance
from korelationofpirson import sim_pearson

def topMatches(critics,person,n=5,similarity=evclid_distance):
    scores=[(similarity(critics,person,other),other) for other in critics if other!=person]
    scores.sort()
    scores.reverse()
    return scores[0:n]

# Получить рекомендации для заданного человека, пользуясь взвешенным средним
# оценок, данных всеми остальными пользователями
def getRecommendations(prefs,person,similarity=sim_pearson):
    totals={}
    simSums={}
    for other in prefs:
    # сравнивать меня с собой же не нужно
        if other==person: continue
        sim=similarity(prefs,person,other)
  # игнорировать нулевые и отрицательные оценки
        if sim<=0: continue
        for item in prefs[other]:
    # оценивать только фильмы, которые я еще не смотрел
            if item not in prefs[person] or prefs[person][item]==0:
    # Коэффициент подобия * Оценка
                totals.setdefault(item,0)
                totals[item]+=prefs[other][item]*sim
      # Сумма коэффициентов подобия
                simSums.setdefault(item,0)
                simSums[item]+=sim
  # Создать нормализованный список
    rankings=[(total/simSums[item],item) for item,total in totals.items( )]
  # Вернуть отсортированный список
    rankings.sort( )
    rankings.reverse( )
    return rankings
print(getRecommendations(critics,"Lisa Rose"))
