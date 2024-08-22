import subprocess
import os
import json  


# 将txt文件的内容变成predict.json文件里的样子
# 读取txt文件内容  
with open('predict.txt', 'r') as file:  
    data_str = file.read().strip()  # 读取文件内容并去除首尾空白字符  
  
# 解析JSON字符串  
data_dict = json.loads(data_str)  
  
# 创建新的JSON结构列表  
new_json_list = []  
for _ in range(3):  # 假设你想要创建三个相同指令的条目  
    new_json_item = {  
        "instruction": json.dumps([data_dict]),  # 将原始数据转换为JSON字符串  
        "input": "",  
        "output": "",  
        "history": []  
    }  
    new_json_list.append(new_json_item)  
  
# 将新的JSON结构写入json文件  
with open('/home/njl/data/lenglian_data/predict.json', 'w') as outfile:  
    json.dump(new_json_list, outfile, indent=4)  # 写入文件并格式化输出  
  
print("转换完成，结果已保存至output.json文件。")

# 进行预测
def run_inference_script(script_path):
    # 构建命令
    command = f"bash {script_path}"
    
    # 执行命令
    process = subprocess.Popen(command, shell=True)
    process.wait()  # 等待命令执行完成

    # 处理输出数据
    
    decoded_post_array = []  
    
    # 拼接完整的文件路径  
    file_path = 'eval_test/llama2_g_epoch2_2_lora_target_all/generated_predictions.jsonl'  
    
    # 打开文件  
    with open(file_path, 'r', encoding='utf-8') as file:  
        # 逐行读取文件  
        for line in file:  
            # 去除可能存在的换行符  
            line = line.strip()  
            # 解析每一行的JSON字符串  
            data = json.loads(line)  
            # 将解析后的数据添加到数组中  
            decoded_post_array.append(data)  

    for data in decoded_post_array:  
        predict_json_str = data['predict']  
        predict_dict = json.loads(predict_json_str)  
        print(predict_dict)
    
# 之后你可以对 decoded_post_array 进行进一步的操作

# # 调用示例
run_inference_script("infer.sh")

