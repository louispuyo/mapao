import os 
import sys
import errno


base_path = os.getenv('BASE_PATH')
default_files_list = ['app.py', 'awsgi.py', 'models.py']

def create(foldername):
    os.mkdir(foldername)
    os.chdir(foldername)
    os.mkdir('php')
    for default_file in default_files_list:
        f = open(base_path+(f'/{foldername}/{default_file}'), 'x')
    for default_file in default_files_list:
        with open(base_path+(f'/{foldername}/{default_file}'), 'a') as file:
            file.write(f'#! {default_file} --- utf8 *-*  python Pao  \n #check the documentation on : https://git@louispuyo/pao')
            file.close()            

if __name__ == "__main__":
    method = sys.argv[1]
    foldername = sys.argv[2]
    if method == '':
        os.system('echo --create --delete')
    if foldername == '':
        os.system('echo --filename missing')
    else:
        if method == 'create':
            create(foldername)
        else:
            print('---- pao ---- by louis')