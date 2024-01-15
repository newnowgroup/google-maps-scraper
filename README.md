<div align="center" style="margin-top: 0;">
  <h1> Google Maps Scraper 🗺️ </h1>
</div>

 Our goal is to scrape all the Google Maps reviews from the stores of the WMF group. <br>
 To do so we decided to fork the "Google Maps Scraper" project. We chose it because it is quite fast, lightweight and completely automated. If you want to check out the original project go [here](https://github.com/omkarcloud/google-maps-scraper). <br>
Also, for more info on the forked project check out the original [README](README_original.md) file.


## 🚀 Getting Started

1️⃣ Download Node.js 18+. Follow instructions [here](https://nodejs.org/en/download).

2️⃣ Clone the repo:
```shell
git clone https://github.com/newnowgroup/google-maps-scraper.git
cd google-maps-scraper
```

2️⃣ Create Conda environment 🐍:
```shell
conda env create --name google-maps-scraper python=3.10 pip
conda activate google-maps-scraper
```

2️⃣ Install Dependencies 📦:
```shell
pip install -r requirements.txt
```

3️⃣ Scrape the reviews:
```shell
python main.py
```

Once the scraping process is complete, you can find your leads inside your OneDrive folder, in the `wmf-reviews` directory.<br>

