
# Split command, excellent for parsing csv
"some,csv,values".split(",") == ["some", "csv", "values"]

# Format Funciton
you="JD"
me="JB"
"I am {0} You are {1}".format(me, you)
## Can also do this:
f"I am {me} and You are {you}" 

# IF
if var=2:
    print("Value is 2")
else:
    print("not 2")

# Truthy and Falsy

var="some value"
if var:
    Print("Number is defied and truthy")

# Tricky IF statements, called Ternary
x =3
y=2
"greater" if x > y else "less than" 

# Lists basically an array.
var_name = [ ]
cars = ["ford", "jeep", "chevy" ]

cars[1] == "jeep"

# Check for value
"jeep" in cars == True

## Check lenght
len(cars) == 3

## Delete, this would shift anything to the left after chevy.  If there was anythign there
del cars[2]

## Display tricks
### Skips first value
cars [1:] == ["ford"]
### Ignore first and last
cars [1:-1] == ["jeep"]

# Printing Elements

cars = ["ford", "jeep", "chevy" ]
print (cars[1])
