# -*- coding: utf-8 -*-
# Copyright (C) 2010 Bastian Kleineidam
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
"""Archive commands for the xz program."""
from patoolib import util


def extract_xz (archive, encoding, cmd, **kwargs):
    """Extract a XZ archive."""
    cmdlist = [util.shell_quote(cmd)]
    if kwargs['verbose']:
        cmdlist.append('-v')
    outfile = util.get_single_outfile(kwargs['outdir'], archive)
    cmdlist.extend(['-c', '-d', '--', util.shell_quote(archive), '>',
        util.shell_quote(outfile)])
    # note that for shell calls the command must be a string
    return (" ".join(cmdlist), {'shell': True})

def test_xz (archive, encoding, cmd, **kwargs):
    """Test a XZ archive."""
    cmdlist = [cmd]
    if kwargs['verbose']:
        cmdlist.append('-v')
    cmdlist.extend(['-t', '--', archive])
    return cmdlist

def create_xz (archive, encoding, cmd, *args, **kwargs):
    """Create a XZ archive."""
    cmdlist = [util.shell_quote(cmd)]
    if kwargs['verbose']:
        cmdlist.append('-v')
    cmdlist.append('-c')
    cmdlist.append('--')
    cmdlist.extend([util.shell_quote(x) for x in args])
    cmdlist.extend(['>', util.shell_quote(archive)])
    # note that for shell calls the command must be a string
    return (" ".join(cmdlist), {'shell': True})
