class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    @staticmethod
    def validate_phone_number(phone_number):
        if len(phone_number) > 10 or len(phone_number) < 10:
            return False
        else:
            return True
class ContactList:
    all_contacts = []

    @classmethod
    def add_contact(cls, name, phone_number):
        # super().__init__(name, phone_number)
        if Contact.validate_phone_number(phone_number):
            new_contact = Contact(name, phone_number)
            cls.all_contacts.append(new_contact)
        else:
            print("Номер должен содержать 10 цифр")

print(ContactList.all_contacts)

ContactList.add_contact("Вася Пупкин", "0700100200")
ContactList.add_contact("Виктор Цой", "0500123456")

for contact in ContactList.all_contacts:
    print(contact.name, contact.phone_number)

ContactList.add_contact("John Doe", "5551234")
