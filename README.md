# PY-LEXIMITED 
#### LEX-ENCODING IN PYTHON

<b>Lex</b>icographically Del<b>imited</b> Encoding for python, why not ay...
 
See: [https://github.com/elenasa/ULAM/wiki/Appendix-D:-Leximited-Format](https://github.com/elenasa/ULAM/wiki/Appendix-D:-Leximited-Format)

Following on from: [https://github.com/walpolea/leximitedjs](https://github.com/walpolea/leximitedjs)


<hr>

### INSTALL

[https://pypi.org/project/leximited/1.0.3/](https://pypi.org/project/leximited/1.0.3/)

``` pip install leximited ```


<hr>

### IMPORT

``` import leximited ```

<hr>
### USE

Call ```leximited.to_leximited()``` with numbers (int or str) or arbitrary strings

```
print(f'INTEGERS: {leximited.to_leximited(1)}')
INTEGERS: 11
```

```
print(f"NUMBERS WITH LEADING 0s: {leximited.to_leximited('002')}")
NUMBERS WITH LEADING 0s: '12'
```

```
print(f'BIG NUMBERS: {leximited.to_leximited(2000000000)}')
BIG NUMBERS: 92102000000000
```

```
print(f"SHORT STRINGS: {leximited.to_leximited('Bh3!!!')}")
SHORT STRINGS: 6Bh3!!!
```

```
print(f'LONG STRINGS: {leximited.to_leximited("a man, a plan, a guy: eleets")}')
LONG STRINGS: 9228a man, a plan, a guy: eleets
```

```
print(f"EMPTY STRINGS: {leximited.to_leximited('')}")
EMPTY STRINGS: 0
```

Also takes lists or tuples, and optionally preserve non-number strings as their original form (convert_text defaults to True to lex-encode everything).

```
in_list = [1, '002', 2000000000, 'Bh3!!!', 'a man, a plan, a guy: eleets', '']
print(f'INPUT: {in_list}')
print(f'OUTPUT: {leximited.list_as_leximited(in_list, convert_text=True)}')

INPUT: [1, '002', 2000000000, 'Bh3!!!', 'a man, a plan, a guy: eleets', '']
OUTPUT: [11, '12', 92102000000000, '6Bh3!!!', '9228a man, a plan, a guy: eleets', '0']

```

