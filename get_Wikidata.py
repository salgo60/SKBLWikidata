""" Search for a record in Wikidata with value SKBLurl in Property P4963 and retrieves ISNI in Property P213
"""
from dataclasses import dataclass
import pywikibot as pwb
from pywikibot import pagegenerators as pg
import urllib.request,json
from wikidataintegrator import wdi_core
import logging

logger = logging.getLogger(__name__)

def get_WDSKBL(SKBLurl):
    import logging
    from dataclasses import dataclass
    from wikidataintegrator import wdi_core

class WikiData:
    ID: str = ""
    ISNI: str = ""


def get_WD(SKBLurl):
    """ SPARQL search using SKBLurl
    :rtype: Wikidata object id, ISNI value"""
    WDobj =""
    ISNIvalue = ""
    query = 'SELECT ?item ?ISNI WHERE { ?item  wdt:P4963 "' + str(SKBLurl) + '". OPTIONAL {?item  wdt:P213 ?ISNI}}'
    site = pwb.Site("wikidata", "wikidata")
    repo = site.data_repository()
    generator = pg.WikidataSPARQLPageGenerator(query, site=site)
    try:
        result = wdi_core.WDItemEngine.execute_sparql_query(query)
        if len(result['results']['bindings']):
            WDobj = result['results']['bindings'][0]['item']['value'].replace("http://www.wikidata.org/entity/","")
            if 'ISNI' in (result['results']['bindings'][0]):
               ISNIvalue = result['results']['bindings'][0]['ISNI']['value']
            logger.info("\t\tWD object = %s ,  WDISNI = %s", WDobj, ISNIvalue)
    except:
        logger.exception("WD read")
    finally:
        pass
    return WDobj, ISNIvalue

