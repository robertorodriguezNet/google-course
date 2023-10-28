#!/usr/bin/env python3

def validate_user(username, minlen):

    # assert genera un error con el mensaje indicado.
    # Es mejor usar raise
    assert type(username) == str, "username must be a string"

    # raise se usa para generar un error.
    # En este caso se genera un ValueError
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True
 