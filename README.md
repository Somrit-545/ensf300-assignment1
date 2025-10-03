
# Console Wars - A Video Game Data Analysis Tool

A terminal-based data analysis program that provides useful insights into video game sales, ranking, and genre popularity across different gaming platforms from 1980-2020.


# Project Overview

Console Wars is a 100% Python based application that analyzes video game data to help users discover detailed information about their favourite gaming platforms. This program utilizes CSV data to provide the detailed insights in an organized way.

# Features

Platform Analysis: Get detailed information for specific gaming platforms
Sales Data: View maximum, minimum, and average sales across different regions
Ranking Information: Discover highest and lowest ranked games
Genre Popularity: Shows which genres are most and least popular on each platform
Regional Variance: Analyze sales data across North America, Europe, Japan, and other regions
User Session TrackingL Keeps track of the users' search history and preferences

# Installation

Prerequisites: Python 3.11.9 or higher
Required Python Packages: numpy and matplotlib
Setup:
    1. Clone or download the project files
    2. All the required files must be in the same directory:
        a) design_project_debug.py (main program)
        b) general_information.py (supporting data)
        c) user_csv.py (CSV handling file)
        d) rank_of_games_by_sales.csv (game ranking file)
        e) sale_number.csv (sales data)
        f) Platform_Year_Genre_Publishers.csv (genre and publisher data)
    3. install requireed packages:
        pip install numpy
        pip install matplotlib


# Example Session
    ----------------------------------------------------------------------
    Welcome to the Console Wars!! This is a program that helps you find out some niche details about your favourite gaming platforms.

    **Note that this date is relevant from 1980-2020.**
    ----------------------------------------------------------------------
    Please choose a gaming platform to find out more about its ranking, genre and sales!

        -type '1' to see the entire list of gaming platforms we currently have.
        -type '0' if you would like to exit this program.
    >> 1

    Here's what we currently have-
    2600, SAT, 3DO, 3DS, DC, DS, GB, GBA, GC, GEN, GG, N64, NES, NG, PC, PCFX, PS, PS2, PS3, PS4, PSP, PSV, SCD, SNES, TG16, WII, WIIU, WS, X360, XB, XONE.

    Please choose a gaming platform to find out more about its ranking, genre and sales!

        -type '1' to see the entire list of gaming platforms we currently have.
        -type '0' if you would like to exit this program.
    >> dc

    Choose one of the following options:
            1. Finding the max (Highest Rank, Most Popular Genre, Highest Sale Numbers)
            2. Finding the min (Lowest Rank, Least Popular Genre, Lowest Sale Numbers)
            3. Finding the average (Average Ranking, Average Amount of Games in All Genres, Average Sale Numbers)
            0. Return to main menu.
    >> 3

    The Average General Data:
    The average rank of all games sold on the DC is 638
    The average units sold in the NA region is 1.26 million units.
    The average units sold in the EU region is 0.61 million units.
    The average units sold in the JP region is 0.52 million units.
    The average units sold in the OTHER region is 0.08 million units.
    The average units sold in the GLOBAL region is 2.42 million units.
    The average games per genre is 2 games.

    Please choose a gaming platform to find out more about its ranking, genre and sales!

        -type '1' to see the entire list of gaming platforms we currently have.
        -type '0' if you would like to exit this program.
    >> 0
    ----------------------------------------------------------------------
    Thank you for using Fadi Salman's Program!


# Key Functions
Core Analysis Functions
    1. get_platform(): Handles user platform selection
    2. usable_data(): Filters data for specific platform
    3. get_max()/get_min()/get_ave(): Calculate statistics
    4. print_max_values()/print_min_values()/print_ave_values(): Display results

Data processing
    1. get_all_companies(): Compiles list of game Platform_Year_Genre_Publishers
    2. get_how_many_games_ranked(): Counts games per publisher
    3. get_top_five(): Identifies top publishers
    4. ave_sale_per_year(): Analyzes yearly sales trends

Output Files:
The program generates two files:
    1. all_user_inputs.txt: Formatted sessino log with timestamps
    2. all_user_inputs.csv: Structured data of user interactions


# Developers
Main developer: Fadi Salman
Supporting developers: 
    1. Omar Al-Mahfoodh
    2. Somrit Dewan
    3. Usman Mirza

# Important Mesage
This program was an educational project for ENDG 233 course which was later refined by the supporting developers for ENSF 300 course.

