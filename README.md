# Spam Checker for Synapse Matrix Server, checks Media Files for content-type

- Documentation: https://github.com/matrix-org/synapse/blob/v1.28.0/docs/spam_checker.md
- Source code: https://github.com/matrix-org/synapse/blob/v1.28.0/synapse/events/spamcheck.py
  - FileInfo: https://github.com/matrix-org/synapse/blob/v1.28.0/synapse/rest/media/v1/_base.py#L289
  - ReadableFileWrapper (file_wrapper): https://github.com/matrix-org/synapse/blob/v1.28.0/synapse/rest/media/v1/media_storage.py#L330
  - ModuleApi: https://github.com/matrix-org/synapse/blob/v1.28.0/synapse/module_api/__init__.py 
  - MediaRepository https://github.com/matrix-org/synapse/blob/v1.28.0/synapse/rest/media/v1/media_repository.py 

- Other Examples:
  - https://github.com/t2bot/synapse-simple-antispam
  - https://github.com/matrix-org/mjolnir/tree/master/synapse_antispam
  - https://github.com/matrix-org/synapse-spamcheck-badlist

## How to build:

https://packaging.python.org/tutorials/packaging-projects/ 

```
cd ${path_to_yout_python_test_dir}
python3 -m build
```

replace `${path_to_yout_python_test_dir}`

scp to server


## How to install:

```
cd /opt/venvs/matrix-synapse
source bin/activate
pip install -U synapse_mediacheck-Telegraphenbauanstalt --find-links file://${local_file_path}/synapse_mediacheck-Telegraphenbauanstalt-0.0.5.tar.gz
deactivate
```

replace `${local_file_path}`

I needed to install `sudo apt-get install python3-distutils`  

Edit Matrix-Synapse Config:

```
spam_checker:
  module: "synapse_mediacheck.SynapseMediacheck"
  config:
    media_path: "/var/lib/matrix-synapse/media/local_content/"
    allowed_mimetypes:
      - "image/jpeg"
      - "image/png"
      - "image/gif"
```

Restart Matrix-Synapse

## The file upload to the server is performed before the file is used in a message

- API:
- Media repo: https://github.com/matrix-org/synapse/blob/develop/docs/media_repository.md
- Config: siehe homeserver.yaml -> media_storage_providers
  