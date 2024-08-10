import os
from subprocess import Popen


def main(directory,repository,user_name,user_email,commit_time):
    if repository is not None:
        start = repository.rfind('/') + 1
        end = repository.rfind('.')
        directory = repository[start:end]

    os.chdir(directory)

    if user_name is not None:
        run(['git', 'config', 'user.name', user_name])

    if user_email is not None:
        run(['git', 'config', 'user.email', user_email])

    contribute(commit_time)

    if repository is not None:
        run(['git', 'push', '-u', 'origin', 'main'])

    print('\nRepository generation ' +
          '\x1b[6;30;42mcompleted successfully\x1b[0m!')


def contribute(date,path):
    # with open(os.path.join(os.getcwd(), 'README.md'), 'a') as file:
    #     file.write(message(date) + '\n\n')
    run(['git', 'add', path])
    run(['git', 'commit', '-m', '"%s"' % message(date),
         '--date', date.strftime('"%Y-%m-%d %H:%M:%S"')])


def run(commands):
    Popen(commands).wait()


def message(path):
    return "updated %s" %path
