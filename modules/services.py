"""
Service enumeration
"""
import subprocess

class Services(object):
    """
    Object for service enumeration
    """
    def __init__(self):
        return

    def get_services(self):
        """
        get services
        """

        services = subprocess.call("ps aux")
        services += subprocess.call("ps -ef")
        services += subprocess.call("top")
        services += subprocess.call("cat /etc/services")
        return services

    def services_as_root(self):
        """
        get root services
        """
        services_as_root = subprocess.call("ps aux | grep root")
        services_as_root += subprocess.call("ps -ef | grep root")
        return services_as_root

    def installed_applications(self):
        """
        get installed applications
        """
        installed_applications = subprocess.call("ls -alh /usr/bin/")
        installed_applications += subprocess.call("ls -alh /sbin/")
        installed_applications += subprocess.call("dpkg -l")
        installed_applications += subprocess.call("rpm -qa")
        installed_applications += subprocess.call("ls -alh /var/cache/apt/archivesO")
        installed_applications += subprocess.call("ls -alh /var/cache/yum/")
        return installed_applications

    def check_service_configurations(self):
        """
        get service configurations
        """
        service_configurations = subprocess.call("cat /etc/syslog.conf")
        service_configurations += subprocess.call("cat /etc/chttp.conf")
        service_configurations += subprocess.call("cat /etc/lighttpd.conf")
        service_configurations += subprocess.call("cat /etc/cups/cupsd.conf")
        service_configurations += subprocess.call("cat /etc/inetd.conf")
        service_configurations += subprocess.call("cat /etc/apache2/apache2.conf")
        service_configurations += subprocess.call("cat /etc/my.conf")
        service_configurations += subprocess.call("cat /etc/httpd/conf/httpd.conf")
        service_configurations += subprocess.call("cat /opt/lampp/etc/httpd.conf")
        service_configurations += subprocess.call("ls -aRl /etc/ | awk '$1 ~ /^.*r.*/")
        return service_configurations

    def get_secheduled_jobs(self):
        """
        get scheduled jobs
        """
        scheduled_jobs = subprocess.call("crontab -l")
        scheduled_jobs = subprocess.call("ls -alh /var/spool/cron")
        scheduled_jobs = subprocess.call("ls -al /etc/ | grep cron")
        scheduled_jobs = subprocess.call("ls -al /etc/cron*")
        scheduled_jobs = subprocess.call("cat /etc/cron*")
        scheduled_jobs = subprocess.call("cat /etc/at.allow")
        scheduled_jobs = subprocess.call("cat /etc/at.deny")
        scheduled_jobs = subprocess.call("cat /etc/cron.allow")
        scheduled_jobs = subprocess.call("cat /etc/cron.deny")
        scheduled_jobs = subprocess.call("cat /etc/crontab")
        scheduled_jobs = subprocess.call("cat /etc/anacrontab")
        scheduled_jobs = subprocess.call("cat /var/spool/cron/crontabs/root")
        return scheduled_jobs

    def check_for_plaintext_passwords(self):
        """
        check for different config files containing passwords
        """
        plaintext_passwords = subprocess.call("grep -i user [filename]")
        plaintext_passwords += subprocess.call("grep -i pass [filename]")
        plaintext_passwords += subprocess.call("grep -C 5 \"password\" [filename]")
        plaintext_passwords += subprocess.call("find . -name \"*.php\" -print0 | xargs -0 grep -i -n \"var $password\"   # Joomla")

        return plaintext_passwords