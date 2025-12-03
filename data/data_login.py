CASOS_LOGIN = [
    ("standard_user", "secret_sauce", True),     # usuario válido, login exitoso
    ("locked_out_user", "secret_sauce", False),  # usuario bloqueado, login falla
    ("usuario_falso", "password_false", False),    # credenciales inválidas, login falla
]