import IPython
from google.colab import output
import subprocess
import sys
import os

my_env = os.environ.copy()
del my_env["DEBIAN_FRONTEND"]
my_env["PS1"] = "\[\033[01;36m\]\h\[\033[00m\] [bash]\[\033[01;34m\] \w $\[\033[00m\] "
my_env["PROMPT_COMMAND"] = "unset PROMPT_COMMAND ; set -m ; clear"
ON_POSIX = 'posix' in sys.builtin_module_names
proc = subprocess.Popen("bash --noprofile --norc -i 2>&1", shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, bufsize=1, universal_newlines = True, close_fds=ON_POSIX, env=my_env)
proc.stdin.flush()

import threading
import time
from queue import Queue, Empty
from threading  import Thread
lock = threading.Lock()

def log(s):
  with lock:
     js_code = "console.log(\"%s\");" % (s)
     display(IPython.display.Javascript(js_code))     

def bash_rcv(out, qq):
    log("bash_rcv receiver started")
    while True:
      s = out.read(1)
      if s == None or s == "":
          time.sleep(0.1)
          log("sleeping")
          continue
      qq.put(s)

q = Queue()
t = Thread(target=bash_rcv, args=(proc.stdout, q))
t.daemon = True
t.start()

def getc(unused):
  tab = []
  try:
     while True:
       cc = q.get_nowait()
       for ccc in cc:
          c = ord(ccc)
          tab.insert(0,c)
          if (c == 10):
            tab.insert(0, 13)
  except:
     pass
  if tab != []:
     js_code = "window.gotstring(%s);" % (tab[::-1].__str__())
     display(IPython.display.Javascript(js_code));
  return IPython.display.JSON({'result': "[]"})    

def send(c):
  proc.stdin.write("%s" % ''.join(c))
  proc.stdin.flush()
  return IPython.display.JSON({'result': "[]"})

output.register_callback('notebook.Send', send)
output.register_callback('notebook.Getc', getc)

content = '''
<div class="container" style="height:400px">
 <div id="terminal0" style="height:400px">
  
   </div>
 </div>
</div>

<script>

var to_send_buffer = "";
var term = null;
var io = null;

function gotchar(c) {
  io.print(String.fromCharCode(c));
};

window.gotchar = gotchar;

function gotstring(c) {
  io.print(String.fromCharCode.apply(null, c));
};

window.gotstring = gotstring;


heartbeat = 0;

async function data_monitor() {
  heartbeat += 1;
  if (to_send_buffer != "") {
    var newv = to_send_buffer;
    to_send_buffer = "";
    var result = await window.google.colab.kernel.invokeFunction('notebook.Send', [newv], {});
  }
}

async function setupHterm() {
  term = new hterm.Terminal();
  term.onTerminalReady = function() {
    io = this.io.push();

    const encoder = new TextEncoder();

    io.onVTKeystroke = (string) => {
        to_send_buffer = to_send_buffer + string;
        //ws.send(encoder.encode(string));
    };
    this.setCursorVisible(true);

    this.keyboard.bindings.addBindings({
      // Allow page refreshing.
      'Ctrl-R': 'PASS',
      // Fullscreen shortcut.
      'F11': 'PASS',
    });
  };
  term.decorate(document.querySelector('#terminal0'));
  term.installKeyboard();
  console.log("term initialized");
}


function onInit() {
     console.log("onInit");
     setTimeout(1000, setupHterm());
     setInterval(function() { data_monitor() }, 10);
     setInterval(function() { window.google.colab.kernel.invokeFunction('notebook.Getc', [""], {}); }, 50);     
}

async function startTerm() {
        const script = document.createElement('script');
        script.type = 'text/javascript';
        script.src = `/nbextensions/google.colab/hterm_all.js`;
        script.onload = async function() {
          await lib.init(onInit);
          console.log("init done");   
        }
        document.body.appendChild(script);
}
startTerm();
</script>
'''

display(IPython.display.HTML(content))
