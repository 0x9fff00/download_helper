# Copyright (C) 2017 0x9fff00

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
from downloaders import curseforge, mediafire
print(curseforge.get_data('advanced-rocketry', '1.10.2', 'Beta'))
print(curseforge.get_data('rftools', '1.10.2', 'Beta'))
print(curseforge.get_url('rftools', '1.7.10', 'Release'))
print(mediafire.get_url('http://www.mediafire.com/file/2czafa60rh4ajhj/mcp908.zip'))
