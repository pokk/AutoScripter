""" Created by jieyi on 4/30/17. """
import os

from utils_zip import zip_files

temp_folder = '~/Documents'
root_remote_folder = '/Sync'


class DecoratorCheckDestination:
    def __call__(self, func):
        def wrapper(*args):
            remote_account = args[0].remote_account
            app_name = args[1]
            # Assign the message callback function.
            msg_callback = args[2]

            src = func(*args)

            if not src or 0 == len(src):
                print(f'NOTICE!! You don\'t install the {app_name}')
                return

            # Zip variables.
            zip_file_name = '.'.join([app_name.split('.')[0], 'zip'])
            full_zip_file = os.path.expanduser(os.path.join(temp_folder, zip_file_name))

            # Zip the app preferences.
            zip_files(src, full_zip_file)
            # Upload.
            # remote_account.upload_file(full_zip_file, os.path.join(root_remote_folder, zip_file_name))
            # Remove the temp file.
            # os.remove(full_zip_file)

        return wrapper


def main():
    pass


if __name__ == '__main__':
    main()
