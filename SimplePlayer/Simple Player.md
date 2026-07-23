# Simple Player
## Common notes
|Shortcut|     Note Name    |          With Dot          |
|--------|------------------|----------------------------|
|`w`/`.w`|Whole Note        |Dotted Whole Note           |
|`h`/`.h`|Half Note         |Dotted Half Note            |
|`q`/`.q`|Quarter Note      |Dotted Quarter Note         |
|`e`/`.e`|Eighth Note       |Dotted Eighth Note          |
|`s`/`.s`|Sixteenth Note    |Dotted Sixteenth Note       |
|`t`/`.t`|Thirty-second Note|Dotted Thirty-second Note   |
|`x`/`.x`|Sixty-fourth Note |Dotted Sixty-fourth Note    |

## Format
It's basically a list with tuples

```python
# See bad_apple.py
bpm = 274
song = [
    ('1','2')
]
```
- 1 should be the frequency example 'C4'.
- 2 should be any of the common notes.