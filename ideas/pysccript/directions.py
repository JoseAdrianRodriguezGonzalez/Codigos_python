import os
import glob
import shutil
#zipfiles = glob.glob("bravos.boots.and.hats/*.json.xz")

#for py_file in zipfiles:
#    try:
#        os.remove(py_file)
#    except OSError as e:
#        print(f"Error:{ e.strerror}")
images = glob.glob("bravos.boots.and.hats/*.jpg")
for image in images:  
    try:
        os.replace(image,"\ newimages\ ")
    except OSError as e:
        print(f'Error{e.strerror}')