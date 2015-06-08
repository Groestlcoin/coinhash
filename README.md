# coinhash

Compilation of coin hash modules.

This package is a collection of various hash algorithms used by cryptocurrencies.

## Usage

```python
    import coinhash
    data = '00'.decode('hex')
    neoscrypt_digest = coinhash.NeoscryptHash(data)
    skein_digest = coinhash.SkeinHash(data)
    qubit_digest = coinhash.QubitHash(data)
    groestl_digest = coinhash.GroestlHash(data, len(data))
    x11_digest = coinhash.X11Hash(data)
```

## License

Individual licenses are located within each algorithm's directory.
