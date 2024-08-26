# flixer-movie-list
Webscraper for getting the list of all movies available on https://theflixertv.to 

## Structure of the site being scraped

The sitemap XML contains lists of movies in the following form:

```xml
<sitemapindex>
    <sitemap>
        <loc>https://theflixertv.to/sitemap-list-1.xml</loc>
    </sitemap>
    <sitemap>
        <loc>https://theflixertv.to/sitemap-list-2.xml</loc>
    </sitemap>
    <sitemap>
        <loc>https://theflixertv.to/sitemap-list-3.xml</loc>
    </sitemap>
    .
    .
    .
    <sitemap>
        <loc>https://theflixertv.to/sitemap-list-29.xml</loc>
    </sitemap>
</sitemapindex>
```

Each of these sitemap's contain sets of urls to the movies, for example in the first list:

```xml
<urlset>
    <url>
        <loc>
            https://theflixertv.to/movie/watch-amp-house-massacre-full-111022
        </loc>
        <changefreq>daily</changefreq>
        <priority>0.7</priority>
    </url>
    .
    .
    .
</urlset>
```

## Usage

To extract the list of currently available movies to a text file:

```console
python scraper.py -filename out.txt
```

To get progress on the scraping you can toggle the verbose flag with either -v or -verbose.

The result will be a text file containing the urls to every movie on the site.
