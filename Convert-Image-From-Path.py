import os
from PIL import Image
def convert_images_to_jpg(root_dir):
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            filepath = os.path.join(subdir, file)
            if filepath.endswith(".png") or filepath.endswith(".jpeg"):
                try:
                    with Image.open(filepath) as im:
                        im.convert("RGB").save(filepath.replace(".png", ".jpg").replace(".jpeg", ".jpg"))
                    os.remove(filepath)
                except Exception as e:
                    # print(e)
                    try:
                        f = filepath.replace(".png", ".jpg").replace(".jpeg", ".jpg")
                        with Image.open(filepath) as im:
                            print('deu certo')
                            os.remove(filepath)
                    except Exception as e:
                        print('Fotos não convertidas:',filepath)
                    

convert_images_to_jpg(r'C:\Users\luanp\Downloads\CCRMonitoracoes\teste\OneDrive_1_28-11-2023')