# Define useful functions for sentiment analysis
import os, sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def open_big_txt(folder, file_name, max_row):
    """Read in the text file and return a dataframe
    
    Args:
        folder: the folder where the text file is stored
        file_name: the name of the text file
        max_row: the maximum number of data to read in
    
    Returns:
        ratings: a dataframe containing the formated data
    """
    ratings = pd.DataFrame(columns = ["beer_name", "beer_id", "brewery_name", "brewery_id", "style", "abv", "date", "user_name", "user_id", "appearance", "aroma", "palate", "taste", "overall", "rating", "text", "review"])
    # open the file
    with open(os.path.join(folder, file_name+".txt"), "r") as f:
        # read the file line by line
        row = dict()
        for line in f:
            # if line number is larger than max_line, break
            if len(ratings) > max_row:
                break
            # the text file recorded chunks of data representing each review
            # beer_name, beer_id, brewery_name, brewery_id, style, abv, date, user_name, user_id, appearance, aroma, palate, taste, overall, rating, text, review
            # the data is recorded in the order above, line by line iteratively
            
            # read in the data, split each line by the colon, and put them into a dataframe
            # represent each review as a row
            
            # split the line by the colon
            line = line.split(":")
            # if the line is empty, skip
            if len(line) < 2:
                continue
            else:
                if line[0] == "beer_name":
                    # start a new row
                    row = dict()
                    row[line[0]] = line[1].strip()
                elif line[0] == "review":
                    # end of the review
                    row[line[0]] = line[1].strip()
                    # append the row to the dataframe
                    ratings.loc[len(ratings)] = row
                else:
                    row[line[0]] = line[1].strip()        
    return ratings
        