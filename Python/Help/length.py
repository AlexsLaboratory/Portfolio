Day = "1222 Days"
# Sides = "-" * 9
Middle = "|" + " " + Day + " " + "|"

# len == 7

if len(Day) == 5:
	Sides = "-" * 9
elif len(Day) == 6:
	Sides = "-" * 10
elif len(Day) == 7:
	Sides = "-" * 11
elif len(Day) == 8:
	Sides = "-" * 12
elif len(Day) == 9:
	Sides = "-" * 13

print(Sides)
print(Middle)
print(Sides)