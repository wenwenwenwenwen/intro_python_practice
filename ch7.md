## tuple and list
1. 建立`years_list`，列出從出生年列到第5個生日
    ```python
    >>> years_list = list(range(1990, 1990+6))
    >>> years_list
    [1990, 1991, 1992, 1993, 1994, 1995]
    >>>
    ```

2. `years_list`的第3個值
    ```python
    >>> years_list[2]
    1992
    >>>
    ```

3. `years_list`最後一個值
    ```python
    >>> years_list[-1]
    1995
    ```

4. 使用"mozzarella", "cinderella", "salmonella"建立things list
    ```python
    >>> things = ["mozzarella", "cinderella", "salmonella"]
    >>>
    ```

5. 將cinderella改為首字大寫，在印出list，是否會改變list內元素? 會
    ```python
    >>> things[1] = things[1].capitalize()
    >>> things
    ['mozzarella', 'Cinderella', 'salmonella']
    >>>
    ```

6. 將mozzarella改成全部大寫再印出list
    ```python
    >>> things[0] = things[0].upper()
    >>> things
    ['MOZZARELLA', 'Cinderella', 'salmonella']
    >>>
    ```

7. 將salmonella刪除再印出list(remove("salmonella"))
    ```python
    >>> things.pop()
    'salmonella'
    >>> things
    ['MOZZARELLA', 'Cinderella']
    >>>
    ```

8. 建立surprise = ["Groucho", "Chico", "Harpo"]
    ```python
    >>> surprise = ["Groucho", "Chico", "Harpo"]
    ```

9. 將surprise最後一個元素改為小寫，將它反過來，再將它第一個字母改為大寫
    ```python
    >>> surprise[-1] = surprise[-1].lower()[-1::-1]
    >>> suprise[-1] = surprise[-1].capitalize()
    >>> surprise
    ['Groucho', 'Chico', 'Oprah']
    >>>
    ```

10. 使用串列生成式建立even list，包含range(10)之內的偶數
    ```python
    >>> even = [i for i in range(10) if i % 2 == 0 ]
    >>> even
    [0, 2, 4, 6, 8]
    >>>
    ```

11. 印出雙行歌謠
    start1 = ["fee", "fie", "foe"]
    rhymes = [
        ("flop", "get a mop"),
        ("fope", "turn the rope"),
        ("fa", "get your ma"),
        ("fudge", "call the judge"),
        ("fat", "pet the cat"),
        ("fog", "walk th dog"),
        ("fun", "say we're done"),
    ]
    start2 = "Someone better"
    對於rhymes裡面的各個tuple(first, second):
    在第一行:
        印出start1裡面每個字串，將它改成首字大寫，並在後面加上一個驚嘆號與一個空格
        再印出first，也改成首字大寫並再後面加上一個驚嘆號
    在第二行:
        印出start2與一個空格
        印出second與一個句點
    ```python
    >>> start1 = ["fee", "fie", "foe"]
    >>> rhymes = [
    ...         ("flop", "get a mop"),
    ...         ("fope", "turn the rope"),
    ...         ("fa", "get your ma"),
    ...         ("fudge", "call the judge"),
    ...         ("fat", "pet the cat"),
    ...         ("fog", "walk th dog"),
    ...         ("fun", "say we're done"),
    ...     ]
    >>> start2 = "Someone better"
    >>> start1 = "".join([i.capitalize() + "! " for i in start1])
    >>> start1
    'Fee! Fie! Foe! '
    >>> for first, second in rhymes:
    ...     print(start1 + first.capitalize() + "!")
    ...     print(start2 + " " + second + ".")
    ... 
    Fee! Fie! Foe! Flop!
    Someone better get a mop.
    Fee! Fie! Foe! Fope!
    Someone better turn the rope.
    Fee! Fie! Foe! Fa!
    Someone better get your ma.
    Fee! Fie! Foe! Fudge!
    Someone better call the judge.
    Fee! Fie! Foe! Fat!
    Someone better pet the cat.
    Fee! Fie! Foe! Fog!
    Someone better walk th dog.
    Fee! Fie! Foe! Fun!
    Someone better say we're done.
    >>> 
    ```