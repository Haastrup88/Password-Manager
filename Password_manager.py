from cryptography.fernet import Fernet
print('Welcome to Oracle Tech'+ '\n' + 'The application is called password manager, a platform where you save and view saved password!')
ready=input("Press 'yes' to continue and 'no' to end the process:").lower()
if ready!='yes':
    quit()
else:
    pass


'''def write_key():
    key=Fernet.generate_key()
    with open('key.key','wb') as key_file:
        key_file.write(key)'''

def read_key():
    file=open('key.key','rb') 
    key=file.read()
    file.close()
    return key


master_password=input('Enter the master password:').lower()
key=read_key()
fer=Fernet(key)

def add():
    usname=input('Enter the username:')
    pwd=input('Enter the password:')
    with open('password.txt','a') as f:
        f.write(usname+'|'+(fer.encrypt(pwd.encode()).decode())+'\n')


def view():
    with open('password.txt','r') as f: 
        for line in f:
            data=line.rstrip()
            username,password=data.split('|')
            print(f"Username:{username} | Password:{(fer.decrypt(password.encode()).decode())}")

while True:
    mode=input('Do you want to add or view password:(add/view).Press q to quit:').lower()
    if mode=='q':
        break
    if mode=='add':
        add()
    elif mode=='view':
        view()
    else:
        print('Invalid Input!')
        continue



