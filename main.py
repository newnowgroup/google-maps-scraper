from src import Gmaps
import os

path_root = os.getenv("ONEDRIVE_PATH")
if not os.path.isdir(path_root):
    raise "you do not have the ONEDRIVE_PATH environment variable set up. Please set it up first."

path_root = os.path.join(path_root, 'additionals')
if not os.path.isdir(path_root):
    os.mkdir(path_root)

# iterate accross all german cities
queries = Gmaps.Cities.Germany("'WMF'")

# iterate accross all countries where there are WMF stores
queries.extend(["'WMF' Switzerland",
                "'WMF' Netherlands",
                "'WMF' Austria",
                "'WMF' France",
                "'WMF' Portugal",])

# scrape additional stores that were missed in the previous scraping
queries.extend(['WMF Filiale Klagenfurt',
                'WMF Filiale Dornbirn',
                'Kaiser Werksverkauf',
                'Silit Werksverkauf'])

Gmaps.places(queries, scrape_reviews=True, reviews_max=Gmaps.ALL_REVIEWS,
             convert_to_english=False, path=os.path.join(path_root, 'gmaps_scraping'),
             lang=Gmaps.Lang.English)
