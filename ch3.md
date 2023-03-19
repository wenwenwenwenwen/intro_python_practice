## 數字
1. 一小時有幾秒?(將每分鐘的秒數乘上每小時的分鐘數)
    ```python
    >>> 60 * 60
    3600
    >>>
    ```

2. 將3.1的結果指派給`second_per_hour`
    ```python
    >>> second_per_hour = 60 * 60
    >>>
    ```

3. 一天有幾秒?(使用`second_per_hour`計算)
    ```python
    >>> second_per_hour * 24
    86400
    >>>
    ```

4. 再次計算一天的秒數，並將結果存入`second_per_day`變數
    ```python
    >>> second_per_day = second_per_hour * 24
    >>>
    ```

5. 將`second_per_day`除以`second_per_hour`，使用浮點數除法(/)
    ```python
    >>> second_per_day / second_per_hour
    24.0
    >>>
    ```

6. 將`second_per_day`除以`second_per_hour`，使用整數除法(//)。除了.0之外其他部分是否相同?yes
    ```python
    >>> second_per_day // second_per_hour
    24
    >>>
    ```