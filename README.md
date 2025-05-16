
# ezdaemon

  

### python module allows you to run programs on the background

  # note: inside the `()` you need to insert the Program path or name
# --->  windows

  

```python

from ezdaemon.ezdaemon import windows

windows.cmd()

# method (via cmd)

windows.powershell()

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

from ezdaemon.ezdaemon import unix

unix.default()


unix.disown()

# works with any unix based

```
