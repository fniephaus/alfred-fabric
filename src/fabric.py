import sys
import os
import commands
from workflow import Workflow

FAB_EXECUTABLE = '/usr/local/bin/fab'

# GitHub repo for self-updating
GITHUB_UPDATE_CONF = {'github_slug': 'fniephaus/alfred-pocket'}
# GitHub Issues
HELP_URL = 'https://github.com/fniephaus/alfred-fabric/issues'

def main(wf):
    # Change prefix to `wf:`
    wf.magic_prefix = 'wf:'

    # extract query
    query = wf.args[0] if len(wf.args) else None

    # load fabfiles from workflow settings
    fabfiles = wf.settings.get('fabfiles', [])

    query_split = query.split(' ')
    if query_split[0] == 'register':
        if len(query_split) == 2 and query_split[1].endswith('.py'):
            if query not in fabfiles:
                fabfiles.append(query_split[1])
                wf.settings['fabfiles'] = fabfiles
            return reopen_workflow()

        wf.add_item(
            'Register new fabfile',
            'Enter the full path to your fabfile.py',
            valid=False,
            icon='icon.png'
        )
        wf.send_feedback()
        sys.exit()

    if len(fabfiles) == 0:
        return reopen_workflow('register ')

    task_list = {}
    for fabfile in fabfiles:
        # list all tasks in the selected fabfile
        tasks = commands.getstatusoutput(
            '%s --fabfile=%s --shortlist' % (FAB_EXECUTABLE, fabfile)
        )[1].split('\n')

        if fabfile in task_list:
            task_list[fabfile] += tasks
        else:
            task_list[fabfile] = tasks

    for fabfile, fabfile_tasks in task_list.iteritems():
        for task in fabfile_tasks:
            if any(query.lower() in x.lower() for x in [task, fabfile]):
                wf.add_item(
                    task,
                    fabfile,
                    arg='%s --fabfile=%s %s' % (FAB_EXECUTABLE, fabfile, task),
                    autocomplete=task,
                    valid=True
                )

    if wf._items == []:
        wf.add_item(
            'No fabric tasks found for "%s".' % query,
            valid=False
        )

    wf.send_feedback()


def reopen_workflow(query=None):
    query = query or ''
    os.system(
        """ osascript -e 'tell application "Alfred 2" to run trigger "open" in workflow "com.fniephaus.fabric" with argument "%s"' """ % (
            query)
    )

if __name__ == '__main__':
    wf = Workflow(update_settings=GITHUB_UPDATE_CONF, help_url=HELP_URL)
    sys.exit(wf.run(main))
