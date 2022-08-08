import logging
import json
import csv

logging.basicConfig(filename='address_book_log.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger()


class Contact:

    def __init__(self, details_dict):
        self.book_name = details_dict.get("book_name")
        self.first_name = details_dict.get("first_name")
        self.last_name = details_dict.get("last_name")
        self.address = details_dict.get("address")
        self.city = details_dict.get("city")
        self.state = details_dict.get("state")
        self.pin = details_dict.get("pin")
        self.phone = details_dict.get("phone")
        self.email = details_dict.get("email")

    def as_json(self):
        """
        This function returns contact details as the dictionary
        :return: dict
        """
        try:
            return {"first_name": self.first_name, "last_name": self.last_name, "address": self.address,
                    "city": self.city, "state": self.state, "pin": self.pin, "phone": self.phone, "email": self.email}
        except Exception as ex:
            logger.exception(ex)

    def as_csv(self):
        try:
            return {"book_name": self.book_name, "first_name": self.first_name, "last_name": self.last_name,
                    "address": self.address, "city": self.city, "state": self.state,
                    "pin": self.pin, "phone": self.phone, "email": self.email}
        except Exception as ex:
            logger.exception(ex)

    def as_string(self):
        """
        This function returns contact details as string
        :return: string
        """
        try:
            return f'{self.first_name} {self.last_name} {self.address} {self.city} {self.state} {self.pin}' \
                   f'{self.phone} {self.email}'
        except Exception as ex:
            logger.exception(ex)


class AddressBook:

    def __init__(self, book_type):
        self.book_type = book_type
        self.contact_dict = {}
        self.json_contact_dict = {}
        self.csv_contact_dict = {}

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
                print(value.as_string())
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
                self.json_contact_dict.pop(name)
                self.csv_contact_dict.pop(name)
            else:
                print("Contact Not Found")
        except Exception as ex:
            logger.exception(ex)

    def add_json_contact(self):
        """
        This function add data to the json file
        :return: None
        """
        try:
            for key, value in self.contact_dict.items():
                self.json_contact_dict.update({key: value.as_json()})
        except Exception as ex:
            logger.exception(ex)

    def add_csv_contact(self):
        """
        This function add data to the csv file
        :return: None
        """
        try:
            for key, value in self.contact_dict.items():
                self.csv_contact_dict.update({key: value.as_csv()})
        except Exception as ex:
            logger.exception(ex)


class MultipleBook:

    def __init__(self):
        self.book_dict = {}
        self.file = "book_json.json"
        self.csv_file = "book_csv.csv"

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

    def add_json(self):
        """
        This function add data to the json file
        :return: None
        """
        try:
            json_dict = {}
            for name, obj in self.book_dict.items():
                json_dict.update({name: obj.json_contact_dict})
            with open(self.file, 'w') as file:
                json.dump(json_dict, file, indent=4)
                file.close()
        except Exception as ex:
            logger.exception(ex)

    def display_json(self):
        """
        This function display data in the json file
        :return: None
        """
        try:
            json_file = open("book_json.json")
            data = json.load(json_file)
            for details in data.items():
                print(details)
            json_file.close()
        except Exception as ex:
            logger.exception(ex)

    def add_csv(self):
        """
        This function add data to the csv file
        :return: None
        """
        try:
            with open(self.csv_file, 'w', newline="") as file:
                field_names = ['book_name', 'first_name', 'last_name', 'address', 'city', 'state', 'pin', 'phone', 'email']
                writer = csv.DictWriter(file, fieldnames=field_names)
                writer.writeheader()
                for key, value in self.book_dict.items():
                    for name, data in value.csv_contact_dict.items():
                        writer.writerow(data)
                file.close()
        except Exception as ex:
            logger.exception(ex)

    def display_csv(self):
        """
        This function display data in the csv file
        :return: None
        """
        try:
            with open(self.csv_file, mode='r') as file:
                csv_file = csv.reader(file)
                for rows in csv_file:
                    print(rows)
                file.close()
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
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        address = input("Enter Address: ")
        city = input("Enter City: ")
        state = input("Enter State: ")
        pin = input("Enter Pin: ")
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")
        details_dict = {"book_name": book_name, "first_name": first_name, "last_name": last_name, "address": address, "city": city,
                        "state": state, "pin": pin, "phone": phone, "email": email}
        contact = Contact(details_dict)
        book.add_contact(contact)
        book.add_json_contact()
        book.add_csv_contact()
        multiple_book.add_book(book)
        multiple_book.add_json()
        multiple_book.add_csv()
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
                book.add_json_contact()
                book.add_csv_contact()
                multiple_book.add_json()
                multiple_book.add_csv()
    except Exception as ex:
        logger.exception(ex)


def delete_contact_function():
    """
    This function call delete contact function Address Book class
    :return: None
    """
    try:
        book_name = input("Enter Book Name to delete: ")
        book = multiple_book.book_dict.get(book_name)
        name = input("Enter a contact name to delete: ")
        book.delete_contact(name)
        book.add_json_contact()
        book.add_csv_contact()
        multiple_book.add_json()
        multiple_book.add_csv()
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


def delete_book_function():
    """
    This function call delete book function Multiple Book class
    :return: None
    """
    try:
        book_name = input("Enter Book Name to delete: ")
        multiple_book.delete_book(book_name)
        multiple_book.add_json()
        multiple_book.add_csv()
    except Exception as ex:
        logger.exception(ex)


def display_json_function():
    """
    This function display the data in the json file
    :return: None
    """
    try:
        multiple_book.display_json()
    except Exception as ex:
        logger.exception(ex)


def display_csv_function():
    """
    This function display the data in the csv file
    :return: None
    """
    try:
        multiple_book.display_csv()
    except Exception as ex:
        logger.exception(ex)


if __name__ == '__main__':
    try:
        multiple_book = MultipleBook()
        while True:
            choice = int(input("Enter 1 to add Contact\n2 to display contact\n3 to update contact\n"
                               "4 to delete contact\n5 to display book\n""6 to delete book\n7 to display json data\n"
                               "8 to display csv file\n0 to exit: "))
            if choice == 0:
                break
            choice_dict = {1: add_contact_function, 2: display_contact_function, 3: update_contact_function,
                           4: delete_contact_function, 5: display_book_function, 6: delete_book_function,
                           7: display_json_function, 8: display_csv_function}
            choice_dict.get(choice)()
    except Exception as e:
        logger.exception(e)
