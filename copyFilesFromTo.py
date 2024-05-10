import os
import shutil

def mover_imagens(diretorio_origem, diretorio_destino,extensions):
    for pasta_atual, subpastas, arquivos in os.walk(diretorio_origem):
        for arquivo in arquivos:
            if arquivo.lower().endswith(extensions):
                caminho_completo_origem = os.path.join(pasta_atual, arquivo)
                caminho_completo_destino = os.path.join(diretorio_destino, arquivo)
            
                shutil.copy2(caminho_completo_origem, caminho_completo_destino)
                print(f"Copied {caminho_completo_origem} to {caminho_completo_destino}")

extensions = (".txt", ".jpg", ".png",".JPG",".PNG")

source_folder = r"C:\Users\luanp\OneDrive\Área de Trabalho\EcoNoroeste\imagens"
destination_folder = r"C:\Users\luanp\OneDrive\Área de Trabalho\EcoNoroeste\unique_folder"

mover_imagens(source_folder, destination_folder,extensions)