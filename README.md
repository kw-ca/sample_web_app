# sample web app

## 環境構築
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
```bash
cd /path/to/sample_web_app/apps/minimal_app
FLASK_APP=app.py FLASK_ENV=development flask run
```
