import os
import sys
import time
from loguru import logger
import torch


class Config:
    def __init__(self):
        # global
        self.seed = 0
        self.cuDNN = True
        self.debug = False
        self.num_workers = 0
        # self.str_time = time.strftime("%Y-%m-%dT%H%M%S", time.localtime(time.time()))
        # path
        self.dataset_dir = "data"
        self.in_path = "data/in.txt"
        self.out_path = "data/out.txt"
        self.save_dir = "data"
        self.model_save_dir = "data"
        for path in (
            self.save_dir,
            self.model_save_dir,
        ):
            if not os.path.exists(path):
                os.makedirs(path)
        # model
        self.d_model = 256
        self.num_head = 8
        self.num_encoder_layers = 2
        self.num_decoder_layers = 2
        self.dim_feedforward = 1024
        self.dropout = 0.1
        # train
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.batch_size = 128
        self.val_ratio = 0.1
        self.epochs = 10
        self.warmup_ratio = 0.12
        self.lr_max = 1e-3
        self.lr_min = 1e-4
        self.beta1 = 0.9
        self.beta2 = 0.98
        self.epsilon = 10e-9
        self.weight_decay = 0.01
        self.early_stop = True
        self.patience = 4
        self.delta = 0
        # test
        print("Config:")
        for key, value in self.__dict__.items():
            print(f"### {key:20} = {value}")
        