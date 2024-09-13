# Function with more than one input

def greet_with(name, location):
    print(f"Hello {name}, Good morning from {location}")
    print(f"Hi {name}, Good afternoon from {location}")
    print(f"Hey {name}, Good evening from {location}")
    
    
# Positional Arguments
greet_with("John", "Accra")

# Keyword Arguments
greet_with(name = "John", location = "Accra")