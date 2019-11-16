import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np

def year_in_war(country_wars, year_row):
    year = year_row['year']
    
    for index, war_row in country_wars.iterrows():
        if war_row['start_year'] <= year <= war_row['end_year']:
            return True
    
    return False

def country_in_war(wars_df, prod_per_year_per_country, country):
    country_wars = (
        wars_df[wars_df['country'].str.contains(country)]
            .groupby(['name', 'start_year', 'end_year'])
            .sum()
            .reset_index()
            .drop('state', axis=1)
    )
    
    country_crops = (
        prod_per_year_per_country[prod_per_year_per_country['country'] == country]
            .drop('country', axis=1)
    )
    
    country_crops['in_war'] = country_crops.apply(lambda row: year_in_war(country_wars, row), axis=1)
    
    return country_crops

def plot_production_and_war(wars_df, prod_per_year_per_country, country):
    
    country_prod_war = country_in_war(wars_df, prod_per_year_per_country, country)


    country_prod_war['war_value'] = np.where(country_prod_war['in_war'], country_prod_war['value'], np.NaN)
    country_prod_war['non_war_value'] = np.where(~country_prod_war['in_war'], country_prod_war['value'], np.NaN)

    f, ax = plt.subplots(1, 1, figsize=(10, 5))
    plt.title(f'Total production of crops in {country}')
    ax.plot_date(country_prod_war['year'], country_prod_war['war_value'], color='red', label='war years', linestyle="-", xdate=True)
    ax.plot_date(country_prod_war['year'], country_prod_war['non_war_value'], color='blue', label='non-war years', linestyle="-", xdate=True)
    plt.xlabel('year')
    plt.ylabel('total crops production')
    ax.legend()