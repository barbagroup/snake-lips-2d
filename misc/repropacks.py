"""Make repro-packs."""

import os
import requests
import shutil
from pathlib import Path
from zipfile import ZipFile

ROOTDIR = Path(__file__).absolute().parents[1]
GH_HEADERS = {
    'Accept': 'application/vnd.github.v3+json',
    'Authorization': f'Bearer {os.environ.get("GH_TOKEN")}'
}
GH_OWNER = 'mesnardo'
GH_REPO = 'snake-lips-2d'
GH_BRANCH = 'dev'
REPROPACKS_NAME = f'{GH_REPO}-repropacks'


def delete_repropacks(path):
    """Delete repropacks if present."""
    if path.is_dir():
        shutil.rmtree(path)


def download_repo(owner, repo, branch, dst):
    """Download archive of GitHub repo and extract into given destination."""
    print('[INFO] Downloading archive from GitHub ...')
    url = f'https://api.github.com/repos/{owner}/{repo}/zipball/{branch}'
    res = requests.get(url, headers=GH_HEADERS)
    res.raise_for_status()

    archive = f'{owner}-{repo}-{branch}.zip'
    with open(archive, 'wb') as out:
        out.write(res.content)

    print(f'[INFO] Extracting archive into {dst} ...')
    with ZipFile(archive, 'r') as obj:
        mainfolder = obj.namelist()[0].split('/')[0]
        obj.extractall()
        shutil.move(mainfolder, dst)

    print('[INFO] Removing archive ...')
    os.remove(archive)


def copy_repropacks_files(dir_from, dir_to):
    """Copy repropacks files."""
    for config in Path(dir_from).glob('**/.repropacks'):
        print(f'[INFO] Processing {config} ...')
        with open(config, 'r') as f:
            objs = [obj.strip('\n') for obj in f.readlines()]
        casedir = config.parent
        for obj in objs:
            for src in casedir.glob(obj):
                dst = dir_to / src.relative_to(dir_from)
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(src, dst)


if __name__ == '__main__':
    delete_repropacks(ROOTDIR / REPROPACKS_NAME)
    download_repo(GH_OWNER, GH_REPO, GH_BRANCH, ROOTDIR / REPROPACKS_NAME)
    copy_repropacks_files(ROOTDIR / 'runs', ROOTDIR / REPROPACKS_NAME / 'runs')
