#!/usr/bin/env bash
# Forwarding pages at addresses the site used to serve — a build-instance-site
# source step (`bun run site:redirects <site dir>`).
#
# Rendered pages live under /<locale>/ (folio-assistant#2527). Links already
# shared to the old addresses forward to the new ones, keeping the query and
# the #fragment, so the change-set issues' links such as /dpi-h-ra/#sec:c and
# /public-comments/#PC-0036 still land on the paragraph or comment.
#
# - /review/: moved to /en/review/ by the first agent-run root publish
#   (2026-10-11, bean n3h9).
# - /dpi-h-ra/: the document, now /en/dpi-h-ra/. The old directory still holds
#   the document's data (graph.jsonld, kg/, blocks/), which keep their IRIs;
#   only its index page is a forwarder.
# - /public-comments/: the comment dashboard, now
#   /en/folio-assistant-core/public-comments/folio/dpi-h-ra/.
# - /mapper/ and /mapper/SMART-RA-Mapper.html: the RA mapper, now under
#   /en/mapper/ (tools/ra-mapper/build-site.sh).
# - /draft/: a short address for the review version's line-numbered PDF in the
#   site's PDF viewer. /draft/#page=80 opens PDF page 80. The public-comment
#   sheet links every section, page and line mention to it, and a short link
#   keeps those rich-text cells small. It opens the display copy,
#   review/public-comment/draft/*.page-labels.pdf (kept out of the library
#   entry, whose contents check:l1-complete fixes): the frozen PDF's exact bytes plus an appended update
#   that labels the pages as printed (Cover, i-x, then 1-243), so the
#   viewer's page box reads "108 (119 of 254)". #page= still counts PDF pages.
#   The frozen PDF itself is never edited.
set -euo pipefail
OUT=$(cd "${1:?usage: site-redirects.sh <site dir>}" && pwd)

redirect() { # <old dir> <new target, relative to the old dir> [<file name>, default index.html]
  mkdir -p "$OUT/$1"
  cat > "$OUT/$1/${3:-index.html}" <<HTML
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Moved</title>
<meta name="robots" content="noindex">
<link rel="canonical" href="$2">
<script>location.replace("$2" + location.search + location.hash);</script>
<meta http-equiv="refresh" content="0; url=$2">
</head>
<body><p>This page has moved to <a href="$2">$2</a>.</p></body>
</html>
HTML
}

redirect review ../en/review/
redirect dpi-h-ra ../en/dpi-h-ra/
redirect public-comments ../en/folio-assistant-core/public-comments/folio/dpi-h-ra/
redirect mapper ../en/mapper/
redirect mapper ../en/mapper/SMART-RA-Mapper.html SMART-RA-Mapper.html
redirect draft '../assets/vendor/pdfjs/web/viewer.html?src=https%3A%2F%2Fraw.githubusercontent.com%2Flitlfred%2Fsmart-ra%2Fmain%2Freview%2Fpublic-comment%2Fdraft%2Fwho-dpi-h-reference-architecture-draft-v1.page-labels.pdf'
