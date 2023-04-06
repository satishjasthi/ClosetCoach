""" Constants used for the test cases.
"""

from tests import PROJECT_ROOT


PROJECT_ROOT = str(PROJECT_ROOT)


TEST_PRODUCT_URLS = {
    "men-tshirts": {
        "html_file_path": PROJECT_ROOT
        + "/tests/test_data/page_url_html/men_tshirts_page_1.html",
        "page_url": "https://www.myntra.com/men-tshirts?p=1",
        "urls": [
            "https://www.myntra.com/tshirts/minions-by-kook-n-keech/minions-by-kook-n-keech-men-purple-boxy-fit-printed-round-neck-pure-cotton-t-shirt/8923841/buy",
            "https://www.myntra.com/tshirts/huetrap/huetrap-men-beige--black-typography-printed-sustainable-t-shirt/11148764/buy",
            "https://www.myntra.com/tshirts/powerlook/powerlook-men-multicoloured-dyed-v-neck-raw-edge-t-shirt/22011764/buy",
            "https://www.myntra.com/tshirts/roadster/roadster-men-black-cotton-pure-cotton-t-shirt/1996777/buy",
            "https://www.myntra.com/tshirts/hrx-by-hrithik-roshan/hrx-by-hrithik-roshan-men-teal-blue-printed-pure-cotton-t-shirt/1700871/buy",
            "https://www.myntra.com/tshirts/hrx-by-hrithik-roshan/hrx-by-hrithik-roshan-men-yellow-printed-cotton-pure-cotton-t-shirt/1700944/buy",
            "https://www.myntra.com/tshirts/difference-of-opinion/difference-of-opinion-men-mint-green-round-neck-drop-shoulder-sleeves-cotton-loose-t-shirt/16407468/buy",
            "https://www.myntra.com/tshirts/roadster/roadster-men-white--pure-cotton-t-shirt/2275365/buy",
            "https://www.myntra.com/tshirts/roadster/roadster-men-grey-melange-longline-t-shirt-with-raw-edges/1824340/buy",
            "https://www.myntra.com/tshirts/louis-philippe-sport/louis-philippe-sport-solid-knitted-polo-collar-t-shirt/21474618/buy",
            "https://www.myntra.com/tshirts/hrx-by-hrithik-roshan/hrx-by-hrithik-roshan-men-fluorescent-green-running-t-shirt-with-raglan-sleeves/7231694/buy",
            "https://www.myntra.com/tshirts/louis-philippe/louis-philippe-men-navy-blue-polo-collar-t-shirt/14047672/buy",
            "https://www.myntra.com/tshirts/roadster/roadster-men-brown-melange-henley-neck-t-shirt/1996770/buy",
            "https://www.myntra.com/tshirts/allen-solly/allen-solly-men-blue-solid-polo-collar-pure-cotton-t-shirt/10766822/buy",
            "https://www.myntra.com/tshirts/indian-terrain/indian-terrain-geometric-printed-polo-collar-pure-cotton-t-shirt/16130416/buy",
            "https://www.myntra.com/tshirts/roadster/roadster-men-green--white-colourblocked-round-neck-pure-cotton-t-shirt/13622286/buy",
            "https://www.myntra.com/tshirts/hrx-by-hrithik-roshan/hrx-by-hrithik-roshan-men-navy-advanced-rapid-dry-t-shirt/2314400/buy",
            "https://www.myntra.com/tshirts/hrx-by-hrithik-roshan/hrx-by-hrithik-roshan-ultralyte-men-black-running-t-shirt/10106341/buy",
            "https://www.myntra.com/tshirts/urbano-fashion/urbano-fashion-men-teal-green-slim-fit-tropical-printed-pure-cotton-t-shirt/12377258/buy",
            "https://www.myntra.com/tshirts/tommy-hilfiger/tommy-hilfiger-men-typography-printed-regular-fit-t-shirt/22306978/buy",
            "https://www.myntra.com/tshirts/hrx-by-hrithik-roshan/hrx-by-hrithik-roshan-men-charcoal-grey-slim-advanced-rapid-dry-raglan-t-shirt/2314372/buy",
            "https://www.myntra.com/tshirts/hrx-by-hrithik-roshan/hrx-by-hrithik-roshan-men-black-rapid-dry-running-t-shirt/10565566/buy",
            "https://www.myntra.com/tshirts/roadster/roadster-men-black-printed-cotton-pure-cotton-t-shirt/8938905/buy",
            "https://www.myntra.com/tshirts/levis/levis-men-pure-cotton-solid-polo-collar-t-shirt-with-applique-detail-/20516638/buy",
            "https://www.myntra.com/tshirts/louis-philippe-sport/louis-philippe-sport-men-solid-polo-collar-t-shirt/21474636/buy",
            "https://www.myntra.com/tshirts/technosport/technosport-colourblocked-high-neck-antimicrobial-t-shirt/22124132/buy",
            "https://www.myntra.com/tshirts/hrx-by-hrithik-roshan/hrx-by-hrithik-roshan-men-off-white-printed-t-shirt/1700946/buy",
            "https://www.myntra.com/tshirts/hm/hm-men-3-pack-regular-fit-pure-cotton-round-neck-t-shirts/22283810/buy",
            "https://www.myntra.com/tshirts/herenow/herenow-men-black--grey-striped-cotton-pure-cotton-t-shirt/9376057/buy",
            "https://www.myntra.com/tshirts/levis/levis-men-pure-cotton-polo-collar-t-shirt/20516498/buy",
            "https://www.myntra.com/tshirts/dillinger/dillinger-men-solid-oversized-t-shirt/20355854/buy",
            "https://www.myntra.com/tshirts/powerlook/powerlook-men-typography-printed-t-shirt/21800810/buy",
            "https://www.myntra.com/tshirts/levis/levis-men-blue-abstract-printed-pure-cotton-t-shirt/18984194/buy",
            "https://www.myntra.com/lounge-tshirts/hm/hm-men-black-sustainable-t-shirt-relaxed-fit/11655366/buy",
            "https://www.myntra.com/tshirts/roadster/roadster-men-beige-colourblocked-raw-edge-t-shirt/2215210/buy",
            "https://www.myntra.com/tshirts/louis-philippe/louis-philippe-men-black-polo-collar-t-shirt/14047664/buy",
            "https://www.myntra.com/tshirts/allen-solly-sport/allen-solly-sport-men-charcoal-grey-solid-polo-collar-t-shirt/13483812/buy",
            "https://www.myntra.com/tshirts/hrx-by-hrithik-roshan/hrx-by-hrithik-roshan-men-white-raglan-sleeved-t-shirt/6555071/buy",
            "https://www.myntra.com/tshirts/roadster/roadster-men-green--white-printed-round-neck-pure-cotton-t-shirt/11545192/buy",
            "https://www.myntra.com/tshirts/powerlook/powerlook-men-geometric-printed-t-shirt/21800806/buy",
            "https://www.myntra.com/tshirts/hrx-by-hrithik-roshan/hrx-by-hrithik-roshan-men-black-raglan-sleeved-active-t-shirt/1411086/buy",
            "https://www.myntra.com/tshirts/us-polo-assn/us-polo-assn-men-black-polo-collar-slim-fit-t-shirt/19182894/buy",
            "https://www.myntra.com/tshirts/louis-philippe/louis-philippe-men-black-solid-polo-collar-pure-cotton-t-shirt/18218732/buy",
            "https://www.myntra.com/tshirts/roadster/roadster-men-black-solid-round-neck-t-shirt/2475892/buy",
            "https://www.myntra.com/tshirts/chimpaaanzee/chimpaaanzee-men-grey-v-neck-loose-t-shirt/22120192/buy",
            "https://www.myntra.com/tshirts/tommy-hilfiger/tommy-hilfiger-men-navy-blue-brand-logo-printed-pure-cotton-slim-fit-t-shirt/18820054/buy",
            "https://www.myntra.com/tshirts/roadster/roadster-polo-collar-t-shirt/21742194/buy",
            "https://www.myntra.com/tshirts/louis-philippe-jeans/louis-philippe-jeans-men-black-graphic-printed-pure-cotton-slim-fit-casual-t-shirt/16878774/buy",
            "https://www.myntra.com/tshirts/herenow/herenow-men-black-printed-round-neck-t-shirt/12816442/buy",
            "https://www.myntra.com/tshirts/roadster/roadster-men-white-henley-neck-t-shirt/17329004/buy",
        ],
    },
    "men-sunglasses": {
        "html_file_path": PROJECT_ROOT
        + "/tests/test_data/page_url_html/men-sunglasses.html",
        "page_url": "https://www.myntra.com/men-sunglasses",
        "urls": [
            "https://www.myntra.com/sunglasses/aligatorr/aligatorr-unisex-black-lens--black-uv-protected-rectangle-sunglasses-agrcandy-260/16768312/buy",
            "https://www.myntra.com/sunglasses/voyage/voyage-unisex-square-sunglasses-58157mg2970/10748540/buy",
            "https://www.myntra.com/sunglasses/resist-eyewear/resist-eyewear-unisex-black-lens--black-wayfarer-sunglasses-with-polarised-and-uv-protected-lens/19631016/buy",
            "https://www.myntra.com/sunglasses/criba/criba-unisex-black-lens--black-rectangle-sunglasses-with-uv-protected-lens-crcandy-260/16566206/buy",
            "https://www.myntra.com/sunglasses/roadster/the-roadster-lifestyle-co-unisex-square-sunglasses-mfb-pn-ps-t9578/9038275/buy",
            "https://www.myntra.com/sunglasses/ray-ban/ray-ban-other-sunglasses-with-polarised-lens-8056597630009/21744854/buy",
            "https://www.myntra.com/sunglasses/voyage/voyage-unisex-black-lens--black-wayfarer-sunglasses-with-uv-protected-lens/17838020/buy",
            "https://www.myntra.com/sunglasses/criba/criba-unisex-black-lens--white-wayfarer-sunglasses-with-uv-protected-lens/17708048/buy",
            "https://www.myntra.com/sunglasses/hrx-by-hrithik-roshan/hrx-by-hrithik-roshan-men-square-sunglasses-mfb-pn-cy-80249/2311896/buy",
            "https://www.myntra.com/sunglasses/vincent-chase/vincent-chase-unisex-grey-lens--black-round-sunglasses-with-polarised-lens/18784828/buy",
            "https://www.myntra.com/sunglasses/hm/hm-gold-toned-frame-round-sunglasses/17784356/buy",
            "https://www.myntra.com/sunglasses/voyage/voyage-unisex-black-lens--black-wayfarer-sunglasses-with-uv-protected-lens/18809060/buy",
            "https://www.myntra.com/sunglasses/ray-ban/ray-ban-other-sunglasses-with-uv-protected-lens-8056597641821/21744878/buy",
            "https://www.myntra.com/sunglasses/criba/criba-unisex-clear-lens--white-rectangle-sunglasses-with-uv-protected-lens-crtrsqrbc/19266006/buy",
            "https://www.myntra.com/sunglasses/hrx-by-hrithik-roshan/hrx-by-hrithik-roshan-unisex-polarised-square-sunglasses-mfb-pn-cy-51922/9038471/buy",
            "https://www.myntra.com/sunglasses/voyage/voyage-unisex-black-lens--black-wayfarer-sunglasses-with-uv-protected-lens/19037770/buy",
            "https://www.myntra.com/sunglasses/resist-eyewear/resist-eyewear-unisex-black-lens-wayfarer-sunglasses-uv-protected-lens-mark-black-black-/19417338/buy",
            "https://www.myntra.com/sunglasses/roadster/the-roadster-lifestyle-co-unisex-oval-sunglasses-mfb-pn-ps-t9941/9038509/buy",
            "https://www.myntra.com/sunglasses/oceanides/oceanides-wayfarer-sunglasses-with-polarised-and-uv-protected-lens-alteablue-blanco-verde/21907334/buy",
            "https://www.myntra.com/sunglasses/voyage/voyage-unisex-black-lens--white-wayfarer-sunglasses-with-uv-protected-lens/17838038/buy",
            "https://www.myntra.com/sunglasses/hrx-by-hrithik-roshan/hrx-by-hrithik-roshan-men-aviator-sunglasses-mfb-pn-cy-59946/2311888/buy",
            "https://www.myntra.com/sunglasses/vincent-chase/vincent-chase-unisex-grey-lens--gunmetal-toned-other-sunglasses-with-uv-protected-lens/19062122/buy",
            "https://www.myntra.com/sunglasses/carlton-london/carlton-london-unisex-polarised-square-sunglasses-r86015/13575906/buy",
            "https://www.myntra.com/sunglasses/voyage/voyage-unisex-black-lens-aviator-sunglasses-with-uv-protected-lens-2038mg3051c/14582818/buy",
            "https://www.myntra.com/sunglasses/oceanides/oceanides-round-sunglasses-with-polarised-and-uv-protected-lens-plutocyrstal/21907338/buy",
            "https://www.myntra.com/sunglasses/hrx-by-hrithik-roshan/hrx-by-hrithik-roshan-men-square-sunglasses-mfb-pn-cy-80249/2311895/buy",
            "https://www.myntra.com/sunglasses/mast--harbour/mast--harbour-unisex-mirrored-wayfarer-sunglasses-mfb-pn-aep128y-9/8431315/buy",
            "https://www.myntra.com/sunglasses/voyage/voyage-unisex-black-square-sunglasses/15166448/buy",
            "https://www.myntra.com/sunglasses/vincent-chase/vincent-chase-unisex-green-lens-aviator-sunglasses-with-polarised-and-uv-protected-lens/19062498/buy",
            "https://www.myntra.com/sunglasses/hrx-by-hrithik-roshan/hrx-by-hrithik-roshan-unisex-polarised-square-sunglasses-mfb-pn-cy-50537/9038251/buy",
            "https://www.myntra.com/sunglasses/ray-ban/ray-ban-lens--square-sunglasses-full-rim-with-uv-protected-lens-8056597625517/21745000/buy",
            "https://www.myntra.com/sunglasses/voyage/voyage-unisex-square-sunglasses-2036mg2977/10748602/buy",
            "https://www.myntra.com/sunglasses/tommy-hilfiger/tommy-hilfiger-grey-lens--black-wayfarer-sunglasses-with-uv-protected-lens-th-joe-c1-52-s/18072136/buy",
            "https://www.myntra.com/sunglasses/hrx-by-hrithik-roshan/hrx-by-hrithik-roshan-unisex-square-sunglasses-mfb-pn-cy-51834/8366671/buy",
            "https://www.myntra.com/sunglasses/intellilens/intellilens-unisex-black-lens--black-square-sunglasses-with-polarised-lens/20241130/buy",
            "https://www.myntra.com/sunglasses/voyage/voyage-unisex-square-sunglasses-8926mg2779/10392589/buy",
            "https://www.myntra.com/sunglasses/ray-ban/ray-ban-lens--gold-toned-aviator-sunglasses-with-polarised-lens-8056597662338/21742130/buy",
            "https://www.myntra.com/sunglasses/ted-smith/ted-smith-unisex-grey-lens--gold-toned-aviator-sunglasses-with-uv-protected-lens/19753006/buy",
            "https://www.myntra.com/sunglasses/fastrack/fastrack-men-wayfarer-sunglasses-nbp357bk1/7822969/buy",
            "https://www.myntra.com/sunglasses/hrx-by-hrithik-roshan/hrx-by-hrithik-roshan-men-aviator-sunglasses/2311891/buy",
            "https://www.myntra.com/sunglasses/voyage/voyage-unisex-black-lens--black-square-sunglasses-with-uv-protected-lens/16712998/buy",
            "https://www.myntra.com/sunglasses/carlton-london/carlton-london-unisex-uv-protected-lens-rectangle-sunglasses/15162836/buy",
            "https://www.myntra.com/sunglasses/ray-ban/ray-ban-aviator-sunglasses-with-polarised-lens-8056597662277/21742154/buy",
            "https://www.myntra.com/sunglasses/intellilens/intellilens-unisex-black-lens--black-sports-sunglasses-with-polarised-lens/20241102/buy",
            "https://www.myntra.com/sunglasses/voyage/voyage-unisex-uv-protected-cateye-sunglasses-b6101mg3174/11456944/buy",
            "https://www.myntra.com/sunglasses/mast--harbour/mast--harbour-unisex-aviator-sunglasses-mfb-pn-ps-dsa1549/5598571/buy",
            "https://www.myntra.com/sunglasses/royal-son/royal-son-unisex-uv-protected-lens-square-sunglasses-rs0038av/11818054/buy",
            "https://www.myntra.com/sunglasses/hrx-by-hrithik-roshan/hrx-by-hrithik-roshan-unisex-square-sunglasses-mfb-pn-cy-82051/8366705/buy",
            "https://www.myntra.com/sunglasses/ray-ban/ray-ban-square-sunglasses-with-uv-protected-lens/21750878/buy",
            "https://www.myntra.com/sunglasses/voyage/voyage-unisex-grey-lens--gunmetal-toned-rectangle-sunglasses-bt192321mg3312-grey/14013070/buy",
        ],
    },
    "men-jackets": {
        "html_file_path": PROJECT_ROOT
        + "/tests/test_data/page_url_html/men-jackets.html",
        "page_url": "https://www.myntra.com/men-jackets",
        "urls": [
            "https://www.myntra.com/jackets/high-star/high-star-men-black-solid-denim-jacket/11275832/buy",
            "https://www.myntra.com/jackets/roadster/roadster-men-red-solid-bomber/4929150/buy",
            "https://www.myntra.com/jackets/hm/hm-men-water-repellent-puffer-jacket/20422978/buy",
            "https://www.myntra.com/jackets/levis/levis-men-blue-solid-denim-jacket/18973556/buy",
            "https://www.myntra.com/jackets/hrx-by-hrithik-roshan/hrx-by-hrithik-roshan-men-olive-green-solid-active-bomber-jacket/4453297/buy",
            "https://www.myntra.com/jackets/powerlook/powerlook-solid-hooded-long-sleeves-sporty-jacket/22040836/buy",
            "https://www.myntra.com/jackets/locomotive/locomotive-men-black-solid-denim-jacket/10936542/buy",
            "https://www.myntra.com/jackets/levis/levis-men-navy-blue-striped-quilted-jacket/18973506/buy",
            "https://www.myntra.com/jackets/roadster/roadster-men-blue-washed-denim-jacket/12288656/buy",
            "https://www.myntra.com/jackets/hrx-by-hrithik-roshan/hrx-by-hrithik-roshan-men-black-solid-active-bomber-jacket/4453295/buy",
            "https://www.myntra.com/jackets/highlander/highlander-men-olive-green-capulet-denim-jacket/16031126/buy",
            "https://www.myntra.com/jackets/technosport/technosport-lightweight-antimicrobial-training-or-gym-sporty-jacket/22167314/buy",
            "https://www.myntra.com/jackets/levis/levis-men-blue-solid-denim-jacket/16803488/buy",
            "https://www.myntra.com/jackets/hrx-by-hrithik-roshan/hrx-by-hrithik-roshan-men-navy-blue-solid-sporty-jacket/4923946/buy",
            "https://www.myntra.com/jackets/highlander/highlander-men-black-solid-denim-jacket/10904232/buy",
            "https://www.myntra.com/jackets/nike/nike-men-black-solid-classic-fz-ft-outdoor-pure-cotton-hooded-bomber-jacket/18962822/buy",
            "https://www.myntra.com/jackets/roadster/roadster-men-navy-blue-washed-denim-jacket/12288724/buy",
            "https://www.myntra.com/jackets/powerlook/powerlook-men-cotton-bomber-jacket/21719844/buy",
            "https://www.myntra.com/jackets/hrx-by-hrithik-roshan/hrx-by-hrithik-roshan-men-white-solid-sporty-jacket/4881810/buy",
            "https://www.myntra.com/jackets/highlander/highlander-men-blue-solid-denim-jacket/10846576/buy",
            "https://www.myntra.com/jackets/gant/gant-men-black-water-resistant-quilted-jacket/20739686/buy",
            "https://www.myntra.com/jackets/powerlook/powerlook-men-organic-cotton-varsity-jacket/21659222/buy",
            "https://www.myntra.com/jackets/allen-solly-sport/allen-solly-sport-men-black-solid-bomber-jacket/10656390/buy",
            "https://www.myntra.com/jackets/technosport/technosport-lightweight-antimicrobial-training-or-gym-sporty-jacket/22167318/buy",
            "https://www.myntra.com/jackets/roadster/roadster-men-blue-solid-denim-jacket/12288602/buy",
            "https://www.myntra.com/jackets/highlander/highlander-men-grey-washed-denim-jacket/10460330/buy",
            "https://www.myntra.com/jackets/allen-solly-sport/allen-solly-sport-men-navy-blue-bomber-jacket/20479030/buy",
            "https://www.myntra.com/jackets/nike/nike-men-grey-melange-solid-classic-fz-ft-outdoor-hooded-pure-cotton-bomber-jacket/13010714/buy",
            "https://www.myntra.com/jackets/roadster/roadster-men-navy-blue-washed-denim-jacket/12288786/buy",
            "https://www.myntra.com/jackets/powerlook/powerlook-washed-spread-collar-long-sleeves-denim-jacket/22040834/buy",
            "https://www.myntra.com/jackets/highlander/highlander-men-black-solid-leather-jacket/10721006/buy",
            "https://www.myntra.com/jackets/hrx-by-hrithik-roshan/hrx-by-hrithik-roshan-men-black-training-rapid-dry-solid-sporty-jacket/9445565/buy",
            "https://www.myntra.com/jackets/roadster/roadster-men-black-washed-hooded-denim-jacket/12288642/buy",
            "https://www.myntra.com/jackets/nike/nike-men-black-solid-sporty-jacket/13252030/buy",
            "https://www.myntra.com/jackets/highlander/highlander-men-white-solid-denim-jacket/10874696/buy",
            "https://www.myntra.com/jackets/technosport/technosport-lightweight-antimicrobial-training-or-gym-sporty-jacket/22167316/buy",
            "https://www.myntra.com/jackets/hrx-by-hrithik-roshan/hrx-by-hrithik-roshan-men-black--grey-camouflage-printed-running-bomber-jacket/4453300/buy",
            "https://www.myntra.com/jackets/roadster/roadster-men-blue-solid-denim-bomber-jacket/12288668/buy",
            "https://www.myntra.com/jackets/adidas/adidas-men-navy-blue-zne-solid-hooded-sporty-jacket/19187014/buy",
            "https://www.myntra.com/jackets/levis/levis-men-blue-solid-denim-jacket/16803346/buy",
            "https://www.myntra.com/jackets/high-star/high-star-men-black-solid-denim-jacket/8081687/buy",
            "https://www.myntra.com/jackets/american-eagle-outfitters/american-eagle-outfitters-men-hooded-padded-jacket--/22163580/buy",
            "https://www.myntra.com/jackets/highlander/highlander-men-grey-washed-denim-jacket/10460306/buy",
            "https://www.myntra.com/jackets/roadster/roadster-men-black-solid-tailored-jacket/6411326/buy",
            "https://www.myntra.com/jackets/nike/nike-men-nike-therma-fit-repel-jacket/20073230/buy",
            "https://www.myntra.com/jackets/puma/puma-men-black-slim-fit-zippered-sporty-jacket/18981588/buy",
            "https://www.myntra.com/jackets/highlander/highlander-men-navy-blue-denim-jacket/16481004/buy",
            "https://www.myntra.com/jackets/roadster/roadster-men-grey-solid-tailored-jacket/6411433/buy",
            "https://www.myntra.com/jackets/reebok/reebok-men-navy-blue-solid-training-sporty-jacket/17209372/buy",
            "https://www.myntra.com/jackets/levis/levis-men-coffee-brown-solid-corduroy-padded-jacket/18973602/buy",
        ],
    },
}


TEST_PRODUCT_DETAILS = {
    "7546900": {
        "html_file_path": PROJECT_ROOT
        + "/tests/test_data/product_details_html/product_7546900.html",
        "product_category": "Tshirts",
        "product_description": "HERENOW Men Navy Polo Collar Cotton Pure Cotton "
        "T-shirt",
        "product_id": "7546900",
        "product_image_urls": "https://assets.myntassets.com/h_720,q_90,w_540/v1/assets/images/7546900/2019/1/24/c9be0d6e-30a4-4242-b4e0-1c166b73f2781548320874402-HERENOW-Men-Polo-Collar-T-shirt-4861548320873235-1.jpg, "
        "https://assets.myntassets.com/h_720,q_90,w_540/v1/assets/images/7546900/2019/1/24/e4fa716f-3181-4c3b-8f35-0d30fc5ff45d1548320874385-HERENOW-Men-Polo-Collar-T-shirt-4861548320873235-2.jpg, "
        "https://assets.myntassets.com/h_720,q_90,w_540/v1/assets/images/7546900/2019/1/24/4ff84b3f-96cc-4e3c-84e2-b6d5d13e06451548320874372-HERENOW-Men-Polo-Collar-T-shirt-4861548320873235-3.jpg, "
        "https://assets.myntassets.com/h_720,q_90,w_540/v1/assets/images/7546900/2019/1/24/e8fca578-9400-4658-8a80-a932e52d4b151548320874353-HERENOW-Men-Polo-Collar-T-shirt-4861548320873235-4.jpg, "
        "https://assets.myntassets.com/h_720,q_90,w_540/v1/assets/images/7546900/2019/1/24/271f9b96-3b40-4330-8ce2-b093af796ac11548320874341-HERENOW-Men-Polo-Collar-T-shirt-4861548320873235-5.jpg",
        "product_metadata": [
            {
                "Complete The Look": "When you need some new basic tees "
                "to allow your statement pieces to "
                "shine, go with this one from "
                "HERE&NOW.",
                "Fit": "Regular Fit",
                "Length": "Regular",
                "Main Trend": "New Basics",
                "Material & Care": "100% cotton",
                "Multipack Set": "Single",
                "Neck": "Polo Collar",
                "Occasion": "Casual",
                "Pattern": "Solid",
                "Print or Pattern Type": "Solid",
                "Product Details": "Navy blue solid T-shirt, has a polo "
                "collar, short sleeves",
                "Size & Fit": "The model (height 6') is wearing a size " "M",
                "Sleeve Length": "Short Sleeves",
                "Sleeve Styling": "Regular Sleeves",
                "Specifications": "Machine-wash",
                "Sustainable": "Regular",
                "Wash Care": "Machine Wash",
                "Weave Type": "Knitted",
            }
        ],
        "product_name": "HERE&NOW",
        "product_num_reviews": "9.4k",
        "product_page_url": "https://www.myntra.com/tshirts/herenow/herenow-men-navy-polo-collar-cotton-pure-cotton-t-shirt/7546900/buy",
        "product_price_after_discount": 376.0,
        "product_rating": 4.1,
    },
    "12222036": {
        "html_file_path": PROJECT_ROOT
        + "/tests/test_data/product_details_html/product_12222036.html",
        "product_category": "Tops",
        "product_description": "Black High Neck Cropped Top",
        "product_id": "12222036",
        "product_image_urls": "https://assets.myntassets.com/h_720,q_90,w_540/v1/assets/images/12222036/2020/10/6/d7ae3065-98d4-42d0-b244-d2b18802ff101601959656577-SASSAFRAS-Women-Black-Solid-High-Neck-Cropped-Top-4441601959-1.jpg, "
        "https://assets.myntassets.com/h_720,q_90,w_540/v1/assets/images/12222036/2020/10/6/5779fc09-4088-48a9-9e0e-2d1d6a3572da1601959656523-SASSAFRAS-Women-Black-Solid-High-Neck-Cropped-Top-4441601959-2.jpg, "
        "https://assets.myntassets.com/h_720,q_90,w_540/v1/assets/images/12222036/2020/10/6/7e3f0bf1-2517-4c35-b3e2-d806322972461601959656454-SASSAFRAS-Women-Black-Solid-High-Neck-Cropped-Top-4441601959-3.jpg, "
        "https://assets.myntassets.com/h_720,q_90,w_540/v1/assets/images/12222036/2020/10/6/4e6fc0b7-c8c6-4ede-9fb2-c1120983a44b1601959656406-SASSAFRAS-Women-Black-Solid-High-Neck-Cropped-Top-4441601959-4.jpg, "
        "https://assets.myntassets.com/h_720,q_90,w_540/v1/assets/images/12222036/2020/10/6/228e1a91-b15b-47d8-b96a-cf596ec4294c1601959656342-SASSAFRAS-Women-Black-Solid-High-Neck-Cropped-Top-4441601959-5.jpg, "
        "https://assets.myntassets.com/h_720,q_90,w_540/v1/assets/images/12222036/2022/3/9/9c1a79c1-e827-4a0c-8b9e-7016734dbf0f1646807736596-SASSAFRAS-Black-High-Neck-Cropped-Top-2561646807736482-6.jpg",
        "product_metadata": [
            {
                "Complete The Look": "This in-season top from SASSAFRAS "
                "ensures comfort and "
                "sophistication all at once.  This "
                "black piece is perfect for "
                "hanging out with friends when you "
                "put it with a fabulous dark denim "
                "jean and your favourite pair of "
                "shoes.",
                "Length": "Crop",
                "Main Trend": "New Basics",
                "Material & Care": "Material: 96% cotton, 4% Lycra",
                "Neck": "High Neck",
                "Occasion": "Casual",
                "Print or Pattern Type": "Solid",
                "Product Details": "Black solid knitted crop top, has a "
                "high neck, and long sleeves",
                "Size & Fit": "The model (height 5'8\") is wearing a " "size S",
                "Sleeve Length": "Long Sleeves",
                "Sleeve Styling": "Regular Sleeves",
                "Specifications": "Machine Wash",
                "Transparency": "Opaque",
                "Type": "Regular",
                "Weave Type": "Knitted",
            }
        ],
        "product_name": "SASSAFRAS",
        "product_num_reviews": "26.2k",
        "product_page_url": "https://www.myntra.com/tops/sassafras/sassafras-black-high-neck-cropped-top/12222036/buy",
        "product_price_after_discount": 419.0,
        "product_rating": 4.5,
    },
    "20276770": {
        "html_file_path": PROJECT_ROOT
        + "/tests/test_data/product_details_html/product_20276770.html",
        "product_category": "Suits",
        "product_description": "Men Black Solid Single-Breasted Slim-Fit 2-Piece "
        "Formal Suit",
        "product_id": "20276770",
        "product_image_urls": "https://assets.myntassets.com/h_720,q_90,w_540/v1/assets/images/20276770/2022/10/6/84b1fff8-1417-4046-817f-4b48940236811665039013460MenBlackTwoPieceSuit1.jpg, "
        "https://assets.myntassets.com/h_720,q_90,w_540/v1/assets/images/20276770/2022/10/6/c83e978a-ed6e-4fb5-af83-c5dae69643f81665039013426MenBlackTwoPieceSuit2.jpg, "
        "https://assets.myntassets.com/h_720,q_90,w_540/v1/assets/images/20276770/2022/10/6/86cf8d62-c398-446c-8792-3fd7b08bd6ef1665039013437MenBlackTwoPieceSuit3.jpg, "
        "https://assets.myntassets.com/h_720,q_90,w_540/v1/assets/images/20276770/2022/10/6/aaf7cd9d-fc28-4df3-bba8-7411793cdaf91665039013449MenBlackTwoPieceSuit4.jpg, "
        "https://assets.myntassets.com/h_720,q_90,w_540/v1/assets/images/20276770/2022/10/6/84c6a271-dfbe-40c0-b386-2595c89a9a621665039013484MenBlackTwoPieceSuit5.jpg, "
        "https://assets.myntassets.com/h_720,q_90,w_540/v1/assets/images/20276770/2022/10/6/1d2e7024-b250-4e42-a0d4-8bac36cc9a581665039013472MenBlackTwoPieceSuit6.jpg",
        "product_metadata": [
            {
                "Bottom Closure": "Zip",
                "Collar": "Notched Lapel",
                "Fabric": "Polyester",
                "Fit": "Slim Fit",
                "Front Styling": "Single-Breasted",
                "Material & Care": "Black solid slim-fit formal "
                "trousers, has a waistband with belt "
                "loops, zip fly with a button "
                "closure",
                "Occasion": "Formal",
                "Pattern": "Solid",
                "Product Details": "Black solid slim-fit formal 2-piece " "suit",
                "Size & Fit": "Black solid slim-fit formal blazer, has "
                "a notched lapel collar, single-breasted "
                "with Single button closures, long "
                "sleeves, two pockets, one chest welt "
                "pocket, an attached lining and a double "
                "vented back hem",
                "Sleeve Length": "Long Sleeves",
                "Specifications": "Slim-Fit",
                "Type": "Blazer and Trousers",
            }
        ],
        "product_name": "Peter England Elite",
        "product_num_reviews": 39.0,
        "product_page_url": "https://www.myntra.com/suits/peter-england-elite/peter-england-elite-men-black-solid-single-breasted-slim-fit-2-piece-formal-suit/20276770/buy",
        "product_price_after_discount": "Rs. 8999",
        "product_rating": 3.7,
    },
}
