import win32com.client
import subprocess
import win32api

shell = win32com.client.Dispatch("WScript.Shell")

# * 3 ways to execute application, subprocess is "cross-platform"
# 1 os.system('notepad.exe')
# 2 win32api.WinExec('notepad.exe')
# 3 subprocess.Popen(['notepad.exe']) #? recommended

program = 'C:\\Program Files (x86)\\_MyProgram\\_FileOne\\_ExecutableFile.exe'
subprocess.Popen(program)

# * open program wait for 3 sec and enter text
win32api.Sleep(3000)  # wait time

# _my_program
shell.SendKeys(f'*ABC123{"__"*5}')  # text
shell.SendKeys("{ENTER}")

# _my_program_2
subprocess.Popen(['_Executable.exe'])
win32api.Sleep(6000)
shell.SendKeys("{ENTER}")
