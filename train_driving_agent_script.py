import os


# env_list = ["dc", "df", "nc", "nf"]  # 4 single model
# env_list = ["day", "night", "daynight2"]  # 2 single model + full model
env_list = ["df01", "nf01"]
tensorboard_dir = "1205_single_model_tensorboard/"
# # 128 000 timesteps: about 2h, total 2h * 3 = 6h
timesteps = "128000"
# timesteps = "512000"
for env in env_list:
    print("Waiting next env", env, "> ", end="")
    a = input()
    print("Start next env > ", env)
    os.system("python train.py --algo sac --vae-path logs_" + env + "/vae-32.pkl -n " + timesteps + " --log-folder logs_" + env + "/ -tb " + tensorboard_dir)
