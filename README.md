# n8n Workflows

This repository stores independent n8n workflow projects. Each project lives in
its own folder under `n8n-workfls` and can include its exported workflow JSON,
setup instructions, screenshots, and safe example data.

## Structure

```text
n8n-workfls/
  wf1/                 # one workflow project
  wf2/                 # another workflow project
  ...
```

Start with the instructions in each workflow folder's `README.md`. Do not
commit credentials, API keys, OAuth client secrets, `.env` files, or n8n's
database/export files containing credentials.

