import os
import subprocess
from datetime import datetime

work_dir = '/home/zli/Videos/gun_videos/'

os.chdir(work_dir)

video_files = []
for root, dirs, filenames in os.walk(work_dir):
    for f in filenames:
        video_files.append(f)

date_str = datetime.today().strftime('%Y%m%d')
count = 0
for video_file in video_files:
    filename = video_file.lower().replace(' ', '_')
    print('****'+filename+'\n')

    sub_dir = str(count)
    count += 1

    if not os.path.exists(sub_dir):
        os.mkdir(sub_dir)

    name_without_ext, ext = os.path.splitext(filename)
    command = ['ffmpeg', '-i', video_file, '-r', '1', work_dir +
                     sub_dir + '/' + name_without_ext + date_str + '%00d.jpg']
    print(command)
    subprocess.run(command)
