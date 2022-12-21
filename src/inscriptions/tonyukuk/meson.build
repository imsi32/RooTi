pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
tonyukukdir = join_paths(pkgdatadir, 'rooti/inscriptions/tonyukuk')

sources = [
  '__init__.py',
  'tonyukuk_page.py',
  'slide_first_stone_west.py',
  'slide_first_stone_south.py',
]

install_data(sources, install_dir: tonyukukdir)
