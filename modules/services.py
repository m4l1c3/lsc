"""
Service enumeration
"""
import os
from modules.logger import Logger

class Services(object):
    """
    Object for service enumeration
    """

    logger = Logger()

    def __init__(self):
        self.services = {}
        self.services_as_root = {}
        self.installed_applications = {}
        self.plaintext_passwords = {}
        self.scheduled_jobs = {}
        self.service_configurations = {}

    def run(self):
        """
        generic run method
        """
        self.logger.normal_output("Running Service Checks")
        self.get_services()
        self.get_services_as_root()
        self.get_installed_applications()
        self.get_for_plaintext_passwords()
        self.get_scheduled_jobs()
        self.get_service_configurations()

    def get_services(self):
        """
        get services
        """
        self.logger.normal_output("Running services")
        self.services.update({"ps aux": os.system("ps aux")})
        self.services.update({"ps aux -ef": os.system("ps -ef")})
        # self.services.update({"top": os.system("top")})
        self.services.update({"cat /etc/services": os.system("cat /etc/services")})

    def get_services_as_root(self):
        """
        get root services
        """
        self.logger.normal_output("Running services as root")
        self.services_as_root.update({"ps aux |grep root": os.system("ps aux | grep root")})
        self.services_as_root.update({"ps -ef | grep root": os.system("ps -ef | grep root")})

    def get_installed_applications(self):
        """
        get installed applications
        """
        self.logger.normal_output("Running installed apps")
        self.installed_applications.update({"ls -alh /usr/bin": os.system("ls -alh /usr/bin/")})
        self.installed_applications.update({"ls -alh /sbin/":  os.system("ls -alh /sbin/")})
        self.installed_applications.update({"dpkg -l":  os.system("dpkg -l")})
        self.installed_applications.update({"rpm -qa":  os.system("rpm -qa")})
        self.installed_applications.update(
            {"ls -alh /var/cache/apt/archives0":  os.system("ls -alh /var/cache/apt/archivesO")}
        )
        self.installed_applications.update(
            {"ls -alh /var/cache/yum":  os.system("ls -alh /var/cache/yum/")}
        )

    def get_service_configurations(self):
        """
        get service configurations
        """
        self.logger.normal_output("Running service configs")
        self.service_configurations.update({"syslog": os.system("cat /etc/syslog.conf")})
        self.service_configurations.update({"chhtp": os.system("cat /etc/chttp.conf")})
        self.service_configurations.update({"lighthttpd": os.system("cat /etc/lighttpd.conf")})
        self.service_configurations.update({"cupsd": os.system("cat /etc/cups/cupsd.conf")})
        self.service_configurations.update({"inetd": os.system("cat /etc/inetd.conf")})
        self.service_configurations.update({"apache2": os.system("cat /etc/apache2/apache2.conf")})
        self.service_configurations.update({"my.conf": os.system("cat /etc/my.conf")})
        self.service_configurations.update({"httpd": os.system("cat /etc/httpd/conf/httpd.conf")})
        self.service_configurations.update(
            {"lamphttpd": os.system("cat /opt/lampp/etc/httpd.conf")}
        )
        self.service_configurations.update(
            {"/etc/": os.system("ls -aRl /etc/ | awk '$1 ~ /^.*r.*/")}
        )

    def get_scheduled_jobs(self):
        """
        get scheduled jobs
        """
        self.logger.normal_output("Running scheduled jobs")
        self.scheduled_jobs.update({"crontab -l": os.system("crontab -l")})
        self.scheduled_jobs.update({"ls alh cron": os.system("ls -alh /var/spool/cron")})
        self.scheduled_jobs.update({"/etc cron": os.system("ls -al /etc/ | grep cron")})
        self.scheduled_jobs.update({"ls -al /etc/cron*": os.system("ls -al /etc/cron*")})
        self.scheduled_jobs.update({"etc/cron": os.system("cat /etc/cron*")})
        self.scheduled_jobs.update({"etc/at.allow": os.system("cat /etc/at.allow")})
        self.scheduled_jobs.update({"etc/at.deny": os.system("cat /etc/at.deny")})
        self.scheduled_jobs.update({"etc/cron.allow": os.system("cat /etc/cron.allow")})
        self.scheduled_jobs.update({"etc/cron.deny": os.system("cat /etc/cron.deny")})
        self.scheduled_jobs.update({"crontab": os.system("cat /etc/crontab")})
        self.scheduled_jobs.update({"acrontab": os.system("cat /etc/anacrontab")})
        self.scheduled_jobs.update({"rootcrontab": os.system("cat /var/spool/cron/crontabs/root")})

    def get_for_plaintext_passwords(self):
        """
        check for different config files containing passwords
        """
        self.logger.normal_output("Running plaintext passwords and users")
        self.plaintext_passwords.update({"grep for user": os.system("grep -i user /*")})
        self.plaintext_passwords.update({"grep for pass": os.system("grep -i pass /*")})
        self.plaintext_passwords.update({"grep -c 5": os.system("grep -C 5 \"password\" /*")})
        self.plaintext_passwords.update({
            "find php $password":
            os.system(
                "find . -name \"*.php\" -print0 | xargs -0 grep -i -n \"var $password\""   # Joomla
            )
        })
