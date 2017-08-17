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

    def get_services(self):
        """
        get services
        """
        self.services.update({"ps aux": os.system("ps aux")})
        self.services.update({"ps aux -ef": os.system("ps -ef")})
        self.services.update({"top": os.system("top")})
        self.services.update({"cat /etc/services": os.system("cat /etc/services")})

    def get_services_as_root(self):
        """
        get root services
        """
        self.services_as_root.update({"ps aux |grep root": os.system("ps aux | grep root")})
        self.services_as_root.update({"ps -ef | grep root": os.system("ps -ef | grep root")})

    def get_installed_applications(self):
        """
        get installed applications
        """
        self.installed_applications.update({"ls -alh /usr/bin": os.system("ls -alh /usr/bin/")})
        self.installed_applications.update({"ls -alh /sbin/":  os.system("ls -alh /sbin/")})
        self.installed_applications.update({"dpkg -l":  os.system("dpkg -l")})
        self.installed_applications.update({"rpm -qa":  os.system("rpm -qa")})
        self.installed_applications.update({"ls -alh /var/cache/apt/archives0":  os.system("ls -alh /var/cache/apt/archivesO")})
        self.installed_applications.update({"ls -alh /var/cache/yum":  os.system("ls -alh /var/cache/yum/")})

    def check_service_configurations(self):
        """
        get service configurations
        """
        service_configurations = os.system("cat /etc/syslog.conf")
        service_configurations += os.system("cat /etc/chttp.conf")
        service_configurations += os.system("cat /etc/lighttpd.conf")
        service_configurations += os.system("cat /etc/cups/cupsd.conf")
        service_configurations += os.system("cat /etc/inetd.conf")
        service_configurations += os.system("cat /etc/apache2/apache2.conf")
        service_configurations += os.system("cat /etc/my.conf")
        service_configurations += os.system("cat /etc/httpd/conf/httpd.conf")
        service_configurations += os.system("cat /opt/lampp/etc/httpd.conf")
        service_configurations += os.system("ls -aRl /etc/ | awk '$1 ~ /^.*r.*/")
        return service_configurations

    def get_secheduled_jobs(self):
        """
        get scheduled jobs
        """
        scheduled_jobs = os.system("crontab -l")
        scheduled_jobs = os.system("ls -alh /var/spool/cron")
        scheduled_jobs = os.system("ls -al /etc/ | grep cron")
        scheduled_jobs = os.system("ls -al /etc/cron*")
        scheduled_jobs = os.system("cat /etc/cron*")
        scheduled_jobs = os.system("cat /etc/at.allow")
        scheduled_jobs = os.system("cat /etc/at.deny")
        scheduled_jobs = os.system("cat /etc/cron.allow")
        scheduled_jobs = os.system("cat /etc/cron.deny")
        scheduled_jobs = os.system("cat /etc/crontab")
        scheduled_jobs = os.system("cat /etc/anacrontab")
        scheduled_jobs = os.system("cat /var/spool/cron/crontabs/root")
        return scheduled_jobs

    def check_for_plaintext_passwords(self):
        """
        check for different config files containing passwords
        """
        plaintext_passwords = os.system("grep -i user [filename]")
        plaintext_passwords += os.system("grep -i pass [filename]")
        plaintext_passwords += os.system("grep -C 5 \"password\" [filename]")
        plaintext_passwords += os.system("find . -name \"*.php\" -print0 | xargs -0 grep -i -n \"var $password\"   # Joomla")

        return plaintext_passwords