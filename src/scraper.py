import requests
import argparse
import xml.etree.ElementTree as et

SITEMAP_URL = "https://theflixertv.to/sitemap.xml"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='Flixer Webscraper',
        description="Given a path to a text file, writes a list of all movies currently on https://theflixertv.to/",
    )
    parser.add_argument("-filename", "-f", type=str, dest="filename", required=True)
    parser.add_argument("-verbose", "-v", action='store_true', default=False, dest="verbose", required=False)
    args = parser.parse_args()

    # open file to write to
    outfile = open(args.filename, "w")

    # need to get the xml file to then parse with et
    sitemap = requests.get(SITEMAP_URL)
    # parse the XML request into a ElementTree obj for traversal
    sitemap_root = et.fromstring(sitemap.content)
    # traverse urls to other xml files containing the lists of movie urls, names, etc
    for sitemap in sitemap_root:
        loc = sitemap[0].text
        if 'list' in loc:
            # parse the movie list
            movielist = requests.get(loc)
            movielist_root = et.fromstring(movielist.content)
            # iterate over urls to movies
            for url in movielist_root:
                outfile.write(url[0].text + '\n')
            if args.verbose: print("Finished extracting {}".format(loc))

    outfile.close()