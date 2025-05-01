import sys
import os
import runpy

# 1. 确保自定义模块能被找到 (通过 PYTHONPATH 或直接修改 sys.path)
#    你的命令行已经设置了 PYTHONPATH，这里可以不用额外添加
#    project_base = '/home/nvidia/ai-lab'
#    if project_base not in sys.path:
#        sys.path.insert(0, project_base)

# 2. 显式导入自定义数据集模块，触发注册
try:
    import wukong_v15.custom_dataset
    print("Successfully imported custom dataset module.")
except ImportError as e:
    print(f"Error importing custom dataset module: {e}")
    print("Please ensure 'wukong_v15' is in PYTHONPATH and custom_dataset.py exists.")
    sys.exit(1)

# 3. 准备运行 infer.py 的参数
#    将原始命令行的参数放在这里
infer_script_path = '/home/nvidia/ai-lab/PaddleX/paddlex/repo_manager/repos/PaddleDetection/tools/infer.py'
config_file = 'config/tinypose_keypoint.yaml'
weights_path = 'output/pp_tinypose_itx/model_final.pdparams'
infer_image = 'data/itx/images/itx_board_007.jpg'
output_dir = 'output/inference_results'

# 构建传递给 infer.py 的 sys.argv
# 注意：第一个元素通常是脚本名称本身
sys.argv = [
    infer_script_path,
    '-c', config_file,
    '-o', f'weights={weights_path}',
    '--infer_img', infer_image,
    '--output_dir', output_dir
    # 如果有其他参数，也添加到这里
]

print(f"Running {infer_script_path} with args: {sys.argv}")

# 4. 使用 runpy 执行原始的 infer.py 脚本
#    这会像直接运行 `python infer.py ...` 一样执行它，但我们的导入已经生效
try:
    runpy.run_path(infer_script_path, run_name="__main__")
except Exception as e:
    print(f"Error running infer.py: {e}")
    import traceback
    traceback.print_exc()
