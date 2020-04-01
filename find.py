import os

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
files = []


def get_files():
    try:
        drives = get_drive_letters()
        for i in range(len(drives)):
            drives[i] += '\\'
        for i in range(len(drives)):
            get_mp3_files_from_drive(drives[i])
    except:
        pass
    
    
    return files


def update_list(path):
    files.append(path)

def get_drive_letters():
    drives = []
    for letter in letters:
        if(os.path.exists(letter+':')):
            drives.append(letter+':')
    return drives

def check_file(name):
    # Put your condition down here!
    if(name):
        return True
    return False

def get_mp3_files_from_drive(drive):
    try:
        targeted_files = []
        for root, dirs, files in os.walk(drive, topdown=True):
            for d in dirs:
                ##Uncomment these to search through the hidden folders
                ## if(d[0]=='.'):
                    ## dirs.remove(d)
                ## elif(d=='$RECYCLE.BIN'):
                    ## dirs.remove(d)
            for name in files:
                if(check_audio(name)):
                    update_list(os.path.join(root, name))
    except:
        pass

if(__name__ == "__main__"):
    get_files()
