import os
import shutil
import time


class FileManager:
    def __init__(self):
        self.root_dir = os.path.dirname(os.path.abspath("main.py"))
        self.limpar_diretorio("downloads")

    def concatenar_root_com_path(self, path):
        return os.path.join(self.root_dir, path)

    def concatenar_paths(self, path1, path2):
        return os.path.join(path1, path2)

    def criar_diretorio(self, dir_name):
        os.mkdir(self.concatenar_root_com_path(dir_name))

    def deletar_diretorio(self, dir_name):
        path = self.concatenar_root_com_path(dir_name)
        if os.path.exists(path):
            shutil.rmtree(path)

    def limpar_diretorio(self, dir_name):
        self.deletar_diretorio(dir_name)
        self.criar_diretorio(dir_name)

    def renomear_arquivo(self, file_path, new_file_path):
        if os.path.exists(file_path):
            os.rename(file_path, new_file_path)

    def renomear_relatorios(self):
        downloads_path = self.concatenar_root_com_path("downloads")
        os.chdir(downloads_path)
        files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
        nomes = ["CallHistoryHistorico.CSV",
                 "HistoricoCallback.CSV",
                 "DiallerCallsHistorico.CSV",
                 "PesquisaSatisfacao.CSV",
                 "AgentActionsHistorico.CSV"]

        for index in range(len(files)):
            old_file_path = self.concatenar_paths(downloads_path, files[index])
            new_file_path = self.concatenar_paths(downloads_path, nomes[index])
            self.renomear_arquivo(files[index], new_file_path)
