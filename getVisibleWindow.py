import ctypes
from ctypes import wintypes

def get_visible_windows():
    visible_windows = []

    EnumWindows = ctypes.windll.user32.EnumWindows
    EnumWindowsProc = ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)
    GetWindowText = ctypes.windll.user32.GetWindowTextW
    IsWindowVisible = ctypes.windll.user32.IsWindowVisible

    # Create a reusable buffer
    buffer_size = 512
    buffer = ctypes.create_unicode_buffer(buffer_size)

    def foreach_window(hwnd, lParam):
        try:
            # Check if the window is currently visible
            if IsWindowVisible(hwnd):
                # Retrieve the window text into the buffer
                if GetWindowText(hwnd, buffer, buffer_size):
                    # Append the window title to the list
                    visible_windows.append(buffer.value)
        except Exception as e:
            # Handle exceptions if they occur during the enumeration
            print(f"Error processing window: {e}")

        return True

    EnumWindows(EnumWindowsProc(foreach_window), 0)

    return visible_windows