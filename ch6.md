## for and while
1. 用for迴圈印出串列[3, 2, 1, 0]的值
    ```python
    >>> l = [3, 2, 1, 0]
    >>> for i in l:
    ...     print(i)
    ... 
    3
    2
    1
    0
    >>>
    ```

2. guess_me = 7; number = 1，寫while迴圈比較number與guess_me，並在迴圈結束時遞增數字
    - number < guess_me -> "too low"
    - number == guess_me -> "found it!"
    - number > guess_me -> "oops" & 離開迴圈
    ```python
    >>> guess_me = 7
    >>> number = 1
    >>> while True:
    ...     if number < guess_me:
    ...         print("too low")
    ...         number = number + 1
    ...     elif number == guess_me:
    ...         print("found it!")
    ...         break
    ...     else:
    ...         print("oops")
    ...         break
    ... 
    too low
    too low
    too low
    too low
    too low
    too low
    found it!
    >>> 
    ```

3. guess_me = 5，使用for迴圈在range(10)之內迭代一個名為number的變數
    - number < guess_me -> "too low"
    - number == guess_me -> "found it!" & 跳出迴圈
    - number > guess_me -> "oops" & 離開迴圈
    ```python
    >>> number = range(10)
    >>> guess_me = 5
    >>> for number in range(10):
    ...     if number < guess_me:
    ...         print("too low")
    ...     elif number == guess_me:
    ...         print("found it!")
    ...         break
    ...     else:
    ...         print("oops")
    ...         break
    ... 
    too low
    too low
    too low
    too low
    too low
    found it!
    >>>
    ```