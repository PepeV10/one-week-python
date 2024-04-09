
#  ----------
#    PART 1
#  ----------
word = "supercalifragilisticexpialidocious"

# Write a for loop that prints out each character in the above "word" variable
for char in word:
    print(char)

print(("*") * 50)
# Write a while loop that does the same thing!
index = 0
while index < len(word):
    print(word[index])
    index += 1

print(("*") * 50)
#  ----------
#    PART 2
#  ----------
# Write a while loop that prints the even numbers from 100 to 140 (including 140)
even = 100
while even <= 140:
    print(even)
    even += 2



# Write a for loop that does the same thing (with range())
for even in range(100, 142, 2):
    print(even)

#  ----------
#    PART 3
#  ----------
# Write a loop that asks a user to input the passphrase "sillygoose" and keeps asking them to do so until they comply:
passphrase = "sillygoose"
user_input = input("Please enter the correct passphrase: ").lower()

while user_input != passphrase:
    print("Your passphrase is incorrect, please enter the correct passphrase: ")
    user_input = input("Try again: ").lower()

