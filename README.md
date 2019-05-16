# Description
Python script which prints basic information about your Linux  to console.

The script accept a single parameter to specify which metrics set to print:

  cpu - prints CPU metrics

  mem - prints RAM metrics
  
  # Requirements
  
  puthon - version > 3.5

  pip

  psutil
  
  # Installation
    pip3 install psutil
    git clone https://github.com/aliubko/os_metrics
    

  # Examples
  
  ```
  $ python metrics.py cpu
  system.cpu.idle 40240.5
  system.cpu.user 1363.84
  system.cpu.guest 0.0
  system.cpu.iowait 59.61
  system.cpu.stolen 0.0
  system.cpu.system 351.53

```
