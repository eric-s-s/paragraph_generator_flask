from multiprocessing import cpu_count

workers = 2 * cpu_count() + 1
bind = "0.0.0.0:8080"

