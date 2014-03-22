import sys
import commands
from workflow import Workflow

FAB_EXECUTABLE = '/usr/local/bin/fab'


def main(wf):
    task_list = commands.getstatusoutput(
        FAB_EXECUTABLE + ' --shortlist')[1].split('\n')
    for task in task_list:
        wf.add_item(
            task, arg=FAB_EXECUTABLE + ' ' + task, autocomplete=task, valid=True)

    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
