import os
import datetime
import git_commit
import argparse

def list_file_dates(directory,test,private):
    file_dates = {}
    exclude_prefixes = ('__', '.')  # exclusion prefixes
    os.chdir(directory)
    #print(directory)
    #print(os.listdir('.'))
    if '.git' not in os.listdir('.') or test:
        print("git isn't initialized, initializing")
        git_commit.init(directory,private,test)
    for root, dirs, files in os.walk('.'):
        dirs[:] = [dirname for dirname in dirs if not dirname.startswith(exclude_prefixes)]
        files = [x for x in files if not x.startswith(exclude_prefixes)]
        for file_name in files:

            file_path = os.path.join(root, file_name)
            
            # Retrieve file timestamps
            created = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
            modified = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
            accessed = datetime.datetime.fromtimestamp(os.path.getatime(file_path))

            baseline = datetime.datetime(2020, 5, 17,23, 55, 59, 342380)
            lst = []
            for i in [modified,accessed]:
                if i > baseline:
                    lst.append(i)
            
            print(f"  File: {file_path}")
            print(f"  Created: {created}")
            print(f"  Modified: {modified}")
            print(f"  Accessed: {accessed}")
            print(f" Date: {min(lst)}")
            if not test:
                git_commit.contribute(min(lst),file_path)
    return

# Example usage
parser = argparse.ArgumentParser(description='push commits dated on file update date')
parser.add_argument('directory', default = '.',
                    help='directory that will be commited and pushed')
parser.add_argument('-T','--test', action='store_true', default=False,
                    help='test the list without commiting')
parser.add_argument('-P','--private',action='store_true',default = False, help='public or private repository')
args = parser.parse_args()
test = args.test
directory_path = args.directory
private = args.private

list_file_dates(directory_path,test,private)

if not test:
    git_commit.run(['git', 'push'])
    print('\nRepository generation ' +
            '\x1b[6;30;42mcompleted successfully\x1b[0m!')