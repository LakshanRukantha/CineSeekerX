import requests

base_url = "https://yts.mx/ajax/search?query="

# headers = {
#     "cookie": "PHPSESSID=PUT_YOUR_PHPSESSID",
# }

def search():
    query = input("Enter a movie name: ")
    url = base_url + query
    response = requests.get(url)
    return response.json()

data = search()

if data["status"] == "ok":
    movie_list = data["data"]
    if movie_list:
        print("\nFound {} movies:".format(len(movie_list)))
        for movie in movie_list:
            print(f"\nTitle: {movie['title']}")
            print(f"Year: {movie['year']}")
            print(f"URL: {movie['url']}")
            print(f"Image: {movie['img']}")
    else:
        print("No movies found.")
else:
    print("Error: {}".format(data["status_message"]))
    