#! /bin/sh

ifnxcp() {
    [ -e "$2" ] || cp "$1" "$2";
}

NAME=$1

ifnxcp %%CHROOT_DGLDIR%%/data/crawl-git-settings/init.txt %%CHROOT_RCFILESDIR%%/crawl-git/"$NAME".rc
ifnxcp %%CHROOT_DGLDIR%%/data/crawl-git.macro %%CHROOT_RCFILESDIR%%/crawl-git/"$NAME".macro
ifnxcp %%CHROOT_DGLDIR%%/data/crawl-0.24-settings/init.txt %%CHROOT_RCFILESDIR%%/crawl-0.24/"$NAME".rc
ifnxcp %%CHROOT_DGLDIR%%/data/crawl-git.macro %%CHROOT_RCFILESDIR%%/crawl-0.24/"$NAME".macro
ifnxcp %%CHROOT_DGLDIR%%/data/crawl-0.23-settings/init.txt %%CHROOT_RCFILESDIR%%/crawl-0.23/"$NAME".rc
ifnxcp %%CHROOT_DGLDIR%%/data/crawl-git.macro %%CHROOT_RCFILESDIR%%/crawl-0.23/"$NAME".macro
ifnxcp %%CHROOT_DGLDIR%%/data/crawl-0.22-settings/init.txt %%CHROOT_RCFILESDIR%%/crawl-0.22/"$NAME".rc
ifnxcp %%CHROOT_DGLDIR%%/data/crawl-git.macro %%CHROOT_RCFILESDIR%%/crawl-0.22/"$NAME".macro
ifnxcp %%CHROOT_DGLDIR%%/data/crawl-0.21-settings/init.txt %%CHROOT_RCFILESDIR%%/crawl-0.21/"$NAME".rc
ifnxcp %%CHROOT_DGLDIR%%/data/crawl-git.macro %%CHROOT_RCFILESDIR%%/crawl-0.21/"$NAME".macro
ifnxcp %%CHROOT_DGLDIR%%/data/crawl-0.18-settings/init.txt %%CHROOT_RCFILESDIR%%/crawl-0.18/"$NAME".rc
ifnxcp %%CHROOT_DGLDIR%%/data/crawl-git.macro %%CHROOT_RCFILESDIR%%/crawl-0.18/"$NAME".macro

ifnxcp %%CHROOT_DGLDIR%%/data/crawl-git-settings/init.txt %%CHROOT_RCFILESDIR%%/crawl-hellcrawl/"$NAME".rc
ifnxcp %%CHROOT_DGLDIR%%/data/crawl-git.macro %%CHROOT_RCFILESDIR%%/crawl-hellcrawl/"$NAME".macro
ifnxcp %%CHROOT_DGLDIR%%/data/crawl-git-settings/init.txt %%CHROOT_RCFILESDIR%%/crawl-bcrawl/"$NAME".rc
ifnxcp %%CHROOT_DGLDIR%%/data/crawl-git.macro %%CHROOT_RCFILESDIR%%/crawl-bcrawl/"$NAME".macro
ifnxcp %%CHROOT_DGLDIR%%/data/crawl-git-settings/init.txt %%CHROOT_RCFILESDIR%%/crawl-bcadrencrawl/"$NAME".rc
ifnxcp %%CHROOT_DGLDIR%%/data/crawl-git.macro %%CHROOT_RCFILESDIR%%/crawl-bcadrencrawl/"$NAME".macro
ifnxcp %%CHROOT_DGLDIR%%/data/crawl-git-settings/init.txt %%CHROOT_RCFILESDIR%%/crawl-gooncrawl/"$NAME".rc
ifnxcp %%CHROOT_DGLDIR%%/data/crawl-git.macro %%CHROOT_RCFILESDIR%%/crawl-gooncrawl/"$NAME".macro
ifnxcp %%CHROOT_DGLDIR%%/data/crawl-git-settings/init.txt %%CHROOT_RCFILESDIR%%/crawl-stoatsoup/"$NAME".rc
ifnxcp %%CHROOT_DGLDIR%%/data/crawl-git.macro %%CHROOT_RCFILESDIR%%/crawl-stoatsoup/"$NAME".macro

mkdir -p %%CHROOT_MORGUEDIR%%/"$NAME"
mkdir -p %%CHROOT_TTYRECDIR%%/"$NAME"
