import datetime

x=datetime.datetime.now()
curr_year=x.year
print("welcome to the Interactive personal data collector")

name=str(input("Enter your name: "))
age=int(input("Enter your age: "))
height=float(input("Enter your height in meters: "))
fav_no=int(input("Enter your favourite No: "))

print("\n\nThank you here is the information that we have collected\n")

print(f"Name: {name} (Type:{type(name)},Memory Address:{id(name)})")
print(f"Age: {age} (Type:{type(age)},Memory Address:{id(age)})")
print(f"Height: {height} (Type:{type(height)},Memory Address:{id(height)})")
print(f"Favoyrite no: {fav_no} (Type:{type(fav_no)},Memory Address:{id(fav_no)})")

print(f"\n\n your birth year is approximately {curr_year-age} according to your age")

print(f"\n\nThank you for using personal data collector")
