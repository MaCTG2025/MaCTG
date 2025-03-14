import os
from pathlib import Path

import docker


def run_test(mount_dir:Path, test_filename:str) -> str:
        image_name = "image:1.0"
        client = docker.from_env()
        uid = os.getuid()
        gid = os.getgid()
        container = client.containers.run(image=image_name,
                                        command=["python", "-uB", f"/work/{test_filename}"],
                                        detach=True,
                                        volumes={os.path.abspath(mount_dir): {"bind": "/work", "mode": "rw"}},
                                        working_dir="/work",
                                        user=f"{uid}:{gid}")
        # show container print
        for line in container.logs(stream=True):
            line.strip()
        
        info = container.logs().decode("utf-8")
        container.stop()
        container.remove()
        print(info)
        return info