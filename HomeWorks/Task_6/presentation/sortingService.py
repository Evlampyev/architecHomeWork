from abc import ABC

from HomeWorks.Task_6.data.iBookSorting import Sorting


class SortingService(ABC):

    def coose_sorting(all_books: list) -> list:
        """Помощь пользователю в выборе способа сортировки книг для вывода на экран"""
        sort = int(input("--Сортировать:--\n"
                         "1 - не сортировать, \n"
                         "2 - по алфавиту, \n"
                         "3 - сортировать по цене по возрастанию: \n"
                         "4 - сортировать по цене убыванию: \n... "))
        if sort == 2:
            all_books = Sorting.by_author(all_books)
        elif sort == 3:
            all_books = Sorting.by_price(all_books)
        elif sort == 4:
            all_books = Sorting.by_price_reverse(all_books)

        return all_books
