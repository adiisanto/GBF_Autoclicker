import ctypes
import psutil

def get_pid_by_window_title(window_title):
    matching_pids = []

    EnumWindows = ctypes.windll.user32.EnumWindows
    EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
    GetWindowText = ctypes.windll.user32.GetWindowTextW
    GetWindowThreadProcessId = ctypes.windll.user32.GetWindowThreadProcessId

    # Callback function to enumerate windows
    def foreach_window(hwnd, lParam):
        try:
            # Retrieve the window text into the buffer
            buffer_size = 512
            buffer = ctypes.create_unicode_buffer(buffer_size)
            GetWindowText(hwnd, buffer, buffer_size)

            # Check if the window is currently visible and the title matches
            if buffer.value and ctypes.windll.user32.IsWindowVisible(hwnd) and window_title.lower() in buffer.value.lower():
                # Get the process ID corresponding to the window
                pid = ctypes.c_ulong()
                tid = GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
                matching_pids.append(pid.value)
        except Exception as e:
            # Handle exceptions if they occur during the enumeration
            print(f"Error processing window: {e}")

        return True

    EnumWindows(EnumWindowsProc(foreach_window), 0)

    return matching_pids
