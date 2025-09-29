# design_project.py
# ENDG 233 F24
# Fadi Salman
# L03 - 5
# A terminal-based data analysis and visualization program in Python.
# You must follow the specifications provided in the project description.
# Remember to include docstrings and comments throughout your code.
import numpy as np
import matplotlib.pyplot as plt
from math import floor
import general_information as gi
import user_csv as cs
import time

def error_message():
    '''This function prints a message when the user enters an invalid input'''

    print(f"-"*70)                                          # Prints "-" 70 times
    print(f"There's an error in your input. Please try again.")    # Prints the error statement
    print(f"-"*70)

def exit_message():
    '''This functions prints the exit message'''

    print(f"-"*70)                                          # Prints "-" 70 times
    print("Thank you for using Fadi Salman's Program! Don't forget to check out the awesome graphs!!")     # Prints the exit message

def get_platform():
    '''Prints out a menu that prompts the user to select a gaming plateform
    
    Returns:
        user_input (str): a capitilized valid input or "0" or "1"
    '''

    # Printing the menu
    print(f"Please choose a gaming plateform to find more data about its ranking, genre and sales")
    print(f"type '1' if you are unsure which plateforms are available.")
    print(f"type '0' if you would like to exit this program.")

    # Prompting user for input and capitalizing it
    user_input_initial = input(">> ")
    user_input = user_input_initial.upper()


    # Checking for invalid input or "1"
    if (user_input != "0" and user_input != "1" and user_input not in gi.PLATFORM):
        error_message()         # Calls error message function
        return get_platform()   # Recalls this function until valid input 

    elif (user_input == "1"):   # Checking if the user wants a list of the platforms
        print()
        platform_list()         # Calls the function to get the list of platforms
        return get_platform()   # Recalls this function

    else:
        # Checks if the user_input is a special case
        if user_input in gi.CHANGED.keys():
            user_input = gi.CHANGED[user_input]     # Changes the special input into its popular name
            return user_input                       # Returns the new user_input
        else:
            return user_input                       # Returns the original user_input unchanged   

def platform_list():
    '''Prints out a list of gaming platforms'''

    for item_pos,item in enumerate(gi.PLATFORM):
        if(item_pos == (len(gi.PLATFORM)-1)):
            print(f"{item}.\n")         # Prints last item and prints new line
        else:
            print(f"{item}, ", end="")  # Prints item in the list


def menu_option():
    ''' Prints menu options and prompts user to select an option to manipulate csv data accordingly
    
    Returns:
        user_input (str): a valid input choosing a specific option
    '''

    # Prints menu options
    print(f"\nChoose one of the following options: ")
    print(f"\t1. Finding the max (Highest Rank, Most Popular Genre, Highest Sale Numbers)")
    print(f"\t2. Finding the min (Lowest Rank, Least Popular Genre, Lowest Sale Numbers)")
    print(f"\t3. Finding the average (Average Ranking, Average Amount of Games in All Genres, Average Sale Numbers)")
    print(f"\t0. Return to main menu.")

    # Prompts user for an input
    user_input = input(">> ")

    # Checking for invalid inputs
    if (user_input != "0" and user_input != "1" and user_input != "2" and user_input != "3"):
        error_message()         # Calls error message function
        return menu_option()    # Recalls this function until a correct valid input
    else:
        return user_input       # Returns the user selection as a string

def get_max(data):
    '''Uses all relevant information to find max rank, sale numbers and most popular genre
    
    Parameters:
        data (lst): Contains all relevant information to calculate max
            [all_ranks,na_sales,eu_sales,jp_sales,other_sales,global_sales, all_genre]   
    
    Returns:
        list: [highest rank, Most sales (na),Most sales (eu) ,Most sales (jp), Most sales (other), Most sales (globally), how many times each genre appeared]
    '''

    # declare all nessesary variables
    initial_genre_list = [0,0,0,0,0,0,0,0,0,0,0,0]
    
    # converting list into numpy arrays
    rank_array = np.array(data[0])
    na_sales_array = np.array(data[1])
    eu_sales_array = np.array(data[2])
    jp_sales_array = np.array(data[3])
    other_sales_array = np.array(data[4])
    global_sales_array = np.array(data[5])

    # loops to count how many times each genre is present
    for j in data[6]:
        for k in range(len(gi.ALL_GENRE)):
            if j == gi.ALL_GENRE[k]:
                initial_genre_list[k] += 1
    
    return [rank_array.min(), na_sales_array.max(),eu_sales_array.max(),jp_sales_array.max(),other_sales_array.max(), global_sales_array.max(), initial_genre_list]

def print_max_values(plateform,info,rank_list,sale_list):
    '''Find the rest of the nessesary information and extra details to print the information to the user in a nice format
    
    Parameters:
        plateform (str): a valid plateform
        info (str): a list containing [highest rank, Most sales (na),Most sales (eu) ,Most sales (jp), Most sales (other), Most sales (globally), how many times each genre appeared]
        rank (nested lst): a list containing multiple list containing [Rank,Name,Platform] of all games in data
        sale (nested lst): a list containing multiple list containing [Platform,NA_Sales,EU_Sales,JP_Sales,Other_Sales,Global_Sales] of all games in data
        genre (nested lst): a list containing multiple list containing [Platform,Year,Genre,Publisher] of all games in data
    
    ''' 

    # Declaring nessesary variables
    num_which_info_is_found_at = [0,0,0,0,0,0,0]        # lst which holds the index at which valuable information is found at
    value_of_max_genre = 0                              # how many games are in the most popular genre
    index_where_max_genre_is_at = 0                     # The index which indicates which genre is the most popular
    

    # Loop to find index where important information is found
    for i in range (len(rank_list)):                # checking orignal data list
        if rank_list[i][0] == info[0]:
            num_which_info_is_found_at[0] = i       # changes the first integer of the list to the index where the information is found 
        

        for j in range(1,6):                        # checks all sales, (NA_Sales,EU_Sales,JP_Sales,Other_Sales,Global_Sales)
            if float(sale_list[i][j]) == info[j]:
                num_which_info_is_found_at[j] = i   # changes a specific index of the list to the index at which the information is found 

        # Find the most popular genre
        for pos,val in enumerate(info[6]):
            if val > value_of_max_genre:
                value_of_max_genre = val            # assigns the number of games of the most popular genre
                index_where_max_genre_is_at = pos   # assigns the position, which can be used to identify the genre


    # Prints all the data for the user
    print(f"\nMaximum Data:")
    print(f"The highest ranking video game in terms of sales is {rank_list[num_which_info_is_found_at[0]][1]} ranking {info[0]} out of 16600")
    # loop to automatically print all the sale number values
    for k in range(1,6):
        print(f"The highest selling video game {gi.REGION_PRINT[k-1]} for the {plateform} is '{rank_list[num_which_info_is_found_at[k]][1]}' selling {info[k]} million units.")
    print(f"The most popular genre is {gi.ALL_GENRE[index_where_max_genre_is_at]} having {value_of_max_genre} games.")
    print()

def aquiring_data_to_useable_form(plateform,rank,sale,genre):
    '''Pulls the correct information according to user selection of the platform
    
    Parameters:
        plateform (str): a valid plateform
        rank (nested lst): a list containing multiple list containing [Rank,Name,Platform] of all games in data
        sale (nested lst): a list containing multiple list containing [Platform,NA_Sales,EU_Sales,JP_Sales,Other_Sales,Global_Sales] of all games in data
        genre (nested lst): a list containing multiple list containing [Platform,Year,Genre,Publisher] of all games in data

    Returns:
        list: [all_ranks,na_sales,eu_sales,jp_sales,other_sales,global_sales, all_genre]
            list contains relevant information about the specific user platform
    '''
    
    # Establishing all needed lists to hold relevant information
    all_ranks = []
    na_sales = []
    eu_sales = []
    jp_sales = []
    other_sales = []
    global_sales = []
    all_genre = [] 
    
    # loops in all items checking for the user plateform and extracts revelant information
    for i in range(len(rank)):
        # checking if the plateform is the same as the user choice
        if (rank[i][2] == plateform):
            # adds ranking of game 
            all_ranks += [int(rank[i][0])]

        # checking if the plateform is the same as the user choice
        if (sale[i][0] == plateform):
            # adds sale data
            na_sales += [float(sale[i][1])]
            eu_sales += [float(sale[i][2])]
            jp_sales += [float(sale[i][3])]
            other_sales += [float(sale[i][4])]
            global_sales += [float(sale[i][5])]

        # checking if the plateform is the same as the user choice
        if (genre[i][0] == plateform):
            # adds genre to list
            all_genre += [genre[i][2]]
    
    # returns all relevant information
    return [all_ranks,na_sales,eu_sales,jp_sales,other_sales,global_sales, all_genre]


def print_max_values(platform,info,rank_list,sale_list):
    '''Finds the nessesary information to print max values and statistics to the user in plain English
    
    Parameters:
        platform (str): a valid platform
        info (str): a list containing [highest rank, Most sales (na),Most sales (eu) ,Most sales (jp), Most sales (other), Most sales (globally), how many times each genre appeared]
        rank (nested lst): a list containing multiple list containing [Rank,Name,Platform] of all games in data
        sale (nested lst): a list containing multiple list containing [Platform,NA_Sales,EU_Sales,JP_Sales,Other_Sales,Global_Sales] of all games in data
    
    ''' 

    # Declaring nessesary variables
    num_which_info_is_found_at = [0,0,0,0,0,0,0]        # lst which holds the index at which valuable information is found at
    value_of_max_genre = 0                              # how many games are in the most popular genre
    index_where_max_genre_is_at = 0                     # The index which indicates which genre is the most popular
    

    # Loop to find index where important information is found
    for i in range (len(rank_list)):                # checking orignal data list
        if rank_list[i][0] == info[0]:
            num_which_info_is_found_at[0] = i       # changes the first integer of the list to the index where the information is found 
        

        for j in range(1,6):                        # checks all sales, (NA_Sales,EU_Sales,JP_Sales,Other_Sales,Global_Sales)
            if float(sale_list[i][j]) == info[j]:
                num_which_info_is_found_at[j] = i   # changes a specific index of the list to the index at which the information is found 

        # Find the most popular genre
        for pos,val in enumerate(info[6]):
            if val > value_of_max_genre:
                value_of_max_genre = val            # assigns the number of games of the most popular genre
                index_where_max_genre_is_at = pos   # assigns the position, which can be used to identify the genre


    # Prints all the data for the user
    print(f"\nMaximum Data:")
    print(f"The highest ranking video game in terms of sales is {rank_list[num_which_info_is_found_at[0]][1]} ranking {info[0]} out of 16600")
    # loop to automatically print all the sale number values
    for k in range(1,6):
        print(f"The highest selling video game {gi.REGION_PRINT[k-1]} for the {platform} is '{rank_list[num_which_info_is_found_at[k]][1]}' selling {info[k]} million units.")
    print(f"The most popular genre is {gi.ALL_GENRE[index_where_max_genre_is_at]} having {value_of_max_genre} games.")
    print()


def print_max_values(plateform,info,rank_list,sale_list):
    '''Find the rest of the nessesary information and extra details to print the information to the user in a nice format
    
    Parameters:
        plateform (str): a valid plateform
        info (str): a list containing [highest rank, Most sales (na),Most sales (eu) ,Most sales (jp), Most sales (other), Most sales (globally), how many times each genre appeared]
        rank (nested lst): a list containing multiple list containing [Rank,Name,Platform] of all games in data
        sale (nested lst): a list containing multiple list containing [Platform,NA_Sales,EU_Sales,JP_Sales,Other_Sales,Global_Sales] of all games in data
        genre (nested lst): a list containing multiple list containing [Platform,Year,Genre,Publisher] of all games in data
    
    ''' 

    # Declaring nessesary variables
    num_which_info_is_found_at = [0,0,0,0,0,0,0]        # lst which holds the index at which valuable information is found at
    value_of_max_genre = 0                              # how many games are in the most popular genre
    index_where_max_genre_is_at = 0                     # The index which indicates which genre is the most popular
    

    # Loop to find index where important information is found
    for i in range (len(rank_list)):                # checking orignal data list
        if rank_list[i][0] == info[0]:
            num_which_info_is_found_at[0] = i       # changes the first integer of the list to the index where the information is found 
        

        for j in range(1,6):                        # checks all sales, (NA_Sales,EU_Sales,JP_Sales,Other_Sales,Global_Sales)
            if float(sale_list[i][j]) == info[j]:
                num_which_info_is_found_at[j] = i   # changes a specific index of the list to the index at which the information is found 

        # Find the most popular genre
        for pos,val in enumerate(info[6]):
            if val > value_of_max_genre:
                value_of_max_genre = val            # assigns the number of games of the most popular genre
                index_where_max_genre_is_at = pos   # assigns the position, which can be used to identify the genre


    # Prints all the data for the user
    print(f"\nMaximum Data:")
    print(f"The highest ranking video game in terms of sales is {rank_list[num_which_info_is_found_at[0]][1]} ranking {info[0]} out of 16600")
    # loop to automatically print all the sale number values
    for k in range(1,6):
        print(f"The highest selling video game {gi.REGION_PRINT[k-1]} for the {plateform} is '{rank_list[num_which_info_is_found_at[k]][1]}' selling {info[k]} million units.")
    print(f"The most popular genre is {gi.ALL_GENRE[index_where_max_genre_is_at]} having {value_of_max_genre} games.")
    print()



def get_min(data):
    '''Uses all relevant information to find the lowest rank, the lowest sale numbers and least popular genre
    
    Parameters:
        data (lst): Contains all relevant information to calculate min
            [all_ranks,na_sales,eu_sales,jp_sales,other_sales,global_sales, all_genre]   
    
    Returns:
        list: [Lowest rank, Least sales (na),Least sales (eu) ,Least sales (jp), Least sales (other), Least sales (globally), how many times each genre appeared]
    '''
    
    # declare all nessesary variables
    initial_genre_list = [0,0,0,0,0,0,0,0,0,0,0,0]
    
    # converting list into numpy arrays
    rank_array = np.array(data[0])
    na_sales_array = np.array(data[1])
    eu_sales_array = np.array(data[2])
    jp_sales_array = np.array(data[3])
    other_sales_array = np.array(data[4])
    global_sales_array = np.array(data[5])


    # loops to count how many times each genre is present
    for genre_in_list in data[6]:
        for specific_genre_index in range(len(gi.ALL_GENRE)):
            if genre_in_list == gi.ALL_GENRE[specific_genre_index]:     # checking to see which genre was found 
                initial_genre_list[specific_genre_index] += 1           # counting the number of times each genre was found
    
    return [rank_array.max(), na_sales_array.min(),eu_sales_array.min(),jp_sales_array.min(),other_sales_array.min(), global_sales_array.min(), initial_genre_list]


def print_min_values(plateform,info,rank_list,sale_list,genre_list):
    '''Find the rest of the nessesary information and extra details to print the information to the user in a nice format
    
    Parameters:
        plateform (str): a valid plateform
        info (str): a list containing [Lowest rank, Least sales (na),Least sales (eu) ,Least sales (jp), Least sales (other), Least sales (globally), average games per genre]
        rank (nested lst): a list containing multiple list containing [Rank,Name,Platform] of all games in data
        sale (nested lst): a list containing multiple list containing [Platform,NA_Sales,EU_Sales,JP_Sales,Other_Sales,Global_Sales] of all games in data
        genre (nested lst): a list containing multiple list containing [Platform,Year,Genre,Publisher] of all games in data
    
    '''


    # Declaring nessesary variables
    num_which_info_is_found_at = [0,0,0,0,0,0,0]
    
    # finding the lowest number of games for a genre 
    value_of_min_genre = min(info[6])
    index_where_min_genre_is_at = 0
    
    # Loop to find index where important information is found
    for i in range (len(rank_list)):
        if rank_list[i][0] == info[0]:
            num_which_info_is_found_at[0] = i
        

        for j in range(1,6):
            if float(sale_list[i][j]) == info[j]:
                num_which_info_is_found_at[j] = i

        for k,l in enumerate(info[6]):
            if l == value_of_min_genre:
                index_where_min_genre_is_at = k


    # Printing all minimum data
    print(f"\nMinimum Data:")
    print(f"The lowest ranking video game in terms of sales is {rank_list[num_which_info_is_found_at[0]][1]} ranking {info[0]} out of 16600")
    
    # Printing sale numbers while checking if the number is too low 
    for k in range(1,6):
        if info[k] == 0:
            print(f"The lowest selling video game {gi.REGION_PRINT[k-1]} for the {plateform} is '{rank_list[num_which_info_is_found_at[k]][1]}' selling less than 10,000 units")
        else:
            print(f"The lowest selling video game {gi.REGION_PRINT[k-1]} for the {plateform} is '{rank_list[num_which_info_is_found_at[k]][1]}' selling {info[k]} million units.")
    
    print(f"The least popular genre is {gi.ALL_GENRE[index_where_min_genre_is_at]} having {value_of_min_genre} games.")
    print()
    




def get_ave(data):
    '''Uses all relevant information to find the average rank, the average sale numbers and the average number of games across all genres
    
    Parameters:
        data (lst): Contains all relevant information to calculate the average
            [all_ranks,na_sales,eu_sales,jp_sales,other_sales,global_sales, all_genre]   
    
    Returns:
        list: [mean rank, average sales (na), average sales (eu), average sales (jp), average sales (other), average sales (globally), average games per genre]
    '''



    #  Declaring nessesary variables
    initial_genre_list = [0,0,0,0,0,0,0,0,0,0,0,0]

    # converting list into numpy arrays
    rank_array = np.array(data[0])
    na_sales_array = np.array(data[1])
    eu_sales_array = np.array(data[2])
    jp_sales_array = np.array(data[3])
    other_sales_array = np.array(data[4])
    global_sales_array = np.array(data[5])
    
    # loops to count how many times each genre is present
    for j in data[6]:
        for k in range(len(gi.ALL_GENRE)):
            if j == gi.ALL_GENRE[k]:
                initial_genre_list[k] += 1
    
    # converts list into numpy array
    all_genres = np.array(initial_genre_list)
    
    return [rank_array.mean(), na_sales_array.mean(),eu_sales_array.mean(),jp_sales_array.mean(),other_sales_array.mean(), global_sales_array.mean(), all_genres.mean()]


def print_ave_values(plateform,info,rank_list,sale_list,genre_list):
    '''Prints the information to the user in a nice format
    
    Parameters:
        plateform (str): a valid plateform
        info (str): a list containing [mean rank, average sales (na), average sales (eu), average sales (jp), average sales (other), average sales (globally), average games per genre]
        rank (nested lst): a list containing multiple list containing [Rank,Name,Platform] of all games in data
        sale (nested lst): a list containing multiple list containing [Platform,NA_Sales,EU_Sales,JP_Sales,Other_Sales,Global_Sales] of all games in data
        genre (nested lst): a list containing multiple list containing [Platform,Year,Genre,Publisher] of all games in data
    
    '''

    # Prints all average data
    print(f"\nThe Average General Data:")
    print(f"The average rank of all games sold on the {plateform} is {floor(info[0])}")
    
    # Printing average sale numbers while checking if the number is too low 
    for i in range(1,6):
        if info[i] == 0:
            print(f"The average units sold in the {gi.REGION[i-1]} region is less than 10,000.")
        else:
            print(f"The average units sold in the {gi.REGION[i-1]} region is {info[i]:.2f} million units.")
    
    print(f"The average games per genre is {floor(info[6])} games.\n")
    



def get_all_companies(genre_list):
    '''Creates a list of all companies that made games
    
    Parameter:
        genre_list (nested lst): a list containing multiple list containing [Platform,Year,Genre,Publisher] of all games in data
    
    Return:
        all_companies (lst): contains every company that made a game good enough to rank on the data sheet
    '''
    
    # Creating an empty list to fill with all the companies 
    all_companies = []

    # loops to try and find all the different companies without repeating any
    for i in range(len(genre_list)):
        if genre_list[i][3] not in all_companies:
            all_companies += [genre_list[i][3]]

    return all_companies

def get_how_many_games_ranked(all_companies,genre):
    '''This function find out how many times each company was present on the data sheets
    
    Parameters: 
        all_companies (lst): Contains all the companies found on the data sheets 
        genre (nested lst): a list containing multiple list containing [Platform,Year,Genre,Publisher] of all games in data
    
    Return:
        all_company_ranking (lst): contains the number of games that ranked and made it on the data sheet 
    '''
    
    # Empty list to hold how many times each company is present on the data sheet
    all_company_ranking = []
    
    # makes the list the size of the number of companies available
    for i in range(len(all_companies)):
        all_company_ranking.append(0)

    # Counts the number of times each company shows up 
    for j in range(len(all_companies)):
        for k in range(len(genre)):
            if all_companies[j] == genre[k][3]:
                all_company_ranking[j] += 1

    return(all_company_ranking)




def get_top_five(all_companies, all_company_ranking):
    ''' This function finds which five companies had the most amount of enteries in the data sheets

    Parameters: 
        all_companies (lst): Contains all the companies found on the data sheets
        all_company_ranking (lst): Contains the number of times each company is found in the data sheets

    Return:
        top_companies_sorted (lst): Returns the top 5 biggest numbers relating to how many times each company is found
        rank_company (lst): Returns a list containting the five most popular companies on the data sheet
    '''
    
    # Defining initial variables
    top_five_companies = []                                             # list that holds the position at which a specific number is found at 
    rank_company = []                                                   # list that holds the top five companies

    # sorts the number of games of each publisher from highest to lowest, making it easy to look at the top 5
    top_companies_sorted = sorted(all_company_ranking, reverse=True)    # assigns the sorted list to another variable
    
    # loops to find the position where each of the 5 biggest numbers are found  
    for i in range(5):
        for pos,val in enumerate(all_company_ranking):
            if top_companies_sorted[i] == val:
                top_five_companies += [pos]

    # loops and uses the previous information to assign the correct company to the number of sales; only top 5.
    for m in top_five_companies:
        rank_company.append(all_companies[m])       # adds the correct company name to the list 


    return top_companies_sorted[:5], rank_company

def ave_sale_per_year(genre_list,sale):
    '''This function finds the total number of sales yearly in each region of the world 

    Parameters:
        genre_list (nested lst): a list containing multiple list containing [Platform,Year,Genre,Publisher] of all games in data
        sale (nested lst): a list containing multiple list containing [Platform,NA_Sales,EU_Sales,JP_Sales,Other_Sales,Global_Sales] of all games in data
    Returns:
        lst: This is a 2d list contains multiple list each having connected columns. 
            [[all the year],[sale in na region],[sales in eu region],[sales in jp region], [sales in other region], [sales globally]]
            this example will show how the first three rows should look:
                [[1980,1981.....]
                 [10, 20........]
                 [30, 40........]]
    '''
    
    
    # Establishing all nessesary variables to hold information
    ave_sales = []
    na_sales = []
    eu_sales = []
    jp_sales = []
    other_sales = [] 
    global_sales = []
    years = []
    count = 0


    # Loops through every year aquiring all the sale numbers in each region
    for j in range(1980,2021):
        years += [j]
        ave_sales += [[0,0,0,0,0]]
        for i in range(len(genre_list)):
            if j == genre_list[i][1]:
                ave_sales[count][0] += sale[i][1]
                ave_sales[count][1] += sale[i][2]
                ave_sales[count][2] += sale[i][3]
                ave_sales[count][3] += sale[i][4]
                ave_sales[count][4] += sale[i][5]
        count += 1


    # assigns the correct sale numbers to the correct region
    for k in range(len(ave_sales)):
        na_sales += [ave_sales[k][0]]
        eu_sales += [ave_sales[k][1]]
        jp_sales += [ave_sales[k][2]]
        other_sales += [ave_sales[k][3]]
        global_sales += [ave_sales[k][4]]
    
    return [years, na_sales, eu_sales, jp_sales,other_sales,global_sales]

# Uses the created functions to read the csv files and assigns them to variables 
rank = cs.read_csv("rank_of_games_by_sales.csv", False)
sale_number = cs.read_csv("sale_number.csv", False)
genre = cs.read_csv("Platform_Year_Genre_Publisher.csv", False)

# The following variables will be used to keep track of the user activity to later use in the write_csv function
number_of_time_the_program_ran = 0
all_platforms_search = []
max_search = 0
min_search = 0
mean_search = 0




# Prints the welcoming message to the user before the main program starts
print(f"Welcome to the Console Wars!! This is a program that helps you find out more about your favorite gaming plateforms.\n**Note that this date is relevant from 1980-2020.**\n\n")

while True:
    # get the user to select a platform by calling the get_plateform function
    user_platform = get_platform()
    
    # Checks if the user would like to exit the program
    if  user_platform == "0":
        break               # exits
    else:
        # keeps track of user platform searches
        all_platforms_search += [str(user_platform)]

        # gets the user to select a menu option by printing the menu and prompting the user to an input
        user_menu_option = menu_option()

        
        if user_menu_option == "1":         # if the user chooses to find out about the max data
            print_max_values(user_platform, get_max(aquiring_data_to_useable_form(user_platform,rank,sale_number,genre)),rank,sale_number) 
            max_search += 1                 # adds another to the count of how many times the user searched this

        elif(user_menu_option == "2"):      # if the user chooses to find out about the min data
            print_min_values(user_platform, get_min(aquiring_data_to_useable_form(user_platform,rank,sale_number, genre)),rank,sale_number)
            min_search += 1                 # adds another to the count of how many times the user searched this

        elif(user_menu_option == "3"):      # if the user chooses to find out about the average data
            print_ave_values(user_platform, get_ave(aquiring_data_to_useable_form(user_platform,rank,sale_number, genre)),rank,sale_number)
            mean_search += 1                # adds another to the count of how many times the user searched this

        elif(user_menu_option == "0"):
            number_of_time_the_program_ran -= 1                 # removes one from the number of times the program ran
            all_platforms_search = all_platforms_search[:-1]    # removes the last platform searched from the list

    number_of_time_the_program_ran += 1                 # keeps track of the number of times the program ran by increasing the value by one





# THIS IS NOT A REQUIREMENT, THIS WAS ONLY FOR FUN
# Creates a text file containing all the user input in a visual way
user_data = []  

# collect all important data and fomats it nicely         
user_data += [[time.ctime(time.time()-25200) + "\n"] , [f"The number of times the program ran is: " + str(number_of_time_the_program_ran)+ "\n"], f"The following platforms were searched:" + str(all_platforms_search) + "\n", [f"Max searches: " + str(max_search),f"\t\tMin searches: " + str(min_search), f"\t\tMean searches: " + str(mean_search)+ "\n\n"]]
cs.write_txt("all_user_inputs_text", user_data, False)


# This portion of the code is using the write_csv function
# it write the following information in this form:
# number_of_time_program_ran,searched_platforms,max_searches,min_searches,mean_searches
user_data_csv = []
user_data_csv += [[str(number_of_time_the_program_ran)], [str(all_platforms_search)], [str(max_search)], [str(min_search)], [str(mean_search)]]
cs.write_csv("all_user_inputs.csv", user_data_csv, False)



# This is the graphing portion of the code
# Establishing all nessesary variables to hold information for graphing
# The nessesary variables for the bar graph:
# The following gets the top 5 publishers using functions
publishers_that_ranked_highly = get_top_five(get_all_companies(genre), get_how_many_games_ranked(get_all_companies(genre), genre))[1]

# The following gets the number of games from the 5 publishers
number_of_games_that_ranked_highly = get_top_five(get_all_companies(genre), get_how_many_games_ranked(get_all_companies(genre), genre)) [0]
five_color = ["orange", "yellow", "green", "red", "blue"]       # 5 colors to make each bar a different color 


# The nessesary variables for the plot graph:
year = ave_sale_per_year(genre,sale_number)[0]                  # The x-axis of the graph 

# The following are the sale numbers in each region which are the y-axis to the graph
na_sales_plot = ave_sale_per_year(genre,sale_number)[1]
eu_sales_plot = ave_sale_per_year(genre,sale_number)[2]
jp_sales_plot = ave_sale_per_year(genre,sale_number)[3]
other_sales_plot = ave_sale_per_year(genre,sale_number)[4]
global_sales_plot = ave_sale_per_year(genre, sale_number)[5]
all_sale_numbers = [na_sales_plot, eu_sales_plot, jp_sales_plot, other_sales_plot, global_sales_plot] 
legend = ["NA", "EU", "JP", "Other", "Global"]
colors_for_plot = ["y", "g", "r", "m", "k"]



# Creating a space to be able to make the garphs
plt.figure()

# Creating the subspace for the first graph (Bar Graph)
plt.subplot(2,1,1)
plt.bar(publishers_that_ranked_highly,number_of_games_that_ranked_highly, color = five_color)
plt.xticks(fontsize = 8)

# labeling all axis and title
plt.title("Top 5 Publishers Between 1980 and 2020")
plt.xlabel("Publishers")
plt.ylabel("Number of Games in Data")



# Creating the second subspace for the second graph (Plot Graph)
plt.subplot(2,1,2)

# Graphing all the sale numbers
for i in range(5):
    plt.plot(year, all_sale_numbers[i], color = colors_for_plot[i])


# Labeling all the axis, creating a legend and titleing the graph
plt.legend(legend)
plt.title("Games Sold Each Year by Each Region of the World")
plt.xlabel("Year")
plt.ylabel("Number of Sales in Millions")


# This function gives spacing between the graphs
plt.tight_layout()

# calls the exit message function
exit_message()

# Shows the graphs
plt.savefig("/usercode/final_plots/final.png")
plt.show()