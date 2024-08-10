import os
from subprocess import Popen


def main(directory,repository):
    if repository is not None:
        start = repository.rfind('/') + 1
        end = repository.rfind('.')
        directory = repository[start:end]

    os.chdir(directory)






def contribute(date,path):
    # with open(os.path.join(os.getcwd(), 'README.md'), 'a') as file:
    #     file.write(message(date) + '\n\n')
    run(['git', 'add', path])
    run(['git', 'commit', '-m', '"%s"' % message(path),
         '--date', date.strftime('"%Y-%m-%d %H:%M:%S"')])


def run(commands):
    Popen(commands).wait()


def message(path):
    return "updated %s" %path
