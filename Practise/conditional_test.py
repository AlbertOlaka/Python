# Checking for equality.
books = 'White Nights'
books == 'White Nights'

# Checking for inequality.
pizza_topping = 'chillies'
if pizza_topping != 'mushrooms':
    print("Hold the mushrooms!")

# Checking using the lower() method
car = 'Audi'
# car.lower = 'audi'

# Numerical Test involing equality, inequality, greater than, less than, greater than and less than.
age = 25
age < 21
age > 21
age <= 21
age >= 21
age == 25
if age != 26:
    print("That's not the correct age. Please try again")

# Test using the and & or keyword.
age_0 = 21
age_1 = 25
age_0 >= 19 and age_1 >= 18
# True
age_1 = 18
age_0 >=19 and age_1 >= 22
#False

age_0 = 20
age_1 = 25
age_0 >= 19 or age_1 >= 26
#True
age_0 = 18
age_0 >= 19 or age_1 >= 26
#False

# Checking whether an item is in a list.
books = ['white nights', 'animal farm', 'east of eden', 'crime and punishment']
'the trial' in books
#False
'white nights' in books
#True

# Checking whether an item is not in a list.
read_books = ['white nights', 'animal farm', 'east of eden', 'crime and punishment']
book = 'the trial'
if books not in read_books:
    print(f"Buy and read {book.title()}")