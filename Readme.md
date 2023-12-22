# Beer Quest - On Finding the "BOBO"
2010's gluten-free bloom and stereotypes around gluten-free consumption.

[Go to the datastory website](https://jay4biopz.github.io/adarescueteam-beerquest/story), or its [repo](https://github.com/Jay4BioPZ/adarescueteam-beerquest.git)

## Abstract

During the 2010s, gluten-free food made a breakthrough in popularity and was much more available in general shops. Interestingly, in France and Belgium, people came up with stereotypes regarding gluten-free consumers and products, describing such a trend as a flash in a pan. One of those stereotypes is about the persona of gluten-free buyers, often described as urban snobbish people who want to distinguish themselves socially by consuming non-usual products, called "Bobo" in European French-speaking areas. One other stereotype is about the quality of gluten-free products, which are often targeted as less tasteful or interesting from a gustatory point of view. Based on all these discussions, the project attempts to characterize the emergence of gluten-free products through the example of beers, as well as demystifying or validating the stereotypes associated with them.
This is done adopting a fictional point of view: the International Beer League (IBL) asking us to investigate a putative increase in consumption of gluten-free beers, and to see who the people drinking gluten-free beer and especially whether they are those "bobos".

## Research Questions:
    - Was there an increase in consumption of gluten-free products during the 2010s, where did it happen and with what dynamics?
    - Is there actual differences in the taste of gluten-free beers and comparable beers?
    - Can sociological particularities be seen between gluten-free beer drinkers and the general population of beer drinkers?

## Methods

### Step 1. Cleaning and preprocessing the data

We have data from the Beeradvocate (BA) and the Ratebeer(RB) websites. To perform preliminary analysis, we constructed the workflow to read in the huge .txt files, identify repeating contents, and convert them into readable dataframes that are then saved as pickle-compressed files. As our analysis compares gluten-free (GF) and non-gluten-free (NGF) beers, we identify GF beers by looking at whether their names contain "gluten". We isolate the reviews and ratings made on those beers to create two datasets: the ratings on GF beers and the ones on NGF beers. We do that for both BA and RB as well as a merged one. Then we filter out the beers from a beer style (amber, blond, ...) that is not present in the GF beers. Later, we create another dataset containing only reviews from RB, in English or French, specifically for the textual analysis.


### Step 2. Primary analysis: Spatiotemporal characteristic of GF beer consumption

We assume that we can understand the evolution of GF beer consumption over the years by looking at the number of ratings over time. We use the interactive plots from plotly to illustrate the spatiotemporal behavior of 6 countries, namely France, Latvia, Belgium, Canada, Denmark, and the USA. The temporal analysis is done worldwide showing the increase in GF-beer consumption, both in brut number of ratings as well as in proportion of GF ratings over all ratings. A second analysis is done spatially, by looking at the number of GF reviews and their proportion per country.


### Step 3. Analysis of GF beers: ratings and sentiment analysis

The dataset contains different rating metrics: rating, taste, appearance, aroma, palate, and overall rating. The evolution of those metrics for both GF and NGF beers was calculated per year for both BA and RB datasets, as the metrics range is different between the datasets. Namely, for RB for the single ratings from 1 to 10, for the overall from 1 to 20, and BA ratings from 1 to 5.
To complement this, sentiment analysis was performed on the written reviews using the vaderSentiment package. This was done to see if their dynamics correlate well with the ratings or if differences between what is rated and what is expressed in the comments could be seen.


### Part 4. Vocabulary analysis 

As a first step, we do a t-SNE plot to illustrate linguistic similarities between the reviewers. It is a non-linear dimensionality reduction method and helps to identify patterns. To support our findings, we perform a logistic regression to be able to predict glutenfree users based on their textual review. Further, we separate the individual words by glutenfree and not glutenfree users and count their frequency making sure that they do not appear in the non-glutenfree dataset. After this, we create a bag of words (BOW) consisting of the words that only are written by glutenfree users and plot it into a beer-shaped jar into a word cloud with the WordCloud package. Last but not least, ChatGPT helps us to rank the words contained in the BOW by their fanciness, with a black box approach, or as GPT states "_I'll use a subjective assessment based on their perceived complexity or rarity in everyday language."_


## Organization within the team

| Name                  | Task                                              |
|-----------------------|--------------------------------------------------------|
| Mathieu Charbonnier   | EDA, Spatiotemporal analysis, Text analysis, Regressions |
| Seif Hamed            | EDA, Story-Ideation and Execution, Website ideation    |
| Alessandro Fulciniti  | Data cleaning, Language processing, Website design      |
| Yung-Cheng Jay Chiang | EDA, Code cleaning, Visualizations, Website design     |
| Emile Dorchies        | EDA, Story-Ideation and Execution, Rating analysis     |

