import os
from huggingface_hub import hf_hub_download

# 设置国内加速镜像（可选，但推荐）
# os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

repo_id = "BAAI/bge-m3"
local_dir = "./model"

# 如果目标目录不存在则创建
os.makedirs(local_dir, exist_ok=True)

# 需要手动下载的文件列表
files = [
    "config.json",
    "config_sentence_transformers.json",
    "tokenizer.json",
    "pytorch_model.bin"
]

for file in files:
    print(f"Downloading {file}")
    # 没有 timeout 参数，直接下载
    hf_hub_download(
        repo_id=repo_id,
        filename=file,
        local_dir=local_dir,
        local_dir_use_symlinks=False,
        resume_download=True,     # 若下载中断可继续
        force_download=False      # 已存在则跳过
    )
