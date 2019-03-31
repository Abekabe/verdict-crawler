# Verdict Crawler

Using python code to crawl verdicts form Judicial yuan of Taiwan. 

## Getting Started

You can obtain the verdict of 所得稅 in 台北高等行政法院 by entering start and end date now. The output file would be a csv file which column is id, number, date, reason, content of verdict.
In addition, each content of verdict would save as txt file at the project_folder/data which use number as file name.

### Prerequisites

```
requests
bs4
```
#### For Windows
To install python and pip, the [link](https://ithelp.ithome.com.tw/articles/10210071?sc=rss.qu) would be useful.
After installing pip, enter following command in the cmd:
```
python -m pip install requests
python -m pip install bs4
```

#### For Linux

Make sure your python and pip is ready, enter following command in the cmd:
```
python -m pip install requests
python -m pip install bs4
```

### Installing

You can download the code from github directly or use command line:

```
git pull https://github.com/Abekabe/verdict-crawler.git
```


## Running the tests
For example, you can execute the code like this:

```
python crawler.py
start(yyyymmdd): 20180901
end(yyyymmdd): 20180910
```
The code will craw the Judicial yuan website automatically. If there show lots of **AttributeError** or **ConnectionError** which means the Judicial yuan website have some protection and you should wait a minute then execute this code again.


## Contributing

1. Fork it (https://github.com/yourname/yourproject/fork)
2. Create your feature branch (git checkout -b feature/fooBar)
3. Commit your changes (git commit -am 'Add some fooBar')
4. Push to the branch (git push origin feature/fooBar)
5. Create a new Pull Request

## Versioning

* 0.1.0
    + The first proper release

## Authors

* **Caleb Lee** - *Initial work* - [Abekabe](https://github.com/Abekabe)

## License

This project is licensed under the MIT License.
