r"""  
## Run Programs in the Background in LINUX!
##        🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧
    """
from os import system

#       !<<<<----- LINUX ----->>>>!
def default(Program):
        r"""# method 1 --> default"""
#region default
        system(f"{Program} &")

        # <----- 1 ----->

def nohup(Program):
        """# method 2 --> nohup"""
#region nohup
        system(f"nohup {Program} &>/dev/null &")

        # <----- 2 ----->

def disown(Program):
        """# method 3 --> disown"""
#region disown
        system(f"{Program} & disown")

        # <----- 3 ----->

def setsid(Program):
        """# method 4 --> setsid"""
#region setsid
        system(f"setsid {Program} &>/dev/null &")

        # <----- 4 ----->
