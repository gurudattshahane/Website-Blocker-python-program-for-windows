import os
import ctypes, sys
import subprocess

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# def destruct_self():
#     subprocess.Popen(['del', sys.argv[0]], shell=True)

def main():
    path = os.path.join("C:\\Windows\\System32\\drivers\\etc","hosts")
    if os.path.exists(path):
        with open(path, 'a') as f:
            f.write("\n127.0.0.1 facebook.com")
            f.write("\n127.0.0.1 www.facebook.com")
            f.write("\n127.0.0.1 instagram.com")
            f.write("\n127.0.0.1 www.instagram.com")
            f.write("\n127.0.0.1 twitter.com")
            f.write("\n127.0.0.1 www.twitter.com")

if __name__ == '__main__':
    if is_admin():
        main()
        # destruct_self()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
