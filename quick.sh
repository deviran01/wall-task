brew install git;
brew install allure;
git clone 'https://github.com/deviran01/wall-task.git'; \
# shellcheck disable=SC2164
cd ./wall-task; \
python3 -m venv venv; \
source venv/bin/activate; \
pip install -r ./pip/requirements.txt;
pytest --alluredir=allure-results
allure serve allure-results;
