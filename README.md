# Upload file to Mega

This GitHub action allows you to upload a file to Mega.

## Usage

```yml
- name: Upload assets
  id: mega-uploader
  uses: gh-actions-projects/mega-upload@v1.0.0
  with:
    folder: public
    dest-dir: databases
    email: ${{ secrets.MEGA_EMAIL }}
    password: ${{ secrets.MEGA_PASSWORD }}
```

**Required Parameters:**

- `folder`: the folder to be uploaded.
- `dest-dir`: the path where files will be saved
- `email`: provide your account email address
- `password`: provide your account password

**Environmetal variables:**

- Nothing

### Outputs

- `url`: url to the uploaded zip file

### Library

- Python **MegaPy** Docs [pypi](https://pypi.org/project/mega.py/)
