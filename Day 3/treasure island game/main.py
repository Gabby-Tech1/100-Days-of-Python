print("Welcome to the Haunted Forest Adventure!")
    
print('''
      
                                          /\
       !__!          O   _    __         /LL\         __    _    O
   /\__('')__/\     /L\  \'._(oo)  _    /LLLL\    _  (OO)_.'/   /L\
  / _        _ \   /LLL\  `.   (_.'/   /LLLLLL\   \'._)   .'   /LLL\
  \/ \/\  /\/ \/  /LLLLL_.' _.'-..'     |.--.|     '..-'._ `'._LLLLL\
        mm         |.-.'__.'____________||__||____________'. __'.-.|
     \_  '\/` \_   ||_||\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\||_||
,__/  /`  ,\_ /'  [_____]\_\_\/\_\_\_\_\_\/\_\_\_\_\_\/\_\_\_\[_____]
   \\/---./  \\   /LLLLL\\_\_//\\\_\_\_\_//\\\_\_\_\_//\\_\_\_/LLLLL\
  .'\\, // '. \\ /LLLLLLL\==//__\\======//oo\\======//__\\===/LLLLLLL\
 /   \\//    \ \/LLLLLLLLL\__|__|________|__|________|__|__ /LLLLLLLLL\
:     \#\   _ :[___________]_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_[___________]
'   _//\ (_// '\|    _   |_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_|   _    |
 \  \ ( \ \/ / )|  .'|'.[__].=============================.[__].'|'.  |
  '. \ \) ).' / |  |-OO| || |          _________          | || |-+-|  |
    `-\/#(`  / /|  |_|_| || |    _    [_________]    _    | || |_|_|  |
     __\ ,\ / / |        || |  .'_'.   |__    _|   .'_'.  | ||        |
    (OO.-----.% |    _   || |  | | |_  (oo)_.'/|   | | |  | ||   _    |
     %%|R.I.P|%%|  .'|'. || |  |-+-|\'._)   .' |   |-+-|  | || .'|'.  |
    %%%|_____|%%|  |-+-| || |  |_|_| '..-'._ `'._  |_|_|  | || |OO-|  |
~^"^~[_________]|  |_|_| || | [_____]  |    '.__.'[_____] | || |_|_|  |
    ''"^"^"~~^"`|        || |          |       |          | ||        |
                | /\     || lc_________|_______|__________| ||        | _
                |_) )_   ||/                               \||      _ | ))
  .-~^"^-__    .' """ '._||_________________________________||______)\.'""'.
              / /\   /\ \__]XXXXXXXXXX[_________]XXXXXXXXXX[__]~"^.'""'.__.'
             |    /_\    |~"^~"^~"^~[_____________]~^"~_________  '.__.'~^"^
             |  _______  |                            /Keep Out/   -"~"-
              \ \W W W/ /                  _-        /________/
               '.\M M/.'               __--             / /
              '~"^"~"^~'.                              / /
   _-"^~"^"-                    __--              _-^~"^"~^-_      
''')

    # First choice
choice1 = input("You are at a fork in the road. Do you want to go 'left' or 'right'? ").lower()
if choice1 == 'left':
    print("You encounter a pack of wolves. Game Over!")
        
elif choice1 == 'right':
    print("You proceed safely deeper into the forest.")
else:
    print("Invalid choice. Game Over!")
        
    
    # Second choice
choice2 = input("You find a rickety bridge and a dark cave. Do you want to 'cross the bridge' or 'enter the cave'? ").lower()
if choice2 == 'cross the bridge':
    print("The bridge collapses and you fall into the river. Game Over!")
        
elif choice2 == 'enter the cave':
    print("You find a hidden passage that leads you further.")
else:
    print("Invalid choice. Game Over!")
        
    
    # Final choice
    choice3 = input("Inside the cave, you find two tunnels: 'tunnel A' and 'tunnel B'. Which one do you choose? ").lower()
    if choice3 == 'tunnel a':
        print("It's a dead end filled with poisonous gas. Game Over!")
    elif choice3 == 'tunnel b':
        print("Congratulations! You found the hidden treasure and won the game!")
    else:
        print("Invalid choice. Game Over!")