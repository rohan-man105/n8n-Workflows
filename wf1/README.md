# LLM Email Code Review

An n8n workflow that watches for email from a chosen sender, uses OpenAI to
summarize the code and add explanatory comments in parallel, then emails the
combined result back to you.

## Contents

- `LLM Workflow (1).json` - the n8n workflow to import.
- `image.png` - workflow screenshot.

## Workflow flow

```text
Gmail Trigger
  -> Summariser ----\
  -> Commentor ------> Merge -> Aggregate -> HTML formatter -> Gmail
```

The workflow currently uses `gpt-4o-mini` for the three OpenAI model nodes and
checks Gmail every minute.

## Prerequisites

- An n8n instance with Gmail and OpenAI nodes available.
- A Gmail OAuth2 credential in n8n.
- An OpenAI API credential in n8n.
- Access to the Gmail account that receives and sends the messages.

## Import and configure

1. In n8n, open **Workflows** and select **Import from File**.
2. Select `LLM Workflow (1).json` from this folder.
3. Open the **Gmail Trigger** and choose your Gmail OAuth2 credential.
4. Open **Send a message** and choose the same (or another) Gmail OAuth2
   credential.
5. Open each **OpenAI Chat Model** node and choose your OpenAI credential.
6. Replace the trigger's sender filter and the email recipient with addresses
   appropriate for your setup.
7. Send a test email containing code in the message text, test the workflow,
   and activate it only after the result looks correct.

## Security and sharing

The JSON references credentials by name/type; it should not contain the secret
values themselves. Nevertheless, it includes email addresses and all prompts,
so keep this project private unless you first replace personal addresses with
placeholders such as `sender@example.com` and `recipient@example.com`.

Never put API keys or OAuth client secrets into workflow node fields, Code
nodes, README files, `.env` files, screenshots, execution exports, or Git
commits. Store them as n8n credentials instead. When someone imports this
workflow, they must create their own credentials and select them in the nodes.

## Maintenance

After a meaningful change in n8n, export the workflow back to this folder and
commit the JSON together with any README update. Use a descriptive commit
message, for example: `feat(wf1): improve code-comment prompt`.

