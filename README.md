# PY-LEXIMITED 

by LCF NERD 218


#### LEX-ENCODING IN PYTHON

<b>Lex</b>icographically Del<b>imited</b> Encoding for python, why not ay...
 
See: [https://github.com/elenasa/ULAM/wiki/Appendix-D:-Leximited-Format](https://github.com/elenasa/ULAM/wiki/Appendix-D:-Leximited-Format)

Following on from: [https://github.com/walpolea/leximitedjs](https://github.com/walpolea/leximitedjs)

WHY? : [https://twitter.com/walpolea/status/1260954256292458497](https://twitter.com/walpolea/status/1260954256292458497)

LIKE THIS? CHECK OUT => [https://www.livingcomputation.org/](https://www.livingcomputation.org/)


<hr>

### INSTALL

[https://pypi.org/project/leximited/1.1.1/](https://pypi.org/project/leximited/1.1.1/)

``` pip install leximited ```


<hr>

### IMPORT

``` import leximited ```

<hr>

### USE

Call ```leximited.to_leximited()``` with numbers (int or str) or arbitrary strings to get their leximited version.

Call ```leximited.from_leximited()``` with lex-encoded numbers (int or str) or arbitrary lex-encoded strings to get their "normal" version.

Also supports lists and tuples and allows for mixed lists with lex-encoding on numbers only, see examples below.


```python
print(f'INTEGERS: {leximited.to_leximited(1)}')
INTEGERS: 11
```

```python
print(f"NUMBERS WITH LEADING 0s: {leximited.to_leximited('002')}")
NUMBERS WITH LEADING 0s: '12'
```

```python
print(f'BIG NUMBERS: {leximited.to_leximited(2000000000)}')
BIG NUMBERS: 92102000000000
```

```python
print(f"SHORT STRINGS: {leximited.to_leximited('Bh3!!!')}")
SHORT STRINGS: 6Bh3!!!
```

```python
print(f'LONG STRINGS: {leximited.to_leximited("a man, a plan, a guy: eleets")}')
LONG STRINGS: 9228a man, a plan, a guy: eleets
```

```python
print(f"EMPTY STRINGS: {leximited.to_leximited('')}")
EMPTY STRINGS: 0
```

Also takes lists or tuples, and optionally preserve non-number strings as their original form (convert_text defaults to True to lex-encode everything).

```python

in_list = [1, '002', 2000000000, 'Bh3!!!', 'a man, a plan, a guy: eleets', '']
print(f'INPUT: {in_list}')
leximited_list = leximited.list_to_leximited(in_list, convert_text=True)
print(f'LEXIMITED: {leximited_list}')
back_again = leximited.list_from_leximited(leximited_list)
print(f'AND BACK AGAIN: {back_again}')

INPUT: [1, '002', 2000000000, 'Bh3!!!', 'a man, a plan, a guy: eleets', '']
LEXIMITED: [11, '12', 92102000000000, '6Bh3!!!', '9228a man, a plan, a guy: eleets', '0']
AND BACK AGAIN: [1, '2', 2000000000, 'Bh3!!!', 'a man, a plan, a guy: eleets', '']

```
Note that the leading zeros are lost when converting back again.




