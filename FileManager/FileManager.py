import os
import shutil
import time


class FileManager:
    def __init__(self):
        self.root_dir = os.path.dirname(os.path.abspath("main.py"))
        self.atto_reports_automation_log = os.path.abspath(
            "atto_reports_automation.log")

    def join_root_with_path(self, dir_name):
        return os.path.join(self.root_dir, dir_name)

    def join_paths(self, dir1, dir2):
        return os.path.join(dir1, dir2)

    def create_directory(self, dir_name):
        os.mkdir(self.join_root_with_path(dir_name))

    def delete_directory(self, dir_name):
        path = self.join_root_with_path(dir_name)
        if os.path.exists(path):
            shutil.rmtree(path)

    def clear_directory(self, dir_name):
        self.delete_directory(dir_name)
        self.create_directory(dir_name)

    def rename_file(self, file_path, new_file_path):
        if os.path.exists(file_path):
            os.rename(file_path, new_file_path)

    def latest_downloaded_file(self, num_file):
        downloads_path = self.join_root_with_path(
            "downloads")
        os.chdir(downloads_path)
        while True:
            files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
            if (len(files) < num_file):
                time.sleep(1)
            else:
                newest = files[-1]
                if ".crdownload" in newest:
                    time.sleep(1)
                else:
                    return newest
