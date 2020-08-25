from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND

from SPARQLWrapper import SPARQLWrapper, JSON


# noinspection PyUnusedLocal
class ListPokemon(APIView):
    """
   View to list all the pokemon from wiki data.
    """
    def get(self, request, format=None):
        """
        Returns a list of all the pokemon using a sparql query on wiki data.
        """
        sparql = SPARQLWrapper("https://query.wikidata.org/sparql", agent='Mozilla/5.0 (Macintosh; Intel Mac OS X '
                                                                          '10_11_5) AppleWebKit/537.36 (KHTML, '
                                                                          'like Gecko) Chrome/50.0.2661.102 '
                                                                          'Safari/537.36')
        sparql.setQuery("""
        #Pokemon!
        #updated 2019-01-21

        # Gotta catch 'em all
        SELECT DISTINCT ?pokemon ?pokemonLabel ?pokedexNumber
        WHERE
        {
            ?pokemon wdt:P31/wdt:P279* wd:Q3966183 .
            ?pokemon p:P1685 ?statement.
            ?statement ps:P1685 ?pokedexNumber;
                      pq:P972 wd:Q20005020.
            FILTER ( !isBLANK(?pokedexNumber) ) .
            SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en" }
        }
        ORDER BY (?pokedexNumber)
        """)
        sparql.setReturnFormat(JSON)
        result = self.normalize(sparql.query().convert())

        return Response(result, status=HTTP_200_OK)

    def normalize(self, result):
        bindings = result['results']['bindings']
        new_result = {
            'pokemon': [],
        }

        for pokemon in bindings:
            new_result['pokemon'].append({
                'wiki_url': pokemon['pokemon']['value'],
                'name': pokemon['pokemonLabel']['value'],
                'pokedex': pokemon['pokedexNumber']['value'],
            })

        return new_result


# noinspection PyUnusedLocal
class GetPokemon(APIView):
    """
    View to get a single pokemon based on a pokedex number.
    """
    def get(self, request, pk, format=None):
        """
        Returns a single or no pokemon based on the specified pokedex
        using a sparql query on wiki data.
        """
        sparql = SPARQLWrapper("https://query.wikidata.org/sparql", agent='Mozilla/5.0 (Macintosh; Intel Mac OS X '
                                                                          '10_11_5) AppleWebKit/537.36 (KHTML, '
                                                                          'like Gecko) Chrome/50.0.2661.102 '
                                                                          'Safari/537.36')
        sparql.setQuery("""
        #Pokemon!
        #updated 2019-01-21

        # Gotta catch 'em all
        SELECT DISTINCT ?pokemon ?pokemonLabel ?pokedexNumber
        WHERE
        {
          ?pokemon wdt:P31/wdt:P279* wd:Q3966183 .
          ?pokemon p:P1685 ?statement.
          ?statement ps:P1685 ?pokedexNumber;
                     pq:P972 wd:Q20005020.

          FILTER ( !isBLANK(?pokedexNumber) ) .
          FILTER ( ?pokedexNumber = "%s").
          SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en" }
        }
        ORDER BY (?pokedexNumber)
        LIMIT 1
        """ % pk)
        sparql.setReturnFormat(JSON)
        result = self.normalize(sparql.query().convert())

        if result is None:
            return Response(status=HTTP_404_NOT_FOUND)

        return Response(result, status=HTTP_200_OK)

    def normalize(self, result):
        bindings = result['results']['bindings']

        if len(bindings) == 0:
            return None

        pokemon = bindings[0]
        new_result = {
            'wiki_url': pokemon['pokemon']['value'],
            'name': pokemon['pokemonLabel']['value'],
            'pokedex': pokemon['pokedexNumber']['value'],
        }

        return new_result
