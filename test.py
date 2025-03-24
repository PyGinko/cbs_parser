import re

error_pattern = re.compile(
    r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}),\s*Error\s*CBS\s*(.+?)\s*\[HRESULT = (0x[0-9A-Fa-f]+)'
)

log_line = "2019-09-02 15:29:43, Error            CBS  Failed to load offline store from boot directory: '\\?\\T:\\' and windows directory: '\\?\\GLOBALROOT\\Device\\HarddiskVolumeShadowCopy30\\Windows\\' [HRESULT = 0x80070013 - ERROR_WRITE_PROTECT]"

match = error_pattern.search(log_line)

if match:
    timestamp = match.group(1)
    message = match.group(2).strip()
    hresult = match.group(3)

    print(f"Timestamp: {timestamp}")
    print(f"Message: {message}")
    print(f"HRESULT: {hresult}")
else:
    print("No match found.")
