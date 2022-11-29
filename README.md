# Access Log Analyzer
***
Access Log Analyzer is a python script to analyze and
produce metadata from access log files.

# Usage

---
***Command Line***  
```commandline
~$ main.py <input_path> <output_path>  [ARG...]
```
---
***Using Docker File***  
- Building container
  ```commandline
  $ docker build -t <container_name> .
  ```
- Running container
  ```commandline
  $ docker run <container_name> <input_path> <output_path> [ARG...]
  ``` 
---
***Arguments***  
--- 
| Argument | Function                      |
|-------------------------------|--------- |
|input_path|input file or directory to analyze|
|output_path| output directory to save the results|
|--mfip| Most frequent IP in the file  |
|--lfip| Lest frequent IP in the file  |
|--eps| Get average events per second |
|--bytes| Total amount of bytes exchanged|
---