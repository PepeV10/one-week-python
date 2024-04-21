"""

Challenges
We’ve included 5 challenges below. Try to answer all of them and polish up your problem-solving skills and your loop expertise.

1. Larger Sum
We are going to start our advanced challenge problems by calculating which list of two inputs has the larger sum. We will iterate through each of the list and calculate the sums, afterwards we will compare the two and return which one has a greater sum. Here are the steps we need:

Define the function to accept two input parameters: lst1 and lst2
Create two variables to record the two sums
Loop through the first list and add up all of the numbers
Loop through the second list and add up all of the numbers
Compare the first and second sum and return the list with the greater sum
Coding question
Questions
Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.

The function should return the list whose elements sum to the greater number. If the sum of the elements of each list are equal, return lst1.

"""
def larger_sum(lst1, lst2):
    sum1 = 0
    sum2 = 0

    for number in lst1:
        sum1 += number
    for number in lst2:
        sum2 += number

    if sum1 >= sum2:
        return lst1
    else:
        return lst2
    
"""
#CodeCademy's Solution
Here’s one way to do it:

def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for number in lst1:
    sum1 += number
  for number in lst2:
    sum2 += number
  if sum1 >= sum2:
    return lst1
  else: 
    return lst2
"""





"""
2. Over 9000
We are constructing a device that is able to measure the power level of our coding abilities and according to the device, it will be impossible for our power levels to be over 9000. Because of this, as we iterate through a list of power values we will count up each of the numbers until our sum reaches a value greater than 9000. Once this happens, we should stop adding the numbers and return the value where we stopped. In order to do this, we will need the following steps:

Define the function to accept a list of numbers
Create a variable to keep track of our sum
Iterate through every element in our list of numbers
Within the loop, add the current number we are looking at to our sum
Still within the loop, check if the sum is greater than 9000. If it is, end the loop
Return the value of the sum when we ended our loop
Coding question
Questions
Create a function named over_nine_thousand() that takes a list of numbers named lst as a parameter.

The function should sum the elements of the list until the sum is greater than 9000. When this happens, the function should return the sum. If the sum of all of the elements is never greater than 9000, the function should return total sum of all the elements. If the list is empty, the function should return 0.

For example, if lst was [8000, 900, 120, 5000], then the function should return 9020.
"""
#Write your function here
def over_nine_thousand(lst):
    sum = 0
    for number in lst:
        sum += number
        if sum > 9000:
            break
    return sum

#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))

"""
#CodeCademy's Solution
Here is this solution:

def over_nine_thousand(lst):
  sum = 0
  for number in lst:
    sum += number
    if (sum > 9000):
      break
  return sum

Our solution follows a similar pattern to some of the other code challenges, except that we have a condition where we end early. In the case where we reach a sum greater than 9000, we can use the break keyword to exit our loop. This will continue to execute the code outside of our loop, which in this case, returns the sum that we found.
"""


"""
3. Max Num
Here is a more traditional coding problem for you. This function will be used to find the maximum number in a list of numbers. This can be accomplished using the max() function in python, but as a challenge, we are going to manually implement this function. Here is what we need to do:

Define the function to accept a list of numbers called nums
Set our default maximum value to be the first element in the list
Loop through every number in the list of numbers
Within the loop, if we find a number greater than our starting maximum, then replace the maximum with what we found.
Return the maximum number
Coding question
Questions
Create a function named max_num() that takes a list of numbers named nums as a parameter.

The function should return the largest number in nums
"""

#Write your function here
def max_num(nums):
    maximum_number = nums[0]
    for num in nums:
        if num > maximum_number:
            maximum_number = num
    return maximum_number

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))

"""
Here is one way to solve this:

def max_num(nums):
  maximum = nums[0]
  for number in nums:
    if number > maximum:
      maximum = number
  return maximum

There are a few different ways to accomplish this task, but the way we did it was to check every element in the list and see if there is one bigger than what we currently think is the biggest. If there is a bigger one, then replace it. We keep replacing the number until the largest number has been found.
"""

"""
4. Same Values
In this challenge, we need to find the indices in two equally sized lists where the numbers match. We will be iterating through both of them at the same time and comparing the values, if the numbers are equal, then we record the index. These are the steps we need to accomplish this:

Define our function to accept two lists of numbers
Create a new list to store our matching indices
Loop through each index to the end of either of our lists
Within the loop, check if our first list at the current index is equal to the second list at the current index. If so, append the index where they matched
Return our list of indices
Coding question
Questions
Write a function named same_values() that takes two lists of numbers of equal size as parameters.

The function should return a list of the indices where the values were equal in lst1 and lst2.

For example, the following code should return [0, 2, 3]

same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5])
"""
#Write your function here
def same_values(lst1, lst2):
    matching_indices = []
    for match in range(len(lst1)):
        if lst1[match] == lst2[match]:
            matching_indices.append(match)
    return matching_indices
        
#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

"""
Here’s how we did it:

def same_values(lst1, lst2):
  new_lst = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      new_lst.append(index)
  return new_lst

In this solution, we used a loop that iterates using the range of the len of our list. This generates the indices we need to iterate through. Note that we assume the lists are of equal size. We then access the element at the current index from each list using lst1[index] and lst2[index]. If they are equal we add the index to the new list. Finally, we return the results.
"""

