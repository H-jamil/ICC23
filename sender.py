import os
import time
import socket
import datetime
import numpy as np
import logging as log
import multiprocessing as mp
import pandas as pd
import re
from config import configurations
from transferClass import *
from transferEnv import *
from optimizer_gd import *
# from optimizer_gd_ import *

import argparse
import gym
import pybullet_envs

# from lib import model
import numpy as np
import torch
log_FORMAT = '%(created)f -- %(levelname)s: %(message)s'
log_file = "logs/" + datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S") + ".log"

if configurations["loglevel"] == "debug":
  log.basicConfig(
      format=log_FORMAT,
      datefmt='%m/%d/%Y %I:%M:%S %p',
      level=log.DEBUG,
      handlers=[
          log.FileHandler(log_file),
          log.StreamHandler()
      ]
    )
  mp.log_to_stderr(log.info)

else:
  log.basicConfig(
      format=log_FORMAT,
      datefmt='%m/%d/%Y %I:%M:%S %p',
      level=log.INFO,
      handlers=[
          log.FileHandler(log_file),
          log.StreamHandler()
      ]
  )
configurations["thread_limit"] = configurations["max_cc"]
configurations["cpu_count"] = mp.cpu_count()

if __name__=="__main__":
  transfer=TransferClass(configurations,log,transfer_emulation=False)
  transferEnvironment=transferEnv(transfer)

  transferEnvironment.reset()
  start_time=time.time()
  final_ccs=gradient_opt(transferEnvironment)
  end_time=time.time()
  total_bytes = np.sum(transfer.file_sizes)
  print(f"total_bytes:{total_bytes} start_time:{start_time}, end_time:{end_time} ")
  transfer_throughput=int((total_bytes*8)/(np.round(end_time-start_time,1)*1000*1000))
  print(f"transfer_throughput {transfer_throughput} Mbps#############")
  print(" ###########  final CCs ",final_ccs)
  transferEnvironment.close()

  # time.sleep(1)
  # transferEnvironment.reset()
  # start_time=time.time()
  # final_ccs=gradient_opt_fast(transferEnvironment)
  # end_time=time.time()
  # total_bytes = np.sum(transfer.file_sizes)
  # print(f"total_bytes:{total_bytes} start_time:{start_time}, end_time:{end_time} ")
  # transfer_throughput=int((total_bytes*8)/(np.round(end_time-start_time,1)*1000*1000))
  # print(f"transfer_throughput {transfer_throughput} Mbps#############")
  # print(" ###########  final CCs ",final_ccs)
  # transferEnvironment.close()

  # time.sleep(1)
  # transferEnvironment.reset()
  # start_time=time.time()
  # final_ccs=bayes_optimizer(transferEnvironment,configurations)
  # end_time=time.time()
  # total_bytes = np.sum(transfer.file_sizes)
  # print(f"total_bytes:{total_bytes} start_time:{start_time}, end_time:{end_time} ")
  # transfer_throughput=int((total_bytes*8)/(np.round(end_time-start_time,1)*1000*1000))
  # print(f"transfer_throughput {transfer_throughput} Mbps#############")
  # print(" ###########  final CCs ",final_ccs)
  # transferEnvironment.close()
  # transferEnvironment.reset()
  # transferEnvironment.close()

