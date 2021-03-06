CVESCAN_DESCRIPTION = "Scan an Ubuntu system for known vulnerabilities."

CVE_HELP = "Report if this system is vulnerable to a specific CVE."

PRIORITY_HELP = (
    "'critical' = show only critical CVEs.\n'high'     = show "
    "critical and high CVEs (default)\n'medium'   = show critical and "
    "high and medium CVEs\n'all'      = show all CVES (no filtering "
    "based on priority)"
)

SILENT_HELP = (
    "Enable script/Silent mode: To be used with "
    "'-c <cve-identifier>'.\nDo not print text output; exit 0 if not "
    "vulnerable, exit 1 if vulnerable."
)

MANIFEST_HELP = (
    "Enable manifest mode. Do not scan the localhost. Instead, run a scan against the\n"
    "specified package manifest file.\n"
    "Note: Package manifest files can be generated by running \n"
    "      `dpkg-query -W > manifest.txt` on the host you wish to scan."
)

FILE_HELP = (
    "Used with '-m' option to override the default behavior. Specify\n "
    "a manifest file to scan instead of downloading an OCI manifest.\n "
    "The file needs to be readable under snap confinement.\n User's home "
    "will likely work, /tmp will likely not work."
)

DB_FILE_HELP = (
    "Specify an Ubuntu vulnerability datbase file to use instead of downloading the \n"
    "latest from people.canonical.com."
)

NAGIOS_HELP = (
    "Enable Nagios mode for use with NRPE.\nTypical nagios-style "
    '"OK|WARNING|CRITICAL|UNKNOWN" messages\n and exit codes of 0, 1, '
    "2, or 3.\n0/OK = not vulnerable to any known and patchable CVEs of "
    "the\n specified priority or higher.\n1/WARNING = vulnerable to at "
    "least one known CVE of the specified\n priority or higher for which "
    "there is no available update.\n2/CRITICAL = vulnerable to at least "
    "one known and patchable CVE of\n the specified priority or higher.\n"
    "3/UNKNOWN = something went wrong with the script, or oscap."
)

UCT_LINKS_HELP = "Provide links to the Ubuntu CVE Tracker for each CVE."

UNRESOLVED_HELP = "Show CVEs that have not yet been resolved."

VERBOSE_HELP = "Enable verbose messages."

VERSION_HELP = "Show CVEScan's version number and exit."

EXPERIMENTAL_HELP = (
    'Enable eXperimental mode. Use experimental (also called "alpha") data \n'
    "from the Ubuntu CVE tracker. The alpha UCT files include information about\n"
    "package updates available for users of Ubuntu Advantage running systems \n"
    "with ESM Apps and ESM Infra enabled."
)

JSON_HELP = "Format output as JSON."

CSV_HELP = "Format output as CSV."

DEBUG_LOG = "debug.log"
LSB_RELEASE_FILE = "/etc/lsb-release"
UA_STATUS_FILE = "/var/lib/ubuntu-advantage/status.json"
SNAPD_HOSTFS = "/var/lib/snapd/hostfs"

UBUNTU_ARCHIVE = "Ubuntu Archive"
UA_APPS = "ESM Apps"
UA_INFRA = "ESM Infra"

UA_INFRA_URL = "https://ubuntu.com/advantage"

REPOSITORY_ENABLED_COLOR_CODE = 2
REPOSITORY_DISABLED_COLOR_CODE = 1
REPOSITORY_UNKNOWN_COLOR_CODE = 3


SUCCESS_RETURN_CODE = 0
ERROR_RETURN_CODE = 1
CLI_ERROR_RETURN_CODE = 2
SYSTEM_VULNERABLE_RETURN_CODE = 3
PATCH_AVAILABLE_RETURN_CODE = 4

# Nagios return codes defined here:
# https://assets.nagios.com/downloads/nagioscore/docs/nagioscore/3/en/pluginapi.html
NAGIOS_OK_RETURN_CODE = 0
NAGIOS_WARNING_RETURN_CODE = 1
NAGIOS_CRITICAL_RETURN_CODE = 2
NAGIOS_UNKNOWN_RETURN_CODE = 3

UNTRIAGED = "untriaged"
ALL = "all"
NEGLIGIBLE = "negligible"
LOW = "low"
MEDIUM = "medium"
HIGH = "high"
CRITICAL = "critical"

PRIORITIES = [NEGLIGIBLE, LOW, MEDIUM, HIGH, CRITICAL]

UCT_URL = "https://people.canonical.com/~ubuntu-security/cve/%s"
UCT_DATA_URL = (
    "https://people.canonical.com/~ubuntu-security/cvescan/ubuntu-vuln-db-%s.json.bz2"
)
