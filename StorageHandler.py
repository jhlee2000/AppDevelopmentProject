"""
HF
The improved version from StorageManager.py
This is to simplify the function of the class
and spilt the task into other classes
Do not change anything before asking(HF)
"""

import shelve

"""
StorageHandler deals with shelve (Persistent storage)
Every Management class will use this class to store
"""


class StorageHandler:

    def __init__(self):
        # error checking only
        print("\n[START OF STORAGE_MANAGEMENT INIT]")
        try:
            self.__db = shelve.open('storage.db', 'r')
            if self.__db.keys() != None:
                print(list(self.__db.keys()))
            self.__db.close()

        except Exception:
            print("Storage not found")
        print("[END OF STORAGE_MANAGEMENT INIT]\n")

    # Default is create dictionary for storage
    def create_new_storage(self, storage_key, dict=True):
        self.__db = shelve.open('storage.db', 'c')

        if (self.__is_key_found(storage_key) == False):

            if dict == True:
                self.__db[storage_key] = {}
                print("Created dictionary: {}".format(storage_key))
            elif dict == False:
                self.__db[storage_key] = []
                print("Created list")

        else:
            print("existing name of storage found, no duplication allowed: {}".format(storage_key))

        self.__db.close()

    def delete_storage(self, storage_key):

        self.__db = shelve.open('storage.db', 'c')

        if (self.__is_key_found(storage_key) == True):
            del self.__db[storage_key]
            print("Deleted storage: {}".format(storage_key))
        else:
            print("no keys found with the given name {} found, cannot delete".format(storage_key))

        self.__db.close()

    # This is use for updating of storage / major changes
    def set_storage(self, storage_key, item):

        self.__db = shelve.open('storage.db', 'c')
        if (self.__is_key_found(storage_key) == True):
            self.__db[storage_key] = item
            print("modified storage: {}".format(storage_key))

        else:
            print("Unable to set item due to storage name not found: {}".format(storage_key))
        self.__db.close()

    # Receive the whole db
    def get_storage(self, storage_key):
        self.__db = shelve.open('storage.db', 'c')

        if (self.__is_key_found(storage_key) == True):
            temp = self.__db[storage_key]
            print("storage name Found: {}".format(storage_key))

        else:
            temp = None
            print("storage name not found with the given key: {}".format(storage_key))

        self.__db.close()
        return temp

    # Get the keys of all the storage
    def get_keys(self):
        self.__db = shelve.open('storage.db', 'c')

        temp = list(self.__db.keys())
        self.__db.close()
        return temp

    # True or False if storage exist
    def storage_exist(self, storage_key):
        self.__db = shelve.open('storage.db', 'c')

        if (self.__is_key_found(storage_key) == True):
            self.__db.close()
            return True

        else:
            self.__db.close()
            return False

    # Show the keys
    def print_keys(self):
        self.__db = shelve.open('storage.db', 'r')
        key_list = self.__db.keys()

        print(list(key_list))
        self.__db.close()

    # For in class use only

    def __is_key_found(self, storage_key):

        key_list = self.__db.keys()
        if storage_key in list(key_list):
            # print(list(key_list))
            return True
        else:
            return False

