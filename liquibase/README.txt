Connecting to the Database

With JDBC, a database is represented by a URL (Uniform Resource Locator). With PostgreSQL™, this takes one of the following forms:

    jdbc:postgresql:database
    jdbc:postgresql:/
    jdbc:postgresql://host/database
    jdbc:postgresql://host/
    jdbc:postgresql://host:port/database
    jdbc:postgresql://host:port/



This directory allows you both run Liquibase in a normal production setting to manage your database as well as develop
and test Liquibase extensions.

ROOT LIQUIBASE DIRECTORY STRUCTURE:
----------------------------------------

The root of this directory is designed to run Liquibase. There are shell and batch scripts (liquibase and liquibase.bat)
which will run the Liquibase command line application.

The "lib" directory is automatically scanned by the liquibase scripts and all .jar files are added to the classpath.
If you have JDBC drivers or Liquibase extensions that you want to be automatically included, add them to this directory.

Liquibase
Liquibase installation and configuration

    Download liquibase from Liquibase download page.

    Extract liquibase-3.x.x-bin.zip into your working directory.

    Add full path of your_working_dir/liquibase-3.x.x-bin path to PATH environment variable.

In Ubuntu 14.04,include liquibase path to PATH environment variable as follows: $vim ~/.bashrc open and add export PATH="your_working_dir/liquibase-3.4.2-bin:$PATH" at the end of file and save this file with pressing :wq and ENTER.

$source ~/.bashrc

In Windows systems,add your_working_dir/liquibase-3.x.x-bin to the system path.

    Run liquibase at your terminal or command promt.If it outputs something help command then you have successfully configured liquibase.

Liquibase Structure

    database/
    ├── changelog
    |   ├── db.changelog-master.xml
    |   └── db.changelog-1.0.xml
    |   ├── db.changelog-1.1.xml
    ├── lib
    |   ├── postgresql.jar
    └── README.md

Project hierarchy contains following folders with their significance:

    changelog:
    This folder maintains all database schema versioning with respective incremental changes. db.changelog-master.xml includes all changelog versions.

    scripts:
    Sometimes Liquibase can not handle complex SQL scripts related to specific database.Those SQL scripts are loaded in respective changelog version. Example Stored Procedure,Views,Triggers.

    lib:
    This folder has database drivers which required to maintain JDBC connections at the time of schema migration.

Liquibase commands

Please follow the Liquibase commandline help.
PostgreSQL schema migration

    Clone this repositoty into your workspace. git clone https://github.com/sharadvishe/liquibase.git

    Go to folder liquibase/database. cd liquibase/database

    Execute below command to migrate/rollback changelog versions which are in the folder changelog:

        To migrate all changelog versions,run below command:
        $liquibase --driver=org.postgresql.Driver --classpath=lib/postgresql.jar --changeLogFile=changelog/db.changelog-master.xml --url="jdbc:postgresql://[host]:[port]/[database]" --username=[username] --password=[password] migrate

        To migrate number of changelog versions,run below command:
        $liquibase --driver=org.postgresql.Driver --classpath=lib/postgresql.jar --changeLogFile=changelog/db.changelog-master.xml --url="jdbc:postgresql://[host]:[port]/[database]" --username=[username] --password=[password] updateCount number

        To rollback last number of changelog versions,run below command:
        $liquibase --driver=org.postgresql.Driver --classpath=lib/postgresql.jar --changeLogFile=changelog/db.changelog-master.xml --url="jdbc:postgresql://[host]:[port]/[database]" --username=[username] --password=[password] rollbackCount number

    Where,
    host : PostgreSQL server ip address
    port : PostgreSQL server port
    username: PostgreSQL server username
    password: PostgreSQL server password
    database: Target PostgreSQL database on which all schema will be maintained.


