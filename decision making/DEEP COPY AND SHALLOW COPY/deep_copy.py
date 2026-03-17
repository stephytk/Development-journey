"""

Example for shallow copy
"""

from copy import deepcopy

aruns_fav_foods = [
    {"meal_type":"breakfast","meal":"dosa"},
    {"meal_type":"lunch","meal":"fish"},
    {"meal_type":"dinner","meal":"fried rice"}

]

har_favt_foods=deepcopy(aruns_fav_foods)

har_favt_foods[0]["meal"]="idly"

print("arun",aruns_fav_foods)

print("hari",har_favt_foods)



