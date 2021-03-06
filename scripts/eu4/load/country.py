import os
import pyradox.format
import pyradox.config
import pyradox.load
import pyradox.struct
import pyradox.txt
import pyradox.yml

parse_countries, get_countries = pyradox.load.load_functions('EU4', 'countries', ('history', 'countries'))

def get_country_name(tag):
    """
    Gets the name a country by its tag according to localization.
    """
    return pyradox.yml.get_localization(tag, ['EU4', 'text', 'countries', 'nw2', 'res_publica', 'aow', 'eldorado', 'tags_phase4'], game = 'EU4')
