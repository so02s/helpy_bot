
def split_text(text, max_length=4000):
    """Разбивает текст на части, каждая из которых не превышает max_length символов."""
    return [text[i:i + max_length] for i in range(0, len(text), max_length)]