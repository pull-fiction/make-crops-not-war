---
title: Make Crops, not War!
layout: page
feature_image: "assets/img/cover-diagonal.svg"
feature_text:
---

## War Vs. <span style="color:RGB(144,167,129)">Agriculture</span>

What are the effects of war on agriculture production? How does it change the way you eat?

History textbooks clearly describe how wars affect a country's economy, social structure and politics. However, the impact on agricultural production have not been studied to the same extent. We are intrigued by this, as it concerns a fundamental necessity for survival: **food**. We will attempt to shed some light on this question through an analysis of data obtained from the following sources:

* [Global Food & Agriculture Statistics](http://www.fao.org/faostat/en/#data).
* [Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page).
* [Lebanon Historical Conflict Mapping and Analysis](https://civilsociety-centre.org/ictj/map/hist/map) by Civil Society Knowledge Centre.

We will begin by exploring the data on a **global level** to seek general correlations before diving deeper into a specific **case study**. Armed conflicts are extremely complex and unique in an unlimited number of ways; it is simply impossible to fully grasp the impacts of war on each country with a global overview. Through an in depth case study, we aim to provide one example of how an armed conflict can impact a country's agriculture. This analysis will help us grasp the sheer magnitude of factors that can potentially come into play when dealing with wars.

We are going to explore **how production changes** and, consequently, trace back **food consumption** at wartime. *Follow us along, you'll discover that worldwide, even in dark times, food is and remains the most valuable social good.* **<-- Not sure about this sentence.**

## How war tastes around the world

To begin, let's take a look at agricultural production growth during periods of conflict and compare them with periods of peace. The following plot illustrates this relationship by using the growth rate during peace on the Y-axis and the rate during war on the X-axis. Each dot represents a country and the color of the dots shows the total amount of years the countries has been in conflict during the timeframe our data. It should be noted that countries who have not experienced conflicts within their territories are not being considered in this plot. **HERE DO WE WANT TO USE TEXT OR LIST TO DESCRIBE THE PLOT?**

* Every dot represents a country that has had war in its territory;
* On the X-axis there's the average rate of change of crop production in wartime;
* On the Y-axis, instead, the average rate of change of crop production in peace;
* The rates of change are shown in percentages;
* The color represents the number of years in war.

<iframe class="plot" src="assets/plots/crop-rate.html"></iframe>

As expected, the majority of countries experience positive crop production growth during peaceful periods. In contrast, the rates during periods of conflict are quite unexpected. As can be seen on the plot, countries tend to experience more extreme changes during times of conflict, whether it be growth or decline. Interestingly, the countries with negative growth rates during conflicts are mainly countries that have not endured many years in war. It is possible that countries that are more frequently in conflict have developed better strategies to protect their agricultural production.

Now, let's continue our investigation country-wise. These last 60 years have been the most peaceful time our world has ever experienced. But did you know we have had 111 wars? The plot below shows the **evolution of total crop production** of each country. The years during which a country was in conflict are displayed in red.

<iframe class="plot" src="assets/plots/crops-vs-year2.html"></iframe>

Clearly, different countries exhibit **wildly different behaviours**. Even the very same country has very different trends in different wars (like, for example, Afghanistan: you can check it on the plot above).

## A case study: Lebanon

We got particularly curious about **Lebanon**. This small Middle-east country has suffered quite a brutal civil war, and not a short one (1975-1990). Despite that, its production **increases** steeply during the conflict. Moreover, the considerable length of the conflict and the fact that it falls nicely in the middle of our food data time frame makes it ideal for our case study. Let's first take another look at the evolution of Lebanon's crop production.


<iframe class="plot" src="assets/plots/leb-crops-vs-year.html"></iframe>



## The background

The scope of our research is not to give an exhaustive description of the war events, nor their cause. For our goal, it suffices to mention that for *15 years*, a country already burdened by *ethnical, religious and political divisions* had to endure a conflict between more than *22 different militias*. This, along with the *ingerence* from Syria, Israel and Palestine has led to approximately **120.000 fatalities**.

## The setting

In order to determine what may have caused the agricultural production to rise, we must first obtain a better understanding of Lebanon's agricultural land distribution. The following map shows the total hectares of land dedicated to agriculture in each of Lebanon's governates (1998?)[^1]. In addition, the locations of the **main events of Lebanese Civil War** have been overlayed onto the map.

<iframe class="plot_ani" src="assets/plots/map-agri-war-leb3.html"></iframe>

What immediately caught our eyes is the disconnect between areas of heavy agricultural production and those of battles. The civil war mainly affected the urban areas, especially the capital Beirut. Nowadays, Beirut hosts more than one third of the population of Lebanon [^2] [^3] and we suspect there was a similar distribution before the war. On the other hand, the most productive area of the country is located in the valleys of Beqaa.

## Our theory...

We believe that the increased production is linked to **internal migration**. As the situation in the cities worsened, some people emigrated out of the country [^4], but others fled to the safer eastern areas, where they had to join the agricultural workforce. It is unlikely that the growth in production can be explained by technological improvements, especially during a civil war where governmental funding would likely be focused in other areas. Hence, it is our opinion that the rise in agricultural output is directly linked to the increase in labor in the sector.

Here is the trend of the **population in Beirut** [^5], between 1950 until today.

<iframe class="plot" src="assets/plots/beirut-population.html"></iframe>

There is a clear change in trend during the years of the civil war as the upward trend completely stops and even decreases during the second half of the war. The return to normal levels of growth directly after the war strongly indicates that the conflict was responsible for this shift in trends.

The following map displays the percentage of **buildings erected** that were erected during the years of the war [^6]. This data was taken in 2007??.

<iframe class="plot_map" src="assets/plots/map-infra-leb2.html"></iframe>

Clearly, rural areas stand out, with percentages of new buildings reaching up to 52%, suggesting the **need of infrastructure for the growing population of these areas**.

Moreover, according to the *CIA World Factbook* [^7], in 2012 there were still 76,000 people internally displaced, due to the Civil War.

From the following table  [^8], we can also observe how the **percentage of Lebanon's GDP represented by agriculture** doubles during the war years, suggesting that working people potentially moved to agriculture from other econonomic sectors.

| Year                        | 1973 | 1974 | 1985 | 1988 | 1990 |
|-----------------------------|:----:|:----:|:----:|:----:|:----:|
| Share of agriculture to GDP |  9%  |  9%  |  <span style="color:RGB(232,90,79)">15%</span> |  <span style="color:RGB(232,90,79)">20%</span> |  <span style="color:RGB(232,90,79)">23%</span> |

<br>

As stated by Atif Abdallah Kubursi in his work *"Lebanon's Agricultural Potential: A Policy Analysis Matrix Approach"* (McMaster University and Econometric Research limited), the "agricultural sector acted as a **buffer sector** which absorbed large numbers of people from the urban areas that sought refuge in the rural areas" [^9].

## How production changes

We will get now in even more detail, as just knowing that the production increased is not enough. How does it change? Do all the different crops change in the same way, to the same amount?

Here is a graph depicting the **growth**, given in percentage, of **different kind of crops** through the war years.
To scale the production of different crops we used the *MinMax transformation* for all the crops that do not have missing values during 1975-1990. After that we picked only top-10 crops in the boundary years for the sake of clarity. Hence, the scores on the Y-axis indicates the percentage of the specific crop production relative to the maxim value (Orange production in 1990). Moreover, to overcome the noise introduced by the natural crop cyclic variation, the plot is on a *quinquennial base*.


<div class="flourish-embed" data-src="visualisation/1126355"></div><script src="https://public.flourish.studio/resources/embed.js"></script>

If we first look at the **score** graph, there’s already something worth noting:

* *Potatoes* have caught up *grapes*, *tomatoes* have caught up *apples*
* *Cucumber* are growing quite fast while *bananas* and *lemons* are almost stable

The **rank** graph is even more interesting. For each year studied, it shows the top crops produced. We can appreciate that

* Most of the crops preserved their relative position with *oranges* firmly holding the first position
* *Potatoes* gained a good 7 positions!
* *Onions* ranked a bit better, and finally obtained a position in the top 10 crops produced
* *Lemons*, *apples* and *bananas* performances are declining
* *Cucumbers* are ranking better


## Why production changes

Considering that these changes did not result in a enhanced **export** [^10]  ADD IMPORT/EXPORT IMAGE AS SOURCE, we suppose that, indeed, they mainly affected internal consumption. In particular, we observe that Lebanon agriculture **slightly changed**.

Before the war, the agricultural sector deeply relied on citrus fruits and **typical Mediterranean cultivations** such as olives, oranges, apples, lemons. After the war, those cultivations are still there and don’t experience major changes. In fact, all of the above are **trees** and therefore human labour cannot really have an impact on their production. What can experience changes are, instead, **cultivated crops**. From the previous analysis, we can appreciate that potatoes, tomatoes, cucumber, and onions are all preferred over sugar beet. What all of this crops have in common? They are **easy to produce, eat and store**, as well as **highly nutritious**. They suit better, therefore, in a poor war scenario.

## What have we learned?

<iframe class="plot_img" src="assets/plots/potatoes.jpg"></iframe>

In a unique way, war has revitalized an initially weak sector at the expense of others in Lebanon. This is not to say that wars are desirable in any way. It just served to show one example of how wars can impact the agriculture sector.
We might indeed conclude that in the overall Lebanese economy, agriculture was **not exploited at its best**. Unveiling this link and revealing the full potential of lebanese agriculture could turn into an **insightful result** for the government: it could show an effective strategy for a general economic development.

Secondly, although our analysis is not general, it helped to shown that along with deaths and destructions, war can also bring major changes in **people's everyday life**. It can not only invade your country, but also, and more remarkably, your personal sphere, causing you to take decisions you wouldn't have taken otherwise. In Lebanon case, it has also caused people **orienting their eating habits** towards a differnt, more basic diet.




## References

[^1]: From "Atlas du Liban: Territoires et société" by Éric Verdeil, Ghaleb Faour and Sébastien Velut. Institut français du Proche-Orient /CNRS Liban (2007). The maps refers to year 1998, but we assumed no major changes to the quality of soil, nor to the environmental and climatic factors would have occured during the war. Therefore, it is still coherent with our analysis.

[^2]: [Beirut population](https://en.wikipedia.org/wiki/Beirut)

[^3]: [Lebanon population](https://en.wikipedia.org/wiki/Lebanon)

[^4]: From "Atlas du Liban: Territoires et société" by Éric Verdeil, Ghaleb Faour and Sébastien Velut. Institut français du Proche-Orient /CNRS Liban (2007).

[^5]: [Beirut Population](http://worldpopulationreview.com/world-cities/beirut-population/)

[^6]: "Things Fall Apart: Containing the Spillover from an Iraqi Civil War" By Daniel Byman, Kenneth Michael Pollack, Page. 139

[^7]: CIA World Factbook. "CIA World Factbook: Lebanon: Refugees and internally displaced persons". CIA World Factbook, 10 September 2012.

[^8]: Bank of Lebanon, Central Statistical Office Annual Reports and Anahar Lebanese statistics, various issues

[^9]: Atif Abdallah Kubursi "Lebanon's Agricultural Potential: A Policy Analysis Matrix Approach"* (McMaster University and Econometric Research limited)

[^10]: COOL PLOT HERE
