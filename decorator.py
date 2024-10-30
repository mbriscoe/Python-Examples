def add_author(func):
    def wrapper(*args):
        func_args = func(*args)
        return f"{func_args}\nBy Mark Briscoe"

    return wrapper


@add_author
def print_article_title(title):
    return "Article Title: " + title


result = print_article_title("How To Be Great!")
print(result)
