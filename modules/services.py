"""
Service enumeration
"""
from modules.logger import Logger
from modules.execute_command import ExecuteCommand

class Services(object):
    """
    Object for service enumeration
    """

    logger = Logger()
    executor = ExecuteCommand()

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
        self.services.update({"ps aux": self.executor.execute_command("ps aux")})
        self.services.update({"ps aux -ef": self.executor.execute_command("ps -ef")})
        # self.services.update({"top": self.executor.execute_command("top")})
        self.services.update({"cat /etc/services": self.executor.execute_command("cat /etc/services")})

    def get_services_as_root(self):
        """
        get root services
        """
        self.logger.normal_output("Running services as root")
        self.services_as_root.update({"ps aux |grep root": self.executor.execute_command("ps aux | grep root")})
        self.services_as_root.update({"ps -ef | grep root": self.executor.execute_command("ps -ef | grep root")})

    def get_installed_applications(self):
        """
        get installed applications
        """
        self.logger.normal_output("Running installed apps")
        self.installed_applications.update({"ls -alh /usr/bin": self.executor.execute_command("ls -alh /usr/bin/")})
        self.installed_applications.update({"ls -alh /sbin/":  self.executor.execute_command("ls -alh /sbin/")})
        self.installed_applications.update({"dpkg -l":  self.executor.execute_command("dpkg -l")})
        self.installed_applications.update({"rpm -qa":  self.executor.execute_command("rpm -qa")})
        self.installed_applications.update(
            {"ls -alh /var/cache/apt/archives0":  self.executor.execute_command("ls -alh /var/cache/apt/archivesO")}
        )
        self.installed_applications.update(
            {"ls -alh /var/cache/yum":  self.executor.execute_command("ls -alh /var/cache/yum/")}
        )

    def get_service_configurations(self):
        """
        get service configurations
        """
        self.logger.normal_output("Running service configs")
        self.service_configurations.update({"syslog": self.executor.execute_command("cat /etc/syslog.conf")})
        self.service_configurations.update({"chhtp": self.executor.execute_command("cat /etc/chttp.conf")})
        self.service_configurations.update({"lighthttpd": self.executor.execute_command("cat /etc/lighttpd.conf")})
        self.service_configurations.update({"cupsd": self.executor.execute_command("cat /etc/cups/cupsd.conf")})
        self.service_configurations.update({"inetd": self.executor.execute_command("cat /etc/inetd.conf")})
        self.service_configurations.update({"apache2": self.executor.execute_command("cat /etc/apache2/apache2.conf")})
        self.service_configurations.update({"my.conf": self.executor.execute_command("cat /etc/my.conf")})
        self.service_configurations.update({"httpd": self.executor.execute_command("cat /etc/httpd/conf/httpd.conf")})
        self.service_configurations.update(
            {"lamphttpd": self.executor.execute_command("cat /opt/lampp/etc/httpd.conf")}
        )
        self.service_configurations.update(
            {"/etc/": self.executor.execute_command("ls -aRl /etc/ | awk '$1 ~ /^.*r.*/")}
        )

    def get_scheduled_jobs(self):
        """
        get scheduled jobs
        """
        self.logger.normal_output("Running scheduled jobs")
        self.scheduled_jobs.update({"crontab -l": self.executor.execute_command("crontab -l")})
        self.scheduled_jobs.update({"ls alh cron": self.executor.execute_command("ls -alh /var/spool/cron")})
        self.scheduled_jobs.update({"/etc cron": self.executor.execute_command("ls -al /etc/ | grep cron")})
        self.scheduled_jobs.update({"ls -al /etc/cron*": self.executor.execute_command("ls -al /etc/cron*")})
        self.scheduled_jobs.update({"etc/cron": self.executor.execute_command("cat /etc/cron*")})
        self.scheduled_jobs.update({"etc/at.allow": self.executor.execute_command("cat /etc/at.allow")})
        self.scheduled_jobs.update({"etc/at.deny": self.executor.execute_command("cat /etc/at.deny")})
        self.scheduled_jobs.update({"etc/cron.allow": self.executor.execute_command("cat /etc/cron.allow")})
        self.scheduled_jobs.update({"etc/cron.deny": self.executor.execute_command("cat /etc/cron.deny")})
        self.scheduled_jobs.update({"crontab": self.executor.execute_command("cat /etc/crontab")})
        self.scheduled_jobs.update({"acrontab": self.executor.execute_command("cat /etc/anacrontab")})
        self.scheduled_jobs.update({"rootcrontab": self.executor.execute_command("cat /var/spool/cron/crontabs/root")})

    def get_for_plaintext_passwords(self):
        """
        check for different config files containing passwords
        """
        self.logger.normal_output("Running plaintext passwords and users")
        self.plaintext_passwords.update({"grep for user": self.executor.execute_command("grep -i user /*")})
        self.plaintext_passwords.update({"grep for pass": self.executor.execute_command("grep -i pass /*")})
        self.plaintext_passwords.update({"grep -c 5": self.executor.execute_command("grep -C 5 \"password\" /*")})
        self.plaintext_passwords.update({
            "find php $password":
            self.executor.execute_command(
                "find . -name \"*.php\" -print0 | xargs -0 grep -i -n \"var $password\""   # Joomla
            )
        })
