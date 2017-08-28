"""A library for launching and killing processes. Requires psutil."""
import psutil,shlex,subprocess

def which(program):
    import os
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None

class Process:
    """A process launched via launch.launch."""
    def __init__(self,cmd):
        args = shlex.split(cmd)
        args[0] = which(args[0])
        self.pid = subprocess.Popen(args).pid

    def kill(self):
        psutil.Process(self.pid).kill()

launchedprocesses = dict()

def launch(name,cmd):
    global launchedprocesses
    if not isRunning(name):
        launchedprocesses[name] = Process(cmd)

def kill(name):
    global launchedprocesses
    if isRunning(name):
        launchedprocesses[name].kill()
        del launchedprocesses[name]

def isRunning(name):
    global launchedprocesses
    return launchedprocesses.get(name,None) is not None
