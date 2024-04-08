from src import Gmaps
import os

path_root = os.getenv("ONEDRIVE_PATH")
if not os.path.isdir(path_root):
    raise "you do not have the ONEDRIVE_PATH environment variable set up. Please set it up first."

path_root = os.path.join(path_root, 'competitors')
if not os.path.isdir(path_root):
    os.mkdir(path_root)

# LeCreuset stores
leCreuset_stores = ['Wertheim Village',
                    'Designer Outlets Wolfsburg',
                    'LE CREUSET Mannheim',
                    'Ingolstadt Village',
                    'Designer Outlet Soltau',
                    'LE CREUSET Münster',
                    'LE CREUSET Stuttgart',
                    'LE CREUSET Berlin',
                    'LE CREUSET Bonn',
                    'LE CREUSET Cologne',
                    'Outlet City Metzingen',
                    'LE CREUSET Bremen',
                    'LE CREUSET Düsseldorf',
                    'Zweibrücken Fashion Outlet',
                    'LE CREUSET Munich',
                    'LE CREUSET Hamburg',
                    'LE CREUSET Trier',
                    'Designer Outlet Neumünster']

# Zwilling
zwilling_stores = ['ZWILLING Shop Munich',
                   'ZWILLING Outlet Ingolstadt',
                   'ZWILLING Outlet Wertheim',
                   'ZWILLING Shop Zweibrücken',
                   'ZWILLING Shop Frankfurt',
                   'ZWILLING Shop Cologne',
                   'ZWILLING Shop Solingen',
                   'ZWILLING Shop Düsseldorf',
                   'ZWILLING Shop Berlin',
                   'ZWILLING Outlet Wustermark',
                   'ZWILLING Outlet Neumünster']


# Fissler
fissler_stores = ['Fissler Store Berlin Köpenick',
                  'Fissler Store Berlin Wedding',
                  'Fissler Store Frankfurt City',
                  'Fissler Store Frankfurt North West Center',
                  'Fissler Store Hamburg',
                  'Fissler Store Kempten',
                  'Fissler Store Karlsruhe',
                  'Fissler Store Koblenz',
                  'Fissler Store Constancy',
                  'Fissler Store Leverkusen',
                  'Fissler Store Lüdenscheid',
                  'Fissler Store Mainz',
                  'Fissler Store Muenster',
                  'Fissler Store Neu Isenburg',
                  'Fissler Store Nuremberg',
                  'Fissler Store regensburg',
                  'Fissler Store Win',
                  'Fissler Store Wetzlar',
                  'Fissler Store Wiesbaden',
                  'Fissler Store Wildau',
                  'Fissler Store Würzburg',]


# Roesle
# NOTE: Metzingen and Halle Leipzig stores not found go gmaps
roesle_stores = ['RÖSLE GmbH & Co. KG - Outlet Berlin',
                 'RÖSLE GmbH & Co. KG - Outlet Ochtrup',
                 'RÖSLE GmbH & Co. KG - Outlet Neumünster',
                 'RÖSLE GmbH & Co. KG - Outlet Rostock',
                 'RÖSLE GmbH & Co. KG - Outlet MARKTOBERDORF',]

queries = leCreuset_stores #+ zwilling_stores + fissler_stores + roesle_stores

Gmaps.places(queries, scrape_reviews=True, reviews_max=Gmaps.ALL_REVIEWS,
             convert_to_english=False, path=os.path.join(path_root, 'gmaps_scraping'),
             lang=Gmaps.Lang.English, max=1)
