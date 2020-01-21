import os


env_list = ["dc", "df", "nc", "nf"]  # 4 single models
tensorboard_dir = "stacked_single_model_tensorboard/"
# 128 000 timesteps: about 2h, total 2h * 4 = 8h
timesteps = "128000"

for env in env_list:
    print("Waiting next env", env, "> ", end="")
    a = input()
    print("Start next env > ", env)
    os.system("python train.py --algo sac --vae-path logs_dncf_stacked/vae-64.pkl -n " + timesteps + " --log-folder logs_" + env + "_stacked/ -tb " + tensorboard_dir)
