import requests
import json
from pprint import pprint


def harvest_contributions(url):
    contributions = []
    response = requests.get(url)
    partial_contributions = response.json()
    contributions.extend(partial_contributions)

    if "next" in response.links:
        pprint(response.links["next"]["url"])
        contributions.extend(harvest_contributions(response.links["next"]["url"]))
        return contributions
    else:
        return []


def main():
    owner = "dexpota"
    url = "https://api.github.com/users/{}/events".format(owner)

    contributions = harvest_contributions(url)

    with open("contributions.json", "w+") as fp:
        json.dump(contributions, fp)


main()
