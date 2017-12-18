from sys import argv
from steem.blog import Blog
from datetime import datetime,timedelta
import time,yaml,sys
import traceback
from slugify import slugify

def backup(user, config_file):
  dict = []
  with open("config/"+config_file, 'r') as stream:
    try:
      dict = yaml.load(stream)
    except yaml.YAMLError as exc:
      print(exc)

  if dict[user] is None or dict[user]=="":
    print ("Cannot find settings for user: %s" % user)
    exit()

  latest_posts_only   = dict[user]["latest_posts_only"]
  check_back_hours    = int(dict[user]["check_back_hours"])
  backup_folder       = dict[user]["backup_folder"]
  add_date_prefix     = dict[user]["add_date_prefix"]
  exclude_categories  = dict[user]["exclude_categories"].split(',')

  number_of_batch = 10
  blog            = Blog(user)

  try:
    posts = blog.take(number_of_batch)
    reached_end = False
    while (posts is not None) and len(posts)>0 and reached_end==False:
      for p in posts:
        _date     = p['created']
        _permlink = p['permlink']
        _title    = p['title']
        _body     = p['body']
        _category = p['tags'][0]

        if latest_posts_only==True and (_date+timedelta(hours=check_back_hours)<datetime.now()):
          print('reached the end, exit...')
          reached_end = True
          break

        if _category not in exclude_categories:
          print("processing %s %s %s" % (_date.strftime('%Y%m%d'), _permlink, _title))
          # use title as filename
          file_name =  "%s.md" % slugify(_title)
          target_md_file_name = "%s%s" % (backup_folder, file_name)

          if add_date_prefix==True:
            target_md_file_name = "%s%s_%s" % (backup_folder,_date.strftime('%Y%m%d'),file_name)

          with open(target_md_file_name, "w") as file:
            file.write(_body)
        else:
          print('  ignored because it is in excluded category list.')

      posts = blog.take(number_of_batch)
  except:
    traceback.print_exc()

if len(sys.argv) !=2:
  print ('Usage: python steemit_backup.py ACCOUNT')
  print ('e.g. python steemit_backup.py yuxi')
  exit()

user        = argv[1]
config_file = 'system_config.yaml'
backup(user, config_file)

