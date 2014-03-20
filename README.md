itunes-connect-autoingestion
============================

A simple Python port of Apple's Autoingestion.class for iTunes Connect

Run it from the command line like this:

```
$ python autoingestion.py <email> <password> <vendor ID> <Sales OR Newsstand> <Daily OR Weekly> <Summary OR Detailed OR Opt-In> <report date as YYYYMMDD>
```

If no report date is specified, yesterday's report will be fetched.

Apple's official docs here: https://www.apple.com/itunesnews/docs/AppStoreReportingInstructions.pdf
