r"""
## Run Programs in the Background in WINDOWS!
    ## 🪟🪟🪟🪟
    """
from os import system

#       !<<<<----- WINDOWS ----->>>>!

def powershell(Program):
        r"""# method 1 --> powershell"""
#region powershell
        system(f'powershell -Command "Start-Process \'{Program}\' -WindowStyle Hidden"')

        # <----- 1 ----->

def cmd(Program):
        r"""# method 2 --> cmd"""
#region cmd
        system(f'start /B "{Program}"')

        # <----- 2 ----->
