## 文字字串
1. 將m開抔的單字改為首字大寫
    ```python
    >>> song = """When an ell grabs your arm,
    ... And it causes great harm,
    ... That's - a moray!"""
    >>> song.replace(" m", " M")
    "When an ell grabs your arm,\nAnd it causes great harm,\nThat's - a Moray!"
    >>> 
    ```

2. 用以下格式列印出問題與答案
    Q:問題
    A:答案
    ```python
    >>> questions = ["We don't serve strings around here. Are you a string?",
    ... "What is said on Father's Day in the forest?",
    ... "What makes the sound Sis'! Boom! Bah!'?"
    ... ]
    >>> answers = [ "An exploding sheep.",
    ... "No, I'm a frayed knot.",
    ... "'Pop!' goes the weasel."]
    >>> f"Q:{questions[0]}"
    "Q:We don't serve strings around here. Are you a string?"
    >>> f"A:{answers[0]}"
    'A:An exploding sheep.'
    >>> f"Q:{questions[1]}"
    "Q:What is said on Father's Day in the forest?"
    >>> f"A:{answers[1]}"
    "A:No, I'm a frayed knot."
    >>> f"Q:{questions[2]}"
    "Q:What makes the sound Sis'! Boom! Bah!'?"
    >>> f"A:{answers[2]}"
    "A:'Pop!' goes the weasel."
    >>>
    ```

3. 用舊的格式化來寫以下的詩，並代入'roast beef'、'ham'、'head'、'clam'
    ```python
    >>> """My kitty cat likes %s,
    ... My kitty cat likes  %s,
    ... My kitty cat fell on his %s,
    ... And now thinks he's a %s.""" % ('roast beef', 'ham', 'head', 'clam')
    "My kitty cat likes roast beef,\nMy kitty cat likes  ham,\nMy kitty cat fell on his head,\nAnd now thinks he's a clam."
    >>>
    ```

4. 使用新式格式化來寫一封公式化信件。將下列的字串存為letter
    ```python
    >>> letter = """Dear {salutation} {name},
    ... Thank you for your letter.We are sorry that our {product}
    ... {verbed} in your {room}. Please note that it should never
    ... be used in a {room}, especially near any {animals}.
    ... Send us your receipt and {amount} for shipping and handling.
    ... We will send your another {product} that, in our tests,
    ... is {percent}% less likely to have {verbed}.
    ... Thank you for your support.
    ... Sincerely,
    ... {spokesman}
    ... {job_title}"""
    >>>
    ```

5. 將值指派給以上各參數並使用letter.format()印出信件
    ```python
    >>> letter.format(salutation="Mr.", name="Sam", product="fan", verbed="broken", room="Room39", animals="goat",  amount="200", percent="12", spokesman="Amy", job_title="Engineer")
    'Dear Mr. Sam,\nThank you for your letter.We are sorry that our fan\nbroken in your Room39. Please note that it should never\nbe used in a Room39, especially near any goat.\nSend us your receipt and 200 for shipping and handling.\nWe will send your another fan that, in our tests,\nis 12% less likely to have broken.\nThank you for your support.\nSincerely,\nAmy\nEngineer'
    >>>
    ```

6. Boaty -> McBoatface; Horsey -> McHorseface; Trainy -> McTrainface，使用%格式化為duck、gourd、spitz印出名字
    ```python
    >>> "%sy: Mc%sface" %("Duck", "Duck")
    'Ducky: McDuckface'
    >>> "%sy: Mc%sface" %("Gourd", "Gourd")
    'Gourdy: McGourdface'
    >>> "%sy: Mc%sface" %("Spitz", "Spitz")
    'Spitzy: McSpitzface'
    >>>
    ```

7. 用format()格式化做同一件事
    ```python
    >>> "{name}y: Mc{name}face".format(name="Duck")
    'Ducky: McDuckface'
    >>> "{name}y: Mc{name}face".format(name="Gourd")
    'Gourdy: McGourdface'
    >>> "{name}y: Mc{name}face".format(name="Spitz")
    'Spitzy: McSpitzface'
    >>>
    ```

8. 用f-string再做一次
    ```python
    >>> name = "Duck"
    >>> f"{name}y: Mc{name}face"
    'Ducky: McDuckface'
    >>> name = "Gourd"
    >>> f"{name}y: Mc{name}face"
    'Gourdy: McGourdface'
    >>> name = "Spitz"
    >>> f"{name}y: Mc{name}face"
    'Spitzy: McSpitzface'
    >>>
    ```