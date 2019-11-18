# pip install sparqlwrapper
# https://rdflib.github.io/sparqlwrapper/

from SPARQLWrapper import SPARQLWrapper, JSON

endpoint_url = "https://query.wikidata.org/sparql"

query = """
SELECT DISTINCT ?armed_conflictLabel ?start_year ?end_year ?participantLabel ?countryWarLabel ?locationLabel
{
  # Get all the armed conflicts
  # (wdt:P31/wdt:P279*) means instance of
  # wd:Q350604 is armed conflict
  ?armed_conflict (wdt:P31/wdt:P279*)  wd:Q350604;
                   wdt:P580 ?start_time;
                   wdt:P710 ?participant.
  
  OPTIONAL { ?armed_conflict wdt:P582 ?end_time. }
  
  # Get start and end years
  BIND(YEAR(?start_time) AS ?start_year) hint:Prior hint:rangeSafe true.
  BIND(YEAR(?end_time) AS ?end_year) hint:Prior hint:rangeSafe true.
  
  # Remove the wars that started before FAOs DB
  FILTER(?start_year >= (1961))
  
  MINUS {
    ?armed_conflict (wdt:P31/wdt:P279*) wd:Q864113 # exclude if is a proxy war
  }
  
  ?participant (wdt:P31/wdt:P279*) wd:Q7210356.
  
  # Get the location of the conflict (if present)
  OPTIONAL { ?armed_conflict wdt:P276 [ wdt:P17 ?countryWar]. }
  OPTIONAL { ?armed_conflict wdt:P276 ?location. }
  
  
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
"""


def get_results(endpoint_url, query):
    sparql = SPARQLWrapper(endpoint_url)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()


results = get_results(endpoint_url, query)

for result in results["results"]["bindings"]:
    print(result)
