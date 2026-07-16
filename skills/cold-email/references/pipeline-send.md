# SEND — Launch via Lemlist

Turn approved copy into a live, sequenced campaign.

## Lemlist API basics

```
Base: https://api.lemlist.com/api
Auth: Basic (empty username, API key as password)
Rate limit: 10 requests/second per team
```

### Key endpoints

```
GET /campaigns # list all
POST /campaigns # create new
POST /campaigns/{id}/sequences # add email sequence steps
POST /campaigns/{id}/leads # add lead(s), batch
POST /campaigns/{id}/start # launch
POST /enrich # find email
POST /enrich/bulk # batch, 500 max
```

## Campaign creation flow

```
1. Create campaign POST /campaigns {"name": "Skool AI Q2"}
2. Add email sequence POST /campaigns/{id}/sequences
3. Upload leads (batch) POST /campaigns/{id}/leads
4. Start campaign POST /campaigns/{id}/start ✅
```

## Variables available in copy

```
# Standard
{{firstName}} {{lastName}} {{email}} {{companyName}} {{phone}} {{linkedinUrl}}

# Custom (from lead data)
{{communityName}} {{memberCount}} {{calculatedLTV}} {{completionRate}}
```

## Sending hygiene

- Warm inboxes; respect per-inbox daily caps (e.g. 15/day per inbox).
- Pause any inbox whose health drops (the real campaign paused 1 of 5 at ~70% health).
- Only send to `verified` emails from the ENRICH stage.
- Update the CRM stage to "Launched Sequence" when a lead enters a campaign.

## Config

Lemlist key → `configs/.lemlist-config.json`.
