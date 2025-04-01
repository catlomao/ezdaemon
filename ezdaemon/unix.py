from os import system

#       !<<<<----- UNIX ----->>>>!
class UNIX:
    r"""
    ## Run Programs in the background , on
    ## ANY UNIX -->  FREEBSD , OPENBSD , MACOS  , etc....
    """
    def default(Program):
        r"""## works with any UNIX-based"""

        system(f"{Program} &")

        # <----- END ----->