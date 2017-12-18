Please follow me on https://steemit.com/@yuxi

## A steemit posts backup tool

As time passes, many steemians have written losts of posts in Steemit. It's a time to think about the backups. Unfortunately, Steemit doesnot provide backup feature. I have implemented a tool to do the backup. It is based on Python Steem library and has been tested on Ubuntu 16. 

## Features

### Multiple users support

The tool can be easily configured to work with multiple accounts - just modify the configuration file and add new user definition.

### Support both full backup and incremental backup

When you run this script first time, you may want to do a full backup. In this case, just change 'latest_posts_only' to 'false' in the configuration file. After this, you may want to schedule a daily cron job to do the backup. To do the incremental backup, just change 'latest_posts_only' to 'true' and 'check_back_hours' to the peroid of hours to check in each run.

### Excluded categories support

People won't backup some posts, e.g. test posts under category 'test'. To enable this, just add categories in 'exclude_categories' in the configuration file.

### Customizable backup folder and file name

The backup folder is also customizable by changing 'backup_folder' property in the configuration file. Also, optional date prefix can be configured to backup file names.
