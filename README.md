# Description
Python script which prints basic information about your Linux  to console.

The script accept a single parameter to specify which metrics set to print:

  cpu - prints CPU metrics

  mem - prints RAM metrics
  
  # Requirements
  
  puthon - version > 3.5

  pip3

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

```
 $ python3 metrics.py mem
 virtual total 12244529152
 virtual used 5699252224
 virtual free 965382144
 virtual shared 581640192
 swap total 2147479552
 swap used 0
 swap free 2147479552
```
