# Copyright (C) 2017-2018 0x9fff00

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
import re
import warnings

from downloaders import curseforge


def get_data(mod, mc_version, release_phase):
    warnings.warn('curseforge_minecraft.get_data is deprecated. Use curseforge.get_data instead.', DeprecationWarning)

    if re.match(r'^\d+.\d+$', mc_version):
        raise NotImplementedError('Minecraft versions with wildcard PATCH versions are no longer supported.')

    new_data = curseforge.get_data(curseforge.addon_slug_to_id('mc', mod), mc_version, release_phase)

    return {
        'url': new_data['url'],
        'name': new_data['file_name'],
        'time': int(new_data['time']),
        'release_phase': new_data['extra']['release_type']
    }


def get_url(mod, mc_version, release_phase):
    warnings.warn('curseforge_minecraft.get_url is deprecated. Use curseforge.get_url instead.', DeprecationWarning)
    return get_data(mod, mc_version, release_phase)['url']
