# Lesson 2 Independent Challenges

## Challenge 1: `magic_pet_shop` (4 points)

| Function parameter(s) | Function return(s) |
|-----------------------|--------------------|
| None                  | None               |

Write a function that asks the user for two responses: firstly, what type of animal would be their ideal pet, and secondly, what they would call their ideal pet. Once you have these, print the following exact text, replacing the first `___` with their pet type response and the second `___` with their pet name response:

```
Unbelievable! We have your ideal pet. This ___ over here is called ___.
```

## Challenge 2: `place_sundries_order` (6 points)

| Function parameter(s) | Function return(s) |
|-----------------------|--------------------|
| None                  | None               |

Write a function that asks the user for two responses: firstly, how many bowls of rice their party would like, and secondly, how many naan breads their party would like. Once you have these, print the following exact text, replacing the `___` with the cost of their order, given that each bowl of rice costs 3.95 currency and each naan bread costs 3.45 currency:

```
Thank you, that will be ___.
```

The cost of their order should be formatted to exactly two decimal places.

## Challenge 3: `fahrenheit_to_celsius` (6 points)

| Function parameter(s)                                         | Function return(s)                            |
|---------------------------------------------------------------|-----------------------------------------------|
| `fahrenheit_temperature`, a temperature in degrees Fahrenheit | The equivalent temperature in degrees Celsius |

Write a function that takes a temperature in degrees Fahrenheit and returns the equivalent temperature in degrees Celsius. You should find the formula for the conversion online and implement it carefully.

**Note: you should not use `input` or `print` in this function.**

## Challenge 4: `should_take_coat` (6 points)

| Function parameter(s) | Function return(s) |
|-----------------------|--------------------|
| None                  | None               |

Write a function that asks the user for a single response: the current temperature in degrees Celsius. If their response is below 15, print the following exact text:

```
You should take a coat with you when you go out.
```

Otherwise, print the following exact text instead:

```
No need for a coat, go as you are.
```

## Challenge 5: `should_take_umbrella_or_coat` (10 points)

| Function parameter(s) | Function return(s) |
|-----------------------|--------------------|
| None                  | None               |

Write a function that firstly asks the user for a single response: whether it is currently raining. If their response is the exact word `yes`, ask them a further question: whether they are going to the city or the countryside. If their response is the exact word `city`, print the following exact text:

```
You should take an umbrella with you when you go out.
```

Otherwise, if their response is the exact word `countryside`, print the following exact text instead:

```
You should take a coat with you when you go out.
```

Otherwise, if their response matches neither word, print the following exact text:

```
I'm not sure whether you should take an umbrella or a coat with you.
```

Back to the original question, if their response to whether it is currently raining is the exact word `no`, print the following exact text:

```
No need for an umbrella or a coat, go as you are.
```

Finally, if their response was neither `yes` nor `no`, print the following exact text:

```
Sorry, I didn't understand your response.
```

## Challenge 6: `calculate_car_hire_cost` (10 points)

| Function parameter(s)                          | Function return(s)             |
|------------------------------------------------|--------------------------------|
| `days`, the number of days to hire the car for | The total cost of the car hire |

Write a function that takes a number of days and returns the total cost of hiring a car for that number of days. Each day costs 60 currency. There are two special offers: if the number of days is at least 3, a discount of 20 currency is applied, or if the number of days is at least 7, a discount of 50 currency is applied. Only one offer can be applied at a time, with the second offer taking precedence over the first.

**Note: you should not use `input` or `print` in this function.**

## Challenge 7: `find_rock_paper_scissors_winner` (18 points)

| Function parameter(s)                                              | Function return(s) |
|--------------------------------------------------------------------|--------------------|
| `player_1_move` and `player_2_move`, the moves made by each player | None               |

Write a function that takes a move for each of two players and prints one of the following exact text snippets, depending on the situation:

```
Player 1 wins!
```

```
Player 2 wins!
```

```
It's a draw.
```

The values passed in will be either `rock`, `paper` or `scissors` (you only have to handle the lowercase versions). You should find the rules of Rock-Paper-Scissors online if you don't already know them, and implement them carefully.

## Challenge 8: `calculate_milliseconds` (6 points)

| Function parameter(s)                                             | Function return(s)                             |
|-------------------------------------------------------------------|------------------------------------------------|
| `hours`, `minutes` and `seconds`, the number of each unit of time | The number of milliseconds across the duration |

Write a function that takes a number of hours, minutes and seconds in a duration, then calculates and returns the total number of milliseconds across that duration.

**Note: you should not use `input` or `print` in this function.**

## Challenge 9: `calculate_course_grade` (14 points)

| Function parameter(s)                                                                         | Function return(s)                                                            |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| `assignment_scores`, a list containing the scores obtained on each assignment from the course | The letter grade that corresponds to the average of all the assignment scores |

Write a function that takes a list containing the scores obtained by a student on each assignment from the course (all equally weighted) and returns the letter grade that corresponds to the average score. The grade thresholds are as follows:

```
A   90 or above
B   80 or above
C   70 or above
D   60 or above
E   50 or above
F   Below 50
```

If the student hasn't submitted any assignments yet, return the exact text `?` instead of a letter grade from the list.

**Note: you should not use `input` or `print` in this function.**

## Challenge 10: `convert_to_variable_name` (6 points)

| Function parameter(s)     | Function return(s)                                               |
|---------------------------|------------------------------------------------------------------|
| `text`, the starting text | Lowercase version of the text with underscores instead of spaces |

Write a function that takes a piece of text and returns a lowercase copy with a single underscore replacing each space. For example:

```
"My favourite food" -> "my_favourite_food"
```

**Note: you should not use `input` or `print` in this function.**

## Challenge 11: `make_boring` (8 points)

| Function parameter(s)     | Function return(s)                                               |
|---------------------------|------------------------------------------------------------------|
| `text`, the starting text | Version of the text with full stops instead of exclamation marks |

Write a function that takes a piece of text and returns a copy of the text with a single full stop replacing each exclamation mark or group of exclamation marks. For example:

```
"Hello!!! How are you? Nice to see you!" -> "Hello. How are you? Nice to see you."
```

**Note: you should not use `input` or `print` in this function.**

## Challenge 12: `check_for_duplicates` (6 points)

| Function parameter(s) | Function return(s)                                        |
|-----------------------|-----------------------------------------------------------|
| `items`, a sequence   | Whether or not there are any duplicate items in the input |

Write a function that takes any sequence (e.g. a `list`, `tuple` or `str`) and returns a boolean value (`True` or `False`) signifying whether the sequence contains any duplicate items. For example:

```
"foregrounds" -> True
"backgrounds" -> False
[1, 2, 3, 4, 5] -> False
(21, 24, 23, 24, 22) -> True
```

**Note: you should not use `input` or `print` in this function.**
