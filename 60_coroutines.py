import time


def searcher():
    # Task which takes 4 seconds to run
    book = "This book is on saksham"
    time.sleep(4)

    while True:
        text = yield
        if text in book:
            print(f"{text} is in book")
        else:
            print(f"{text} is not in book")


print("Search started")
search = searcher()
next(search)  # This would take 4 seconds
search.send("saksham")
word = input("Enter a word = ")
search.send(word)  # Now this would not take time again

search.close()  # This is how to close coroutine
# Now onwards this coroutine will not work until started again
