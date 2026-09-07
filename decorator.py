def add_author(func):
    def wrapper(*args):
        func_args = func(*args)
        return f"{func_args}\nBy Mark Briscoe"

    return wrapper


@add_author
def print_article_title(title):
    return "Article Title: " + title


@add_author
def quote_of_the_day(quote):
    return "Quote of the day: " + quote


result = quote_of_the_day("We love mixins!")

print(result)
