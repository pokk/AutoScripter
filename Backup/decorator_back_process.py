""" Created by jieyi on 4/30/17. """
import os
from shutil import rmtree, copyfile, copytree

from Backup import warning_str


class DecoratorCheckDestination:
    @staticmethod
    def remove_backup(path):
        if os.path.isdir(path):
            rmtree(path)
        elif os.path.isfile(path):
            os.remove(path)

    @staticmethod
    def copy_backup(src, dst):
        if os.path.isdir(src):
            copytree(src, dst)
        elif os.path.isfile(src):
            copyfile(src, dst)

    def __call__(self, func):
        def wrapper(*args):
            destination_path = os.path.expanduser('~/Dropbox')
            # Checking if Dropbox is installed or not.
            if os.path.exists(destination_path):
                sync_folder = '/'.join([destination_path, 'Sync'])
                # Checking if sync folder exists or not.
                if not os.path.exists(sync_folder):
                    # If not, create it.
                    os.mkdir(sync_folder)

                src, dst = func(args[0], args[1], sync_folder)

                # If there exists a src preference, then remove it.
                for s, d in zip(src, dst):
                    # Ignore the src which isn't exist.
                    if not os.path.exists(s):
                        print(warning_str % s.split('/')[-1])
                        continue
                    if os.path.exists(d):
                        self.remove_backup(d)
                    # For that there are only file.
                    target_folder = '/'.join(d.split('/')[:-1])
                    if not os.path.exists(target_folder):
                        # If not, create it.
                        os.mkdir(target_folder)

                    # Sync the preference.
                    self.copy_backup(s, d)

                    print(f'Finished sync {d.split("/")[-1]} 👍👍👍👍')
            else:
                print(warning_str % 'Dropbox')

        return wrapper


def main():
    pass


if __name__ == '__main__':
    main()
