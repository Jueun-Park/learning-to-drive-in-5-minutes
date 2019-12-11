import os


# env_list = ["dc", "df", "nc", "nf"]  # 4 single model
# env_list = ["day", "night", "daynight2"]  # 2 single model + full model
env_list = ["df01", "nf01"]
n_samples = "12500"
for env in env_list:
    os.system("python -m vae.train --n-samples " + n_samples + " --n-epochs 50 --verbose 0 --z-size 32 -f record_" + env + "/ --save-path logs_" + env + "/")
