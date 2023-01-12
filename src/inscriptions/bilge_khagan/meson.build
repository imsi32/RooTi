pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
bilgekhagandir = join_paths(pkgdatadir, 'rooti/inscriptions/bilge_khagan')

sources = [
  '__init__.py',
  'bilge_khagan_page.py',
  'bilge_khagan_slide_south.py',
  'bilge_khagan_slide_southeast.py',
  'bilge_khagan_slide_east.py',
  'bilge_khagan_slide_northeast.py',
  'bilge_khagan_slide_north.py',
  'bilge_khagan_slide_west.py',
  'bilge_khagan_slide_southwest.py',
]

install_data(sources, install_dir: bilgekhagandir)
