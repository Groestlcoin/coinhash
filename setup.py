from distutils.core import setup, Extension

### Extensions ###

neoscrypt_module = Extension('coinhash.neoscrypt',
                        sources = ['coinhash/neoscrypt/neoscryptmodule.c',
                                    'coinhash/neoscrypt/neoscrypt.c'],
                        include_dirs=['coinhash/neoscrypt'])


skeinhash_module = Extension('coinhash.skeinhash',
                               sources = ['coinhash/skeinhash/skeinmodule.c',
                                          'coinhash/skeinhash/skeinhash.c',
                                          'coinhash/skeinhash/skein.c',
                                          'coinhash/skeinhash/sha2.c'],
                               include_dirs=['coinhash/skeinhash'],
                               extra_compile_args=['-O1'])

qubit_hash_module = Extension('coinhash.qubit_hash',
                               sources = ['coinhash/qubit_hash/qubitmodule.c',
                                          'coinhash/qubit_hash/qubit.c',
                                          'coinhash/qubit_hash/sha3/cubehash.c',
                                          'coinhash/qubit_hash/sha3/echo.c',
                                          'coinhash/qubit_hash/sha3/luffa.c',
                                          'coinhash/qubit_hash/sha3/simd.c',
                                          'coinhash/qubit_hash/sha3/shavite.c'],
                               include_dirs=['coinhash/qubit_hash', 'coinhash/qubit_hash/sha3'])


groestlcoin_hash_module = Extension('coinhash.groestlcoin_hash',
                                sources = ['coinhash/groestl/groestlcoinmodule.c',
                                            'coinhash/groestl/groestl.c'],
                                include_dirs=['coinhash/groestl'])

darkcoin_hash_module = Extension('coinhash.darkcoin_hash',
                                 sources = ['coinhash/darkcoin_hash/darkcoinmodule.c',
                                            'coinhash/darkcoin_hash/darkcoin.c',
                                            'coinhash/darkcoin_hash/sha3/blake.c',
                                            'coinhash/darkcoin_hash/sha3/bmw.c',
                                            'coinhash/darkcoin_hash/sha3/groestl.c',
                                            'coinhash/darkcoin_hash/sha3/jh.c',
                                            'coinhash/darkcoin_hash/sha3/keccak.c',
                                            'coinhash/darkcoin_hash/sha3/skein.c',
                                            'coinhash/darkcoin_hash/sha3/cubehash.c',
                                            'coinhash/darkcoin_hash/sha3/echo.c',
                                            'coinhash/darkcoin_hash/sha3/luffa.c',
                                            'coinhash/darkcoin_hash/sha3/simd.c',
                                            'coinhash/darkcoin_hash/sha3/shavite.c'],
                               include_dirs=['coinhash/darkcoin_hash', 'coinhash/darkcoin_hash/sha3'])

ltc_scrypt_module = Extension('coinhash.ltc_scrypt',
                              sources=['coinhash/ltc_scrypt/scryptmodule.c',
                                       'coinhash/ltc_scrypt/scrypt.c'],
                              include_dirs=['coinhash/ltc_scrypt'])


setup(
    name = 'coinhash',
    version = '1.0',
    description = 'Compilation of coin hash algorithms.',
    long_description = 'Compilation of coin hash algorithms. Individual licenses are located in their respective directories.',
    package_dir = {
        'coinhash': 'coinhash'
    },
    ext_modules = [neoscrypt_module,
                skeinhash_module,
                qubit_hash_module,
                groestlcoin_hash_module,
                darkcoin_hash_module],
    py_modules = [
        'coinhash.__init__'
    ]
)

