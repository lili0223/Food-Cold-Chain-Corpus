import json
import os
from random import randint, shuffle

import chardet
from dateutil.parser import parse

try:
    from json.decoder import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError

data_prefix = "examplesdata/"
datapair_slice_size = 1
num_samples_per_example = 30
test_data_list = "testdata/tdatalist.json"
test_dataset_directory = "testdata"

def shuffle_elements(rand_order, source_list):
    result_list = []
    for r_order in rand_order:
        result_list.append(source_list[r_order])

    return result_list
def shuffle_elements(rand_order, source_list):
    result_list = []
    for r_order in rand_order:
        result_list.append(source_list[r_order])

    return result_list


# inspect variable type float
def isfloat(x):
    try:
        a = float(x)
    except ValueError:
        return False
    else:
        return True


# inspect variable type int
def isint(x):
    try:
        a = float(x)
        b = int(a)
    except ValueError:
        return False
    else:
        return a == b


def is_date(string):
    if isint(string) or isfloat(string):
        return False
    try:
        # print(string)
        parse(string)
        return True
    except ValueError:
        return False

def non_null_label(full_array, label_key):
    result_val = 0
    for row in full_array:
        if (row[label_key] is not None):
            result_val = row[label_key]
            return result_val
        else:
            result_val = 0
    return result_val

def generate_field_types(t_data):
    # print (t_data[0])
    data_labels = {"str": 0, "num": 0, "dt": 0}
    field_name_types = {}
    field_name_types_array = []
    for field_name in t_data[0]:
        current_label = non_null_label(t_data,
                                       field_name)  # t_data[0][field_name]
        # print("=====", current_label, field_name)
        if (is_date(current_label) and not (isint(current_label)) and not (isfloat(current_label))):
            replace_num_var = "dt" + str(data_labels["dt"])
            data_labels["dt"] = data_labels["dt"] + 1
            field_name_types[field_name] = replace_num_var
            field_name_types_array.append({field_name: replace_num_var})
        elif (isint(current_label) or isfloat(current_label)):
            replace_num_var = "num" + str(data_labels["num"])
            data_labels["num"] = data_labels["num"] + 1
            field_name_types[field_name] = replace_num_var
            field_name_types_array.append({field_name: replace_num_var})
        else:
            replace_str_var = "str" + str(data_labels["str"])
            data_labels["str"] = data_labels["str"] + 1
            field_name_types[field_name] = replace_str_var
            field_name_types_array.append({field_name: replace_str_var})
    # print(field_name_types_array)
    return list(reversed(field_name_types_array))

def replace_fieldnames(source_data, field_name_types, replace_direction):
    # for field_name in field_name_types:
    #     if (replace_direction):
    #         source_data = str(source_data).replace(
    #             str(field_name), field_name_types[field_name])
    #     else:
    #         source_data = str(source_data).replace(
    #             str(field_name_types[field_name]), field_name)
    # return source_data
    for field_name in field_name_types:
        # print(field_name)
        # print(source_data)
        field = list(field_name.keys())[0]
        value = field_name[field]
        # print(field, value)

        if (replace_direction):
            source_data = str(source_data).replace(str(field), value)
        else:
            source_data = str(source_data).replace(str(value), field)
    return source_data



def generate_data_pairs(examples_directory, train_data_output_directory):
    all_sources_hold = []
    all_target_hold = []
    target_vega_spec = []
    max_source_seq_length = 0
    max_target_seq_length = 0

    print("Generating source and target pairs ======")
    for subdir, dirs, files in os.walk(examples_directory):
        for file in files:
            filepath = subdir + os.sep + file
            # print(filepath)
            if filepath.endswith("vl.json"):
                data = json.load(open(filepath,encoding='utf-8'))

                if ("url" in data["data"]):

                    data_file_url = data_prefix + data["data"]["url"].rsplit(
                        '/', 1)[-1]
                    # print(data_file_url)
                    # del data["_info"]
                    if ("_any" in data["encoding"]):
                        del data["encoding"]["_any"]
                    del data["data"]
                    # del data["config"]

                    if ("x" in data["encoding"]
                            and "scale" in data["encoding"]["x"]):
                        # print(data["encoding"]["x"]["scale"])
                        del data["encoding"]["x"]["scale"]

                    if ("y" in data["encoding"]
                            and "scale" in data["encoding"]["y"]):
                        # print("y", data["encoding"]["y"]["scale"])
                        del data["encoding"]["y"]["scale"]

                    # print(data)

                    # target_vega_spec = str(json.dumps(data))
                    target_vega_spec = data
                    # print(target_vega_spec)
                    # target_vega_spec = target_vega_spec.replace(
                    #     ', "_any": false', '')

                    # keep track of max targe sequence length
                    if len(target_vega_spec) > max_target_seq_length:
                        max_target_seq_length = len(target_vega_spec)

                    data_content = json.load(open(data_file_url,encoding='utf-8'))
                    # print("Content lenght", len(data_content), data_file_url)
                    data_holder = []
                    for i in range(0, datapair_slice_size):
                        selected_index = randint(0, len(data_content) - 1)
                        data_holder.append(data_content[selected_index])
                    source_data_spec = str(json.dumps(data_holder))

                    # Generate field name types
                    t_data = data_content
                    # # print (t_data[0])
                    # data_labels = {"str":0,"num":0}
                    # field_name_types = {}
                    field_name_types = generate_field_types(t_data)

                    # Sample each example file a few times
                    for i in range(0, num_samples_per_example):
                        data_holder = []
                        for i in range(0, datapair_slice_size):
                            selected_index = randint(0, len(data_content) - 1)
                            data_holder.append(data_content[selected_index])

                        # source_data_spec = str(json.dumps(data_holder))
                        source_data_spec = data_holder

                        # Replace filednames with normalized string and norm values
                        target_vega_spec = replace_fieldnames(
                            target_vega_spec, field_name_types, True)
                        source_data_spec = replace_fieldnames(
                            source_data_spec, field_name_types, True)
                        # for field_name in field_name_types:
                        #     target_vega_spec = target_vega_spec.replace(
                        #         str(field_name), field_name_types[field_name])
                        #     source_data_spec = source_data_spec.replace(
                        #         str(field_name), field_name_types[field_name])

                        # print(source_data_spec, "=****=", target_vega_spec,
                        #       "==========\n")

                        # Keep track of maximum source sequence length
                        if len(source_data_spec) > max_source_seq_length:
                            max_source_seq_length = len(source_data_spec)

                        all_sources_hold.append(source_data_spec)
                        all_target_hold.append(target_vega_spec)
                    # break
    # print(all_sources_hold)
    with open(
            train_data_output_directory + "/all_train1.sources",
            mode='wt',
            encoding='utf-8') as outfile:
        outfile.write('\n'.join(str(line) for line in all_sources_hold))
    with open(
            train_data_output_directory + "/all_train1.targets",
            mode='wt',
            encoding='utf-8') as outfile:
        outfile.write('\n'.join(str(line) for line in all_target_hold))

    print("size of all files", len(all_sources_hold), len(all_target_hold))
    print("Max Source Seq Lenght", max_source_seq_length)
    print("Max Target Seq Lenght", max_target_seq_length)

# 从testdata文件夹中随机抽取一个json数据返回
def load_test_dataset():
    if not (os.path.exists(test_data_list)):
        print("Test data list does not exists. Creating it now at",
              test_data_list)
        file_list = []
        for subdir, dirs, files in os.walk(test_dataset_directory):
            for file in files:
                filepath = subdir + os.sep + file
                if filepath.endswith("json"):
                    file_list.append(filepath)
                    print(filepath)
        with open(test_data_list, 'w') as outfile:
            print("writing test data file list to file")
            json.dump(file_list, outfile)
    
    all_json_files = json.load(open(test_data_list))
    # print("Selecting a dataset at random from ", len(all_json_files))
    data = json.load(open(all_json_files[randint(0, len(all_json_files) - 1)]))
    return (data)




def forward_norm(source_data, destination_file, f_names):

    source_data_first_sample = source_data[0]
    source_data_first_sample = replace_fieldnames(source_data_first_sample,
                                                  f_names, True)
    source_data_first_sample = source_data_first_sample.replace("'", '"')
    # print("************",  source_data_first_sample )

    try:
        source_data_first_sample = json.loads(source_data_first_sample)
    except JSONDecodeError as e:
        return False

    # Write normalized JSON to file for seq2seq model
    # print("Writing data to file:", source_data_first_sample)
    write_data_to_file(destination_file, source_data_first_sample)
    # with open(destination_file, 'w') as source_data_file:
    #     json.dump(source_data_first_sample, source_data_file)
    #     # source_data_file.write((json.dumps(source_data)))
    return True

def backward_norm(decoded_string, f_names):
    return replace_fieldnames(decoded_string, f_names, False)

def write_data_to_file(destination_file, source_data_first_sample):
    # Write normalized JSON to file for seq2seq model
    # print("Writing data to file:", source_data_first_sample)
    with open(destination_file, 'w') as source_data_file:
        json.dump(source_data_first_sample, source_data_file)
        # source_data_file.write((json.dumps(source_data)))