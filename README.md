# Fika Script email automation

## Instructions

1. Create a YAML file named recipients.yaml and fill in the email recipients, according to recipients.yaml.template, and place the file in the repo root folder.
2. Create a YAML file named message.yaml and fill in the email message, according to message.yaml.template, and place the file in the repo root folder.
3. Send email to the top recipient in the recipients.yaml, with the message in message.yaml, by executing

```bash
  python3 ./email_automation.py send recipient.yaml message.yaml
```

3. Rotate recipients in recipients.yaml, i.e. move the top recipient to the bottom, by executing

```bash
  python3 ./email_automation.py rotate 
```

4. Create a cronjob via crontab and schedule sending and rotation. Call the command below, and follow the instructions that appear

```bash
  crontab -e 
```

5. Here is an example of a working cronjob. Remember that the time is given in the system's time, so if the system has time UTC and your time is UTC+2, you need to offset your job time by 2 hours
```
# Edit this file to introduce tasks to be run by cron.
# 
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
# 
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').
# 
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
# 
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
# 
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
# 
# For more information see the manual pages of crontab(5) and cron(8)
# 
# m h  dom mon dow   command
0 8 * * 1 /home/alexander_bukk/workspace/email-automation/venv/bin/python3 /home/alexander_bukk/workspace/email-automation/email_automation.py send /home/alexander_bukk/workspace/email-automation/recipients.yaml /home/alexander_bukk/workspace/email-automation/message.yaml
0 8 * * 3 /home/alexander_bukk/workspace/email-automation/venv/bin/python3 /home/alexander_bukk/workspace/email-automation/email_automation.py send /home/alexander_bukk/workspace/email-automation/recipients.yaml /home/alexander_bukk/workspace/email-automation/message.yaml
0 15 * * 4 /home/alexander_bukk/workspace/email-automation/venv/bin/python3 /home/alexander_bukk/workspace/email-automation/email_automation.py rotate /home/alexander_bukk/workspace/email-automation/recipients.yaml
```