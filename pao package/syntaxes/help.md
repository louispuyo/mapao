`?` The question mark indicates zero or one occurrences of the preceding element. For example, `colou?r` matches both `"color"` and `"colour". *` The asterisk indicates zero or more occurrences of the preceding element. For example, `ab*c` matches `"ac"`, `"abc"`, `"abbc"`, `"abbbc"`, and so on. `+` The plus sign indicates one or more occurrences of the preceding element. For example, ab+c matches "abc", "abbc", "abbbc", and so on, but not "ac". 
- `{n}` => The preceding item is matched exactly n times. 
- `{min,}` => The preceding item is matched min or more times. 
- `{min,max}` => The preceding item is matched at least min times, but not more than max times.


