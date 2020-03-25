# Problem Set 1
# Name: Jordan Becker
# Time Spent: 0:30
# Last Modified: March 20, 2020

# Problem 1.a:

# Here are the variables:
P = float(input("Please input initial principal balance: "))
r = float(input("Please input interest rate: "))
n = int(input("How many times is the interest applied per time period ? "))
t = int(input("How many times has the period elapsed ? "))


def main():
	# This is the solution:
	A = int(P * ((1 + (r / n) ** (n *t)))
			# Testing by printing A
	    

	#Problem 1.b:

	weather = [70, 75, 80, 85, 90, 95, 100, 105, 110, 115]
	i = 0;
	if i < len(weather):
		c = ((weather[i])-32) * 5/9
		i += 1
		print(c)

if __name__ == "__main__":
	main()