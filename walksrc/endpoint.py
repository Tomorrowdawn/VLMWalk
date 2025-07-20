import os
devices = "4,5" #change this according to your devices
os.environ["CUDA_VISIBLE_DEVICES"] = devices

from sglang.utils import launch_server_cmd, wait_for_server
hub = os.environ["HF_MODELS_CACHE"]
name = "Qwen2.5-VL-7B-Instruct" ##Qwen/Qwen2.5-VL-7B-Instruct if you want to download it from hub.
path = os.path.join(hub, name)

vision_process, port = launch_server_cmd(
    f"""
python3 -m sglang.launch_server --model-path {path} --tp 2
"""
)
print(f"Vision server launched on port {port}")
wait_for_server(f"http://localhost:{port}")
print(f"Vision server (pid: {vision_process.pid}) is ready")