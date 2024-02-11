import handle_user_input as hui
import os

def print_banner():
    print("""

 ____  ____  ____  __ _  ____  __  ____    ____   __  ____ 
(    \(  __)/ ___)(  / )(_  _)/  \(  _ \  (  _ \ /  \(_  _)
 ) D ( ) _) \___ \ )  (   )( (  O )) __/   ) _ ((  O ) )(  
(____/(____)(____/(__\_) (__) \__/(__)    (____/ \__/ (__) 
                                                                             

    """)



def main():
    print_banner()
    hui.execute_user_command()

main()