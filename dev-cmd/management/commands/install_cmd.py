from django.core.management.base import BaseCommand
from main import settings
import os
import shutil


def copy_cmds_to_dirs():
    src = settings.BASE_DIR+"\dev-cmd\src"
    dest = settings.BASE_DIR
    src_files = os.listdir(src)
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        if (os.path.isfile(full_file_name)):
            shutil.copy(full_file_name, dest)

class Command(BaseCommand):

    def handle(self, **options):
        copy_cmds_to_dirs()
