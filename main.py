# input


class Library(object):
    def __init__(self, books, signup_time, books_scanned_per_day):
        self.books = books
        self.signup_time = signup_time
        self.books_scanned_per_day = books_scanned_per_day


input_file = 'input/' + input()

with open(input_file, 'r') as f:
    lines = []
    for line in f:
        lines.append(line)

book_cnt, library_cnt, day_cnt = [*map(int, lines[0].split())]
book_scores = [*map(int, lines[1].split())]
libraries = []

lines_idx = 2
for _ in range(library_cnt):
    library_book_count, library_signup_time, library_scanned_per_day = [*map(int, lines[lines_idx].split())]
    library_books = [*map(int, lines[lines_idx + 1].split())]
    libraries.append(Library(library_books, library_signup_time, library_scanned_per_day))

