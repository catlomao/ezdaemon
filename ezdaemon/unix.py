r"""
    ## Run Programs in the background , on
    ## ANY UNIX -->  FREEBSD , OPENBSD , MACOS  , etc....
    """
from os import system

#       !<<<<----- UNIX ----->>>>!

def default(Program):
        r"""## works with any UNIX-based"""

        system(f"{Program} &")
        # <----- 1 ----->


def disown(Program):
        """# method 2 --> disown"""

        system(f"{Program} & disown")

        # <----- 2 ----->

        # <----- END ----->
