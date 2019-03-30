from dataclasses import dataclass
import urllib.request
import json
import logging
import get_Wikidata

logger = logging.getLogger(__name__)


@dataclass
class SKBLWDcontainer:
    """Class for keeping track of SKBL records in KARP and the related WD record
    Attributes
    ----------
    SKBL_URI str
        a string used as an argument in the webslution and the same value as in Wikidata Property P4963
    SKBL_ID str
        ID used by json to access a record in KARP
    WD str
        Wikidata unique Qnumber
    SKBL_ISNI str
        cleaned ISNI number found in KARP all 000000... etc are deleted
    WD_ISNI str
        ISNI number in Wikidata Property P213
    Methods
    -------
    is_same_isni()
        True if WD ISNI and SKBL ISNI is the same
    """

    SKBL_URI: str = ""
    SKBL_ID: str = ""
    WD: str = ""
    SKBL_ISNI: str = ""
    WD_ISNI: str = ""

    def is_same_isni(self) -> bool:
        if self.SKBL_ISNI.replace(" ", "") == self.WD_ISNI.replace(" ", ""):
            return True
        return False


searchURLs = {'https://ws.spraakbanken.gu.se/ws/karp/v4/minientry?mode=skbl&q=extended%7C%7Cand%7Cnamn.search' +
              '%7Cexists&resource=skbl&show=name,lifespan&size=10000&start=0'}


def get_skbl_item(item):
    """ Populate the SKBLWDcontainer from SKBL and Wikidata 
    :rtype: SKBLWDcontainer
    """

    skbl_wd_rec = SKBLWDcontainer(SKBL_ID=item.get('_id', ''))

    skbl_wd_rec.SKBL_ISNI = get_isni(skbl_wd_rec.SKBL_ID)
    skbl_wd_rec.SKBL_URI = get_url(skbl_wd_rec.SKBL_ID)
    skbl_wd_rec.WD, skbl_wd_rec.WD_ISNI = get_Wikidata.get_WD(skbl_wd_rec.SKBL_URI)

    if not skbl_wd_rec.is_same_isni():
        logger.error(
            "Mismatch: http://www.wikidata.org/wiki/%s SKBL: https://skbl.se/sv/artikel/%s.json" +
            "\t\t  WD ISNI: %s SKBL ISNI: %s",
            skbl_wd_rec.WD, skbl_wd_rec.SKBL_ID, skbl_wd_rec.WD_ISNI, skbl_wd_rec.SKBL_ISNI)
    return skbl_wd_rec


def get_isni(skbl_id):
    """ ISNI and clean the ISNI number

    * defined in type and have id
    * can have 0000000000000000 --> no ISNI
    * can have type but no value

    Warning
    -------
    * if isni is 0000000000000000
    * if type is not found
    """

    json_url = "https://skbl.se/sv/artikel/" + skbl_id + ".json"

    isni = ""
    with urllib.request.urlopen(json_url) as url:
        data = json.loads(url.read().decode())
        if 'id' in data:
            for item in data["id"]:
                try:
                    if 'type' in item:
                        if item["type"] == "ISNI":
                            if 'id' in item:
                                if item["id"] == "0000000000000000":
                                    logger.warning("\tSKBLISNI 0000000000000000 %s ", json_url)
                                else:
                                    isni = item["id"]
                                    logger.info("\tSKBLISNI = %s", isni)
                        else:
                            logger.warning("%s missing type  ", json_url)

                except ValueError:
                    logger.exception("Missing ID in JSON")
                    pass
                finally:
                    pass
        else:
            logger.warning("Missing id %s", json_url)
    return isni


def get_url(skbl_id):
    """KARP.URL is the same value as Wikidata has in the SKBL property P4963 """

    json_url = "https://skbl.se/sv/artikel/" + skbl_id + ".json"

    skbl_url = ""
    with urllib.request.urlopen(json_url) as url:
        data = json.loads(url.read().decode())
        if 'url' in data:
            skbl_url = data["url"]
        else:
            logger.warning("Missing url %s", json_url)
    return skbl_url


def get_skbl_records(skbl_items):
    """ loops SKBL
    """
    for search in searchURLs:
        logger.info("Search: %s", search)
        with urllib.request.urlopen(search) as url:
            data = json.loads(url.read().decode())
            for item in data["hits"]["hits"]:
                try:
                    skbl_items.append(get_skbl_item(item))

                except ValueError:
                    logger.exception("Error in get_skbl_records : %s", item)
                    pass
                finally:
                    pass

    return skbl_items
