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
  parser = argparse.ArgumentParser()
  parser.add_argument("--algo", default="GD", type=str, required=True, help='Optimization Algorithm')
  parser.add_argument("--runtime", type=int, required=True,  help="duration of the run")
  parser.add_argument("--identifier", type=str, required=True,  help="identifier for the run")

  args = parser.parse_args()
  identifier=args.algo+'_'+str(args.runtime)+'_'+args.identifier
  transfer=TransferClass(configurations,log,transfer_emulation=False,runTime=args.runtime)
  transferEnvironment=transferEnv(transfer,runTime=args.runtime,identity=identifier)
  transferEnvironment.reset()
  start_time=time.time()
  if args.algo=="GD":
    final_ccs=gradient_opt(transferEnvironment)
  elif args.algo=="GD_FAST":
    final_ccs=gradient_opt_fast(transferEnvironment)
  elif args.algo=="BO":
    final_ccs=bayes_optimizer(transferEnvironment,configurations)
  else:
    final_ccs=gradient_opt(transferEnvironment)
  end_time=time.time()
  transferEnvironment.reset()
  total_bytes = np.sum(transfer.file_sizes)
  print(f"total_bytes:{total_bytes} start_time:{start_time}, end_time:{end_time} ")
  transfer_throughput=int((total_bytes*8)/(np.round(end_time-start_time,1)*1000*1000))
  print(f"transfer_throughput {transfer_throughput} Mbps#############")
  print(" ###########  final CCs ",final_ccs)
  transferEnvironment.close()

