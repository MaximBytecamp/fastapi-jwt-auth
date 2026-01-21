import bcrypt


def get_password_hash(password: str) -> str:
    """
    Хеширует пароль с помощью bcrypt.
    
    Args:
        password: Пароль в открытом виде
        
    Returns:
        Хешированный пароль
    """

    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed.decode("utf-8")
