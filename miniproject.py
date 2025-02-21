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
    """
    matrix = np.zeros((len(t) + 1, len(s)+1))

    for fil in range(1, len(t)+1):
        for col in range(1, len(s)+1):
            if t[fil - 1] != s[col - 1]:
                if matrix[fil-1,col] > matrix[fil,col - 1]:
                    matrix[fil, col] = matrix[fil-1,col]
                else:
                    matrix[fil, col] = matrix[fil,col-1]
            else:
                matrix[fil,col]=matrix[fil-1, col-1] + 1
    return matrix


def lcs(s, t):
    """
    """
    matrix = lcs_matrix(s, t)
    fil = len(t)
    col = len(s)
    lcstring = ""
    while col >= 0 and fil >= 0:
        if matrix[fil,col] == matrix[fil-1, col]:
            fil -= 1
        elif matrix[fil,col] == matrix[fil, col-1]:
            col -= 1
        else:
            lcstring += s[col-1]
            fil -= 1
            col -= 1
    return lcstring[::-1]


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
    """
    pass

for k in range(1, 11):
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
def greedy_value(l_weights, l_values, max_weight):
    """
    """
    pass

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
def optimal_value(l_weights, l_values, max_weight):
    """
    """
    pass

l_weights = [4, 4, 5]
l_values  = [10, 11, 15]
max_weight = 8

print(optimal_value(l_weights, l_values, max_weight))


