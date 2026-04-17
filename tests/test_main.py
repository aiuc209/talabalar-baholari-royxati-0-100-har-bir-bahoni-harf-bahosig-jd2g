import pytest

def grade_letter(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'

def test_grade_letter():
    assert grade_letter(95) == 'A'
    assert grade_letter(85) == 'B'
    assert grade_letter(75) == 'C'
    assert grade_letter(65) == 'D'
    assert grade_letter(55) == 'F'
    assert grade_letter(0) == 'F'

def test_grade_letter_invalid():
    with pytest.raises(TypeError):
        grade_letter('A')

def test_grade_letter_out_of_range():
    with pytest.raises(ValueError):
        grade_letter(105)
    with pytest.raises(ValueError):
        grade_letter(-5)

def grade_letter_list(grades):
    return [grade_letter(grade) for grade in grades]

def test_grade_letter_list():
    assert grade_letter_list([95, 85, 75, 65, 55]) == ['A', 'B', 'C', 'D', 'F']

def test_grade_letter_list_empty():
    assert grade_letter_list([]) == []
