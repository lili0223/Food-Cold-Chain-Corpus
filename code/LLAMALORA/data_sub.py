# 打开源文件和目标文件
with open('sourcedata/all_train2.sources', 'r') as source_file, open('sourcedata/processed_train.sources', 'w') as target_file:
    line_count = 0
    for line in source_file:
        if line_count % 50 < 30:
            target_file.write(line)
        line_count += 1

with open('sourcedata/all_train2.targets', 'r') as source_file, open('sourcedata/processed_train.targets', 'w') as target_file:
    line_count = 0
    for line in source_file:
        if line_count % 50 < 30:
            target_file.write(line)
        line_count += 1
