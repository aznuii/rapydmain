rapydmain is framework for python batch script.

# Features
- Automatically load config(JSON format).
- Output message when changed rapydmain status(e.g. script began, script ended, error occued).
- Automatically setup logger(use python logging).

# Usage
1. Setup project directories & files, like pj_template(https://github.com/aznuii/rapydmain/tree/main/pj_template).
```
[pj_dir]/
    config/
        fw.json
        loggin.json
        [any config file]
    log/
        [any log file]
```

2. Setup python script.
```
pip install rapydmain
```

3. Coding python script.
Use by "with" statement.
```
with rapydmain(Path(__file__).parent.parent) as main:
    # load config
    value = main.config['any1']['any2']

    # logging
    main.logger.info('log')
```
