# Encrypter module

Custom Base58 coding/decoding module written in Python. For now, the module uses only the alphabet used for Bitcoun adresses and IPFS hashes.

## Base58
The Base58 encoding format is designed for use in Bitcoin and is used in many other cryptocurrencies. It offers a balance between compact performace, readability, definition and error prevention. Base58 is a suset of Base64 that uses lowercase and uppercase letters and numbers, but without some characters that are often mistaken for each other and can be identical in some fonts. In particular, Base58 is Base64 without number 0 (zero), O (capital letter O), l (small letter L), I (large letter i), and characters "\+" and "/". Or, simply put, it is a set of uppercase and lowercase letters and numbers without the four (0, O, L, I) mentioned above. In contrast to Base64, the digits of the encoding do not line up well with byte boundaries of the original data. For this reason, the method is well-suited to encode large integers, but not designed to encode longer portions of binary data. The actual order of letters in the alphabet depends on the application, which is the reason why the term "Base58" alone is not enough to fully describe the format. A variant, Base56, excludes 1 (one) and o (lowercase o) compared to Base58.


## How does it Work?
To encode a string manually first we have to convert it to a Hex ascii string. For example let's say our string is name "Hana":




|#    |Symbol   | HEX value|#    |Symbol   | HEX value|#    |Symbol   | HEX value|
|:---:|:-------:|:--------:|:---:|:-------:|:--------:|:---:|:-------:|:--------:|
|1.   |        0|        30|11.  |        A|        41|37.  |        a|        61|
|2.   |        1|        31|12.  |        B|        42|38.  |        b|        62|
|3.   |        2|        32|13.  |        C|        43|39.  |        c|        63|
|4.   |        3|        33|14.  |        D|        44|40.  |        d|        64|
|5.   |        4|        34|15.  |        E|        45|41.  |        e|        65|
|6.   |        5|        35|16.  |        F|        46|42.  |        f|        66|
|7.   |        6|        36|17.  |        G|        47|43.  |        g|        67|
|8.   |        7|        37|18.  |        H|        48|44.  |        h|        68|
|9.   |        8|        38|19.  |        I|        49|45.  |        i|        69|
|10.  |        9|        39|20.  |        J|        4A|46.  |        j|        6A|
|     |         |          |21.  |        K|        4B|47.  |        k|        6B|
|     |         |          |22.  |        L|        4C|48.  |        l|        6C|
|     |         |          |23.  |        M|        4D|49.  |        m|        6D|
|     |         |          |24.  |        N|        4E|50.  |        n|        6E|
|     |         |          |25.  |        O|        4F|51.  |        o|        6F|
|     |         |          |26.  |        P|        50|52.  |        p|        70|
|     |         |          |27.  |        Q|        51|53.  |        q|        71|
|     |         |          |28.  |        R|        52|54.  |        r|        72|
|     |         |          |29.  |        S|        53|55.  |        s|        73|
|     |         |          |30.  |        T|        54|56.  |        t|        74|
|     |         |          |31.  |        U|        55|57.  |        u|        75|
|     |         |          |32.  |        V|        56|58.  |        v|        76|
|     |         |          |33.  |        W|        57|59.  |        w|        77|
|     |         |          |34.  |        X|        58|60.  |        x|        78|
|     |         |          |35.  |        Y|        59|61.  |        y|        79|
|     |         |          |36.  |        Z|        5A|62.  |        z|        7A|



# Module usage

Importing the module for Base58 encoding and decoding
```python
from encripter import Encripter
```

# Encoding
Input:
```python
from encripter import Encripter

encripter = Encripter()

text_to_encode = "Test string to encode"
text_encoded = encripter.b58encode(text_to_encode)
print(text_encoded)
```

Output:
```
6C11q3kb5UkAaE5hfb1WMZ78KUsEt
```


# Decoding
Input:
```python
from encripter import Encripter

encripter = Encripter()

text_to_decode = "6C11q3kb5UkAaE5hfb1WMZ78KUsEt"
text_decoded = encripter.b58decode(text_to_decode)
print(text_decoded)
```

Output:
```
Test string to encode
```
