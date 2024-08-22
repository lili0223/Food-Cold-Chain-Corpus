from random import shuffle
import data_utils

data_split_params = [{
    "tag": "train",
    "percentage": [0, 0.8]
}, {
    "tag": "dev",
    "percentage": [0.8, 0.9]
}, {
    "tag": "test",
    "percentage": [0.9, 1]
}]
sources_file_path = 'sourcedata/all_train.sources'
targets_file_path = 'sourcedata/all_train.targets'
train_data_output_directory = "sourcedata"
# 读取文件内容
with open(sources_file_path, 'r', encoding='utf-8') as file:
    lines1 = file.readlines()
# 每一行的字符串，将其转换为列表中的元素
data_list_sources = []
for line in lines1:
    # 去除字符串两侧的空白字符，并将字符串转换为列表元素
    data_list_sources.append(line.strip())


# 读取文件内容
with open(targets_file_path, 'r', encoding='utf-8') as file:
    lines2 = file.readlines()
# 处理每一行的字符串，将其转换为列表中的元素
data_list_targets = []
for line in lines2:
    # 去除字符串两侧的空白字符，并将字符串转换为列表元素
    data_list_targets.append(line.strip())

# 输出处理后的列表
# print(data_list_sources)
# print(data_list_targets)

# Uniformly shuffle source and target sequence pair lists
rand_list = list(range(0, len(data_list_sources) - 1))

shuffle(rand_list)
# print(rand_list)
# print(len(data_list_sources))
all_sources_hold = data_utils.shuffle_elements(rand_list, data_list_sources)
all_target_hold = data_utils.shuffle_elements(rand_list, data_list_targets)

for param in data_split_params:
    with open(
            train_data_output_directory + "/" + param["tag"] + ".sources",
            mode='wt',
            encoding='utf-8') as outfile:
        outfile.write('\n'.join(
            str(line) for line in all_sources_hold[int(
                param["percentage"][0] * len(all_sources_hold)):int(
                param["percentage"][1] * len(all_sources_hold))]))
    print("  > Saved ",
          train_data_output_directory + "/" + param["tag"] + ".sources")
    with open(
            train_data_output_directory + "/" + param["tag"] + ".targets",
            mode='wt',
            encoding='utf-8') as outfile:
        outfile.write('\n'.join(
            str(line) for line in all_target_hold[int(
                param["percentage"][0] * len(all_target_hold)):int(
                param["percentage"][1] * len(all_target_hold))]))
    print("  > Saved ",
          train_data_output_directory + "/" + param["tag"] + ".targets")