# ImageUrl2Data
## Quick Sublime Text 3 plugin to embed images in markdown.

### Use for:

You have a markdown file with an image link like

`https://assets-cdn.github.com/images/modules/open_graph/github-octocat.png`
![](https://assets-cdn.github.com/images/modules/open_graph/github-octocat.png).

Your file is no longer self contained.

Run the "Image URL to Data" (from the command palette) on the selected url
and it will be replaced by something like:

``
data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABLAAAAJ2CAIAAADAIuwLA
ACLNklEQVR42uzXAQEAAAABIP9PM0S9KAUAAOCSEAIAAAghAAAAQggAAIAQAgAAIIQAAAA
IIQAAAEIIAACAEAIAACCEAAAACCEAAABCCAAAgBACAAAghAAAAAghAAAAQggAAIAQAgAAI
IRjvw4EAAAAAID8XxvhQlVVVUNYVVXVEFZVVTWEVVVVDWFVVVVDWFVV1RBWVVU1hFVVVUN
YVVXVEFZVV ...
``

Self-containment regained.