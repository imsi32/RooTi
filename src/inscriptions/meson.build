pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
inscriptionsdir = join_paths(pkgdatadir, 'rooti/inscriptions')

subdir('bilge_khagan')
subdir('koltigin')
subdir('tonyukuk')

sources = [
  '__init__.py',
]

install_data(sources, install_dir: inscriptionsdir)
