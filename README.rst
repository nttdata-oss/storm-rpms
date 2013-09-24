##################################
README
##################################

.. sectnum::

==========================
Concept
==========================

* Deploy binaries of Storm to /var/lib/storm.
* Manage the serice packages separately from the main sources of Storm.
* Make "storm" user and "storm" group to start processes.
* Use shell scripts provided by the Storm project to manage processes.

==========================
Requriement
==========================
* CentOS6
* The following packages should be installed.

  + rpm-build
  + zip, unzip

==========================
How to make Storm rpm
==========================

------------------
Clone spec files
------------------
Download spec files from the repository.

command example::

 $ cd <your working directory>
 $ git clone https://bitbucket.org/dobachi/storm-rpm.git

------------------------
Download storm binaries
------------------------
Download storm binaries from the official download link.

command example::

 $ wget https://dl.dropbox.com/u/133901206/storm-0.9.0-wip21.zip

Rename zip file.

command example::

 $ unzip -o storm-0.9.0-wip21.zip
 $ mv storm-0.9.0-wip21 storm-0.9.0
 $ tar cvzf storm-0.9.0.tgz storm-0.9.0

Copy tgz file to the rpmbuild directory.

command example::

 $ cp storm-0.9.0.tgz ~/rpmbuild/SOURCES

------------------
Copy spec file
------------------

Copy spec file of storm to the rpmbuild directory.

command example::

 $ cp storm-rpm/storm.spec  ~/rpmbuild/SPECS

-----------
Build rpm
-----------
Build rpm.

command example::

 $ rpmbuild -ba /root/rpmbuild/SPECS/storm.spec

================================
How to make Storm service rpm
================================

-------------------------------
Copy scripts and make tar file
-------------------------------
Copy scripts and config files to rpmbuild directory.

command example::

 $ mkdir ~/rpmbuild/SOURCES/storm-service-0.9.0
 $ cp -r storm-rpm/init.d ~/rpmbuild/SOURCES/storm-service-0.9.0
 $ cp -r storm-rpm/sysconfig ~/rpmbuild/SOURCES/storm-service-0.9.0

Make tar file.

command example::

 $ cd ~/rpmbuild/SOURCES
 $ tar cvzf storm-service-0.9.0.tgz storm-service-0.9.0

------------------
Copy spec file
------------------
Copy spec file of storm to the rpmbuild directory.

command example::

 $ cd <your working directory>
 $ cp storm-rpm/storm-service.spec  ~/rpmbuild/SPECS

-----------
Build rpm
-----------
Build rpm.

command example::

 $ rpmbuild -ba /root/rpmbuild/SPECS/storm-service.spec

=========================
ToDo
=========================
The following is the main of ToDo.

* <to-do>



.. vim: ft=rst tw=0
