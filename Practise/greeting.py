# Creating personalized messages using f string and by accessing the names by index and formating using title()
names = ['john', 'albert', 'michael', 'sarah', 'hannah', 'tania']
print(f"Good Morning {names[0].title()}, how was your night?")
print(f"Good Afternon {names[4].title()}, how is your day going so far?")
print(f"Good Evening {names[-1].title()}, I hope you had a lovely day and wishing you a very good night.")
