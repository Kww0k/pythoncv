import psutil


def is_process_running(process_name):
    for proc in psutil.process_iter(['name']):
        try:
            if process_name.lower() in proc.info['name'].lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


# 使用示例
if is_process_running('wemeetapp.exe'):
    print('进程正在运行')
else:
    print('进程未运行')