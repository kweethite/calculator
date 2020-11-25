with open('password.txt','r') as pw:
    pwd = pw.read()
    pw.close()
print("""
 w:::::w         w:::::w         w:::::wee::::::::::::ee  l::::l   cc:::::::::::::::c oo:::::::::::oo  mm:::::::m  m:::::::mm   ee::::::::::::ee       t:::::::::::::::::t     oo:::::::::::oo        cc:::::::::::::::c  a::::::::::::a   l::::l   cc:::::::::::::::cu::::u    u::::u   l::::l   a::::::::::::a t:::::::::::::::::t     oo:::::::::::oo r::::rrr:::::::::r  
  w:::::w       w:::::::w       w:::::we::::::eeeee:::::eel::::l  c:::::::::::::::::co:::::::::::::::om::::::::::mm::::::::::m e::::::eeeee:::::ee     t:::::::::::::::::t    o:::::::::::::::o      c:::::::::::::::::c  aaaaaaaaa:::::a  l::::l  c:::::::::::::::::cu::::u    u::::u   l::::l   aaaaaaaaa:::::at:::::::::::::::::t    o:::::::::::::::or:::::::::::::::::r 
   w:::::w     w:::::::::w     w:::::we::::::e     e:::::el::::l c:::::::cccccc:::::co:::::ooooo:::::om::::::::::::::::::::::me::::::e     e:::::e     tttttt:::::::tttttt    o:::::ooooo:::::o     c:::::::cccccc:::::c           a::::a  l::::l c:::::::cccccc:::::cu::::u    u::::u   l::::l            a::::atttttt:::::::tttttt    o:::::ooooo:::::orr::::::rrrrr::::::r
    w:::::w   w:::::w:::::w   w:::::w e:::::::eeeee::::::el::::l c::::::c     ccccccco::::o     o::::om:::::mmm::::::mmm:::::me:::::::eeeee::::::e           t:::::t          o::::o     o::::o     c::::::c     ccccccc    aaaaaaa:::::a  l::::l c::::::c     cccccccu::::u    u::::u   l::::l     aaaaaaa:::::a      t:::::t          o::::o     o::::o r:::::r     r:::::r
     w:::::w w:::::w w:::::w w:::::w  e:::::::::::::::::e l::::l c:::::c             o::::o     o::::om::::m   m::::m   m::::me:::::::::::::::::e            t:::::t          o::::o     o::::o     c:::::c               aa::::::::::::a  l::::l c:::::c             u::::u    u::::u   l::::l   aa::::::::::::a      t:::::t          o::::o     o::::o r:::::r     rrrrrrr
      w:::::w:::::w   w:::::w:::::w   e::::::eeeeeeeeeee  l::::l c:::::c             o::::o     o::::om::::m   m::::m   m::::me::::::eeeeeeeeeee             t:::::t          o::::o     o::::o     c:::::c              a::::aaaa::::::a  l::::l c:::::c             u::::u    u::::u   l::::l  a::::aaaa::::::a      t:::::t          o::::o     o::::o r:::::r            
       w:::::::::w     w:::::::::w    e:::::::e           l::::l c::::::c     ccccccco::::o     o::::om::::m   m::::m   m::::me:::::::e                      t:::::t    tttttto::::o     o::::o     c::::::c     ccccccca::::a    a:::::a  l::::l c::::::c     cccccccu:::::uuuu:::::u   l::::l a::::a    a:::::a      t:::::t    tttttto::::o     o::::o r:::::r            
        w:::::::w       w:::::::w     e::::::::e         l::::::lc:::::::cccccc:::::co:::::ooooo:::::om::::m   m::::m   m::::me::::::::e                     t::::::tttt:::::to:::::ooooo:::::o     c:::::::cccccc:::::ca::::a    a:::::a l::::::lc:::::::cccccc:::::cu:::::::::::::::uul::::::la::::a    a:::::a      t::::::tttt:::::to:::::ooooo:::::o r:::::r            
         w:::::w         w:::::w       e::::::::eeeeeeee l::::::l c:::::::::::::::::co:::::::::::::::om::::m   m::::m   m::::m e::::::::eeeeeeee             tt::::::::::::::to:::::::::::::::o      c:::::::::::::::::ca:::::aaaa::::::a l::::::l c:::::::::::::::::c u:::::::::::::::ul::::::la:::::aaaa::::::a      tt::::::::::::::to:::::::::::::::o r:::::r            
          w:::w           w:::w         ee:::::::::::::e l::::::l  cc:::::::::::::::c oo:::::::::::oo m::::m   m::::m   m::::m  ee:::::::::::::e               tt:::::::::::tt oo:::::::::::oo        cc:::::::::::::::c a::::::::::aa:::al::::::l  cc:::::::::::::::c  uu::::::::uu:::ul::::::l a::::::::::aa:::a       tt:::::::::::tt oo:::::::::::oo  r:::::r            
           www             www            eeeeeeeeeeeeee llllllll    cccccccccccccccc   ooooooooooo   mmmmmm   mmmmmm   mmmmmm    eeeeeeeeeeeeee                 ttttttttttt     ooooooooooo            cccccccccccccccc  aaaaaaaaaa  aaaallllllll    cccccccccccccccc    uuuuuuuu  uuuullllllll  aaaaaaaaaa  aaaa         ttttttttttt     ooooooooooo    rrrrrrr            
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

