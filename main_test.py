import main
import time


test_csv = [
    # "sample/wolf/village_g12.csv",
    "sample/wolf/village_g19.csv",
    "sample/wolf/village_g21.csv"
]
sum_time = 0

for csv in test_csv:
    start = time.time()
    main.run(csv)
    process_time = time.time() - start
    sum_time += process_time
    print(process_time)


average = sum_time / len(test_csv)
print(average)