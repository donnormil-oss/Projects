from apify_client import ApifyClient
import os

def job(Joburl):
    client = ApifyClient(os.getenv("APIFY_API_TOKEN"))
    run_input = {
    "count": 100,
    "scrapeCompany": True,
    "splitByLocation": False,
    "urls": [Joburl]
}
    run = client.actor("curious_coder/linkedin-jobs-scraper").call(run_input=run_input) 
    dataset_id = run["defaultDatasetId"]
    items = list(client.dataset(dataset_id).iterate_items())

    data = items[0]
    comp_name = data.get("companyName")
    career_pg_url = data.get("compayUrl")
    job_url = data.get("jobUrl")

    return comp_name,career_pg_url,job_url


if __name__  == "__main__":
    url = "https://www.linkedin.com/jobs/search/?keywords=software&location=United%20States"
    print(job(url))
