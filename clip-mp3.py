import datetime
import os
import sys
import time

from pydub import AudioSegment

path = sys.argv[1]

start_str = sys.argv[2]
end_str = sys.argv[3]


def parseTime(time_star: str):
    x = time.strptime(time_star.split(',')[0], '%H:%M:%S')
    return datetime.timedelta(hours=x.tm_hour,
                              minutes=x.tm_min,
                              seconds=x.tm_sec).total_seconds()


# Time to miliseconds
startTime = parseTime(start_str) * 1000
endTime = parseTime(end_str) * 1000

dir_name = os.path.dirname(os.path.realpath(path))

# Opening file and extracting segment
song = AudioSegment.from_file(path)
extract = song[startTime:endTime]

# Saving
extract.export(os.path.join(dir_name, 'clip.mp3'), format="mp3")
