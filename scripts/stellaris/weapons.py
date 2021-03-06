import _initpath
import pyradox.config
import pyradox.csv
import os

weapon_path = os.path.join(
    pyradox.config.basedirs['Stellaris'],
    'common',
    'component_templates',
    'weapon_components.csv')

data = pyradox.csv.parse_file(weapon_path)

print(data.to_wiki())
f = open('out/weapons.csv', 'w')
f.write(data.to_csv())
f.close()
