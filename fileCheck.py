import os
import pyudev

# Run continously
while True:
    # detect usb plugin
    context = pyudev.Context()
    for device in context.list_devices(subsystem='block', DEVTYPE='partition'):
        print(device.get('ID_FS_LABEL', 'unlabeled partition'))
        # check file system to see how old last modified files are
        for filename in os.listdir(device):           # iterate through all files in directories
            info = os.stat(filename)
            if( info.st_mtime > 2.628 * (10**9)):
                # delete files
                os.remove(filename)


'''
Extra notes:

I have not tested this....

we may need to add a break statement or something similiar to that so the code will actually run

'''