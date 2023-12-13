# A beer tale: 2010's gluten-free bloom and stereotypes around gluten-free consumption.

[Go to the Milestone P2 code](./code/P2_Milestone.ipynb)

## Abstract

During the 2010s, gluten-free food made a breakthrough in popularity and was much more available in general shops. Interestingly, in France and Belgium, people came up with stereotypes regarding gluten-free consumers and products, describing such a trend as a flash in a pan. One of those stereotypes is about the persona of gluten-free buyers, often described as urban snobbish people who want to distinguish themselves socially by consuming non-usual products, called "Bobo" in European French-speaking areas. One other stereotype is about the quality of gluten-free products, which are often targeted as less tasteful or interesting from a gustatory point of view. Based on all these discussions, the project attempts to characterize the emergence of gluten-free products through the example of beers, as well as demystifying or validating the stereotypes associated with them.

## Research Questions:
    - Was there actually an increase in consumption of gluten-free products during the 2010's?
    - Is this phenomenon only European or also impactful in other regions of the world?
    - Can sociological particularities be seen between gluten-free beer drinkers and the general population of beer drinkers?
    - Is there actual differences in the taste of gluten-free beers and comparable beers?

## Methods

Part 1. Loading data, cleaning and preprocessing

We have data from the Beeradvocate and the Ratebeer websites. To perform preliminary analysis, we constructed the workflow to read in the huge .txt files, identify repeating contents, and convert them into readable dataframes.

Datasets to work with:
(1) the whole dataset
(2) the gluten free dataset: reviews/ratings on gluten free beers.
(3) the non-gluten free dataset: reviews/ratings on non-gluten free beers made by those who also gave ratings to gluten free beers (for better sample size balancing and data matching)
(4) the non-gluten free dataset: reviews/ratings on non-gluten free beers made by people who didn’t give ratings to gluten free beers.
(5) (to be discussed)

For dataset (2), we extracted the gluten free beers by keywords filtering from the ./ratings.txt file of the RateBeer and both ./ratings.txt and ./reviews.txt files from BeerAdvocate. The exploratory data analysis was done with dataset (2). For dataset (3) and (4), we will filter by user_id that appear in dataset (2), such that we exclude the users that comment only on glutenfree beers.

Part 2. EDA 
After diluting the gluten free beers out of the whole dataset, a temporal analysis on the availability of beers as well as on the popularity of these beers has been done, in terms of how many beers were produced across the years. We also analyzed how many ratings were written from 2006 to 2017, observing a steep increase for gluten-free beers in Europe in 2012 compared to all beers, which could be the beginning of the trend, and an increase worldwide too. Not only the amount of reviews, but also the numerical rating increased overall and for each individual parameter (aroma, appearance, palate, taste) with changes between all beers and gluten-free beers. This gives insight on whether there are actual differences in tastes between gluten-free and other beers. However data were not type of beer-matched, which could bring bias into those parameters. An initial vocabulary analysis was done with word clouds, but no significant insight could be achieved from it.


Part 3. Sentiment analysis

In addition to numerical ratings, text reviews should also reflect how the consumer think about the products. We thought that it would be interesting to inspect the sentiment of gluten free beer text reviews in the following aspects:
(1) correlation with the ratings
(2) trend across regions (countries) and time (year)
However, after discussing more in depth, the initial analysis turned out to need a more fine-grained structure. The next part is describing the procedure we have in mind in detail.

(until here: things already done)

Part 4. “Fanciness” analysis

To study the possible “bobo” persona proposed in our research questions, we study the spatiotemporal evolution of “fanciness” wording from the comment, as speaking in a imaged way with literate words is a key feature of this social group. From the EDA, we learned that it’s possible to study the frequency of words. Here, we start with compute the frequency of the top-N (N~100) most frequency adjectives from dataset (1). From these top frequent adjectives, we manually classify them into 3 different categories: positive, negative, neutral. Among these three categories, we further distinguish fancy and non-fancy words. For each dimension, we define the so-called fanciness score: a weighted sum for fancy word (+) and non-fancy word (-) appearance. As text is in different languages, this is done for each language frequently found in the dataset and spoken by the group at a fluent level (English, French and German).  Spacy package is used to define the language of the comments.
Next, for dataset (2), (3), and (4), we compute such fanciness scores, plot them in 3D space in user and region level to see how it is different between conditions. Clustering methods can be applied to discover underlying structures. These steps could guide us to understand if there are sociological particularities in between.

Example beer adjectives: https://describingwords.io/for/beer


## Proposed Timeline

until 01.12.23 - Deadline Homework 2

until 08.12.23 - Prepare all relevant datasets for the following analysis, get N most used adjectives per language.

until 15.12.23 - Do the sentiment analysis, vocabulary analysis manual labeling of adjectives and start working on the formatting of the Github website

until 22.12.23 - Hand-in deadline, wrap-up the analysis, draw the conclusions from the data , finalize the data story on the website, and prepare the readme file.


## Organization within the team

| Names| Tasks |
| --- | ----------- |
| Mathieu Charbonnier | EDA, Data cleaning, Language processing|
| Seif Hamed | EDA, Data cleaning, Plots |
| Alessandro Fulciniti | EDA, Data cleaning, Github website|
| Yung-Cheng Jay Chiang | Sentiment analysis|
| Emile Dorchies | Story, Ideation, EDA|


12/13 discussion

Storyline
- Spatiotemporal analysis (almost done by Mathieu)
  - Dataset: whole dataset (BA + RB) 
- Rating analysis (Emile)
  - Dataset: beer-type-matched gluten-free/non-gluten-free dataset (D2)
  - Method: regression separately on each rating metrics
  - Assumption: gluten-free beers taste worse 
- Review analysis
  - Dataset: all the reviews left by unique users in the gluten-free beer reviews
  - Keep only french and english
  - Tokenization -> stop/space/punc cleaning -> stemming -> pos tag -> pick adj and adv
  - Study the freq of these keywords (histogram, word cloud)
  - Characterize unique users by the bag of keywords they use: `[good: 0.1, light: 0.2, ...]` -> TF-IDF matrix
  - Dimension reduction/clustering -> characterize users according to the word they use
