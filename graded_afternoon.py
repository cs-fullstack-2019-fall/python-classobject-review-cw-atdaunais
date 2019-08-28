def main():
    # created new objects in my class then printed the overwritten string value
    newMovie1 = Movie("The Polar Express", "G", "2004")
    newMovie2 = Movie("The Lego Movie", "PG", "2014")
    print(newMovie1)
    print(newMovie2)

    newProduct1 = Product(50, 75, "Bananas")
    newProduct2 = Product(5, 150, "Reese's")
    print(newProduct1)
    print(newProduct2)


# movie class with 3 attributes
class Movie:
    def __init__(self, movieName, rating, yearReleased):
        self.movieName = movieName
        self.rating = rating
        self.yearReleased = yearReleased

    def __str__(self): # overwrites the default string method
        full_object_props = f"Properties of Movie:\n" \
                            f"movieName = {self.movieName}\n" \
                            f"rating = {self.rating}\n" \
                            f"yearReleased = {self.yearReleased}\n"
        return full_object_props


class Product:
    def __init__(self, price, quantity, name):
        self.price = price
        self.quantity = quantity
        self.name = name

    def __str__(self): # overwrites default string method with my own coded message
        object_str = f"Properties of Product:\n" \
                     f"price = ${self.price}\n" \
                     f"quantity = {self.quantity}\n" \
                     f"name = {self.name}\n"
        return object_str


main()
