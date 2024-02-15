# Function to convert a name into initials
def abbrev_name(name):
    # Split the string name into a list containing two words
    parts = name.split()

    # Get the first character of each item and convert to uppercase
    initials = [p[0].upper() for p in parts]

    # Join the initials as a string with a period and return
    return '.'.join(initials)
print(abbrev_name("Alex Higson"))