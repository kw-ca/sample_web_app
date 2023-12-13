# sample web app

## 環境構築
### AL2環境
```bash
yum install gcc zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel tk-devel libffi-devel patch
```

### python
- install pyenv
```bash
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```
- 環境変数の設定
```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
```
- install python
```bash
pyenv install 3.9.7
pyenv global 3.9.7
```

- install pipenv
```bash
pip install pipenv
cd /path/to/sample_web_app
pipenv install
echo "export PIPENV_VENV_IN_PROJECT=true" >> ~/.bash_profile
```

## 実行方法
- 開発環境
```bash
cd /path/to/sample_web_app/apps/minimal_app
FLASK_APP=app.py FLASK_ENV=development flask run -p 3000
```
- 本番環境
```bash
waitress-serve --port 3000 --call "app:create_app"
```
