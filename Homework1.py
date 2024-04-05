
#example
class Book:
    def __init__(self, title, author, publisher, city, year):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.city = city
        self.year = year
        self.total_inventory = 0

    def write_bib_entry(self):
        return f"{self.author} ({self.year}). {self.title}. {self.city}: {self.publisher}."

    def title_year(self):
        return f"{self.title} ({self.year})"

    def set_total_inventory(self, total):
        self.total_inventory = total

    def get_total_inventory(self):
        return self.total_inventory

    def sold_one(self):
        if self.total_inventory > 0:
            self.total_inventory -= 1
        else:
            print("There are no items left to sell.")


class Article:
    def __init__(self, title, author, journal, year):
        self.title = title
        self.author = author
        self.journal = journal
        self.year = year
        self.total_inventory = 0

    def write_bib_entry(self):
        return f"{self.author} ({self.year}). \"{self.title}.\" {self.journal}."

    def title_year(self):
        return f"{self.title} ({self.year})"

    def set_total_inventory(self, total):
        self.total_inventory = total

    def get_total_inventory(self):
        return self.total_inventory

    def sold_one(self):
        if self.total_inventory > 0:
            self.total_inventory -= 1
        else:
            print("There are no items left to sell.")


# Create instances of Book and Article
book1 = Book("The Catcher in the Rye", "J.D. Salinger", "Little, Brown and Company", "New York", 1951)
book1.set_total_inventory(5)

article1 = Article("Artificial Intelligence: A Modern Approach", "Stuart Russell, Peter Norvig", "Journal of Artificial Intelligence Research", 1995)
article1.set_total_inventory(10)

# Add instances to the titles list
titles = [book1, article1]

# Loop through the list and print title, year, and total inventory
for item in titles:
    print(f"{item.title_year()}: {item.get_total_inventory()}")

# Calculate total number of items
total_items = sum(item.get_total_inventory() for item in titles)
print("Total number of items:", total_items)

# Sell two items for each title and print remaining inventory
for item in titles:
    item.sold_one()
    item.sold_one()
    print(f"{item.title_year()}: {item.get_total_inventory()}")

# Scatter plot of height vs. weight
import matplotlib.pyplot as plt

heights = [160, 170, 180, 165, 175]  # heights in cm
weights = [60, 70, 80, 55, 75]        # weights in kg

plt.scatter(weights, heights, marker='o', s=100)
plt.xlabel('Weight (kg)')
plt.ylabel('Height (cm)')
plt.title('Height vs. Weight')
plt.grid(True)
plt.show()
