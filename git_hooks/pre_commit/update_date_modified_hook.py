#!/usr/bin/env python3
import subprocess, datetime


def update_date_modified_hook():
    status = subprocess.check_output(["git","status"])
    for status_line in status.split(b"\n"):
        status_line = status_line.strip()
        if not status_line.startswith(b"modified:"): continue
        modified_file = status_line.replace(b"modified:",b"").strip()
        print(modified_file)
        if not modified_file.endswith(b".md"): continue
        header_checked = False
        with open(modified_file,"r+b") as overwriter:
            read_line = None
            while read_line != b"":
                line_pos = overwriter.tell()
                read_line = overwriter.readline()
                if read_line.strip() == b"": continue # skip empty lines
                if not header_checked:
                    if read_line.strip() != b"---": break # not a file with a header
                    header_checked = True
                    continue
                else:
                    if read_line.strip() == b"---": break # end of header
                    if read_line.startswith(b"update: Last Updated "):
                        overwriter.seek(line_pos)
                        update_time = datetime.datetime.now(datetime.timezone.utc)
                        update_time_str = datetime.datetime.strftime(update_time, "%a, %e %b %Y %H:%M:%S %z")
                        overwriter.write(b"update: Last Updated ")
                        overwriter.write(update_time_str.encode())
                        break # updated date/time
                        
print("This is a pre-commit hook for auto-update of timestamp on articles")
try:
    update_date_modified_hook()
except Exception as e:
    import sys
    sys.exit("Failed because {}".format(e))