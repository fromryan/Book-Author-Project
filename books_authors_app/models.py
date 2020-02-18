from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<Book object: {self.title},{self.desc},{self.authors}, {self.id}>"




class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    books = models.ManyToManyField(Book, related_name='authors')
    notes = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<Author object: {self.first_name},{self.last_name},{self.books}, {self.notes}>"




# book1 = Book.objects.create(title='C Sharp',desc='')
# book2 = Book.objects.create(title='Java',desc='')
# book3 = Book.objects.create(title='Python',desc='')
# book4 = Book.objects.create(title='PHP',desc='')
# book5 = Book.objects.create(title='Ruby',desc='')

# author1 = Author.objects.create(first_name='Emily', last_name='Dickinson')
# author2 = Author.objects.create(first_name='Fyodor', last_name='Dostoevksy')
# author3 = Author.objects.create(first_name='William', last_name='Shakespeare')
# author4 = Author.objects.create(first_name='Lau', last_name='Tzu')
# author5 = Author.objects.create(first_name='Jane', last_name='Austen')

# book1_update = Book.objects.get(title='C Sharp')
# book1_update.title = 'C #'
# book1.book1_update.save()

# author1_update = Author.objects.get(first_name='Emily')
# author1_update.first_name = 'Bill'
# author1_update.save()

# book1.authors.add(author2)
# book2.authors.add(author2)
# book3.authors.add(author3)

# book1.authors.add(author3)
# book2.authors.add(author3)
# book3.authors.add(author3)
# book4.authors.add(author3)

# all_books = Book.objects.all()
# all_books.authors.add(author4)

# all_authors_for_book3 = book3.authors.all()


# Book.objects.get(title='Python').authors.remove(author2)

# book2.authors.add(author5)

# author1.books.all()

# book5.authors.all()