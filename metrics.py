import sys
import psutil

try:
    metric_os = sys.argv[1]
except Exception:
    print("You don't use any argument. Set - cpu or mem")
    sys.exit(1)

if metric_os == "cpu":
    cpu = psutil.cpu_times(percpu=False)
    print("system.cpu.idle", cpu.idle)
    print("system.cpu.user", cpu.user)
    print("system.cpu.guest", cpu.guest)
    print("system.cpu.iowait", cpu.iowait)
    print("system.cpu.stolen", cpu.steal)
    print("system.cpu.system", cpu.system)

elif metric_os == "mem":
    print("virtual total", psutil.virtual_memory().total)
    print("virtual used", psutil.virtual_memory().used)
    print("virtual free", psutil.virtual_memory().free)
    print("virtual shared", psutil.virtual_memory().shared)
    print("swap total", psutil.swap_memory().total)
    print("swap used", psutil.swap_memory().used)
    print("swap free", psutil.swap_memory().free)
else:
    print("Argument is wrong. Use cpu or mem")
