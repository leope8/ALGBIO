# %% [markdown]
# # Miniproject
# 
# You have to turn in
# 
# * a file 
# 
#   >`mp_apellidos.ipynb` 
#   
#   where `apellidos` are the last names of the members of each team. Just fill in the cell codes below with your functions and run the lines that currently start with comments. Make sure it works fine by executing Kernel/Restart & Run All.
#   
#   **Don't forget to write function docstrings and an adequate control of function parameters.** 
#     
#     
# * a file 
#   
#   >`mp_apellidos.html` 
#   
#   with an `html` rendering of the previous `.ipynb` file (for instance, if working with Jupyter notebooks, just apply `File / Download as HTML` after a correct run of `Kernel/Restart & Run All`).
# 
# **Submitting your work**
# 
# 1. Create a folder named `apellidos` and place there the previous `.ipynb`and `.html` files.
# 2. Compress **the folder** with 7zip, WinZip or a similar tool to create a `apellidos.zip` compressed file.
# 3. Upload this zipped file using the moodle link.
# 
# **Very important!!!**
# 
# *Make sure you follow the file naming conventions above*. If not, you may be asked to resubmit your work.

# %%


# %% [markdown]
# ## Question 1: Finding the Longest Common Subsequence
# 
# We have not paid too much attention to it, but we have in the slides the basis of a dynamic programming algorithm to find the length of **longest common subsequence** between two strings, i.e. the longest, perhaps non consecutive, string that appears in both.  
# 
# Notice that **we do not impose** the constraint of the **characters in the sequence be consecutive**; with that requirement the problem is called the **common substring problem**.
# 
# Write first a Python function `lcs_matrix(s, t)` that receives two strings `s, t` and returns the dynamic programming matrix used to compute the length of their longest common subsequence.
# 
# Then write a Python function `lcs(s, t)` that returns a string with a longest common subsequence, using the LCS matrix returned by the previous function.

# %%
import numpy as np

def lcs_matrix(s, t):
    """
    Compute the dynamic programming matrix for the longest common subsequence (LCS) of two strings.

    Parameters:
    s (str): The first string.
    t (str): The second string.

    Returns:
    numpy.ndarray: A matrix where the entry at (i, j) contains the length of the LCS of s[:j] and t[:i].
    """
    matrix = np.zeros((len(t) + 1, len(s)+1))

    for fil in range(1, len(t)+1):
        for col in range(1, len(s)+1):
            if t[fil - 1] != s[col - 1]: # if the characters are different, the value is the maximum of the previous values
                if matrix[fil-1,col] > matrix[fil,col - 1]: # the previous row is greater than the previous column
                    matrix[fil, col] = matrix[fil-1,col] # so we take the previous row
                else:
                    matrix[fil, col] = matrix[fil,col-1] # otherwise we take the previous column
            else: # if the characters are the same, we add 1 to the diagonal
                matrix[fil,col]=matrix[fil-1, col-1] + 1 
    return matrix


def lcs(s, t):
    """
    Find a longest common subsequence (LCS) of two strings using the dynamic programming matrix.

    Parameters:
    s (str): The first string.
    t (str): The second string.

    Returns:
    str: A longest common subsequence of s and t.
    """
    matrix = lcs_matrix(s, t) # we compute the matrix
    fil = len(t)
    col = len(s)
    lcstring = ""
    while col >= 0 and fil >= 0: # we iterate until we reach the first row or column
        if matrix[fil,col] == matrix[fil-1, col]: # if the value is the same as the previous row, we move up
            fil -= 1
        elif matrix[fil,col] == matrix[fil, col-1]: # if the value is the same as the previous column, we move left
            col -= 1
        else: # if the value is different, we add the character to the string and move diagonally
            lcstring += s[col-1]
            fil -= 1
            col -= 1
    return lcstring[::-1] # we return the string in reverse order


for s, t in zip(['bananas', 'biscuit', 'confidential'], ['bahamas', 'suitcase', 'trascendental']):
    lc_str = lcs(s, t)
    print(s, t, lc_str)

# %% [markdown]
# ## Question 2: The Pascal Triangle
# 
# Pascal's triangle is a triangular array of integers constructed with the following formula:
# 
# * The first row consists of the number 1.
# * For each subsequent row, each element is the sum of the numbers directly above it, on either side.
# 
# For example, here are the first few rows:  
# ```text 
#     1  
#    1 1  
#   1 2 1  
#  1 3 3 1  
# 1 4 6 4 1 
# ``` 
# 
# Write a Python function `pascal_row(k)` that returns the `k`-th row of Pascal's triangle. Assume the single `1` to be the 0-th row.  
# 
# *Hint: Make it a recursive function that computes first the previous row `k-1` and uses it to compute the current one.*

# %%
def pascal_row(k):
    """
    Generate the k-th row of Pascal's triangle.

    Parameters:
    k (int): The row index (0-based) of Pascal's triangle to generate.

    Returns:
    list: The k-th row of Pascal's triangle.
    """
    def nextRow(prev_row):
        """
        Generate the next row in Pascal's triangle given the previous row.

        Parameters:
        prev_row (list): The previous row of Pascal's triangle.

        Returns:
        list: The next row of Pascal's triangle.
        """
        next_row = [0]*(len(prev_row)+1) # the length of the next row is that of the prevoius row + 1
        for j in range(0,len(next_row)):
            if j == 0 or j == len(prev_row): # the first and last elements of the row are always 1
                next_row[j] = prev_row[0]
            else: 
                next_row[j] = prev_row[j-1] + prev_row[j] # the other elements are the sum of the two elements above them
        return next_row

    row = [1]

    for i in range(0,k): # generate the k-th row by iterating k times
        row = nextRow(row) 

    return row

for k in range(0, 11):
    tr = pascal_row(k)
    print(tr)

# %% [markdown]
# ## Question 3: The 0-1 Knapsack Problem
# 
# As a sideline to our studies we are considering entering the bank robbing business, for which we must be able to solve the following problem: if we have a knapsack which stands a total integer weight of $W$ and there are $n$ items in the bank's vault with integer values $v_i$ and weights $w_i$, how do we choose those that maximize our loot without breaking the knapsack? Recall that we are in a 0-1 situation: you either take the entire item or none at all.
# 
# A greedy strategy (natural under the circumstances!) is to order the items by descending relative values $\frac{v_i}{w_i}$ and add them to the knapsack until the allowed total weight $W$ is surpassed. Remember that you cannot take cannot take a fraction of an item.
# 
# Write a function `greedy_value(l_weights, l_values, max_weight)` that returns the value of the maximal loot made up of elements with weights in `l_weights` and values in `l_values` that can be carried away in a knapsack which can hold at most a weight `max_weight`. 

# %%
import numpy as np

def greedy_value(l_weights, l_values, max_weight):
    """
    Solves the 0-1 Knapsack problem with a greedy algorithm.

    Input:
    l_weights (list): List of weights of the items
    l_values (list):  List of values of the items
    max_weight (int): Maximum weight capacity of the knapsack

    Output: Int: Total value of the items in the knapsack

    The greedy algorithm could be described as follows:
    1. Sort the items by value/weight ratio
    2. If the item fits, add them to the knapsack
    3. If the item doesn't fit, return the total value of the items already in the knapsack
    """
 
    assert all(isinstance(i, int) for i in l_weights) and all(isinstance(i, int) for i in l_values) and isinstance(max_weight, int), "The weights, values and maximum weight must be integers"
    assert len(l_weights) == len(l_values), "The lists of weights and values must have the same length"

    knapsack = [0] * len(l_weights)                                                     #We will store the items in the knapsack in a binary list, 1 if in it, 0 if not
    weight, value = np.array(l_weights), np.array(l_values)                             #We convert the lists to numpy arrays to work with them
    sortval = sorted(list(enumerate(value/weight)), key=lambda x: x[1], reverse=True)   #We sort the items by value/weight ratio, using ennumerate to keep track of the original index
    
    for item in sortval:                    #We iterate over the items sorted by value/weight ratio

        if weight[item[0]] <= max_weight:   #If the item fits in the knapsack
            max_weight -= weight[item[0]]   #We substract the weight of the item from the maximum weight
            knapsack[item[0]] = 1           #We add the item to the knapsack

        else:                               #If the item doesn't fit in the knapsack
            return sum(value*knapsack)      #We return the total value of the items in the knapsack



l_weights = [4, 4, 5]
l_values  = [10, 11, 15]
max_weight = 8


print(greedy_value(l_weights, l_values, max_weight))
# %% [markdown]
# ## Question 4: Dynamic Programming to Solve the 0-1 Knapsack Problem
# 
# Looking at the output of your greedy function on the previous example, you should be aware that your greedy strategy won't always give an optimal loot.
# But don't worry, Dynamic Programming comes to the rescue!
# 
# Devise a dynamic programming strategy to maximize the loot and explain it in this markdown cell.
# 
# Then, write in the next cell a Python function `optimal_value(l_weights, l_values, max_weight)` that returns the value of the maximal loot made up of elements with weights in `l_weights` and values in `l_values` that can be carried away in a knapsack which can hold at most a weight `max_weight`. 

# %%
import numpy as np

def optimal_value(l_weights, l_values, max_weight):
    """
    Solves the Knapsack problem with using dinamic programming.

    Input:
    l_weights (list): List of weights of the items
    l_values (list): List of values of the items
    max_weight (int): Maximum weight capacity of the knapsack

    Output: Int: Total value of the items in the knapsack

    We use a modified version of the coin exchange algorithm.
    Instead of: n(i,c) = min( n(i-1, c), 1    + n(i,   c-vi))
        Select the minimum number of coins between
        the optimal number of coins without the coin we are adding
        and the optimal number of coins with the coin we are adding

    We use:     t(i,w) = max( t(i-1, w), vi + t(i-1, w-wi))
        Select the maximum value between
        the optimal value without the object we are adding
        and the optimal value with the object we are adding

    The main changes are that we don't minimize the number of coins, but maximize the value
    And that we don't use 1 + n(i, c-vi), but vi + t(i-1, w-wi)
    Instead of adding a coin (1) to the optimal number of coins with spare change to add our coin n(c-vi)
    we add the value of the object (vi) to the optimal value we had before adding the object and with space to add it t(i-1, w-wi)
    """
    
    assert all(isinstance(i, int) for i in l_weights) and all(isinstance(i, int) for i in l_values) and isinstance(max_weight, int), "The weights, values and maximum weight must be integers"
    assert len(l_weights) == len(l_values), "The lists of weights and values must have the same length"

    n = len(l_weights)
    
    table = np.array([[0] * (max_weight + 1)] * (n + 1)) #We create a table filled with 0, we'll consider the first row as "No item" and the first column as "No weight"

    for weight in range(1, max_weight + 1):              #We start iterating in weight=1 because the value of max_weight=0 is always 0
        for item in range (1, n + 1):                    #We start iterating in item=1 because the value of adding no item is always 0

            if l_weights[item - 1] <= weight:            #If the item fits in the space left in the knapsack
                table[item][weight] = max(l_values[item - 1] + table[item - 1][weight - l_weights[item - 1]] , table[item - 1][weight]) #We apply the algorithm described
                
            else:                                           #If the item doesn't fit
                table[item][weight] = table[item-1][weight] #We just copy the value of the previous item
                
    return table[n][max_weight]



l_weights = [4, 4, 5]
l_values  = [10, 11, 15]
max_weight = 8

print(optimal_value(l_weights, l_values, max_weight))

