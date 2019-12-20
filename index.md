---
title: Make Crops, not War!
layout: page
feature_image: "assets/img/cover-diagonal.svg"
feature_text:
---

## War is served

What are the effects of war on agriculture production? How does it change the way you eat?

History textbooks clearly describe how wars affect a country's economy, social structure and politics. However, the impacts on agricultural production have not been studied to the same extent. We are intrigued by this, as it concerns a fundamental necessity for survival: food. We will attempt to shed some light on this question through an analysis of data obtained from the following sources:

* Global Food & Agriculture Statistics.
* Uppsala Conflict Data Program/PRIO Armed Conflict Dataset.
* Wikidata Query Service.

We will begin by exploring the data on a global level to seek general correlations before delving deeper into a specific case study. Armed conflicts are extremely complex and unique in an unlimited number of ways; it is simply impossible to fully grasp the impacts of war on each country with a global overview. Through an in depth case study, we aim to provide one example of how an armed conflict can impact a country's agriculture. This analysis will help us visualize the sheer magnitude of factors that can potentially come into play when dealing with wars.

We are going to explore how production changes and, consequently, trace back food consumption at wartime. Follow us along, you'll discover that worldwide, even in dark times, food is and remains the most valuable social good.

## How war tastes around the world

First, it is possible to observe a plot that allows to get a global view of the effects of war on countries crop production. It is possible to read it in this way:

* Every dot represents a country that has had war in its territory;
* On the X-axis there's the average rate of change of crop production in wartime;
* On the Y-axis, instead, the average rate of change of crop production in peace;
* The production is normalized according to both country size and population to allow a more fair comparison;
* The rates of change are shown in percentages;
* The color represents the number of years in war.

<iframe class="plot" src="assets/plots/crop-rate.html"></iframe>

As expected, during peace, the majority of countries experience positive crop production growth. However, the obtained result during times of war is quite unexpected. One would be led to believe that a country’s crop production would generally decrease in periods of conflict within its boundaries. The rates during periods of conflict are substantially polarized (between -4% and +4%). Interestingly, the countries with negative growth rates during conflicts are mainly countries that have not experienced many years in war. It is possible that countries that are more frequently in conflict have developed better strategies to protect their agricultural production.



So we will continue our investigation country-wise.
These last 60 years have been the most peaceful time our world has ever experienced. But did you know we have had 111 wars? The plot below shows the evolution of total crop production of each country. The years during which a country was in conflict are displayed in red.
We let you find out for yourselves not only the countries involved in war, but also how their conflicts "tasted like" in terms of agricultural production. Prepare to be surprised.

<iframe class="plot" src="assets/plots/crops-vs-year2.html"></iframe>

Clearly, different countries exhibit wildly different behaviours while there are conflicts within their territory. Even the very same country has very different trends in different wars (like, for example, Afghanistan, it is possibile to check it on the plot above).

## A case study: Lebanon

From your brief analysis, you might have seen something really bizarre. We have too.

<iframe class="plot" src="assets/plots/leb-crops-vs-year.html"></iframe>

We got particularly curious about Lebanon. This little Middle-east country has suffered quite a brutal civil war, and not a short one (1975-1990). Despite that, its production increases weirdly and remarkably during the conflict.

## The background

The scope of our research is not to give an exaustive description of the war events, nor their cause. For our aim, it suffices to say that for 15 years, a country already proven by etnhical, religious and political divisions,  had to also suffer the fight between more than 22 different militias. This, together with the external ingerence from Syria, Israel, Palestine, has led to approximately 120.000 fatalities.

## The setting

In the following plot, it is possible to see where the main events of Lebanese Civil War happened year-by-year. Not only, the underlying green graph shows an overall distribution of agricultural production in the different regions. The darker the colour, the more surface is dedicated to agriculture (given in hundreds of hectares).

<iframe class="plot_ani" src="assets/plots/map-agri-war-leb3.html"></iframe>

What immediately caught our eyes is the completely different localization of the two phenomena. The civil war mainly affected the urban area, especially the capital Beirut that by itself host more than half the population of Lebanon. On the other hand, the productive area of the country is located in the fertile Beqaa's valleys.

## Why production increases

Our best explanation for the increased production is therefore linked to internal migration. As the situation in the cities worsened, some people emigrate, but others fled to the safer eastern areas, where they devoted themselves to agriculture.

The following two graphs help us better visualize what was happening in the urban and rural area, respectively.

Here is the trend of the population in Beirut, between 1950 until today.

<iframe class="plot" src="assets/plots/beirut-population.html"></iframe>

It is quite clear that not only the positive trend stopped with the war, but it turned to negative after 5 years from the beginning.

Moving to the rural area, it is interesting to notice this is the area where the growth of buildings erected during the war is more significant. 

<iframe class="plot_map" src="assets/plots/map-infra-leb2.html"></iframe>


 Our explanation is further substantiated by various sources:

* CIA World Factbook. "CIA World Factbook: Lebanon: Refugees and internally displaced persons" (2012) accounting for approximately 76,000 people displaced within Lebanon;

* The increase in the value added by agriculture to GDP through the war years;
<table>
<colgroup>
<col width="40%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
</colgroup>
<thead>
<tr class="header">
<th>Year</th>
<th>1973</th>
<th>1974</th>
<th>1985</th>
<th>1988</th>
<th>1990</th>
</tr>
</thead>
<tbody>
<tr>
<th markdown="span"><font size="4">Share of agriculture to GDP</font></th>
<td markdown="span">9%</td>
<td markdown="span">9%</td>
<td markdown="span">15%</td>
<td markdown="span">20%</td>
<td markdown="span">23%</td>
</tr>
</tbody>
</table>
* The production curve getting more steep when the war got even tougher with Israel invasion in 1982;

As stated by Atif Abdallah Kubursi in his work "Lebanon's Agricultural Potential: A Policy Analysis Matrix Approach" (McMaster University and Econometric Research limited), the "agricultural sector acted as a buffer sector which absorbed large numbers of people from the urban areas that sought refuge in the rural areas".

## What have we learned?

In a very counterintuitive and special way, war has revitalized an intially weak sector. This is not to say that war are desiderable in any ways. It just served to show that in the overall Lebanese economy, agriculture was not exploited at its best. Unveiling this link and revealing the full potential of lebanese agriculture could turn into an insightful result for institutions: it could indicate an effective strategy for an overall economic development.

## How production changes

We will get now in even more detail. Just knowing that the production increase is not enough. How does it change? All the different crops change in the same way, to the same amount?

Here is a graph depicting the growth, given in percentage, of different kind of crops through the war years. For the sake of clarity,only the most produced crops have been selected and a min-max normalization as been applied. Moreover, to overcome the noise introduced by the natural crop cyclic variation, our analysis would be quinquennial.

<div class="flourish-embed" data-src="visualisation/1121702"></div>
<script src="https://public.flourish.studio/resources/embed.js"></script>

If we first look at the score graph, there’s already something surprising:
* Potatoes have catch up oranges, tomatoes have catch up apples;
* Cucumber are growing quite fast while sugar beet is decreasing;

The rank graph is even more interesting. For each year studied, it shows the top crops produces. We can appreciate that

* Most of the crops preserved their relative position
* Potatoes gained a good 9 positions!
* Onions ranked a bit better, and obtained a position in the top 10 crops produced
* Lemons and olives performances are declining
* Sugar beet, once the second most produced crops, at the end of the war is not even in the 10 ten!


## Why production changes

Considering that all these changes did not result in a enhanced export, we suppose that indeed, they mainly affected internal consumption. In particular, we observe that Lebanon agriculture slightly changed.
Before the war the sector deeply relied on citrus fruits and typical Mediterranean cultivations such as olives, oranges, apples, lemons.
After the war those cultivations are still and don’t experience major changes. In fact all of the above are trees and therefore human labour cannot really have an impact on  their production. What can experience changes are, instead, cultivated crops. From the previous analysis we can appreciate that potatoes, tomatoes, cucumber, onions are all preferred over sugar beet. What all of this  crops have in common? They are easy to produce, eat and store, as well as highly nutritious. They suit better, therefore, in a poor war scenario.

## What have we learned?

Although our analysis is not general, it has served to shown that along with deaths and destructions, war can also bring major changes in people's everyday life. It can not only invade your country, but also and more remarkably your personal sphere, causing you to take decisions you wouldn't have taken otherwise. In Lebanon case, it has also cause people orienting their eating habits towards a differnt, more basic diet.
