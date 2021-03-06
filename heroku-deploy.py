import os
import shutil
import sys

FILE_PATH = os.path.dirname(os.path.realpath(__file__))


def init_deploy():
    shutil.rmtree(os.path.join(FILE_PATH, 'web'))


def copy_backend():
    shutil.copytree(
        os.path.join(FILE_PATH, 'backend'),
        os.path.join(FILE_PATH, 'web'),
        ignore=shutil.ignore_patterns('node_modules', '.env', 'db.json', '.eslintrc.js', 'tests'))


def build_frontend():
    os.system('cd frontend && npm run build')


def copy_build_folder():
    shutil.copytree(
        os.path.join(FILE_PATH, 'frontend', 'build'),
        os.path.join(FILE_PATH, 'web', 'build'))
    shutil.rmtree(os.path.join(FILE_PATH, 'frontend', 'build'))


def main():
    init_deploy()
    copy_backend()
    build_frontend()
    copy_build_folder()


if __name__ == "__main__":
    main()
