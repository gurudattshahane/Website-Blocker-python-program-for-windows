import os
import ctypes, sys
import subprocess

# Checks whether the user have admin priviledges or not
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def main():
    path = os.path.join("C:\\Windows\\System32\\drivers\\etc","hosts")
    if os.path.exists(path):
        with open(path, 'a') as f:
            # Example websites
            f.write("\n127.0.0.1 facebook.com")
            f.write("\n127.0.0.1 www.facebook.com")
            f.write("\n127.0.0.1 instagram.com")
            f.write("\n127.0.0.1 www.instagram.com")

if __name__ == '__main__':
    if is_admin():
        main()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

# Note: If you want to revert the changes, then you will have to manually edit C:\\Windows\\System32\\drivers\\etc\\hosts file 
# and remove added entries.
# In this case:
# 127.0.0.1 facebook.com
# 127.0.0.1 www.facebook.com
# 127.0.0.1 instagram.com
# 127.0.0.1 www.instagram.com
