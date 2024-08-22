
from nltk.translate.bleu_score import sentence_bleu
from rouge import Rouge
import json

# 加载参考答案文件
reference_data = []
with open('/home/njl/data/unknow_data/test_replace.csv', 'r', encoding='utf-8') as f:
    for line in f:
        # 解析每行数据中的 JSON 对象
        entry = json.loads(line.strip())
        reference_data.append(entry)

# 加载预测结果文件
prediction_data = []
with open('/home/njl/t5_train/output/t5_2.txt', 'r', encoding='utf-8') as f:
    for line in f:
        # 解析每行数据中的 JSON 对象
        entry = json.loads(line.strip())
        prediction_data.append(entry)

# 提取参考答案中的 "encoding" 和 "mark" 字段作为参考答案
reference_encoding = [entry['encoding'] for entry in reference_data]
reference_mark = [entry['mark'] for entry in reference_data]

# 提取预测结果中的 "encoding" 和 "mark" 字段作为预测结果
prediction_encoding = [entry['encoding'] for entry in prediction_data]
prediction_mark = [entry['mark'] for entry in prediction_data]

# 计算 BLEU-4 分数
# 这里假设参考答案和预测结果的格式是一致的，直接计算 BLEU-4 分数
bleu_scores = [sentence_bleu([ref.split()], pred.split(), weights=(0.25, 0.25, 0.25, 0.25)) for ref, pred in zip(reference_mark, prediction_mark)]

print("BLEU-4 分数:", bleu_scores)

# 计算 ROUGE 分数
rouge = Rouge()
scores = rouge.get_scores(prediction_mark, reference_mark, avg=True)

print("ROUGE-1 分数:", scores['rouge-1'])
print("ROUGE-2 分数:", scores['rouge-2'])
print("ROUGE-L 分数:", scores['rouge-l'])