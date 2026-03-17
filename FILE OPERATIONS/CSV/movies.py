#Write a Python program to read the file move.csv and print the first 5 rows.

from csv import DictReader

fr=open("FILE OPERATIONS\\CSV\\movies.csv")

data=list(DictReader(fr))

print(data[:5])

#Write a program to count how many movie records are present in move.csv (excluding the header).


print(len(data))

#Write a program to read the header row from move.csv and print all column names.

col_names=[col for col in data[0]]

print(col_names)

#Accept a year from the user and display all movie titles released in that year from move.csv.

year_wise_summary={}

for d in data:

    year=d.get("Year of Release")

    all_movie_title=d.get("Name")

    if year in year_wise_summary:

        year_wise_summary[year]+=all_movie_title
    else:
        year_wise_summary[year]=all_movie_title

print(year_wise_summary)


#5. Read move.csv and print the movie with the highest rating.
highest_rating={}


for d in data:

    rating=float(d.get("Rating"))

    movie_name=d.get("Name")

    if rating in highest_rating:

        highest_rating[rating]+=movie_name

    else:

        highest_rating[rating]=movie_name

print(max(highest_rating))

#6. Accept a genre from the user (e.g., Action, Drama, Romance) and print all matching movies from move.csv.

# genre=input("enter the genre")

# all_match_movies=[d.get("Name")for d in data if Action in g.get("Movie Categories") ]

# print(all_match_movies)


#7. Create a new CSV file named top_rated.csv and write all movies from move.csv with a rating greater than 8.0.

fw=open("FILE OPERATIONS\\CSV\\top_rated.csv","w")

for d in data:

    fw.write( d.get("Rating") )

    print("completed")


#Read move.csv, calculate how many movies are in each genre (Movie Categories), and write the output into genre_count.txt

movie_count={}


for d in data:

    mov_name = (d.get("Name"))

    movie_genre=d.get("Movie Categories")

    if movie_genre in movie_count:

        movie_count[movie_genre]+=mov_name

    else:
        movie_count[movie_genre]=mov_name


print(movie_count)

#Read all movies from move.csv and write them into sorted_movies.csv sorted in descending order of rating.


movie_lst=[[v,k] for k,v in movie_count.items()]

print(sorted(movie_lst,reverse=True))














    







 








   
