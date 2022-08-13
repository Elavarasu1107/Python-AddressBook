import pytest
from address_book import Contact, AddressBook, MultipleBook


@pytest.fixture
def contact_object():
    return Contact({"first_name": "Ela", "last_name": "Appu", "address": "11A", "city": "Salem",
                    "state": "Tamil Nadu", "pin": "654321", "phone": "9087654321", "email": "abc@gmail.com"})


@pytest.fixture
def book():
    return AddressBook("Family")


@pytest.fixture
def multiple_book():
    return MultipleBook()


def test_add_contact(contact_object, book):
    assert len(book.contact_dict) == 0
    book.add_contact(contact_object)
    assert len(book.contact_dict) == 1


def test_get_contact(contact_object, book):
    book.add_contact(contact_object)
    actual = book.get_contact("Ela")
    assert actual == contact_object


def test_update_contact(contact_object, book):
    book.add_contact(contact_object)
    updated_dict = {"first_name": "Ela", "last_name": "Appusamy", "address": "11A", "city": "Salem",
                    "state": "Tamil Nadu", "pin": "654321", "phone": "9087654321", "email": "efg@gmail.com"}
    book.update_contact(contact_object, updated_dict)
    assert contact_object.last_name == "Appusamy"
    assert contact_object.email == "efg@gmail.com"


def test_delete_contact(contact_object, book):
    book.add_contact(contact_object)
    assert len(book.contact_dict) == 1
    book.delete_contact("Ela")
    assert len(book.contact_dict) == 0


def test_add_book(contact_object, book, multiple_book):
    book.add_contact(contact_object)
    assert len(multiple_book.book_dict) == 0
    multiple_book.add_book(book)
    assert len(multiple_book.book_dict) == 1


def test_get_book(contact_object, book, multiple_book):
    book.add_contact(contact_object)
    multiple_book.add_book(book)
    actual = multiple_book.get_book("Family")
    assert actual == book


def test_delete_book(contact_object, book, multiple_book):
    book.add_contact(contact_object)
    multiple_book.add_book(book)
    assert len(multiple_book.book_dict) == 1
    multiple_book.delete_book("Family")
    assert len(multiple_book.book_dict) == 0
