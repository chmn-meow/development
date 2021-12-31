import os
import servicemanager
import shutil
import subprocess
import sys
import win32event
import win32service
import win32serviceutil

SRCDIR = "D:\\python\\development"
TGTDIR = "C:\\Windows\\TEMP"


class PMServer(win32serviceutil.ServiceFramework):
    _svc_name_ = "PermissionsMonitorSerer"
    _svc_display_name_ = "Permissions Monitor Server"
    _svc_description_ = (
        "Creates and executes VBScripts at regular intervals." + " Nothing to see here!"
    )

    def __init__(self, args):
        self.vbs = os.path.join(TGTDIR, "pms_task.vbs")
        self.timeout = 1000 * 60

        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def main(self):
        while True:
            ret_code = win32event.WaitForSingleObject(self.hWaitStop, self.timeout)
            if ret_code == win32event.WAIT_OBJECT_0:
                servicemanager.LogInfoMsg("Service is stopping")
                break
            src = os.path.join(SRCDIR, "pms_task.vbs")
            shutil.copy(src, self.vbs)
            subprocess.call(f"cscript.exe {self.vbs}", shell=False)
            os.unlink(self.vbs)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        self.ReportServiceStatus(win32service.SERVICE_RUNNING)
        self.main()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(PMServer)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(PMServer)
