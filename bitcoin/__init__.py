# Copyright (C) 2012-2018 The python-bitcoinlib developers
#
# This file is part of python-bitcoinlib.
#
# It is subject to the license terms in the LICENSE file found in the top-level
# directory of this distribution.
#
# No part of python-bitcoinlib, including this file, may be copied, modified,
# propagated, or distributed except according to the terms contained in the
# LICENSE file.

from __future__ import absolute_import, division, print_function, unicode_literals

import bitcoin.core

# Note that setup.py can break if __init__.py imports any external
# dependencies, as these might not be installed when setup.py runs. In this
# case __version__ could be moved to a separate version.py and imported here.
__version__ = '0.10.2dev'

class MainParams(bitcoin.core.CoreMainParams):
    MESSAGE_START = b'\xc0\xc0\xc0\xc0'
    DEFAULT_PORT = 8335
    RPC_PORT = 8335
    DNS_SEEDS = (('multidoge.org', 'seed.multidoge.org'),
        ('multidoge.org', 'seed2.multidoge.org'),
        ('denarius.pro','veryseed.denarius.pro'),
        ('denarius.pro','muchseed.denarius.pro'),
        ('denarius.pro','suchseed.denarius.pro'),
        ('dogecoin.com','seed.dogecoin.com'),
        ('dogechain.info','seed.dogechain.info'),
        ('mophides.com','seed.mophides.com'),
        ('dglibrary.org','seed.dglibrary.org'))
    BASE58_PREFIXES = {'PUBKEY_ADDR':30,
                       'SCRIPT_ADDR':22,
                       'SECRET_KEY' :158}    
    BECH32_HRP = ''  

class TestNetParams(bitcoin.core.CoreTestNetParams):
    MESSAGE_START = b'\xfc\xc1\xb7\xdc'
    DEFAULT_PORT = 18335
    RPC_PORT = 18335
    DNS_SEEDS = ()
    BASE58_PREFIXES = {'PUBKEY_ADDR':113,
                       'SCRIPT_ADDR':196,
                       'SECRET_KEY' :241}
    BECH32_HRP = ''

class RegTestParams(bitcoin.core.CoreRegTestParams):
    MESSAGE_START = b'\xfc\xc1\xb7\xdc'
    DEFAULT_PORT = 18335
    RPC_PORT = 18335
    DNS_SEEDS = ()
    BASE58_PREFIXES = {'PUBKEY_ADDR':113,
                       'SCRIPT_ADDR':196,
                       'SECRET_KEY' :241}
    BECH32_HRP = ''

"""Master global setting for what chain params we're using.

However, don't set this directly, use SelectParams() instead so as to set the
bitcoin.core.params correctly too.
"""
#params = bitcoin.core.coreparams = MainParams()
params = MainParams()

def SelectParams(name):
    """Select the chain parameters to use

    name is one of 'mainnet', 'testnet', or 'regtest'

    Default chain is 'mainnet'
    """
    global params
    bitcoin.core._SelectCoreParams(name)
    if name == 'mainnet':
        params = bitcoin.core.coreparams = MainParams()
    elif name == 'testnet':
        params = bitcoin.core.coreparams = TestNetParams()
    elif name == 'regtest':
        params = bitcoin.core.coreparams = RegTestParams()
    else:
        raise ValueError('Unknown chain %r' % name)
