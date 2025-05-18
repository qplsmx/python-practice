# 멀티프로세스를 이용한 누적합 구하기
import multiprocessing
import time

# 누적합 계산을 위한 함수
def compute_sum(start, end, result, index):
    print(f"Process {index} started: calculating sum from {start} to {end}")
    total = sum(range(start, end + 1))
    time.sleep(1)  # 작업 시간 시뮬레이션
    result[index] = total
    print(f"Process {index} finished: partial sum = {total}")

if __name__ == '__main__':
    # 누적합 범위 설정
    N = 1000000
    num_processes = 4
    chunk_size = N // num_processes

    # 프로세스 간 결과 공유를 위한 Manager 사용
    manager = multiprocessing.Manager()
    result = manager.dict()

    processes = []

    for i in range(num_processes):
        start = i * chunk_size + 1
        end = (i + 1) * chunk_size if i < num_processes - 1 else N
        p = multiprocessing.Process(target=compute_sum, args=(start, end, result, i))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    total_sum = sum(result.values())
    print(f"Final total sum: {total_sum}")
