# coinhash

Compilation of coin hash modules.

This package is a collection of various hash algorithms used by cryptocurrencies.

## Usage

```python
    import coinhash
    data = '00'.decode('hex')
    neoscrypt_digest = coinhash.neoscrypt_hash(data)
    skein_digest = coinhash.skein_hash(data)
    qubit_digest = coinhash.qubit_hash(data)
    groestl_digest = coinhash.groestl_hash(data, len(data))
    x11_digest = coinhash.x11_hash(data)
```

## License

Individual licenses are located within each algorithm's directory.
