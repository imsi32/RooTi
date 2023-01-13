pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
koltigindir = join_paths(pkgdatadir, 'rooti/inscriptions/koltigin')

sources = [
  '__init__.py',
  'koltigin_page.py',
  'koltigin_slide_south.py',
  'koltigin_slide_southeast.py',
  'koltigin_slide_east.py',
  'koltigin_slide_northeast.py',
  'koltigin_slide_north.py',
  'koltigin_slide_west.py',
  'koltigin_slide_southwest.py',
]

install_data(sources, install_dir: koltigindir)
