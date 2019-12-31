import logging
try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

dgl_mode = True

bind_nonsecure = True # Set to false to only use SSL
bind_address = "127.0.0.1"
bind_port = 8000

bind_pairs = (
    ("127.0.0.1", 8000),
)

logging_config = {
    "filename": "%%CHROOT_WEBDIR%%/run/webtiles.log",
    "level": logging.INFO,
    "format": "%(asctime)s %(levelname)s: %(message)s"
}

password_db = "%%CHROOT_LOGIN_DB%%"

static_path = "%%CHROOT_WEBDIR%%/static"
template_path = "%%CHROOT_WEBDIR%%/templates/"

# Path for server-side unix sockets (to be used to communicate with crawl)
server_socket_path = None # Uses global temp dir

# Server name, so far only used in the ttyrec metadata
server_id = "cko"

# Disable caching of game data files
game_data_no_cache = False

# Watch socket dirs for games not started by the server
watch_socket_dirs = True

# Game configs
# %n in paths is replaced by the current username
games = OrderedDict([

    ("dcss-0.24", dict(
        name = "Play 0.24",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        separator = "<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span>latest version:</span>&nbsp;",
        send_json_options = True,
        pre_options  = [ "0.24" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-0.24/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-0.24/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "%%WEB_MORGUE_URL%%/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%/crawl-24/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets")),
    ("spr-0.24", dict(
        name = "Sprint",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        pre_options  = [ "0.24" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-0.24/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-0.24/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "%%WEB_MORGUE_URL%%/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%/crawl-24-sprint/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets",
        options = ["-sprint"])),
    ("tut-0.24", dict(
        name = "Tutorial",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        pre_options  = [ "0.24" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-0.24/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-0.24/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "%%WEB_MORGUE_URL%%/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%/crawl-24-tut/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets",
        options = ["-tutorial"])),

    ("dcss-git", dict(
        name = "Play trunk",
        crawl_binary = "/bin/crawl-git-launcher.sh",
        separator = "<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span>unstable:</span>&nbsp;",
        send_json_options = True,
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-git/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-git/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "%%WEB_MORGUE_URL%%/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%/crawl-git/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets")),
    ("spr-git", dict(
        name = "Sprint",
        crawl_binary = "/bin/crawl-git-launcher.sh",
        send_json_options = True,
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-git/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-git/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "%%WEB_MORGUE_URL%%/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%/crawl-git-sprint/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets",
        options = ["-sprint"])),

    ("dcss-0.23", dict(
        name = "Play 0.23",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        separator = "<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<details style='display:inline-block;'><summary style='cursor:pointer; -webkit-user-select:none; -moz-user-select:none; -ms-user-select:none; user-select:none;'>Click to see older versions</summary>",
        send_json_options = True,
        pre_options  = [ "0.23" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-0.23/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-0.23/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "%%WEB_MORGUE_URL%%/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%/crawl-23/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets")),
    ("spr-0.23", dict(
        name = "Sprint",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        pre_options  = [ "0.23" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-0.23/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-0.23/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "%%WEB_MORGUE_URL%%/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%/crawl-23-sprint/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets",
        options = ["-sprint"])),
    ("dcss-0.22", dict(
        name = "Play 0.22",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        separator = "<br>",
        send_json_options = True,
        pre_options  = [ "0.22" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-0.22/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-0.22/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "%%WEB_MORGUE_URL%%/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%/crawl-22/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets")),
    ("spr-0.22", dict(
        name = "Sprint",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        pre_options  = [ "0.22" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-0.22/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-0.22/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "%%WEB_MORGUE_URL%%/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%/crawl-22-sprint/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets",
        options = ["-sprint"])),
    ("dcss-0.21", dict(
        name = "Play 0.21",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        separator = "<br>",
        send_json_options = True,
        pre_options  = [ "0.21" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-0.21/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-0.21/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "%%WEB_MORGUE_URL%%/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%/crawl-21/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets")),
    ("spr-0.21", dict(
        name = "Sprint",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        pre_options  = [ "0.21" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-0.21/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-0.21/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "%%WEB_MORGUE_URL%%/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%/crawl-21-sprint/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets",
        options = ["-sprint"])),
    ("dcss-0.18", dict(
        name = "Play 0.18",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        separator = "<br>",
        send_json_options = True,
        pre_options  = [ "0.18" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-0.18/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-0.18/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "%%WEB_MORGUE_URL%%/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%/crawl-18/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets")),
    ("spr-0.18", dict(
        name = "Sprint",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        pre_options  = [ "0.18" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-0.18/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-0.18/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "%%WEB_MORGUE_URL%%/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%/crawl-18-sprint/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets",
        options = ["-sprint"])),

    ("dcss-hellcrawl", dict(
        name = "hellcrawl",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        separator = "</details><br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span>forks:</span>&nbsp;",
        send_json_options = True,
        pre_options  = [ "hellcrawl" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-hellcrawl/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-hellcrawl/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "%%WEB_MORGUE_URL%%/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%/crawl-hellcrawl/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets")),
    ("dcss-bcrawl", dict(
        name = "bcrawl",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        separator = "|",
        send_json_options = True,
        pre_options  = [ "bcrawl" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-bcrawl/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-bcrawl/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "%%WEB_MORGUE_URL%%/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%/crawl-bcrawl/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets")),
    ("dcss-bcrawl-adv", dict(
        name = "(Adventure)",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        separator = "",
        send_json_options = True,
        pre_options  = [ "bcrawl" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-bcrawl/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-bcrawl/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "%%WEB_MORGUE_URL%%/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%/crawl-bcrawl-adv/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets",
        options = ["-adventure"])),
    ("dcss-bcadrencrawl", dict(
        name = "BcadrenCrawl",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        separator = "|",
        send_json_options = True,
        pre_options  = [ "bcadrencrawl" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-bcadrencrawl/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-bcadrencrawl/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "%%WEB_MORGUE_URL%%/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%/crawl-bcadrencrawl/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets")),
    ("dcss-gooncrawl", dict(
        name = "Gooncrawl",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        separator = "<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;",
        send_json_options = True,
        pre_options  = [ "gooncrawl" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-gooncrawl/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-gooncrawl/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "%%WEB_MORGUE_URL%%/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%/crawl-gooncrawl/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets")),
    ("dcss-stoatsoup", dict(
        name = "StoatSoup",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        separator = "|",
        send_json_options = True,
        pre_options  = [ "stoatsoup" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-stoatsoup/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-stoatsoup/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "%%WEB_MORGUE_URL%%/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%/crawl-stoatsoup/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets")),
    ("dcss-bloatcrawl2", dict(
        name = "bloatcrawl2",
        crawl_binary = "/bin/crawl-stable-launcher.sh",
        separator = "|",
        send_json_options = True,
        pre_options  = [ "bloatcrawl2" ],
        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-bloatcrawl2/",
        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-bloatcrawl2/",
        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
        morgue_url = "%%WEB_MORGUE_URL%%/%n/",
        inprogress_path = "%%CHROOT_INPROGRESSDIR%%/crawl-bloatcrawl2/",
        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
        socket_path = "%%CHROOT_WEBDIR%%/sockets")),
#    ("dcss-positional-magic", dict(
#        name = "positional-magic",
#        crawl_binary = "/bin/crawl-stable-launcher.sh",
#        separator = "<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span>experimental:</span>&nbsp;",
#        send_json_options = True,
#        pre_options  = [ "positional-magic" ],
#        rcfile_path = "%%CHROOT_RCFILESDIR%%/crawl-git/",
#        macro_path = "%%CHROOT_RCFILESDIR%%/crawl-git/",
#        morgue_path = "%%CHROOT_MORGUEDIR%%/%n/",
#        morgue_url = "%%WEB_MORGUE_URL%%/%n/",
#        inprogress_path = "%%CHROOT_INPROGRESSDIR%%/crawl-positional-magic/",
#        ttyrec_path = "%%CHROOT_TTYRECDIR%%/%n/",
#        socket_path = "%%CHROOT_WEBDIR%%/sockets")),
])

dgl_status_file = "%%CHROOT_WEBDIR%%/run/status"

# Set to None not to read milestones
milestone_file = [
    "%%CHROOT_CRAWL_GAMEDIR%%/saves/milestones",
    "%%CHROOT_CRAWL_GAMEDIR%%/saves/milestones-tutorial",
    "%%CHROOT_CRAWL_GAMEDIR%%/saves/milestones-sprint",
    "%%CHROOT_CRAWL_BASEDIR%%/crawl-0.24/saves/milestones",
    "%%CHROOT_CRAWL_BASEDIR%%/crawl-0.24/saves/milestones-tutorial",
    "%%CHROOT_CRAWL_BASEDIR%%/crawl-0.24/saves/milestones-sprint",
    "%%CHROOT_CRAWL_BASEDIR%%/crawl-0.23/saves/milestones",
    "%%CHROOT_CRAWL_BASEDIR%%/crawl-0.23/saves/milestones-tutorial",
    "%%CHROOT_CRAWL_BASEDIR%%/crawl-0.23/saves/milestones-sprint",
    "%%CHROOT_CRAWL_BASEDIR%%/crawl-0.22/saves/milestones",
    "%%CHROOT_CRAWL_BASEDIR%%/crawl-0.22/saves/milestones-tutorial",
    "%%CHROOT_CRAWL_BASEDIR%%/crawl-0.22/saves/milestones-sprint",
    "%%CHROOT_CRAWL_BASEDIR%%/crawl-0.21/saves/milestones",
    "%%CHROOT_CRAWL_BASEDIR%%/crawl-0.21/saves/milestones-sprint"
    "%%CHROOT_CRAWL_BASEDIR%%/crawl-0.18/saves/milestones",
    "%%CHROOT_CRAWL_BASEDIR%%/crawl-0.18/saves/milestones-sprint"
]

status_file_update_rate = 5

recording_term_size = (80, 24)

max_connections = 500

# Script to initialize a user, e.g. make sure the paths
# and the rc file exist. This is not done by the server
# at the moment.
init_player_program = "/bin/init-webtiles.sh"

ssl_options = None # No SSL
#ssl_options = {
#    "certfile": "/ckeys/kelbi.org/cert.crt",
#    "keyfile": "/ckeys/kelbi.org/privkey.key",
#    "ca_certs": "/ckeys/kelbi.org/chain.pem"
#keep commented out    "ca_certs": "/ckeys/kelbi.org/fullchain.pem"
#}
ssl_address = "104.131.30.97"
ssl_port = 8081

ssl_bind_pairs = (
    ("104.131.30.97", 8081),
)

connection_timeout = 600
max_idle_time = 5 * 60 * 60

use_gzip = False

# Seconds until stale HTTP connections are closed
# This needs a patch currently not in mainline tornado.
http_connection_timeout = None
http_xheaders = True

kill_timeout = 10 # Seconds until crawl is killed after HUP is sent

nick_regex = r"^[a-zA-Z0-9]{2,20}$"
max_passwd_length = 20

allow_password_reset = True # Set to true to allow users to request a password reset email. Some settings must be properly configured for this to work

# Set to the primary URL where a player would reach the main lobby
# For example: "http://crawl.akrasiac.org/"
# This is required for for password reset, as it will be the base URL for
# recovery URLs.
lobby_url = "https://crawl.kelbi.org/"

# Proper SMTP settings are required for password reset to function properly.
# if smtp_host is anything other than `localhost`, you may need to adjust the
# timeout settings (see server.py, calls to ioloop.set_blocking_log_threshold).
# Ideally, test out these settings carefully in a non-production setting
# before enabling this, as there's a bunch of ways for this to go wrong and you
# don't want to get your SMTP server blacklisted.
smtp_host = ""
smtp_port = 465
smtp_use_ssl = True
smtp_user = "" # set to None for no auth
smtp_password = ""
smtp_from_addr = "" # The address from which automated
# emails will be sent

# crypt() algorithm, e.g. "1" for MD5 or "6" for SHA-512; see crypt(3).
# If false, use traditional DES (but then only the first eight characters
# are significant).
crypt_algorithm = "6"
# If crypt_algorithm is true, the length of the salt string to use.  If
# crypt_algorithm is false, a two-character salt is used.
crypt_salt_length = 16

login_token_lifetime = 7 # Days

uid = 1002  # If this is not None, the server will setuid to that (numeric) id
gid = 1002  # after binding its sockets.

umask = None # e.g. 0077

chroot = "%%DGL_CHROOT%%"

pidfile = "%%CHROOT_WEBDIR%%/run/webtiles.pid"
daemon = True # If true, the server will detach from the session after startup

player_url = "http://crawl.akrasiac.org/scoring/players/%s.html"
