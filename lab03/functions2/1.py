movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#Task 1
def imdbTest(*dict) :
    for i in range(0, len(movies)) :
        x = movies[i]["imdb"]
        if(x > 5.5) :
            print(movies[i]["name"] + " - True")  
        else :
            print(movies[i]["name"] + " - False")

imdbTest(movies)

print("\n")

#Task 2
def niceFilm(*dict) :
    for i in range(0, len(movies)) :
        x = movies[i]["imdb"]
        if(x > 5.5) :
            print(movies[i]["name"])  

niceFilm(movies)

print("\n") 

#Task 3
myStr = input("Enter the category :\n")

def category(*dict) :
    for i in range(0, len(movies)) :
        x = movies[i]["category"] 
        if(x == myStr) :
            print(movies[i]["name"])

category(movies)

print("\n") 

#Task 4
def avrgIMDB(*dict) :
    sum = 0
    for i in range(0, len(movies)) :
        sum += movies[i]["imdb"]
    print(sum / len(movies))

avrgIMDB(movies)

print("\n") 

#Task 5
def avrgCategoryIMDB(*dict) :
    sum = 0
    count = 0
    for i in range(0, len(movies)) :
        x = movies[i]["category"] 
        if(x == myStr) :
            count += 1
            sum += movies[i]["imdb"]
    print(sum / count)

avrgCategoryIMDB(movies)
