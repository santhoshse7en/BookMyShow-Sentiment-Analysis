# BookMyShow Sentiment Analysis

This is the code for the BookMyShow Sentiment Analyzer

## Dependencies

    * selenium
    * vaderSentiment
    * chromedriver-install

## Dependencies Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install following
```bash
pip install -r requirements.txt
```

## Usage

Download it by clicking the green download button here on Github. You only need to parse argument specific BookMyShow Movie_URL.

```bash
python main.py --movie_url 'https://in.bookmyshow.com/hyderabad/movies/20/ET00042213'

or

python main.py -m 'https://in.bookmyshow.com/hyderabad/movies/20/ET00042213'
```

## Output

![capture](https://user-images.githubusercontent.com/47944792/53886316-c3002b00-4045-11e9-8a56-10ef06275951.PNG)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
