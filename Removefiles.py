import time
import os
import shutil

days=30
mypath="C:/Users/hiswa/OneDrive/Desktop/BYJUS/Projects/Mod3/c99/files"

seconds=time.time()-(days*24*60*60)
if (os.path.exists(mypath)) :
    for root, dirs, files in os.walk(mypath):
        if seconds >= os.stat(root).st_ctime:
            os.remove(root)
            deleted_folders_cnt += 1

            break
        else:
            for folder in dirs:
                subFoldPath = os.path.join(root,folder)
                if seconds >= os.stat(subFoldPath).st_ctime:
                    shutil.rmtree(subFoldPath)
                    deleted_files_cnt += 1

            for mother in files:
                filePath =os.path.join(root,mother)
                if seconds >= os.stat(subFoldPath).st_ctime:
                    os.remove(filePath)
                    deleted_mothers_cnt += 1

        
        for externalMother in files:
                filePath =os.path.join(root,externalMother)
                if seconds >= os.stat(subFoldPath).st_ctime:
                    os.remove(filePath)
                    deleted_externalMothers_cnt += 1
else:
    print("Path not found...")