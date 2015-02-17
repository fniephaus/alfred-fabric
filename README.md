Fabric for Alfred
=============

Quickly execute your Fabric tasks using Alfred v2

![Fabric for Alfred Screenshot](https://raw.github.com/mateusrevoredo/alfred-fabric/master/screenshot-01.png)

![Fabric for Alfred Screenshot](https://raw.github.com/mateusrevoredo/alfred-fabric/master/screenshot-02.png)

## Installing
Create a YAML file in your home directory named `~/.fabfiles.yml`
```
  - name: Fabfile 1
    path: /Users/mateusrevoredo/Dropbox/fabfile.py
    icon: ~/Downloads/vagrant-icon.png

  - name: Fabfile 2
    path: /hoadf/asdfadffasdf
```

Add an entry for each fabfile that you want to list in the workflow.

Each entry must have the following fields:

* #####Name
 Name to be displayed in the list

* #####Path
 Full path of the fabfile

* #####Icon(optional)
 Path to an image file to be used to identify the fabfile.
 If this field is not supplied the script will use the default icon as shown in the image above

## Requirements
- [Fabric](http://fabfile.org) needs to be installed and configured
