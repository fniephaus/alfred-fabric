import sys
import commands
from os.path import expanduser
from workflow import Workflow

FAB_EXECUTABLE = '/usr/local/bin/fab'

def main(wf):
    import yaml

    # expand user folder
    home = expanduser("~")

    # open raw file
    stream = open(home + '/.fabfiles.yml')

    # load file as a python object
    fabfiles = yaml.load(stream)

    # extract query
    query = wf.args[0] if len(wf.args) else None
    # remove backslash from query
    query = query.replace("\\","")

    # check if there are any matches
    fabfile = filter(lambda x: x['name'] == query, fabfiles)

    # in there's a match
    if query and fabfile and len(fabfile) > 0:

        # list all tasks in the selected fabfile
        task_list = commands.getstatusoutput(
            FAB_EXECUTABLE + ' --fabfile=' + fabfile[0]['path'] + ' --shortlist')[1].split('\n')

        if not 'Traceback' in task_list[0]:
            for task in task_list:
                wf.add_item(
                    task, arg=FAB_EXECUTABLE + ' --fabfile=' + fabfile[0]['path'] + ' ' + task, autocomplete=task, valid=True)
        else:
            wf.add_item(
                'An error occurred', 'Please check your "~/.fabfiles.yml" file or your fabfile', valid=False)

    # otherwise, list configured fabfiles
    else:
        for fabfile in fabfiles:
            wf.add_item(
                fabfile['name'], ' ' + fabfile['path'], autocomplete=fabfile['name'], valid=False,
                icon=fabfile['icon'] if 'icon' in fabfile else 'icon.png')

    # write data
    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow(libraries=['./lib'])
    sys.exit(wf.run(main))
