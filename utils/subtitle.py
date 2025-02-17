from dash import html

data_source_details = {
    "rethink19": dict(
        name="EA Survey 2019",
        url="https://www.rethinkpriorities.org/blog/2019/12/5/ea-survey-2019-series-community-demographics-amp-characteristics",
        download_url="/assets/data/rp_survey_data_2019/rp_survey_2019.xlsx",
    ),
    "rethink19-geo": dict(
        name="EA Survey 2019",
        url="https://rethinkpriorities.org/publications/eas2019-geographic-distribution-of-eas",
        download_url="/assets/data/rp_survey_data_2019/country2.csv",
    ),
    "ea_forum": dict(
        name="forum.effectivealtruism.org",
        url="https://forum.effectivealtruism.org/graphiql",
        download_url="/assets/data/general_ea/ea_forum.json",
    ),
    "open_phil": dict(
        name="openphilanthropy.org",
        url="https://www.openphilanthropy.org/giving/grants",
        download_url="https://www.openphilanthropy.org/giving/grants/spreadsheet",
    ),
    "funds_payout": dict(
        name="funds.effectivealtruism.org",
        url="https://funds.effectivealtruism.org/",
        download_url="/assets/data/general_ea/ea_funds_grants.csv",
    ),
    "founders_pledge": dict(
        name="founderspledge.com",
        url="https://founderspledge.com/",
        download_url="/assets/data/donations_overview/misc.csv",
    ),
    "gwwc": dict(
        name="givingwhatwecan.org",
        url="https://www.givingwhatwecan.org/",
        download_url="/assets/data/donations_overview/misc.csv",
    ),
    "growth": dict(
        name="EA Growth Metrics for 2018",
        url="https://forum.effectivealtruism.org/posts/MBJvDDw2sFGkFCA29/is-ea-growing-ea-growth-metrics-for-2018",
    ),
    "gwwc_pledges": dict(
        name="dashboard.effectivealtruism.org",
        url="http://dashboard.effectivealtruism.org/public/question/a8499095-be16-46fe-af1f-e3e56ee04e88",
        download_url="/assets/data/donations_overview/misc.csv",
        custom_class_gwwc="gwwc-subtitle",
    ),
    "gwwc_donations": dict(
        name="dashboard.effectivealtruism.org",
        url="http://dashboard.effectivealtruism.org/public/question/9906735e-1350-4353-9828-bb3ec16137e3",
        download_url="/assets/data/donations_overview/misc.csv",
        custom_class_gwwc="gwwc-subtitle",
    ),
    "gwwc_orgs": dict(
        name="dashboard.effectivealtruism.org",
        url="http://dashboard.effectivealtruism.org/public/question/b3887098-686a-491c-9f9c-9a5b0e2b7fd8",
        download_url="/assets/data/donations_overview/misc.csv",
        custom_class_gwwc="gwwc-subtitle",
    ),
    "x-risks": dict(
        name="The Precipice by Toby Ord",
        url="https://res.cloudinary.com/dwbqmbkdb/image/upload/v1586225593/Table_6.1_td3bzd.png",
        download_url="https://res.cloudinary.com/dwbqmbkdb/image/upload/v1586225593/Table_6.1_td3bzd.png",
    ),
    "key-ea-numbers": dict(
        name="Key EA Numbers",
        url="https://github.com/benthamite/EA-numbers",
        download_url="https://raw.githubusercontent.com/benthamite/EA-numbers/main/EA-numbers.json",
    ),
}


def get_data_source(data_sources):

    download_img_url = "/assets/images/ui-images/download.svg"

    if len(data_sources) == 0:
        return html.Div()

    if type(data_sources) == str:
        data_sources = [data_sources]

    content = ["Data source: "]

    list_of_source_links = []
    for data_source in data_sources:

        details = data_source_details[data_source]

        content.append(html.A(details["name"], href=details["url"]))

        # download link
        if "download_url" in details:
            content.append(
                html.A(
                    html.Img(src=download_img_url, className="icon-download"),
                    href=details["download_url"],
                )
            )

        content.append(", ")

    # Remove the last comma.
    content[-1] = ""

    for data_sources in data_source:
        details = data_source_details[data_source]

        if "custom_class_gwwc" in details:
            return html.P(content, className="download_subtitle gwwc-subtitle")
        else:
            return html.P(content, className="download_subtitle")


def get_instructions(zoom=False, hover="bars", extra_text=[]):

    content = []

    if hover:
        content.append(f"Hover for more details.")

    if zoom:
        content.append("Click and drag to zoom. Double click to unzoom.")

    if type(extra_text) == str:
        content.append(extra_text)
    elif type(extra_text) == list:
        content.extend(extra_text)

    return html.P(" ".join(content))
