# GNU Typist - improved typing tutor program for UNIX systems
# Copyright (C) 1998  Simon Baldwin (simonb@sco.com)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

#
# Demonstration
#
*:MENU
M: "Demo"
 :PART_1  "Part 1"
 :PART_2  "Part 2"
 :PART_3  "Part 3"
 :EXIT    "Exit"

*:PART_1
B:Part 1
d:type
G:MENU

*:PART_2
B:Part 2
d:Печатать
G:MENU

*:PART_3
B:Part 3
d:type and пeчатать
G:MENU

*:EXIT
X:
