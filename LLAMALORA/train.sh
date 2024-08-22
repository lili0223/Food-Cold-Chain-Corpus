export WANDB_DISABLED=true


# torchrun --nproc_per_node 2 src/train_bash.py \
#     --stage sft \
#     --model_name_or_path /root/hdd/llm/Llama-2-7b-chat-hf \
#     --do_train \
#     --dataset train_g \
#     --template llama2 \
#     --finetuning_type lora \
#     --lora_target "q_proj, k_proj, v_proj" \
#     --output_dir /root/LLaMA-Efficient-Tuning/model_saved_total/llama2_g_epoch3_lora_target_all \
#     --overwrite_cache \
#     --per_device_train_batch_size 28 \
#     --gradient_accumulation_steps 2 \
#     --lr_scheduler_type cosine \
#     --logging_steps 10 \
#     --save_steps 1000 \
#     --learning_rate 1e-3 \
#     --num_train_epochs 2.0 \
#     --plot_loss \
#     --bf16 \
#     "$@"

# CUDA_VISIBLE_DEVICES=1 python src/train_bash.py \
#     --stage sft \
#     --model_name_or_path /root/hdd/llm/Llama-2-7b-chat-hf \
#     --do_predict \
#     --dataset test_g \
#     --template llama2 \
#     --finetuning_type lora \
#     --lora_target "q_proj, k_proj, v_proj" \
#     --checkpoint_dir /root/LLaMA-Efficient-Tuning/model_saved_total/llama2_g_epoch3_lora_target_all \
#     --output_dir /root/LLaMA-Efficient-Tuning/eval_test/llama2_g_epoch3_lora_target_all \
#     --per_device_eval_batch_size 24 \
#     --max_samples 1000000 \
#     --predict_with_generate \

# CUDA_VISIBLE_DEVICES=3,4,6 torchrun --nnodes=1 --standalone --nproc_per_node=gpu src/train_bash.py \
#     --stage sft \
#     --model_name_or_path /home/njl/llama2_new/Llama-2-7b-chat-hf \
#     --do_train \
#     --dataset train_lenglian \
#     --template llama2 \
#     --finetuning_type lora \
#     --lora_target "q_proj, k_proj, v_proj" \
#     --checkpoint_dir /home/njl/LLAMALORA/model_lenglian_saved_total/llama2_g_epoch4_2_lora_target_all \
#     --output_dir /home/njl/LLAMALORA/model_lenglian_saved_total/llama2_g_epoch6_2_lora_target_all \
#     --overwrite_cache \
#     --per_device_train_batch_size 5 \
#     --gradient_accumulation_steps 2 \
#     --lr_scheduler_type cosine \
#     --logging_steps 10 \
#     --save_steps 10000 \
#     --learning_rate 7e-4 \
#     --num_train_epochs 2.0 \
#     --plot_loss \
#     --bf16 \
#     "$@"

CUDA_VISIBLE_DEVICES=6 python src/train_bash.py \
   --stage sft \
   --model_name_or_path /home/njl/llama2_new/Llama-2-7b-chat-hf \
   --do_predict \
   --dataset test_lenglian \
   --template llama2 \
   --finetuning_type lora \
   --lora_target "q_proj, k_proj, v_proj" \
   --checkpoint_dir /home/njl/LLAMALORA/model_lenglian_saved_total/llama2_g_epoch6_2_lora_target_all \
   --output_dir /home/njl/LLAMALORA/lenglian_test/llama2_g_epoch6_2_lora_target_all \
   --per_device_eval_batch_size 6 \
   --max_samples 1000000 \
   --predict_with_generate \
#
# CUDA_VISIBLE_DEVICES=5 python src/train_bash.py \
#     --stage sft \
#     --model_name_or_path /home/njl/llama2_new/Llama-2-7b-chat-hf \
#     --do_predict \
#     --dataset test2_g \
#     --template llama2 \
#     --finetuning_type lora \
#     --lora_target "q_proj, k_proj, v_proj" \
#     --checkpoint_dir /home/njl/LLAMALORA/model_saved_total/llama2_g_epoch2_2_lora_target_all \
#     --output_dir /home/njl/LLAMALORA/eval_test/llama2_g_epoch2_2_lora_target_all_test2 \
#     --per_device_eval_batch_size 10 \
#     --max_samples 1000000 \
#     --predict_with_generate \




# 单卡的
# CUDA_VISIBLE_DEVICES=5 python src/train_bash.py \
#     --stage sft \
#     --model_name_or_path /home/njl/llama2_new/Llama-2-7b-chat-hf \
#     --do_train \
#     --dataset train2_g \
#     --template llama2 \
#     --finetuning_type lora \
#     --lora_target "q_proj, k_proj, v_proj" \
#     --output_dir /home/njl/LLAMALORA/model_saved_total/llama2_g_singal_epoch2_2_lora_target_all \
#     --overwrite_cache \
#     --per_device_train_batch_size 5 \
#     --gradient_accumulation_steps 2 \
#     --lr_scheduler_type cosine \
#     --logging_steps 10 \
#     --save_steps 1000 \
#     --learning_rate 1e-3 \
#     --num_train_epochs 2.0 \
#     --plot_loss \
#     --bf16 \
#     "$@"

# CUDA_VISIBLE_DEVICES=5 python src/train_bash.py \
#     --stage sft \
#     --model_name_or_path /home/njl/llama2_new/Llama-2-7b-chat-hf \
#     --do_predict \
#     --dataset test2_g \
#     --template llama2 \
#     --finetuning_type lora \
#     --lora_target "q_proj, k_proj, v_proj" \
#     --checkpoint_dir /home/njl/LLAMALORA/model_saved_total/llama2_g_singal_epoch2_2_lora_target_all \
#     --output_dir /home/njl/LLAMALORA/eval_test/llama2_g_singal_epoch2_2_lora_target_all_test2 \
#     --per_device_eval_batch_size 8 \
#     --max_samples 1000000 \
#     --predict_with_generate \
