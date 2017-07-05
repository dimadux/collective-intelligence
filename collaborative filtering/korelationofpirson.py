from math import sqrt
def sim_pearson(prefs,p1,p2):
  # Получить список предметов, оцененных обоими
  si={}
  for item in prefs[p1]:
    if item in prefs[p2]: si[item]=1
  n=len(si)
  # Если нет ни одной общей оценки, вернуть 0
  if n==0: return 0
  # Вычислить сумму всех предпочтений
  sum1=sum([prefs[p1][it] for it in si])
  sum2=sum([prefs[p2][it] for it in si])
  # Вычислить сумму квадратов
  sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
  sum2Sq=sum([pow(prefs[p2][it],2) for it in si])
  # Вычислить сумму произведений
  pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])
  # Вычислить коэффициент Пирсона
  num=pSum-(sum1*sum2/n)
  den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
  if den==0: return 0
  r=num/den
  return r
