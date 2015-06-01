if __name__ == "__main__":
    from firefly.master.master import Master
    master = Master()
    master.config('config.json', "appmain.py")
    master.start()
