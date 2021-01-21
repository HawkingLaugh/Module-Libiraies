import os, psutil

def show_ram_usage():
    process = psutil.Process(os.getpid())
    usage = "{} MB".format(process.memory_info().rss / 1024 ** 2)
    return usage

if __name__ == "__main__":
    print(show_ram_usage())