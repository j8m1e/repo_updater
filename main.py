import os
import datetime
import time
import git_commit

def list_file_dates(directory):
    print()
    file_dates = {}
    exclude_prefixes = ('__', '.')  # exclusion prefixes
    for root, dirs, files in os.walk(directory):
        
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
            for i in [created,modified,accessed]:
                if i > baseline:
                    lst.append(i)
            
            print(f"  File: {file_path}")
            # print(f"  Created: {created}")
            # print(f"  Modified: {modified}")
            # print(f"  Accessed: {accessed}")

            print(min(lst))
            git_commit.contribute(min(lst),file_path)
    return

# Example usage
directory_path = '.'
list_file_dates(directory_path)
