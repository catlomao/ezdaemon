
# ezdaemon

  

### python module allows you to run programs on the background

  

# --->  windows

  

```python

from ezdaemon.ezdaemon import win

win.cmd()

# method (via cmd)

win.powershell()

# method (via powershell)

```

# ---> linux

```python

from ezdaemon.ezdaemon import linux

linux.default()

linux.disown()

linux.nohup()

linux.setsid()

# a lot of method's you could use!

```

  

# ---> unix

```python

from ezdaemon.ezdaemon import UNIX

UNIX.default()

# works with any unix based

```
