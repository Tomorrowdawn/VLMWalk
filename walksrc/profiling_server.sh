# set trace path
if [ ! -d "walksrc" ]; then
    echo "Please run this script from the parent directory of 'walksrc'."
    exit 1
fi

export SGLANG_TORCH_PROFILER_DIR=logs/sglang_pytorch_profile
export CUDA_VISIBLE_DEVICES="0, 1"

model_path=$HF_MODELS_CACHE/Qwen2.5-VL-7B-Instruct
# start server
uv run -m sglang.launch_server --model-path $model_path --tp 2
