# Fika Script email automation

## Instructions

1. Create a YAML file named recipients.yaml and fill in the email recipients, according to recipients.yaml.template, and place the file in the repo root folder.
2. Send email to the top recipient in the recipients.yaml by executing

```bash
  python3 ./email_automation.py send 
```

3. Rotate recipients in recipients.yaml, i.e. move the top recipient to the bottom, by executing

```bash
  python3 ./email_automation.py rotate 
```

4. Create a cronjob via crontab and schedule sending and rotation. Call the command below, and follow the instructions that appear

```bash
  crontab -e 
```

5. Here is an example of a working cronjob
TODO
