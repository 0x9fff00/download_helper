# Copyright (C) 2017 0x9fff00

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import urllib.request
from bs4 import BeautifulSoup

mc_version_to_filter = {
    '1.7': '1738749986%3A5',
    '1.7.2': '2020709689%3A361',
    '1.7.10': '2020709689%3A4449',
    '1.8': '1738749986%3A4',
    '1.8.0': '2020709689%3A4455',
    '1.8.8': '2020709689%3A5703',
    '1.8.9': '2020709689%3A5806',
    '1.9': '1738749986%3A552',
    '1.9.0': '2020709689%3A5946',
    '1.9.4': '2020709689%3A6084',
    '1.10': '1738749986%3A572',
    '1.10.0': '2020709689%3A6144',
    '1.10.2': '2020709689%3A6170',
    '1.11': '1738749986%3A599',
    '1.11.0': '2020709689%3A6317',
    '1.11.2': '2020709689%3A6452'
}

def get_data(mod, mc_version, release_phase):
    downloads_html = urllib.request.urlopen('https://minecraft.curseforge.com/projects/{}/files?filter-game-version={}'.format(mod, mc_version_to_filter[mc_version])).read()
    downloads_soup = BeautifulSoup(downloads_html, 'html.parser')
    download_soups = downloads_soup.find_all('tr', {'class': 'project-file-list-item'})

    for download_soup in download_soups:
        download_release_phase = download_soup.find('div', {'class': 'release-phase tip'}).get('title')

        if release_phase == download_release_phase or release_phase == 'Alpha' or (release_phase == 'Beta' and download_release_phase == 'Release'):
            time = int(download_soup.find('abbr', {'class': 'tip standard-date standard-datetime'}).get('data-epoch'))
            name = download_soup.find('a', {'class': 'overflow-tip'}).string
            link = download_soup.find('a', {'class': 'button tip fa-icon-download icon-only'}).get('href')

            return {
                'url': 'https://minecraft.curseforge.com' + link,
                'name': name,
                'time': time,
                'release_phase': download_release_phase
            }

def get_url(mod, mc_version, release_phase):
    return get_data(mod, mc_version, release_phase)['url']
