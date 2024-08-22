from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import data_utils
import json
import subprocess

try:
    from json.decoder import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError

app = Flask(__name__, )
# 创建了一个CORS对象，并将其应用到app上。CORS是跨域资源共享的缩写，它允许Web应用程序从不同的域名或端口请求和访问资源
cors = CORS(app)
# 设置了CORS的请求头部分为Content-Type。这是一种常见的请求头设置，用于指定请求或响应中的内容类型。
app.config['CORS_HEADERS'] = 'Content-Type'

destination_file = "predict.txt"



# 进行预测
def run_inference_script(script_path):
    # 构建命令
    command = f"bash {script_path}"
    
    # 执行命令
    process = subprocess.Popen(command, shell=True)
    process.wait()  # 等待命令执行完成



@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/testdata")
def testdata(): 
    return jsonify(data_utils.load_test_dataset())

@app.route("/inference", methods=['POST'])
def inference():
    input_data = request.json

    # Catch bad JSONDecodeError
    try:
        source_data = json.loads(str(input_data["sourcedata"]))
    except JSONDecodeError as e:
        response_payload = {
            "status": False,
            "reason": "Bad JSON: Unable to decode source JSON.  "
        }
        return jsonify(response_payload)

    if len(source_data) == 0:
        response_payload = {"status": False, "reason": "Empty JSON!!!!.  "}
        return jsonify(response_payload)

    # Perform preprocessing - forward normalization on first data sample
    f_names = data_utils.generate_field_types(source_data)
    fnorm_result = data_utils.forward_norm(source_data, destination_file,
                                           f_names)

    if (not fnorm_result):
        response_payload = {"status": False, "reason": "JSON decode error  "}
        return jsonify(response_payload)

   # 将txt文件的内容变成predict.json文件里的样子 
    with open('predict.txt', 'r') as file:  
        data_str = file.read().strip()  # 读取文件内容并去除首尾空白字符  
  
    # 解析JSON字符串  
    data_dict = json.loads(data_str)  
    
    # 创建新的JSON结构列表  
    new_json_list = []  
    for _ in range(15):  # 假设你想要创建三个相同指令的条目  
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

#     # 开始预测

    run_inference_script("infer.sh")


     # 处理输出数据
    
    
    # 拼接完整的文件路径  
    file_path = 'eval_test/llama2_g_epoch2_2_lora_target_all/generated_predictions.jsonl'  
    decoded_string = []
    # 打开文件  
    with open(file_path, 'r', encoding='utf-8') as file:  
        # 逐行读取文件  
        for line in file:  
            # 去除可能存在的换行符  
            line = line.strip()  
            # 解析每一行的JSON字符串  
            data = json.loads(line)  
            # 将解析后的数据添加到数组中  
            predict_json_str = data.get('predict', '{}')
            decoded_string.append(predict_json_str)
        print(decoded_string)  
    
    print(source_data)
    

    try:
        vega_spec = json.dumps(decoded_string)
        # print("===== vega spec =====", vega_spec)
        response_payload = {
            "vegaspec": vega_spec,
            "status": True,
            "data": source_data
        }
    except JSONDecodeError as e:
        response_payload = {
            "status": False,
            "reason": "Model did not produce a valid vegalite JSON",
            "vegaspec": decoded_string
        }
    # print(response_payload)
    return jsonify(response_payload)




if __name__ == "__main__":

    print("Starting webserver: ")
    app.config['APPLICATION_ROOT'] = "static"
    app.run(host='0.0.0.0', debug=True, port=5001, threaded=True)