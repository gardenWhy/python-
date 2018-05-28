user_file = 'user.txt'
lock_file = 'user_lock.txt'
with open(user_file, 'r') as f:
    user = f.read().split('\n')
    user_list = {}
    for r in user:
        name, password = r.split(',')
        user_list[name] = str(password)
with open(lock_file) as f:
    lock = f.read().split('\n')[:-1]


def login(username, password):
    if username in user_list:
        if username in lock:
            print('!!!=你的账号已经被锁定=!!!')
            return 0
        else:
            if username == user_list[username]:
                print("恭喜你登陆成功！欢迎使用系统！")
                return 0
            else:
                print("登陆失败！用户或密码错误")
                return 1
    else:
        print("登陆失败！用户或密码错误")
        return 2


const = 0
while const < 3:
    username = input("请输入你的用户名:")
    password = input("请输入你的密码:")
    result = login(username, password)
    if result == 0:
        break
    elif result == 3:
        break
    const += 1

    if const == 3:
        with open(lock_file, 'w') as f:
            f.write(username + '\n')
        print("输入错误三次，您的账户已被锁定，请联系管理员！")
