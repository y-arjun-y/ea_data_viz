# [Effective Altruism Data](https://effectivealtruismdata.com)

![Effective Altruism Data](/assets/images/ea-data/eadata.png)

[Effective Altruism](https://www.effectivealtruism.org/) (EA) is movement that uses evidence and careful analysis to figure out how we can use our resources to help others the most.

There are several EA organisations that collect data on grants, donors, and pledges. This website aggregates and visualises that data.

Made with Python using [Dash](https://dash.plotly.com/) and deployed on [effectivealtruismdata.com](https://effectivealtruismdata.com) with [Heroku](heroku.com).

For more awesome EA-related data visualizations, see the [EA Hub map](https://eahub.org/) and the [EA Funds dashboard](https://app.effectivealtruism.org/funds/about/stats).

## How To Run

1. Install [pipenv](https://pipenv.pypa.io/en/latest/).
2. Run the following in the terminal:

```
git clone https://github.com/hamishhuggard/ea_data_viz.git
cd ea_data_viz
pipenv run python app.py
```
