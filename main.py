#Import Packages
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from datetime import datetime
import argparse
import sys, time

parser = argparse.ArgumentParser(add_help=False, description=('Download reviews from BookMyShow'))
parser.add_argument('--help', '-h', action='help', default=argparse.SUPPRESS, help='Show this help message and exit')
parser.add_argument('--movie_url', '-m', help='Enter Url extract reviews')
args = parser.parse_args()

no_of_pagedowns, review = 60, []
url = args.movie_url + '/user-reviews'
options = Options()
options.add_argument("--headless")
browser = webdriver.Chrome(options=options)
browser.get(url)
start_time = datetime.now()
time.sleep(1)

element = browser.find_element_by_tag_name("body")

while no_of_pagedowns:
    element.send_keys(Keys.PAGE_DOWN)
    time_delta = datetime.now() - start_time
    time.sleep(1)
    sys.stdout.write('\r' + str(time_delta) + " seconds off" + '\r')
    sys.stdout.flush()
    no_of_pagedowns-=1

try:
    review_elems = browser.find_elements_by_class_name("__reviewer-text")
    for post in review_elems:
        review.append(post.text)
except TimeoutException:
    print("Timed out waiting for page to load")

browser.quit()

def review_analyzer(review):
    analyser = SentimentIntensityAnalyzer()
    neu_sum, neg_sum, compound_sum, pos_sum, count = 0,0,0,0,0
    for comment in review:
        count += 1
        sys.stdout.write('Downloaded %d comment(s)\r' % count)
        sys.stdout.flush()
        score = analyser.polarity_scores(comment)
        neu_sum += score['neu']
        neg_sum += score['neg']
        pos_sum += score['pos']

    if count:
        print('\nAnalyzing comments')
        time.sleep(1)
        final_scores = {"neu" : round(neu_sum / count, 3), "neg" : round(neg_sum / count, 3), "pos" : round(pos_sum / count, 3), "compound" : round(compound_sum / count, 3)}
        return final_scores
    else:
        return None


if __name__ == '__main__':
    pol_scores = review_analyzer(review)
    print("Polarity Scores: ", pol_scores)
