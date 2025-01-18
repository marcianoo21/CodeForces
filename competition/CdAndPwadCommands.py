n = int(input()) 
command = [] 
for _ in range(n):
    line = input()
    commands = line.split(' ')
    # print("elelel", commands)
    if commands[0] == 'pwd':
        command.append('/')
        print(*command)
    else:
        print("ckomand1", commands[1])
        if '..' in commands[1]:
            dir = commands[1].split('/')
            print("dir",dir)
            for ele in range(len(dir)):
                print("ele",dir[ele])
                if '..' not in dir[ele]:
                    command.append(dir[ele])
                    print("not in", command)
                else:
                    print("in", command)
                    command.pop(command[-1])
                    print("in afer", command)
        else:
            command.append(commands[1])
            # print(command + '/')
            print(command[:-1])
   

# tes = "/home/vasya"
# part = tes[tes.startswith('/'):-1]+ '/'
# tes = tes.replace(tes[tes.endswith('/'):1], '')
# print(tes)