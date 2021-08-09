#!/usr/bin/python
# coding=utf8

import os
import sys

mirror = "buzhiyun"
namespace = "google_containers"
prefix = "gcr.io"
specialPrefix = "k8s.gcr.io"

def execute_sys_cmd(cmd):
    result = os.system(cmd)
    if result != 0:
        print(cmd + " failed.")
        sys.exit(-1)

def usage():
    print("Usage: " + sys.argv[0] + " pull ${image}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()
        sys.exit(-1)

    # image name like k8s.gcr.io/kube-apiserver:v1.14.1 or gcr.io/google_containers/kube-apiserver:v1.14.1
    image = sys.argv[2]
    imageArray = image.split("/")
    newImage = ""
    if image.startswith(specialPrefix) :
        newImage = image.replace(specialPrefix,'registry.aliyuncs.com/google_containers')

    if image.startswith(prefix):
        newImage = image.replace(prefix,'registry.aliyuncs.com')

    #newImage = "/".join(seq)
    print(newImage)

    print("-- pull {image} from {imageNew} instead --".format(image=image,imageNew=newImage))
    cmd = "docker pull {image}".format(image=newImage)
    execute_sys_cmd(cmd)

    cmd = "docker tag {newImage} {image}".format(newImage=newImage, image=image)
    execute_sys_cmd(cmd)

    cmd = "docker rmi {newImage}".format(newImage=newImage)
    execute_sys_cmd(cmd)

    print("-- pull {image} done --".format(image=image))
    sys.exit(0)
