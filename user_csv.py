# user_csv.py
# ENDG 233 F24
# Fadi Salman
# L03 - 5
# A terminal-based data analysis and visualization program in Python.
# You must follow the specifications provided in the project description.
# Remember to include docstrings and comments throughout your code.
import numpy as np
import matplotlib as plt
import csv
import os

def check_file_exists(filename):
    '''Checks if a file exists'''
    return os.path.exists(filename)

def read_csv(filename, include_headers):
    ''' This function take a file name and reads the csv file and converts it to a 2D list

    Parameters:
        filename (str): a string that indicates the file name
        include_headers (bool): Tells the code whether to include headers or not in the 2D list

    Returns:
        full_list (2D list): contains all the contents of data file
    '''
    
    # declares all the nessesary variables
    full_list = []
    row = []

    # acts as a flag to indicate whether to skip the header
    skip = True

    if include_headers:
        skip = False
    
    if not check_file_exists(filename):
        print(f"Error: File '{filename}' not found!")
        return []

    # opening the file and indicating that the code should read it 
    f = open(filename, "r")
    

    # loops through everyline and ensures that the type of each data is correct
    for line in f:
        # if True then it skips the first line  
        if skip:
            skip = False
            
            
        else:
            row = line.replace("\n", "").split(",")
            
            for pos,val in enumerate(row):
                # removing the "." to check if the rest of the characters are digits
                remove_dot = val.replace(".", "") 

                if (remove_dot.isdigit()):              # if all digits then converts the data to float
                    row[pos] = float(row[pos])
            
            full_list += [row]
    
    return full_list


def write_csv(filename, data, overwrite):
    '''This function takes in data in a list and writes it as a csv file
    
    Parameters:
        filename (str): a string that indicates the file name
        data (lst): list containing all nessesary information
        overwrite (bool): Tells the code whether to overwrite or to append the data
    '''
    
    # setting a variable to indicate whether it will append or overwrite
    write_condition = "a"
    if overwrite:
        write_condition = "w"
    
    # opens the file or creates a new file to write in
    f = open(filename, write_condition)

    # loops through the data inputed and writes it in a csv format
    for i in range(len(data)):
        # loops through every list in the big data list
        for j in data[i]:
            f.write(j)
        if i < (len(data)-1):
            f.write(",")
        else:
            f.write("\n")
    
    f.close()
    

def write_txt(filename,data,overwrite):
    '''This function takes in data in a list and writes it as a text file
    
    Parameters:
        filename (str): a string that indicates the file name
        data (lst): list containing all nessesary information
        overwrite (bool): Tells the code whether to overwrite or to append the data
    '''
    
    # setting a variable to indicate whether it will append or overwrite
    write_condition = "a"
    if overwrite:
        write_condition = "w"
    
    # opens the file or creates a new file to write in
    f = open(filename, write_condition)

    # loops through the data inputed and writes it in a text format
    for i in range(len(data)):
        for j in data[i]:
            f.write(j)
    
    f.close()


if __name__ == "__main__":
    user_data = [["John"],["92"],['75'],['84'],['86'],['94']]
    data = read_csv("sale_number.csv", False)
    print(data)
    array = np.array(data)
    print(array)
    write_csv("test.csv", user_data, True)




