# Make crops, not war

# Abstract

The impacts of war on a country’s economy, social structure and politics are generally well documented and understood. However, impact on food and crop production has not been studied to the same extent. Through a brief literature research, it has been found that most papers about the topic are quite outdated. Our intention is to fill in this gap through an analysis of the UN Dataset on Food Production in conjunction with war data obtained through WikiData and the UCDP Armed Conflict Dataset. The increased globalization of food markets along with the amount of significant armed conflicts that have occured in recent years lead us to believe that there are interesting discoveries to be made. Initially, the effects of war on total agricultural production within the countries where conflicts have taken place will be analysed. Then, we will select a few countries with interesting fluctuations in their agricultural and livestock productions and dig deeper into these cases.

# Research questions

- How does war impact the production of crops and livestock?
- What can cause an impact? Is there any difference in the impact of symmetric and asymmetric warfare, or state and non-state warfare?
- How different is the impact of war on the countries the war is located in and in the other countries that are involved in the war (e.g. the US in Afghanistan War)?
- Has war a different impact in different zones of the world?
- If there’s a significant change in agricultural production due to war, is it temporary or it stabilizes with time?

# Dataset

- [Global Food & Agriculture Statistics](https://www.kaggle.com/unitednations/global-food-agriculture-statistics): we are using this dataset to see how agriculture changed before, during and after wars (e.g. crops and livestock production, export, import)
- [Wikidata Query Service](https://query.wikidata.org/): We are using this dataset to obtain information about wars (e.g. place, actors involved, start and end dates). Initially, we were only going to use the Uppsala dataset for this purpose, but we found Wikidata to have more complete and relevant information.
- [Uppsala Conflict Data Program/PRIO Armed Conflict Dataset](https://ucdp.uu.se/): We will now only refer to this dataset as a complement to the data we obtained using Wikidata. It contains interesting data about the severity of different armed conflicts that may be useful when categorizing the wars which we will analyse.

# A list of internal milestones up until project milestone 2

- Data acquisition (deadline 04.11.19)
    - Set up a framework in order to efficiently work using the cluster.
    - Determine which data will be relevant to our questions along with the level of detail that will be required.
    - Create a sub-dataset in order to be able to work locally on our machines.
- Data transformation (deadline 18.11.19)
    - Choose which wars to analyze.
    - Look for correlations, and write an analysis on the Jupyter Notebook.
- Data visualization (deadline 25.11.19)
    - Produce basic visualizations to clearly convey our findings.
    - Formulate a general concept of our data story.

# Questions for TAs

- Is it better to cherry-pick just some wars in order to get a good representations of wars around the world, or somehow analyze all the wars that are in the dataset?
- Which are the UN's dataset tables that could be more useful?
