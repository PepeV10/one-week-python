"""
Python Code Challenges: Functions
Python Code Challenges involving functions.

This article will help you review Python functions by providing some code challenges.

Some of these challenges are difficult! Take some time to think about them before starting to code.

You might not get the solution correct on your first try — look at your output, try to find where you’re going wrong, and iterate on your solution.

Finally, if you get stuck, use our solution code! If you “Check Answer” twice with an incorrect solution, you should see an option to get our solution code. However, truly investigate that solution — experiment and play with the solution code until you have a good grasp of how it is working. Good luck!

Function Syntax
As a refresher, function syntax looks like this:

def some_function(some_input1, some_input2):
  # … do something with the inputs …
  return output

For example, a function that returns the sum of the first and last elements of a given list might look like this:

def first_plus_last(lst):
  return lst[0] + lst[-1]

And this would produce output like:

# >>> first_plus_last([1, 2, 3, 4])
5
# >>> first_plus_last([8, 2, 5, -8])
0
# >>> first_plus_last([-10, 2, 3, -4])
-14

Challenges
We’ve included 5 challenges below. Try to answer all of them and polish up your problem-solving skills and your function expertise.
"""





"""
1. Tenth Power
Let’s create some functions which can help us solve math problems! For this first function, we are going to take the tenth power of a number. In order to do this we need to do three things:

Set up the function header for tenth_power which accepts one parameter
Take the tenth power of the input value
Return the result
Coding question
Questions
Write a function named tenth_power() that has one parameter named num.

The function should return num raised to the 10th power.
"""
# Write your tenth_power function here:
def tenth_power(number):
    return number ** 10


# Uncomment these function calls to test your tenth_power function:
#print(tenth_power(1))
# 1 to the 10th power is 1
#print(tenth_power(0))
# 0 to the 10th power is 0
#print(tenth_power(2))
# 2 to the 10th power is 1024

"""
Let’s go over this solution:

def tenth_power(num):
  return num ** 10

This is one way to solve this problem using two lines of code.

The first line is the function header which uses def to define the function followed by the function name. Within the parentheses we include num which is our formal parameter. Because of this, num is the variable name for the value we pass into this function.

On our next line, we use return to show that this function is going to return a value when it is called. Next to the return keyword, we define what value is going to be returned. Since we need the tenth power of our input value, we can use the power operator in python which is **. Using this knowledge, in order to get the tenth power of our input value, we use num ** 10.
"""





"""
2. Square Root
Another useful function for solving math problems is the square root function. We can create this using similar steps from the last problem. The code will look very similar. We need to:

Set up the function header for square_root which accepts one parameter
Take the square root of the input value
Return the result
Coding question
Questions
Write a function named square_root() that has one parameter named num.

Use exponents (**) to return the square root of num.
"""
# Write your square_root function here:
def square_root(num):
    return num ** 0.5

# Uncomment these function calls to test your square_root function:
#print(square_root(16))
# should print 4
#print(square_root(100))
# should print 10

"""
Let’s go over one possible solution:

def square_root(num):
  return num ** 0.5

As you can see, this solution is very similar to the last problem. In this case, the only changes we need are the function name and changing the power value to 0.5. We define the function called square_root with one parameter. We then take the one half power of the input value which is mathematically the same as taking the square root and return it.
"""

"""
3. Win Percentage
Next, we will create a function which calculates the percentage of games won. In order to do this, we will need to know how many total games there were and divide the number of wins by the total number of games. For this function, there will be two input parameters, the number of wins and the number of losses. We also need to make sure that we return the result as a percentage (in the range of 0 to 100). In order to create this method we need the following steps:

Define the function header with two parameters, wins and losses
Calculate the total number of games using the number of wins and losses
Get the ratio of winning using the number of wins out of the total number of games.
Convert the ratio to a percentage
Return the percentage
Coding question
Questions
Create a function called win_percentage() that takes two parameters named wins and losses.

This function should return out the total percentage of games won by a team based on these two numbers.
"""

# Write your win_percentage function here:
def win_percentage(wins, losses):
    # Calculate the total number of games
    total_games = wins + losses
    # Avoid division by zero error
    if total_games == 0:
        return 0
    # Calculate the percentage of wins
    percentage_wins = (wins / total_games) * 100
    return percentage_wins

# Uncomment these function calls to test your win_percentage function:
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100

"""
Let’s go over how we completed this function:

def win_percentage(wins, losses):
  total_games = wins + losses
  ratio_won = wins / total_games
  return ratio_won * 100

First, we defined our function with two parameters, one for games won and one for games lost. Next, we calculated the total number of games using the number of wins + losses. After that, we use calculate the ratio of wins out of the total number of games by dividing wins by our total_games variable. Since this gives us a ratio and we want it in percentage form, we multiply the answer by 100 and return it.
"""