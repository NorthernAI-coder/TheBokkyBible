#!/bin/sh

# <link href="https://cdn.jsdelivr.net/npm/vuetify@3.7.2/dist/vuetify.min.css" rel="stylesheet">
# Get vuetify[.min].css 3.9.5
SOURCE=https://cdn.jsdelivr.net/npm/vuetify@3.9.5/dist/vuetify.css
DEST=../docs/css/vuetify_3.9.5.css
wget $SOURCE -O $DEST
SOURCE=https://cdn.jsdelivr.net/npm/vuetify@3.9.5/dist/vuetify.min.css
DEST=../docs/css/vuetify_3.9.5.min.css
wget $SOURCE -O $DEST

# <script src="https://unpkg.com/vue@3/dist/vue.global.prod.js"></script>
# Get vue[.prod].js 3.5.29
SOURCE=https://cdn.jsdelivr.net/npm/vue@3.5.29/dist/vue.global.js
DEST=../docs/js/vue_3.5.29.js
wget $SOURCE -O $DEST
SOURCE=https://cdn.jsdelivr.net/npm/vue@3.5.29/dist/vue.global.prod.js
DEST=../docs/js/vue_3.5.29.prod.js
wget $SOURCE -O $DEST

# <script src="https://cdn.jsdelivr.net/npm/vuetify@3.7.2/dist/vuetify.min.js"></script>
# Get vuetify[.min].js 3.9.5
SOURCE=https://cdn.jsdelivr.net/npm/vuetify@3.9.5/dist/vuetify.js
DEST=../docs/js/vuetify_3.9.5.js
wget $SOURCE -O $DEST
SOURCE=https://cdn.jsdelivr.net/npm/vuetify@3.9.5/dist/vuetify.min.js
DEST=../docs/js/vuetify_3.9.5.min.js
wget $SOURCE -O $DEST

# <script src="https://unpkg.com/dexie@4/dist/dexie.js"></script>
# Get dexie[.min].js 4.3.0
SOURCE=https://cdn.jsdelivr.net/npm/dexie@4.3.0/dist/dexie.js
DEST=../docs/js/dexie_4.3.0.js
wget $SOURCE -O $DEST
SOURCE=https://cdn.jsdelivr.net/npm/dexie@4.3.0/dist/dexie.min.js
DEST=../docs/js/dexie_4.3.0.min.js
wget $SOURCE -O $DEST

# Get marked[.min].js 18.0.0
SOURCE=https://cdn.jsdelivr.net/npm/marked@18.0.0/lib/marked.umd.js
DEST=../docs/js/marked_18.0.0.umd.js
wget $SOURCE -O $DEST
SOURCE=https://cdn.jsdelivr.net/npm/marked@18.0.0/lib/marked.umd.min.js
DEST=../docs/js/marked_18.0.0.umd.min.js
wget $SOURCE -O $DEST

# Get marked-gfm-heading-id[.min].js 4.1.4
SOURCE=https://cdn.jsdelivr.net/npm/marked-gfm-heading-id@4.1.4/lib/index.umd.js
DEST=../docs/js/marked-gfm-heading-id_4.1.4.umd.js
wget $SOURCE -O $DEST
SOURCE=https://cdn.jsdelivr.net/npm/marked-gfm-heading-id@4.1.4/lib/index.umd.min.js
DEST=../docs/js/marked-gfm-heading-id_4.1.4.umd.min.js
wget $SOURCE -O $DEST

# <link href="https://cdn.jsdelivr.net/npm/@mdi/font@latest/css/materialdesignicons.min.css" rel="stylesheet">
# Get materialdesignicons[.min].css 7.4.47
SOURCE=https://cdnjs.cloudflare.com/ajax/libs/MaterialDesign-Webfont/7.4.47/css/materialdesignicons.css
DEST=../docs/css/materialdesignicons_7.4.47.css
wget $SOURCE -O $DEST
SOURCE=https://cdnjs.cloudflare.com/ajax/libs/MaterialDesign-Webfont/7.4.47/css/materialdesignicons.min.css
DEST=../docs/css/materialdesignicons_7.4.47.min.css
wget $SOURCE -O $DEST

# Get materialdesignicons-webfont.woff2 7.4.47
SOURCE=https://cdnjs.cloudflare.com/ajax/libs/MaterialDesign-Webfont/7.4.47/fonts/materialdesignicons-webfont.woff2
DEST=../docs/fonts/materialdesignicons-webfont.woff2
wget $SOURCE -O $DEST

# Get moment[.min].js 2.24.0
SOURCE=https://cdn.jsdelivr.net/npm/moment@2.24.0/moment.js
DEST=../docs/js/moment_2.24.0.js
wget $SOURCE -O $DEST
SOURCE=https://cdn.jsdelivr.net/npm/moment@2.24.0/min/moment.min.js
DEST=../docs/js/moment_2.24.0.min.js
wget $SOURCE -O $DEST

# Get minisearch[.min].js 7.2.0
SOURCE=https://cdn.jsdelivr.net/npm/minisearch@7.2.0/dist/umd/index.js
DEST=../docs/js/minisearch_7.2.0.js
wget $SOURCE -O $DEST
SOURCE=https://cdn.jsdelivr.net/npm/minisearch@7.2.0/dist/umd/index.min.js
DEST=../docs/js/minisearch_7.2.0.min.js
wget $SOURCE -O $DEST

# <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.11.1/build/styles/default.css">
# <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.11.1/build/styles/default.min.css">
# Get highlight[.min].css 11.11.1
SOURCE=https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.11.1/build/styles/default.css
DEST=../docs/css/highlight_11.11.1.css
wget $SOURCE -O $DEST
SOURCE=https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.11.1/build/styles/default.min.css
DEST=../docs/css/highlight_11.11.1.min.css
wget $SOURCE -O $DEST

# <script src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.11.1/build/highlight.js"></script>
# <script src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.11.1/build/highlight.min.js"></script>
# Get highlight[.min].js 11.11.1
SOURCE=https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.11.1/build/highlight.js
DEST=../docs/js/highlight_11.11.1.js
wget $SOURCE -O $DEST
SOURCE=https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.11.1/build/highlight.min.js
DEST=../docs/js/highlight_11.11.1.min.js
wget $SOURCE -O $DEST

# https://raw.githubusercontent.com/highlightjs/highlight.js/3e628edbe34d2ffb9166ff365f614f56621597be/src/styles/github.css
# highlight.js github.css
SOURCE=https://raw.githubusercontent.com/highlightjs/highlight.js/3e628edbe34d2ffb9166ff365f614f56621597be/src/styles/github.css
DEST=../docs/css/github.css
wget $SOURCE -O $DEST


######## UNUSED ########

#
# # Get vuex[.min].js 4.1.0
# SOURCE=https://cdn.jsdelivr.net/npm/vuex@4.1.0/dist/vuex.global.js
# DEST=../docs/js/vuex_4.1.0.js
# wget $SOURCE -O $DEST
# SOURCE=https://cdn.jsdelivr.net/npm/vuex@4.1.0/dist/vuex.global.min.js
# DEST=../docs/js/vuex_4.1.0.min.js
# wget $SOURCE -O $DEST
#
# # Get vue-router[.min].js 4.5.0
# SOURCE=https://cdn.jsdelivr.net/npm/vue-router@4.5.0/dist/vue-router.global.js
# DEST=../docs/js/vue-router_4.5.0.js
# wget $SOURCE -O $DEST
# SOURCE=https://cdn.jsdelivr.net/npm/vue-router@4.5.0/dist/vue-router.global.min.js
# DEST=../docs/js/vuex_4.5.0.min.js
# wget $SOURCE -O $DEST
#
# # Get ethers[.min].js 5.8.0
# SOURCE=https://cdnjs.cloudflare.com/ajax/libs/ethers/5.8.0/ethers.umd.js
# DEST=../docs/js/ethers_5.8.0.umd.js
# wget $SOURCE -O $DEST
# SOURCE=https://cdnjs.cloudflare.com/ajax/libs/ethers/5.8.0/ethers.umd.min.js
# DEST=../docs/js/ethers_5.8.0.umd.min.js
# wget $SOURCE -O $DEST
#
# # Get prism[.min].css 1.24.1
# SOURCE=https://cdnjs.cloudflare.com/ajax/libs/prism/1.24.1/themes/prism.css
# DEST=../docs/css/prism_1.24.1.css
# wget $SOURCE -O $DEST
# SOURCE=https://cdnjs.cloudflare.com/ajax/libs/prism/1.24.1/themes/prism.min.css
# DEST=../docs/css/prism_1.24.1.min.css
# wget $SOURCE -O $DEST
#
# # Get prism[.min].js 1.24.1
# SOURCE=https://cdnjs.cloudflare.com/ajax/libs/prism/1.24.1/prism.js
# DEST=../docs/js/prism_1.24.1.js
# wget $SOURCE -O $DEST
# SOURCE=https://cdnjs.cloudflare.com/ajax/libs/prism/1.24.1/prism.min.js
# DEST=../docs/js/prism_1.24.1.min.js
# wget $SOURCE -O $DEST
#
# # Get prism-solidity[.min].js 1.24.1
# SOURCE=https://cdnjs.cloudflare.com/ajax/libs/prism/1.24.1/components/prism-solidity.js
# DEST=../docs/js/prism-solidity_1.24.1.js
# wget $SOURCE -O $DEST
# SOURCE=https://cdnjs.cloudflare.com/ajax/libs/prism/1.24.1/components/prism-solidity.min.js
# DEST=../docs/js/prism-solidity_1.24.1.min.js
# wget $SOURCE -O $DEST
#
# # Get apexcharts[.min].js 4.5.0
# SOURCE=https://cdn.jsdelivr.net/npm/apexcharts@4.5.0/dist/apexcharts.js
# DEST=../docs/js/apexcharts_4.5.0.js
# wget $SOURCE -O $DEST
# SOURCE=https://cdn.jsdelivr.net/npm/apexcharts@4.5.0/dist/apexcharts.min.js
# DEST=../docs/js/apexcharts_4.5.0.min.js
# wget $SOURCE -O $DEST
#
# # Get vue3-apexcharts@1.8.0
# SOURCE=https://cdn.jsdelivr.net/npm/vue3-apexcharts@1.8.0/dist/vue3-apexcharts.umd.cjs
# DEST=../docs/js/vue3-apexcharts_1.8.0.js
# wget $SOURCE -O $DEST
