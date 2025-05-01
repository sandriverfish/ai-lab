import os
import sys
import paddle
import ppdet
from ppdet.core.workspace import create, load_config
from ppdet.engine import Trainer
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config",
        type=str,
        default=None,
        help="Configuration file path")
    parser.add_argument(
        "--use_gpu",
        action='store_true',
        default=False,
        help="Whether to use GPU")
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    
    # Set device based on args
    if args.use_gpu:
        paddle.device.set_device('gpu:0')
    else:
        paddle.device.set_device('cpu')
    
    # Load configuration from YAML
    cfg = load_config(args.config)
    
    # Create trainer with loaded config
    trainer = Trainer(cfg)
    
    # Start training
    trainer.train()

if __name__ == '__main__':
    main()