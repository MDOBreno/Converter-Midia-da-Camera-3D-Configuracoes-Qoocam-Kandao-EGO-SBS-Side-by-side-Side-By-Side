import os
import re
from datetime import datetime, timedelta

# Arquivos na pasta atual
files = os.listdir(".")
pattern = re.compile(r"(\d{4})_(\d{8})_(\d{6})")  # Ex: 0041_20240107_193726

# Função para formatar a data correta
def get_formatted_date(name, subtract_100_years=False, add_timezone=False):
    match = pattern.search(name)
    if not match:
        return None
    date_str = match.group(2) + match.group(3)  # '20240107' + '193726'
    dt = datetime.strptime(date_str, "%Y%m%d%H%M%S")
    if subtract_100_years:
        dt = dt.replace(year=dt.year - 100)
    if add_timezone:
        dt -= timedelta(hours=-3)
    return dt.strftime("%Y:%m:%d %H:%M:%S")

# Gerar comandos do exiftool
commands = []

for f in files:
    ext = f.lower().split('.')[-1]
    if ext not in ["heic", "mov", "jpg", "m4v"]:
        continue

    subtract_100 = ext in ["jpg", "m4v"]
    ajust_by_timezone = ext in ["mov", "m4v"]
    timestamp = get_formatted_date(f, subtract_100_years=subtract_100, add_timezone=ajust_by_timezone)
    if not timestamp:
        continue

    if ext == "heic":
        cmd = f'''exiftool \
"-DateTimeOriginal={timestamp}" \
"-CreateDate={timestamp}" \
"-ModifyDate={timestamp}" \
"-XMP:DateCreated={timestamp}" \
"-XMP:CreateDate={timestamp}" \
"-XMP:ModifyDate={timestamp}" \
-overwrite_original "{f}"'''
    elif ext in ["mov", "m4v"]:
        cmd = f'''exiftool \
"-QuickTime:CreateDate={timestamp}" \
"-QuickTime:ModifyDate={timestamp}" \
"-TrackCreateDate={timestamp}" \
"-TrackModifyDate={timestamp}" \
"-MediaCreateDate={timestamp}" \
"-MediaModifyDate={timestamp}" \
-overwrite_original "{f}"'''
    elif ext == "jpg":
        cmd = f'''exiftool \
"-DateTimeOriginal={timestamp}" \
"-CreateDate={timestamp}" \
"-ModifyDate={timestamp}" \
-overwrite_original "{f}"'''
    else:
        continue

    commands.append(cmd)

# Escreve um shell script executável para Mac/Linux
with open("corrigir_datas.sh", "w") as f:
    f.write("#!/bin/bash\n")
    for cmd in commands:
        f.write(cmd + "\n")
    f.write('rm -f "./corrigir_datas.sh" "./corrigir_datas.bat"\n')

# Também salva versão para Windows (bat)
with open("corrigir_datas.bat", "w") as f:
    for cmd in commands:
        f.write(cmd.replace("\\\n", "") + "\n")
    f.write('del "corrigir_datas.bat"\n')
    f.write('del "corrigir_datas.sh"\n')

print("Script gerado com sucesso.")