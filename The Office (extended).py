from requests import get
from requests.packages.urllib3 import disable_warnings, exceptions
from bs4 import BeautifulSoup as soup
from subprocess import Popen

disable_warnings(exceptions.InsecureRequestWarning)


media_player = r'C:\Program Files\DAUM\PotPlayer\PotPlayerMini64.exe'

season = input('Enter season [1-9] : ')

season_dir = f"https://office:this is why we can't have nice things@ennben.helios.feralhosting.com/The%20Office/S{season}/"
res = get(season_dir, verify=False)

anchors = map(lambda x: x.string, soup(res.content, features='html5lib').findAll('a'))
episode_names = list(filter(lambda x: x.string.startswith('S0'), anchors))

print()

for index, name in enumerate(episode_names):
    print('%2d. %s' %(index+1, name[:-4]))

episode = int(input(f'\nEnter episode : [1-{len(episode_names)}] : ')) - 1

Popen([media_player, season_dir + episode_names[episode]])
