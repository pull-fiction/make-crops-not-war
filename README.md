# Make crops, not war

Milestone 3 update.

- Data story: [https://pull-fiction.github.io/make-crops-not-war/](https://pull-fiction.github.io/make-crops-not-war/)

- Notebook: [project.html](project.ipynb)

Our data story has been tested on Firefox and Chrome, on 13" and 15" laptops.

## Detailed contribution

- Michael Blackburn: data wrangling, general analysis, agriculture map, buildings map
- Edoardo Debenedetti: data wrangling, general analysis, war events map, Beirut population
- Maksim Kriukov: data exploration, specific crops production changes, import/export analysis
- Simona Leserri: data exploration, specific crops production changes, production change motivations

We will all work on the poster and presentation.

The analysis has been done jointly by everyone with equal contributions.

## Abstract

The impacts of war on a country’s economy, social structure and politics are generally well documented and understood. However, impact on food and crop production has not been studied to the same extent. Through a brief literature research, it has been found that most papers about the topic are quite outdated. Our intention is to fill in this gap through an analysis of the UN Dataset on Food Production in conjunction with war data obtained through WikiData and Lebanon Historical Conflict Mapping and Analysis by Civil Society Knowledge Centre. The increased globalization of food markets along with the amount of significant armed conflicts that have occured in recent years lead us to believe that there are interesting discoveries to be made. For the scope of our project, we will look into the civil war that occured in Lebanon.

## Research questions

- How and why have war impacted the overall agricultural production of crops in Lebanon? 

  - We chose to only focus on crops as the data on import/export had too many missing data points. We will focus on a a single country in order to obtain meaningful results. Wars are too unique and have too many variables to obtain meaningful results by attempting to generalize over a large quantity of them. We want to see if, at least for a specific case, we can observe a correlation and explain the reason behind it.

- How and why have war changed the food produced in Lebanon?

  - We want to grasp, for the most important crops, the trends in their production and guess why the production has oriented itself in this direction

## Dataset

- [Global Food & Agriculture Statistics](https://www.kaggle.com/unitednations/global-food-agriculture-statistics): We are using this dataset to see how agriculture changed before, during and after wars (e.g. crops and livestock production)

- [Wikidata Query Service](https://query.wikidata.org/): We are using this dataset to obtain information about wars (e.g. place, actors involved, start and end dates). Initially, we were only going to use the Uppsala dataset for this purpose, but we found Wikidata to have more complete and relevant information. The query we are making can be found in [get_wiki_data.py](src/get_wiki_data.py) file.

- [Lebanon Historical Conflict Mapping and Analysis by Civil Society Knowledge Centre](https://civilsociety-centre.org/ictj/map):We are using this to visualize where the events occurred, year-by-year 

## A list of internal milestones up until project milestone 3

- Finalize any correlations we have chosen for our data story (deadline 05.12.19)

  - Further analyse Afghanistan and Lebanon based on how they were affected by wars.

  - From these countries, determine causes of the correlations we are seeing.

  - Categorize each war of interest in the selected countries.    

- Data story write-up and visualization creation (deadline 16.12.19)

  - Create meaningful visualizations of the correlations we found.

  - Write the story.

- Create article to tell our story. (deadline 19.12.19)

  - Present our visualization and story in the format of our choice.

- Final review of data story and submission (deadline 20.12.19)

  - As a group, final review of our story.

  - Submit Milestone 3