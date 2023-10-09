import logging
import sys


class Settings:
    def __init__(self):
        # ------------------------------------------------------------------------------#
        # logging settings
        # ------------------------------------------------------------------------------#
        fmt = "%(asctime)s - [%(levelname)s] - %(module)s:%(funcName)s " "- %(message)s"
        logging_level = logging.INFO
        logging.basicConfig(format=fmt, level=logging_level, stream=sys.stdout)
        self.logger = logging.getLogger(__name__)

        # ------------------------------------------------------------------------------#
        # price settings
        # ------------------------------------------------------------------------------#
        self.max_price = 1500

        # ------------------------------------------------------------------------------#
        # URLs
        # ------------------------------------------------------------------------------#
        self.urls_to_scrape = [
            f"https://www.kleinanzeigen.de/s-wohnung-mieten/steglitz/anzeige:angebote/preis::{self.max_price}/c203l3414+wohnung_mieten.qm_d:65.00%2C+wohnung_mieten.swap_s:nein+wohnung_mieten.zimmer_d:2.5%2C",
            f"https://www.kleinanzeigen.de/s-wohnung-mieten/schoeneberg/anzeige:angebote/preis::{self.max_price}/c203l3414+wohnung_mieten.qm_d:65.00%2C+wohnung_mieten.swap_s:nein+wohnung_mieten.zimmer_d:2.5%2C",
            f"https://www.kleinanzeigen.de/s-wohnung-mieten/wilmersdorf/anzeige:angebote/preis::{self.max_price}/c203l3414+wohnung_mieten.qm_d:65.00%2C+wohnung_mieten.swap_s:nein+wohnung_mieten.zimmer_d:2.5%2C",
            f"https://www.kleinanzeigen.de/s-wohnung-mieten/friedenau/anzeige:angebote/preis::{self.max_price}/c203l3414+wohnung_mieten.qm_d:65.00%2C+wohnung_mieten.swap_s:nein+wohnung_mieten.zimmer_d:2.5%2C"
        ]

        # ------------------------------------------------------------------------------#
        # keywords to exclude
        # ------------------------------------------------------------------------------#
        self.exclude_keywords = [
            "untermiete",
            "sublet",
            "tausch",
            "suche",
            "gesucht",
            "sucht",
            "zwischenmiete",
            "wohngemeinschaft",
            "wg ",
            "lichtenrade",
            "spandau",
            "wedding",
            "pendler",
        ]
