# A beer tale: 2010's gluten-free bloom and stereotypes around gluten-free consumption.

[Go to the Milestone P2 code](./code/P2_Milestone.ipynb)

## Abstract

During the 2010s, gluten-free food made a breakthrough in popularity and was much more available in general shops. Interestingly, in France and Belgium, people came up with stereotypes regarding gluten-free consumers and products, describing such a trend as a flash in a pan. One of those stereotypes is about the persona of gluten-free buyers, often described as urban snobbish people who want to distinguish themselves socially by consuming non-usual products, called "Bobo" in European French-speaking areas. One other stereotype is about the quality of gluten-free products, which are often targeted as less tasteful or interesting from a gustatory point of view. Based on all these discussions, the project attempts to characterize the emergence of gluten-free products through the example of beers, as well as demystifying or validating the stereotypes associated with them.
This is done adopting a fictional point of view: the International Beer League (IBL) asking us to investigate on a putative increase on consumption of gluten-free beers, and to see who are the people drinking gluten-free beer and especially whether they are those "bobos".

## Research Questions:
    - Was there actually an increase in consumption of gluten-free products during the 2010's, where did it happen and with what dynamics?
    - Is there actual differences in the taste of gluten-free beers and comparable beers?
    - Can sociological particularities be seen between gluten-free beer drinkers and the general population of beer drinkers?

## Methods

Step 1. Cleaning and preprocessing the data

We have data from the Beeradvocate (BA) and the Ratebeer(RB) websites. To perform preliminary analysis, we constructed the workflow to read in the huge .txt files, identify repeating contents, and convert them into readable dataframes that are then saved as pickle compressed files. As our analysis compare gluten-free (GF) and non-gluten-free (NGF) beers, we identified GF beers looking at whether their name contain "gluten". We isolated the reviews and ratings made on those beers to create two dataset: the ratings on GF beers and the ones on NGL beers. We did that for both BA and RB as well as a merged one. Then we filtered out the beers from a beerstyle (amber, blond, ...) that was not present in the the GF beers. Later on, we created other dataset containing reviews from RB in English or French. This was done using the Scapy package. BA dataset was not done for computational reason, as identifying language on millions of reviews is long.


Step 2. Primary analysis: time and spatial characteristic of GF beers consumption

To know about the evolution of GF beers consumption, we take the number of ratings as a proxy. A first temporal analysis was done worldwide to show the increase in GF-beer consumption, both in brut number of ratings as well as in proportion of GF ratings over all ratings. A second analysis was done spatially, by looking at the number of GF reviews and their proportion per country, and then plotted on an interactive map (**METHOD ?**). Another temporal analysis was done on some specific country, looking at the dynamic of the number of rating through the years. This is also shown on an interactive plot.


Step 3. Analysis of GF beers: ratings and emotion analysis

The dataset contain different rating metrics: rating, taste, appearance, aroma, palate, overall rating. The evolution of those metrics for both GF and NGF beers were calculated per year for both BA and RB datasets, as the metrics range are different between the datasets. Beerstyle was thought to be a possible confounding factor for the ratings between GF and NGF beers, as they have widely different beerstyle proportion. To address that, a subset of each dataset was created with the same proportion of beerstyle as the GF ratings. 
To complement this, an emotion analysis was performed on the written reviews using the vaderSentiment package. This was done to see if their dynamics correlates well with the ratings or if differences between what is rated and what is expressed in the comments could be seen.


Part 4. Vocabulary analysis **TO BE DONE, can't do it-Emile**

_To study the possible “bobo” persona proposed in our research questions, we study the spatiotemporal evolution of “fanciness” wording from the comment, as speaking in a imaged way with literate words is a key feature of this social group. From the EDA, we learned that it’s possible to study the frequency of words. Here, we start with compute the frequency of the top-N (N~100) most frequency adjectives from dataset (1). From these top frequent adjectives, we manually classify them into 3 different categories: positive, negative, neutral. Among these three categories, we further distinguish fancy and non-fancy words. For each dimension, we define the so-called fanciness score: a weighted sum for fancy word (+) and non-fancy word (-) appearance. As text is in different languages, this is done for each language frequently found in the dataset and spoken by the group at a fluent level (English, French and German).  Spacy package is used to define the language of the comments.
Next, for dataset (2), (3), and (4), we compute such fanciness scores, plot them in 3D space in user and region level to see how it is different between conditions. Clustering methods can be applied to discover underlying structures. These steps could guide us to understand if there are sociological particularities in between._

Example beer adjectives: https://describingwords.io/for/beer


## Organization within the team


|-----------------------|--------------------------------------------------------|
| Mathieu Charbonnier   | EDA, Spatiotemporal analysis, Text analysis, Regressions |
| Seif Hamed            | EDA, Story-Ideation and Execution, Website ideation    |
| Alessandro Fulciniti  | Data cleaning, Language processing, Website design      |
| Yung-Cheng Jay Chiang | EDA, Code cleaning, Visualizations, Website design     |
| Emile Dorchies        | EDA, Story-Ideation and Execution, Ratings analysis     |


