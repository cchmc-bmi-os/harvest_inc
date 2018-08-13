from optparse import make_option
from django.core.management.base import BaseCommand
import os
import datetime
from django.conf import settings
import subprocess

def backup_name(filename, tag, date_tag, suffix, schema):
    date_str = datetime.datetime.now().strftime("%Y-%m-%d_%H%M")
    schema = schema + '_' if schema else ''
    bak = date_str + '_' + schema + filename + '_' + tag + suffix if date_tag else schema + filename + tag + suffix
    return (bak)

def backup(filename, outdir, tag, date_tag, suffix, schema):
    bak = backup_name(filename, tag, date_tag, suffix, schema)
    print('Backing up {} in {}'.format(bak, outdir))

    if not os.path.isdir(outdir):
        raise Exception('{} does not exists -don\'t know where to write the backup file'.format(outdir))

    DBS = settings.DATABASES
    db = DBS['default']
    if 'postgresql' not in db['ENGINE']:
        raise Exception('The backup command works only for Postgres databases')

    schema = '--schema {}'.format(schema) if schema else ''
    cmd = 'pg_dump -h {0} -U {1} {2} --format plain {3}> {4}'.format(
        db['HOST'],
        db['USER'],
        db['NAME'],
        schema,
        os.path.join(outdir, bak)
        )
    print(cmd)
    subprocess.call(cmd, shell=True)
    subprocess.call(["ls", "-al", outdir])

class Command(BaseCommand):
    """Creates a database backup

    """
    help = 'Creates a database backup'

    option_list = BaseCommand.option_list + (
        make_option(
            '--filename',
            dest='filename',
            default='backup',
            help='Core of the backup filename.',
        ),
        make_option(
            '--outdir',
            dest='outdir',
            default='../../db_backup',
            help='Directory where to write the backup file.',
        ),
        make_option(
            '--tag',
            dest='tag',
            default='',
            help='Add the tag to the file name.',
        ),
        make_option(
            '--date_tag',
            dest='date_tag',
            default=True,
            help='Set to false to avoid appending the date to the backup filename.',
        ),
        make_option(
            '--suffix',
            dest='suffix',
            default='.backup',
            help='Backup file suffix.',
        ),
        make_option(
            '--schema',
            dest='schema',
            default='',
            help='Schema to be saved..',
        ),

    )

    def handle(self, *args, **options):
        print('Start...')
        filename = options['filename']
        outdir = options['outdir']
        tag = options['tag']
        date_tag = (bool)(options['date_tag'])
        suffix = options['suffix']
        schema = options['schema']
        backup(filename, outdir, tag, date_tag, suffix, schema)
        print('Done.')
