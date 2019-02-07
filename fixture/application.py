from pywinauto.application import Application as WinApplication

class Application:

    def __init__(self, target):
        self.application = WinApplication(backend="win32").start(target)


    def destroy(self):
        pass