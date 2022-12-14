# Encrypter module

Custom Base58 encoding/decoding module written in Python. For now, the module uses only the alphabet used for Bitcoun adresses and IPFS hashes.

## Base58
The Base58 encoding format is designed for use in Bitcoin and is used in many other cryptocurrencies. It offers a balance between compact performace, readability, definition and error prevention. Base58 is a suset of Base64 that uses lowercase and uppercase letters and numbers, but without some characters that are often mistaken for each other and can be identical in some fonts. In particular, Base58 is Base64 without number 0 (zero), O (capital letter O), l (small letter L), I (large letter i), and characters "\+" and "/". Or, simply put, it is a set of uppercase and lowercase letters and numbers without the four (0, O, L, I) mentioned above. In contrast to Base64, the digits of the encoding do not line up well with byte boundaries of the original data. For this reason, the method is well-suited to encode large integers, but not designed to encode longer portions of binary data. The actual order of letters in the alphabet depends on the application, which is the reason why the term "Base58" alone is not enough to fully describe the format. A variant, Base56, excludes 1 (one) and o (lowercase o) compared to Base58.


## How does it Work?
To encode a string manually first we have to convert it to a Hex ascii string. For example let's say our string is name "Hana":


Shown bellow is a partial table of ascii code.

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

From the table we get the hex value of the name "Hana"
|Letter|Hex value|
|:----:|:-------:|
|H     |48       |
|a     |61       |
|n     |6E       |
|a     |61       |

so the hex value of "Hana" is: 48 61 6E 61

Next, we have to convert the text value to base 10 value:
```
48616E61 = (4*16^7)+(8*16^6)+(6*16^5)+(1*16^4)+(6*16^3)+(14*16^2)+(6*16^1)+(1*16^0) = 1214344801
```
Now we have to look at our alphabet:
|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|26|27|28|29|30|31|32|33|34|35|36|37|38|39|40|41|42|43|44|45|46|47|48|49|50|51|52|53|54|55|56|57|58|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1  |2  |3  |4  |5  |6  |7  |8  |9  |A  |B  |C  |D  |E  |F  |G  |H  |J  |K  |L  |M  |N  |P  |Q  |R  |S  |T  |U  |V  |W  |X  |Y  |Z  |a  |b  |c  |d  |e  |f  |g  |h  |i  |j  |k  |m  |n  |o  |p  |q  |r  |s  |t  |u  |v  |w  |x  |y  |z  |


Iteration 1:
```
1214344801 // 58 = 20936979
1214344801 % 58 = 19 
19 + 1 = 20 => TABLE(20) => L
```

Iteration 2:
```
20936979 // 58 = 360982
20936979 % 58 = 23
23 + 1 = 24 => TABLE(24) => Q
```

Iteration 3:
```
360982 // 58 = 6223
360982 % 58 = 48
48 + 1 = 49 => TABLE(49) => q
```

Iteration 4:
```
6223 // 58 = 107
6223 % 58 = 17
17 + 1 = 18 => TABLE(18) => J
```

Iteration 5:
```
107 // 58 = 1
107 % 58 = 49
49 + 1 = 50 => TABLE(50) => r
```

Iteration 6:
```
1 // 58 = 0
1 % 58 = 1
1 + 1 = 2 => TABLE(2) => 2
```

So the final Base58 encoded message is: ```"2rJqQL"```

# Module usage

Importing the module for Base58 encoding and decoding
```python
from encrypter import Encrypter
```

# Encoding
Input:
```python
from encrypter import Encrypter

encrypter = Encrypter()

text_to_encode = "Test string to encode"
text_encoded = encrypter.b58encode(text_to_encode)
print(text_encoded)
```

Output:
```
6C11q3kb5UkAaE5hfb1WMZ78KUsEt
```


# Decoding
Input:
```python
from encrypter import Encrypter

encrypter = Encrypter()

text_to_decode = "6C11q3kb5UkAaE5hfb1WMZ78KUsEt"
text_decoded = encrypter.b58decode(text_to_decode)
print(text_decoded)
```

Output:
```
Test string to encode
```
