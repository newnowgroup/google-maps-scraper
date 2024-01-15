from src import Gmaps
import os

path_root = os.getenv("ONEDRIVE_PATH")
if not os.path.isdir(path_root):
    raise "you do not have the ONEDRIVE_PATH environment variable set up. Please set it up first."

queries = ["WMF"]

Gmaps.places(queries, scrape_reviews=True, reviews_max=Gmaps.ALL_REVIEWS,
             convert_to_english=False, path=path_root)
