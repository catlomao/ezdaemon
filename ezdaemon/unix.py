r"""
    ## Run Programs in the background , on
    ## ANY UNIX -->  FREEBSD , OPENBSD , MACOS  , etc....
    """
from os import system

#       !<<<<----- UNIX ----->>>>!

def default(Program):
        r"""## works with any UNIX-based"""

        system(f"{Program} &")

        # <----- END ----->
