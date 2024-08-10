import os
from subprocess import Popen


def init(directory,private = False,test= True):
    print(directory,private,test)
    if not test:
        run(['git', 'init'])
        run(['gh', 'repo', 'create', '[<name>]', '--private', '-s', '.'])






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
