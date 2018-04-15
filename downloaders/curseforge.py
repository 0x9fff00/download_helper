# Copyright (C) 2018 0x9fff00

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import operator

import dateutil.parser
import dateutil.tz

from .. import util

API_BASE = 'https://cursemeta.dries007.net/api/v2/direct'
API_GET_ADDON_FILES = API_BASE + '/GetAllFilesForAddOn/{addon_id}'
API_GET_MATCH_FROM_SLUG = API_BASE + '/GetRepositoryMatchFromSlug/{game_slug}/{addon_slug}'

RELEASE_TYPE_MAP = {
    'Release': ['Release'],
    'Beta': ['Release', 'Beta'],
    'Alpha': ['Release', 'Beta', 'Alpha'],
}

cache_addon_slug_to_id = {}


def addon_slug_to_id(game_slug, addon_slug):
    if (game_slug, addon_slug) in cache_addon_slug_to_id:
        return cache_addon_slug_to_id[(game_slug, addon_slug)]
    else:
        return_value = \
            util.parse_json_from_url(API_GET_MATCH_FROM_SLUG.format(game_slug=game_slug, addon_slug=addon_slug))['Id']
        cache_addon_slug_to_id[(game_slug, addon_slug)] = return_value
        return return_value


def get_data(addon_id, preferred_game_version, release_type, extra_game_versions=None):
    if extra_game_versions is None:
        extra_game_versions = []

    matches = []
    files = util.parse_json_from_url(API_GET_ADDON_FILES.format(addon_id=addon_id))

    def match_files_for_game_version(game_version):
        for file in files:
            if game_version in file['GameVersion'] and file['ReleaseType'] in RELEASE_TYPE_MAP[release_type] and not \
                    file['IsAlternate']:
                matches.append({
                    'url': file['DownloadURL'],
                    'file_name': file['FileName'],
                    'time': dateutil.parser.isoparse(file['FileDate']).replace(tzinfo=dateutil.tz.tzutc()).timestamp(),
                    'extra': {
                        'release_type': file['ReleaseType'],
                        'game_versions': file['GameVersion'],
                        'dependencies': file['Dependencies'],
                    }
                })

    match_files_for_game_version(preferred_game_version)

    if extra_game_versions:
        version_index = 0
        while not matches:
            if version_index < len(extra_game_versions):
                match_files_for_game_version(extra_game_versions[version_index])
                version_index += 1
            else:
                break

    if not matches:
        return None
    else:
        matches.sort(key=operator.itemgetter('time'), reverse=True)
        return matches[0]


def get_url(addon_id, preferred_game_version, release_type, extra_game_versions=None):
    return get_data(addon_id, preferred_game_version, release_type, extra_game_versions=extra_game_versions)['url']
