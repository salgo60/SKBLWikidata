"""Compare SKBL records in KARP with Wikidata records """
import datetime
import csv
from typing import List
import logging
from get_SKBL import SKBLWDcontainer
import get_SKBL

__version__ = "0.0.1"


def format_skbl_ISNI(SKBL_ISNI):
    ISNI = ""
    if len(SKBL_ISNI):
        ISNI = SKBL_ISNI[:4] + " " + SKBL_ISNI[4:8] + " " + SKBL_ISNI[8:12] + " " + SKBL_ISNI[12:16]
    return ISNI


def main():
    skbl_items: List[SKBLWDcontainer] = []  # Contains SKBL items

    # Create logger
    today = str(datetime.date.today())
    LOG_FORMAT: str = "%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s"
    logging.basicConfig(filename="log/get_skbl_" + today + ".log",
                        level=logging.INFO,
                        format=LOG_FORMAT)

    logger = logging.getLogger()
    # Add terminal logging
    logging.getLogger().addHandler(logging.StreamHandler())
    logger.info("Version %s", __version__)

    logger.info("Start query SKBL")
    get_SKBL.get_skbl_records(skbl_items)

    csv_filename = "skbl.csv"
    with open(csv_filename, 'w', encoding='UTF-8') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL, )
        i = 0
        for i in range(len(skbl_items)):
            wr.writerow([skbl_items[i].SKBL_URI,
                         skbl_items[i].SKBL_ID,
                         format_skbl_ISNI(skbl_items[i].SKBL_ISNI),
                         skbl_items[i].WD,
                         skbl_items[i].WD_ISNI
                         ])

    logger.info("CSV file %s created with SKBL/WD = %s", csv_filename, i + 1)


def get_SKBL_items():
    return get_SKBL_items


if __name__ == "__main__":
    main()



