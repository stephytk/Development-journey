movies = [
    [1, "K.G.F: Chapter 1", "Yash", "Kannada", 8.2, 1234567],
    [2, "K.G.F: Chapter 2", "Yash", "Kannada", 8.3, 678900],
    [3, "K.G.F: Chapter 3", "Yash", "Kannada", 9.5, 456789], # Anticipated
    [4, "Salaar: Part 1 – Ceasefire", "Prabhas", "Telugu", 6.5, 45678567],
    [5, "Pushpa 2: The Rule", "Allu Arjun", "Telugu", 10.0, 1234567], # Hype Rating
    [6, "Aavesham", "Fahadh Faasil", "Malayalam", 7.9, 1234567]
]

# display all movie title

movie_title={di[1] for di in movies}
print(movie_title)

# movie with top rating

top_ranking=max([di[4] for di in movies])
print(f"Top ranking {top_ranking}")




# display kannada movies

kannada_movies=[m[1] for m in movies if m[3]=="Kannada"]
print(kannada_movies)

# display movies whre actor is yash

actor_yash=[a[1] for a in movies if a[2]=="Yash" ]
print(actor_yash)

# which language most number of movies

most_movie_number=max([lst[-3] for lst in movies])

most_movie_number=[lst[3] for lst in movies if lst[3]==most_movie_number]
print(most_movie_number)

# # movie with max budget

# mx_budget=max([di[5]for di in movies]
# print(mx_budget)
# # languages

