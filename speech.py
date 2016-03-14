from subprocess import Popen, PIPE
import json


SPEECH = 'cscript "C:\Program Files\Jampal\ptts.vbs"'


def say(text):

    proc = Popen(["echo", text, "|", SPEECH], stdout=PIPE)
    stdoutdata, stderrdata = proc.communicate()
