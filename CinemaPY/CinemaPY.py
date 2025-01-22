# Activity 2

# Introduction
# Your friend Ana enjoys a lot going to the cinema.
# She wants to keep a tracking list of the movies
# watched during the year and store her personal movie rating.

# This rating will be a number of stars, but she does
# not want to write them down one by one.

# Instead, she asked you to write a simple program to write
# down as many stars as the value of a given number between 0 and 100.

# In the case of rating a very bad movie with 0 stars,
# she asked you to display a single character dash.

# Input
# An integer number between 0 and 100.

# Output
# Print out the number of stars corresponding to the given number greater than zero.
# In the case of reading a zero then the output will be a single dash.

# Example 1

# Input
# 5

# Output
# *****

# Example 2

# Input
# 0

# Output
# -

rating = int(input("Movie rating: "))
if rating == 0:
    print("-")
else:
    for x in range(rating):
        print("*", end="")
    print("")