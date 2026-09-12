''' 2. Write a program that reads input data from the console - a password (one line of random text)
and checks if the input matches the phrase "s3cr3t!P@ssw0rd". If it matches, print "Welcome",
otherwise print "Wrong password!".'''

password = input("Enter your password: ")

if password == "s3cr3t!P@ssw0rd":
    print("Welcome")
else:
    print("Wrong password!")