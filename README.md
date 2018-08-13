# Harvest for LPDR IBEMC

## Versions

a0.1 - Init full backups: Git tag + full database backup in db_backup
a0.2 - Subset 1 2 3 with cleanup concepts and categories, fixed stats on all fields. Made available to ACMG 11/2/2016.

## Features

- clean project structure
    - `_site` directory for web server document root
        - copied static files and user uploaded media files
        - works well with nginx's `try_files` directive
        - `maintenance` directory for toggling maintenance mode's
- server configurations for nginx, uWSGI, and Supervisor
    - note: the paths will need to be updated to match your environment
- tiered settings for easier cross-environment support
    - `global_settings.py` for environment-independent settings
    - `local_settings.py` for environment-specific settings (not versioned)
    - `settings.py` for bringing them together and post-setup
- `local_settings.py.sample` template
- integration with [r.js](https://github.com/jrburke/r.js/)
    - compiles javascript/src => javascript/min
    - note: this requires NodeJS to be installed
- context processor for including more direct static urls
    - `{{ CSS_URL }}`
    - `{{ JAVASCRIPT_URL }}`
    - `{{ IMAGES_URL }}`
- full-featured fabfile.py for one-command deployment

## Local Settings

`local_settings.py` is intentionally not versioned (via .gitignore). It should
contain any environment-specific settings and/or sensitive settings such as
passwords, the `SECRET_KEY` and other information that should not be in version
control. Defining `local_settings.py` is not mandatory but will warn if it does
not exist.

## Fabfile Commands

- `mm_on` - turns on maintenance mode
- `mm_off` - turns off maintenance mode
- `deploy` - deploy a specific Git commit or tag to the host
