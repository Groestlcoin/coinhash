import hashlib

def SHA256dHash(x):
    return hashlib.sha256(hashlib.sha256(x).digest()).digest()

from neoscrypt import getPoWHash as NeoscryptHash
from skeinhash import getPoWHash as SkeinHash
from qubit_hash import getPoWHash as QubitHash
from groestlcoin_hash import getHash as GroestlHash
from darkcoin_hash import getPoWHash as X11Hash
from ltc_scrypt import getPoWHash as ScryptHash
