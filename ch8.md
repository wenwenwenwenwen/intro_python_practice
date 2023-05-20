## dict and set
1. 
    ```python
    >>> e2f = {"dog": "chien", "cat": "chat", "walrus": "morse"}
    >>> e2f
    {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
    >>> 
    ```

2. 印出e2f的walrus法文
    ```python
    >>> e2f["walrus"]
    'morse'
    >>>
    ```

3. 用e2f製作法英字典f2e
    ```python
    >>> f2e = {v: k for k, v in e2f.items()}
    >>>
    ```

4. 印出法文單字chien的英文
    ```python
    >>> f2e["chien"]
    'dog'
    >>>
    ```

5. 印出e2f的英文單字集合
    ```python
    >>> e2f.keys()
    dict_keys(['dog', 'cat', 'walrus'])
    >>> 
    ```

6. 製作一個多層字典，稱為life。將這些字串當成最頂層的鍵：'animals'，'plants'與'other'。讓'animals'鍵引用另一個擁有'cats'、'octopi'與'emus'鍵的字典。讓'cats'鍵引用一個字串串列，其值為'Henri'、'Grumpy'與'Lucy'。讓所有其他鍵引用空字典。
    ```python
    >>> life = {"animals": {"cats": ["Henri", "Grumpy", "Lucy"], "octopi": {}, "emus":{}}, "plants": {}, "other": {}}
    >>> life
    {'animals': {'cats': ['Henri', 'Grumpy', 'Lucy'], 'octopi': {}, 'emus': {}}, 'plants': {}, 'other': {}}
    >>>
    ```

7. 印出life最頂層的鍵
    ```python
    >>> life.keys()
    dict_keys(['animals', 'plants', 'other'])
    >>>
    ```

8. 印出life['animals']的鍵
    ```python
    >>> life["animals"].keys()
    dict_keys(['cats', 'octopi', 'emus'])
    >>> 
    ```

9. 印出life['animals']['cats']的值
    ```python
    >>> life["animals"]["cats"]
    ['Henri', 'Grumpy', 'Lucy']
    >>>
    ```

10. 用字典生成式製作字典squares。使用range(10)來回傳鍵，並將各個鍵的平方當成值
    ```python
    >>> squares = {k: k**2 for k in range(10)}
    >>> squares
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
    >>>
    ```

11. 使用集合生成式和range(10)之內的奇數來製作odd集合
    ```python
    >>> odd = {i for i in range(10) if i%2 != 0}
    >>> odd
    {1, 3, 5, 7, 9}
    >>>
    ```

12. 使用產生器生成式來回傳字串'Got '與range(10)內的一個數字。使用for迴圈迭代它
    ```python
    >>> generator_object = (i for i in range(10))
    >>> for x in generator_object:
    ...     print(f"Got {x}")
    ... 
    Got 0
    Got 1
    Got 2
    Got 3
    Got 4
    Got 5
    Got 6
    Got 7
    Got 8
    Got 9
    >>> 
    ```

13. 使用zip()和鍵tuple('optimist', 'pessimist', 'troll')與值tuple('The glass is half full', 'The glass is half empty', 'How did you get a glass?')來製作一個字典
    ```python
    >>> k = ('optimist', 'pessimist', 'troll')
    >>> v = ('The glass is half full', 'The glass is half empty', 'How did you get a glass?')
    >>> output = {k: v for k, v in zip(k,v)}
    >>> output
    {'optimist': 'The glass is half full', 'pessimist': 'The glass is half empty', 'troll': 'How did you get a glass?'}
    >>>
    ```

14. 使用zip()製作movies字典，配對這些串列：titles = ['Creature of Habit', 'Crewel Fate', 'Sharks On a Plane']與plot = ['A nun turns into a monster', 'A haunted yarn shop', 'Check your exits']
    ```python
    >>> titles = ['Creature of Habit', 'Crewel Fate', 'Sharks On a Plane']
    >>> plot = ['A nun turns into a monster', 'A haunted yarn shop', 'Check your exits']
    >>> movies = {title: p for title, p in zip(titles, plot)}
    >>> movies
    {'Creature of Habit': 'A nun turns into a monster', 'Crewel Fate': 'A haunted yarn shop', 'Sharks On a Plane': 'Check your exits'}
    >>>
    ```