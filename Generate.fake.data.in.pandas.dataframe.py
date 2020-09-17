from faker import Faker
fake = Faker()
import random
import pandas as pd

# make dataframe using lists
# Make list of names, email, time (min) spent in meeting, random number
name_array = [fake.name() for _ in range(30)]
email_array = [fake.email() for _ in range(30)]
time_mtg_array = [random.randrange(0, 60) for _ in range(30)]
# comb = zip (name_array, email_array, time_mtg_array)
df =pd.DataFrame(list(zip(name_array, email_array, time_mtg_array)), columns=['Name', 'Email', 'Duration'])

# Make dataframe using method format
dfalt= pd.DataFrame({
    'Name': (fake.name() for _ in range(30)),
    'Email': (fake.email() for _ in range(30)),
    'Duration': (random.randrange(0,60) for _ in range(30))
})
print (dfalt)