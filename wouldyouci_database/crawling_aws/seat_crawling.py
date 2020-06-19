import threading
import update_seats
import datetime
import sys

print('==================== START', datetime.datetime.now(), '=====================')
print()


def execute_per_minute(second=10.0, num=1):
    print(f'시간: {datetime.datetime.now()} {num} 번째')
    num += 1
    update_seats.cinemaLoop()
    print('루프 종료')
    print('잠깐 쉬기 10초')
    threading.Timer(second, execute_per_minute, [second, num]).start()


execute_per_minute(10, 1)
