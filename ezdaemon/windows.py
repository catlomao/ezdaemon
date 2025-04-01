from os import system

#       !<<<<----- WINDOWS ----->>>>!
class win:
    r"""
## Run Programs in the Background in WINDOWS!
    ## 🪟🪟🪟🪟
    """
    def powershell(Program):
        r"""# method 1 --> powershell"""

        system(f'Start-Process "{Program}" -WindowStyle Hidden')

        # <----- 1 ----->

    def cmd(Program):
        r"""# method 2 --> cmd"""

        system(f'start /B "{Program}"')

        # <----- 2 ----->