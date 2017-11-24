A painless way to get metadata from sites.

## Installation

`pip install metascrapy`

## Usage

```
import metascrapy

scraper = metascrapy.Metadata()
scraper.scrape('www.google.com')
scraper.title
# 'Google'
```

## Available Metadata

* `title`
* `description`
* `image`
* `x_frame_options`

Submit an issue or PR for more!