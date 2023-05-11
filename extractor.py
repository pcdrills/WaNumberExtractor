import pandas as pd
from NumberValidator import Validator
from Saver import Saver
from Cleaner import Cleaner

INPUT_FILE = "Twhats.txt"

# Read the content of the file
with open(INPUT_FILE) as file:
    contents = pd.read_csv(file)


# Create a dataframe for the contents and extract just the column of phone numbers
# Separate and extract phone numbers form the text
dframe = pd.DataFrame(contents)
just_phone_numbers = dframe["username"]


# Cleanup the Encoding from the numbers
# Get hold of just the phone numbers and save them to a list
cleaning = Cleaner()
cleaned_numbers = cleaning.clean(just_phone_numbers)


# Create a validator object
# Call the validator class to validate the phone numbers
val = Validator()
validated_numbers = val.validate(cleaned_numbers)


#Write output to a text file
output = Saver()
output.save(validated_numbers)