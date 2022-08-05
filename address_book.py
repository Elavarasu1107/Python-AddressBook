import logging

logging.basicConfig(filename='address_book_log.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger()


class Contact:

    def __init__(self, details_dict):
        self.first_name = details_dict.get("first_name")
        self.last_name = details_dict.get("last_name")
        self.address = details_dict.get("address")
        self.city = details_dict.get("city")
        self.state = details_dict.get("state")
        self.pin = details_dict.get("pin")
        self.phone = details_dict.get("phone")
        self.email = details_dict.get("email")


class AddressBook:

    def __init__(self, book_type):
        self.book_type = book_type
        self.contact_dict = {}

    def add_contact(self, contact_model):
        """
        This function add contacts to the dictionary
        :param contact_model: type
        :return: None
        """
        try:
            self.contact_dict.update({contact_model.first_name: contact_model})
        except Exception as ex:
            logger.exception(ex)

    def display_contact(self):
        """
        This function displays the data in the dictionary
        :return: None
        """
        try:
            for key, value in self.contact_dict.items():
                print(f'{key} {value.last_name} {value.address} {value.city} {value.state} {value.pin}'
                      f' {value.phone} {value.email}')
        except Exception as ex:
            logger.exception(ex)

    def get_contact(self, name):
        """
        This function get the data of a contact
        :param name: string
        :return: object
        """
        try:
            return self.contact_dict.get(name)
        except Exception as ex:
            logger.exception(ex)

    def update_contact(self, contact_obj, updated_dict):
        """
        The function updates the contact in the dictionary if exist
        :param contact_obj: object
        :param updated_dict: dict
        :return: None
        """
        try:
            contact_obj.last_name = updated_dict.get("last_name")
            contact_obj.address = updated_dict.get("address")
            contact_obj.city = updated_dict.get("city")
            contact_obj.state = updated_dict.get("state")
            contact_obj.pin = updated_dict.get("pin")
            contact_obj.phone = updated_dict.get("phone")
            contact_obj.email = updated_dict.get("email")
        except Exception as ex:
            logger.exception(ex)

    def delete_contact(self, name):
        """
        This function deletes the contact in the dictionary
        :param name: string
        :return: None
        """
        try:
            if name in self.contact_dict:
                self.contact_dict.pop(name)
            else:
                print("Contact Not Found")
        except Exception as ex:
            logger.exception(ex)


class MultipleBook:

    def __init__(self):
        self.book_dict = {}

    def add_book(self, book_obj):
        """
        This function add a contact to the book
        :param book_obj: object
        :return: None
        """
        try:
            self.book_dict.update({book_obj.book_type: book_obj})
        except Exception as ex:
            logger.exception(ex)

    def display_book(self):
        """
        This function display the contacts in the book
        :return: None
        """
        try:
            for book_name, book_data in self.book_dict.items():
                print(f'Book Name: {book_name} Object: {book_data.contact_dict}')
        except Exception as ex:
            logger.exception(ex)

    def get_book(self, book_name):
        """
        This function retrieve contact in the particular book
        :param book_name: string
        :return: object
        """
        try:
            return self.book_dict.get(book_name)
        except Exception as ex:
            logger.exception(ex)

    def update_book(self, book_obj, updated_data_dict):
        """
        This function update the data in the book
        :param book_obj: object
        :param updated_data_dict: dict
        :return: None
        """
        try:
            book_obj.last_name = updated_data_dict.get("last_name")
            book_obj.address = updated_data_dict.get("address")
            book_obj.city = updated_data_dict.get("city")
            book_obj.state = updated_data_dict.get("state")
            book_obj.pin = updated_data_dict.get("pin")
            book_obj.phone = updated_data_dict.get("phone")
            book_obj.email = updated_data_dict.get("email")
        except Exception as ex:
            logger.exception(ex)

    def delete_book(self, book_name):
        """
        This function delete the book if exist
        :param book_name: string
        :return: None
        """
        try:
            if book_name in self.book_dict:
                self.book_dict.pop(book_name)
            else:
                print("Address Book Not Found")
        except Exception as ex:
            logger.exception(ex)


def add_contact_function():
    """
    This function call the add contact function Address Book class
    :return: None
    """
    try:
        book_name = input("Enter Book Name: ")
        book = multiple_book.book_dict.get(book_name)
        if book is None:
            book = AddressBook(book_name)
            multiple_book.add_book(book)
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        address = input("Enter Address: ")
        city = input("Enter City: ")
        state = input("Enter State: ")
        pin = input("Enter Pin: ")
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")
        details_dict = {"first_name": first_name, "last_name": last_name, "address": address, "city": city,
                        "state": state, "pin": pin, "phone": phone, "email": email}
        contact = Contact(details_dict)
        book.add_contact(contact)
    except Exception as ex:
        logger.exception(ex)


def display_contact_function():
    """
    This function call the display contact function Address Book class
    :return: None
    """
    try:
        book_name = input("Enter Book Name: ")
        book = multiple_book.book_dict.get(book_name)
        if book is not None:
            book.display_contact()
    except Exception as ex:
        logger.exception(ex)


def update_contact_function():
    """
    This function call the update contact function Address Book class
    :return: None
    """
    try:
        book_name = input("Enter Book Name to Update: ")
        book = multiple_book.book_dict.get(book_name)
        if book is None:
            print("Address Book Not Found")
        else:
            name = input("Enter a contact name to update: ")
            contact_obj = book.get_contact(name)
            if contact_obj is None:
                print("Contact Not Found")
            else:
                last_name = input("Enter Last Name: ")
                address = input("Enter Address: ")
                city = input("Enter City: ")
                state = input("Enter State: ")
                pin = input("Enter Pin: ")
                phone = input("Enter Phone: ")
                email = input("Enter Email: ")
                updated_dict = {"last_name": last_name, "address": address, "city": city,
                                "state": state, "pin": pin, "phone": phone, "email": email}
                book.update_contact(contact_obj, updated_dict)
    except Exception as ex:
        logger.exception(ex)


def delete_contact_function():
    """
    This function call delete contact function Address Book class
    :return: None
    """
    try:
        book_name = input("Enter Book Name to Update: ")
        book = multiple_book.book_dict.get(book_name)
        name = input("Enter a contact name to delete: ")
        book.delete_contact(name)
    except Exception as ex:
        logger.exception(ex)


def display_book_function():
    """
    This function call display book function Multiple Book class
    :return: None
    """
    try:
        multiple_book.display_book()
    except Exception as ex:
        logger.exception(ex)


def update_book_function():
    """
    This function call update book function Multiple Book class
    :return: None
    """
    try:
        book_name = input("Enter Book Name to Update: ")
        book = multiple_book.book_dict.get(book_name)
        if book is None:
            print("Address Book Not Found")
        else:
            name = input("Enter a contact name to update: ")
            contact_obj = book.get_contact(name)
            if contact_obj is None:
                print("Contact Not Found")
            else:
                last_name = input("Enter Last Name: ")
                address = input("Enter Address: ")
                city = input("Enter City: ")
                state = input("Enter State: ")
                pin = input("Enter Pin: ")
                phone = input("Enter Phone: ")
                email = input("Enter Email: ")
                updated_dict = {"last_name": last_name, "address": address, "city": city,
                                "state": state, "pin": pin, "phone": phone, "email": email}
                book.update_contact(contact_obj, updated_dict)
    except Exception as ex:
        logger.exception(ex)


def delete_book_function():
    """
    This function call delete book function Multiple Book class
    :return: None
    """
    try:
        book_name = input("Enter Book Name to delete: ")
        multiple_book.delete_book(book_name)
    except Exception as ex:
        logger.exception(ex)


if __name__ == '__main__':
    try:
        multiple_book = MultipleBook()
        while True:
            choice = int(input("Enter 1 to add Contact\n2 to display contact\n3 to update contact\n"
                               "4 to delete contact\n5 to display book\n6 to update book\n"
                               "7 to delete book\n0 to exit: "))
            if choice == 0:
                break
            choice_dict = {1: add_contact_function, 2: display_contact_function, 3: update_contact_function,
                           4: delete_contact_function, 5: display_book_function, 6: update_book_function,
                           7: delete_book_function}
            choice_dict.get(choice)()
    except Exception as e:
        logger.exception(e)

