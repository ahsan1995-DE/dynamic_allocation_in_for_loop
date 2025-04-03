# -*- coding: utf-8 -*-
"""
Author: Ahsn Ayaz
Date: 14 MArch 2025

This is a template script file for dynamic accessing and updating
vairables, arrays and dictionaries using two approaches of Globals()
Dictionaries.
"""
#####################################################################
########################## USING GLOBALS() ##########################
#####################################################################

################## For integer variables ##################

# x_1 = 0
# x_2 = 0
# x_3 = 0

# def increment_variables():
#     global x_1, x_2, x_3

#     # Loop through index 1 to 3
#     for i in range(1, 4):        
#         globals()[f"x_{i}"]+=1
        

#     return x_1, x_2, x_3  # Return the updated values

# # Call the function and print results
# a, b, c = increment_variables()
# print(a,b,c)

################## For dictionaries ##################

# x_1 = {}
# x_2 = {}
# x_3 = {}

# def increment_variables():
#     global x_1, x_2, x_3

#     # Loop through index 1 to 3
#     for i in range(1, 4):        
#         globals()[f"x_{i}"][i]=i
        

#     return x_1, x_2, x_3  # Return the updated values

# # Call the function and print results
# a, b, c = increment_variables()
# print(a,b,c)

################## For Arrays ##################

# x_1 = []
# x_2 = []
# x_3 = []

# def increment_variables():
#     global x_1, x_2, x_3

#     # Loop through index 1 to 3
#     for i in range(1, 4):        
#         globals()[f"x_{i}"].append(i)
        

#     return x_1, x_2, x_3  # Return the updated values

# # Call the function and print results
# a, b, c = increment_variables()
# print(a,b,c)

########################################################################
########################## USING DICTIONARIES ##########################
########################################################################

################## Master dictionary ##################

# def update_dictionaries():
#     # Define multiple dictionaries
#     dict_1 = {}
#     dict_2 = {}
#     dict_3 = {}

#     # Store them in a master dictionary
#     master_dict = {1: dict_1, 2: dict_2, 3: dict_3}

#     # Loop through index 1 to 3
#     for i in range(1, 4):
#         master_dict[i][f"key_{i}"] = f"value_{i}"  # Add key-value pair dynamically

#     return dict_1, dict_2, dict_3  # Returning updated dictionaries

# # Call the function and print results
# dict_1, dict_2, dict_3 = update_dictionaries()
# print(dict_1, dict_2, dict_3)

################## Dictionary of arrays ##################

# def update_arrays():
#     # Define multiple dictionaries
#     array_1 = []
#     array_2 = []
#     array_3 = []

#     # Store them in a master dictionary
#     master_dict = {1: array_1, 2: array_2, 3: array_3}

#     # Loop through index 1 to 3
#     for i in range(1, 4):
#         master_dict[i].append(i) # Appending dynamically dynamically

#     return array_1, array_2, array_3  # Returning updated arrays

# # Call the function and print results
# array_1, array_2, array_3 = update_arrays()
# print(array_1, array_2, array_3)

################## Dictionary of variables ##################

# def increment_variables():
#     # Define variables using a dictionary
#     variables = {"x_1": 0, "x_2": 0, "x_3": 0}

#     # Loop through index 1 to 3
#     for i in range(1, 4):
#         key = f"x_{i}"  # Construct the variable name dynamically
#         variables[key] += 1  # Increment its value

#     return variables  # Return the updated values

# # Call the function and print results
# result = increment_variables()
# print(result)
