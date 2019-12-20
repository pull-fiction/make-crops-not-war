---
title: Make Crops, not War!
layout: page
feature_image: "assets/img/cover-diagonal.svg"
feature_text:
---

## War is served

What are the effects of war on agriculture production? How does it change the way you eat?

History textbooks clearly describe how wars affect a country's economy, social structure and politics. However, the impact on agricultural production have not been studied to the same extent. We are intrigued by this, as it concerns a fundamental necessity for survival: food. We will attempt to shed some light on this question through an analysis of data obtained from the following sources:

* [Global Food & Agriculture Statistics](http://www.fao.org/faostat/en/#data).
* [Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page).
* [Lebanon Historical Conflict Mapping and Analysis](https://civilsociety-centre.org/ictj/map/hist/map) by Civil Society Knowledge Centre.

We will begin by exploring the data on a global level to seek general correlations before diving deeper into a specific case study. Armed conflicts are extremely complex and unique in an unlimited number of ways; it is simply impossible to fully grasp the impacts of war on each country with a global overview. Through an in depth case study, we aim to provide one example of how an armed conflict can impact a country's agriculture. This analysis will help us visualize the sheer magnitude of factors that can potentially come into play when dealing with wars.

We are going to explore how production changes and, consequently, trace back food consumption at wartime. Follow us along, you'll discover that worldwide, even in dark times, food is and remains the most valuable social good.

## How war tastes around the world

First, it is possible to observe a plot that allows to get a global view of the effects of war on countries crop production. It is possible to read it in this way:

* Every dot represents a country that has had war in its territory;
* On the X-axis there's the average rate of change of crop production in wartime;
* On the Y-axis, instead, the average rate of change of crop production in peace;
* The production is normalized according to both country size and population to allow for a more fair comparison;
* The rates of change are shown in percentages;
* The color represents the number of years in war.

<iframe class="plot" src="assets/plots/crop-rate.html"></iframe>

As expected, during peace, the majority of countries experience positive crop production growth. However, the obtained result during times of war is quite unexpected. One would be led to believe that a country’s crop production would generally decrease in periods of conflict within its boundaries. The rates during periods of conflict are substantially confined between -4% and +4%. Interestingly, the countries with negative growth rates during conflicts are mainly countries that have not experienced many years in war. It is possible that countries that are more frequently in conflict have developed better strategies to protect their agricultural production.

Now, let us continue our investigation country-wise. These last 60 years have been the most peaceful time our world has ever experienced. But did you know we have had 111 wars? The plot below shows the evolution of total crop production of each country. The years during which a country was in conflict are displayed in red.
We let you find out for yourselves not only the countries involved in war, but also how their conflicts "tasted like" in terms of agricultural production. Prepare to be surprised.

<iframe class="plot" src="assets/plots/crops-vs-year2.html"></iframe>

Clearly, different countries exhibit wildly different behaviours while there are conflicts within their territory. Even the very same country has very different trends in different wars (like, for example, Afghanistan: you can check it on the plot above).

## A case study: Lebanon

From your brief analysis, you might have seen something really bizarre. We have too.

<iframe class="plot" src="assets/plots/leb-crops-vs-year.html"></iframe>

We got particularly curious about Lebanon. This small Middle-east country has suffered quite a brutal civil war, and not a short one (1975-1990). Despite that, its production increases weirdly and remarkably during the conflict.

## The background

The scope of our research is not to give an exaustive description of the war events, nor their cause. For our aim, it suffices to say that for 15 years, a country already proven by etnhical, religious and political divisions,  had to also suffer the fight between more than 22 different militias. This, together with the external ingerence from Syria, Israel, and Palestine, has led to approximately 120.000 fatalities.

## The setting

In the following plot, it is possible to see where the main events of Lebanese Civil War happened year-by-year. Not only, the underlying green graph shows an overall distribution of agricultural production in the different regions. The darker the colour, the more surface is dedicated to agriculture (given in hectares).

<iframe class="plot_ani" src="assets/plots/map-agri-war-leb3.html"></iframe>

What immediately caught our eyes is the completely different localization of the two phenomena. The civil war mainly affected the urban area, especially the capital Beirut whose urban area, by itself, nowadays hosts more than one third of the population of Lebanon. On the other hand, the productive area of the country is located in the fertile Beqaa's valleys.

## Why production increases

Our best explanation for the increased production is therefore linked to internal migration. As the situation in the cities worsened, some people emigrated out of the country, but others fled to the safer eastern areas, where they devoted themselves to agriculture.

The following two graphs help us better visualize what was happening in the urban and rural area, respectively.

Here is the trend of the population in Beirut, between 1950 until today.

<iframe class="plot" src="assets/plots/beirut-population.html"></iframe>

It is quite clear that not only the positive trend stopped with the war, but it turned to negative after 5 years from the beginning.

In the following plot, we show the percentage of new buildings erected during the years of the war.

<iframe class="plot_map" src="assets/plots/map-infra-leb2.html"></iframe>

Clearly, rural areas stand out, with percentages of new buildings reaching 52%, suggesting the need of houses for people moving there.

Moreover, according to the CIA World Factbook, in 2012 there were still 76,000 people internally displaced, due to the Civil War.

From the following table [SOURCE], we can aslo observe how the percentage of Lebanon's GDP represented by agriculture doubles doring the war years, meaning that working people moved to agriculture from other econonomic sectors.

| Year                        | 1973 | 1974 | 1985 | 1988 | 1990 |
|-----------------------------|:----:|:----:|:----:|:----:|:----:|
| Share of agriculture to GDP |  9%  |  9%  |  15% |  20% |  23% |

<br>

As stated by Atif Abdallah Kubursi in his work "Lebanon's Agricultural Potential: A Policy Analysis Matrix Approach" (McMaster University and Econometric Research limited), the "agricultural sector acted as a buffer sector which absorbed large numbers of people from the urban areas that sought refuge in the rural areas".

## What have we learned?

In a very counterintuitive and special way, war has revitalized an intially weak sector. This is not to say that war are desiderable in any ways. It just served to show that in the overall Lebanese economy, agriculture was not exploited at its best. Unveiling this link and revealing the full potential of lebanese agriculture could turn into an insightful result for the government: it could show an effective strategy for an overall economic development.

## How production changes

We will get now in even more detail, as just knowing that the production increased is not enough. How does it change? Do all the different crops change in the same way, to the same amount?

Here is a graph depicting the growth, given in percentage, of different kind of crops through the war years. For the sake of clarity, only the most produced crops have been selected and a min-max normalization as been applied. Moreover, to overcome the noise introduced by the natural crop cyclic variation, the plot is on a quinquennial base.

<iframe src='https://public.flourish.studio/visualisation/1121702/embed' frameborder='0' scrolling='no' style='width:100%;height:600px;'></iframe><div style='width:100%!;margin-top:4px!important;text-align:right!important;'><a class='flourish-credit' href='https://public.flourish.studio/visualisation/1121702/?utm_source=embed&utm_campaign=visualisation/1121702' target='_top' style='text-decoration:none!important'><img alt='Products viz' src='https://public.flourish.studio/resources/made_with_flourish.svg' style='width:105px!important;height:16px!important;border:none!important;margin:0!important;'> </a></div>

If we first look at the score graph, there’s already something worth noting:

* Potatoes have caught up oranges, tomatoes have caught up apples;
* Cucumber are growing quite fast while sugar beet is decreasing;

The rank graph is even more interesting. For each year studied, it shows the top crops produces. We can appreciate that

* Most of the crops preserved their relative position
* Potatoes gained a good 9 positions!
* Onions ranked a bit better, and obtained a position in the top 10 crops produced
* Lemons and olives performances are declining
* Sugar beet, once the second most produced crops, at the end of the war is not even in the 10 ten!

## Why production changes

Considering that these changes did not result in a enhanced export [ADD IMPORT/EXPORT IMAGE AS SOURCE], we suppose that, indeed, they mainly affected internal consumption. In particular, we observe that Lebanon agriculture slightly changed.

Before the war, the agricultural sector deeply relied on citrus fruits and typical Mediterranean cultivations such as olives, oranges, apples, lemons. After the war, those cultivations are still and don’t experience major changes. In fact, all of the above are trees and therefore human labour cannot really have an impact on their production. What can experience changes are, instead, cultivated crops. From the previous analysis, we can appreciate that potatoes, tomatoes, cucumber, and onions are all preferred over sugar beet. What all of this crops have in common? They are easy to produce, eat and store, as well as highly nutritious. They suit better, therefore, in a poor war scenario.

## What have we learned?

Although our analysis is not general, it helped to shown that along with deaths and destructions, war can also bring major changes in people's everyday life. It can not only invade your country, but also, and more remarkably, your personal sphere, causing you to take decisions you wouldn't have taken otherwise. In Lebanon case, it has also caused people orienting their eating habits towards a differnt, more basic diet.

## References

[1] CIA World Factbook.
