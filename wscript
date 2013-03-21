VERSION="0.1.2"
TTF_VERSION="0.1"
APPNAME='mittaphap'
LICENSE='OFL.txt'
COPYRIGHT="Copyright SIL International, 2012"

for f in ['Regular', 'Book', 'Bold', 'Book-Bold'] :
	p = 'src/Mittaphap-' + f
	fnt = font(target = 'Mittaphap-' + f + '.ttf',
				source = p + '.sfd',
				license = ofl('Mittaphap'),
				version = TTF_VERSION,
				opentype = internal(),
				graphite = gdl(p[4:] + '.gdl',
								master = 'src/mittaphap.gdl',
								params = '-w3521'),
				ap = p + '.xml',
				script = 'lao '
			)
