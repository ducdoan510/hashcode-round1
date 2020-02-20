# input

class Library(object):
    def __init__(self, id, books, signup_time, books_scanned_per_day):
        self.id = id
        self.books = books
        self.activeDay = -1
        self.signup_time = signup_time
        self.books_scanned_per_day = books_scanned_per_day
        self.scanned_books = []

    def getNextBooks(self):
        cur_book_scores = [(book_scores[i], i) for i in [book_id for book_id in self.books if book_scores[book_id] > 0]]
        cur_book_scores = sorted(cur_book_scores, reverse=True) # [(book_score, index)]
        return cur_book_scores
    
    def value(self):
        k = max((day_cnt - self.signup_time), 0) * self.books_scanned_per_day
        return sum([book[0] for book in self.getNextBooks()[:k]])
    
    def score(self):
        nextBooks = self.getNextBooks()
        self.scanned_books.extend([item[1] for item in nextBooks])
        s = sum([item[0] for item in nextBooks])
        for _, book_idx in nextBooks:
            book_scores[book_idx] = 0
        return s
        


input_file = 'input/a_example.txt'

with open(input_file, 'r') as f:
    lines = []
    for line in f:
        lines.append(line)

book_cnt, library_cnt, day_cnt = [*map(int, lines[0].split())]
book_scores = [*map(int, lines[1].split())]
libraries = []

lines_idx = 2
for idx in range(library_cnt):
    library_book_count, library_signup_time, library_scanned_per_day = [*map(int, lines[lines_idx].split())]
    library_books = [*map(int, lines[lines_idx + 1].split())]
    libraries.append(Library(idx, library_books, library_signup_time, library_scanned_per_day))
    lines_idx += 2


scores = 0
active_libs = []
nextSignupDay = 0


def findNextLibrary(curr_date):
    if libraries:
        selected_lib = libraries.pop(0)
        selected_lib.activeDay = curr_date + selected_lib.signup_time
        active_libs.append(selected_lib)
        return selected_lib.activeDay
    return -1


def udpateLibraries():
    libraries.sort(key=lambda lib: lib.value(), reverse=True)


for day in range(day_cnt):
    udpateLibraries()
    if day == nextSignupDay:
        nextSignupDay = findNextLibrary(day)
    for lib in active_libs:
        if day > lib.activeDay:
            scores += lib.score()

with open('output/a_example.txt', 'w') as f_out:
    active_libs = [lib for lib in active_libs if lib.activeDay < day_cnt]
    f_out.writelines([str(len(active_libs)) + '\n'])
    for lib in active_libs:
        lib_result = "{} {}\n".format(lib.id, len(lib.scanned_books))
        f_out.writelines([lib_result])
        f_out.writelines([' '.join(map(str, lib.scanned_books)) + '\n'])

