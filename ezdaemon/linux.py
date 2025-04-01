from os import system

#       !<<<<----- LINUX ----->>>>!
class linux:
    r"""  
## Run Programs in the Background in LINUX!
##        🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧
    """
    def default(Program):
        r"""# method 1 --> default"""

        system(f"{Program} &")

        # <----- 1 ----->

    def nohup(Program):
        """# method 2 --> nohup"""

        system(f"nohup {Program} &>/dev/null &")

        # <----- 2 ----->

    def disown(Program):
        """# method 3 --> disown"""

        system(f"{Program} & disown")

        # <----- 3 ----->

    def setsid(Program):
        """# method 4 --> setsid"""

        system(f"setsid {Program} &>/dev/null &")

        # <----- 4 ----->