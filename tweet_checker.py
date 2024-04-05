tweet = input("Please enter your Tweet: \n").lower()
tweet_length = len(tweet)
accepted_length = 140

if tweet_length <= accepted_length:
    print(f"That {tweet_length} char tweet will work!")
else:
    above_length = tweet_length - accepted_length
    print(f"Your tweet is {above_length} chars too long!")

"""
max_chars = 140
print("*" * 30)
tweet = input("Enter your potential Tweet: ")
char_count = len(tweet)

if char_count < max_chars:
    print(f"That {char_count} character tweet will work!")
else:
    print(f"That {char_count} character tweet is {char_count - max_chars} characters too long!")
"""
