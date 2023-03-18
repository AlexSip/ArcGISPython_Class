import os
path = r"C:\Sip_Task_1_Folder"

os.mkdir(path)
os.mkdir(path + "/draft_code")
os.mkdir(path + "/draft_code/pending")
os.mkdir(path + "/draft_code/complete")
os.mkdir(path + "/includes")
os.mkdir(path + "/layouts")
os.mkdir(path + "/layouts/default")
os.mkdir(path + "/layouts/post")
os.mkdir(path + "/layouts/post/posted")
os.mkdir(path + "/site")

os.rmdir(path + "/site")
os.rmdir(path + "/layouts/post/posted")
os.rmdir(path + "/layouts/post")
os.rmdir(path + "/layouts/default")
os.rmdir(path + "/layouts")
os.rmdir(path + "/includes")
os.rmdir(path + "/draft_code/complete")
os.rmdir(path + "/draft_code/pending")
os.rmdir(path + "/draft_code")
