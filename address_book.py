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

    def __init__(self, contact_type):
        self.contact_type = contact_type
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


def add_contact_function():
    try:
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
    try:
        book.display_contact()
    except Exception as ex:
        logger.exception(ex)


def update_contact_function():
    try:
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
    try:
        name = input("Enter a contact name to delete: ")
        book.delete_contact(name)
    except Exception as ex:
        logger.exception(ex)


if __name__ == '__main__':
    try:
        book = AddressBook("contact")
        while True:
            choice = int(input("Enter 1 to add Contact\n2 to display contact\n3 to update contact\n"
                               "4 to delete contact\n0 to exit: "))
            if choice == 0:
                break
            choice_dict = {1: add_contact_function, 2: display_contact_function, 3: update_contact_function,
                           4: delete_contact_function}
            choice_dict.get(choice)()
    except Exception as e:
        logger.exception(e)

