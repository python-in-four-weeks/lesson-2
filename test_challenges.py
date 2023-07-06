import pytest
from pytest_mock import MockerFixture

from io import StringIO
from math import isclose
from typing import Sequence

import challenges


@pytest.mark.parametrize('pet_type, pet_name, expected_output', [
    ('dog', 'Spot', 'Unbelievable! We have your ideal pet. This dog over here is called Spot.'),
    ('cat', 'Fluffy', 'Unbelievable! We have your ideal pet. This cat over here is called Fluffy.'),
])
def test_magic_pet_shop(
        mocker: MockerFixture,
        pet_type: str,
        pet_name: str,
        expected_output: str) -> None:
    mocker.patch('builtins.input', side_effect=[pet_type, pet_name])
    mock_stdout = mocker.patch('sys.stdout', new_callable=StringIO)
    challenges.magic_pet_shop()
    outputted_lines = mock_stdout.getvalue().splitlines()
    assert len(outputted_lines) > 0, "There doesn't seem to be any output"
    assert len(outputted_lines) < 2, "There seem to be too many printed lines"
    assert outputted_lines[-1] == expected_output, f"A {pet_type} called {pet_name} should generate the output \"{expected_output}\""


@pytest.mark.parametrize('rice_bowl_count, naan_bread_count, expected_output', [
    ('0', '0', 'Thank you, that will be 0.00.'),
    ('3', '4', 'Thank you, that will be 25.65.'),
    ('2', '10', 'Thank you, that will be 42.40.'),
])
def test_place_sundries_order(
        mocker: MockerFixture,
        rice_bowl_count: str,
        naan_bread_count: str,
        expected_output: str) -> None:
    mocker.patch('builtins.input', side_effect=[rice_bowl_count, naan_bread_count])
    mock_stdout = mocker.patch('sys.stdout', new_callable=StringIO)
    challenges.place_sundries_order()
    outputted_lines = mock_stdout.getvalue().splitlines()
    assert len(outputted_lines) > 0, "There doesn't seem to be any output"
    assert len(outputted_lines) < 2, "There seem to be too many printed lines"
    assert outputted_lines[-1] == expected_output, f"An order of {rice_bowl_count} rice and {naan_bread_count} naan should generate the output \"{expected_output}\""


@pytest.mark.parametrize('fahrenheit_temperature, expected_celsius_temperature', [
    (32, 0),
    (0, -160 / 9),
    (86, 30),
])
def test_fahrenheit_to_celsius(
        fahrenheit_temperature: float,
        expected_celsius_temperature: float) -> None:
    celsius_temperature = challenges.fahrenheit_to_celsius(fahrenheit_temperature)
    assert isclose(celsius_temperature, expected_celsius_temperature), f"{fahrenheit_temperature} in Fahrenheit should correspond to {expected_celsius_temperature} in Celsius"


@pytest.mark.parametrize('temperature, expected_output', [
    ('20', 'No need for a coat, go as you are.'),
    ('15', 'No need for a coat, go as you are.'),
    ('-1', 'You should take a coat with you when you go out.'),
])
def test_should_take_coat(
        mocker: MockerFixture,
        temperature: str,
        expected_output: str) -> None:
    mocker.patch('builtins.input', side_effect=[temperature])
    mock_stdout = mocker.patch('sys.stdout', new_callable=StringIO)
    challenges.should_take_coat()
    outputted_lines = mock_stdout.getvalue().splitlines()
    assert len(outputted_lines) > 0, "There doesn't seem to be any output"
    assert len(outputted_lines) < 2, "There seem to be too many printed lines"
    assert outputted_lines[-1] == expected_output, f"A temperature of {temperature} should generate the output \"{expected_output}\""


@pytest.mark.parametrize('is_raining, city_or_countryside, expected_output', [
    ('yes', 'city', 'You should take an umbrella with you when you go out.'),
    ('yes', 'countryside', 'You should take a coat with you when you go out.'),
    ('yes', 'suburbs', 'I\'m not sure whether you should take an umbrella or a coat with you.'),
    ('no', None, 'No need for an umbrella or a coat, go as you are.'),
    ('maybe', None, 'Sorry, I didn\'t understand your response.'),
])
def test_should_take_umbrella_or_coat(
        mocker: MockerFixture,
        is_raining: str,
        city_or_countryside: str | None,
        expected_output: str) -> None:
    mocker.patch('builtins.input', side_effect=[is_raining, city_or_countryside])
    mock_stdout = mocker.patch('sys.stdout', new_callable=StringIO)
    challenges.should_take_umbrella_or_coat()
    outputted_lines = mock_stdout.getvalue().splitlines()
    assert len(outputted_lines) > 0, "There doesn't seem to be any output"
    assert len(outputted_lines) < 2, "There seem to be too many printed lines"
    is_raining_clause = f'An "is_raining" value of "{is_raining}"'
    city_or_countryside_clause = '' if city_or_countryside is None else f' and a "city_or_countryside" value of "{city_or_countryside}"'
    assert outputted_lines[-1] == expected_output, f"{is_raining_clause}{city_or_countryside_clause} should generate the output \"{expected_output}\""


@pytest.mark.parametrize('days, expected_cost', [
    (2, 120),
    (3, 160),
    (5, 280),
    (7, 370),
    (8, 430),
])
def test_calculate_car_hire_cost(
        days: int,
        expected_cost: int) -> None:
    cost = challenges.calculate_car_hire_cost(days)
    assert cost == expected_cost, f"The cost for {days} days should have been {expected_cost}"


@pytest.mark.parametrize('player_1_move, player_2_move, expected_output', [
    ('rock', 'rock', 'It\'s a draw.'),
    ('rock', 'paper', 'Player 2 wins!'),
    ('rock', 'scissors', 'Player 1 wins!'),
    ('paper', 'rock', 'Player 1 wins!'),
    ('paper', 'paper', 'It\'s a draw.'),
    ('paper', 'scissors', 'Player 2 wins!'),
    ('scissors', 'rock', 'Player 2 wins!'),
    ('scissors', 'paper', 'Player 1 wins!'),
    ('scissors', 'scissors', 'It\'s a draw.'),
])
def test_find_rock_paper_scissors_winner(
        mocker: MockerFixture,
        player_1_move: challenges.RockPaperScissorsMove,
        player_2_move: challenges.RockPaperScissorsMove,
        expected_output: str) -> None:
    mock_stdout = mocker.patch('sys.stdout', new_callable=StringIO)
    challenges.find_rock_paper_scissors_winner(player_1_move, player_2_move)
    outputted_lines = mock_stdout.getvalue().splitlines()
    assert len(outputted_lines) > 0, "There doesn't seem to be any output"
    assert len(outputted_lines) < 2, "There seem to be too many printed lines"
    assert outputted_lines[-1] == expected_output, f"Player 1 playing {player_1_move} and player 2 playing {player_2_move} should generate the output \"{expected_output}\""


@pytest.mark.parametrize('hours, minutes, seconds, expected_milliseconds', [
    (0, 0, 0, 0),
    (2, 10, 38, 7838000),
    (6, 21, 55, 22915000),
])
def test_calculate_milliseconds(
        hours: int,
        minutes: int,
        seconds: int,
        expected_milliseconds: int) -> None:
    milliseconds = challenges.calculate_milliseconds(hours, minutes, seconds)
    assert milliseconds == expected_milliseconds, f"{hours} hours, {minutes} minutes and {seconds} seconds should equal {expected_milliseconds} milliseconds"


@pytest.mark.parametrize('assignment_scores, expected_grade', [
    ([], '?'),
    ([70], 'C'),
    ([41, 68], 'E'),
    ([10, 40, 60], 'F'),
    ([99, 82, 91, 93], 'A'),
    ([51, 47, 72, 70, 65], 'D'),
    ([90, 94, 67, 68, 85, 81], 'B'),
])
def test_calculate_course_grade(
        assignment_scores: list[int],
        expected_grade: challenges.CourseGrade) -> None:
    grade = challenges.calculate_course_grade(assignment_scores)
    assert grade == expected_grade, f"A student with scores {assignment_scores} should receive a grade {expected_grade}"


@pytest.mark.parametrize('text, expected_variable_name', [
    ('', ''),
    (' ', '_'),
    (' My FAVOURITE   food', '_my_favourite___food'),
])
def test_convert_to_variable_name(
        text: str,
        expected_variable_name: str) -> None:
    variable_name = challenges.convert_to_variable_name(text)
    assert variable_name == expected_variable_name, f"The text \"{text}\" should correspond to the variable name \"{expected_variable_name}\""


@pytest.mark.parametrize('text, expected_boring_text', [
    ('', ''),
    ('!', '.'),
    ('I can\'t! Believe! It!', 'I can\'t. Believe. It.'),
    ('I can\'t! Believe!! It!!!', 'I can\'t. Believe. It.'),
])
def test_make_boring(
        text: str,
        expected_boring_text: str) -> None:
    boring_text = challenges.make_boring(text)
    assert boring_text == expected_boring_text, f"The text \"{text}\" should correspond to the boring text \"{expected_boring_text}\""


@pytest.mark.parametrize('sequence, expected_contains_duplicate', [
    ('', False),
    ((2, 7, 6, 3, 11), False),
    (['Feel', 'the', 'beat', 'from', 'the', 'tambourine'], True),
])
def test_check_for_duplicates(
        sequence: Sequence,
        expected_contains_duplicate: bool) -> None:
    contains_duplicate = challenges.check_for_duplicates(sequence)
    if isinstance(sequence, str):
        sequence = f'"{sequence}"'
    assert contains_duplicate == expected_contains_duplicate, f"The sequence {sequence} {'does' if expected_contains_duplicate else 'does not'} contain duplicates"
