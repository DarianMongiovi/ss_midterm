Running ss_discord_bot.py will initiate posting one haiku to the discord channel.

Schedule as a cron job to run twice a day at noon and midnight.

*Open cron tab
crontab -e

*Add entry
0 0,12 * * * /home/user/Desktop/ss_midterm/cron_job.sh >> /home/user/Desktop/ss_midterm/bot_log.txt 2>&1

