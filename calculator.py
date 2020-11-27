with open('password.txt','r') as pw:
    pwd = pw.read()
    pw.close()
pprint(""███████╗██╗██╗     ███╗   ███╗██████╗ ██╗     ███████╗
██╔════╝██║██║     ████╗ ████║██╔══██╗██║     ██╔════╝
███████╗██║██║     ██╔████╔██║██████╔╝██║     █████╗
╚════██║██║██║     ██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝
███████║██║███████╗██║ ╚═╝ ██║██║     ███████╗███████╗
╚══════╝╚═╝╚══════╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝

 ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗
██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝
██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                                   """)
                                                                                                                                                          """)
password = input('Please Enter tool password : ')

if password == pwd:
    first = int(input("Enter first Number : "))
    last = int(input("Enter last number : "))
    op = input("whant do you want : ")
    if op =='+':
        print(first + last)
    elif op == '-':
        print(first - last)
    elif op == '*':
        print == '*'
    elif op == '/':
        print(first / last)

    else:
        print("please Enter number only")
else:
    print ("invalid password"
            )
    print ("please contact thitethite080@gmail.com")

