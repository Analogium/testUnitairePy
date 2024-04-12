# Définitions des fonctions
def capitalize_first_letter(s):
    """Capitalise la première lettre de la chaîne."""
    if not s:
        return ""
    return s[0].upper() + s[1:]

def reverse_string(s):
    """Inverse l'ordre des caractères dans la chaîne."""
    return s[::-1]

def add_exclamation(s):
    """Ajoute un point d'exclamation à la fin de la chaîne."""
    return s + "!"

# Tests des fonctions avec pytest
def test_capitalize_first_letter():
    assert capitalize_first_letter("hello") == "Hello"
    assert capitalize_first_letter("") == ""
    assert capitalize_first_letter("a") == "A"

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"

def test_add_exclamation():
    assert add_exclamation("hello") == "hello!"
    assert add_exclamation("") == "!"
    assert add_exclamation("a") == "a!"
