# CUDA_VISIBLE_DEVICES=4 python src/train_bash.py \
#    --stage sft \
#    --model_name_or_path /home/njl/llama2_new/Llama-2-7b-chat-hf \
#    --do_predict \
#    --dataset test_100 \
#    --template llama2 \
#    --finetuning_type lora \
#    --lora_target "q_proj, k_proj, v_proj" \
#    --checkpoint_dir /home/njl/LLAMALORA/model_saved_total/llama2_g_epoch2_2_lora_target_all \
#    --output_dir /home/njl/LLAMALORA/eval_test/llama2_g_epoch2_2_lora_target_all \
#    --per_device_eval_batch_size 6 \
#    --max_samples 1000000 \
#    --predict_with_generate \

CUDA_VISIBLE_DEVICES=4 python src/train_bash.py \
   --stage sft \
   --model_name_or_path /home/njl/llama2_new/Llama-2-7b-chat-hf \
   --do_predict \
   --dataset predict_lenglian \
   --template llama2 \
   --finetuning_type lora \
   --lora_target "q_proj, k_proj, v_proj" \
   --checkpoint_dir /home/njl/LLAMALORA/model_lenglian_saved_total/llama2_g_epoch4_2_lora_target_all \
   --output_dir /home/njl/LLAMALORA/eval_test/llama2_g_epoch2_2_lora_target_all \
   --per_device_eval_batch_size 6 \
   --max_samples 1000000 \
   --predict_with_generate \