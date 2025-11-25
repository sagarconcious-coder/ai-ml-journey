with open("log.txt","r") as f:
    total_lines = 0
    total_errors =0
    total_warnings = 0
    total_info = 0

    for line in f:
        total_lines += 1
        line = line.strip()
        if line.startswith("ERROR"):
            total_errors+=1
        elif line.startswith("WARNING"):
            total_warnings+=1
        elif line.startswith("INFO"):
            total_info+=1


with open("summary.txt","w")as f:
    txt = f"""Total lines: {total_lines}
Errors: {total_errors}
Warnings: {total_warnings}
Info: {total_info}
    """
    f.write(txt)





