from time import time


def ft_tqdm(lst):
    total = len(lst)
    progress = 0
    start = time()
    for elem in lst:
        yield elem
        progress += 1
        done = int(50 * progress / total)
        curr_time = int(time()-start)
        print(f"\r[{int(progress/total*100)}%][{'=' * done}{' ' *(50 - done)}]\
            "f"{progress}/{total} {curr_time}s ETA: \
            {int(curr_time/progress*total- curr_time)}s", end="")
